#!/usr/bin/env python3
"""test_direction.py - the direction stage (tahoemap/direction.py) against planted answers, and at full scale.

    python tests/test_direction.py [--src OUT --data DATA] [--work DIR] [--no-fixture] [--no-scale]
                                   [--scale-genes 4000,8000] [--keep]

0. Unit checks: drug_target counts one molecule under two names (the real Tahoe pairs) once; a level edge's
   'direction clear' allows for the edge having been selected because it is strong (simulated pairs).
1. Synthetic run. Copies a finished synthetic output (default: run_tests.py's, /tmp/tahoemap_test/out_seed0 and
   data_seed0; made with run_tests.py when missing), runs `python -m tahoemap.direction` on the copy in its own
   process and checks the answers make_synthetic_tahoe.py planted (ground_truth.json next to the data): TP53 -> most
   P53_ACTIVITY genes with the right sign and a grade; TP53 -> cells under the DNA-damaging drugs; PSMD10's level ->
   Ixazomib and ACSL4's -> Artesunate; MTAP-null -> Pemetrexed; the drug-target classes (glucocorticoids, MTOR,
   statins); that random pseudo-groups give ~no edges; that no edge lacks p / q / grade, that the written-edge and
   grade rules hold and every alert starts with the warning sign; that the TP53-deleted lines are seen as not
   expressing TP53; that a small gene chunk gives identical edges. Reasons in tiers (direction VERSION 3): (a) the
   edges' (source_col, target_col, target_dd, kind, grade, sign, q) equal tests/fixtures/direction_v2_seed0.tsv (made
   from VERSION 2's seed-0 edges: the tiers change no edge, grade, sign or q); (b) the reasons of alerts_all are
   exactly those of the four tiers, in order; (c) each graded reason is in the tier its threshold gives (read apart
   from direction.reason_tier) and art_share agrees with drugdoses_all; (d) some edges carry no alert; (e) an output
   of VERSION 2 (no tier columns) still reads through direction_view; (f) the names in a reason equal the full set
   it describes (every shared target, every co-occurring gene: VERSION 4 cuts no list). Unit: reason_tier at and
   around each threshold.
   check(out) runs these on any finished output (tests/checks.py).
2. Variants of the synthetic output: without metadata, relations, drug targets and cell numbers (the empty edges
   table keeps its column types), and with lines.csv lacking its Organ column (organs come from the metadata).
3. A 50-line fixture (3,000 genes x 300 drug-doses): (a) a genotype-dependent programme P that dominates the
   other responsive genes of its drug-doses, next to genes Q that respond the same in every line - P is found at
   grade A, Q never gets grade A and its edges say they rest on the global-sensitivity correction; (b) a
   line-wide damping (DAMP lines show 0.3x of every planted response, at narrow, near-threshold and broad
   drug-doses alike) - no gene-specific edges; (c) a random group - ~no edges.
4. Scale: generated outputs with the real numbers of drug-doses (1,132) and lines (50, 16 organs in realistic
   proportions), 4,000 / 8,000 genes (any list with --scale-genes, e.g. 16643), many drug-doses with line-to-line
   differences in cell numbers, tissue-specific absent genes, random small driver groups and hypermutated lines,
   40 compounds that move some genes in every line (as most drugs do), and planted answers: a genotype-dependent
   programme (found), a line-wide global resistance at broad drug-doses (not called gene-specific), TP53 / KEAP1
   effects, a natural knockout with partner effects (response and baseline), a lone natural-knockout effect on cell
   numbers (MTAP-null), a gene whose level modulates its partners' responses (level edges, direction clear) and one
   whose level sets a drug's effect (permuted levels give no more edges than the FDR allows); the pseudo-groups and the
   random driver groups give ~no edges and are rarely tissue-confounded; peak memory and minutes are measured and
   extrapolated to the real 16,643 genes (within ~3 GB and a few minutes). Each fixture's tensor is deleted after
   its run (DDL_lfc is a hard link of DDL_z where the file system allows: only the folds shown in readings use it).
Prints PASS / FAIL per check with its numbers; exit code 1 if anything fails.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)
DEFAULT_WORKDIR = "/tmp/tahoemap_test" if os.name != "nt" else os.path.join(tempfile.gettempdir(), "tahoemap_test")
RESULTS = []
FULL_GENES = 16643
MEM_LIMIT_GB = 3.0
MINUTES_LIMIT = 10.0
WARN = "⚠"


def report(name, fn):
    try:
        ok, detail = fn()
        status = "PASS" if ok else "FAIL"
    except Exception as e:  # noqa: BLE001
        import traceback
        status, detail = "FAIL", f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=4)}"
    RESULTS.append((status, name, str(detail)))
    print(f"  [{status}] {name} -- {detail}", flush=True)


def run_stage(out, data, extra=()):
    cmd = [sys.executable, "-m", "tahoemap.direction", "--out", out, *(["--data", data] if data else []), *extra]
    t0 = time.time()
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace")
    dt = time.time() - t0
    with open(os.path.join(out, "direction_console.log"), "w", encoding="utf-8") as fh:
        fh.write(r.stdout + "\n" + r.stderr)
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
    info = {}
    p = os.path.join(out, "direction", "info.json")
    if r.returncode == 0 and os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            info = json.load(fh)
    return r.returncode, dt, info, r.stdout


def copy_output(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst, symlinks=True, ignore=shutil.ignore_patterns("vault", "map", "review"))
    shutil.rmtree(os.path.join(dst, "direction"), ignore_errors=True)


def load(out):
    d = os.path.join(out, "direction")
    e = pd.read_parquet(os.path.join(d, "edges.parquet"))
    g = pd.read_parquet(os.path.join(d, "groups.parquet"))
    with open(os.path.join(d, "controls.json"), encoding="utf-8") as fh:
        ctl = json.load(fh)
    return e, g, ctl


def table_wide(e):
    """Edges significant over the whole table (grades A / B possible): q < 0.10 and, where present, q_group."""
    return (e["q"] < 0.10) & (e["q_group"].isna() | (e["q_group"] < 0.10))


def integrity(e):
    """Every edge has p, q and a grade; the written-edge rule, the grade rules and the alert format hold."""
    from tahoemap import direction as Dm
    bad = []
    if not e["p"].notna().all() or not np.isfinite(e["p"]).all():
        bad.append("p missing")
    grouped = e["kind"].str.startswith("genotype") | (e["kind"] == "level_sensitivity")
    written = np.where(grouped, e["q_group"] < 0.10, e["q"] < 0.10)
    if not written.all():
        bad.append(f"{int((~written).sum())} edges without q (q_group for grouped kinds) < 0.10")
    if not e["q"].notna().all():
        bad.append("q missing")
    if not e["grade"].isin(["A", "B", "C"]).all():
        bad.append("grade")
    if not e["kind"].isin(Dm.KINDS).all():
        bad.append("kind")
    if not e["sign"].isin([-1, 0, 1]).all():
        bad.append("sign")
    if ((e["source"] == "") | (e["target"] == "")).any():
        bad.append("empty source / target")
    if ((e["target_type"] == "gene") & (e["source_col"] == e["target_col"]) & (e["source_col"] >= 0)).any():
        bad.append("self edge")
    a = e[e["grade"] == "A"]
    rule = a["kind"].str.startswith("genotype") & (a["q"] < 0.05) & (a["q_group"] < 0.10) & \
        (a["n_altered"] >= 5) & (a["n_intact"] >= 5) & ~a["alerts"].str.contains(
            "tissue-confounded|co-occurs with|compared across organs|exists only relative|significant within this|"
            "sit on the other side")
    if not rule.all():
        bad.append(f"{int((~rule).sum())} grade-A edges break the A rule")
    tc = e["kind"].str.startswith("genotype") & e["alerts"].str.contains("tissue-confounded")
    if not (e.loc[tc, "grade"] == "C").all():
        bad.append("a tissue-confounded genotype edge is not grade C")
    only_group = e["kind"].str.startswith("genotype") & ~table_wide(e)
    if not (e.loc[only_group, "grade"] == "C").all():
        bad.append("an edge significant only within its group is not grade C")
    al = e["alerts"].fillna("")
    if not ((al == "") | al.str.startswith(WARN + " ")).all():
        bad.append("an alert without the warning sign")
    n = al.map(lambda s: s.count("; ") + 1 if s else 0)
    if not (n == e["n_alerts"]).all():
        bad.append("n_alerts")
    return bad, len(a)


# ----------------------------------------------------------------------------- reasons in tiers (direction VERSION 3)
FIXTURE = os.path.join(HERE, "fixtures", "direction_v2_seed0.tsv")
FIX_COLS = ["source_col", "target_col", "target_dd", "kind", "grade", "sign", "q"]
TIER_TEXT = ("alerts", "notes", "caveats", "support")
SEED0_DIMS = {"genes": 1198, "drugdoses": 282, "lines": 18}      # the seed-0 synthetic run of run_tests.py


def fixture_lines(e):
    """The edges as the fixture holds them: one tab-separated line per edge (q with repr precision), sorted."""
    return sorted("\t".join(str(x) for x in (int(r[0]), int(r[1]), int(r[2]), str(r[3]), str(r[4]), int(r[5]),
                                               repr(float(r[6]))))
                  for r in e[FIX_COLS].itertuples(index=False, name=None))


def read_fixture(path=FIXTURE):
    with open(path, encoding="utf-8") as fh:
        rows = fh.read().splitlines()
    return rows[0].split("\t"), sorted(x for x in rows[1:] if x)


def _split(t):
    t = str(t or "").strip()
    if t.startswith(WARN):
        t = t[len(WARN):].strip()
    return [x.strip() for x in t.split("; ") if x.strip()]


def _subsequence(part, whole):
    it = iter(whole)
    return all(any(x == y for y in it) for x in part)


def expected_tier(reason, kind, art_share, first_flagged):
    """The tier a reason should be in, written apart from direction.reason_tier (the test's oracle): (tier,
    category). first_flagged: the first of the edge's top_drugdoses carries an artifact flag (None: unknown)."""
    import re
    from tahoemap import direction as Dm
    cav = {x.replace("; ", ", ") for x in (Dm.DRUG_ALERT, Dm.TISSUE_ALERT, Dm.PRECISION_ALERT)}
    if reason in cav:
        return "caveats", "caveat"
    if re.match(r"^consistent across \d+ compounds \(", reason) or (
            reason.startswith("the lines lacking ") and reason.endswith(": genotype evidence too")):
        return "support", "support"
    m = re.match(r"^\S+ measured in (\d+) of the (\d+) and (\d+) of the (\d+) lines$", reason)
    if m:
        a, na, i, ni = map(int, m.groups())
        low = min(a, i) < Dm.FULL_SIDE or a / na < Dm.NOTE_MEASURED_FRAC or i / ni < Dm.NOTE_MEASURED_FRAC
        return ("alerts" if low else "notes"), "measured"
    if reason.startswith("supporting drug-doses with artifact flags ("):
        strongest = ", the strongest among them):" in reason
        if kind in ("genotype_response", "null_response") and first_flagged is not None and \
                strongest != bool(first_flagged):
            return "mismatch", "artifact flags: 'the strongest among them' does not match top_drugdoses"
        m = re.search(r"\((\d+) of the (\d+) supporting compounds", reason)
        if m:
            share = int(m.group(1)) / int(m.group(2))
        else:
            share = float(art_share) if art_share is not None else float("nan")
        alert = strongest or not np.isfinite(share) or share >= Dm.NOTE_ART_SHARE
        return ("alerts" if alert else "notes"), "artifact flags"
    m = re.match(r"^compared within organs: (\d+) of the (\d+) .+? and (\d+) of the (\d+) others share an organ",
                 reason)
    if m:
        a, na, i, ni = map(int, m.groups())
        low = a / na < Dm.NOTE_WITHIN_ORGAN_FRAC or i / ni < Dm.NOTE_WITHIN_ORGAN_FRAC
        return ("alerts" if low else "notes"), "within organs"
    if reason.startswith("other genes are absent from most of these lines too: "):
        m = re.search(r"\(and (\d+) more line sets\): any of them", reason)
        total = reason.count(" (overlap ") + (int(m.group(1)) if m else 0)
        return ("alerts" if total <= Dm.NOTE_COABSENT_SETS else "notes"), "co-absent sets"
    m = re.match(r"^\S+ itself is not expressed in (\d+) of the (\d+) altered lines", reason)
    if m:
        k, n = map(int, m.groups())
        return ("alerts" if k / n > Dm.NOTE_NOT_EXPRESSED_FRAC else "notes"), "not expressed"
    return "alerts", "other"


