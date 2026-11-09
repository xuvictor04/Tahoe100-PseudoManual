---
symbol: "DCDC1"
type: "gene"
col: 10034
ensembl_id: "ENSG00000170959"
name: "doublecortin domain containing 1"
location: "11p14.1"
module: 10
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 49
n_dd_up: 37
n_dd_down: 16
n_dd_up_clean: 31
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# DCDC1

*doublecortin domain containing 1* — 11p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.2× (z +24.5, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.673× (z -6.0, q 1e-06, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF11]] (+0.65, fdr 7e-06), [[DNAH7]] (+0.57, fdr 1e-05), [[LNC-LBCS]] (+0.55, fdr 1e-05); moves opposite to [[THEM4]] (-0.54, fdr 6e-04), [[CARNMT1]] (-0.51, fdr 6e-05), [[WDR75]] (-0.50, fdr 0.001, ⚠ not reproduced), [[ASB13]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.2×** | +24.5 | 0e+00 | 45/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.28×** | +21.7 | 0e+00 | 32/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.21×** | +20.9 | 0e+00 | 44/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.17×** | +19.2 | 0e+00 | 44/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.75×** | +13.5 | 3e-39 | 40/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +10.5 | 6e-24 | 2/7 (HOP62, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +10.3 | 4e-23 | 8/18 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.97×** | +10.1 | 3e-22 | 23/45 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.60×** | +10.1 | 4e-22 | 25/36 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **5.97×** | +9.9 | 3e-21 | 35/42 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +9.8 | 5e-21 | 24/39 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +8.4 | 2e-15 | 21/38 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.12×** | +7.9 | 9e-14 | 19/43 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +7.5 | 2e-12 | 2/9 (HOP62, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +7.2 | 3e-11 | 18/35 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +6.6 | 1e-09 | 20/42 (A-172, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.81×** | +6.2 | 2e-08 | 16/44 (NCI-H23, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 8e-04 | 9/45 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.673×** | -6.0 | 1e-06 | 22/44 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -5.9 | 1e-06 | 18/44 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.609×** | -5.3 | 3e-05 | 14/46 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -5.0 | 1e-04 | 18/32 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.631×** | -4.9 | 1e-04 | 15/46 (SNU-1, SHP-77, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.637×** | -4.8 | 2e-04 | 17/43 (LOX-IMVI, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.675×** | -4.2 | 0.002 | 11/36 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -3.7 | 0.015 | 14/45 (LOX-IMVI, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.618×** | -3.6 | 0.016 | 5/46 (SW 1271, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.711×** | -3.6 | 0.016 | 21/46 (SW480, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.722×** | -3.3 | 0.042 | 15/43 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.732×** | -3.3 | 0.043 | 12/42 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.736×** | -3.3 | 0.050 | 11/44 (C-33 A, CFPAC-1, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.054 | 13/45 (SHP-77, A-427, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.737×** | -3.1 | 0.065 | 8/46 (H4, AN3 CA, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.14 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 23.0× (z +11.6) | — |
| [[A498 (line)]] | wt | 5.73 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 15.9× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 1.84 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 22.4× (z +10.5) | — |
| [[SW480 (line)]] | alt | 5.28 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.0487× (z -14.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 3.25 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 29.6× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 4.31 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 13.2× (z +9.6) | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0730× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -8.6) |
| [[A-172 (line)]] | wt | 2.48 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 28.8× (z +9.6) | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 3.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.100× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 3.23 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 31.9× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 3.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +10.8) | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF11]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[DNAH7]] | +0.57 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[LNC-LBCS]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[BBS9]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CFAP43]] | +0.53 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[TNKS]] | +0.52 | +0.28 / +0.49 | both halves | 3e-04 |  |
| [[LINC01414]] | +0.52 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[AK8]] | +0.51 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PACRG]] | +0.51 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[DNAI7]] | +0.51 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SPATA17]] | +0.50 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[TMEM232]] | +0.50 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM4]] | -0.54 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[CARNMT1]] | -0.51 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[WDR75]] | -0.50 | -0.16 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[ASB13]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[SLC25A15]] | -0.48 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[ZNF485]] | -0.47 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[KLHL8]] | -0.47 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[ANKS6]] | -0.45 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[MTG1]] | -0.45 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NT5M]] | -0.45 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[ACTR3B]] | -0.45 | -0.08 / -0.47 | ⚠ not reproduced | 0.003 |  |
| [[TRIM65]] | -0.45 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[METTL8]] | -0.44 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[ENTR1]] | -0.44 | -0.23 / -0.46 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DCDC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DNAI1]] | B | DNAI1 activity raises DCDC1's level | lines that do not express DNAI1 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without DNAI1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FBXO15, KCNK15-AS1, CRB1; maybe low, not absent |
| [[SPATA17]] | C | SPATA17 activity raises DCDC1's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without SPATA17 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.270). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (22.3, 38.4); signed map (54.4, 19.4). **Vector** length 57.6, 8.64% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +21.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | doublecortin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.1 — chr11:30,830,369-31,369,810 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46154; previously DCDC5 |
| Gene groups (HGNC) | Doublecortin superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [M0R2J8](https://www.uniprot.org/uniprotkb/M0R2J8) (Doublecortin domain-containing protein 1):

> Microtubule-binding protein which plays an important role in mediating dynein-dependent transport of RAB8A-positive vesicles to the midbody during cytokinesis.

**Summary**, from NCBI Gene [341019](https://www.ncbi.nlm.nih.gov/gene/341019):

> This gene encodes a member of the doublecortin family. The protein encoded by this gene is a hydrophilic, intracellular protein. It contains a single doublecortin domain and is unable to bind microtubules and to regulate microtubule polymerization. This gene is mainly expressed in adult testis. It does not have a mouse homolog. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:20625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20625) · Entrez [341019](https://www.ncbi.nlm.nih.gov/gene/341019) · UniProt [M0R2J8](https://www.uniprot.org/uniprotkb/M0R2J8) · Ensembl [ENSG00000170959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170959)

## Data

Gene col 10034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10034); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10034]; `tensor/DDL_lfc|DDL_z.npy` [10034]; `embed/gene_vectors.npy` [10034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10034 or target_col == 10034). Every well: [[DCDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
