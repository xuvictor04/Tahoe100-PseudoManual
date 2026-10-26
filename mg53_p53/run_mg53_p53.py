#!/usr/bin/env python3
"""Run the MG53 (TRIM72) / p53 analysis on a computed Tahoe-100M folder, then build the summary tables.

Needs a method-v3 atlas (<data>/atlas: 'tahoe_atlas.py compute', with its pseudobulk/ kept) and a gene panel run
(<data>/gene_panel: 'tahoe_gene_panel.py all'); nothing is read from the 340 GB of cells again, and nothing is written
into atlas/ or gene_panel/. Each step runs one script of this folder with its tables going to <out>/<step>/tables:

    python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M                 # all data steps + summary (~45 min)
    python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps summary # rebuild the summary tables only
    python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps literature   # optional; needs internet

Steps (default: all but literature, in this order):
  perturbations   upstream_perturbations/trim72_upstream_landscape.py  which drug-doses and classes move TRIM72 (~1 min)
  coregulation    upstream_coregulation/upstream_coregulation.py       co-regulated genes, baseline partners, locus
                  (~25 min the first time: one pass over atlas/pseudobulk; downloads TF list, HGNC and Ensembl
                  coordinates into <out>/upstream_coregulation/external, so it needs internet once)
  p53_dependence  p53_dependence/p53_dependence.py                     TP53-WT vs altered induction (~3 min)
  downstream      downstream_p53/downstream_p53.py                     TRIM72 vs p53 output, incl. single cells (~8 min)
  two_way         two_way/two_way.py               TRIM72 -> p53 / pathways over all drug-doses x lines, with drug-dose
                                                   and line fixed effects; TP53 WT minus altered as the control (~20 min)
  single_cell_all single_cell_all/single_cell_all.py  the same contrast in single cells of all wells, with placebo genes;
                                                   plus an ATF3-adjusted sensitivity run (one pass over gene_panel/cells)
  upstream_tf     upstream_tf/upstream_tf.py       transcription-factor activities and line features vs TRIM72
                                                   (one pass over atlas/pseudobulk; downloads CollecTRI/DoRothEA once)
  literature      literature/pubmed_screen.py + external_checks.py     PubMed/Europe PMC, p53 census, ChIP-Atlas
  summary         summary_tables.py                                    <out>/SUMMARY.md and <out>/summary/*.csv
Memory: under ~3 GB per step. Output default: <data>/mg53_p53. Log: <out>/run_mg53_p53.log.
"""
import argparse
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = {   # step: (folder, [(script, output subfolder, extra arguments, takes --data)])
    "perturbations": ("upstream_perturbations", [("trim72_upstream_landscape.py", "", [], False)]),
    "coregulation": ("upstream_coregulation", [("upstream_coregulation.py", "", [], False)]),
    "p53_dependence": ("p53_dependence", [("p53_dependence.py", "", [], True)]),
    "downstream": ("downstream_p53", [("downstream_p53.py", "", [], True)]),
    "two_way": ("two_way", [("two_way.py", "", [], True)]),
    "single_cell_all": ("single_cell_all", [("single_cell_all.py", "", [], True),
                                            ("single_cell_all.py", "adjusted_ATF3", ["--adjust", "ATF3"], True)]),
    "upstream_tf": ("upstream_tf", [("upstream_tf.py", "", [], True)]),
    "literature": ("literature", [("pubmed_screen.py", "", [], False), ("external_checks.py", "", [], False)]),
}
DEFAULT = "perturbations,coregulation,p53_dependence,downstream,two_way,single_cell_all,upstream_tf,summary"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("TAHOE_DATA") or os.path.expanduser("~/Tahoe-100M"),
                    help="Tahoe-100M folder holding atlas/ and gene_panel/ (default $TAHOE_DATA or ~/Tahoe-100M)")
    ap.add_argument("--out", default=None, help="output folder (default <data>/mg53_p53)")
    ap.add_argument("--steps", default=DEFAULT, help="comma list of: " + ", ".join(list(STEPS) + ["summary"]))
    a = ap.parse_args()
    data = os.path.abspath(os.path.expanduser(a.data))
    out = os.path.abspath(os.path.expanduser(a.out or os.path.join(data, "mg53_p53")))
    steps = [s.strip() for s in a.steps.split(",") if s.strip()]
    bad = [s for s in steps if s not in STEPS and s != "summary"]
    if bad:
        sys.exit(f"unknown step(s): {', '.join(bad)}; choose from {', '.join(list(STEPS) + ['summary'])}")
    need = [os.path.join(data, "atlas", "effects", "complete.json"), os.path.join(data, "gene_panel", "results")]
    if any(s in STEPS and s != "literature" for s in steps):
        missing = [p for p in need if not os.path.exists(p)]
        if missing:
            sys.exit("not found: " + ", ".join(missing) + "\nRun the atlas ('tahoe_atlas.py compute') and the gene panel "
                     "('tahoe_gene_panel.py all') on this folder first (or: tahoe run).")
    os.makedirs(out, exist_ok=True)
    logp = os.path.join(out, "run_mg53_p53.log")
    with open(logp, "a", encoding="utf-8") as log:
        def say(msg):
            line = time.strftime("[%H:%M:%S] ") + msg
            print(line, flush=True)
            log.write(line + "\n")
            log.flush()

        say(f"data {data}; out {out}; steps {', '.join(steps)}")
        for s in steps:
            t0 = time.time()
            if s == "summary":
                runs = [([sys.executable, os.path.join(HERE, "summary_tables.py"), "--in", out, "--data", data],
                         os.environ.copy())]
            else:
                folder, scripts = STEPS[s]
                runs = []
                for script, sub, extra, takes_data in scripts:
                    env = dict(os.environ, MG53_DATA=data, MG53_OUT=os.path.join(out, folder, sub))
                    os.makedirs(env["MG53_OUT"], exist_ok=True)
                    runs.append(([sys.executable, os.path.join(HERE, folder, script)]
                                 + (["--data", data] if takes_data else []) + extra, env))
            for cmd, env in runs:
                say(f"{s}: {' '.join(os.path.relpath(c) if c.endswith('.py') else c for c in cmd[1:])}"
                    + (f"  (out {env['MG53_OUT']})" if "MG53_OUT" in env else ""))
                p = subprocess.run(cmd, env=env, stdout=log, stderr=subprocess.STDOUT)
                if p.returncode:
                    say(f"{s} FAILED (exit {p.returncode}); the end of {logp} has the error. Finished steps are kept.")
                    sys.exit(p.returncode)
            say(f"{s} done in {(time.time() - t0) / 60:.1f} min")
        if "summary" in steps:
            say(f"Start with {os.path.join(out, 'SUMMARY.md')} (tables also in {os.path.join(out, 'summary')})")


if __name__ == "__main__":
    main()
