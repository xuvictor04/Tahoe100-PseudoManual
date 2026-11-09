---
symbol: "FAM76B"
type: "gene"
col: 1188
ensembl_id: "ENSG00000077458"
name: "family with sequence similarity 76 member B"
location: "11q21"
module: 130
arm: "+"
pooled_cpm: 42.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# FAM76B

*family with sequence similarity 76 member B* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +17.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Peretinoin (drug)]] 5 µM: 0.788× (z -5.1, q 1e-04, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPLL]] (+0.62, fdr 1e-05), [[TAPT1]] (+0.59, fdr 3e-05), [[DYRK4]] (+0.59, fdr 1e-05); moves opposite to [[CMIP]] (-0.57, fdr 2e-05), [[NF2]] (-0.53, fdr 4e-05), [[CLPB]] (-0.51, fdr 3e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +17.9 | 0e+00 | 42/48 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +7.6 | 8e-12 | 26/48 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.3 | 6e-11 | 25/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.2 | 3e-05 | 22/48 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +4.7 | 3e-04 | 17/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.5 | 6e-04 | 17/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.5 | 6e-04 | 21/48 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 0.001 | 20/48 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +4.3 | 0.001 | 16/48 (C-33 A, SK-MEL-2, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.18× | +3.7 | 0.011 | 21/47 (KATO III, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.051 | 4/48 (C32, SW48, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | 1.16× | +3.1 | 0.097 | 17/47 (LoVo, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1188.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | **0.788×** | -5.1 | 1e-04 | 23/47 (NCI-H23, J82, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -5.1 | 1e-04 | 0/48 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -4.9 | 2e-04 | 22/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.805×** | -4.8 | 2e-04 | 19/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.816×** | -4.5 | 7e-04 | 20/47 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.817×** | -4.5 | 7e-04 | 13/48 (NCI-H1792, SNU-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.817×** | -4.3 | 0.001 | 21/40 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.840× | -3.7 | 0.018 | 21/48 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.733×** | -3.6 | 0.020 | 13/46 (HT-29, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.852× | -3.6 | 0.021 | 12/47 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.854× | -3.5 | 0.023 | 14/48 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -3.3 | 0.039 | 10/48 (PANC-1, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.867× | -3.2 | 0.064 | 13/48 (COLO 205, RPMI-7951, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.873× | -3.0 | 0.100 | 13/47 (HT-29, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 71.8 | 6 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.04× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 48.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.151× (z -8.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[KATO III (line)]] | alt | 65.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 43.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) | [[Lonafarnib (drug)]] 5 µM 0.142× (z -9.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 68.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.492× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 69.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 32.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +13.2) | — |
| [[HCT15 (line)]] | alt | 39.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 46.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 41.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.213× (z -10.6) |
| [[J82 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 53.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.6) | — |
| [[RKO (line)]] | wt | 26.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.118× (z -11.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 1 | — | [[4EGI-1 (drug)]] 5 µM 0.0651× (z -8.6) |
| [[SW 1271 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 39.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 55.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +16.8) | — |
| [[SW48 (line)]] | wt | 33.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.6) | — |
| [[A-172 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPLL]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TAPT1]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[DYRK4]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PUS10]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[MFSD8]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CEP44]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LNX2]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LSM8]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[C14orf28]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[NUP133]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CMC4]] | +0.53 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[CEP57]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 | STRING 545; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NCOA2]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMIP]] | -0.57 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[NF2]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CLPB]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[RRP7BP-1]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[DFFA]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[FLNC]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[STIP1]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[YWHAG]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PLCXD2]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MRPS28]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[FERMT3]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[HSP90AA1]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM76B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.4, -53.6); signed map (-0.9, 1.4). **Vector** length 92.0, 19.0% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.4 | +1.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | -5.3 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 76 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:95,768,953-95,790,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33371 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5HYJ3](https://www.uniprot.org/uniprotkb/Q5HYJ3) (Protein FAM76B):

> Negatively regulates the NF-kappa-B-mediated inflammatory pathway by preventing the translocation of HNRNPA2B1 from the nucleus to the cytoplasm. Inhibits the PI3K/Akt/NF-kappa-B pathway-mediated polarization of M1 macrophages by binding to and stabilizing PIK3CD mRNA, resulting in increased levels of PIK3CD protein and increased levels of phosphorylated downstream target AKT which leads to decreased NF-kappa-B signaling.

**Summary**, from NCBI Gene [143684](https://www.ncbi.nlm.nih.gov/gene/143684):

> Predicted to enable RNA binding activity. Involved in several processes, including mRNA stabilization; negative regulation of macrophage activation; and negative regulation of protein export from nucleus. Located in nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28492) · Entrez [143684](https://www.ncbi.nlm.nih.gov/gene/143684) · UniProt [Q5HYJ3](https://www.uniprot.org/uniprotkb/Q5HYJ3) · Ensembl [ENSG00000077458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077458)

## Data

Gene col 1188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1188); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1188]; `tensor/DDL_lfc|DDL_z.npy` [1188]; `embed/gene_vectors.npy` [1188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1188 or target_col == 1188). Every well: [[FAM76B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM76B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
