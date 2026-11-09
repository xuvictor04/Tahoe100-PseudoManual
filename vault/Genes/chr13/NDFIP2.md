---
symbol: "NDFIP2"
type: "gene"
col: 2251
ensembl_id: "ENSG00000102471"
name: "Nedd4 family interacting protein 2"
location: "13q31.1"
module: 46
arm: "-"
pooled_cpm: 74.72
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# NDFIP2

*Nedd4 family interacting protein 2* — 13q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.51× (z +9.4, q 2e-18, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.531× (z -20.3, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST3GAL5]] (+0.59, fdr 4e-05), [[DNMBP]] (+0.58, fdr 2e-05), [[TGM2]] (+0.58, fdr 3e-05); moves opposite to [[ZCCHC8]] (-0.62, fdr 5e-05), [[DNAI4]] (-0.60, fdr 1e-04), [[RNF217-AS1]] (-0.59, fdr 4e-05).
> It sits in the **-** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +9.4 | 2e-18 | 31/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +8.9 | 2e-16 | 36/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +8.4 | 7e-15 | 34/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +6.2 | 9e-08 | 28/48 (SW480, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.1 | 2e-07 | 24/47 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +6.0 | 2e-07 | 24/47 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.5 | 5e-04 | 17/48 (J82, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.008 | 20/48 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.16× | +3.4 | 0.041 | 17/46 (J82, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.531×** | -20.3 | 0e+00 | 43/48 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -10.0 | 6e-21 | 37/49 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -9.2 | 6e-18 | 38/46 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.811×** | -6.7 | 3e-09 | 24/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -5.7 | 1e-06 | 27/46 (RKO, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.785×** | -5.5 | 4e-06 | 24/47 (CHP-212, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.800×** | -5.0 | 4e-05 | 20/48 (SW 900, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.810×** | -4.8 | 1e-04 | 23/47 (AsPC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.805×** | -4.7 | 1e-04 | 21/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.814×** | -4.7 | 2e-04 | 21/47 (HT-29, AsPC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.821×** | -4.5 | 4e-04 | 21/46 (A498, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -4.5 | 4e-04 | 17/47 (A498, Hs 766T, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.833×** | -4.4 | 4e-04 | 19/49 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.825×** | -4.4 | 5e-04 | 20/47 (AsPC-1, HT-29, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.3 | 6e-04 | 19/47 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.833×** | -4.3 | 6e-04 | 20/47 (SW 900, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.862× | -3.4 | 0.024 | 12/46 (AsPC-1, H4, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.057 | 18/47 (SW 900, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.1 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 2.13× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 98.8 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -14.8) |
| [[KATO III (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 84.5 | 0 | 3 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.448× (z -9.4) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.1) |
| [[PANC-1 (line)]] | alt | 36.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.13× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -11.4) |
| [[SW 900 (line)]] | alt | 75.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -13.5) |
| [[A498 (line)]] | wt | 84.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -10.6) |
| [[COLO 205 (line)]] | alt | 230 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -18.0) |
| [[HT-29 (line)]] | alt | 132 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -13.4) |
| [[LoVo (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -13.3) |
| [[SW1417 (line)]] | alt | 83.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.7) |
| [[SW480 (line)]] | alt | 152 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.69× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -11.2) |
| [[A549 (line)]] | wt | 38.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.6) |
| [[C32 (line)]] | wt | 54.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 90.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.4) |
| [[Hs 766T (line)]] | wt | 98.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -19.3) |
| [[hTERT-HPNE (line)]] | wt | 88.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.9) |
| [[J82 (line)]] | alt | 82.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 171 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 83.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 62.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.3) |
| [[RKO (line)]] | wt | 82.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.8) |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -8.7) |
| [[SW 1271 (line)]] | alt | 67.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0936× (z -8.6) |
| [[SW48 (line)]] | wt | 71.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.46× (z +9.2) | — |
| [[A-172 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL5]] | +0.59 | +0.44 / +0.43 | both halves | 4e-05 |  |
| [[DNMBP]] | +0.58 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TGM2]] | +0.58 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[NAPG]] | +0.57 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[HPCAL1]] | +0.56 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[ARHGAP18]] | +0.55 | +0.21 / +0.59 | both halves | 6e-04 |  |
| [[EML4]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[MPP1]] | +0.54 | +0.36 / +0.35 | both halves | 1e-04 |  |
| [[HDAC1]] | +0.53 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[DCUN1D3]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[HLTF]] | +0.53 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[PRKAR2B]] | +0.53 | +0.37 / +0.45 | both halves | 9e-05 |  |

## Genes that move opposite

*70 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC8]] | -0.62 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[DNAI4]] | -0.60 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[RNF217-AS1]] | -0.59 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FBXW4]] | -0.58 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[LINC02100]] | -0.58 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[TSTD3]] | -0.58 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[TRAF3IP2-AS1]] | -0.58 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[PLS3-AS1]] | -0.58 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[KRBOX5]] | -0.57 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[MYLK-AS1]] | -0.57 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[C2orf76]] | -0.56 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[RNF146]] | -0.56 | -0.52 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NDFIP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers NDFIP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises NDFIP2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **-** arm (projection on the module's main direction -0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.9, 15.1); signed map (4.6, 50.8). **Vector** length 119, 31.6% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.7 | +8.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.6 | +6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +9.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.6 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -20.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | Nedd4 family interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.1 — chr13:79,481,155-79,556,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1165, N4wbp5a |
| Gene groups (HGNC) | NDFIP family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV92](https://www.uniprot.org/uniprotkb/Q9NV92) (NEDD4 family-interacting protein 2):

> Activates HECT domain-containing E3 ubiquitin-protein ligases, including ITCH, NEDD4, NEDD4L, SMURF2, WWP1 and WWP2, and consequently modulates the stability of their targets. As a result, may control many cellular processes. Recruits ITCH, NEDD4 and SMURF2 to endosomal membranes. Negatively regulates KCNH2 potassium channel activity by decreasing its cell-surface expression and interfering with channel maturation through recruitment of NEDD4L to the Golgi apparatus and multivesicular body …

**Summary**, from NCBI Gene [54602](https://www.ncbi.nlm.nih.gov/gene/54602):

> Enables WW domain binding activity. Involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Located in several cellular components, including Golgi apparatus; mitochondrion; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18537) · Entrez [54602](https://www.ncbi.nlm.nih.gov/gene/54602) · UniProt [Q9NV92](https://www.uniprot.org/uniprotkb/Q9NV92) · Ensembl [ENSG00000102471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102471)

## Data

Gene col 2251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2251); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2251]; `tensor/DDL_lfc|DDL_z.npy` [2251]; `embed/gene_vectors.npy` [2251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2251 or target_col == 2251). Every well: [[NDFIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDFIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
