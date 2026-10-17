#!/usr/bin/env python3
"""
run_smoke.py - smoke-test every script of this repo against the synthetic Tahoe-100M data.

    python tests/run_smoke.py [--workdir DIR] [--regen] [--only small,atlas,mtap,panel,wrapper] [--workers 2]

1. Generates the synthetic download once into DIR/synthetic_tahoe (tests/make_synthetic_tahoe.py, ~1-2 min), and
   reuses it on later runs (regenerated automatically when the generator changed; --regen forces it).
2. Runs each script as a subprocess with this Python, from a scratch folder, writing into DIR:
     small  01_preview_parquet.py, 02_find_mtap_gankyrin.py, old_drug_effect_uncorrected.py   -> DIR/small
     atlas  tahoe_atlas.py check, compute, lookup x4, agents --dry-run, bundle      -> DIR/synthetic_tahoe/atlas
            (= <data>/atlas, where tahoe_mtap_gankyrin.py and the gene panel look for it, as on a real download)
     mtap   tahoe_mtap_gankyrin.py all + coreg (uses the atlas's composition shifts)        -> DIR/mtap_gankyrin
     panel  tahoe_gene_panel.py check, all (reads DIR/mtap_gankyrin and the atlas), agents --dry-run, analyze
            again with --prior none, bundle; a copy next to an older tahoe_mtap_gankyrin.py   -> DIR/gene_panel
     wrapper  tahoe_status.py status/next/facts on those outputs (both done, Next: tahoe bundle, 80 columns; older
              method stamps read 'outdated'), bash -n tahoe, tahoe help (bash only)       -> DIR/wrapper_state
   Each stage starts from an empty output folder.
3. Checks the outputs against the planted ground truth (DIR/synthetic_tahoe/ground_truth.json): one PASS/FAIL line
   per check (WARN = known weakness whose outcome depends on chance in these small data; it does not fail the run),
   a JSON summary in DIR/smoke_results.json, logs of every command in DIR/logs/. Exit code 1 on any FAIL.
   Checks named 'v3: ...' test method v3 on the traps planted for it (ground_truth.json 'method_v3').

DIR defaults to $TAHOE_SMOKE_DIR, else <system temp folder>/tahoe_smoke. No API key is used: the agents step runs
with --dry-run and the API-key variables are removed from the environment of every command.
To add a stage: write one function decorated with @stage("name") (see stage_panel for an example).
"""

import argparse
import glob
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import warnings
import zipfile
from collections import OrderedDict

import numpy as np
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
METHOD_VERSION = 3          # tahoe_atlas.EFFECTS_VERSION, tahoe_mtap_gankyrin.METHOD_VERSION, panel run_info.json
DMSO = "DMSO_TF"
# the flags the atlas, tahoe_mtap_gankyrin.py and the panel all define (v3 spec section 6; strings exact)
SHARED_FLAGS = ["toxic", "low cells (technical?)", "plate-row cell shift", "transcription drop", "cell-cycle shift",
                "composition shift", "noisy plate (z scaled)", "unreliable plate only",
                "position correction uncertain", "position not correctable", "wells disagree"]
PAIR_TYPES = {"same position, other plate", "different position", "same plate", "unreliable plate"}
NOISE_RNA = (r"^(7SK|RN7SK|RNU|SNOR|SCARNA|MT-|MTND|MTCO|MTATP|MTCY|RP[LS]\d+[A-Z]*P\d|H1-\d|H[2-4]C\d|H2[AB]C\d|"
             r"ENSG)")    # RULEBOOK rule 7, H1-* histones and RPL13AP5-style ribosomal pseudogenes included
GROWTH_DRUGS = {"Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)", "5-Fluorouracil", "Pemetrexed",
                "Ixazomib", "Artesunate", "Bortezomib"}       # planted cell-number effects (line-selective or toxic)

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
        self.A = os.path.join(self.D, "atlas")       # <data>/atlas: found there by tahoe_mtap_gankyrin.py and the panel
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


# ---- method v3 helpers
def flagset(v):
    """'toxic; transcription drop' -> {'toxic', 'transcription drop'} (NaN / empty -> empty set)."""
    return {x.strip() for x in v.split(";") if x.strip()} if isinstance(v, str) else set()


def dkey(drug, conc):
    return str(drug), round(float(conc), 6)


def flag_map(t):
    """{(drug, conc): set of flags} of a per drug-dose table."""
    return {dkey(d, c): flagset(f) for d, c, f in zip(t["drug"], t["conc"], t["flags"])}


def is_true(s):
    return s.astype(str).str.strip().str.lower().isin(["true", "1", "yes"])


def read_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def repo_int(fname, name):
    """An integer constant of a repo script, read from its source (NAME = 3), or None."""
    try:
        m = re.search(rf"^{name}\s*=\s*(\d+)", read_text(os.path.join(REPO, fname)), re.M)
    except OSError:
        return None
    return int(m.group(1)) if m else None


def planted_wells(gt):
    """{(drug, conc): {'reliable': [samples], 'unreliable': [samples]}} from the planted layout (failed well out)."""
    unrel = gt["method_v3"]["unreliable_plate"]["plate"]
    out = {}
    for w in gt["layout"]:
        if w["drug"] != DMSO and w["sample"] != gt["failed_well"]["sample"]:
            e = out.setdefault(dkey(w["drug"], w["conc"]), {"reliable": [], "unreliable": []})
            e["unreliable" if w["plate"] == unrel else "reliable"].append(w["sample"])
    return out


def used_wells(e):
    """The wells method v3 uses for a drug-dose: its reliable ones, or its unreliable ones when it has no other."""
    return e["reliable"] or e["unreliable"]


def atlas_v3_ready(ctx):
    try:
        return read_json(os.path.join(ctx.A, "effects", "complete.json")).get("version") == METHOD_VERSION
    except (OSError, ValueError, AttributeError):
        return False


def mentions(text, *needles):
    """The needles missing from text (whitespace-insensitive: the briefs are wrapped at ~118 columns, so a sentence
    may continue on the next line)."""
    flat = " ".join(str(text).split())
    return [n for n in needles if " ".join(n.split()) not in flat]


def check_option(ctx, script, opt="--unreliable-plates"):
    rc, text = ctx.run(f"help_{os.path.basename(script).split('.')[0]}", [PY, script, "--help"])
    ctx.record(f"v3: {os.path.basename(script)} --help lists {opt}", rc == 0 and opt in text, f"exit {rc}" +
               ("" if opt in text else f"; '{opt}' not in --help"))


TOXIC_CHECK = ("plate-row cell loss and low-dose-only loss read 'low cells (technical?)', not 'toxic'; the planted "
               "toxic drug-doses stay 'toxic'")


def toxic_rules(gt, t, need_low=True):
    """v3 'toxic' (TOXIC_CHECK) on a per drug-dose table t (drug, conc, flags). need_low=False: only 'not toxic'."""
    v3 = gt["method_v3"]
    F = flag_map(t)
    rc, lo = v3["row_cell_loss"], v3["low_dose_cell_loss"]
    row = [F.get(dkey(d, rc["conc"]), set()) for d in rc["drugs"]]
    n_tox, n_low, n_row = (sum(f in x for x in row) for f in ("toxic", "low cells (technical?)",
                                                               "plate-row cell shift"))
    q = F.get(dkey(lo["drug"], lo["conc"]), set())
    tox = {f"{x['drug']} {x['conc']:g}": "toxic" in F.get(dkey(x["drug"], x["conc"]), set())
           for x in gt["toxic_drug_doses"]}
    ok = n_tox == 0 and all(tox.values()) and "toxic" not in q and \
        (not need_low or (n_low >= 10 and n_row >= 10 and "low cells (technical?)" in q
                          and "plate-row cell shift" not in q))
    return ok, (f"{rc['plate']} row {rc['row']} drugs at {rc['conc']:g} uM: {n_tox}/12 toxic, {n_low}/12 low cells, "
                f"{n_row}/12 plate-row cell shift; {lo['drug']} {lo['conc']:g}: {sorted(q)}; planted toxic: {tox}")


def toxic_expected(t):
    """The v3 'toxic' rule, re-implemented here from the spec and the findings (one definition in both scripts):
    mean cells < -1 log2; < -1 also after subtracting the plate row's median where that row is itself shifted (|row|
    > 0.8; else the plain value); with several used wells the best one (cells_log2_best_well) < -0.5; no higher dose
    of the drug with mean cells >= -1. Returns a boolean Series (rows with cells >= -1: False)."""
    c = pd.to_numeric(t["cells_log2_vs_plate"], errors="coerce").fillna(0.0)
    r = pd.to_numeric(t["row_cells_log2"], errors="coerce").fillna(0.0)
    beyond = np.where(r.abs() > 0.8, np.maximum(c, c - r), c)
    best = pd.to_numeric(t["cells_log2_best_well"], errors="coerce") if "cells_log2_best_well" in t else \
        pd.Series(np.nan, index=t.index)
    conc = pd.to_numeric(t["conc"], errors="coerce")
    higher = [bool(((t["drug"] == d) & (conc > k) & (c >= -1)).any()) for d, k in zip(t["drug"], conc)]
    return pd.Series((c < -1) & (beyond < -1) & ~(best >= -0.5) & ~np.array(higher), index=t.index)


def toxic_rule_check(t, name):
    """Every drug-dose of t flagged 'toxic' exactly when toxic_expected says so, 'low cells (technical?)' for the
    other drug-doses below -1 (values within 0.02 of a cut are not counted)."""
    want = toxic_expected(t)
    got = t["flags"].map(lambda f: "toxic" in flagset(f))
    low = t["flags"].map(lambda f: "low cells (technical?)" in flagset(f))
    c = pd.to_numeric(t["cells_log2_vs_plate"], errors="coerce").fillna(0.0)
    cols = [x for x in ("cells_log2_vs_plate", "row_cells_log2", "cells_log2_best_well") if x in t]
    near = pd.concat([(pd.to_numeric(t[x], errors="coerce") - v).abs() < 0.02 for x in cols for v in (-1.0, -0.5)],
                     axis=1).any(axis=1)
    bad = t[((want != got) | ((c < -1) & ~got & ~low)) & ~near]
    return bad.empty and "cells_log2_best_well" in t, (
        f"{name}: {int(want.sum())} drug-doses meet the rule, {int(got.sum())} flagged 'toxic', "
        f"{int(low.sum())} 'low cells (technical?)'; cells_log2_best_well column: {'cells_log2_best_well' in t}; "
        f"disagree: {fmt_top(bad, ['drug', 'conc', 'flags'], 4) or 'none'}")


def repo_modules():
    """tahoe_mtap_gankyrin and tahoe_atlas of this repo, imported here (unit checks on crafted inputs)."""
    sys.path.insert(0, REPO)
    try:
        import tahoe_mtap_gankyrin as T
        import tahoe_atlas as A
        return T, A
    finally:
        sys.path.remove(REPO)


def cell_cycle_rule(t, s, g, sz, gz):
    """Drug-doses whose 'cell-cycle shift' flag disagrees with the v3 rule: |S or G2M shift| > 0.5, or > 0.25 with
    that module's |z| >= 4 (values within 0.01 / 0.1 of a cut are not counted)."""
    S, G, Sz, Gz = (pd.to_numeric(t[c], errors="coerce").fillna(0).abs() for c in (s, g, sz, gz))
    want = (S > 0.5) | (G > 0.5) | ((S > 0.25) & (Sz >= 4)) | ((G > 0.25) & (Gz >= 4))
    near = ((S - 0.5).abs() < 0.01) | ((G - 0.5).abs() < 0.01) | ((S - 0.25).abs() < 0.01) | \
        ((G - 0.25).abs() < 0.01) | ((Sz - 4).abs() < 0.1) | ((Gz - 4).abs() < 0.1)
    got = t["flags"].map(lambda f: "cell-cycle shift" in flagset(f))
    bad = t[(want != got) & ~near]
    return bad, int(want.sum())


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
            # uncorrected: the tests of wells in H1 read MTAP high (the artifact the corrected scripts remove). Read
            # per test (MTAP_DE_all_tests.csv has the plate): plate13 gives 92 drug-doses a third well, so a drug-
            # dose median over its rows mixes the H1 well with two others (shown for reference)
            t = pd.read_csv(os.path.join(old, "MTAP_by_drug_and_dose.csv"))
            lay = pd.DataFrame(ctx.gt["layout"])
            h1 = lay[(lay["well"] == "H1")][["drug", "conc", "plate"]]
            m = t.merge(h1, left_on=["drug", "concentration"], right_on=["drug", "conc"])
            other = t[~t.set_index(["drug", "concentration"]).index.isin(list(zip(m["drug"], m["concentration"])))]
            a, b = m["median_lfc"].median(), other["median_lfc"].median()
            at = pd.read_csv(os.path.join(old, "MTAP_DE_all_tests.csv"), dtype={"plate": str})
            keys = {(d, round(float(c), 6), str(p).replace("plate", "")) for d, c, p in
                    zip(h1["drug"], h1["conc"], h1["plate"])}
            here = np.array([(d, round(float(c), 6), str(p)) in keys for d, c, p in
                             zip(at["drug"], at["concentration"], at["plate"])], dtype=bool)
            x, y = at.loc[here, "log2FoldChange"].median(), at.loc[~here, "log2FoldChange"].median()
            return x - y > 0.2, (f"median uncorrected MTAP lfc of the {int(here.sum())} tests of H1 wells {x:.2f} vs "
                                 f"the other tests {y:.2f} (per drug-dose: H1 drug-doses {a:.2f}, others {b:.2f})")
        ctx.check("old_drug_effect: H1 artifact visible in uncorrected MTAP lfc (tests of H1 wells)", h1_inflated)


