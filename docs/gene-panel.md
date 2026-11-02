# The gene panel: ferroptosis, pyroptosis, p53, NAPEPLD, TRIM72, ABCB1/ABCG2


`tahoe_gene_panel.py` applies the MTAP/Gankyrin method to your gene list:
- **Ferroptosis (13):** PTGS2, CHAC1, SLC7A11, GPX4, ACSL4, LPCAT3, AIFM2 (FSP1), NFE2L2, HMOX1, TFRC, FTH1, FTL, NCOA4.
- **Pyroptosis (11):** GSDMD, GSDME, NLRP3, AIM2, PYCARD (ASC), CASP1, CASP4, CASP5, CASP3, IL1B, IL18.
- **p53 (11):** TP53, CDKN1A (p21), MDM2, BBC3 (PUMA), PMAIP1 (NOXA), BAX, GADD45A, SESN1, SESN2, FDXR, ZMAT3.
- **Additional:** NAPEPLD (NAPE-PLD) and TRIM72 (MG53).
- **Drug efflux (2):** ABCB1 (MDR1, P-glycoprotein) and ABCG2 (BCRP). Both are off in most carcinoma lines and
  high in a few; the `efflux` angle asks which lines express each pump and whether its known substrates (taxanes,
  vinca alkaloids, anthracyclines for ABCB1; mitoxantrone, topotecan, irinotecan, methotrexate for ABCG2) deplete
  the pump-high lines less than the other lines in the same wells. mRNA and 24-h cell numbers cannot show transporter
  activity, so a sparing pattern is "consistent with efflux", not proof of it.

It extracts MTAP, PSMD10 (Gankyrin), CDKN2A and CDKN2B again for the cross-links, and 73 context genes (more p53
targets, NRF2, ATF4/ISR, UPR, heat shock, interferon, NF-kB) that tell a specific response from a general stress
program. Keep the current `tahoe_mtap_gankyrin.py` and `tahoe_atlas.py` next to it (copy them over older versions:
it stops when `tahoe_mtap_gankyrin.py` is older than method v3). It takes the composition shift, the plate factors
and 'wells disagree' from the computed atlas (`<data>/atlas`, `--atlas DIR|none`) once its effects are method v3, so
MTAP and PSMD10 agree between the two; without it, it fits its own plate factors and says so. An earlier
`mtap_gankyrin/` output made before v3 is still compared, but differs by design (summary.txt says why);
`tahoe mtap` redoes its analysis with v3 in minutes.

```bash
python3 tahoe_gene_panel.py check                                   # preflight: data, genes, TP53 annotation, earlier run, disk
python3 tahoe_gene_panel.py all --limit-files 30 --out panel_trial  # optional trial (minutes) in its own folder
nohup python3 tahoe_gene_panel.py all > /dev/null 2>&1 &            # the full run: extract + analyze + bundle (~1 h)
tail -f gene_panel/gene_panel.log
```
```powershell
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py check
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py all       # leave the window open; log in gene_panel\gene_panel.log
```
The trial gets its own folder so that its results, briefs and bundle never mix with the full run's; it reads only the
first files, so its cross-links to the earlier run differ by design (look at `panel_trial/results/summary.txt`, then
delete the folder). When a repo update adds genes to the built-in panel (ABCB1 and ABCG2 were added after the first
release), an extract made before them is out of date: `extract`/`all` deletes the old per-cell files and reads the
cells again, and `tahoe status` shows the panel as `done, but outdated (new genes in the panel)` with `tahoe run`
redoing it. The agent briefs are written by `analyze`: they name the Python and the scripts that ran it,
and they offer genome-wide look-ups (`tahoe_atlas.py lookup`) only if the atlas is already computed in
`<data>/atlas`. If the atlas comes later, or is computed again, rerun `python3 tahoe_gene_panel.py analyze`
(minutes) before the panel's agents: then the panel also takes the atlas's composition shift and plate factors
(`tahoe status` says when; `tahoe run` does it).