def _first_flagged(out):
    """{drug-dose label: carries an artifact flag} from atlas/effects/drugdose.csv (as the stage labels and flags)."""
    from tahoemap import atlas_core as A
    from tahoemap import direction as Dm
    dd = pd.read_csv(os.path.join(out, "atlas", "effects", "drugdose.csv"), dtype={"dose": str},
                     keep_default_na=False)
    fl = dd["flags"].astype(str) if "flags" in dd else pd.Series([""] * len(dd))
    return {Dm._dd_label(a, b): bool(A.has_artifact(f)) for a, b, f in zip(dd["drug"], dd["dose"], fl)}


def tier_checks(out, fixture=None):
    """The reasons in tiers on a finished output: [(name, fn)], fn() -> (ok, detail). fixture: compare the edges'
    (source_col, target_col, target_dd, kind, grade, sign, q) with tests/fixtures/direction_v2_seed0.tsv (None:
    when the output has the seed-0 synthetic run's dimensions)."""
    import collections
    from tahoemap import direction_view as DV
    d = os.path.join(out, "direction")
    e = pd.read_parquet(os.path.join(d, "edges.parquet"))
    g = pd.read_parquet(os.path.join(d, "groups.parquet"))
    info = json.load(open(os.path.join(d, "info.json"), encoding="utf-8"))
    if fixture is None:
        fixture = all(info.get(k) == v for k, v in SEED0_DIMS.items())
    checks = []

    def fix():
        if not fixture:
            return "warn", f"not the seed-0 synthetic run ({ {k: info.get(k) for k in SEED0_DIMS} }): not compared"
        head, want = read_fixture()
        got = fixture_lines(e)
        a, b = collections.Counter(got), collections.Counter(want)
        return head == FIX_COLS and got == want, (
            f"{len(got)} edges vs {len(want)} in the fixture; only here: {list((a - b).elements())[:3]}; only in the "
            f"fixture: {list((b - a).elements())[:3]}")
    checks.append(("(a) the edges, grades, signs and q equal the direction VERSION 2 fixture (seed 0)", fix))

    def union():
        bad = []
        for i in range(len(e)):
            every = _split(e["alerts_all"].iat[i])
            parts = [_split(e[t].iat[i]) for t in TIER_TEXT]
            if collections.Counter(every) != collections.Counter(x for p in parts for x in p):
                bad.append((i, "multiset"))
            elif not all(_subsequence(p, every) for p in parts):
                bad.append((i, "order"))
            if [len(p) for p in parts] != [int(e[f"n_{t}"].iat[i]) for t in TIER_TEXT]:
                bad.append((i, "counts"))
            al = str(e["alerts"].iat[i] or "")
            if (al != "" and not al.startswith(WARN + " ")) or any(
                    WARN in str(e[t].iat[i] or "") for t in ("notes", "caveats", "support", "alerts_all")):
                bad.append((i, "warning sign outside alerts"))
        for i in range(len(g)):
            every = _split(g["alerts_all"].iat[i])
            parts = _split(g["alerts"].iat[i]) + _split(g["notes"].iat[i])
            if collections.Counter(every) != collections.Counter(parts):
                bad.append((f"group {i}", "multiset"))
        dt = {c: str(e[c].dtype) for c in ("n_alerts", "n_notes", "n_caveats", "n_support", "art_share")}
        types = all(v == "int16" for k, v in dt.items() if k != "art_share") and dt["art_share"] == "float32"
        return not bad and types, (f"{len(e)} edges, {len(g)} groups: alerts_all = alerts + notes + caveats + support "
                                   f"(same reasons, each tier in alerts_all's order, counts); problems {bad[:5]}; "
                                   f"types {dt}")
    checks.append(("(b) every reason of alerts_all is in exactly one tier (the multiset of the four tiers), in order",
                   union))

    def graded():
        ff = _first_flagged(out)
        cnt, bad = collections.Counter(), []
        for i in range(len(e)):
            kind = str(e["kind"].iat[i])
            top = str(e["top_drugdoses"].iat[i] or "")
            first = top.split("; ")[0].rsplit(": ", 1)[0] if top else ""
            fflag = ff.get(first) if first else None
            where = {r: t for t in TIER_TEXT for r in _split(e[t].iat[i])}
            for r in _split(e["alerts_all"].iat[i]):
                want, cat = expected_tier(r, kind, e["art_share"].iat[i], fflag)
                cnt[(cat, where.get(r))] += 1
                if want != where.get(r):
                    bad.append((i, cat, want, where.get(r), r[:90]))
        for i in range(len(g)):
            where = {r: t for t in ("alerts", "notes") for r in _split(g[t].iat[i])}
            for r in _split(g["alerts_all"].iat[i]):
                want, cat = expected_tier(r, "", np.nan, None)
                if want != where.get(r):
                    bad.append((f"group {i}", cat, want, where.get(r), r[:90]))
        tally = "; ".join(f"{c}: {n} in {t}" for (c, t), n in sorted(cnt.items(), key=lambda x: (x[0][0],
                                                                                                    str(x[0][1]))))
        return not bad, f"{tally}; misplaced {len(bad)}: {bad[:4]}"
    checks.append(("(c) each graded reason is in the tier its threshold gives (an independent reading of the "
                   "numbers), every other reason in its fixed tier", graded))

    def art():
        """art_share of the response edges agrees with drugdoses_all (contrasts rounded to 0.1) and the artifact
        reason lists exactly the flagged drug-doses with a value."""
        import re
        resp = e["kind"].isin(["genotype_response", "null_response"])
        bad, n = [], 0
        for i in np.flatnonzero(resp.to_numpy()):
            items = [x for x in str(e["drugdoses_all"].iat[i]).split("; ") if x]
            vals = []
            for x in items:
                m = re.search(r"\(z diff ([-+]?[0-9.]+)\)", x)
                if m:
                    vals.append((abs(float(m.group(1))), "[artifact flags:" in x, x.split(": ", 1)[0]))
            tot = sum(v for v, _, _ in vals)
            sh = float(e["art_share"].iat[i])
            if tot >= 5 and np.isfinite(sh) and abs(sum(v for v, f, _ in vals if f) / tot - sh) > 0.1:
                bad.append((i, "share", round(sh, 3)))
            flagged = [lab for _, f, lab in vals if f]
            rs = [r for r in _split(e["alerts_all"].iat[i]) if r.startswith("supporting drug-doses with artifact")]
            if bool(flagged) != bool(rs) or (rs and not all(f"{lab} (" in rs[0] for lab in flagged)):
                bad.append((i, "reason", flagged[:2], rs[:1]))
            n += 1
        notresp = e.loc[~resp, "art_share"]
        return not bad and bool(notresp.isna().all()), (
            f"{n} response edges (art_share from drugdoses_all within 0.1; the artifact reason names every flagged "
            f"drug-dose with a value); other kinds NaN: {bool(notresp.isna().all())}; problems {bad[:4]}")
    checks.append(("art_share and drugdoses_all of the response edges agree with the artifact-flag reason", art))

    def unalerted():
        n0 = int((e["n_alerts"] == 0).sum())
        dv = DV.load(out, cache=False)
        rows = dv.rows
        k = int((~rows["has_alert"]).sum())
        shown, n_more, _ = DV.cap(rows, 5)
        by = e[e["n_alerts"] == 0].groupby("kind").size().to_dict()
        return n0 > 0 and k > 0 and len(shown) > 5 and dv.tiered, (
            f"{n0} of {len(e)} edges without an alert ({by}); {k} of {len(rows)} display rows; the cap rule at 5 "
            f"now adds the strongest rows without an alert: {len(shown)} shown, {n_more} more")
    checks.append(("(d) some edges carry no alert, so the warning sign tells rows apart (and the cap rule can add "
                   "unalerted rows)", unalerted))

    def old_output():
        return old_output_check(out)
    checks.append(("(e) an output of direction VERSION 2 (no tier columns) still reads through direction_view: "
                   "alerts = every reason, the other tiers empty", old_output))

    def full_lists():
        return reason_list_check(out, e, g)
    checks.append(("(f) the names in a reason equal the full set it describes (every shared target, every "
                   "co-occurring gene: no list is cut)", full_lists))
    return checks


def reason_list_check(out, e, g):
    """'the supporting compounds also share ...' names every target the supporting compounds share besides the
    arrow's source (recomputed from atlas/effects/drugdose.csv targets, one molecule per salt base as the stage
    counts it); 'co-occurs with ...' of a genotype group names every gene of its cooccurs_with column, and of an edge
    every one (a natural knockout's edge: every one but the gene itself)."""
    import re
    from tahoemap import direction as Dm
    from tahoemap.common import read_effects_index
    dd = read_effects_index(os.path.join(out, "atlas", "effects"))["drugdose"]
    tg = {}
    for name, t in zip(dd["drug"].astype(str), dd["targets"] if "targets" in dd else [""] * len(dd)):
        tg.setdefault(Dm._molecule_key(name), set()).update(Dm._split_targets(t))
    head = "the supporting compounds also share "
    bad, n_sh, n_co, longest = [], 0, 0, 0
    for src, sup, al in zip(e["source"].astype(str), e["compounds_supporting"].fillna("").astype(str),
                            e["alerts_all"].fillna("").astype(str)):
        for r in _split(al):
            if not r.startswith(head):
                continue
            n_sh += 1
            got = r[len(head):].split(": ")[0].split(", ")
            keys = [Dm._molecule_key(x.split(" / ")[0]) for x in sup.split("; ") if x]
            want = sorted(set.intersection(*[tg.get(k, set()) for k in keys]) - {src.upper()}) if keys else []
            longest = max(longest, len(want))
            if got != want:
                bad.append(f"{src}: names {got}, shares {want}")
    co_head = "co-occurs with "
    rx = re.compile(r"(\S+)-altered lines \(overlap [0-9.]+\)")
    cw = dict(zip(g["description"].astype(str), g["cooccurs_with"].fillna("").astype(str)))
    gene_of = dict(zip(g["description"].astype(str), g["gene"].astype(str)))
    for desc, kind, al in zip(g["description"].astype(str), g["kind"].astype(str),
                              g["alerts_all"].fillna("").astype(str)):
        if kind.startswith("null"):        # a natural knockout names them on its edges (without the gene itself)
            continue
        want = [x.rsplit(" (", 1)[0] for x in cw.get(desc, "").split("; ") if x]
        got = [m.group(1) for r in _split(al) if r.startswith(co_head) for m in rx.finditer(r)]
        n_co += bool(want)
        if got != want:
            bad.append(f"group {desc}: names {got}, cooccurs_with {want}")
    for grp, src, al in zip(e["group"].astype(str), e["source"].astype(str), e["alerts_all"].fillna("").astype(str)):
        if grp not in cw:
            continue
        own = {src.upper(), gene_of.get(grp, "").upper()}
        want_all = [x.rsplit(" (", 1)[0] for x in cw[grp].split("; ") if x]
        for r in _split(al):
            if r.startswith(co_head):
                got = [m.group(1) for m in rx.finditer(r)]
                if got != want_all and got != [x for x in want_all if x.upper() not in own]:
                    bad.append(f"edge {src} ({grp}): names {got}, cooccurs_with {want_all}")
    return not bad and n_sh > 0, (f"{n_sh} 'also share' reasons name every shared target (up to {longest}); "
                                  f"{n_co} groups name every co-occurring gene" + (f"; wrong: {bad[:4]}" if bad
                                                                                    else ""))


