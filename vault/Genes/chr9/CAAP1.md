---
symbol: "CAAP1"
type: "gene"
col: 4164
ensembl_id: "ENSG00000120159"
name: "caspase activity and apoptosis inhibitor 1"
location: "9p21.2"
module: 219
arm: "+"
pooled_cpm: 55.08
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# CAAP1

*caspase activity and apoptosis inhibitor 1* — 9p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +15.5, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.657× (z -10.1, q 2e-21, down in 25 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.789× (z -8.9, q 2e-16, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPHOSPH6]] (+0.59, fdr 1e-05), [[CWC22]] (+0.59, fdr 1e-05), [[BCAN-AS2]] (+0.59, fdr 1e-05); moves opposite to [[ADD1]] (-0.57, fdr 1e-05), [[SEC61A2]] (-0.57, fdr 3e-05), [[CDIPT]] (-0.56, fdr 3e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +15.5 | 0e+00 | 36/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +11.0 | 9e-26 | 36/47 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +10.4 | 4e-23 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +9.5 | 2e-19 | 35/47 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +8.8 | 1e-16 | 29/47 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +8.0 | 1e-13 | 28/47 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +5.1 | 3e-05 | 18/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.18× | +4.4 | 7e-04 | 15/47 (A-172, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.027 | 11/47 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.090 | 9/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.10 | 8/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -10.1 | 2e-21 | 25/43 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -8.9 | 2e-16 | 30/47 (A498, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.794×** | -5.5 | 6e-06 | 24/47 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -4.8 | 3e-04 | 21/47 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -4.4 | 0.001 | 16/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.852× | -4.2 | 0.002 | 19/47 (SW480, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -4.2 | 0.003 | 19/47 (KATO III, SW480, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.875× | -3.5 | 0.029 | 18/47 (SW480, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.5 | 0.031 | 14/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.868× | -3.4 | 0.040 | 10/47 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.917× | -3.2 | 0.062 | 8/47 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.098 | 11/48 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.891× | -3.0 | 0.10 | 6/47 (HS-578T, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 40.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 51.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.549× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 69.2 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -8.9) |
| [[A-172 (line)]] | wt | 38.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.8) | — |
| [[RKO (line)]] | wt | 88.6 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.3) |
| [[SW480 (line)]] | alt | 85.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.533× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 44.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -11.3) |
| [[A549 (line)]] | wt | 65.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -8.6) |
| [[BT-474 (line)]] | alt | 15.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 60.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 36.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 50.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 27.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.1) | — |
| [[A498 (line)]] | wt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.1) | — |
| [[CHP-212 (line)]] | wt | 91.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0512× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 99.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 48.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.3) |
| [[Hs 766T (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0955× (z -12.4) ⚠ toxic |
| [[HT-29 (line)]] | alt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.9) | — |
| [[KATO III (line)]] | alt | 82.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.391× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 71.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.461× (z -10.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 73.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.394× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 63.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -9.5) |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.84 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CWC22]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[BCAN-AS2]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[JPX]] | +0.58 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RBMXL1]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MAP9]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LINC00460]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GORAB]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[EXOC6]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CEBPZ]] | +0.56 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[TAF1A]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[METTL2A]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADD1]] | -0.57 | -0.71 / -0.53 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.57 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[CDIPT]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PCMTD1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CACNB3]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[UBE2Q2]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CTSD]] | -0.53 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[GNAS]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[DCUN1D4]] | -0.52 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[MICA]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[RUSC1]] | -0.51 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[BMPR1A]] | -0.51 | -0.54 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CAAP1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers CAAP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.5, 0.3); signed map (13.2, -48.0). **Vector** length 104, 24.5% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.7 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | caspase activity and apoptosis inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.2 — chr9:26,840,685-26,892,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13657, CAAP; previously C9orf82 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8G2](https://www.uniprot.org/uniprotkb/Q9H8G2) (Caspase activity and apoptosis inhibitor 1):

> Anti-apoptotic protein that modulates a caspase-10 dependent mitochondrial caspase-3/9 feedback amplification loop.

**Summary**, from NCBI Gene [79886](https://www.ncbi.nlm.nih.gov/gene/79886):

> Involved in negative regulation of apoptotic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25834) · Entrez [79886](https://www.ncbi.nlm.nih.gov/gene/79886) · UniProt [Q9H8G2](https://www.uniprot.org/uniprotkb/Q9H8G2) · Ensembl [ENSG00000120159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120159)

## Data

Gene col 4164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4164); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4164]; `tensor/DDL_lfc|DDL_z.npy` [4164]; `embed/gene_vectors.npy` [4164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4164 or target_col == 4164). Every well: [[CAAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