# ============================================================================= stage: atlas
@stage("atlas")
def stage_atlas(ctx):
    gt = ctx.gt
    A = fresh(ctx.A)                  # <data>/atlas: the panel and tahoe_mtap_gankyrin.py read it from there
    script = os.path.join(REPO, "tahoe_atlas.py")
    base = ["--data", ctx.D, "--out", A]
    ctx.run_ok("check", [PY, script, "check"] + base + ["--dry-run"])
    # --min-cells 10 as the mtap and panel stages, so that the atlas and the panel compute the same profiles
    txt = ctx.run_ok("compute", [PY, script, "compute"] + base + ["--workers", str(ctx.workers), "--min-cells", "10"],
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
            # largest single-gene shifts of the positions that hold >= 3 drug wells (a position artifact needs
            # several drugs; plate13's drug wells in H11/H12, DMSO positions elsewhere, are one drug each)
            t = read_positions()
            by_shift = list(t[t["n_drug_wells"] >= 3].sort_values("top_shift", ascending=False)["well"])
            got = {w: t.loc[t["well"] == w, "top_gene"].iloc[0] for w in planted}
            ok = got == planted and {"H1", "D10"} <= set(by_shift[:3])
            srt = t.sort_values("top_shift", ascending=False)
            return ok, (f"top gene per position {got}; largest single-gene shifts at "
                        f"{fmt_top(srt, ['well', 'n_drug_wells', 'top_gene', 'top_shift'], 5)} (well, drug wells, "
                        f"gene, shift); top 3 of the positions with >= 3 drug wells: {by_shift[:3]}")
        ctx.check("quality/position_effects: H1, D10 in the top-3 largest shifts (positions with >= 3 drug wells); "
                  "MTAP/PSMD10/CHAC1 top at H1/D10/A12", position_genes)

        def position_sensitive():
            # positions with >= 3 drug wells only (as above): plate13's H11/H12 hold one drug each
            t = pd.read_csv(os.path.join(ang, "quality", "position_sensitive_genes.csv"))
            n = read_positions().set_index("well")["n_drug_wells"]
            t = t[t["worst_well"].map(n).fillna(0) >= 3].head(10)
            got = {g: w for g, w in zip(t["gene"], t["worst_well"])}
            ok = all(got.get(g) == w for w, g in planted.items())
            return ok, f"top 10: {fmt_top(t, ['gene', 'worst_well', 'shift_log2'], 10)}"
        ctx.check("quality/position_sensitive_genes: MTAP->H1, PSMD10->D10, CHAC1->A12 in the top 10 (positions with "
                  ">= 3 drug wells)", position_sensitive)

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
        v3_atlas(ctx, A)
    v3_units(ctx)
    check_option(ctx, script)

    # look-ups, agents (dry run), bundle
    if os.path.exists(os.path.join(A, "effects", "DD_beta.npy")):
        for kind, name, must in (("gene", "PSMD10", "largest well-position shift: D10"),
                                 ("drug", "Bortezomib", "toxic"), ("line", "A549", "# A549"),
                                 ("corr", "MTAP", "co-regulated with MTAP")):
            out = ctx.run_ok(f"lookup_{kind}", [PY, script, "lookup", kind, name] + base)
            if out is not None:
                ctx.record(f"lookup {kind} {name}: card content", must in out,
                           f"expects '{must}'" + ("" if must in out else f"; got: {tail(out, 4)}"))
        if ctx.gt.get("method_v3"):                # spec 5: DD_posunc shown in 'lookup' (the co-located pair's TFRC)
            co = ctx.gt["method_v3"]["co_location"]
            out = ctx.run_ok("lookup_gene_TFRC", [PY, script, "lookup", "gene", "TFRC"] + base)
            if out is not None:
                m = re.search(r"uncertain in (\d+) drug-doses", out)
                n_unc = int(m.group(1)) if m else -1
                ctx.record("v3: lookup gene TFRC: the card counts the drug-doses whose position correction is "
                           f"uncertain (>= the 3 doses of {co['inert']}) and has a 'position' column",
                           n_unc >= 3 and " position" in out, f"uncertain in {n_unc} drug-doses" if m else
                           f"no 'uncertain in N drug-doses' in: {tail(out, 4)}")
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
            need = ["computation/effects/drugdose.csv", "computation/angles/quality/position_effects.csv",
                    "computation/effects/genes.csv", "computation/effects/README_effects.md"]
            miss = [n for n in need if n not in names]
            return len(comp) >= 20 and not miss, \
                f"{len(comp)} computation/ files" + (f"; missing {miss}" if miss else "")
        ctx.check("atlas_bundle.zip lists computation/ files", bundle)

        def bundle_briefs():
            with zipfile.ZipFile(os.path.join(A, "atlas_bundle.zip")) as z:
                names = set(z.namelist())
            want = [os.path.basename(d) for d in glob.glob(os.path.join(ang, "*"))
                    if os.path.exists(os.path.join(d, "brief.md"))]
            miss = [a for a in want if f"briefs/{a}.md" not in names]
            return bool(want) and not miss, f"{len(want) - len(miss)}/{len(want)} briefs/<angle>.md" + \
                (f"; missing {miss}" if miss else "")
        ctx.check("v3: atlas_bundle.zip holds every angle's brief (briefs/<angle>.md)", bundle_briefs)


# ============================================================================= stage: MTAP / Gankyrin
@stage("mtap")
def stage_mtap(ctx):
    gt = ctx.gt
    out = fresh(os.path.join(ctx.W, "mtap_gankyrin"))
    R = os.path.join(out, "results")
    script = os.path.join(REPO, "tahoe_mtap_gankyrin.py")
    atlas_ready = atlas_v3_ready(ctx)              # then it normalises composition with the atlas's shifts
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
        v3_mtap(ctx, R, atlas_ready)
    check_option(ctx, script)

    txt = ctx.run_ok("coreg", [PY, script, "coreg", "--data", ctx.D, "--out", out],
                     expect_files=[os.path.join(R, f) for f in ("coregulation_summary.txt", "coregulated_with_MTAP.csv",
                                                                 "coregulated_with_Gankyrin_PSMD10.csv")])
    if txt is not None:
        def coreg_rows():
            n = {f: len(pd.read_csv(os.path.join(R, f))) for f in ("coregulated_with_MTAP.csv",
                                                                   "coregulated_with_Gankyrin_PSMD10.csv")}
            return all(v >= 50 for v in n.values()), f"rows {n}"
        ctx.check("coreg: partner tables filled", coreg_rows)


# ============================================================================= stage: gene panel
def auc_of(pos, neg):
    """P(a random pos value > a random neg value), ties count half."""
    pos, neg = [float(x) for x in pos], [float(x) for x in neg]
    if not pos or not neg:
        return float("nan")
    wins = sum((a > b) + 0.5 * (a == b) for a in pos for b in neg)
    return wins / (len(pos) * len(neg))


@stage("panel")
def stage_panel(ctx):
    """tahoe_gene_panel.py check, all (extract + analyze + bundle, reading the mtap stage's output as the earlier
    run), agents --dry-run, bundle; then the planted ground truth and the reproduction of tahoe_mtap_gankyrin.py."""
    gt = ctx.gt
    script = os.path.join(REPO, "tahoe_gene_panel.py")
    if not os.path.exists(script):
        ctx.skip("tahoe_gene_panel.py", "not in the repo: stage skipped")
        return
    out = fresh(os.path.join(ctx.W, "gene_panel"))
    R = os.path.join(out, "results")
    prior = os.path.join(ctx.W, "mtap_gankyrin")
    have_prior = os.path.exists(os.path.join(prior, "results", "MTAP_null_selective_drugs.csv"))
    base = ["--data", ctx.D, "--out", out]
    ctx.run_ok("check", [PY, script, "check"] + base + ["--prior", prior])
    txt = ctx.run_ok("all", [PY, script, "all"] + base + ["--workers", str(ctx.workers), "--min-cells", "10",
                                                          "--prior", prior],
                     expect_files=[os.path.join(R, f) for f in
                                   ("summary.txt", "README_columns.txt", "panel_genes.csv", "expression_by_line.csv",
                                    "positive_controls.csv", "pathway_scores_by_dose.csv", "drug_context_by_dose.csv",
                                    "ferro_markers_with_context.csv", "p53_wt_vs_altered.csv",
                                    "p53_functional_status.csv", "p53_wt_selective_growth.csv",
                                    "MTAP_null_selective_drugs.csv", "loss_groups.csv", "loss_screens.csv",
                                    "reexpression_in_silenced_lines.csv", "level_vs_growth.csv",
                                    "cell_cycle_by_line.csv", "coregulation_matrix.csv", "crosslinks.csv",
                                    "efflux_high_lines_growth.csv", "efflux_substrate_test.csv",
                                    "efflux_active_drugs.csv",
                                    "well_position_effects.csv", "plate_dmso_offsets.csv", "CHAC1_drug_summary.csv",
                                    "PSMD10_drug_effects_by_dose.csv")] + [os.path.join(out, "gene_panel_bundle.zip")])
    ang = os.path.join(out, "angles")
    angles = ["ferroptosis", "pyroptosis", "p53", "napepld_trim72", "efflux", "crosslinks"]
    if txt is not None:
        bad = [x.strip() for x in txt.splitlines() if "WARNING:" in x and " failed:" in x]
        ctx.record("all: every analysis step ran (no 'WARNING: ... failed')", not bad, "; ".join(bad)[:1500] or
                   "none failed")

        def csv(name):
            return pd.read_csv(os.path.join(R, name))

        def p53_top():
            t = csv("p53_wt_vs_altered.csv").sort_values("z_wt_more", ascending=False)
            dd = {"Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)", "5-Fluorouracil"}
            ok = set(top_k(t["drug"], 3)) <= dd and dd <= set(top_k(t["drug"], 6))
            return ok, f"top: {fmt_top(t, ['drug', 'conc', 'z_wt_more'], 6)}"
        ctx.check("p53_wt_vs_altered: Doxorubicin, Topotecan, 5-FU top the WT-vs-altered screen", p53_top)

        def p53_auc():
            t = csv("p53_functional_status.csv").dropna(subset=["p53_responsiveness_log2"])
            wt = t["tp53_annotation"].astype(str).str.startswith("wild type")
            a = auc_of(t.loc[wt, "p53_responsiveness_log2"], t.loc[~wt, "p53_responsiveness_log2"])
            want = set(gt["group_ids"]["tp53_wt"])
            same = set(t.loc[wt, "cell_line_id"]) == want
            return a >= 0.9 and same, f"AUC responsiveness WT vs altered {a:.2f}; WT annotation == planted: {same}"
        ctx.check("p53_functional_status: responsiveness separates TP53 WT from altered (AUC >= 0.9)", p53_auc)

        def dmf():
            s_ = csv("pathway_scores_by_dose.csv")
            s_ = s_[s_["score"] == "NRF2"].sort_values("z", ascending=False)
            h = csv("HMOX1_drug_effects_by_dose.csv").sort_values("z_corrected", ascending=False)
            ok = s_["drug"].iloc[0] == "Dimethyl fumarate" and h["drug"].iloc[0] == "Dimethyl fumarate"
            return ok, f"NRF2: {fmt_top(s_, ['drug', 'conc', 'z'], 2)}; HMOX1: {fmt_top(h, ['drug', 'conc', 'fold_change'], 2)}"
        ctx.check("Dimethyl fumarate tops the NRF2 score and the HMOX1 inducers", dmf)

        def ferro():
            t = csv("ferro_markers_with_context.csv")

            def row(d):
                r = t[(t["drug"] == d) & (t["conc"] == 5.0)].iloc[0]
                return r["z"], r["fdr_up"], r["ISR_z"], str(r["reading"]) if pd.notna(r["reading"]) else ""
            az, aq, ai, ar = row("Artesunate")
            uz, uq, ui, ur = row("Auranofin")
            ok = (az >= 3 and aq < 0.1 and ai < 3 and bool(ar) and "artifact" not in ar
                  and uz >= 3 and uq < 0.1 and ui >= 3 and bool(ur) and "artifact" not in ur)
            return ok, (f"Artesunate 5: markers z {az:.1f}, fdr {aq:.2g}, ISR z {ai:.1f} ({ar}); Auranofin 5: markers "
                        f"z {uz:.1f}, fdr {uq:.2g}, ISR z {ui:.1f} ({ur})")
        ctx.check("FERRO_MARKERS: Artesunate 5 uM up with ISR_z < 3, Auranofin 5 uM with ISR_z >= 3 (both read)", ferro)

        def inducer(gene, drugs, k):
            t = csv(f"{gene}_drug_effects_by_dose.csv").sort_values("z_corrected", ascending=False)
            return bool(set(drugs) & set(top_k(t["drug"], k))), \
                f"{gene}: {fmt_top(t, ['drug', 'conc', 'fold_change', 'z_corrected'], k)}"
        ctx.check("TFRC: Ciclopirox is the top inducer", lambda: inducer("TFRC", ["Ciclopirox"], 1))
        ctx.check("NAPEPLD: Rimonabant in the top-3 inducers", lambda: inducer("NAPEPLD", ["Rimonabant"], 3))

        def gsdme():
            t = csv("reexpression_in_silenced_lines.csv")
            t = t[t["gene"] == "GSDME"].sort_values("z_corrected", ascending=False)
            dnmt = {"Decitabine", "5-Azacytidine"}
            ok = t["drug"].iloc[0] in dnmt and dnmt <= set(top_k(t["drug"], 3))
            return ok, f"GSDME in the silenced lines: {fmt_top(t, ['drug', 'conc', 'fold_change', 'z_corrected'], 4)}"
        ctx.check("GSDME: Decitabine / 5-Azacytidine top the inducers in the GSDME-silenced lines", gsdme)

        def reexpr():
            t = csv("reexpression_in_silenced_lines.csv")
            t["reading"] = t["reading"].fillna("").astype(str)
            re_ = t["reading"].str.startswith("re-expression")
            dele = t[t["gene"].isin(["CDKN2A", "CDKN2B"])]
            g = t[(t["gene"] == "GSDME") & re_].sort_values("z_corrected", ascending=False)
            ok = not (dele["reading"].str.startswith("re-expression")).any() and \
                set(dele["gene"]) == {"CDKN2A", "CDKN2B"} and len(g) > 0 and g["drug"].iloc[0] == "Decitabine"
            return ok, (f"CDKN2A/B rows: {dele.groupby('gene')['reading'].first().to_dict()}; GSDME 're-expression' "
                        f"readings: {fmt_top(g, ['drug', 'conc', 'fold_change', 'z_corrected'], 3)}")
        ctx.check("re-expression: none for the deleted CDKN2A/CDKN2B; Decitabine tops the GSDME re-expression readings",
                  reexpr)

        def il1b():
            t = csv("expression_by_line.csv")
            got = set(t.loc[(t["gene"] == "IL1B") & t["expressed"].astype(bool), "cell_line_id"].astype(str))
            want = set(gt["group_ids"]["il1b_expressing"])
            pg = csv("panel_genes.csv").set_index("gene")
            return got == want and pg.at["IL1B", "ambient_cpm"] > 0, \
                (f"IL1B expressed in {sorted(got)}; planted {sorted(want)}; ambient {pg.at['IL1B', 'ambient_cpm']:.2f} "
                 f"CPM (af {pg.at['IL1B', 'ambient_fraction']:.3f})")
        ctx.check("expression: IL1B expressed (above ambient) only in the planted il1b_expressing lines", il1b)

        def loss_gsdme():
            t = csv("loss_groups.csv")
            r = t[t["gene"] == "GSDME"]
            if r.empty:
                return False, f"no GSDME loss group; groups: {list(t['gene'])}"
            got = {x.strip() for x in str(r["cell_line_ids"].iloc[0]).split(",")}
            want = set(gt["group_ids"]["gsdme_silenced"])
            return got == want, f"GSDME loss group {r['lines'].iloc[0]}; planted {sorted(gt['groups']['gsdme_silenced'])}"
        ctx.check("loss_groups: GSDME loss group == the planted GSDME-silenced lines", loss_gsdme)

        def expression():
            t = csv("panel_genes.csv").set_index("gene")["status"].astype(str)
            ok = "not expressed" in t["TRIM72"] and all(t[g] != "testable" for g in ("NLRP3", "CASP5", "AIM2"))
            return ok, "; ".join(f"{g}: {t[g][:45]}" for g in ("TRIM72", "NLRP3", "CASP5", "AIM2", "GSDME"))
        ctx.check("panel_genes: TRIM72 'not expressed'; NLRP3/CASP5/AIM2 not testable", expression)

        def level(gene, drug):
            t = csv("level_vs_growth.csv")
            t = t[t["gene"] == gene].sort_values("z")
            r = t[(t["drug"] == drug) & (t["conc"] == 5.0)]
            ok = drug in top_k(t["drug"], 3) and not r.empty and r["rho"].iloc[0] < 0
            return ok, f"{gene}: {fmt_top(t, ['drug', 'conc', 'rho', 'z'], 3)}"
        ctx.check("level_vs_growth: ACSL4 level predicts Artesunate depletion (top 3, rho < 0)",
                  lambda: level("ACSL4", "Artesunate"))
        ctx.check("level_vs_growth: PSMD10 level predicts Ixazomib depletion (top 3, rho < 0)",
                  lambda: level("PSMD10", "Ixazomib"))

        def pemetrexed():
            t = csv("MTAP_null_selective_drugs.csv").sort_values("z_selective")
            return "Pemetrexed" in top_k(t["drug"], 3), f"top: {fmt_top(t, ['drug', 'conc', 'z_selective'], 3)}"
        ctx.check("MTAP_null_selective_drugs: Pemetrexed in the top 3", pemetrexed)

        def efflux_expression():
            t = csv("expression_by_line.csv")
            pg = csv("panel_genes.csv").set_index("gene")
            out, ok = [], True
            for gene, group in (("ABCB1", "abcb1_high"), ("ABCG2", "abcg2_high")):
                got = set(t.loc[(t["gene"] == gene) & t["expressed"].astype(bool), "cell_line_id"].astype(str))
                want = set(gt["group_ids"].get(group, []))
                ok &= got == want and str(pg.at[gene, "status"]) == "testable"
                out.append(f"{gene} expressed in {sorted(got)} (planted {sorted(want)}); status {pg.at[gene, 'status']}")
            return ok, "; ".join(out)
        ctx.check("efflux: ABCB1 / ABCG2 expressed (above ambient) only in the planted pump-high lines, both testable",
                  efflux_expression)

        def efflux_group():
            # the pump-high group the screen built must be exactly the planted high lines (only expression is
            # planted, no growth effect, so z_spared is not checked)
            t = csv("efflux_high_lines_growth.csv")
            name = {l["cell_line_id"]: l["cell_name"] for l in gt["lines"]}
            out, ok = [], True
            for gene, group in (("ABCB1", "abcb1_high"), ("ABCG2", "abcg2_high")):
                r = t[t["pump"] == gene]
                got = set(str(r["high_lines"].iloc[0]).split(", ")) if len(r) else set()
                want = {name[i] for i in gt["group_ids"][group]}
                ok &= got == want and len(r) > 0
                out.append(f"{gene}: high group {sorted(got)} (planted {sorted(want)})")
            return ok, "; ".join(out)
        ctx.check("efflux: the screen's pump-high group == the planted ABCB1 / ABCG2 high lines", efflux_group)

        def efflux_test_ran():
            t = csv("efflux_substrate_test.csv")
            pumps = set(t["pump"]) if len(t) else set()
            d = csv("efflux_active_drugs.csv")
            # the growth screen ran for both pumps and the substrate test produced rows (no planted sparing, so the
            # AUC is not asserted); the active-drug table lists drug-doses that depleted cells
            return {"ABCB1", "ABCG2"} <= pumps and len(d) > 0, \
                f"substrate test pumps {sorted(pumps)}; active drug-doses {len(d)}"
        ctx.check("efflux: the substrate test and active-drug table are produced for both pumps", efflux_test_ran)

        def bortezomib():
            t = csv("drug_context_by_dose.csv")
            r = t[(t["drug"] == "Bortezomib") & (t["conc"] == 5.0)].iloc[0]
            f, c = str(r["flags"]), str(r["context"])
            return "toxic" in f and "HEAT_SHOCK up" in c and "PROTEASOME up" in c, f"flags: {f}; context: {c}"
        ctx.check("drug_context: Bortezomib 5 uM toxic with HEAT_SHOCK / PROTEASOME context", bortezomib)

        def chac1():
            w = csv("well_position_effects.csv")
            w = w[w["gene"] == "CHAC1"].sort_values("z_vs_other_positions", ascending=False)
            e = csv("CHAC1_drug_effects_by_dose.csv")
            inducers = {"Auranofin", "Artesunate", "Bortezomib"}
            a12 = e[e["wells"].astype(str).str.split(",").map(lambda s: "A12" in s)]
            bad_calls = a12[(a12["call"] == "up") & ~a12["drug"].isin(inducers)]
            calls = e[e["call"] == "up"]
            other = calls[~calls["drug"].isin(inducers)]
            # chance false calls: at most what an FDR of 10% allows (method-independent: ceil(0.10 x the calls));
            # the zero of the original check depended on the data draw (this one: Bentamapimod 0.5 uM, q ~0.1)
            allowed = math.ceil(0.10 * len(calls))
            ok = w["well"].iloc[0] == "A12" and bad_calls.empty and len(other) <= allowed
            return ok, (f"top CHAC1 position {w['well'].iloc[0]} ({w['median_effect_plate_corrected'].iloc[0]:+.2f}); "
                        f"{len(a12)} drug-doses sat in A12, up calls among them not planted: {len(bad_calls)}; "
                        f"all CHAC1 up calls: {sorted(set(calls['drug']))}; not planted: {len(other)} (FDR 10% "
                        f"allows {allowed} of {len(calls)}): {fmt_top(other, ['drug', 'conc', 'fdr_up'], 3) or 'none'}")
        ctx.check("CHAC1: A12 position effect found and removed (no CHAC1 call driven by A12; unplanted up calls "
                  "within the 10% FDR)", chac1)

        def bortezomib_controls():
            # planted 3x HMOX1 and 2x CHAC1 (5 uM; 40% of the log effect at 0.5 uM). The toxic 5 uM dose keeps ~7
            # cells per line and well (5 lines measured) and one of its two wells sits on the noisy plate (z divided
            # by ~2), so its call is not guaranteed; the rise must show at 5 uM and be called at >= 1 dose
            out, ok = [], True
            for g, fold in (("HMOX1", 3.0), ("CHAC1", 2.0)):
                e = csv(f"{g}_drug_effects_by_dose.csv")
                b = e[e["drug"] == "Bortezomib"].set_index("conc")
                called = sorted(float(c) for c in b.index[b["call"].fillna("") == "up"])
                fc5 = float(b.at[5.0, "fold_change"]) if 5.0 in b.index else np.nan
                ok &= bool(called) and fc5 >= 1.5
                out.append(f"{g} (planted {fold:g}x): called up at {called or 'no dose'}; 5 uM {fc5:.2f}x "
                           f"(z {float(b.at[5.0, 'z_corrected']) if 5.0 in b.index else np.nan:.1f})")
            return ok, "; ".join(out)
        ctx.check("Bortezomib (positive control): HMOX1 and CHAC1 called up at >= 1 dose and >= 1.5x at the toxic "
                  "5 uM", bortezomib_controls)

        def plate2():
            p = csv("plate_dmso_offsets.csv")
            top = {g: p[p["gene"] == g].sort_values("dmso_offset", ascending=False)["plate"].iloc[0]
                   for g in ("CDKN1A", "PSMD10")}
            e = csv("CDKN1A_drug_effects_by_dose.csv")
            e = e[e["plates"].astype(str).str.split(",").map(lambda s: "plate2" in s)]
            u, c = e["log2FC_vs_DMSO_uncorrected"].median(), e["log2FC_corrected"].abs().median()
            calls = int((e["call"] == "up").sum())
            ok = set(top.values()) == {"plate2"} and u > 0.15 and c < 0.12 and calls == 0
            return ok, (f"top DMSO-offset plate {top}; CDKN1A drug-doses on plate2: median uncorrected log2FC {u:.2f}, "
                        f"median |corrected| {c:.2f}, up calls {calls}")
        ctx.check("plate2 DMSO offset seen (CDKN1A, PSMD10) and not in the corrected calls", plate2)

        def failed():
            t = csv("excluded_failed_wells.csv")
            return gt["failed_well"]["sample"] in set(t["sample"]), f"excluded {list(t['sample'])}"
        ctx.check("excluded_failed_wells: the failed well is excluded", failed)

        def controls():
            t = csv("positive_controls.csv")
            want = [("NRF2 target genes", "Dimethyl fumarate"), ("raises HMOX1", "Dimethyl fumarate"),
                    ("proteasome subunits", "Bortezomib"), ("heat-shock genes", "Bortezomib"),
                    ("TFRC", "Ciclopirox"), ("GSDME", "Decitabine"), ("interferon", "Decitabine"),
                    ("G2/M genes", "Paclitaxel"), ("transcription drop", "Dinaciclib"),
                    ("raise P53_ACTIVITY", "Topotecan (hydrochloride)"), ("TP53-wild-type", "5-Fluorouracil")]
            res = {}
            for key, drug in want:
                r = t[t["expectation"].str.contains(key, regex=False) & (t["drug"] == drug)]
                res[f"{key}/{drug}"] = r["verdict"].iloc[0] if len(r) else "missing"
            bad = {k: v for k, v in res.items() if v != "clear"}
            return not bad, f"not clear: {bad}" if bad else f"{len(res)} planted controls clear"
        ctx.check("positive_controls: every planted control is 'clear'", controls)

        def at24():
            t = csv("positive_controls.csv")
            vals = set(t["expected_at_24h"].astype(str))
            dnmt = set(t.loc[t["expectation"].str.startswith("DNMT"), "expected_at_24h"].astype(str))
            return vals == {"robust", "uncertain"} and dnmt == {"uncertain"}, \
                f"expected_at_24h values {sorted(vals)}; DNMT rows {sorted(dnmt)}"
        ctx.check("positive_controls.csv has expected_at_24h (robust / uncertain; DNMT inhibitors uncertain)", at24)

        def prior_agreement():
            if not have_prior:
                return False, f"no earlier run in {prior} (run the mtap stage first)"
            t = csv("crosslinks.csv").set_index("comparison")
            w = float(t.loc["well positions (sample_map.csv)", "value"])
            m = str(t.loc["MTAP-null calls", "reading"])
            return w == 100.0 and m == "identical", f"wells at the same position {w:.1f}%; MTAP-null calls: {m}"
        ctx.check("crosslinks: 100% of wells agree with the earlier run; identical MTAP-null calls", prior_agreement)

        def reproduce(mine, theirs, key, cols):
            a = pd.read_csv(os.path.join(R, mine))
            b = pd.read_csv(os.path.join(prior, "results", theirs))
            if key:
                a = a[a["gene"] == key]
            m = a.merge(b, on=["drug", "conc"], suffixes=("", "_t"))
            d = {c: float((m[c] - m[ct + ("_t" if c == ct else "")]).abs().max()) for c, ct in cols}
            ok = len(m) == len(a) == len(b) and all(v <= 1e-6 for v in d.values())
            return ok, f"{len(m)}/{len(b)} drug-doses matched; max |difference| " + \
                ", ".join(f"{c} {v:.2g}" for c, v in d.items())
        if have_prior:
            ctx.check("reproduces tahoe_mtap_gankyrin MTAP_null_selective_drugs.csv (z, depletion) within 1e-6",
                      lambda: reproduce("MTAP_null_selective_drugs.csv", "MTAP_null_selective_drugs.csv", None,
                                        [("z_selective", "z_selective"), ("extra_log2_depletion_of_MTAP_null",
                                                                          "extra_log2_depletion_of_MTAP_null")]))
            ctx.check("reproduces tahoe_mtap_gankyrin Gankyrin_level_vs_drug_response.csv (rho, partial, z) "
                      "within 1e-6",
                      lambda: reproduce("level_vs_growth.csv", "Gankyrin_level_vs_drug_response.csv", "PSMD10",
                                        [("rho", "rho"), ("rho_partial_G2M", "rho_partial_G2M"),
                                         ("z", "z_corrected")]))
        else:
            ctx.skip("reproduction of tahoe_mtap_gankyrin.py", f"no earlier run in {prior}: run the mtap stage first")

        def sections():
            with open(os.path.join(R, "summary.txt"), encoding="utf-8") as fh:
                lines = fh.read().splitlines()
            missing = [k for k in range(1, 11) if not any(x.startswith(f"{k}. ") for x in lines)]
            return not missing and "Steps that failed: none" in lines, \
                (f"missing sections {missing}" if missing else "sections 1-10 present") + \
                ("" if "Steps that failed: none" in lines else "; some steps failed")
        ctx.check("summary.txt has sections 1-10 and no failed step", sections)

        def briefs():
            miss = [a for a in angles if not os.path.exists(os.path.join(ang, a, "brief.md"))]
            return not miss, f"missing brief.md: {miss}" if miss else f"{len(angles)} angle folders with brief.md"
        ctx.check("angles: every angle folder has brief.md", briefs)
        v3_panel(ctx, out)
    check_option(ctx, script)
    v3_panel_guard(ctx, script)
    txt = ctx.run_ok("agents_dry_run", [PY, script, "agents"] + base + ["--dry-run"])
    if txt is not None:
        def prompts():
            folders = [d for d in glob.glob(os.path.join(ang, "*")) if os.path.exists(os.path.join(d, "brief.md"))]
            miss = [os.path.basename(d) for d in folders if not os.path.exists(os.path.join(d, "agent_prompt.txt"))]
            return len(folders) == len(angles) and not miss, f"{len(folders)} prompts" + (f"; missing {miss}"
                                                                                          if miss else "")
        ctx.check("agents --dry-run: a prompt per angle", prompts)

        def agents_log():
            f = os.path.join(out, "agents.log")
            with open(f, encoding="utf-8") as fh:
                t = fh.read()
            return "Dry run" in t, f"{f}: {len(t)} bytes" + ("" if "Dry run" in t else "; no 'Dry run' line")
        ctx.check("agents --dry-run writes gene_panel/agents.log", agents_log)
    # a rerun of analyze: earlier results moved aside, earlier tables gone from the agent folders, the agents' own
    # scripts kept, and a report older than the new analysis left out of the bundle. It runs without the earlier
    # run (--prior none): the cross-links then speak of this run only (v3 spec section 8)
    p53dir = os.path.join(ang, "p53")
    stale, script_ = os.path.join(p53dir, "stale_table.csv"), os.path.join(p53dir, "agent_script.py")
    old_rep = os.path.join(out, "reports", "02_pyroptosis.md")
    if os.path.isdir(p53dir):
        os.makedirs(os.path.dirname(old_rep), exist_ok=True)
        for f, text in ((stale, "a,b\n1,2\n"), (script_, "print(1)\n"), (old_rep, "# old report\n" + "x" * 300)):
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(text)
    txt = ctx.run_ok("analyze_again", [PY, script, "analyze"] + base + ["--min-cells", "10", "--prior", "none"],
                     expect_files=[os.path.join(R, "previous_run", "summary.txt"), os.path.join(R, "summary.txt")])
    if txt is not None:
        def rerun():
            prev = sorted(os.listdir(os.path.join(R, "previous_run")))
            ok = not os.path.exists(stale) and os.path.exists(script_) and \
                os.path.exists(os.path.join(p53dir, "brief.md")) and "summary.txt" in prev
            return ok, (f"previous_run/: {len(prev)} files; stale angle table removed: {not os.path.exists(stale)}; "
                        f"agent script kept: {os.path.exists(script_)}")
        ctx.check("analyze again: earlier results in results/previous_run/, stale angle tables removed", rerun)
        v3_noprior(ctx, out)
    txt = ctx.run_ok("bundle", [PY, script, "bundle"] + base, expect_files=[os.path.join(out, "gene_panel_bundle.zip")])
    if txt is not None:
        def bundle():
            with zipfile.ZipFile(os.path.join(out, "gene_panel_bundle.zip")) as z:
                names = z.namelist()
            need = ["computation/results/summary.txt", "computation/results/positive_controls.csv",
                    "computation/gene_panel.log", "agent_logs/agents.log"]
            miss = [n for n in need if n not in names]
            stale_rep = "reports/02_pyroptosis.md" in names
            return not miss and not stale_rep, f"{len(names)} files" + (f"; missing {miss}" if miss else "") + \
                ("; holds a report older than the analysis" if stale_rep else "; out-of-date report left out")
        ctx.check("gene_panel_bundle.zip holds the summary, positive controls and both logs, no out-of-date report",
                  bundle)

        def bundle_v3():
            with zipfile.ZipFile(os.path.join(out, "gene_panel_bundle.zip")) as z:
                names = z.namelist()
            miss = [f"briefs/{a}.md" for a in angles if f"briefs/{a}.md" not in names] + \
                [f for f in ("results/run_info.json", "results/well_effects.csv.gz")
                 if not any(n.endswith(f) for n in names)]
            return not miss, f"{len(names)} files" + (f"; missing {miss}" if miss else "; briefs, run_info.json and "
                                                                                       "well_effects.csv.gz in")
        ctx.check("v3: gene_panel_bundle.zip holds briefs/<pathway>.md, results/run_info.json, "
                  "results/well_effects.csv.gz", bundle_v3)


# ============================================================================= stage: the 'tahoe' command
@stage("wrapper")
def stage_wrapper(ctx):
    """tahoe_status.py on the finished outputs of the stages above (both runs done, a sensible Next line), then
    'bash -n tahoe' and 'tahoe help'. Needs the atlas and panel stages' outputs in DIR (skipped without them)."""
    status = os.path.join(REPO, "tahoe_status.py")
    tahoe = os.path.join(REPO, "tahoe")
    if not os.path.exists(status) or not os.path.exists(tahoe):
        ctx.skip("tahoe / tahoe_status.py", "not in the repo: stage skipped")
        return
    outs = {"atlas": ctx.A, "panel": os.path.join(ctx.W, "gene_panel"), "mtap": os.path.join(ctx.W, "mtap_gankyrin")}
    if not (os.path.exists(os.path.join(outs["atlas"], "atlas.log"))
            and os.path.exists(os.path.join(outs["panel"], "gene_panel.log"))):
        ctx.skip("tahoe_status.py on the smoke outputs", "no atlas / gene panel outputs in DIR: run those stages first")
    else:
        state = fresh(os.path.join(ctx.W, "wrapper_state"))      # no job files: as for runs started by hand
        base = ["--data", ctx.D, "--atlas-out", outs["atlas"], "--panel-out", outs["panel"], "--mtap-out", outs["mtap"],
                "--state", state]
        cols = ctx.env.get("COLUMNS")
        ctx.env["COLUMNS"] = "80"                                 # the screen as in an 80-column SSH window
        try:
            txt = ctx.run_ok("status", [PY, status, "status"] + base)
        finally:
            if cols is None:
                ctx.env.pop("COLUMNS", None)
            else:
                ctx.env["COLUMNS"] = cols
        if txt is not None:
            rows = txt.splitlines()

            def row(label):
                return next((r for r in rows if r.startswith(label)), "")
            ctx.check("status: atlas and gene panel reported done",
                      lambda: (row("Atlas").split()[1:2] == ["done"] and row("Gene panel").split()[2:3] == ["done"],
                               f"{row('Atlas').strip()} | {row('Gene panel').strip()}"))
            ctx.check("status: download complete (expression files and metadata)",
                      lambda: ("done:" in row("Download") and "4 of 4 metadata" in row("Download"), row("Download")))
            nxt = row("Next:")
            ctx.check("status: one Next line, saying 'tahoe bundle' (both done, no agents yet, no bundle zip)",
                      lambda: (sum(r.startswith("Next:") for r in rows) == 1 and "tahoe bundle" in nxt, nxt))
            wide = [r for r in rows[1:] if len(r) > 79]
            ctx.check("status: every line fits an 80-column window (long ones wrapped, none cut off)",
                      lambda: (not wide and not any(r.rstrip().endswith("...") for r in rows),
                               f"{len(wide)} lines over 79 characters" + (f": {wide[0]!r}" if wide else "")))
            nx = ctx.run_ok("next", [PY, status, "next"] + base)
            if nx is not None:
                ctx.check("'tahoe_status.py next' says what the status screen's Next line says",
                          lambda: (nx.strip().startswith(nxt[len("Next: "):].strip()), nx.strip()))
        txt = ctx.run_ok("facts", [PY, status, "facts"] + base)
        if txt is not None:
            facts = dict(x.split("=", 1) for x in txt.splitlines() if "=" in x)
            want = {"atlas": "done", "panel": "done", "atlas_ready": "1", "panel_ready": "1", "running": "",
                    "queued": ""}
            ctx.check("facts: atlas/panel done and ready, nothing running or queued",
                      lambda: (all(facts.get(k) == v for k, v in want.items()),
                               ", ".join(f"{k}={facts.get(k)!r}" for k in want)))

            def interrupted():
                # 'angles' killed part-way after a new 'effects': some briefs older than effects/complete.json
                cj = os.path.join(outs["atlas"], "effects", "complete.json")
                bs = sorted(glob.glob(os.path.join(outs["atlas"], "angles", "*", "brief.md")))[:3]
                keep = {b: (os.stat(b).st_atime, os.stat(b).st_mtime) for b in bs}
                old = os.path.getmtime(cj) - 60
                try:
                    for b in bs:
                        os.utime(b, (old, old))
                    rc, text = ctx.run("facts_interrupted_angles", [PY, status, "facts"] + base)
                    f = dict(x.split("=", 1) for x in text.splitlines() if "=" in x)
                    ok = rc == 0 and f.get("atlas_ready") == "0" and "angles" in f.get("atlas_plan", "").split()
                    return ok, (f"{len(bs)} of the briefs older than the effects: "
                                f"atlas_ready={f.get('atlas_ready')!r}, atlas_plan={f.get('atlas_plan')!r}")
                finally:
                    for b, (a, m) in keep.items():
                        os.utime(b, (a, m))
            ctx.check("v3: status: briefs older than the effects (an interrupted 'angles') are not ready; 'tahoe run' "
                      "plans angles", interrupted)
        v3_outdated(ctx, base, outs["panel"])
        v3_briefcheck(ctx, base)
    bash = shutil.which("bash")
    if sys.platform == "win32" or not bash:
        ctx.skip("bash -n tahoe, tahoe help", "no bash here (Windows uses the PowerShell commands)")
        return
    ctx.run_ok("bash_n", [bash, "-n", tahoe])
    txt = ctx.run_ok("help", [bash, tahoe, "help"])
    if txt is not None:
        names = ["run", "atlas", "panel", "mtap", "log", "bundle", "agents", "stop", "setup", "download", "test",
                 "update"]
        lines = txt.strip().splitlines()
        missing = [n for n in names if f"tahoe {n}" not in txt]
        ctx.record("tahoe help: every command listed in <= 20 lines", not missing and len(lines) <= 20,
                   f"{len(lines)} lines" + (f"; missing {missing}" if missing else ""))
        wide = [x for x in lines if len(x) > 79 and "(data:" not in x]
        ctx.record("tahoe help: lines fit an 80-column window", not wide,
                   f"longest {max(len(x) for x in lines)} characters" + (f": {wide[0]!r}" if wide else ""))


# ============================================================================= method v3 checks (spec section 10)
# Each trap of ground_truth.json 'method_v3' (tests/make_synthetic_tahoe.py) and what v3 should make of it; the
# names, columns, files and flag strings are those of the v3 method (README.md, 'Method v3').
def no_v3(ctx, what):
    if ctx.gt.get("method_v3"):
        return False
    ctx.skip(f"v3: {what}", "ground_truth.json has no 'method_v3' (data from an older generator: run with --regen)")
    return True


def v3_atlas(ctx, A):
    """tahoe_atlas.py: version stamp, plate factors, unreliable plate, co-location, uncorrectable position,
    composition, flags, statistics (spec sections 2-7, 9)."""
    if no_v3(ctx, "atlas checks"):
        return
    gt, v3 = ctx.gt, ctx.gt["method_v3"]
    fxd, ang = os.path.join(A, "effects"), os.path.join(A, "angles")
    unrel, noisy = v3["unreliable_plate"]["plate"], v3["noisy_plate"]
    regular = [p for p in gt["plates"] if p != unrel]
    lay = {w["sample"]: w for w in gt["layout"]}
    W = planted_wells(gt)
    cache = {}

    def csv(rel, **kw):
        if rel not in cache:
            cache[rel] = pd.read_csv(os.path.join(A, rel), **kw)
        return cache[rel]

    def npy(name):
        if name not in cache:
            cache[name] = np.asarray(np.load(os.path.join(fxd, f"{name}.npy"), mmap_mode="r"), dtype=float)
        return cache[name]

    def dd():
        t = csv("effects/drugdose.csv", dtype={"drug": str, "dose": str})
        t["flags"] = t["flags"].fillna("").astype(str)
        return t

    def genes():
        g = csv("effects/genes.csv")
        return dict(zip(g["symbol"].astype(str), g["col"].astype(int))), \
            np.flatnonzero((g["kind"] == "gene").to_numpy())

    def stamp():
        have, want = read_json(os.path.join(fxd, "complete.json")).get("version"), repo_int("tahoe_atlas.py",
                                                                                          "EFFECTS_VERSION")
        return have == want == METHOD_VERSION, f"complete.json version {have}; tahoe_atlas.py EFFECTS_VERSION {want}"
    ctx.check("v3: effects/complete.json version 3 (tahoe_atlas.EFFECTS_VERSION 3)", stamp)

    # ---- a. noisy plate (section 3)
    def plate_scale():
        # one row per (plate, dose) present, each carrying the factor of the group it joins ('group'): the group rows
        # are those whose (plate, dose) is the group itself
        t = csv("effects/plate_scale.csv", dtype={"plate": str, "dose": str})
        t = t[t["group"].astype(str) == t["plate"] + " " + t["dose"]].copy()
        t["dose"] = pd.to_numeric(t["dose"], errors="coerce")
        n = t.groupby("plate").size().to_dict()
        nz = t.loc[t["plate"] == noisy["plate"], "factor"]
        peer = t[t["plate"].isin(noisy["peers"])]
        rest = t.loc[~t["plate"].isin([noisy["plate"], unrel]), "factor"]
        ok = (len(nz) == 1 and 1.5 <= float(nz.iloc[0]) <= 2.8 and len(peer) and (peer["factor"] <= 1.15).all()
              and (peer["factor_raw"] < 0.85).all() and (t["factor"] >= 1 - 1e-9).all() and rest.max() <= 1.25
              and all(n.get(p) == 1 for p in regular) and n.get(unrel) == 3)
        return ok, "; ".join(f"{r.plate} {r.dose:g} uM {r.factor:.2f} (raw {r.factor_raw:.2f}, {int(r.n_wells)} wells)"
                             for r in t.itertuples())
    ctx.check(f"v3: plate_scale.csv: noisy {noisy['plate']} factor ~2, its peer 1 (never narrowed), the others "
              f"<= 1.25; one group per regular plate (the 0.05 uM reference well joins it), 3 on {unrel}", plate_scale)

    def dd_plate_scale():
        t = csv("effects/plate_scale.csv", dtype={"plate": str})
        fac = {(p, round(float(d), 6)): f for p, d, f in zip(t["plate"], pd.to_numeric(t["dose"]), t["factor"])}
        big = t.sort_values("n_wells").groupby("plate").tail(1).set_index("plate")["factor"].to_dict()
        bad, badflag, n5 = [], [], 0
        for r in dd().itertuples():
            e = W.get(dkey(r.drug, r.conc))
            if e is None:
                continue
            want = float(np.mean([fac.get((lay[s]["plate"], round(lay[s]["conc"], 6)), big.get(lay[s]["plate"]))
                                  for s in used_wells(e)]))
            if not abs(r.plate_scale - want) <= 0.02:
                bad.append(f"{r.drug} {r.conc:g} {r.plate_scale:.2f} (mean of its wells' factors {want:.2f})")
            if ("noisy plate (z scaled)" in flagset(r.flags)) != (r.plate_scale > 1.2):
                badflag.append(f"{r.drug} {r.conc:g} ({r.plate_scale:.2f}: {r.flags})")
            n5 += bool(r.conc == 5.0 and r.plate_scale > 1.2)
        return not bad and not badflag and n5 >= 70, (
            f"{n5} 5 uM drug-doses scaled > 1.2 and flagged; plate_scale wrong: {bad[:3] or 'none'}; flag wrong: "
            f"{badflag[:3] or 'none'}")
    ctx.check("v3: drugdose.csv plate_scale = mean factor of the used wells; 'noisy plate (z scaled)' when > 1.2 (the "
              "5 uM drug-doses)", dd_plate_scale)

    def spurious():
        inert = set(v3["inert_drugs"]) - set(v3["row_cell_loss"]["drugs"])
        t = dd()
        t = t[t["drug"].isin(inert)]
        s = {c: int(t.loc[np.isclose(t["conc"], c), "n_sig_genes"].sum()) for c in (0.05, 0.5, 5.0)}
        return s[5.0] <= 2 * max(s[0.05], s[0.5]) + 10, (
            f"significant genes summed over the {t['drug'].nunique()} inert drugs by dose: {s} (the 5 uM drug-doses "
            f"have a well on {noisy['plate']}; the old method gave ~1,100 at 5 uM vs ~60 at 0.5 uM)")
    ctx.check("v3: the noisy plate's spurious calls are gone (inert drugs: 5 uM <= 2 x the lower doses + 10 "
              "significant genes)", spurious)

    # ---- b. unreliable plate (section 4)
    def only13():
        want = {dkey(x["drug"], x["conc"]) for x in v3["unreliable_plate"]["only_there"]}
        got = {k for k, f in flag_map(dd()).items() if "unreliable plate only" in f}
        return got == want, f"flagged {sorted(got)}; planted {sorted(want)}"
    ctx.check(f"v3: drug-doses only on {unrel} (and only they) flagged 'unreliable plate only'", only13)

    def reliable_only():
        wl = csv("effects/wells.csv", dtype={"sample": str, "plate": str})
        row = {s: i for i, s in enumerate(wl["sample"])}
        W2, L = npy("W2"), npy("DD_lfc")
        badn, worst, n = [], 0.0, 0
        for i, r in enumerate(dd().itertuples()):
            e = W.get(dkey(r.drug, r.conc))
            if not e or not e["reliable"] or not e["unreliable"]:
                continue
            n += 1
            if int(r.n_wells) != len(e["reliable"]):
                badn.append(f"{r.drug} {r.conc:g}: n_wells {r.n_wells}, reliable wells {len(e['reliable'])}")
            m = np.nanmean(W2[[row[s] for s in e["reliable"]]], axis=0)
            ok = np.isfinite(m) & np.isfinite(L[i])
            if ok.any():
                worst = max(worst, float(np.max(np.abs(L[i][ok] - m[ok]))))
        return n >= 50 and not badn and worst < 1e-3, (
            f"{n} drug-doses with a {unrel} well and reliable ones: n_wells = reliable wells "
            + ("for all" if not badn else f"NOT for {'; '.join(badn[:3])}")
            + f"; max |DD_lfc - mean W2 of the reliable wells| {worst:.2g}; wells.csv keeps the {unrel} wells: "
            + str(bool((wl["plate"] == unrel).any())))
    ctx.check(f"v3: drug-doses with a {unrel} well use only their reliable wells (n_wells, DD_lfc = mean W2 of those)",
              reliable_only)

    def replicates():
        t = csv("angles/quality/replicates.csv", dtype={"drug": str, "dose": str})
        js = json.dumps(read_json(os.path.join(ang, "quality", "summary.json")))
        d = dd()
        on = ["drug", "dose"] if "dose" in t else ["drug", "conc"]
        ts = t.merge(d.loc[d["n_sig_genes"] >= 10, on], on=on)
        med = ts.groupby("pair_type")["r"].median().to_dict()
        types = set(t["pair_type"].astype(str))
        need = PAIR_TYPES                   # same plate: the row-loss drugs' positions on plate6 (planted)
        ok = types <= PAIR_TYPES and need <= types and \
            med.get("unreliable plate", 1.0) < med.get("different position", 0.0) - 0.1 and \
            all(p in js for p in ("unreliable plate", "different position"))
        return ok, (f"pair types {sorted(types)}; median r (drug-doses with >= 10 significant genes): "
                    + ", ".join(f"{k} {v:.2f}" for k, v in med.items())
                    + f"; summary.json names the pair types: {'unreliable plate' in js}")
    ctx.check(f"v3: quality/replicates.csv pair_type; {unrel} pairs agree less than pairs at a different position; "
              "summary.json per pair type", replicates)

    def same_position_null():
        js = read_json(os.path.join(ang, "quality", "summary.json"))
        v, r = js.get("same_position_random_pair_median_r"), js.get("random_pair_median_r")
        ok = isinstance(v, (int, float)) and math.isfinite(v) and isinstance(r, (int, float)) and math.isfinite(r)
        return ok, f"random pairs median r {r}; same-position random pairs median r {v}"
    ctx.check("v3: quality/summary.json has the same-position null next to the random-pair null", same_position_null)

    # ---- c. co-location, d. uncorrectable position (section 5)
    def coloc():
        c = v3["co_location"]
        col, gi = genes()
        own = [col[x] for x in c["genes"] if x in col]
        down = [col[x] for x in gt["extra_not_in_panel_spec"]["synthetic gene sets"]["COLOC_DOWN"] if x in col]
        d = dd()
        L, U = npy("DD_lfc"), npy("DD_posunc")
        y = np.flatnonzero((d["drug"] == c["inert"]).to_numpy())
        x = np.flatnonzero((d["drug"] == c["strong"]).to_numpy())
        x5 = np.flatnonzero(((d["drug"] == c["strong"]) & np.isclose(d["conc"], 5.0)).to_numpy())
        other = np.setdiff1d(gi, own)
        y_eff = float(np.nanmedian(np.abs(L[np.ix_(y, own)])))
        y_unc, y_oth, x_unc = (float(np.mean(U[np.ix_(r, k)])) for r, k in ((y, own), (y, other), (x, own)))
        x_eff = float(np.nanmedian(L[np.ix_(x5, down)]))
        before = float(np.median(np.abs(list(c["inert_log2_before_fix"].values()))))
        # (the strong drug is 'uncertain' on its genes too: its only donors, the inert drug's wells, carry the
        # pass-1 mirror image, |z| >= 3; with no correction its own effect is right, which is what counts)
        ok = y_eff < 0.15 and y_unc >= 0.8 and y_oth <= 0.1 and x_eff <= -1.0
        return ok, (f"{c['inert']} on {c['strong']}'s {len(own)} genes: median |log2FC| {y_eff:.2f} (the mirror image "
                    f"before the fix: ~{before:.2f}), DD_posunc {100 * y_unc:.0f}% (its other genes "
                    f"{100 * y_oth:.0f}%); {c['strong']}: DD_posunc {100 * x_unc:.0f}%, own down genes at 5 uM "
                    f"{x_eff:.2f} log2")
    ctx.check("v3: co-located inert drug ~0 on the strong drug's genes, DD_posunc ('position correction uncertain') "
              "there and not on its other genes; the strong drug's own effect kept", coloc)

    def uncorrectable():
        u = v3["uncorrectable"]
        d = dd()
        want = {dkey(u["drug"], u["conc"])}
        col = {dkey(a, b) for a, b, v in zip(d["drug"], d["conc"], is_true(d["position_not_correctable"])) if v}
        fl = {k for k, f in flag_map(d).items() if "position not correctable" in f}
        wl = csv("effects/wells.csv", dtype={"sample": str, "plate": str})
        h = wl[(wl["drug"] == u["drug"]) & (wl["well"] == u["well"])]
        clean = [c for c in wl.columns if "clean" in c.lower()]
        ok = col == want and fl == want and len(h) == len(u["plates"]) and (h["position_wells_used"] < 3).all() and \
            bool(clean)
        return ok, (f"position_not_correctable {sorted(col)}, flag {sorted(fl)} (planted {sorted(want)}); "
                    f"{u['drug']} {u['well']} wells: donors {sorted(set(h['position_wells_used']))}; "
                    f"clean-donor column in wells.csv: {clean or 'none'}")
    ctx.check(f"v3: {v3['uncorrectable']['drug']} 0.05 uM (in {v3['uncorrectable']['well']} on every plate) and only "
              "it 'position not correctable'; wells.csv donors and clean donors", uncorrectable)

    # ---- e. composition (section 2)
    def composition():
        c = v3["composition"]
        p = pd.read_parquet(os.path.join(fxd, "composition_shift.parquet"))
        wl = csv("effects/wells.csv", dtype={"sample": str, "plate": str})
        exp = c["expected_shift_log2_by_dose"]["5.0"]
        cw = wl.loc[(wl["drug"] == c["drug"]) & np.isclose(wl["conc"], 5.0), "composition_shift_log2"]
        oth = wl.loc[~is_true(wl["is_dmso"]) & (wl["drug"] != c["drug"]), "composition_shift_log2"]
        d = dd()
        i = int(np.flatnonzero(((d["drug"] == c["drug"]) & np.isclose(d["conc"], 5.0)).to_numpy())[0])
        r = d.iloc[i]
        nflag = sum("composition shift" in f for f in flag_map(d).values())
        col, gi = genes()
        tg = [col[x] for x in c["genes"] if x in col]
        L = npy("DD_lfc")
        rest, tgt = float(np.nanmedian(L[i, np.setdiff1d(gi, tg)])), float(np.nanmedian(L[i, tg]))
        ok = {"sample", "cell_line_id", "shift_log2"} <= set(p.columns) and len(cw) == 2 and \
            float((cw - exp).abs().max()) <= 0.2 and abs(float(oth.median())) < 0.05 and \
            r["composition_shift_log2"] <= -0.3 and "composition shift" in flagset(r["flags"]) and nflag <= 3 and \
            abs(rest) < 0.1 and tgt >= 3
        return ok, (f"{c['drug']} 5 uM wells {', '.join(f'{v:+.2f}' for v in cw)} (planted ~{exp:+.2f}), drug-dose "
                    f"{r['composition_shift_log2']:+.2f}, flags '{r['flags']}'; other drug wells median "
                    f"{float(oth.median()):+.3f}; {nflag} drug-doses flagged; after the normalisation its other genes "
                    f"median log2FC {rest:+.2f} (before ~{exp:+.2f}), the {len(tg)} genes it raises {tgt:+.2f}")
    ctx.check("v3: composition_shift.parquet; the composition-shift drug's wells / drug-dose read the planted shift, "
              "flagged 'composition shift'; its other genes ~0 after the normalisation", composition)

    # ---- f. and the other flags (section 6)
    ctx.check("v3: atlas drugdose.csv: " + TOXIC_CHECK, lambda: toxic_rules(gt, dd()))

    def cell_cycle():
        bad, n = cell_cycle_rule(dd(), "S_PHASE_lfc", "G2M_PHASE_lfc", "S_PHASE_z", "G2M_PHASE_z")
        return bad.empty, f"{n} drug-doses meet the rule; flag disagrees: " + \
            (fmt_top(bad, ["drug", "conc", "flags"], 4) or "none")
    ctx.check("v3: 'cell-cycle shift' = |S or G2M| > 0.5, or > 0.25 with |z| >= 4 (drugdose.csv)", cell_cycle)

    def disagree():
        d = dd()
        rr = pd.to_numeric(d["replicate_r"], errors="coerce")
        want = (rr < 0.1) & (d["n_sig_genes"] >= 100) & (d["n_wells"] >= 2)
        got = d["flags"].map(lambda f: "wells disagree" in flagset(f))
        bad = d[want != got]
        return bad.empty, (f"replicate_r for {int(rr.notna().sum())} drug-doses; {int(got.sum())} flagged 'wells "
                           f"disagree'; rule broken for: {fmt_top(bad, ['drug', 'conc'], 4) or 'none'}")
    ctx.check("v3: drugdose.csv replicate_r; 'wells disagree' = r < 0.1 with >= 100 significant genes", disagree)

    # ---- focus angles, statistics (section 7), briefs (section 9)
    def focus_lines():
        res = {}
        for g in ("MTAP", "PSMD10"):
            t = csv(f"angles/focus_{g}/drug_effects.csv")
            b = csv(f"angles/focus_{g}/baseline_by_line.csv")
            res[g] = (int(t["lines_measured"].max()), int(is_true(b["expressing"]).sum()))
        return all(a <= b for a, b in res.values()), "; ".join(f"{g}: lines_measured up to {a}, {b} lines express it"
                                                                for g, (a, b) in res.items())
    ctx.check("v3: focus drug_effects.csv per-line columns count only the lines that express the gene", focus_lines)

    def focus_flags():
        F = flag_map(csv("angles/focus_MTAP/drug_effects.csv"))
        u = v3["uncorrectable"]
        got = {f"{u['drug']} {u['conc']:g}": "position not correctable" in F.get(dkey(u["drug"], u["conc"]), set())}
        got.update({f"{x['drug']} {x['conc']:g}": "unreliable plate only" in F.get(dkey(x["drug"], x["conc"]), set())
                    for x in v3["unreliable_plate"]["only_there"]})
        return all(got.values()), f"flags in focus_MTAP/drug_effects.csv: {got}"
    ctx.check("v3: focus_MTAP/drug_effects.csv carries 'position not correctable' / 'unreliable plate only'",
              focus_flags)

    def focus_brief():
        out = {}
        for g in ("MTAP", "PSMD10"):
            b = read_text(os.path.join(ang, f"focus_{g}", "brief.md"))
            out[g] = mentions(b, "analysis of these data was inconclusive", "S_PHASE_z", "G2M_PHASE_z", "PROTEASOME_z",
                              "loss_selective_drugs.csv") + (["(names bentamapimod)"] if "bentamapimod" in b.lower()
                                                             else [])
        return not any(out.values()), "; ".join(f"focus_{g}: missing {m}" if m else f"focus_{g}: ok"
                                                 for g, m in out.items())
    ctx.check("v3: focus briefs: the 'inconclusive earlier analysis' context (no hard-coded bentamapimod)",
              focus_brief)

    def empirical_null():
        hits = []
        for rel in ("focus_MTAP/level_vs_growth.csv", "focus_PSMD10/level_vs_growth.csv",
                    "cell_state/proliferation_dependent_drugs.csv"):
            t = csv(f"angles/{rel}")
            h = t[(t["q"] < 0.1) & ~t["drug"].isin(GROWTH_DRUGS)]
            hits += [f"{rel.split('/')[0]}: {d} {c:g}" for d, c in zip(h["drug"], h["conc"])]
        return not hits, f"q < 0.1 from drugs without a planted growth effect: {hits[:6] or 'none'}"
    ctx.check("v3: focus level_vs_growth / proliferation_dependent_drugs (empirical null): no q < 0.1 hit from a drug "
              "without a planted growth effect", empirical_null)

    def biomarkers():
        t = csv("angles/biomarkers/selective_drugs.csv")
        rep = is_true(t["replicated"]).astype(int)
        ok = len(t) > 0 and bool((rep.diff().fillna(0) <= 0).all())
        return ok, f"{int(rep.sum())} of {len(t)} selective drug-doses replicated; replicated ones listed first: {ok}"
    ctx.check("v3: biomarkers/selective_drugs.csv 'replicated' column, ranked replicated first", biomarkers)

    def small_group():
        t = csv("angles/line_response/feature_response_top.csv")
        sg = is_true(t["small_group"])
        b = read_text(os.path.join(ang, "line_response", "brief.md"))
        ok = len(t) > 0 and bool((sg == (t["n_group_lines"] <= 4)).all()) and "small_group" in b
        return ok, f"{int(sg.sum())} of {len(t)} rows small_group; the brief names it: {'small_group' in b}"
    ctx.check("v3: line_response/feature_response_top.csv small_group = n_group_lines <= 4 (and in the brief)",
              small_group)

    def lowest_dose():
        t = csv("angles/drugs/drug_summary.csv")
        bad = []
        for r in t.itertuples():
            doses = [float(x) for x in str(r.doses).split(" / ")]
            ns = [int(float(x)) for x in str(r.n_sig_by_dose).split(" / ")]
            ok_from = [i for i in range(len(ns)) if all(n >= 10 for n in ns[i:])]
            want = doses[ok_from[0]] if ok_from else ("low dose only (noise?)" if max(ns) >= 10 else None)
            got = r.lowest_active_dose
            if want is None:
                good = pd.isna(got) or str(got).strip() in ("", "nan")
            elif isinstance(want, str):
                good = str(got) == want
            else:
                try:
                    good = abs(float(got) - want) < 1e-9
                except (TypeError, ValueError):
                    good = False
            if not good:
                bad.append(f"{r.drug}: {got} (n_sig {r.n_sig_by_dose}; rule: {want})")
        n_low = sum(str(x) == "low dose only (noise?)" for x in t["lowest_active_dose"])
        return not bad, f"{len(t)} drugs, {n_low} 'low dose only (noise?)'; rule broken for: {bad[:3] or 'none'}"
    ctx.check("v3: drugs/drug_summary.csv lowest_active_dose: lowest dose with it and every higher dose >= 10 genes, "
              "else 'low dose only (noise?)'", lowest_dose)

    def gene_lists():
        out = {}
        for f, dirn in (("inducible_genes.csv", "up"), ("repressible_genes.csv", "down")):
            t = csv(f"angles/genes/{f}")
            per = int(t.groupby([f"best_{dirn}_drug", f"best_{dirn}_conc"]).size().max()) if len(t) else 0
            out[f] = (per, int(t["gene"].astype(str).str.match(NOISE_RNA).sum()), len(t))
        return all(p <= 25 and k == 0 for p, k, _ in out.values()), \
            "; ".join(f"{f}: {n} genes, at most {p} per best drug-dose, {k} noise-class RNAs"
                      for f, (p, k, n) in out.items())
    ctx.check("v3: genes/inducible_genes.csv, repressible_genes.csv: <= 25 genes per best drug-dose, no noise-class "
              "RNAs", gene_lists)

    def calib_table():
        hits = []
        for f in sorted(glob.glob(os.path.join(ang, "quality", "*.csv"))):
            c = list(pd.read_csv(f, nrows=2).columns)
            if "plate" in c and any(x in c for x in ("dose", "conc")) and sum("1.96" in x for x in c) >= 2:
                hits.append(os.path.basename(f))
        return bool(hits), f"plate x dose calibration tables (before / after scaling): {hits or 'none'}"
    ctx.check("v3: quality angle has a plate x dose calibration table (% |z| > 1.96 / > 3 before and after scaling)",
              calib_table)

    ctx.check("v3: atlas drugdose.csv 'toxic' follows the rule (row subtracted only when the row is shifted; best "
              "used well; no higher dose recovering), other cell loss 'low cells (technical?)'",
              lambda: toxic_rule_check(dd(), "drugdose.csv"))

    def coloc_clean():
        c = v3.get("co_location_clean")
        if not c:
            return False, "ground_truth.json has no method_v3 co_location_clean (old generator?)"
        col, _gi = genes()
        own = np.array([col[x] for x in c["genes"] if x in col])
        w = csv("effects/wells.csv", dtype={"sample": str, "plate": str, "drug": str})
        hit = np.flatnonzero(((w["drug"] == c["inert"]) & (w["plate"] == c["inert_plate"]) &
                              (w["well"] == c["well"])).to_numpy())
        if not hit.size or not own.size:
            return False, f"no {c['inert']} well at {c['well']} on {c['inert_plate']} in wells.csv / genes missing"
        i = int(hit[0])
        W1, W2, U = npy("W1")[:, own], npy("W2")[:, own], npy("posunc")[:, own]
        drugw = ~w["is_dmso"].astype(bool).to_numpy()
        slot, dname = w["slot"].to_numpy(dtype=float), w["drug"].to_numpy(dtype=object)

        def donors_of(j):
            return np.flatnonzero(drugw & (slot == slot[j]) & (dname != dname[j]))

        def med3(rows):                       # the median of >= 3 donors with a value, else 0 (per gene)
            V = W1[rows]
            k = np.isfinite(V).sum(axis=0)
            m = np.nanmedian(V, axis=0) if len(rows) else np.full(V.shape[1], np.nan)
            return np.where(k >= 3, m, 0.0), k
        # the first pass (every donor), its robust z (reliable drug wells, the pass-1 plate factor), recomputed
        eff1 = np.zeros_like(W1)
        for j in np.flatnonzero(drugw):
            eff1[j] = med3(donors_of(j))[0]
        W2a = W1 - eff1
        rel = drugw & ~is_true(w["unreliable_plate"]).to_numpy()
        c1 = np.nanmedian(W2a[rel], axis=0)
        s1 = 1.4826 * np.nanmedian(np.abs(W2a[rel] - c1), axis=0)
        za = (W2a - c1) / (s1 * w["plate_scale_pass1"].to_numpy(dtype=float)[:, None])
        dn = donors_of(i)
        V = np.where(np.abs(za[dn]) < 3, W1[dn], np.nan)     # clean donors only
        k = np.isfinite(V).sum(axis=0)
        want = np.where(k >= 3, np.nanmedian(V, axis=0), 0.0)
        got = W1[i] - W2[i]
        same = float(np.mean(np.abs(got - want) < 1e-3))
        strong = np.isin(dn, np.flatnonzero(dname == c["strong"]))
        dropped = float(np.mean((np.abs(za[dn][strong]) >= 3).any(axis=0)))
        alld = med3(dn)[0]
        differ = float(np.mean(np.abs(alld - want) > 1e-3))
        unc = float(U[i].astype(bool).mean())
        after = float(np.nanmedian(np.abs(W2[i])))
        ndrug = int(pd.unique(dname[dn]).size)
        d = dd()
        x5 = np.flatnonzero(((d["drug"] == c["strong"]) & np.isclose(d["conc"], 5.0)).to_numpy())
        down = [col[g] for g, v in c["strong_log2_top_dose"].items() if v < 0 and g in col]
        x_eff = float(np.nanmedian(npy("DD_lfc")[np.ix_(x5, down)])) if x5.size and down else np.nan
        ok = len(dn) >= 6 and ndrug >= 4 and unc <= 0.2 and same >= 0.95 and dropped >= 0.9 and differ >= 0.5 \
            and after < 0.2 and x_eff <= -1.0 and bool((k >= 3).mean() >= 0.8)
        return ok, (f"{c['inert']} {c['inert_plate']} {c['well']}: {len(dn)} donor wells of {ndrug} drugs; on "
                    f"{c['strong']}'s {len(own)} genes: a {c['strong']} donor dropped as unclean for "
                    f"{100 * dropped:.0f}%, the correction = the median of the clean donors (recomputed) for "
                    f"{100 * same:.0f}% (every donor's median would differ for {100 * differ:.0f}%), 'position "
                    f"correction uncertain' {100 * unc:.0f}%; median |log2FC| {after:.2f}; {c['strong']} 5 uM own "
                    f"down genes {x_eff:.2f} log2")
    ctx.check("v3: co-location with enough clean donors (6 donors of >= 4 drugs, one strong): the inert drug's well "
              "is corrected by the median of its clean donors (the strong drug's wells dropped), ~0 on its genes, NOT "
              "'position correction uncertain'", coloc_clean)

    def gene_factors():
        # each gene's divisor per plate group = max(group factor, its own spread ratio / 1.3), recomputed from W2
        w = csv("effects/wells.csv", dtype={"sample": str, "plate": str, "drug": str, "dose": str})
        FG = npy("plate_scale_gene")
        W2 = npy("W2")
        drugw = ~w["is_dmso"].astype(bool).to_numpy()
        rel = drugw & ~is_true(w["unreliable_plate"]).to_numpy()
        c = np.nanmedian(W2[rel], axis=0)
        gid = w["plate_scale_group_id"].to_numpy(dtype=int)
        name = {int(i): str(w.loc[gid == i, "plate_scale_group"].iloc[0]) for i in np.unique(gid) if i >= 0}
        fac = {int(i): float(w.loc[gid == i, "plate_scale"].iloc[0]) for i in name}
        mad = {i: 1.4826 * np.nanmedian(np.abs(W2[drugw & (gid == i)] - c), axis=0) for i in name}
        unrel_p = set(w.loc[is_true(w["unreliable_plate"]), "plate"])
        worst, n_wide, n_bad = 0.0, 0, 0
        for i, nm in name.items():
            p, d = nm.split(" ", 1)
            peers = [j for j, m in name.items() if m.split(" ", 1)[1] == d and m.split(" ", 1)[0] != p
                     and m.split(" ", 1)[0] not in unrel_p]
            if peers:
                ref = np.nanmedian(np.vstack([mad[j] for j in peers]), axis=0)
                ratio = mad[i] / np.where(ref > 0, ref, np.nan)
                want = np.where(np.isfinite(ratio), np.maximum(fac[i], ratio / 1.3), fac[i])
            else:
                want = np.full(FG.shape[1], fac[i])
            dev = np.abs(FG[i] - want)
            worst = max(worst, float(np.nanmax(dev)))
            n_bad += int((dev > 1e-3).sum())
            n_wide += int((FG[i] > fac[i] + 1e-6).sum())
        cal = os.path.join(ang, "quality", "calibration_by_plate_gene.csv")
        has = os.path.exists(cal) and {"MTAP", "PSMD10"} <= set(pd.read_csv(cal)["gene"].astype(str))
        return n_bad == 0 and n_wide > 0 and has, (
            f"plate_scale_gene.npy {FG.shape}: {n_wide} group x gene values widened beyond their group; values off "
            f"the definition: {n_bad} (max |diff| {worst:.2g}); quality/calibration_by_plate_gene.csv with MTAP and "
            f"PSMD10: {has}")
    ctx.check("v3: per-gene plate factors (plate_scale_gene.npy) = max(group factor, the gene's own spread ratio / "
              "1.3), recomputed from W2; per-gene calibration rows in the quality angle", gene_factors)

    def replicate_units():
        js = read_json(os.path.join(ang, "quality", "summary.json"))
        by = js.get("replicate_median_r_by_pair_type", {})
        t = csv("angles/quality/replicates.csv", dtype={"drug": str, "dose": str})
        bad = [k for k, v in by.items() if not isinstance(v, dict) or "drug_doses" not in v or "drugs" not in v]
        nd = {k: int(v.get("drug_doses", -1)) for k, v in by.items() if isinstance(v, dict)}
        rows = t.groupby("pair_type").size().to_dict()          # one row per drug-dose and pair type
        nc = is_true(t["position_not_correctable"]) if "position_not_correctable" in t else pd.Series(False, t.index)
        pos = {"same position, other plate", "different position"}
        # the two position types count a drug-dose once (pairs with a well without correction go to their own type)
        off = {k: (nd.get(k), n) for k, n in rows.items() if (nd.get(k) != n if k not in pos else nd.get(k, 0) > n)}
        if (nc & t["pair_type"].isin(pos)).any() and "position not correctable (either well)" not in nd:
            off["position not correctable (either well)"] = "missing"
        sc = js.get("plates_z_scaled_over_1.2", {})
        q = read_text(os.path.join(ang, "quality", "brief.md"))
        small = mentions(q, "each drug-dose counted once")
        return not bad and not off and noisy["plate"] in " ".join(sc) and len(sc) <= len(regular) and not small, (
            f"summary.json per pair type (drug-doses): {nd}; replicates.csv rows per type {rows}; mismatch "
            f"{off or 'none'}; scaled groups {sc}; brief says 'each drug-dose counted once': {not small}")
    ctx.check("v3: replicate agreement per pair type counts each drug-dose once (summary.json, brief); the scaled "
              "plate groups exclude joined control wells", replicate_units)

    def focus_nan():
        bad = {}
        for g in ("MTAP", "PSMD10"):
            t = csv(f"angles/focus_{g}/drug_effects.csv")
            nanfc = ~np.isfinite(pd.to_numeric(t["fold_change"], errors="coerce"))
            bad[g] = int((nanfc & (t["lines_measured"] > 0)).sum())
        return not any(bad.values()), (f"drug-doses without a fold change (no well with >= 5 lines) but with "
                                       f"per-line columns: {bad}")
    ctx.check("v3: focus per-line columns follow the 5-line rule (no lines_measured where the fold change is NaN)",
              focus_nan)

    def calib_measured():
        t = csv("angles/quality/calibration_by_plate.csv", dtype={"plate": str})
        w = csv("effects/wells.csv", dtype={"sample": str, "plate": str, "drug": str, "dose": str})
        _col, gi = genes()
        Z = npy("Z")
        drugw = ~w["is_dmso"].astype(bool).to_numpy()
        rc = v3["row_cell_loss"]
        r = t[(t["plate"] == rc["plate"]) & np.isclose(pd.to_numeric(t["dose"]), rc["conc"])].iloc[0]
        rows = np.flatnonzero(drugw & (w["plate"] == rc["plate"]).to_numpy() & np.isclose(w["conc"], rc["conc"]))
        z = np.abs(Z[np.ix_(rows, gi)])
        want = 100 * float((z > 1.96).sum()) / max(int(np.isfinite(z).sum()), 1)
        return abs(float(r["pct_abs_z_over_1.96"]) - want) < 0.01 and "pct_z_missing" in t, (
            f"{rc['plate']} {rc['conc']:g} uM (the row-loss plate): table {r['pct_abs_z_over_1.96']:.2f}% vs "
            f"{want:.2f}% of the measured z beyond 1.96 ({100 * float(np.mean(~np.isfinite(z))):.1f}% missing)")
    ctx.check("v3: calibration_by_plate.csv shares are of the measured z (a missing z is not 'within 1.96')",
              calib_measured)

    def briefs():
        q = read_text(os.path.join(ang, "quality", "brief.md"))
        n = int(read_json(os.path.join(ang, "quality", "summary.json"))["genes"])
        miss = mentions(q, noisy["plate"], unrel, "B11", "composition", "low cells (technical?)",
                        "plate-row cell shift", "position correction uncertain", "position not correctable",
                        "unreliable plate only", "noisy plate (z scaled)")
        if "~15,000" in q:
            miss.append("(still says ~15,000 genes)")
        if f"{n:,}" not in q and f" {n} " not in q:
            miss.append(f"(the gene count {n:,} is not filled in)")
        return not miss, f"quality/brief.md (METHODS / RULEBOOK) misses: {miss or 'nothing'}"
    ctx.check(f"v3: atlas METHODS / RULEBOOK from the data: {noisy['plate']} (factor), {unrel}, its DMSO in B11, the "
              "new flags, the gene count", briefs)
    ctx.check("v3: atlas briefs name the tahoe_atlas.py that wrote them, and every script path they name exists",
              lambda: brief_paths(glob.glob(os.path.join(ang, "*", "brief.md")), "tahoe_atlas.py"))

    def cell_loss_text():
        texts = {os.path.basename(os.path.dirname(b)): read_text(b) for b in glob.glob(os.path.join(ang, "*",
                                                                                                    "brief.md"))}
        flat = {k: " ".join(v.split()) for k, v in texts.items()}
        old = [k for k, v in flat.items() if "recovery artifact" in v or "do not rely on its expression" in v]
        need = mentions(texts.get("quality", ""), "non-monotonic dose response", "agree on cell loss",
                        "each drug-dose counted once")
        umi = [g for g in ("focus_MTAP", "focus_PSMD10") if "umi_per_cell_log2_vs_plate" not in flat.get(g, "")]
        return not old and not need and not umi, (f"briefs still calling low cells 'recovery artifacts': "
                                                  f"{old or 'none'}; quality brief misses {need or 'nothing'}; focus "
                                                  f"briefs without the sequencing-depth check: {umi or 'none'}")
    ctx.check("v3: briefs: 'low cells (technical?)' is 'not confirmed' (no 'recovery artifact'), top-dose 'toxic' is "
              "weak evidence, replicates per drug-dose, the focus briefs ask for sequencing depth", cell_loss_text)

    def angles_stamp():
        aj = os.path.join(ang, "complete.json")
        cj = os.path.join(fxd, "complete.json")
        js = read_json(aj) if os.path.exists(aj) else {}
        ok = js.get("effects_version") == METHOD_VERSION and js.get("failed") == [] and \
            os.path.getmtime(aj) >= os.path.getmtime(cj)
        return ok, f"angles/complete.json: {js or 'missing'}"
    ctx.check("v3: 'angles' writes angles/complete.json last (no failed angle), newer than effects/complete.json",
              angles_stamp)


def v3_units(ctx):
    """Method-v3 definitions on crafted inputs, in this process (the review of the real-data run): the 'toxic' rule
    in tahoe_mtap_gankyrin.flag_rows and tahoe_atlas.flags_for alike; one --unreliable-plates parser; the stale-brief
    guard reads quoted paths with spaces; the noise-RNA classes; one salt-form helper; the per-gene plate factor."""
    if no_v3(ctx, "unit checks"):
        return
    try:
        T, A = repo_modules()
    except BaseException as e:  # noqa: BLE001 (SystemExit of a guard included)
        ctx.record("v3: unit checks (tahoe_mtap_gankyrin / tahoe_atlas import)", False, f"{type(e).__name__}: {e}")
        return

    def toxic():
        # (drug, conc, cells, row, best well or NaN) -> expected; real-data cases of the review
        rows = [("Bortezomib", 0.5, -0.18, 0.02, np.nan, ""), ("Bortezomib", 5.0, -1.37, -0.59, np.nan, "toxic"),
                ("RowLost", 5.0, -1.45, -1.12, np.nan, "low cells (technical?)"),      # plate 2 row D: technical
                ("RowLost2", 5.0, -2.40, -1.12, np.nan, "toxic"),                      # beyond a lost row
                ("Selinexor", 5.0, -1.11, 0.17, 0.29, "low cells (technical?)"),       # one well -2.5, one +0.3
                ("Doxo", 5.0, -1.20, 0.04, -0.97, "toxic"),                            # both wells lost cells
                ("Docetaxel", 0.05, -1.67, 0.0, np.nan, "low cells (technical?)"), ("Docetaxel", 0.5, 0.28, 0.0,
                                                                                  np.nan, "")]
        t = pd.DataFrame(rows, columns=["drug", "conc", "cells_log2_vs_plate", "row_cells_log2",
                                        "cells_log2_best_well", "want"])
        tf = [("toxic" if "toxic" in flagset(f) else "low cells (technical?)" if "low cells (technical?)" in
               flagset(f) else "") for f in T.flag_rows(t.drop(columns="want"))]
        a = t.drop(columns="want").copy()
        a["cells_log2_best_higher_dose"] = [a.loc[(a["drug"] == d) & (a["conc"] > c), "cells_log2_vs_plate"].max()
                                            for d, c in zip(a["drug"], a["conc"])]
        af = [("toxic" if "toxic" in flagset(f) else "low cells (technical?)" if "low cells (technical?)" in
               flagset(f) else "") for f in (A.flags_for(r) for r in a.to_dict("records"))]
        bad = [f"{d} {c:g}: T '{x}', atlas '{y}', want '{w}'" for d, c, x, y, w in
               zip(t["drug"], t["conc"], tf, af, t["want"]) if not x == y == w]
        return not bad, f"{len(t)} crafted drug-doses; wrong: {bad or 'none'}"
    ctx.check("v3: unit: 'toxic' (5 uM loss beside toxic neighbours stays toxic; a lost row or a replicate well that "
              "kept its cells reads 'low cells (technical?)'), identical in both scripts", toxic)

    def parser():
        plates = ["plate1", "plate2", "plate13"]
        sm = pd.DataFrame({"plate": plates})
        out = {sp: (T.unreliable_plates(sm, sp), A.unreliable_plates(sp, plates))
               for sp in (None, "", "Plate13", "PLATE13", "13", "none", "no", "plate13, plate2")}
        want = {None: ["plate13"], "": ["plate13"], "Plate13": ["plate13"], "PLATE13": ["plate13"], "13": ["plate13"],
                "none": [], "no": [], "plate13, plate2": ["plate2", "plate13"]}
        bad = {k: v for k, v in out.items() if not v[0] == v[1] == want[k]}
        return not bad, f"--unreliable-plates T / atlas disagree or wrong: {bad or 'none'}"
    ctx.check("v3: unit: one --unreliable-plates parser (any case, numbers, '' = default, none / no)", parser)

    def stale_guard():
        d = fresh(os.path.join(ctx.scratch, "stale_brief"))
        gone = os.path.join(d, "my copy", "tahoe_atlas.py")
        b = os.path.join(d, "brief.md")
        with open(b, "w", encoding="utf-8") as fh:
            fh.write(f"- Look-up: `{PY} '{gone}' --out x lookup gene MTAP`\n")
        got = A.stale_brief_scripts([{"brief": b, "name": "quality"}])
        return gone in got, f"stale paths found: {got}"
    ctx.check("v3: unit: the agents' stale-brief guard finds a deleted quoted script path with a space", stale_guard)

    def noise_rna():
        rx = re.compile(NOISE_RNA)
        noise = ["H1-2", "H1-4", "H1-10", "RPL13AP5", "RPS4XP1", "RPL23AP49", "H2AC4", "H3C1", "RN7SK", "MTND1P23"]
        keep = ["MTAP", "HMOX1", "RPL22L1", "RPS6KA1", "RPS27A", "RPL36AL", "RPS4Y1", "H1FX", "HSPA1A"]
        bad = [g for g in noise if not (A.NOISE_RNA_RE.match(g) and rx.match(g))] + \
            [g for g in keep if A.NOISE_RNA_RE.match(g)]
        return not bad, f"misclassified: {bad or 'none'}"
    ctx.check("v3: unit: noise-RNA classes of RULEBOOK rule 7 (H1-* histones, RPL13AP5-style pseudogenes) "
              "and real genes kept", noise_rna)

    def salts():
        cases = {"Topotecan (hydrochloride)": "Topotecan", "(R)-Verapamil (hydrochloride)": "(R)-Verapamil",
                 "Dapagliflozin ((2S)-1,2-propanediol, hydrate)": "Dapagliflozin", "Erdafitinib ": "Erdafitinib",
                 "Trametinib (DMSO_TF solvate)": "Trametinib"}
        bad = {k: T.salt_base(k) for k, v in cases.items() if T.salt_base(k) != v}
        return not bad, f"salt_base wrong: {bad or 'none'}"
    ctx.check("v3: unit: one salt-form helper (nested brackets, no empty base)", salts)

    def feature_factor():
        f = T.feature_factors(np.array([1.0, 1.45, 1.45, 2.0]), np.array([np.nan, 1.22, 2.46, 0.5]))
        want = np.array([1.0, 1.45, 2.46 / 1.3, 2.0])
        return bool(np.allclose(f, want)), f"feature_factors {np.round(f, 3).tolist()} (want {np.round(want, 3)})"
    ctx.check("v3: unit: a gene's plate factor = max(group factor, own spread ratio / 1.3), never below the group's",
              feature_factor)


SCRIPT_PATH = re.compile(r"[\"']([^\"'\n]*?tahoe_(?:atlas|gene_panel|mtap_gankyrin)\.py)[\"']|"
                         r"((?:[A-Za-z]:)?[^\s`'\"()]*[/\\]tahoe_(?:atlas|gene_panel|mtap_gankyrin)\.py)")


def brief_paths(files, me):
    """Every brief names the script that wrote it (me), and every tahoe_*.py path it names exists."""
    no_me, gone = [], set()
    for f in files:
        t = read_text(f)
        if me not in t:
            no_me.append(os.path.basename(os.path.dirname(f)))
        for m in SCRIPT_PATH.findall(t):
            p = os.path.expanduser((m[0] or m[1]).strip())
            if os.path.isabs(p) and not os.path.exists(p):
                gone.add(p)
    return bool(files) and not no_me and not gone, (f"{len(files)} briefs; without {me}: {no_me or 'none'}; script "
                                                    f"paths that do not exist: {sorted(gone)[:3] or 'none'}")


def v3_mtap(ctx, R, atlas_ready):
    """tahoe_mtap_gankyrin.py (the corrected method T): version, flags, unreliable plate, composition."""
    if no_v3(ctx, "tahoe_mtap_gankyrin.py checks"):
        return
    gt, v3 = ctx.gt, ctx.gt["method_v3"]
    ctx.check("v3: tahoe_mtap_gankyrin.METHOD_VERSION 3",
              lambda: (repo_int("tahoe_mtap_gankyrin.py", "METHOD_VERSION") == METHOD_VERSION,
                       f"METHOD_VERSION {repo_int('tahoe_mtap_gankyrin.py', 'METHOD_VERSION')}"))

    def tab():
        t = pd.read_csv(os.path.join(R, "MTAP_drug_effects_by_dose.csv"))
        t["flags"] = t["flags"].fillna("").astype(str)
        return t
    ctx.check("v3: MTAP_drug_effects_by_dose.csv: " + V3_TABLE_FLAGS, lambda: table_flags(gt, tab()))
    ctx.check("v3: MTAP_drug_effects_by_dose.csv: drug-doses with a plate13 well count only their reliable wells "
              "(n_plates)", lambda: reliable_counts(gt, tab()))
    ctx.check("v3: MTAP_drug_effects_by_dose.csv: " + TOXIC_CHECK, lambda: toxic_rules(gt, tab()))
    ctx.check("v3: MTAP_drug_effects_by_dose.csv: the drug-doses with a well on the noisy plate 'noisy plate (z "
              "scaled)', plate_scale > 1.2", lambda: noisy_rows(gt, tab()))

    def composition():
        s = read_text(os.path.join(R, "summary.txt"))
        c = v3["composition"]
        f = flag_map(tab()).get(dkey(c["drug"], 5.0), set())
        said = "composition normalisation not applied" in s
        if atlas_ready:
            return not said and "composition shift" in f, (f"atlas ready when it ran: normalisation applied "
                                                           f"(summary says 'not applied': {said}); {c['drug']} 5 uM "
                                                           f"flags {sorted(f)}")
        return said, f"no atlas when it ran: summary.txt says 'composition normalisation not applied': {said}"
    ctx.check("v3: composition normalisation from <data>/atlas (or summary.txt says it was not applied)", composition)


V3_TABLE_FLAGS = ("the reference drug 0.05 uM 'position not correctable', the plate13-only drug-doses 'unreliable "
                  "plate only'; no 'plate DMSO offset' flag (the column kept)")


def table_flags(gt, t):
    """V3_TABLE_FLAGS on a per drug-dose gene table (T or the panel)."""
    v3 = gt["method_v3"]
    F = flag_map(t)
    u = v3["uncorrectable"]
    got = {f"{u['drug']} {u['conc']:g} not correctable": "position not correctable" in
           F.get(dkey(u["drug"], u["conc"]), set())}
    got.update({f"{x['drug']} {x['conc']:g} unreliable only": "unreliable plate only" in
                F.get(dkey(x["drug"], x["conc"]), set()) for x in v3["unreliable_plate"]["only_there"]})
    n_off = sum("plate DMSO offset" in f for f in F.values())
    return all(got.values()) and n_off == 0 and "plate_dmso_offset" in t, \
        f"{got}; 'plate DMSO offset' flags: {n_off}; plate_dmso_offset column: {'plate_dmso_offset' in t}"


def reliable_counts(gt, t):
    W = planted_wells(gt)
    bad, n = [], 0
    for r in t.itertuples():
        e = W.get(dkey(r.drug, r.conc))
        if e and e["reliable"] and e["unreliable"]:
            n += 1
            if int(r.n_plates) != len(e["reliable"]):
                bad.append(f"{r.drug} {r.conc:g}: {r.n_plates} wells (reliable {len(e['reliable'])})")
    return n >= 50 and not bad, f"{n} drug-doses with a plate13 well; counted wrong: {bad[:4] or 'none'}"


def noisy_rows(gt, t):
    """The drug-doses whose used wells include one on the noisy plate at 5 uM are scaled (> 1.2) and flagged
    'noisy plate (z scaled)'; those without a well there are not (the reference drug's 0.05 uM, with one of its six
    wells there, is left out: ~1.17)."""
    noisy = gt["method_v3"]["noisy_plate"]["plate"]
    lay = {w["sample"]: w for w in gt["layout"]}
    W = planted_wells(gt)
    ref = dkey(gt["method_v3"]["uncorrectable"]["drug"], gt["method_v3"]["uncorrectable"]["conc"])
    miss, extra, n = [], [], 0
    for r in t.itertuples():
        k = dkey(r.drug, r.conc)
        e = W.get(k)
        if e is None or k == ref:
            continue
        on = any(lay[s]["plate"] == noisy for s in used_wells(e))
        got = "noisy plate (z scaled)" in flagset(r.flags) and r.plate_scale > 1.2
        n += on
        if on and not got:
            miss.append(f"{r.drug} {r.conc:g}")
        if got and not on:
            extra.append(f"{r.drug} {r.conc:g}")
    return n >= 50 and len(miss) <= 0.05 * n and not extra, (f"{n - len(miss)} of {n} drug-doses with a {noisy} well "
                                                              f"scaled and flagged; not: {miss[:3] or 'none'}; "
                                                              f"flagged without one: {extra[:3] or 'none'}")


def v3_panel(ctx, out):
    """tahoe_gene_panel.py after 'all' (with the earlier run): version, atlas agreement and imports, traps a-f,
    p53 pattern, re-expression gating, summary and briefs (spec sections 2-9)."""
    if no_v3(ctx, "gene panel checks"):
        return
    gt, v3 = ctx.gt, ctx.gt["method_v3"]
    R = os.path.join(out, "results")
    ang = os.path.join(out, "angles")
    noisy, unrel = v3["noisy_plate"]["plate"], v3["unreliable_plate"]["plate"]
    cache = {}

    def csv(name):
        if name not in cache:
            t = pd.read_csv(os.path.join(R, name))
            if "flags" in t:
                t["flags"] = t["flags"].fillna("").astype(str)
            cache[name] = t
        return cache[name]

    ctx.check("v3: results/run_info.json method_version 3", lambda: (
        read_json(os.path.join(R, "run_info.json")).get("method_version") == METHOD_VERSION,
        f"run_info.json: {read_json(os.path.join(R, 'run_info.json'))}"))
    ready = atlas_v3_ready(ctx)
    if not ready:
        ctx.skip("v3: atlas vs panel (MTAP/PSMD10 agreement, imported plate factors and composition shifts)",
                 f"no v3 atlas in {ctx.A}: run the atlas stage first")
    else:
        for g in ("MTAP", "PSMD10"):
            ctx.check(f"v3: atlas focus_{g}/drug_effects.csv and panel {g}_drug_effects_by_dose.csv agree (fold "
                      "change, z, calls, shared flags)",
                      lambda g=g: agreement(ctx, csv(f"{g}_drug_effects_by_dose.csv"), g))

        def factors():
            a = pd.read_csv(os.path.join(ctx.A, "effects", "drugdose.csv"))[["drug", "conc", "plate_scale"]]
            p = csv("MTAP_drug_effects_by_dose.csv")
            m = a.merge(p[["drug", "conc", "plate_scale"]], on=["drug", "conc"], suffixes=("_atlas", "_panel"))
            d = (m["plate_scale_atlas"] - m["plate_scale_panel"]).abs()
            return len(m) == len(p) and float(d.max()) <= 1e-6, (
                f"{len(m)} drug-doses: max |plate_scale atlas - panel| {float(d.max()):.2g}")
        ctx.check("v3: the panel uses the atlas's plate factors (plate_scale equal)", factors)

        def comp():
            c = v3["composition"]
            we = pd.read_csv(os.path.join(R, "well_effects.csv.gz"), dtype={"sample": str})
            aw = pd.read_csv(os.path.join(ctx.A, "effects", "wells.csv"), dtype={"sample": str})
            m = we[["sample", "composition_shift_log2"]].merge(aw[["sample", "composition_shift_log2"]], on="sample",
                                                               suffixes=("_panel", "_atlas"))
            d = float((m["composition_shift_log2_panel"] - m["composition_shift_log2_atlas"]).abs().max())
            f = flag_map(csv("drug_context_by_dose.csv")).get(dkey(c["drug"], 5.0), set())
            pg = csv("panel_genes.csv")
            vals, five = [], []
            for g in pg.loc[pg["status"].astype(str) == "testable", "gene"]:
                path = os.path.join(R, f"{g}_drug_effects_by_dose.csv")
                if os.path.exists(path):
                    t = pd.read_csv(path)
                    r = t[(t["drug"] == c["drug"]) & np.isclose(t["conc"], 5.0)]
                    if len(r):
                        vals.append(float(r["log2FC_corrected"].iloc[0]))
                    five.append(t.loc[np.isclose(t["conc"], 5.0), ["drug", "log2FC_corrected"]])
            med = float(np.median(np.abs(vals))) if vals else np.nan
            centre = float(np.median(vals)) if vals else np.nan
            # the noise floor: the same median |log2FC| of the other 5 uM drug-doses (their wells, like this one's,
            # sit on plate5 and the noisy plate6, so ~0.14 rather than the ~0.07 of the lower doses)
            f5 = pd.concat(five) if five else pd.DataFrame(columns=["drug", "log2FC_corrected"])
            f5 = f5[f5["drug"] != c["drug"]]
            floor = float(f5.groupby("drug")["log2FC_corrected"].apply(lambda x: np.median(np.abs(x))).median())
            ok = len(m) >= 0.9 * len(aw) and d <= 0.02 and "composition shift" in f and abs(centre) < 0.1 and \
                med <= max(0.15, 1.3 * floor)
            return ok, (
                f"{len(m)} wells: max |shift panel - atlas| {d:.3g}; {c['drug']} 5 uM flags {sorted(f)}; over "
                f"{len(vals)} testable panel genes its median log2FC {centre:+.2f} and median |log2FC| {med:.2f} "
                f"(other 5 uM drug-doses {floor:.2f}; before the fix ~{c['expected_shift_log2_by_dose']['5.0']:+.2f})")
        ctx.check("v3: the panel imports the atlas composition shift (well_effects.csv.gz); the composition-shift "
                  "drug's panel genes ~0, flagged", comp)

    def coloc():
        c = v3["co_location"]
        t = csv("TFRC_drug_effects_by_dose.csv")
        y = t[t["drug"] == c["inert"]]
        x5 = t[(t["drug"] == c["strong"]) & np.isclose(t["conc"], 5.0)].iloc[0]
        # its own well noise is ~0.09 log2 per drug-dose: each dose within 0.3, their mean within 0.15
        yok = len(y) == 3 and bool((y["log2FC_corrected"].abs() < 0.3).all()) and \
            abs(float(y["log2FC_corrected"].mean())) < 0.15 and \
            all("position correction uncertain" in flagset(f) for f in y["flags"]) and \
            bool((y["call"].fillna("") == "").all())
        xok = x5["log2FC_corrected"] <= -0.6 and x5["call"] == "down"     # (uncertain too: see v3_atlas coloc)
        by_dose = ", ".join(f"{v:+.2f}" for v in y["log2FC_corrected"])
        return yok and xok, (f"{c['inert']} TFRC log2FC by dose {by_dose} "
                             f"(before the fix ~+{c['inert_log2_before_fix']['TFRC']:.2f}), flags {list(y['flags'])}, "
                             f"calls {list(y['call'].fillna(''))}; {c['strong']} 5 uM {x5['log2FC_corrected']:+.2f}, "
                             f"call '{x5['call']}', flags '{x5['flags']}'")
    ctx.check("v3: TFRC: the co-located inert drug ~0 and 'position correction uncertain' (no call); the strong "
              "drug's TFRC decrease kept", coloc)
    for g in ("MTAP", "TFRC"):
        ctx.check(f"v3: panel {g}_drug_effects_by_dose.csv: " + V3_TABLE_FLAGS,
                  lambda g=g: table_flags(gt, csv(f"{g}_drug_effects_by_dose.csv")))
    ctx.check("v3: panel MTAP_drug_effects_by_dose.csv: drug-doses with a plate13 well count only their reliable "
              "wells (n_plates)", lambda: reliable_counts(gt, csv("MTAP_drug_effects_by_dose.csv")))
    ctx.check("v3: panel MTAP_drug_effects_by_dose.csv: the 5 uM drug-doses 'noisy plate (z scaled)'",
              lambda: noisy_rows(gt, csv("MTAP_drug_effects_by_dose.csv")))
    ctx.check("v3: panel drug_context_by_dose.csv: " + TOXIC_CHECK,
              lambda: toxic_rules(gt, csv("drug_context_by_dose.csv")))

    def cell_cycle():
        bad, n = cell_cycle_rule(csv("drug_context_by_dose.csv"), "S_PHASE_shift_log2", "G2M_PHASE_shift_log2",
                                 "S_PHASE_z", "G2M_PHASE_z")
        return len(bad) <= 2, f"{n} drug-doses meet the rule; flag disagrees: " + \
            (fmt_top(bad, ["drug", "conc", "flags"], 4) or "none")
    ctx.check("v3: panel 'cell-cycle shift' = |S or G2M| > 0.5, or > 0.25 with |z| >= 4 (drug_context_by_dose.csv)",
              cell_cycle)

    def no_offset_flag():
        bad = []
        for f in sorted(glob.glob(os.path.join(R, "*_by_dose.csv"))):
            t = pd.read_csv(f, usecols=lambda c: c == "flags")
            if "flags" in t and t["flags"].map(lambda x: "plate DMSO offset" in flagset(x)).any():
                bad.append(os.path.basename(f))
        return not bad, f"tables with a 'plate DMSO offset' flag: {bad[:4] or 'none'}"
    ctx.check("v3: no 'plate DMSO offset' flag in any panel table (plate_dmso_offsets.csv keeps the offsets)",
              no_offset_flag)

    def p53_pattern():
        t = csv("p53_wt_vs_altered.csv")
        ok_ = t["wt_mean_log2"].notna() & t["all_lines_P53_ACTIVITY_z"].notna()
        t = t[ok_]
        want = np.where((t["wt_mean_log2"] >= math.log2(1.2)) & (t["all_lines_P53_ACTIVITY_z"] > 0), "WT induction",
                        "relative (altered lines fall)")
        bad = t[t["pattern"].astype(str).to_numpy() != want]
        dd3 = {d: str(t.loc[(t["drug"] == d) & np.isclose(t["conc"], 5.0), "pattern"].iloc[0])
               for d in ("Doxorubicin (hydrochloride)", "Topotecan (hydrochloride)", "5-Fluorouracil")}
        s = read_text(os.path.join(R, "summary.txt"))
        ok = bad.empty and all(v == "WT induction" for v in dd3.values()) and "WT induction" in s
        return ok, (f"rule broken for {len(bad)} rows; DNA-damage drugs at 5 uM: {dd3}; summary.txt prints the "
                    f"pattern: {'WT induction' in s}")
    ctx.check("v3: p53_wt_vs_altered.csv 'pattern' (WT induction / relative (altered lines fall)), in summary.txt",
              p53_pattern)

    def reexpr():
        t = csv("reexpression_in_silenced_lines.csv")
        rd = t["reading"].fillna("").astype(str)
        re_ = t[rd.str.startswith("re-expression")]
        bad = re_[pd.to_numeric(re_["n_lines_up"], errors="coerce").fillna(0) < 2]
        return not re_.empty and bad.empty, (f"{len(re_)} 're-expression' readings; with < 2 lines up: "
                                             f"{fmt_top(bad, ['gene', 'drug', 'conc', 'n_lines_up'], 3) or 'none'}")
    ctx.check("v3: re-expression readings need >= 2 lost lines up", reexpr)

    def ambient_floor():
        t = csv("reexpression_in_silenced_lines.csv")
        rd = t["reading"].fillna("").astype(str)
        z = pd.to_numeric(t["z_corrected"], errors="coerce")
        c1 = t[(t["gene"] == "CASP1") & (z >= 3)]
        c1_ok = (rd[c1.index] == "lost lines read ambient only: not interpretable").all()
        amb = (pd.to_numeric(c1["lost_lines_median_cpm_dmso"], errors="coerce") <=
               1.5 * pd.to_numeric(c1["ambient_cpm"], errors="coerce")).all()
        g = t[(t["gene"] == "GSDME") & (t["drug"] == "Decitabine") & np.isclose(t["conc"], 5.0)]
        g_ok = len(g) == 1 and rd[g.index[0]].startswith("re-expression")
        return len(c1) > 0 and c1_ok and amb and g_ok, (
            f"CASP1 (planted absent, no deleted line) rows with z >= 3: {len(c1)}, readings "
            f"{sorted(set(rd[c1.index]))} (lost lines at <= 1.5x ambient: {amb}); GSDME (silenced, ~2x ambient) "
            f"Decitabine 5 uM: {rd[g.index[0]] if len(g) else 'missing'}")
    ctx.check("v3: re-expression: lost lines at the ambient floor read 'ambient only' without deleted lines too "
              "(CASP1); GSDME Decitabine 5 uM stays 're-expression'", ambient_floor)

    def toxic_tables():
        out = [toxic_rule_check(csv(n), n) for n in ("drug_context_by_dose.csv", "MTAP_drug_effects_by_dose.csv")]
        return all(o[0] for o in out), " | ".join(o[1] for o in out)
    ctx.check("v3: panel 'toxic' follows the rule (drug_context_by_dose.csv, MTAP_drug_effects_by_dose.csv)",
              toxic_tables)

    def gene_factors():
        t = csv("plate_scale_by_gene.csv")
        r = pd.to_numeric(t["spread_ratio"], errors="coerce")
        want = np.where(np.isfinite(r), np.maximum(t["group_factor"], r / 1.3), t["group_factor"])
        bad = int((np.abs(t["factor"] - want) > 1e-6).sum())
        ps = csv("plate_scale.csv").set_index("group")["factor"]
        gbad = int((np.abs(t["group_factor"] - t["group"].map(ps)) > 1e-6).sum())
        agree = "not compared (no v3 atlas)"
        if atlas_v3_ready(ctx):
            w = pd.read_csv(os.path.join(ctx.A, "effects", "wells.csv"), dtype={"plate": str, "dose": str})
            g = pd.read_csv(os.path.join(ctx.A, "effects", "genes.csv"))
            FG = np.load(os.path.join(ctx.A, "effects", "plate_scale_gene.npy"))
            ids = w[w["plate_scale_group_id"] >= 0].drop_duplicates("plate_scale_group_id")
            gid = {str(a).replace(" ", "|"): int(b)
                   for a, b in zip(ids["plate_scale_group"], ids["plate_scale_group_id"])}
            col = dict(zip(g["symbol"].astype(str), g["col"].astype(int)))
            d = [abs(float(f) - float(FG[gid[G], col[ft]])) for ft, G, f in zip(t["feature"], t["group"], t["factor"])
                 if ft in ("MTAP", "PSMD10") and G in gid and ft in col]
            agree = f"MTAP / PSMD10 vs the atlas's plate_scale_gene.npy: {len(d)} values, max |diff| " \
                    f"{max(d) if d else float('nan'):.2g}"
            if not d or max(d) > 1e-4:
                bad += 1
        wide = int((t["factor"] > t["group_factor"] + 1e-9).sum())
        return bad == 0 and gbad == 0 and wide > 0, (
            f"{len(t)} feature x group rows, {wide} widened beyond the group; off the definition: {bad}; group factor "
            f"not the plate_scale.csv one: {gbad}; {agree}")
    ctx.check("v3: panel plate_scale_by_gene.csv: factor = max(group factor, spread_ratio / 1.3); MTAP / PSMD10 "
              "equal to the atlas's", gene_factors)

    def typical_lines():
        # a gene measured in 6 lines, 2 of them usable in few wells (real CASP5: NCI-H596 2% and NCI-H2122 19% of
        # wells): its value comes from the lines a typical well has, not from wells holding 5 of the 6
        T, _A = repo_modules()
        keep_min, T.MIN_CELLS = T.MIN_CELLS, 10             # as the panel run (--min-cells 10)
        wl = pd.read_parquet(os.path.join(out, "well_line.parquet"))
        wl["sample"], wl["cell_line_id"] = wl["sample"].astype(str), wl["cell_line_id"].astype(str)
        sm = pd.read_csv(os.path.join(out, "sample_map.csv"), dtype={"sample": str, "plate": str, "drug": str})
        sm["is_dmso"] = sm["is_dmso"].astype(bool)
        sm["well"] = sm["well"].fillna("")
        sm = T.mark_unreliable(sm, [unrel])
        lines = sorted(wl["cell_line_id"].unique())
        keep6, sparse = lines[:6], lines[:2]
        rng = np.random.default_rng(0)
        wells = sm["sample"].unique()
        for ln, frac in zip(sparse, (0.02, 0.19)):
            okw = set(rng.choice(wells, int(frac * len(wells)), replace=False))
            wl.loc[(wl["cell_line_id"] == ln) & ~wl["sample"].isin(okw), "n_cells"] = 0
        dw = set(sm.loc[~sm["is_dmso"], "sample"])

        def share(gene, excl):
            M = T.Method(sm)
            W1 = M.cache[M.add(wl, gene, excl)]["W"]["W1"]
            return 100 * W1[W1.index.isin(dw)].notna().sum() / len(dw)
        try:
            a = share("CASP4", [x for x in lines if x not in keep6])
            b = share("MTAP", [])
        finally:
            T.MIN_CELLS = keep_min
        return a >= 90 and b >= 90, (f"CASP4 restricted to 6 lines (2 sparse): {a:.1f}% of drug wells keep a value "
                                     f"(the 5-line rule on any-well line count gave ~10%); MTAP (all lines): {b:.1f}%")
    ctx.check("v3: a gene measured in < 5 lines in a typical well keeps a value in nearly every well (6 lines, 2 "
              "sparse)", typical_lines)

    def pos_wells():
        if not atlas_v3_ready(ctx):
            return True, "no v3 atlas: not compared"
        a = pd.read_csv(os.path.join(ctx.A, "angles", "focus_MTAP", "drug_effects.csv"))
        m = a.merge(csv("MTAP_drug_effects_by_dose.csv"), on=["drug", "conc"], suffixes=("_a", "_p"))
        d = (m["position_wells_used_a"] - m["position_wells_used_p"]).abs()
        return float(d.max()) < 1e-6, (f"{len(m)} drug-doses: max |position_wells_used atlas - panel| "
                                       f"{float(d.max()):.3g}")
    ctx.check("v3: position_wells_used means the same in the atlas and the panel (mean over the used wells)", pos_wells)

    def summary():
        s = read_text(os.path.join(R, "summary.txt"))
        h4 = next((x for x in s.splitlines() if x.startswith("4. ")), "")
        pc = csv("positive_controls.csv")
        ro = [str(v) for v in pc.loc[pc["expectation"].astype(str).str.contains("GSDME", regex=False), "readout"]
              .dropna()] if "readout" in pc else []
        miss = [r for r in ro if r[:40] not in s]
        return "dose-level" in h4.lower() and bool(ro) and not miss, (f"section 4 header: '{h4.strip()}'; GSDME "
                                                                      f"readout printed: {not miss and bool(ro)}")
    ctx.check("v3: summary.txt: section 4 header says the calls use the dose-level FDR; positive controls print their "
              "readout", summary)

    def shared_expected():
        s = " ".join(read_text(os.path.join(R, "summary.txt")).split())
        src = "the atlas's genome-wide significant genes" if ready else "genes with a call at any dose"
        ok = "matched for drug activity" in s and (not ready or src in s)
        i = s.find("matched for drug activity")
        return ok, (s[max(0, i - 120): i + 120] if i >= 0 else "no 'matched for drug activity' in summary.txt")
    ctx.check("v3: crosslinks: the shared-drug count is compared with an expectation matched for drug activity "
              "(the atlas's significant genes when the atlas is there)", shared_expected)

    def well_effects():
        we = pd.read_csv(os.path.join(R, "well_effects.csv.gz"), dtype={"sample": str, "plate": str})
        lead = ["sample", "plate", "well", "drug", "conc", "unreliable_plate", "plate_scale", "composition_shift_log2"]
        mt = [c for c in we.columns[len(lead):] if c.upper().startswith("MTAP")]
        unr = set(we.loc[is_true(we["unreliable_plate"]), "plate"])
        ok = list(we.columns[:len(lead)]) == lead and any("z" in c.lower() for c in mt) and \
            any("log2fc" in c.lower() or "w2" in c.lower() for c in mt) and unr == {unrel} and \
            {"MTAP_log2FC_uncorrected", "MTAP_position_state"} <= set(we.columns) and \
            set(pd.unique(we["TFRC_position_state"].dropna())) >= {0, 1}
        return ok, (f"columns {list(we.columns[:len(lead) + 2])}...; MTAP columns {mt}; unreliable_plate rows on "
                    f"{sorted(unr)}")
    ctx.check("v3: results/well_effects.csv.gz: per well sample ... composition_shift_log2, then log2FC and z per gene "
              "(+ the uncorrected value and the position state: TFRC has corrected and uncertain wells)", well_effects)

    def briefs():
        names = [a for a in os.listdir(ang) if os.path.exists(os.path.join(ang, a, "brief.md"))]
        txt = {a: read_text(os.path.join(ang, a, "brief.md")) for a in names}
        miss = {a: mentions(t, noisy, unrel, "B11", "low cells (technical?)", "composition") for a, t in txt.items()}
        miss["napepld_trim72"] = miss.get("napepld_trim72", []) + mentions(txt.get("napepld_trim72", ""),
                                                                           "MG53 protein")
        miss["pyroptosis"] = miss.get("pyroptosis", []) + mentions(txt.get("pyroptosis", ""),
                                                                   *gt["groups"]["il1b_expressing"])
        miss = {a: m for a, m in miss.items() if m}
        return not miss, f"missing: {miss or 'nothing'}"
    ctx.check(f"v3: panel briefs (PANEL_METHODS / RULEBOOK from the data: {noisy}, {unrel}, B11, the new flags; "
              "TRIM72 -> MG53 protein; the IL1B lines)", briefs)
    def panel_text():
        texts = {os.path.basename(os.path.dirname(b)): " ".join(read_text(b).split())
                 for b in glob.glob(os.path.join(ang, "*", "brief.md"))}
        old = [k for k, v in texts.items() if "do not rely on its expression changes" in v or "<CELL_REP>" in v]
        rep = [k for k, v in texts.items() if "Rules for interpreting" in v and "agree on cell loss" not in v]
        x = texts.get("crosslinks", "")
        title = x.startswith("# Angle: Cross-links to MTAP / Gankyrin") or "Cross-links to MTAP / Gankyrin" in x[:200]
        return not old and not rep and title, (
            f"briefs telling agents to ignore low-cell drug-doses (or an unfilled <CELL_REP>): {old or 'none'}; "
            f"without the cell-loss replication sentence: {rep or 'none'}; crosslinks heading: {x[:70]!r}")
    ctx.check("v3: panel briefs: 'low cells (technical?)' not dismissed, how well wells agree on cell loss (from "
              "the data); the crosslinks heading names no earlier analysis", panel_text)
    ctx.check("v3: panel briefs name the tahoe_gene_panel.py that wrote them, and every script path they name exists",
              lambda: brief_paths(glob.glob(os.path.join(ang, "*", "brief.md")), "tahoe_gene_panel.py"))


def agreement(ctx, p, gene):
    """Atlas focus vs panel on EVERY drug-dose: one definition in both (tahoe_mtap_gankyrin.py leaves out a well with
    < 5 measured lines, MIN_LINES, as the atlas does, so toxic wells and the plate-row loss are no exception). A
    drug-dose without a value (every used well too thin) must be missing in both."""
    a = pd.read_csv(os.path.join(ctx.A, "angles", f"focus_{gene}", "drug_effects.csv"))
    m = a.merge(p, on=["drug", "conc"], suffixes=("_a", "_p"))
    la, lp = np.log2(m["fold_change_a"]), np.log2(m["fold_change_p"])
    na, np_ = ~np.isfinite(la), ~np.isfinite(lp)
    k = m[~na & ~np_]
    la, lp = la[~na & ~np_], lp[~na & ~np_]
    dfc = (la - lp).abs()
    dz = (k["z"] - k["z_corrected"]).abs()
    lfc = math.log2(1.2)
    call_a = np.where((k["q_up"] < 0.1) & (la >= lfc) & (k["pct_lines_up"] >= 60), "up",
                      np.where((k["q_down"] < 0.1) & (la <= -lfc) & (k["pct_lines_up"] <= 40), "down", ""))
    calls = int((call_a != k["call"].fillna("").to_numpy()).sum())
    fm = [(d, c, sorted(x), sorted(y)) for d, c, f1, f2 in zip(m["drug"], m["conc"], m["flags_a"], m["flags_p"])
          for x, y in [(flagset(f1) & set(SHARED_FLAGS), flagset(f2) & set(SHARED_FLAGS))] if x != y]
    pz = float((dz <= 0.05 + 0.03 * k["z_corrected"].abs()).mean())
    pf = float((dfc <= 1e-3).mean())
    ok = len(m) == len(a) == len(p) and (na == np_).all() and len(k) >= 0.9 * len(m) and pf >= 0.98 and \
        float(dfc.max()) <= 0.02 and pz >= 0.95 and calls <= 2 and len(fm) <= 0.03 * len(m)
    return ok, (f"{len(m)} of {len(a)}/{len(p)} drug-doses matched, {len(k)} with a value in both (no value in "
                f"atlas / panel only: {int((na & ~np_).sum())} / {int((np_ & ~na).sum())}): log2FC equal (1e-3) for "
                f"{100 * pf:.0f}% (max diff {float(dfc.max()):.3f}), z within 3% for {100 * pz:.0f}%, calls differ "
                f"{calls}, shared flags differ {len(fm)} {fm[:2] if fm else ''}")


def v3_noprior(ctx, out):
    """The panel's second analyze ran with --prior none: crosslinks without an earlier run (spec section 8)."""
    if no_v3(ctx, "no-prior crosslinks"):
        return
    R, ang = os.path.join(out, "results"), os.path.join(out, "angles")

    def noprior():
        b = read_text(os.path.join(ang, "crosslinks", "brief.md"))
        s = read_text(os.path.join(R, "summary.txt"))
        xl = pd.read_csv(os.path.join(R, "crosslinks.csv"))
        rep = xl[xl["category"] == "reproducibility"]
        bad = [x for x, cond in (("the crosslinks brief names prior/", "prior/" in b),
                                 ("the brief asks for reproducibility vs the earlier run",
                                  "reproducibility vs the earlier run" in b),
                                 ("'two runs' in summary.txt or the brief", "two runs" in s or "two runs" in b),
                                 ("summary.txt lacks \"this run's MTAP / PSMD10 lists\"",
                                  "this run's MTAP / PSMD10 lists" not in s),
                                 ("angles/crosslinks/prior exists", os.path.isdir(os.path.join(ang, "crosslinks",
                                                                                                "prior"))),
                                 ("crosslinks.csv compares with an earlier run",
                                  len(rep) != 1 or "not found" not in str(rep["reading"].iloc[0]))) if cond]
        return not bad, "; ".join(bad) or "no earlier run named anywhere; 'this run's MTAP / PSMD10 lists'"
    ctx.check("v3: --prior none: crosslinks brief and summary.txt speak of this run only (no prior/, no 'two runs')",
              noprior)


def v3_panel_guard(ctx, script):
    """The panel refuses a tahoe_mtap_gankyrin.py older than method v3 (a copy next to it with METHOD_VERSION 2, or
    without the constant as before v3)."""
    if no_v3(ctx, "panel version guard"):
        return
    d = fresh(os.path.join(ctx.scratch, "older_tahoe_mtap_gankyrin"))
    shutil.copy2(script, d)
    src = read_text(os.path.join(REPO, "tahoe_mtap_gankyrin.py"))
    with open(os.path.join(d, "tahoe_mtap_gankyrin.py"), "w", encoding="utf-8") as fh:
        fh.write(re.sub(r"^METHOD_VERSION\s*=.*$", "METHOD_VERSION = 2", src, flags=re.M))
    rc, text = ctx.run("older_T", [PY, os.path.join(d, os.path.basename(script)), "--help"])
    ctx.record("v3: tahoe_gene_panel.py stops next to a tahoe_mtap_gankyrin.py with METHOD_VERSION < 3",
               rc not in (0, "timeout") and "tahoe_mtap_gankyrin.py" in text,
               f"exit {rc}: {tail(text, 2)}")


def v3_outdated(ctx, base, panel_out):
    """tahoe_status.py: atlas effects stamped < 3 or panel results < 3 read 'done, but outdated', Next: tahoe run."""
    if no_v3(ctx, "tahoe_status outdated"):
        return
    status = os.path.join(REPO, "tahoe_status.py")
    cj = os.path.join(ctx.A, "effects", "complete.json")
    ri = os.path.join(panel_out, "results", "run_info.json")
    keep = {p: read_text(p) for p in (cj, ri) if os.path.exists(p)}
    times = {p: (os.stat(p).st_atime, os.stat(p).st_mtime) for p in keep}

    def put(p, obj):
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(obj, fh)

    def restore():
        for p in (cj, ri):
            if p in keep:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(keep[p])
                os.utime(p, times[p])       # readiness compares the stamps' times with the briefs'
            elif os.path.exists(p):
                os.remove(p)
    try:
        for label, path, obj in (("atlas", cj, {"version": METHOD_VERSION - 1}),
                                 ("panel", ri, {"method_version": METHOD_VERSION - 1})):
            restore()
            if os.path.exists(os.path.dirname(path)):
                old = read_json(path) if path in keep else {}
                put(path, {**old, **obj})
            rc, text = ctx.run(f"status_outdated_{label}", [PY, status, "status"] + base)
            rows = text.splitlines()
            row = next((r for r in rows if r.startswith("Atlas" if label == "atlas" else "Gene panel")), "")
            nxt = next((r for r in rows if r.startswith("Next:")), "")
            ok = rc == 0 and "outdated" in row and "tahoe run" in nxt
            ctx.record(f"v3: status: {label} stamped method {METHOD_VERSION - 1} reads 'done, but outdated', Next: "
                       "tahoe run", ok, f"{row.strip()} | {nxt.strip()}")
    finally:
        restore()


def v3_briefcheck(ctx, base):
    """'tahoe agents' preflight (tahoe_status.py briefcheck; spec 9): silent on briefs whose script paths exist; one
    line per missing script when a brief names a copy that was deleted. The agents themselves are not run."""
    if no_v3(ctx, "briefcheck"):
        return
    status = os.path.join(REPO, "tahoe_status.py")
    rc, text = ctx.run("briefcheck", [PY, status, "briefcheck", "--job", "atlas panel"] + base)
    ctx.record("v3: briefcheck: no missing script named in the smoke run's briefs", rc == 0 and not text.strip(),
               f"exit {rc}; output: {tail(text, 3) or 'none'}")
    b = os.path.join(ctx.A, "angles", "quality", "brief.md")
    if not os.path.exists(b):
        ctx.record("v3: briefcheck names a deleted copy of tahoe_atlas.py", False, f"{b} missing")
        return
    keep = read_text(b)
    gone = os.path.join(ctx.scratch, "deleted_copy", "tahoe_atlas.py")
    try:
        with open(b, "a", encoding="utf-8") as fh:
            fh.write(f"\n- Look-up: `{PY} {gone} lookup gene MTAP`\n")
        rc, text = ctx.run("briefcheck_missing", [PY, status, "briefcheck", "--job", "atlas"] + base)
        hit = [x.split("\t") for x in text.splitlines() if x.startswith("atlas\t")]
        ok = rc == 0 and any(len(h) >= 3 and h[1] == gone and "quality" in h[2] for h in hit)
        ctx.record("v3: briefcheck names a deleted copy of tahoe_atlas.py that a brief still names (the 'tahoe "
                   "agents' refusal)", ok, f"exit {rc}; output: {tail(text, 3) or 'none'}")
    finally:
        with open(b, "w", encoding="utf-8") as fh:
            fh.write(keep)


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
    warnings.filterwarnings("ignore", category=RuntimeWarning)       # all-NaN medians in the checks' numpy work
    want = [s.strip() for s in args.only.split(",") if s.strip()] or list(STAGES)
    unknown = [s for s in want if s not in STAGES]
    if unknown:
        sys.exit(f"unknown stage(s) {unknown}; choose from {list(STAGES)}")
    want = [s for s in STAGES if s in want]          # always in stage order: the atlas feeds mtap and the panel
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