def old_output_check(out):
    """Rebuild this output's direction folder as VERSION 2 wrote it (alerts = every reason with the sign, no tier,
    art_share or drugdoses_all columns; groups without notes / alerts_all) in a temporary folder, read it through
    direction_view, and compare with the VERSION 3 reading: the same rows in the same order; every reason an alert;
    the texts, counts, cap rule, look-ups and merged rows work."""
    from tahoemap import direction as Dm
    from tahoemap import direction_view as DV
    tmp = tempfile.mkdtemp(prefix="tahoe_dir_v2_")
    try:
        os.makedirs(os.path.join(tmp, "direction"))
        os.makedirs(os.path.join(tmp, "atlas"))
        src = os.path.join(out, "atlas", "effects")
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(tmp, "atlas", "effects"),
                            ignore=lambda d_, names: [x for x in names if x.endswith(".npy")])
        d = os.path.join(out, "direction")
        for f in ("controls.json", "info.json"):
            shutil.copy(os.path.join(d, f), os.path.join(tmp, "direction", f))
        e = pd.read_parquet(os.path.join(d, "edges.parquet"))
        g = pd.read_parquet(os.path.join(d, "groups.parquet"))
        v2 = e.drop(columns=[c for c in Dm.TIER_COLS + ("art_share", "drugdoses_all") if c in e])
        v2["alerts"] = [Dm._join(_split(t)) for t in e["alerts_all"]]
        v2["n_alerts"] = np.array([len(_split(t)) for t in e["alerts_all"]], dtype=np.int16)
        v2.to_parquet(os.path.join(tmp, "direction", "edges.parquet"), index=False)
        g2 = g.drop(columns=["notes", "alerts_all"])
        g2["alerts"] = [Dm._join(_split(t)) for t in g["alerts_all"]]
        g2.to_parquet(os.path.join(tmp, "direction", "groups.parquet"), index=False)
        new = DV.load(out, cache=False)
        old = DV.load(tmp, cache=False)
        bad = []
        if old.tiered or not new.tiered:
            bad.append("tiered flags")
        if list(old.rows["members"]) != list(new.rows["members"]):
            bad.append("display rows differ")
        if not all(DV.alert_reasons(r) == DV.all_reasons(r) for _, r in old.rows.iterrows()):
            bad.append("an old row's alerts are not every reason")
        if not all(DV.alert_reasons(o) == DV.all_reasons(o) and sorted(DV.all_reasons(o)) == sorted(
                DV.all_reasons(n)) for (_, o), (_, n) in zip(old.rows.iterrows(), new.rows.iterrows())):
            bad.append("old rows: reasons differ from the new rows' alerts_all")
        if (old.rows[["n_notes", "n_caveats", "n_support"]].to_numpy() != 0).any() or (
                old.rows[["notes", "caveats", "support"]] != "").to_numpy().any():
            bad.append("old rows: tiers other than alerts are not empty")
        if not bool((old.rows["has_alert"] == (old.rows["n_alerts"] > 0)).all()):
            bad.append("has_alert")
        r0 = old.rows.iloc[0]
        line = DV.edge_line(r0)
        t = DV.texts(r0)
        if not (line and t["notes_short"] == "" and t["n_alerts"] == len(DV.all_reasons(r0))
                and "notes:" not in line):
            bad.append("edge_line / texts")
        tp = old.downstream("TP53")
        ct = DV.counts_text(tp, "arrows")
        shown, n_more, n_al = DV.cap(old.rows, 5)
        if len(shown) + n_more != len(old.rows) or not ct:
            bad.append("cap / counts_text")
        if len(old.groups) and not (old.groups["alerts_all"].astype(str).str.len() > 0).any():
            bad.append("old groups: alerts_all")
        return not bad, (f"{len(old.rows)} display rows read from the rebuilt VERSION 2 folder, "
                         f"{int(old.rows['has_alert'].sum())} with an alert (VERSION 3: "
                         f"{int(new.rows['has_alert'].sum())}); '{DV.ascii_signs(line)[:100]}'; counts '{ct}'; "
                         f"problems {bad or 'none'}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check(out, data=None, fixture=None):
    """The direction checks of a finished output, for tests/checks.py (design I5): the reasons in tiers (tier_checks)
    and the edge rules (integrity). Returns [(name, ok, detail)], ok True, False or 'warn'. data is not needed (kept
    for the common signature)."""
    res = []
    e = pd.read_parquet(os.path.join(out, "direction", "edges.parquet"))
    bad, na = integrity(e)
    res.append(("edges: p, q, grade, kind, sign; the written-edge, grade and alert rules", not bad,
                "; ".join(bad) if bad else f"ok ({len(e)} edges, {na} grade A)"))
    for name, fn in tier_checks(out, fixture):
        try:
            ok, detail = fn()
        except Exception as ex:  # noqa: BLE001
            ok, detail = False, f"{type(ex).__name__}: {ex}"
        res.append((name, ok, str(detail)))
    return res


def tier_unit_checks():
    """direction.reason_tier on constructed reasons at and around each threshold (no output needed)."""
    from tahoemap import direction as Dm
    F, M, W, C, N = (Dm.FULL_SIDE, Dm.NOTE_MEASURED_FRAC, Dm.NOTE_WITHIN_ORGAN_FRAC, Dm.NOTE_COABSENT_SETS,
                     Dm.NOTE_NOT_EXPRESSED_FRAC)
    cases = [
        ("Y measured in 6 of the 8 and 10 of the 10 lines", np.nan, "notes" if 6 >= M * 8 and 6 >= F else "alerts"),
        ("Y measured in 5 of the 8 and 10 of the 10 lines", np.nan, "alerts" if 5 < M * 8 else "notes"),
        ("Y measured in 4 of the 4 and 10 of the 10 lines", np.nan, "alerts" if 4 < F else "notes"),
        ("Y measured in 30 of the 33 and 16 of the 17 lines", np.nan, "notes"),
        ("supporting drug-doses with artifact flags (49% of the evidence): A 5 µM (toxic)", 0.4999, "notes"),
        ("supporting drug-doses with artifact flags (50% of the evidence): A 5 µM (toxic)", 0.5, "alerts"),
        ("supporting drug-doses with artifact flags (10% of the evidence, the strongest among them): A 5 µM (toxic)",
         0.1, "alerts"),
        ("supporting drug-doses with artifact flags (share of the evidence not measurable): A 5 µM (toxic)",
         np.nan, "alerts"),
        ("supporting drug-doses with artifact flags (1 of the 3 supporting compounds): A 5 µM (toxic)", np.nan,
         "notes"),
        ("supporting drug-doses with artifact flags (2 of the 4 supporting compounds): A 5 µM (toxic)", np.nan,
         "alerts"),
        ("supporting drug-doses with artifact flags: A 5 µM (toxic)", np.nan, "alerts"),       # VERSION 2 words
        ("compared within organs: 10 of the 20 TP53-altered lines and 15 of the 30 others share an organ with lines "
         "of the other side (the comparison rests on those)", np.nan, "notes" if 10 >= W * 20 else "alerts"),
        ("compared within organs: 9 of the 20 TP53-altered lines and 30 of the 30 others share an organ with lines of "
         "the other side (the comparison rests on those)", np.nan, "alerts"),
        ("other genes are absent from most of these lines too: A (overlap 0.80), B (overlap 0.70), C (overlap 0.60) "
         f"(and {C - 3} more line sets): any of them could be the cause", np.nan, "alerts"),
        ("other genes are absent from most of these lines too: A (overlap 0.80), B (overlap 0.70), C (overlap 0.60) "
         f"(and {C - 2} more line sets): any of them could be the cause", np.nan, "notes"),
        ("other genes are absent from most of these lines too: MTAP (+2 absent from the same lines) (overlap 0.62): "
         "any of them could be the cause", np.nan, "alerts"),
        ("TP53 itself is not expressed in 8 of the 33 altered lines (deletion or silencing)", np.nan,
         "alerts" if 8 > N * 33 else "notes"),
        ("TP53 itself is not expressed in 9 of the 33 altered lines (deletion or silencing)", np.nan,
         "alerts" if 9 > N * 33 else "notes"),
        (Dm.DRUG_ALERT, np.nan, "caveats"), (Dm.TISSUE_ALERT.replace("; ", ", "), np.nan, "caveats"),
        (Dm.PRECISION_ALERT, np.nan, "caveats"),
        ("consistent across 3 compounds (A, B, C)", np.nan, "support"),
        ("the lines lacking MTAP carry a recorded loss of MTAP (overlap 0.80): genotype evidence too", np.nan,
         "support"),
        ("few lines (4 vs 13)", np.nan, "alerts"), ("a reason this code does not know", np.nan, "alerts")]
    bad = []
    for r, a, want in cases:
        got = Dm.reason_tier(r, a)
        # the test's own reading too (it does not know VERSION 2's words, which stay an alert)
        oracle = want if r.startswith("supporting drug-doses with artifact flags: ") else \
            expected_tier(r, "genotype_response", a, None)[0]
        if got != want or oracle != want:
            bad.append((r[:60], got, oracle, want))
    return not bad, f"{len(cases)} reasons at and around the thresholds; wrong (reason, tier, oracle, want): " \
                    f"{bad or 'none'}"


# ----------------------------------------------------------------------------- 0. unit checks (no output needed)
def unit_checks():
    """(a) drug_target counts one molecule once: the real Tahoe names of one molecule in two forms ('Ixazomib' /
    'Ixazomib citrate', 'Larotrectinib' / 'Larotrectinib sulfate', 'crizotinib' / 'Crizotinib (hydrochloride)'), each
    moving a gene alone, give no edge (one molecule is not >= 2 compounds), while two different molecules do. (b) the
    direction of a level edge allows for its selection: on simulated pairs whose two directions are equally strong, the
    written edges are rarely called 'direction clear' (a plain bootstrap called 20-60% of them clear), while a pair
    with one real direction often is, and its reverse never."""
    import types
    from scipy import stats
    from tahoemap import direction as Dm
    from tahoemap import tlib as T

    def molecules():
        real = [("Bortezomib", "PSMB5"), ("Ixazomib", "PSMB5"), ("Ixazomib citrate", "PSMB1, PSMB2, PSMB5"),
                ("Larotrectinib", "NTRK1, NTRK2, NTRK3"), ("Larotrectinib sulfate", "NTRK1, NTRK2, NTRK3"),
                ("Entrectinib", "ALK, NTRK1, NTRK2, NTRK3, ROS1"), ("crizotinib", "ALK, MET, ROS1"),
                ("Crizotinib (hydrochloride)", "ALK, MET, ROS1"), ("Abemaciclib", "CDK4, CDK6"),
                ("Ribociclib", "CDK4, CDK6")]
        drugs = real + [(f"Other{i:02d}", "") for i in range(60)]
        dd = pd.DataFrame([{"drug": d, "dose": x, "targets": t, "moa_broad": "inhibitor/antagonist", "flags": ""}
                           for d, t in drugs for x in ("0.05", "0.5", "5")])
        Dn, gK = len(dd), 4
        c = types.SimpleNamespace(dd=dd, Dn=Dn, gK=gK, col_of={})
        c.salt = np.array([T.salt_base(x) for x in dd["drug"]], dtype=object)
        c.sym = np.array(["YIXA", "YLARO", "YCRIZ", "YCDK"], dtype=object)
        c.sig_up = np.zeros((Dn, gK), bool)
        c.sig_dn = np.zeros((Dn, gK), bool)
        moved = {0: ("Ixazomib", "Ixazomib citrate"), 1: ("Larotrectinib", "Larotrectinib sulfate"),
                 2: ("crizotinib", "Crizotinib (hydrochloride)"), 3: ("Abemaciclib", "Ribociclib")}
        for i, (d, x) in enumerate(zip(dd["drug"], dd["dose"])):
            for g, names in moved.items():
                if d in names and x == "5":
                    c.sig_up[i, g] = True
        for g in range(gK):                         # a background: two unrelated compounds move each gene too
            for k in (12 + g, 40 + g):
                c.sig_up[3 * k + 2, g] = True
        c.Zp = np.full((Dn, gK), 4.0, np.float32)
        c.lfc_p = np.ones((Dn, gK), np.float32)
        c.dd_label = [f"{a} {b} µM" for a, b in zip(dd["drug"], dd["dose"])]
        c.dd_art = np.zeros(Dn, bool)
        c.dd_flags = [""] * Dn
        rows, _n = Dm._drug_target(c)
        tg = sorted({r["target"] for r in rows})
        keys = {Dm._molecule_key(x) for x in ("Ixazomib", "Ixazomib citrate", "crizotinib",
                                                "Crizotinib (hydrochloride)", "Larotrectinib", "Larotrectinib sulfate")}
        return (tg == ["YCDK"] and len(keys) == 3 and Dm._molecule_key("(S)-Crizotinib") != "crizotinib",
                f"genes with a drug_target edge: {tg} (expected only YCDK, moved by 2 different molecules); "
                f"6 names -> {len(keys)} molecules; " + "; ".join(f"{r['source']} -> {r['target']}: {r['reading']}"
                                                                    for r in rows[:2]))
    report("drug_target: one molecule under two names counts once (the real Tahoe pairs)", molecules)

    def level_selection():
        rng = np.random.default_rng(5)
        res = {}
        for name, (L, rf, rr, npairs, share) in {"equal": (50, 0.4, 0.4, 3000, 0.05),
                                                 "one-way": (50, 0.6, 0.0, 1500, 0.05)}.items():
            G = 2 * npairs
            X, Y = rng.standard_normal((G, L)), rng.standard_normal((G, L))
            eff = rng.random(npairs) < share
            for i in np.flatnonzero(eff):
                u, v = rng.standard_normal(L), rng.standard_normal(L)
                X[2 * i] = np.sqrt(rf) * u + np.sqrt(1 - rf) * rng.standard_normal(L)
                Y[2 * i + 1] = np.sqrt(rf) * u + np.sqrt(1 - rf) * rng.standard_normal(L)
                X[2 * i + 1] = np.sqrt(rr) * v + np.sqrt(1 - rr) * rng.standard_normal(L)
                Y[2 * i] = np.sqrt(rr) * v + np.sqrt(1 - rr) * rng.standard_normal(L)
            xi = np.r_[np.arange(0, G, 2), np.arange(1, G, 2)]
            yi = np.r_[np.arange(1, G, 2), np.arange(0, G, 2)]
            r, n = Dm._masked_corr(X[xi], Y[yi])
            dof = n - 2
            p = 2 * stats.t.sf(np.abs(Dm._r_to_t(r, dof)), dof)
            q, cut = Dm._bh(p), Dm._bh_cut(p)
            rrev = np.r_[r[npairs:], r[:npairs]]
            fwd = np.r_[np.ones(npairs, bool), np.zeros(npairs, bool)]
            hit = np.flatnonzero(q < Dm.Q_SIG)
            n_clear = n_rev_clear = 0
            for h in hit:
                pdir, _k = Dm._level_direction(X, Y, int(xi[h]), int(yi[h]), 100 + int(h), float(r[h]),
                                               float(rrev[h]), int(dof[h]), int(dof[h]),
                                               Dm._r_cut(cut, int(dof[h]), 1.0))
                clr = bool(np.isfinite(pdir) and pdir < Dm.LEVEL_DIR_P and abs(r[h]) > abs(rrev[h]))
                n_clear += clr
                n_rev_clear += clr and not fwd[h] and bool(eff[int(h) % npairs])    # a real pair's null direction
            res[name] = (len(hit), n_clear, n_rev_clear)
        (we, ce, _), (wo, co, ro) = res["equal"], res["one-way"]
        return (we >= 50 and ce <= max(2, 0.05 * we) and wo >= 30 and co >= 0.2 * wo and ro == 0,
                f"equally strong directions: {ce} of {we} written edges called clear (<= 5%); one real direction: "
                f"{co} of {wo} clear, reverse edges called clear {ro}")
    report("level: 'direction clear' allows for the edge's selection (simulated pairs)", level_selection)


# ----------------------------------------------------------------------------- 1. the synthetic run
def synthetic_checks(out, data, info, console):
    dd_ = os.path.join(out, "direction")
    e, g, ctl = load(out)
    with open(os.path.join(data, "ground_truth.json"), encoding="utf-8") as fh:
        truth = json.load(fh)
    sys.path.insert(0, HERE)
    import make_synthetic_tahoe as MS
    genes = set(pd.read_csv(os.path.join(out, "atlas", "effects", "genes.csv"))["symbol"].astype(str))
    p53 = [x for x in MS.P53_ACTIVITY if x in genes]

    report("outputs written (edges, groups, controls, info, README)", lambda: (
        all(os.path.exists(os.path.join(dd_, f)) for f in ("edges.parquet", "groups.parquet", "controls.json",
                                                            "info.json", "README.md"))
        and os.path.exists(os.path.join(out, "stages", "direction.json")),
        f"{len(e)} edges, {len(g)} groups; by kind {info.get('edges_by_kind')}"))

    def integ():
        bad, na = integrity(e)
        return not bad, ("ok: every edge has p and q, passes its family's BH (q, or q_group for genotype and "
                         f"level_sensitivity), a grade, kind and sign; {na} grade-A edges, all within the rule; "
                         "group-only edges are grade C; alerts start with the warning sign" if not bad
                         else "; ".join(bad))
    report("no edge lacks p / q / grade; written-edge, grade and alert rules hold", integ)

    def tp53():
        r = e[(e["kind"] == "genotype_response") & (e["source"] == "TP53")]
        hit = r[r["target"].isin(p53)]
        right = hit[hit["sign"] == 1]
        prec = len(hit) / max(1, len(r))
        ctl_k = [v for k, v in ctl["positive"].items() if k.startswith("TP53") and "p53 targets" in k]
        ranks = sorted(x["rank"] for x in (ctl_k[0]["per_gene"] if ctl_k else []) if x["gene"] in p53)
        top = sum(x <= 0.05 * 1198 for x in ranks)
        tw = right[table_wide(right)]
        # grade A, or B where an alteration of another gene sits on one side (on seed 0 the TP53-intact colon lines
        # are the KMT2D / CTNNB1-altered ones, which blocks grade A)
        ab = tw[(tw["grade"] == "A") | ((tw["grade"] == "B") & tw["alerts"].str.contains(
            "sit on the other side|co-occurs with"))]
        ok = len(right) >= 0.4 * len(p53) and prec >= 0.8 and (hit["sign"] == -1).sum() == 0 and \
            len(ab) > 0 and top >= 0.5 * len(p53)
        return ok, (f"{len(right)} of {len(p53)} P53_ACTIVITY genes with an edge, sign +1 ({(hit['sign'] == -1).sum()}"
                    f" wrong sign); grades {right['grade'].value_counts().to_dict()} ({len(tw)} significant over the "
                    f"whole table, the rest within the TP53 group only: grade C); {len(hit)} of the {len(r)} TP53 "
                    f"response edges are P53_ACTIVITY genes ({prec:.0%}); {top} of {len(p53)} ranked in the top 5% of "
                    f"all genes (ranks {ranks[:12]}...)")
    report("TP53 -> most P53_ACTIVITY genes (sign +1, graded A, or B with another alteration on a side)", tp53)

    def tp53_sens():
        s = e[(e["kind"] == "genotype_sensitivity") & (e["source"] == "TP53")]
        st = s[table_wide(s)]
        want = ["Doxorubicin (hydrochloride) 5", "Topotecan (hydrochloride) 5", "5-Fluorouracil 5"]
        got = [w for w in want if ((st["target"] == f"cells under {w} µM") & (st["sign"] == -1)).any()]
        return len(got) >= 2 and (st["sign"] == 1).sum() == 0, (
            f"{len(got)} of 3 DNA-damaging drugs at 5 µM over the whole table ({', '.join(got)}), sign -1 (TP53 "
            f"activity sensitises), none of the table-wide ones with sign +1; all TP53 sensitivity edges: "
            f"{s[['target', 'grade', 'sign', 'q', 'q_group']].round(4).to_dict('records')}")
    report("TP53 -> cells under the DNA-damaging drugs (sign -1)", tp53_sens)

    def level(gene, drug):
        s = e[(e["kind"] == "level_sensitivity") & (e["source"] == gene) & e["target"].str.contains(drug, regex=False)]
        ok = len(s) >= 1 and (s["sign"] == -1).all() and (s["grade"] == "C").all()
        return ok, (f"{gene} -> {s['target'].tolist()} r {s['r'].round(2).tolist()} q {s['q'].round(4).tolist()} "
                    f"q within the drug-dose {s['q_group'].round(4).tolist()} grade {s['grade'].tolist()}")
    report("PSMD10 level -> cells under Ixazomib (sign -1)", lambda: level("PSMD10", "Ixazomib"))
    report("ACSL4 level -> cells under Artesunate (sign -1)", lambda: level("ACSL4", "Artesunate"))

    def mtap():
        s = e[(e["kind"] == "null_sensitivity") & (e["source"] == "MTAP") & e["target"].str.contains("Pemetrexed")]
        ok = len(s) >= 1 and (s["sign"] == 1).all()
        al = s["alerts"].iloc[0] if len(s) else ""
        return ok, (f"MTAP-null -> {s['target'].tolist()} (sign +1: MTAP protects), grade {s['grade'].tolist()}, "
                    f"q {s['q'].round(4).tolist()}; alerts: {al[:160]}")
    report("MTAP-null lines -> depleted by Pemetrexed (null_sensitivity)", mtap)

    def drug_targets():
        sets = truth["extra_not_in_panel_spec"]["synthetic gene sets"]
        d = e[e["kind"] == "drug_target"]
        out, ok = [], True
        for src, name, sign in (("NR3C1", "GLUCO", 1), ("MTOR", "RIBI", 1), ("HMGCR", "CHOL", -1)):
            members = set(sets[name])
            x = d[(d["source"] == src) & d["target"].isin(members)]
            wrong = int((x["sign"] != sign).sum())
            ok &= len(x) >= 0.4 * len(members) and wrong == 0
            out.append(f"{src} -> {name}: {len(x)} of {len(members)} (wrong sign {wrong})")
        return ok, "; ".join(out)
    report("drug_target: glucocorticoid / MTOR / statin classes, sign relative to the target's activity", drug_targets)

    def negatives():
        s = ctl["negative"]["summary"]
        pse = ctl["negative"]["pseudo"]
        ok = all(pse[k]["edges_mean_per_group"] <= 0.1 and (pse[k]["edges_per_tested"] or 0) <= 1e-4
                 for k in pse) and pse["response"]["groups"] >= 50
        return ok, "; ".join(f"{k}: pseudo {v['pseudo_edges_mean_per_group']} table-wide edges/group vs real "
                             f"{v['real_edges_mean_per_group']} (within the group only: pseudo "
                             f"{v['pseudo_within_group_edges_mean_per_group']} vs real "
                             f"{v['real_within_group_edges_mean_per_group']}; expected false edges "
                             f"{v['expected_false_edges']} table-wide, {v['expected_false_edges_within_group']} "
                             f"within groups)" for k, v in s.items()) + f"; {pse['response']['groups']} pseudo-groups"
    report("random pseudo-groups give ~no edges (empirical false-positive rate)", negatives)

    def deleted():
        r = g[(g["gene"] == "TP53") & (g["kind"] == "genotype")]
        n = int(r["x_not_expressed_in_altered"].max()) if len(r) else -1
        ok = n == len(truth["groups"]["tp53_deleted"])
        a = r["alerts"].iloc[0] if len(r) else ""
        no = r["notes"].iloc[0] if len(r) and "notes" in r else ""
        return ok, f"TP53 not expressed in {n} of its altered lines (planted deletions: " \
                   f"{truth['groups']['tp53_deleted']}); the reason is an alert: {'itself is not expressed' in a}, " \
                   f"a note: {'itself is not expressed' in no}"
    report("TP53-deleted lines seen as not expressing TP53", deleted)

    def readme():
        txt = open(os.path.join(dd_, "README.md"), encoding="utf-8").read()
        miss = [c for c in list(e.columns) + list(g.columns) if f"`{c}`" not in txt]
        return not miss and "columns without a description" not in console, f"undocumented: {miss}"
    report("README.md documents every column", readme)
    for name, fn in tier_checks(out, fixture=bool(a_fixture(out))):
        report(name, fn)
    return e


def a_fixture(out):
    """The output is the seed-0 synthetic run (its dimensions): the direction VERSION 2 fixture applies."""
    info = json.load(open(os.path.join(out, "direction", "info.json"), encoding="utf-8"))
    return all(info.get(k) == v for k, v in SEED0_DIMS.items())


def chunk_check(src_out, data, work, e_ref):
    out2 = os.path.join(work, "out_chunk")
    copy_output(src_out, out2)
    rc, dt, info, _ = run_stage(out2, data, ("--chunk", "97"))
    e2 = pd.read_parquet(os.path.join(out2, "direction", "edges.parquet")) if rc == 0 else None

    def same():
        if e2 is None:
            return False, f"exit code {rc}"
        cols = ["kind", "source", "target", "grade", "sign"]
        a = e_ref[cols].sort_values(cols).reset_index(drop=True)
        b = e2[cols].sort_values(cols).reset_index(drop=True)
        qd = float(np.max(np.abs(np.sort(e_ref["q"].to_numpy()) - np.sort(e2["q"].to_numpy())))) if len(a) == len(
            b) else np.inf
        return a.equals(b) and qd < 1e-9, f"{len(a)} vs {len(b)} edges, chunk {info.get('chunk')} genes, " \
                                          f"max q difference {qd:.1e}"
    report("identical edges with a small gene chunk (97 genes)", same)
    shutil.rmtree(out2, ignore_errors=True)


# ----------------------------------------------------------------------------- 2. variants
def variant_checks(src_out, data, work):
    import pyarrow.parquet as pq
    # (a) nothing optional: no metadata, no relations, no drug targets, no cell numbers
    out = os.path.join(work, "out_bare")
    copy_output(src_out, out)
    shutil.rmtree(os.path.join(out, "relations"), ignore_errors=True)
    fx = os.path.join(out, "atlas", "effects")
    for f in ("DD_A.npy", "DD_Az.npy", "file_index.json"):
        for p in (os.path.join(fx, f), os.path.join(out, "atlas", f)):
            if os.path.exists(p):
                os.remove(p)
    dd = pd.read_csv(os.path.join(fx, "drugdose.csv"))
    dd = dd.drop(columns=[c for c in ("targets", "moa-broad", "moa_broad") if c in dd])
    dd.to_csv(os.path.join(fx, "drugdose.csv"), index=False)
    lines = pd.read_csv(os.path.join(fx, "lines.csv"))
    lines.drop(columns=[c for c in ("drivers", "driver_changes") if c in lines]).to_csv(
        os.path.join(fx, "lines.csv"), index=False)
    shutil.rmtree(os.path.join(out, "tables"), ignore_errors=True)
    rc, _, info, _ = run_stage(out, None, ("--pseudo", "5"))

    def bare():
        if rc != 0:
            return False, f"exit code {rc}"
        sch = pq.read_schema(os.path.join(out, "direction", "edges.parquet"))
        nulls = [f.name for f in sch if str(f.type) == "null"]
        n = pq.read_metadata(os.path.join(out, "direction", "edges.parquet")).num_rows
        return not nulls, f"{n} edges; columns of Arrow type null: {nulls or 'none'} ({len(sch)} columns)"
    report("variant without metadata / relations / targets / cell numbers: runs, typed columns", bare)
    shutil.rmtree(out, ignore_errors=True)
    # (b) lines.csv without Organ: the metadata's Organ is used
    out = os.path.join(work, "out_noorgan")
    copy_output(src_out, out)
    fx = os.path.join(out, "atlas", "effects")
    lines = pd.read_csv(os.path.join(fx, "lines.csv"))
    lines.drop(columns=["Organ"]).to_csv(os.path.join(fx, "lines.csv"), index=False)
    rc, _, info, _ = run_stage(out, data, ("--pseudo", "5"))

    def noorgan():
        if rc != 0:
            return False, f"exit code {rc}"
        g = pd.read_parquet(os.path.join(out, "direction", "groups.parquet"))
        unk = g["organs_altered"].str.contains("unknown:").sum() + g["alerts"].str.contains("unknown:").sum()
        return unk == 0 and info.get("lines_with_organ") == len(lines), (
            f"organs from {info.get('organs_from')!r}, {info.get('lines_with_organ')} of {len(lines)} lines with an "
            f"organ; groups mentioning 'unknown:' organs {int(unk)}")
    report("variant with lines.csv lacking Organ: organs come from the metadata", noorgan)
    shutil.rmtree(out, ignore_errors=True)


# ----------------------------------------------------------------------------- 3. the 50-line fixture
def _write_common(out, data, gK, Dn, L, organ, rng, drugrows=None):
    fx = os.path.join(out, "atlas", "effects")
    for d in (fx, os.path.join(out, "tensor"), os.path.join(out, "relations"), os.path.join(data, "metadata")):
        os.makedirs(d, exist_ok=True)
    G = gK + 3
    sym = [f"FG{i:05d}" for i in range(gK)] + ["S_PHASE", "G2M_PHASE", "PROTEASOME"]
    pc = np.exp(rng.normal(5.0, 1.0, G))
    return fx, G, sym, pc


def _link_or_copy_lfc(tdir, fac):
    """DDL_lfc as a hard link of DDL_z (no extra disk; only the folds shown in readings read it), else a copy x fac."""
    z, lf = os.path.join(tdir, "DDL_z.npy"), os.path.join(tdir, "DDL_lfc.npy")
    if os.path.exists(lf):
        os.remove(lf)
    try:
        os.link(z, lf)
        return
    except OSError:
        pass
    from tahoemap.common import open_memmap
    a = np.load(z, mmap_mode="r")
    b = open_memmap(lf, a.shape, np.float32)
    for g0 in range(0, a.shape[0], 500):
        b[g0:g0 + 500] = a[g0:g0 + 500] * fac
    del a, b


def make_small_fixture(root, seed=7):
    """3,000 genes x 300 drug-doses x 50 lines (10 organs x 5). Planted (z units, per line): 16 narrow programmes
    (20 genes x 3 drug-doses, every line); broad genes B (400 x 4 drug-doses, every line; pooled z just below
    significance at 2 of the 4); programme P (300 genes) at 4 other drug-doses only where DOMG is intact (0.4x in the
    DOMG lines) and genes Q (100) responding there identically in every line; DAMP lines show 0.3x of every planted
    response. NULLG: 20 random lines (a control)."""
    from tahoemap.common import open_memmap
    gK, Dn, L = 3000, 300, 50
    rng = np.random.default_rng(seed)
    shutil.rmtree(root, ignore_errors=True)
    out, data = os.path.join(root, "out"), os.path.join(root, "data")
    organs = np.array([f"Organ{k}" for k in range(10)], dtype=object)[np.arange(L) % 10]
    fx, G, sym, pc = _write_common(out, data, gK, Dn, L, organs, rng)
    pd.DataFrame({"col": np.arange(G), "kind": ["gene"] * gK + ["module"] * 3, "token": np.arange(3, 3 + G),
                  "symbol": sym, "label": sym, "pooled_cpm": pc, "median_line_cpm": pc,
                  "n_lines_expressing": L}).to_csv(os.path.join(fx, "genes.csv"), index=False)
    pd.DataFrame([{"drug": f"Drug{i // 3:03d}", "dose": ["0.05", "0.5", "5"][i % 3], "conc": [0.05, 0.5, 5.0][i % 3],
                   "flags": "", "targets": "", "moa_broad": "inhibitor/antagonist", "plates": "p1", "wells": "A1"}
                  for i in range(Dn)]).to_csv(os.path.join(fx, "drugdose.csv"), index=False)
    pd.DataFrame({"cell_line_id": [f"CVCL_F{i:03d}" for i in range(L)], "cell_name": [f"Line{i:02d}" for i in range(L)],
                  "Organ": organs, "in_growth_analysis": True}).to_csv(os.path.join(fx, "lines.csv"), index=False)
    domg = np.zeros(L, bool)
    domg[[i for i in range(L) if (i // 10) % 2 == 0]] = True                # 25 lines, 2-3 per organ
    damp = np.zeros(L, bool)
    damp[[i for i in range(L) if i % 4 in (1, 2)]] = True                   # 25 lines, another pattern
    nullg = np.zeros(L, bool)
    nullg[rng.choice(L, 20, replace=False)] = True
    meta = []
    for i in range(L):
        for gene, on in (("DOMG", domg[i]), ("DAMP", damp[i]), ("NULLG", nullg[i]), ("ANCHOR", True)):
            if on:
                meta.append({"cell_name": f"Line{i:02d}", "Cell_ID_DepMap": f"ACH-{i:06d}",
                             "Cell_ID_Cellosaur": f"CVCL_F{i:03d}", "Organ": organs[i], "Driver_Gene_Symbol": gene,
                             "Driver_VarZyg": "Hom", "Driver_VarType": "Missense",
                             "Driver_ProtEffect_or_CdnaEffect": "p.X1Y",
                             "Driver_Mech_InferDM": None if gene == "ANCHOR" else "LoF",
                             "Driver_GeneType_DM": "Suppressor"})
    pd.DataFrame(meta).to_parquet(os.path.join(data, "metadata", "cell_line_metadata.parquet"), index=False)
    lc = pc[None, :] * np.exp(rng.normal(0, 0.4, (L, G)))
    np.save(os.path.join(fx, "line_cpm.npy"), lc.astype(np.float32))
    np.save(os.path.join(fx, "expr_mask.npy"), np.ones((L, G), bool))
    np.save(os.path.join(out, "tensor", "line_measured.npy"), np.ones((L, gK), bool))
    sig = np.zeros((Dn, gK), np.float32)                                     # in every line
    progs = []
    for p in range(16):
        gg, dd = np.arange(1000 + 20 * p, 1020 + 20 * p), np.arange(3 * p, 3 * p + 3)
        sig[np.ix_(dd, gg)] = 5.0
        progs.append(gg)
    B, dB = np.arange(100, 500), np.arange(200, 212, 3)
    sig[np.ix_(dB, B)] = 5.0
    P, Q, dP = np.arange(600, 900), np.arange(900, 1000), np.arange(250, 262, 3)
    sig[np.ix_(dP, Q)] = 5.0
    sigP = np.zeros((Dn, gK), np.float32)
    sigP[np.ix_(dP, P)] = 5.0                                                # only where DOMG is intact
    lf_damp = np.where(damp, 0.3, 1.0).astype(np.float32)
    lf_dom = np.where(domg, 0.4, 1.0).astype(np.float32)
    Zp = rng.standard_normal((Dn, G)).astype(np.float32) * 0.3
    Zp[:, :gK] += sig * float(lf_damp.mean())
    Zp[np.ix_(dP, P)] = 4.0                                                  # P: significant pooled (the median line)
    Zp[np.ix_(dB[[1, 3]], B)] = 2.5                                          # near the threshold: not significant
    q = np.where(np.abs(Zp) >= 3, 1e-5, 1.0).astype(np.float32)
    np.save(os.path.join(fx, "DD_z.npy"), Zp)
    np.save(os.path.join(fx, "DD_lfc.npy"), (Zp * 0.15).astype(np.float32))
    np.save(os.path.join(fx, "DD_qup.npy"), q)
    np.save(os.path.join(fx, "DD_qdn.npy"), np.ones((Dn, G), np.float32))
    A = rng.normal(0, 0.3, (Dn, L))
    np.save(os.path.join(fx, "DD_A.npy"), A.astype(np.float32))
    np.save(os.path.join(fx, "DD_Az.npy"), (A / 0.3).astype(np.float32))
    Zt = open_memmap(os.path.join(out, "tensor", "DDL_z.npy"), (gK, Dn, L), np.float32)
    for g0 in range(0, gK, 500):
        g1 = min(gK, g0 + 500)
        z = rng.standard_normal((g1 - g0, Dn, L), dtype=np.float32)
        z += sig[:, g0:g1].T[:, :, None] * lf_damp[None, None, :]
        z += sigP[:, g0:g1].T[:, :, None] * (lf_damp * lf_dom)[None, None, :]
        Zt[g0:g1] = z
    del Zt
    _link_or_copy_lfc(os.path.join(out, "tensor"), 0.15)
    a = np.repeat(np.arange(gK), 30)
    b = rng.integers(0, gK, a.size)
    ex = []
    for gg in progs + [P, Q]:
        pa, pb = np.meshgrid(gg, gg)
        k = pa.ravel() != pb.ravel()
        ex.append((pa.ravel()[k], pb.ravel()[k]))
    a = np.r_[a, np.concatenate([x[0] for x in ex])]
    b = np.r_[b, np.concatenate([x[1] for x in ex])]
    m = a != b
    pd.DataFrame({"col_a": a[m], "col_b": b[m], "cos": rng.uniform(0.3, 0.9, int(m.sum())).astype(np.float32)}) \
        .to_parquet(os.path.join(out, "relations", "gene_relations.parquet"), index=False)
    return out, data, {"P": P, "Q": Q, "B": B, "progs": np.concatenate(progs)}


def small_fixture_checks(work):
    root = os.path.join(work, "fixture50")
    out, data, plant = make_small_fixture(root)
    rc, dt, info, _ = run_stage(out, data, ("--pseudo", "20"))
    report("50-line fixture: stage finishes", lambda: (rc == 0, f"exit code {rc} in {dt:.0f} s; correction "
                                                              f"{info.get('global_sensitivity_correction')}"))
    if rc != 0:
        return
    e, _, _ = load(out)
    r = e[e["kind"] == "genotype_response"]

    def names(ix):
        return {f"FG{i:05d}" for i in ix}

    def dom():
        d = r[r["source"] == "DOMG"]
        p = d[d["target"].isin(names(plant["P"]))]
        q = d[d["target"].isin(names(plant["Q"]))]
        pa = int(((p["sign"] == 1) & (p["grade"] == "A")).sum())
        q_al = int(q["alerts"].str.contains("exists only relative").sum())
        q_c = int((~q["alerts"].str.contains("exists only relative") & (q["grade"] == "C")).sum())
        ok = pa >= 0.9 * len(plant["P"]) and (q["grade"] == "A").sum() == 0 and q_al + q_c == len(q) and \
            q_al >= 0.5 * len(plant["Q"])
        return ok, (f"DOMG -> P: {len(p)} of {len(plant['P'])} edges, {pa} grade A with sign +1; DOMG -> Q (same "
                    f"response in every line): {len(q)} edges, grades {q['grade'].value_counts().to_dict()}, "
                    f"{q_al} of them alerted as resting on the correction (raw_share median "
                    f"{q['raw_share'].median() if len(q) else float('nan'):.2f}), {q_c} other (grade C leads)")
    report("50-line fixture: a dominant genotype-dependent programme does not create grade-A edges elsewhere", dom)

    def damp():
        d = e[e["source"] == "DAMP"]
        planted = names(np.r_[plant["P"], plant["Q"], plant["B"], plant["progs"]])
        n = int(d["target"].isin(planted).sum())
        return n <= 0.02 * len(planted), (
            f"DAMP (0.3x of every planted response in its 25 lines, narrow, near-threshold and broad drug-doses) "
            f"-> {n} of the {len(planted)} planted responsive genes ({len(d)} DAMP edges in all, grades "
            f"{d['grade'].value_counts().to_dict()}); the line-wide responsiveness absorbs it")
    report("50-line fixture: a line-wide damping is not called gene-specific", damp)

    def nullg():
        d = e[e["source"] == "NULLG"]
        return len(d) <= 3, f"random group NULLG (20 lines): {len(d)} edges {d[['kind', 'grade']].values.tolist()}"
    report("50-line fixture: a random group gives ~no edges", nullg)
    shutil.rmtree(os.path.join(out, "tensor"), ignore_errors=True)


# ----------------------------------------------------------------------------- 4. scale fixture
ORGANS = [("Lung", 14), ("Pancreas", 6), ("Bowel", 6), ("Breast", 4), ("Skin", 3), ("Ovary", 3), ("Kidney", 2),
          ("Liver", 2), ("Stomach", 2), ("Esophagus", 2), ("Bladder", 1), ("Uterus", 1), ("Cervix", 1), ("CNS", 1),
          ("Bone", 1), ("HeadNeck", 1)]
NAMED = {"TP53": 50, "KRAS": 51, "CDKN2A": 52, "CDKN2B": 53, "KEAP1": 55, "MTAP": 64, "NQO1": 70, "HMOX1": 71,
         "AKR1C1": 72, "AKR1C2": 73, "TXNRD1": 74, "GCLM": 75, "SRXN1": 76, "NULLX": 700, "LEVX": 800}


def make_fixture(root, gK, Dn=1132, L=50, seed=1):
    """A tahoemap output with the real numbers of drug-doses and lines (see the module docstring, 4)."""
    from tahoemap.common import open_memmap
    rng = np.random.default_rng(seed)
    shutil.rmtree(root, ignore_errors=True)
    out, data = os.path.join(root, "out"), os.path.join(root, "data")
    organ = np.array(sum([[o] * n for o, n in ORGANS], []), dtype=object)[rng.permutation(L)]
    fx, G, sym, pc = _write_common(out, data, gK, Dn, L, organ, rng)
    for s, i in NAMED.items():
        sym[i] = s
    pd.DataFrame({"col": np.arange(G), "kind": ["gene"] * gK + ["module"] * 3, "token": np.arange(3, 3 + G),
                  "symbol": sym, "label": sym, "pooled_cpm": pc, "median_line_cpm": pc,
                  "n_lines_expressing": L}).to_csv(os.path.join(fx, "genes.csv"), index=False)
    rows = []
    for i in range(Dn):
        d = i // 3
        tg = f"TGT{d % 40}, TGT{d % 40 + 1}" if d % 3 == 0 else ""
        rows.append({"drug": f"Drug{d:03d}", "dose": ["0.05", "0.5", "5"][i % 3], "conc": [0.05, 0.5, 5.0][i % 3],
                     "flags": "", "targets": tg, "moa_broad": "inhibitor/antagonist", "plates": "p1", "wells": "A1"})
    pd.DataFrame(rows).to_csv(os.path.join(fx, "drugdose.csv"), index=False)
    pd.DataFrame({"cell_line_id": [f"CVCL_F{i:03d}" for i in range(L)], "cell_name": [f"Line{i:02d}" for i in range(L)],
                  "Organ": organ, "in_growth_analysis": True}).to_csv(os.path.join(fx, "lines.csv"), index=False)
    oi = {o: np.flatnonzero(organ == o) for o, _ in ORGANS}

    def within(frac, s):
        r = np.random.default_rng(s)
        m = np.zeros(L, bool)
        for idx in oi.values():
            k = int(round(frac * idx.size))
            if idx.size >= 2:
                k = min(max(k, 1), idx.size - 1)
            m[r.choice(idx, size=k, replace=False)] = True
        return m
    dep, res, tp53, cdkn2a = within(0.5, 11), within(0.5, 12), within(0.68, 13), within(0.45, 14)
    keap1 = np.zeros(L, bool)
    keap1[oi["Lung"][6:12]] = True
    hyper = np.zeros(L, bool)
    hyper[np.r_[oi["Bowel"][3:6], oi["Stomach"][:1], oi["Uterus"][:1], oi["Lung"][12:13]]] = True
    meta = []

    def add(i, gene, mech, vt="Missense"):
        meta.append({"cell_name": f"Line{i:02d}", "Cell_ID_DepMap": f"ACH-{i:06d}",
                     "Cell_ID_Cellosaur": f"CVCL_F{i:03d}", "Organ": organ[i], "Driver_Gene_Symbol": gene,
                     "Driver_VarZyg": "Hom", "Driver_VarType": vt,
                     "Driver_ProtEffect_or_CdnaEffect": "p.X1Y", "Driver_Mech_InferDM": mech,
                     "Driver_GeneType_DM": "Suppressor"})
    pool = [f"HYP{k:03d}" for k in range(150)]
    for i in range(L):
        add(i, "ANCHOR", None)
        if dep[i]:
            add(i, "FAKEDEP", "LoF")
        if res[i]:
            add(i, "FAKERES", "LoF")
        if tp53[i]:
            add(i, "TP53", "LoF" if rng.random() < 0.8 else None)
        if cdkn2a[i]:
            add(i, "CDKN2A", "LoF", "Deletion")
            if rng.random() < 0.7:
                add(i, "CDKN2B", "LoF", "Deletion")
        if keap1[i]:
            add(i, "KEAP1", "LoF")
        for k in range(60):                                               # random drivers: ~3-15 lines each
            if rng.random() < 0.03 + 0.15 * (k % 7) / 7:
                add(i, f"DRV{k:02d}", ["LoF", "GoF", None][k % 3])
        if hyper[i]:
            for gname in rng.choice(pool, size=30, replace=False):
                add(i, gname, [None, "LoF", "LoF", "GoF"][int(rng.integers(4))])
    pd.DataFrame(meta).to_parquet(os.path.join(data, "metadata", "cell_line_metadata.parquet"), index=False)
    # baseline: line-to-line variation; ~45% of genes absent from 1-4 organs (and a few flipped lines), 5% from a
    # few random lines
    lc = pc[None, :] * np.exp(rng.normal(0, 0.5, (L, G)))
    absent = np.zeros((L, G), bool)
    u = rng.random(gK)
    orgs = list(oi)
    for x in np.flatnonzero(u < 0.45):
        chosen = rng.choice(len(orgs), size=int(rng.integers(1, 5)), replace=False)
        absent[:, x] = np.isin(organ, [orgs[j] for j in chosen]) ^ (rng.random(L) < 0.08)
    for x in np.flatnonzero((u >= 0.45) & (u < 0.5)):
        absent[rng.choice(L, size=int(rng.integers(3, 8)), replace=False), x] = True
    nullx = within(0.2, 15)
    absent[:, 700] = nullx
    absent[:, 701:746] = False
    absent[:, 801:831] = False
    for name, x in NAMED.items():
        if name not in ("NULLX", "MTAP"):
            absent[:, x] = False
    absent[:, NAMED["MTAP"]] = cdkn2a                                       # MTAP lost with the CDKN2A deletion
    lc[absent] = pc[None, :].repeat(L, 0)[absent] * 0.05
    for s in ("NQO1", "HMOX1", "AKR1C1", "AKR1C2", "TXNRD1", "GCLM", "SRXN1"):
        lc[keap1, NAMED[s]] *= 5.0                                          # KEAP1 loss raises the NRF2 targets
    lc[np.ix_(nullx, np.arange(731, 746))] /= 4.0                          # NULLX absent: partners 4x lower
    levx = rng.normal(0, 1.0, L)
    lc[:, 800] = pc[800] * np.exp(levx)                                     # LEVX's level varies strongly
    np.save(os.path.join(fx, "line_cpm.npy"), lc.astype(np.float32))
    np.save(os.path.join(fx, "expr_mask.npy"), np.ones((L, G), bool))
    meas = ~absent[:, :gK]
    np.save(os.path.join(out, "tensor", "line_measured.npy"), meas)
    prog, d1 = np.arange(100, 140), np.arange(30, 36)
    broad, d2 = np.arange(200, 600), np.arange(60, 72, 3)
    nprog, dnull = np.arange(701, 731), np.arange(240, 246)
    lprog, dlev = np.arange(801, 831), np.arange(300, 306)
    # 40 compounds (2 doses each) that move 15 genes each in every line, as most drugs do: the lines' overall
    # responsiveness is read from such responses
    uni = [(np.arange(1000 + 15 * p, 1015 + 15 * p), 3 * (140 + p) + np.array([1, 2])) for p in range(40)]
    Zp = rng.standard_normal((Dn, G)).astype(np.float32)
    q = np.ones((Dn, G), np.float32)
    for P_, D_, zv, qv in [(prog, d1, 4.0, 1e-4), (broad, d2, 5.0, 1e-6), (nprog, dnull, 4.0, 1e-4),
                           (lprog, dlev, 4.0, 1e-4)] + [(u, d, 4.0, 1e-4) for u, d in uni]:
        Zp[np.ix_(D_, P_)] = zv
        q[np.ix_(D_, P_)] = qv
    np.save(os.path.join(fx, "DD_z.npy"), Zp)
    np.save(os.path.join(fx, "DD_lfc.npy"), (Zp * 0.15).astype(np.float32))
    np.save(os.path.join(fx, "DD_qup.npy"), q)
    np.save(os.path.join(fx, "DD_qdn.npy"), np.ones((Dn, G), np.float32))
    # cell numbers: line-specific drug effects (most drug-doses differ between lines) + planted effects
    A = rng.normal(0, 0.3, (Dn, L)) + rng.normal(0, 0.4, (Dn, 1)) * rng.normal(0, 1, (1, L))
    A[10] = rng.normal(0, 0.3, L)
    A[10, ~dep] -= 1.0                                                      # FAKEDEP-intact lines grow less
    lvl = np.log2(lc[:, 600] + 1)
    A[11] = rng.normal(0, 0.3, L) - 0.8 * (lvl - lvl.mean()) / lvl.std()    # FG00600's level -> sensitivity
    A[12] = rng.normal(0, 0.3, L)
    A[12, absent[:, NAMED["MTAP"]]] -= 1.2                                  # MTAP-null lines depleted
    A[13] = rng.normal(0, 0.3, L)
    A[13, tp53] += 0.9                                                      # TP53-altered lines resist
    np.save(os.path.join(fx, "DD_A.npy"), A.astype(np.float32))
    np.save(os.path.join(fx, "DD_Az.npy"), (A / 0.3).astype(np.float32))
    Zt = open_memmap(os.path.join(out, "tensor", "DDL_z.npy"), (gK, Dn, L), np.float32)
    levs = (levx - levx.mean()) / levx.std()
    for g0 in range(0, gK, 500):
        g1 = min(gK, g0 + 500)
        z = rng.standard_normal((g1 - g0, Dn, L), dtype=np.float32)
        for x in range(g0, g1):
            zz = z[x - g0]
            if 100 <= x < 140:
                zz[np.ix_(d1, np.flatnonzero(~dep))] += 6.0                 # only where FAKEDEP is intact
                zz[np.ix_(d1, np.flatnonzero(dep))] += 0.3
            if 200 <= x < 600:
                zz[np.ix_(d2, np.flatnonzero(~res))] += 5.0
                zz[np.ix_(d2, np.flatnonzero(res))] += 1.5                  # 0.3x: global resistance
            if 701 <= x < 731:
                zz[np.ix_(dnull, np.flatnonzero(~nullx))] += 6.0            # only where NULLX is expressed
                zz[np.ix_(dnull, np.flatnonzero(nullx))] += 0.5
            if 801 <= x < 831:
                zz[dlev] += (4.0 + 2.0 * levs)[None, :]                     # scales with LEVX's level
            if 1000 <= x < 1600:
                zz[uni[(x - 1000) // 15][1]] += 4.0                         # every line
        z[~meas[:, g0:g1].T[:, None, :].repeat(Dn, 1)] = np.nan
        Zt[g0:g1] = z
    del Zt
    _link_or_copy_lfc(os.path.join(out, "tensor"), 0.15)
    a = np.repeat(np.arange(gK), 100)
    b = rng.integers(0, gK, a.size)
    ex = []
    for P_ in [prog, np.r_[700, nprog, np.arange(731, 746)], np.r_[800, lprog]] + [u for u, _ in uni]:
        pa, pb = np.meshgrid(P_, P_)
        k = pa.ravel() != pb.ravel()
        ex.append((pa.ravel()[k], pb.ravel()[k]))
    a = np.r_[a, np.concatenate([x[0] for x in ex])]
    b = np.r_[b, np.concatenate([x[1] for x in ex])]
    m = a != b
    pd.DataFrame({"col_a": a[m], "col_b": b[m], "cos": rng.uniform(0.3, 0.9, int(m.sum())).astype(np.float32)}) \
        .to_parquet(os.path.join(out, "relations", "gene_relations.parquet"), index=False)
    return out, data, {"prog": prog, "broad": broad, "nprog": nprog, "nbase": np.arange(731, 746), "lprog": lprog}


def scale_checks(work, sizes):
    pts = []
    for gK in sizes:
        root = os.path.join(work, f"scale_{gK}")
        t0 = time.time()
        out, data, plant = make_fixture(root, gK)
        print(f"  fixture with {gK:,} genes x 1,132 drug-doses x 50 lines made in {(time.time() - t0) / 60:.1f} min",
              flush=True)
        rc, dt, info, _ = run_stage(out, data)
        shutil.rmtree(os.path.join(out, "tensor"), ignore_errors=True)       # free the disk for the next one
        pts.append((gK, rc, dt, info, out, plant))
        if rc != 0:
            break
    ok_runs = [p for p in pts if p[1] == 0]
    report("scale runs finish", lambda: (len(ok_runs) == len(sizes), "; ".join(
        f"{p[0]:,} genes: exit {p[1]}, {p[2] / 60:.2f} min, peak {p[3].get('peak_rss_mb')} MB" for p in pts)))
    if not ok_runs:
        return
    gK, _, _, info, out, plant = ok_runs[-1]
    e, g, ctl = load(out)
    tw = table_wide(e)

    def names(ix):
        return set(f"FG{i:05d}" for i in ix)

    def programme():
        r = e[(e["kind"] == "genotype_response") & (e["source"] == "FAKEDEP")]
        tg = names(plant["prog"])
        hit = r[r["target"].isin(tg) & (r["sign"] == 1)]
        prec = len(r[r["target"].isin(tg)]) / max(1, len(r))
        return len(hit) >= 0.8 * len(tg) and prec >= 0.8 and (hit["grade"] == "A").mean() >= 0.8, (
            f"FAKEDEP -> {len(hit)} of {len(tg)} programme genes (sign +1), {len(r)} FAKEDEP response edges "
            f"({prec:.0%} in the programme); grades {hit['grade'].value_counts().to_dict()}")
    report(f"scale ({gK:,} genes): a genotype-dependent programme is found (grade A)", programme)

    def global_res():
        r = e[(e["kind"] == "genotype_response") & (e["source"] == "FAKERES")]
        tg = names(plant["broad"])
        n = int(r["target"].isin(tg).sum())
        return n <= 0.05 * len(tg), (f"FAKERES (0.3x response in its lines at 4 broad drug-doses) -> {n} of the "
                                     f"{len(tg)} genes that respond there")
    report(f"scale ({gK:,} genes): a line-wide global resistance is not called gene-specific", global_res)

    def planted_cells():
        s = e[(e["kind"] == "genotype_sensitivity") & (e["source"] == "FAKEDEP") & (e["target_dd"] == 10) & tw]
        t = e[(e["kind"] == "genotype_sensitivity") & (e["source"] == "TP53") & (e["target_dd"] == 13) & tw]
        lv = e[(e["kind"] == "level_sensitivity") & (e["source"] == "FG00600") & (e["target_dd"] == 11) & tw]
        mt = e[(e["kind"] == "null_sensitivity") & (e["source"] == "MTAP") & (e["target_dd"] == 12)]
        ok = (len(s) == 1 and (s["sign"] == -1).all() and (t["sign"] == -1).any() and (t["sign"] != 1).all()
              and len(lv) == 1 and (lv["sign"] == -1).all() and len(mt) >= 1 and (mt["sign"] == 1).all())
        nt = info["tests"]["expression_null"]
        n_null = nt.get("sensitivity_within_organs", 0) + nt.get("sensitivity_across_organs", 0)
        return ok, (f"FAKEDEP -> cells (sign {s['sign'].tolist()}); TP53 -> cells (sign {t['sign'].tolist()}: -1 for "
                    "loss of function, 0 = not inferred for 'altered (any record)'; "
                    f"{t['group'].tolist()}); FG00600 level -> cells (sign {lv['sign'].tolist()}, q "
                    f"{lv['q'].round(6).tolist()}); MTAP-null -> cells, a lone effect among {n_null:,} tests (sign "
                    f"{mt['sign'].tolist()}, q {mt['q'].round(6).tolist()}, grade {mt['grade'].tolist()})")
    report(f"scale ({gK:,} genes): planted effects on cell numbers (genotype, level, lone natural knockout)",
          planted_cells)

    def keap1():
        b = e[(e["kind"] == "genotype_baseline") & (e["source"] == "KEAP1")]
        tg = {"NQO1", "HMOX1", "AKR1C1", "AKR1C2", "TXNRD1", "GCLM", "SRXN1"}
        h = b[b["target"].isin(tg)]
        return len(h) >= 3 and (h["sign"] == -1).all(), (
            f"KEAP1 (6 Lung lines; targets 5x) -> {len(h)} of 7 NRF2 targets at baseline, signs {h['sign'].tolist()}, "
            "grades "
            f"{h['grade'].value_counts().to_dict()}")
    report(f"scale ({gK:,} genes): KEAP1 -> NRF2 targets (baseline, sign -1)", keap1)

    def nullx():
        rr = e[(e["kind"] == "null_response") & (e["source"] == "NULLX") & e["target"].isin(names(plant["nprog"]))]
        bb = e[(e["kind"] == "null_baseline") & (e["source"] == "NULLX") & e["target"].isin(names(plant["nbase"]))]
        return len(rr) >= 0.6 * len(plant["nprog"]) and len(bb) >= 0.6 * len(plant["nbase"]) and \
            (rr["sign"] == 1).all() and (bb["sign"] == 1).all(), (
                f"NULLX-null (12 lines) -> {len(rr)} of {len(plant['nprog'])} partners' responses, {len(bb)} of "
                f"{len(plant['nbase'])} partners' baseline levels (4x lower; sign +1), grades "
                f"{pd.concat([rr, bb])['grade'].value_counts().to_dict()}")
    report(f"scale ({gK:,} genes): a natural knockout's partner effects (null_response, null_baseline)", nullx)

    def levx():
        lv = e[(e["kind"] == "level") & (e["source"] == "LEVX") & e["target"].isin(names(plant["lprog"]))]
        clear = int(lv["direction_clear"].fillna(False).astype(bool).sum())
        rev = e[(e["kind"] == "level") & (e["target"] == "LEVX") & (e["direction_clear"].fillna(False).astype(bool))]
        return len(lv) >= 0.6 * len(plant["lprog"]) and clear >= 0.5 * len(lv) and len(rev) == 0, (
            f"LEVX's level -> {len(lv)} of {len(plant['lprog'])} partners' responses (q max "
            f"{lv['q'].max() if len(lv) else float('nan'):.2g}), {clear} with the direction clear; reverse edges "
            f"called clear: {len(rev)}; among {info['tests']['level_pairs']:,} directed pairs")
    report(f"scale ({gK:,} genes): a level modulator -> its partners (level, direction clear)", levx)

    def negatives():
        s = ctl["negative"]["summary"]
        rnd = e[e["source"].str.match(r"^(DRV\d+|HYP\d+)$") & e["kind"].str.startswith("genotype")]
        rnd_tw = rnd[table_wide(rnd)]
        n_rnd = int(g[(g["kind"] == "genotype") & g["gene"].str.match(r"^(DRV\d+|HYP\d+)$")].shape[0])
        rate = sum((v["pseudo_edges_mean_per_group"] or 0) for v in s.values())
        ok = all((v["pseudo_edges_mean_per_group"] or 0) <= 0.2 for v in s.values()) and \
            len(rnd_tw) <= max(5.0, 2.0 * rate * n_rnd)
        return ok, ("; ".join(f"{k}: pseudo {v['pseudo_edges_mean_per_group']} vs real "
                              f"{v['real_edges_mean_per_group']} table-wide edges per group" for k, v in s.items())
                    + f"; random driver groups (DRV / HYP, {n_rnd} groups, no planted effect): {len(rnd_tw)} "
                      f"table-wide edges (the pseudo rate predicts {rate * n_rnd:.1f}), {len(rnd) - len(rnd_tw)} "
                      "within their group only (grade C)")
    report(f"scale ({gK:,} genes): pseudo-groups and random driver groups give ~no edges", negatives)

    def tissue():
        ps = g[g["kind"] == "pseudo"]
        rd = g[(g["kind"] == "genotype") & g["gene"].str.match(r"^(DRV\d+|HYP\d+)$")]
        a, b = float(ps["tissue_confounded"].mean()), float(rd["tissue_confounded"].mean())
        nul = info["groups_tested"]
        return a <= 0.2 and b <= 0.25 and nul["expression_null_line_sets_across_organs"] > 0, (
            f"tissue-confounded: {a:.0%} of {len(ps)} pseudo-groups, {b:.0%} of {len(rd)} random driver groups (16 "
            f"organs, Lung 14 of 50 lines); expression-null sets compared across organs (tested, separate BH "
            f"family): {nul['expression_null_line_sets_across_organs']:,} of {nul['expression_null_line_sets']:,}")
    report(f"scale ({gK:,} genes): the tissue alert fires only on organ-concentrated comparisons", tissue)

    def controls():
        ef = info["expected_false_edges"]
        lv = ctl["level_controls"]
        ok = all((ef[k]["expected_false"] or 0) <= 0.1 * ef[k]["edges"] + 3 for k in ("level", "level_sensitivity"))
        return ok, ("expected false edges: " + "; ".join(f"{k} {v['expected_false']} of {v['edges']}"
                                                           for k, v in ef.items())
                    + f"; level calibration {lv['level'].get('calibration')}; level_sensitivity calibration "
                      f"{lv['level_sensitivity'].get('calibration')}, {info['variable_drugdoses']} variable "
                      "drug-doses")
    report(f"scale ({gK:,} genes): permuted-level controls give no more level edges than the 10% FDR allows",
          controls)

    def extrapolate():
        if len(ok_runs) < 2:
            g_, _, dt, inf, _, _ = ok_runs[0]
            mem = inf["peak_rss_mb"] / 1024 * max(1.0, FULL_GENES / g_)
            mins = dt / 60 * max(1.0, FULL_GENES / g_)
        else:
            (g1, _, t1, i1, _, _), (g2, _, t2, i2, _, _) = ok_runs[-2], ok_runs[-1]
            m1, m2 = i1["peak_rss_mb"] / 1024, i2["peak_rss_mb"] / 1024
            mem = m2 + max(0.0, (m2 - m1) / (g2 - g1) * (FULL_GENES - g2))
            mins = t2 / 60 + max(0.0, (t2 - t1) / 60 / (g2 - g1) * (FULL_GENES - g2))
        inf = ok_runs[-1][3]
        return mem <= MEM_LIMIT_GB and mins <= MINUTES_LIMIT, (
            f"{'measured at' if ok_runs[-1][0] >= FULL_GENES else 'extrapolated to'} {FULL_GENES:,} genes: peak "
            f"{mem:.2f} GB (limit {MEM_LIMIT_GB}), {mins:.1f} min (limit {MINUTES_LIMIT}; this machine: "
            f"{os.cpu_count()} CPUs); largest run: {inf.get('groups_tested')}, {inf.get('variable_drugdoses')} "
            f"variable drug-doses, chunk {inf.get('chunk')} genes")
    report("scale: bounded memory and time", extrapolate)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=None, help="a finished synthetic output (default: run_tests.py's out_seed0)")
    ap.add_argument("--data", default=None, help="its data folder (with ground_truth.json)")
    ap.add_argument("--work", default=None, help="work folder (default: a temporary folder)")
    ap.add_argument("--no-fixture", action="store_true", help="skip the 50-line fixture")
    ap.add_argument("--no-scale", action="store_true", help="skip the full-dimension scale runs")
    ap.add_argument("--scale-genes", default="4000,8000", help="genes of the scale fixtures (e.g. 16643)")
    ap.add_argument("--keep", action="store_true", help="keep the work folder")
    a = ap.parse_args()
    src = a.src or os.path.join(DEFAULT_WORKDIR, "out_seed0")
    data = a.data or os.path.join(os.path.dirname(src), "data_seed0")
    if not os.path.exists(os.path.join(src, "stages", "relations.json")):
        print(f"{src} has no finished synthetic run: making one with run_tests.py ...", flush=True)
        subprocess.run([sys.executable, os.path.join(HERE, "run_tests.py"), "--workdir", os.path.dirname(src)],
                       cwd=REPO, check=False)
    work = a.work or tempfile.mkdtemp(prefix="tahoe_direction_")
    os.makedirs(work, exist_ok=True)
    print(f"Synthetic output {src}; work folder {work}", flush=True)
    unit_checks()
    report("reasons in tiers: each threshold sends a reason to the right tier (constructed reasons)",
           tier_unit_checks)
    out = os.path.join(work, "out")
    copy_output(src, out)
    rc, dt, info, console = run_stage(out, data)
    report("stage finishes on the synthetic output", lambda: (
        rc == 0, f"exit code {rc} in {dt:.0f} s, peak memory {info.get('peak_rss_mb')} MB, "
                 f"{info.get('edges')} edges"))
    if rc == 0:
        report("synthetic run within bounded memory (< 1.5 GB)", lambda: (
            (info.get("peak_rss_mb") or 0) < 1536, f"peak RSS {info.get('peak_rss_mb')} MB, chunk {info.get('chunk')}"))
        e = synthetic_checks(out, data, info, console)
        chunk_check(src, data, work, e)
        variant_checks(src, data, work)
    if not a.no_fixture:
        small_fixture_checks(work)
    if not a.no_scale:
        scale_checks(work, [int(x) for x in a.scale_genes.split(",") if x.strip()])
    n = {s: sum(r[0] == s for r in RESULTS) for s in ("PASS", "FAIL")}
    print(f"\n{n['PASS']} passed, {n['FAIL']} failed", flush=True)
    if not a.keep and not a.work:
        shutil.rmtree(work, ignore_errors=True)
    sys.exit(1 if n["FAIL"] else 0)


if __name__ == "__main__":
    main()
