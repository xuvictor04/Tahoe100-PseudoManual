#!/usr/bin/env python3
"""
run_smoke.py - smoke-test every script of this repo against the synthetic Tahoe-100M data.

    python tests/run_smoke.py [--workdir DIR] [--regen] [--only small,mtap,atlas,panel] [--workers 2]

1. Generates the synthetic download once into DIR/synthetic_tahoe (tests/make_synthetic_tahoe.py, ~1-2 min), and
   reuses it on later runs (regenerated automatically when the generator changed; --regen forces it).
2. Runs each script as a subprocess with this Python, from a scratch folder, writing into DIR:
     small  01_preview_parquet.py, 02_find_mtap_gankyrin.py, old_drug_effect_uncorrected.py   -> DIR/small
     mtap   tahoe_mtap_gankyrin.py all + coreg                                                 -> DIR/mtap_gankyrin
     atlas  tahoe_atlas.py check, compute, lookup x4, agents --dry-run, bundle                 -> DIR/atlas
     panel  tahoe_gene_panel.py extract + analyze (skipped while that script does not exist)   -> DIR/gene_panel
   Each stage starts from an empty output folder.
3. Checks the outputs against the planted ground truth (DIR/synthetic_tahoe/ground_truth.json): one PASS/FAIL line
   per check (WARN = known weakness whose outcome depends on chance in these small data; it does not fail the run),
   a JSON summary in DIR/smoke_results.json, logs of every command in DIR/logs/. Exit code 1 on any FAIL.

DIR defaults to $TAHOE_SMOKE_DIR, else <system temp folder>/tahoe_smoke. No API key is used: the agents step runs
with --dry-run and the API-key variables are removed from the environment of every command.
To add a stage: write one function decorated with @stage("name") (see stage_panel at the end).
"""

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import zipfile
from collections import OrderedDict

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
GENERATOR = os.path.join(HERE, "make_synthetic_tahoe.py")
PY = sys.executable
SECRET_ENV = ["ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK",
              "CLAUDE_CODE_USE_VERTEX"]
ATLAS_ANGLES = ["quality", "drugs", "genes", "classes", "cell_lines", "biomarkers", "line_response", "programs",
                "cell_state"]
TIMEOUT = 45 * 60

STAGES = OrderedDict()


def stage(name):
    """Register a stage: a function taking the Ctx. Stages run in registration order."""
    def deco(fn):
        STAGES[name] = fn
        return fn
    return deco