| Step | What it does | Time (estimate) |
|---|---|---|
| `extract` | One pass over all cells: per-cell counts of the panel, anchor and context genes plus the S/G2M/proteasome modules (`gene_panel/cells/`, ~2.5 GB; resumable). | ~1 h, like the MTAP/Gankyrin extract (longer from a hard drive); up to ~3 GB memory per worker + ~1 GB for the main process |
| `analyze` | Corrected drug effects per gene, pathway scores, the p53 screens, loss and level screens, cell cycle, co-regulation, cross-links, positive controls, `summary.txt`, the agent briefs, and the bundle. | a few minutes (~2-4 GB memory) |
| `agents` | One Claude agent per pathway (ferroptosis, pyroptosis, p53, napepld_trim72, efflux, crosslinks) plus an overview. | ~20-45 min |

What `analyze` does (all with the corrections above; `gene_panel/results/README_columns.txt` explains every file; a
rerun of `analyze` moves the earlier results to `gene_panel/results/previous_run/`):
- **Expression.** Which lines express each gene. A line counts as expressing a gene (and enters its drug effects)
  when it reads >= 25% of the median line, >= 1 CPM and >= 2x the level ambient RNA alone gives (ambient = the share
  of the pooled MTAP level that the MTAP-null lines read, times the gene's pooled level), so lines that only carry
  ambient RNA of a gene few lines express are left out. Genes with fewer than 2 counts per well x line profile are
  flagged `low counts` and get no calls; scores built only from such genes are flagged `low counts`. In a real
  Tahoe file, PYCARD (ASC), CASP1 and CASP5 are near zero in almost every line and GSDMD is low (median ~5 CPM).
  NLRP3, AIM2 and IL1B are expressed in a handful of lines (AIM2 e.g. in C32 and NCI-H2122; IL1B in RPMI-7951, HOP62
  and NCI-H1792), and TRIM72 is low (a few lines at ~10-20 CPM). Expect much of the inflammasome to be untestable or
  line-specific.
- **Drug effects.** Effects on every gene (`<GENE>_drug_summary.csv`, one row per drug; `..._by_dose.csv`). Every
  drug-dose carries its stress context: ISR, NRF2, UPR, heat-shock, interferon, NF-kB, p53 and cell-cycle scores,
  plus the flags of the [Method v3](#method-v3-what-changed-and-why) table and its `plate_scale` and
  `composition_shift_log2`. This shows, for example, whether CHAC1/SLC7A11/PTGS2 rise with or without a general ATF4
  stress response. Calls use the dose-level FDR. Pathway scores are the mean member z (each member on its own noise
  scale); their fold change is the mean member log2FC.
- **p53.** TP53 status comes from the cell-line driver table (any TP53 row = altered). The analysis checks:
  - which drugs raise p53 targets more in TP53-wild-type than in altered lines in the same wells, and whether that
    is `WT induction` or only `relative (altered lines fall)` (the `pattern` column);
  - a genotype-blind functional p53 status per line, with its agreement with the annotation (AUC) and the
    discordant lines;
  - whether TP53-wild-type lines are depleted more.

  The library has no MDM2 inhibitor: the expected activators are DNA-damaging drugs and antimetabolites, plus
  selinexor (XPO1 inhibitor: keeps p53 in the nucleus). CDKN1A also rises without p53 (HDAC inhibitors), so it is
  never read alone.
- **Loss and level screens.** Lines that lost a gene (e.g. GSDME silencing) are tested for selective depletion
  (the MTAP-null screen) and for re-expression (e.g. DNMT inhibitors; lines with a deletion in the cell-line metadata
  are left out of it: there is nothing to re-express). Re-expression is compared with the lines deleted for the gene
  in the same wells (pure ambient RNA) and needs >= 2 lines up and a dose pattern; lost lines that read no more than
  ambient give `lost lines read ambient only: not interpretable`. For every gene, the analysis tests whether a line's
  baseline level predicts which lines a drug depletes (the Gankyrin test), raw and within lineage.
- **Cross-links to the earlier run** (read from `<data>/mtap_gankyrin`; `--prior DIR` or `--prior none`):
  - agreement of the well map, the MTAP-null calls and the MTAP/PSMD10 effects (identical when both runs read the
    same files with the same `--min-cells`; a `--limit-files` trial differs by design);
  - Gankyrin vs p53 and NRF2 activity;
  - CDKN2A deletion (p16 and ARF lost; from the cell-line metadata, not the MTAP-null call: NCI-H460, A498 and A-427
    lost CDKN2A but keep MTAP) vs p53 activity, with MTAP-null as a 9p21 proxy. Expected: no difference in
    DNA-damage responsiveness (DNA damage activates p53 without ARF);
  - MTAP-null vs the ferroptosis genes;
  - drugs significant (drug-level FDR < 0.10) for MTAP / PSMD10 and for a panel gene, with the number expected
    among drugs of the same activity (strong drugs are in every list). Without an earlier run these are this run's
    MTAP / PSMD10 lists: the same wells, so no reproducibility claim.
- **Drug efflux** (`efflux_high_lines_growth.csv`, `efflux_substrate_test.csv`, `efflux_active_drugs.csv`, summary
  section 8). For ABCB1 and ABCG2 the analysis names the pump-high lines (those above ambient when a minority, else
  the top quarter by level) and tests whether the pump's known substrates deplete them less than the other lines in
  the same wells (`z_spared` > 0), and less than non-substrate drugs of similar potency (`auc` > 0.5), by the group
  screen and the within-lineage level-vs-growth test. At 24 h, with few pump-high lines and mostly cytostatic
  depletion, expect a weak or absent signal; mRNA and cell numbers cannot show transporter activity.
- **Positive controls** (`positive_controls.csv`, summary section 3). Each expected effect is listed with its
  verdict and whether it is expected at 24 h (`expected_at_24h`):
  - robust: DNA damage -> p53 targets (more in TP53-wild-type lines); proteasome inhibitors -> proteasome and
    heat-shock genes and HMOX1; the HSP90 inhibitor -> heat-shock genes; ciclopirox -> TFRC; antimitotics -> G2/M;
    dinaciclib -> transcription drop;
  - uncertain at 24 h or at <= 5 uM: decitabine / 5-azacytidine -> GSDME in silenced lines and interferon genes
    (demethylation needs several divisions; usually seen after days); dimethyl fumarate -> NRF2 targets and HMOX1;
    COX inhibitors -> PTGS2 (reported only).

  A robust control that is absent lowers trust in the data; an uncertain one that is absent says nothing about the
  method.

Start with `gene_panel/results/summary.txt` (section 1 checks the artifacts and the agreement with the earlier run,
section 3 the positive controls), then upload `gene_panel/gene_panel_bundle.zip` to Claude to check the numbers
before any agent runs. Scope: mRNA 24 h after the drug. That means no protein, lipid peroxidation, iron, caspase or
gasdermin cleavage, and no death mode: the reports speak of a "ferroptosis-like signature" and label hypotheses.

Agents (after Claude has checked the bundle; same SDK, API key, options, refusal rules and cost cap as the atlas).
Their progress goes to `gene_panel/agents.log`; each agent's own work log is `gene_panel/angles/<pathway>/agent.log`.
Reports: `gene_panel/reports/01_ferroptosis.md` ... `05_crosslinks.md` and `00_overview.md`; costs and status in
`gene_panel/reports/agents_summary.csv`. When the agents finish, `gene_panel/gene_panel_bundle.zip` is remade with
the reports: upload it to Claude. At most 6 agents x `--budget` (default $5) = $30; typical use is well below.
```bash
nohup python3 tahoe_gene_panel.py agents > /dev/null 2>&1 &   # or --dry-run first; --angles p53,ferroptosis for a subset
tail -f gene_panel/agents.log
```
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-..."     # in the same window
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py agents   # log: gene_panel\agents.log
```
Other options:
- `--unreliable-plates LIST|none` (default `plate13` when present) and `--atlas DIR|none` (the atlas to take the
  composition shift and plate factors from; default `<data>/atlas`): see Method v3.
- `--genes "SYM[:pathway],..."` adds genes; it needs a new `--out`, because the per-cell files of another gene list
  are never mixed. Aliases are accepted: FSP1, DFNA5, ASC, MG53, NAPE-PLD, P21, PUMA, NOXA.
- `--tp53-wt` / `--tp53-altered` override the annotation, and `--mtap-null` overrides the MTAP-null call.
- `--layout`, `--min-cells` and `--workers` work as in the MTAP/Gankyrin trial.

