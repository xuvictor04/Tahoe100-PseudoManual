---
symbol: "STARD3NL"
type: "gene"
col: 203
ensembl_id: "ENSG00000010270"
name: "STARD3 N-terminal like"
location: "7p14.1"
module: 57
arm: "+"
pooled_cpm: 42.52
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# STARD3NL

*STARD3 N-terminal like* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.97× (z +8.4, q 2e-14, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.487× (z -24.2, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPSS1]] (+0.67, fdr 3e-05), [[NDRG3]] (+0.66, fdr 1e-05), [[TMEM9]] (+0.65, fdr 1e-05); moves opposite to [[ANKRD17-DT]] (-0.65, fdr 3e-05), [[ASH1L]] (-0.64, fdr 3e-05), [[PSMD6-AS2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +8.4 | 2e-14 | 31/47 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +6.4 | 4e-08 | 20/46 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +5.2 | 4e-05 | 16/46 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +5.0 | 6e-05 | 18/46 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.4 | 0.001 | 19/46 (C32, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.20×** | +4.4 | 0.001 | 18/42 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.0 | 0.005 | 17/46 (LoVo, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.18× | +3.9 | 0.007 | 12/46 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.029 | 14/41 (NCI-H2030, NCI-H460, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.487×** | -24.2 | 0e+00 | 45/46 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.559×** | -19.6 | 0e+00 | 39/46 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -12.1 | 1e-31 | 40/46 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -12.1 | 2e-31 | 32/46 (AN3 CA, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -11.0 | 7e-26 | 29/46 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -10.4 | 3e-23 | 36/46 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.710×** | -8.2 | 3e-14 | 33/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -8.1 | 4e-14 | 32/46 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -7.9 | 1e-13 | 34/46 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -7.6 | 2e-12 | 26/46 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.752×** | -6.5 | 3e-09 | 22/46 (SNU-423, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.769×** | -6.3 | 2e-08 | 23/46 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -6.1 | 4e-08 | 24/46 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.819×** | -4.7 | 8e-05 | 20/46 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.887× | -4.0 | 0.002 | 11/46 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.869× | -3.4 | 0.027 | 7/46 (hTERT-HPNE, RPMI-7951, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.869× | -3.2 | 0.038 | 11/46 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 43.1 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -16.9) |
| [[SW480 (line)]] | alt | 45.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -15.3) |
| [[A498 (line)]] | wt | 108 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -13.3) |
| [[AN3 CA (line)]] | alt | 58.4 | 0 | 3 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0652× (z -13.7) |
| [[H4 (line)]] | wt | 93.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0406× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.8) |
| [[HOP62 (line)]] | alt | 40.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -17.7) |
| [[HS-578T (line)]] | alt | 63.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.215× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 50.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 39.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 78.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.9) |
| [[A-172 (line)]] | wt | 59.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.6) |
| [[A-427 (line)]] | wt | 41.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.7) |
| [[COLO 205 (line)]] | alt | 24.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -9.5) |
| [[Hs 766T (line)]] | wt | 36.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -15.9) |
| [[LoVo (line)]] | wt | 23.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 33.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -26.4) |
| [[NCI-H2030 (line)]] | alt | 49.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.4) |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.8) |
| [[A549 (line)]] | wt | 50.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 55.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.1) |
| [[J82 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.2) |
| [[PANC-1 (line)]] | alt | 60.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -12.9) |
| [[RKO (line)]] | wt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 43.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.6) |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -8.5) |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.5) |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPSS1]] | +0.67 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[NDRG3]] | +0.66 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TMEM9]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.65 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[USP35]] | +0.63 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[VAMP7]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[THYN1]] | +0.62 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[RADX]] | +0.62 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[NTAN1]] | +0.62 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[GNPDA2]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[DLD]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | -0.65 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.64 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[PSMD6-AS2]] | -0.62 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.62 | -0.73 / -0.24 | both halves | 5e-04 |  |
| [[DNAI4]] | -0.61 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[CREBBP]] | -0.60 | -0.52 / -0.39 | both halves | 6e-05 | pathway: Metabolism of steroids |
| [[RBBP6]] | -0.60 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[BAZ1A]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.70 / -0.25 | both halves | 4e-04 |  |
| [[ZNF337-AS1]] | -0.58 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[CUX1]] | -0.58 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[WARS2-AS1]] | -0.58 | -0.63 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises STARD3NL's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00888]] | B | LINC00888 activity raises STARD3NL's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 2.42× lower at baseline in the lines without LINC00888 | 0.030 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |
| [[KATNAL1]] | B | KATNAL1 activity raises STARD3NL's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without KATNAL1 | 0.034 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[KIF3C]] | B | KIF3C activity raises STARD3NL's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 3.34× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.4, -6.4); signed map (-34.6, -14.0). **Vector** length 107, 25.5% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.2 | +6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.3 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -24.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -19.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.2 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | STARD3 N-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:38,178,245-38,230,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MENTHO, MGC3251 |
| Reactome | 4 pathways, smallest: Pregnenolone biosynthesis; Metabolism of steroid hormones; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [O95772](https://www.uniprot.org/uniprotkb/O95772) (STARD3 N-terminal-like protein):

> Tethering protein that creates contact site between the endoplasmic reticulum and late endosomes: localizes to late endosome membranes and contacts the endoplasmic reticulum via interaction with VAPA and VAPB.

**Summary**, from NCBI Gene [83930](https://www.ncbi.nlm.nih.gov/gene/83930):

> This gene encodes a late-endosomal protein that contains a conserved MENTAL (MLN64 N-terminal) domain. The encoded protein binds cholesterol molecules and may play a role in endosomal cholesterol transport through interactions with metastatic lymph node protein 64 (MLN64). [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:19169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19169) · Entrez [83930](https://www.ncbi.nlm.nih.gov/gene/83930) · UniProt [O95772](https://www.uniprot.org/uniprotkb/O95772) · Ensembl [ENSG00000010270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010270)

## Data

Gene col 203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 203); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 203]; `tensor/DDL_lfc|DDL_z.npy` [203]; `embed/gene_vectors.npy` [203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 203 or target_col == 203). Every well: [[STARD3NL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD3NL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