# ============================================================================= context: commands and checks
class Ctx:
    def __init__(self, args):
        self.args = args
        self.W = os.path.abspath(args.workdir)
        self.D = os.path.join(self.W, "synthetic_tahoe")
        self.logs = os.path.join(self.W, "logs")
        self.scratch = os.path.join(self.W, "scratch")
        for d in (self.W, self.logs, self.scratch):
            os.makedirs(d, exist_ok=True)
        self.workers = args.workers
        self.results = []          # {stage, check, status, detail}
        self.commands = []         # {stage, name, argv, cwd, rc, seconds, log}
        self.stage = ""
        self.gt = None
        self.env = {k: v for k, v in os.environ.items() if k not in SECRET_ENV}
        self.env["PYTHONIOENCODING"] = "utf-8"
        self.env["PYTHONDONTWRITEBYTECODE"] = "1"

    # ---- commands
    def run(self, name, argv, cwd=None, timeout=TIMEOUT):
        """Run one command; output goes to logs/<stage>_<name>.log. Returns (returncode, stdout+stderr text)."""
        cwd = cwd or self.scratch
        os.makedirs(cwd, exist_ok=True)
        logf = os.path.join(self.logs, f"{self.stage}_{name}.log")
        t0 = time.time()
        print(f"  $ {' '.join(argv[1:])}   (cwd {cwd})", flush=True)
        with open(logf, "w", encoding="utf-8") as fh:
            try:
                p = subprocess.run(argv, cwd=cwd, env=self.env, stdout=fh, stderr=subprocess.STDOUT,
                                   timeout=timeout)
                rc = p.returncode
            except subprocess.TimeoutExpired:
                rc = "timeout"
                fh.write(f"\n[run_smoke] TIMEOUT after {timeout} s\n")
        dt = time.time() - t0
        with open(logf, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        self.commands.append({"stage": self.stage, "name": name, "argv": argv, "cwd": cwd, "rc": rc,
                              "seconds": round(dt, 1), "log": logf})
        print(f"    -> exit {rc} in {dt:.0f} s (log: {logf})", flush=True)
        return rc, text

    def run_ok(self, name, argv, cwd=None, expect_files=(), timeout=TIMEOUT):
        """Run and check exit code 0 + expected output files. Returns the output text (or None on failure)."""
        rc, text = self.run(name, argv, cwd, timeout)
        if rc != 0:
            self.record(f"{name}: exit code", False, f"exit {rc}; last lines: {tail(text)}")
            return None
        missing = [f for f in expect_files if not os.path.exists(f)]
        self.record(f"{name}: runs", not missing, "exit 0" + (f"; missing {missing}" if missing else ""))
        return text

    # ---- checks
    def record(self, check, ok, detail="", status=None):
        status = status or ("PASS" if ok else "FAIL")
        self.results.append({"stage": self.stage, "check": check, "status": status, "detail": str(detail)})
        print(f"  [{status}] {check}" + (f" - {detail}" if detail else ""), flush=True)

    def check(self, name, fn):
        """fn() -> (ok, detail). Exceptions (missing file, column) count as FAIL."""
        try:
            ok, detail = fn()
        except Exception as e:  # noqa: BLE001
            ok, detail = False, f"{type(e).__name__}: {e}"
        self.record(name, ok, detail)
        return ok

    def skip(self, check, reason):
        self.record(check, True, reason, status="SKIP")


def tail(text, n=6):
    lines = [x for x in text.strip().splitlines() if x.strip()]
    return " | ".join(lines[-n:])[-1500:]


def top_k(series, k):
    return list(series.head(k))


def fmt_top(df, cols, k=5):
    return "; ".join(" ".join(str(r[c]) for c in cols) for _, r in df.head(k).iterrows())


# ============================================================================= data
def source_hash():
    sys.path.insert(0, HERE)
    try:
        import make_synthetic_tahoe as M
        return M.source_hash()
    finally:
        sys.path.remove(HERE)


def ensure_data(ctx):
    gt_path = os.path.join(ctx.D, "ground_truth.json")
    want = source_hash()
    have, seed = None, None
    if os.path.exists(gt_path):
        with open(gt_path) as fh:
            g = json.load(fh)
        have, seed = g.get("generator_sha1"), g.get("params", {}).get("seed")
    ctx.stage = "data"
    if ctx.args.regen or have != want or seed != ctx.args.seed:
        why = "--regen" if ctx.args.regen else ("no data yet" if have is None else
                                                 "generator changed" if have != want else "other --seed")
        print(f"Generating synthetic data into {ctx.D} ({why}) ...", flush=True)
        if os.path.exists(ctx.D):
            shutil.rmtree(ctx.D)
        rc, text = ctx.run("generate", [PY, GENERATOR, ctx.D, "--seed", str(ctx.args.seed)], cwd=ctx.scratch)
        ctx.record("generate synthetic data", rc == 0 and os.path.exists(gt_path),
                   f"exit {rc}" + ("" if rc == 0 else f": {tail(text)}"))
        if rc != 0:
            return False
    else:
        print(f"Reusing synthetic data in {ctx.D}", flush=True)
    with open(gt_path) as fh:
        ctx.gt = json.load(fh)
    return True


def fresh(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)
    return path


# ============================================================================= stage: small scripts
@stage("small")
def stage_small(ctx):
    out = fresh(os.path.join(ctx.W, "small"))
    ctx.run_ok("01_preview", [PY, os.path.join(REPO, "01_preview_parquet.py"), ctx.D], cwd=out,
               expect_files=[os.path.join(out, "tahoe_preview.txt"), os.path.join(out, "tahoe_preview.csv")])
    ms = os.path.join(out, "mtap_search")
    txt = ctx.run_ok("02_find", [PY, os.path.join(REPO, "02_find_mtap_gankyrin.py"), ctx.D], cwd=out,
                     expect_files=[os.path.join(ms, "search_summary.txt"),
                                   os.path.join(ms, "pseudobulk_MTAP_PSMD10_raw.csv")])
    if txt is not None:
        def raw_has_both():
            t = pd.read_csv(os.path.join(ms, "pseudobulk_MTAP_PSMD10_raw.csv"))
            n = t["gene_name"].value_counts().to_dict()
            return {"MTAP", "PSMD10"} <= set(n), f"rows per gene {n}"
        ctx.check("02_find: raw DE tests for MTAP and PSMD10", raw_has_both)
        ctx.check("02_find: gene metadata hits found",
                  lambda: (bool(glob.glob(os.path.join(ms, "*gene_metadata*_hits.csv"))),
                           ", ".join(os.path.basename(f) for f in glob.glob(os.path.join(ms, "*_hits.csv")))))
    # old_drug_effect_uncorrected.py has no data argument: it globs **/*.parquet from its cwd, so it runs inside
    # the data folder and writes to an absolute output folder outside it.
    old = os.path.join(out, "mtap_old")
    txt = ctx.run_ok("old_drug_effect", [PY, os.path.join(REPO, "old_drug_effect_uncorrected.py"), "MTAP", old],
                     cwd=ctx.D, expect_files=[os.path.join(old, f"MTAP_{s}.csv")
                                              for s in ("DE_all_tests", "by_drug_and_dose", "top_drugs")])
    if txt is not None:
        def h1_inflated():
            # uncorrected: drugs that sat in H1 look like MTAP inducers (the artifact the corrected scripts remove)
            t = pd.read_csv(os.path.join(old, "MTAP_by_drug_and_dose.csv"))
            lay = pd.DataFrame(ctx.gt["layout"])
            h1 = lay[(lay["well"] == "H1")][["drug", "conc"]]
            m = t.merge(h1, left_on=["drug", "concentration"], right_on=["drug", "conc"])
            other = t[~t.set_index(["drug", "concentration"]).index.isin(list(zip(m["drug"], m["concentration"])))]
            a, b = m["median_lfc"].median(), other["median_lfc"].median()
            return a - b > 0.2, f"median uncorrected MTAP lfc of H1 drug-doses {a:.2f} vs others {b:.2f}"
        ctx.check("old_drug_effect: H1 artifact visible in uncorrected MTAP lfc", h1_inflated)


# ============================================================================= stage: MTAP / Gankyrin
@stage("mtap")
def stage_mtap(ctx):
    gt = ctx.gt
    out = fresh(os.path.join(ctx.W, "mtap_gankyrin"))
    R = os.path.join(out, "results")
    script = os.path.join(REPO, "tahoe_mtap_gankyrin.py")
    txt = ctx.run_ok("all", [PY, script, "all", "--data", ctx.D, "--out", out, "--workers", str(ctx.workers),
                             "--min-cells", "10"],
                     expect_files=[os.path.join(R, f) for f in
                                   ("summary.txt", "well_position_effects.csv", "plate_dmso_offsets.csv",
                                    "baseline_by_cell_line.csv", "MTAP_null_selective_drugs.csv",
                                    "Gankyrin_level_vs_drug_response.csv", "excluded_failed_wells.csv",
                                    "MTAP_drug_effects_by_dose.csv", "Gankyrin_PSMD10_drug_effects_by_dose.csv",
                                    "PROTEASOME_module_drug_effects_by_dose.csv", "cell_cycle_by_cell_line.csv")])
    if txt is not None:
        bad = [x.strip() for x in txt.splitlines() if "WARNING:" in x and " failed:" in x]
        ctx.record("analyze: every analysis ran (no 'WARNING: ... failed')", not bad, "; ".join(bad)[:1500] or
                   "none failed")

        def pos(gene, well):
            t = pd.read_csv(os.path.join(R, "well_position_effects.csv"))
            t = t[t["gene"] == gene].sort_values("z_vs_other_positions", ascending=False)
            top = top_k(t["well"], 3)
            return well in top, f"top {gene} positions: {fmt_top(t, ['well', 'median_effect_plate_corrected'], 3)}"
        ctx.check("well_position_effects: H1 in top-3 MTAP positions", lambda: pos("MTAP", "H1"))
        ctx.check("well_position_effects: D10 in top-3 PSMD10 positions", lambda: pos("PSMD10", "D10"))

        def plate2():
            t = pd.read_csv(os.path.join(R, "plate_dmso_offsets.csv"))
            t = t[t["gene"] == "PSMD10"].sort_values("dmso_offset", ascending=False)
            return t["plate"].iloc[0] == "plate2", f"PSMD10 DMSO offsets: {fmt_top(t, ['plate', 'dmso_offset'], 3)}"
        ctx.check("plate_dmso_offsets: plate2 has the top PSMD10 DMSO offset", plate2)

        def null_lines():
            t = pd.read_csv(os.path.join(R, "baseline_by_cell_line.csv"))
            got = set(t.loc[t["MTAP_null"].astype(str).str.lower() == "true", "cell_line_id"])
            want = set(gt["group_ids"]["mtap_null"])
            return got == want, f"called {sorted(got)}; planted {sorted(want)}"
        ctx.check("baseline: MTAP-null lines == planted", null_lines)

        def pemetrexed():
            t = pd.read_csv(os.path.join(R, "MTAP_null_selective_drugs.csv"))
            return "Pemetrexed" in top_k(t["drug"], 3), f"top: {fmt_top(t, ['drug', 'conc', 'z_selective'], 4)}"
        ctx.check("MTAP_null_selective_drugs: Pemetrexed in top 3", pemetrexed)

        def ixazomib():
            t = pd.read_csv(os.path.join(R, "Gankyrin_level_vs_drug_response.csv"))
            t = t[t["reading"] == "high-Gankyrin lines depleted more"]
            return "Ixazomib" in top_k(t["drug"], 3), f"top: {fmt_top(t, ['drug', 'conc', 'rho', 'z_corrected'], 4)}"
        ctx.check("Gankyrin_level_vs_drug_response: Ixazomib in top 3 'depleted more'", ixazomib)

        def failed():
            t = pd.read_csv(os.path.join(R, "excluded_failed_wells.csv"))
            want = gt["failed_well"]["sample"]
            return want in set(t["sample"]), f"excluded {list(t['sample'])}; planted {want}"
        ctx.check("excluded_failed_wells: the failed well is excluded", failed)

        def sections():
            with open(os.path.join(R, "summary.txt"), encoding="utf-8") as fh:
                lines = fh.read().splitlines()
            missing = [k for k in range(1, 10) if not any(x.startswith(f"{k}. ") for x in lines)]
            return not missing, "missing sections " + str(missing) if missing else "sections 1-9 present"
        ctx.check("summary.txt has sections 1-9", sections)

        def bortezomib_flags():
            t = pd.read_csv(os.path.join(R, "MTAP_drug_effects_by_dose.csv"))
            f = str(t.loc[(t["drug"] == "Bortezomib") & (t["conc"] == 5.0), "flags"].iloc[0])
            return "toxic" in f and "transcription drop" in f, f"Bortezomib 5 uM flags: {f}"
        ctx.check("drug effects: Bortezomib 5 uM flagged toxic + transcription drop", bortezomib_flags)

        def proteasome():
            t = pd.read_csv(os.path.join(R, "PROTEASOME_module_drug_effects_by_dose.csv"))
            t = t.sort_values("z_corrected", ascending=False)
            top = list(zip(t["drug"], t["conc"]))[:3]
            return ("Bortezomib", 5.0) in top, f"top PROTEASOME: {fmt_top(t, ['drug', 'conc', 'fold_change'], 3)}"
        ctx.check("PROTEASOME module: Bortezomib 5 uM in top 3", proteasome)

        def dmso_offset_ignored():
            t = pd.read_csv(os.path.join(R, "Gankyrin_PSMD10_drug_effects_by_dose.csv"))
            t = t[t["plates"].astype(str).str.split(",").map(lambda s: "plate2" in s)]
            u, c = t["log2FC_vs_DMSO_uncorrected"].median(), t["log2FC_corrected"].abs().median()
            return u > 0.15 and c < 0.12, (f"drug-doses on plate2: median uncorrected PSMD10 log2FC {u:.2f}, "
                                           f"median |corrected| {c:.2f}")
        ctx.check("Gankyrin effects: plate2 DMSO offset inflates uncorrected, not corrected", dmso_offset_ignored)

        def psmd10_cycle():
            t = pd.read_csv(os.path.join(R, "cell_cycle_by_cell_line.csv"))
            v = t["PSMD10_log2_top_vs_bottom_G2M_PHASE_quartile"]
            return v.median() > 0.1, f"median log2 G2M-high vs low {v.median():.2f} (planted 1.25x in G2M cells)"
        ctx.check("cell cycle: PSMD10 higher in G2M-high cells", psmd10_cycle)

    txt = ctx.run_ok("coreg", [PY, script, "coreg", "--data", ctx.D, "--out", out],
                     expect_files=[os.path.join(R, f) for f in ("coregulation_summary.txt", "coregulated_with_MTAP.csv",
                                                                 "coregulated_with_Gankyrin_PSMD10.csv")])
    if txt is not None:
        def coreg_rows():
            n = {f: len(pd.read_csv(os.path.join(R, f))) for f in ("coregulated_with_MTAP.csv",
                                                                   "coregulated_with_Gankyrin_PSMD10.csv")}
            return all(v >= 50 for v in n.values()), f"rows {n}"
        ctx.check("coreg: partner tables filled", coreg_rows)


# ============================================================================= stage: atlas
@stage("atlas")
def stage_atlas(ctx):
    gt = ctx.gt
    A = fresh(os.path.join(ctx.W, "atlas"))
    script = os.path.join(REPO, "tahoe_atlas.py")
    base = ["--data", ctx.D, "--out", A]
    ctx.run_ok("check", [PY, script, "check"] + base + ["--dry-run"])
    txt = ctx.run_ok("compute", [PY, script, "compute"] + base + ["--workers", str(ctx.workers)],
                     expect_files=[os.path.join(A, "atlas_bundle.zip"), os.path.join(A, "effects", "DD_beta.npy")])
    ang = os.path.join(A, "angles")
    if txt is not None:
        bad = [x for x in txt.splitlines() if "ERROR in" in x or "FAILED:" in x]
        ctx.record("compute: every angle ran without error", not bad,
                   "; ".join(bad) if bad else "no 'ERROR in angle' lines")

        def briefs():
            want = ATLAS_ANGLES + ["focus_MTAP", "focus_PSMD10"]
            miss = [a for a in want if not os.path.exists(os.path.join(ang, a, "brief.md"))]
            return not miss, f"missing brief.md: {miss}" if miss else f"{len(want)} angle folders with brief.md"
        ctx.check("angles: every angle folder has brief.md (incl. focus_MTAP, focus_PSMD10)", briefs)

        def read_positions():
            t = pd.read_csv(os.path.join(ang, "quality", "position_effects.csv"))
            t["row"] = range(1, len(t) + 1)
            first = t["top_up"].astype(str).str.split(";").str[0].str.strip()
            t["top_gene"] = first.str.split(" ").str[0]
            t["top_shift"] = pd.to_numeric(first.str.split(" ").str[1], errors="coerce")
            return t

        planted = {w: v["gene"] for w, v in gt["well_position_artifacts"].items()}

        def position_genes():
            # robust: each artifact position's most shifted gene is the planted one, and H1 and D10 carry the
            # largest single-gene shifts of all 96 positions (top 3)
            t = read_positions()
            by_shift = list(t.sort_values("top_shift", ascending=False)["well"])
            got = {w: t.loc[t["well"] == w, "top_gene"].iloc[0] for w in planted}
            ok = got == planted and {"H1", "D10"} <= set(by_shift[:3])
            return ok, (f"top gene per position {got}; largest single-gene shifts at "
                        f"{fmt_top(t.sort_values('top_shift', ascending=False), ['well', 'top_gene', 'top_shift'], 4)}")
        ctx.check("quality/position_effects: H1, D10 in the top-3 largest shifts; MTAP/PSMD10/CHAC1 top at "
                  "H1/D10/A12", position_genes)

        def position_sensitive():
            t = pd.read_csv(os.path.join(ang, "quality", "position_sensitive_genes.csv")).head(10)
            got = {g: w for g, w in zip(t["gene"], t["worst_well"])}
            ok = all(got.get(g) == w for w, g in planted.items())
            return ok, f"top 10: {fmt_top(t, ['gene', 'worst_well', 'shift_log2'], 10)}"
        ctx.check("quality/position_sensitive_genes: MTAP->H1, PSMD10->D10, CHAC1->A12 in the top 10",
                  position_sensitive)

        # The file is sorted by the NUMBER of genes shifted > 1.2x. Chance gives 0-6 such genes per position, so a
        # single-gene artifact (H1 = MTAP only) lands anywhere from row ~5 to ~40 depending on the seed: reported as
        # WARN (never fails the run) so that a lucky seed cannot hide the weakness and an unlucky one cannot fail it.
        try:
            t = read_positions()
            rows = {w: int(t.loc[t["well"] == w, "row"].iloc[0]) for w in ("H1", "D10")}
            ok = all(r <= 10 for r in rows.values())
            ctx.record("quality/position_effects: H1 and D10 in the first 10 rows (file order)", ok,
                       f"rows (sorted by genes_up_over_1.2x): {rows}; first rows "
                       f"{fmt_top(t, ['well', 'genes_up_over_1.2x', 'top_gene'], 5)}", status=None if ok else "WARN")
        except Exception as e:  # noqa: BLE001
            ctx.record("quality/position_effects: file order", False, f"{type(e).__name__}: {e}")

        def hmox1():
            t = pd.read_parquet(os.path.join(ang, "genes", "gene_top_drugs.parquet"))
            t = t[(t["gene"] == "HMOX1") & (t["direction"] == "up")].sort_values("rank")
            return t["drug"].iloc[0] == "Dimethyl fumarate", \
                f"HMOX1 inducers: {fmt_top(t, ['drug', 'conc', 'fold_change'], 3)}"
        ctx.check("genes: Dimethyl fumarate is the top HMOX1 inducer", hmox1)

        def bortezomib_toxic():
            t = pd.read_csv(os.path.join(A, "effects", "drugdose.csv"))
            f = str(t.loc[(t["drug"] == "Bortezomib") & (t["conc"] == 5.0), "flags"].iloc[0])
            return "toxic" in f, f"Bortezomib 5 uM flags: {f}"
        ctx.check("effects: Bortezomib 5 uM flagged toxic", bortezomib_toxic)

        def genotype_mtap():
            t = pd.read_csv(os.path.join(ang, "cell_lines", "genotype_selective_drugs.csv"))
            f = t[t["feature"].astype(str).str.contains("MTAP not expressed", regex=False)]
            if f.empty:
                return False, "no 'MTAP not expressed' feature; features: " + ", ".join(sorted(set(t["feature"]))[:12])
            lines = set(x.strip() for x in str(f["lines"].iloc[0]).split(","))
            want = set(gt["groups"]["mtap_null"])
            f = f.sort_values("z")
            return lines == want and "Pemetrexed" in top_k(f["drug"], 3), \
                (f"feature '{f['feature'].iloc[0]}' lines {sorted(lines)}; top drugs "
                 f"{fmt_top(f, ['drug', 'conc', 'z'], 3)}")
        ctx.check("cell_lines/genotype_selective_drugs: 'MTAP not expressed' = planted lines, Pemetrexed top 3",
                  genotype_mtap)

        def failed_well():
            t = pd.read_csv(os.path.join(A, "effects", "failed_wells.csv"))
            return gt["failed_well"]["sample"] in set(t["sample"]), f"failed wells: {list(t['sample'])}"
        ctx.check("effects: the failed well is excluded", failed_well)

        def plate2_offset():
            t = pd.read_csv(os.path.join(ang, "quality", "plate_dmso_offsets.csv"))
            r = t[t["plate"] == "plate2"].iloc[0]
            top = [x.strip().split(" ")[0] for x in str(r["top_dmso_low"]).split(";")[:5]]
            return bool({"PSMD10", "CDKN1A"} & set(top)), f"plate2 genes reading low in DMSO: {top}"
        ctx.check("quality/plate_dmso_offsets: plate2 DMSO low for PSMD10/CDKN1A", plate2_offset)

        def drugdose(drug, conc, col):
            t = pd.read_csv(os.path.join(A, "effects", "drugdose.csv"))
            return t.loc[(t["drug"] == drug) & (t["conc"] == conc), col].iloc[0]
        ctx.check("effects: Dinaciclib 5 uM flagged transcription drop",
                  lambda: ("transcription drop" in str(drugdose("Dinaciclib", 5.0, "flags")),
                           f"flags: {drugdose('Dinaciclib', 5.0, 'flags')}; UMIs/cell "
                           f"{2 ** drugdose('Dinaciclib', 5.0, 'umi_per_cell_log2_vs_plate'):.2f}x"))

        def paclitaxel():
            t = pd.read_csv(os.path.join(ang, "cell_state", "drug_cell_cycle.csv"))
            r = t[(t["drug"] == "Paclitaxel") & (t["conc"] == 5.0)].iloc[0]
            return r["cell_cycle_call"] == "G2/M build-up", \
                f"call '{r['cell_cycle_call']}', G2M {2 ** r['G2M_PHASE_lfc']:.2f}x"
        ctx.check("cell_state: Paclitaxel 5 uM = G2/M build-up", paclitaxel)

        def inducer(gene, drugs, k):
            t = pd.read_parquet(os.path.join(ang, "genes", "gene_top_drugs.parquet"))
            t = t[(t["gene"] == gene) & (t["direction"] == "up")].sort_values("rank")
            return bool(set(drugs) & set(top_k(t["drug"], k))), \
                f"{gene} inducers: {fmt_top(t, ['drug', 'conc', 'fold_change'], k)}"
        ctx.check("genes: Ciclopirox in top-2 TFRC inducers", lambda: inducer("TFRC", ["Ciclopirox"], 2))
        ctx.check("genes: Rimonabant in top-3 NAPEPLD inducers", lambda: inducer("NAPEPLD", ["Rimonabant"], 3))
        ctx.check("genes: Bortezomib in top-3 HSPA1A inducers", lambda: inducer("HSPA1A", ["Bortezomib"], 3))
        ctx.check("genes: a DNMT inhibitor in top-3 ISG15 inducers",
                  lambda: inducer("ISG15", ["Decitabine", "5-Azacytidine"], 3))

        def focus_level(gene, drug, k, fname="level_vs_growth.csv", col="z"):
            t = pd.read_csv(os.path.join(ang, f"focus_{gene}", fname)).sort_values(col)
            return drug in top_k(t["drug"], k), f"top: {fmt_top(t, ['drug', 'conc', col], k)}"
        ctx.check("focus_PSMD10/level_vs_growth: Ixazomib in top 3",
                  lambda: focus_level("PSMD10", "Ixazomib", 3))
        if os.path.exists(os.path.join(ang, "focus_MTAP", "loss_selective_drugs.csv")):
            ctx.check("focus_MTAP/loss_selective_drugs: Pemetrexed in top 3",
                      lambda: focus_level("MTAP", "Pemetrexed", 3, "loss_selective_drugs.csv"))
        else:
            ctx.record("focus_MTAP/loss_selective_drugs.csv written", False, "file missing (no MTAP loss group?)")

        def loss_group():
            t = pd.read_csv(os.path.join(ang, "cell_lines", "expression_loss_groups.csv"))
            want = set(gt["groups"]["mtap_null"])
            hit = [r for _, r in t.iterrows() if "MTAP" in str(r["genes"]).split(", ")]
            if not hit:
                return False, f"no loss group with MTAP; groups: {list(t['group'])[:8]}"
            lines = set(x.strip() for x in str(hit[0]["lines"]).split(","))
            return lines == want, f"group '{hit[0]['group']}' lines {sorted(lines)}"
        ctx.check("cell_lines/expression_loss_groups: MTAP loss group = planted lines", loss_group)

        def biomarker(drug, gene):
            t = pd.read_csv(os.path.join(ang, "biomarkers", "biomarker_top10.csv"))
            t = t[(t["drug"] == drug) & (t["conc"] == 5.0)]
            if t.empty:
                return False, f"{drug} 5 uM not eligible in biomarker_top10.csv"
            r = t[t["gene"] == gene]
            return (not r.empty and r["rho"].iloc[0] < 0), \
                f"{drug} 5 uM markers: {fmt_top(t, ['gene', 'rho'], 5)}"
        ctx.check("biomarkers: ACSL4 predicts Artesunate 5 uM depletion (top 10, rho < 0)",
                  lambda: biomarker("Artesunate", "ACSL4"))
        ctx.check("biomarkers: PSMD10 predicts Ixazomib 5 uM depletion (top 10, rho < 0)",
                  lambda: biomarker("Ixazomib", "PSMD10"))

        def hdac_class():
            t = pd.read_csv(os.path.join(ang, "classes", "class_summary.csv"))
            r = t[(t["kind"] == "mechanism") & (t["group"] == "HDAC inhibitor")]
            if r.empty:
                return False, "no HDAC inhibitor class row"
            r = r.iloc[0]
            return r["outlier_drug"] == "Carbamazepine" and r["consistency_z"] > 2, \
                f"consistency_z {r['consistency_z']:.1f}, outlier {r['outlier_drug']}"
        ctx.check("classes: HDAC inhibitors coherent, Carbamazepine the outlier (extra planted)", hdac_class)

    # look-ups, agents (dry run), bundle
    if os.path.exists(os.path.join(A, "effects", "DD_beta.npy")):
        for kind, name, must in (("gene", "PSMD10", "largest well-position shift: D10"),
                                 ("drug", "Bortezomib", "toxic"), ("line", "A549", "# A549"),
                                 ("corr", "MTAP", "co-regulated with MTAP")):
            out = ctx.run_ok(f"lookup_{kind}", [PY, script, "lookup", kind, name] + base)
            if out is not None:
                ctx.record(f"lookup {kind} {name}: card content", must in out,
                           f"expects '{must}'" + ("" if must in out else f"; got: {tail(out, 4)}"))
        txt = ctx.run_ok("agents_dry_run", [PY, script, "agents"] + base + ["--dry-run"])
        if txt is not None:
            def prompts():
                folders = [d for d in glob.glob(os.path.join(ang, "*")) if os.path.exists(os.path.join(d, "brief.md"))]
                miss = [os.path.basename(d) for d in folders if not os.path.exists(os.path.join(d, "agent_prompt.txt"))]
                return bool(folders) and not miss, f"{len(folders)} prompts" + (f"; missing {miss}" if miss else "")
            ctx.check("agents --dry-run: a prompt per angle", prompts)
    else:
        ctx.skip("lookup / agents --dry-run", "effects missing (compute failed)")
    txt = ctx.run_ok("bundle", [PY, script, "bundle"] + base, expect_files=[os.path.join(A, "atlas_bundle.zip")])
    if txt is not None:
        def bundle():
            with zipfile.ZipFile(os.path.join(A, "atlas_bundle.zip")) as z:
                names = z.namelist()
            comp = [n for n in names if n.startswith("computation/")]
            need = ["computation/effects/drugdose.csv", "computation/angles/quality/position_effects.csv"]
            miss = [n for n in need if n not in names]
            return len(comp) >= 20 and not miss, \
                f"{len(comp)} computation/ files" + (f"; missing {miss}" if miss else "")
        ctx.check("atlas_bundle.zip lists computation/ files", bundle)


# ============================================================================= stage: gene panel (future)
@stage("panel")
def stage_panel(ctx):
    """Placeholder for tahoe_gene_panel.py (extract/analyze into DIR/gene_panel). Skipped until the script exists.
    When it lands: keep the two commands below and add ground-truth checks from ctx.gt ('planted_drug_effects_top_dose',
    'groups', 'expression_facts', 'measured_expression', 'well_position_artifacts', 'plate_dmso_offset')."""
    script = os.path.join(REPO, "tahoe_gene_panel.py")
    if not os.path.exists(script):
        ctx.skip("tahoe_gene_panel.py", "not in the repo yet: stage skipped")
        return
    out = fresh(os.path.join(ctx.W, "gene_panel"))
    ctx.run_ok("extract", [PY, script, "extract", "--data", ctx.D, "--out", out, "--workers", str(ctx.workers)])
    ctx.run_ok("analyze", [PY, script, "analyze", "--data", ctx.D, "--out", out])
    ctx.check("gene_panel: output written", lambda: (any(os.scandir(out)), f"{len(os.listdir(out))} entries in {out}"))


# ============================================================================= main
def default_workdir():
    return os.environ.get("TAHOE_SMOKE_DIR") or os.path.join(tempfile.gettempdir(), "tahoe_smoke")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", default=default_workdir(), help="data + outputs (default: %(default)s)")
    ap.add_argument("--regen", action="store_true", help="regenerate the synthetic data")
    ap.add_argument("--only", default="", help="comma-separated stages: " + ",".join(STAGES))
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0, help="generator seed (data are regenerated when it changes)")
    args = ap.parse_args()
    want = [s.strip() for s in args.only.split(",") if s.strip()] or list(STAGES)
    unknown = [s for s in want if s not in STAGES]
    if unknown:
        sys.exit(f"unknown stage(s) {unknown}; choose from {list(STAGES)}")
    ctx = Ctx(args)
    t0 = time.time()
    print(f"Smoke test: python {sys.version.split()[0]} ({PY}); repo {REPO}; workdir {ctx.W}", flush=True)
    timings = {}
    if ensure_data(ctx):
        timings["data"] = round(time.time() - t0, 1)
        for name in want:
            ctx.stage = name
            print(f"\n=== stage {name} ===", flush=True)
            t1 = time.time()
            try:
                STAGES[name](ctx)
            except Exception:  # noqa: BLE001
                ctx.record(f"stage {name} crashed in run_smoke.py", False, traceback.format_exc()[-1500:])
            timings[name] = round(time.time() - t1, 1)
    counts = {s: sum(r["status"] == s for r in ctx.results) for s in ("PASS", "FAIL", "WARN", "SKIP")}
    summary = {"python": PY, "python_version": sys.version.split()[0], "repo": REPO, "workdir": ctx.W,
               "data": ctx.D, "stages": want, "seconds_total": round(time.time() - t0, 1),
               "seconds_by_stage": timings, "counts": counts, "results": ctx.results, "commands": ctx.commands}
    with open(os.path.join(ctx.W, "smoke_results.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print(f"\n{counts['PASS']} PASS, {counts['FAIL']} FAIL, {counts['WARN']} WARN, {counts['SKIP']} SKIP in "
          f"{summary['seconds_total']:.0f} s (stages: {timings}) -> {os.path.join(ctx.W, 'smoke_results.json')}")
    for r in ctx.results:
        if r["status"] in ("FAIL", "WARN"):
            print(f"  {r['status']} [{r['stage']}] {r['check']}: {r['detail'][:300]}")
    sys.exit(1 if counts["FAIL"] else 0)


if __name__ == "__main__":
    main()
