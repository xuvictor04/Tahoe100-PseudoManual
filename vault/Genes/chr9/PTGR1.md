---
symbol: "PTGR1"
type: "gene"
col: 2812
ensembl_id: "ENSG00000106853"
name: "prostaglandin reductase 1"
location: "9q31.3"
module: 117
arm: "+"
pooled_cpm: 81.86
n_lines_expressing: 42
n_dd_up: 23
n_dd_down: 14
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# PTGR1

*prostaglandin reductase 1* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +10.6, q 1e-23, up in 34 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.612× (z -12.3, q 6e-32, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1C1]] (+0.62, fdr 7e-06), [[YWHAG]] (+0.60, fdr 1e-05), [[TXNRD1]] (+0.57, fdr 1e-05); moves opposite to [[ARHGAP1]] (-0.48, fdr 2e-05), [[FAM110A]] (-0.46, fdr 3e-05), [[ICAM3]] (-0.44, fdr 4e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02057]] → it (grade B ⚠); 5 go from it, the strongest it → [[SYTL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +10.6 | 1e-23 | 34/40 (NCI-H1792, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +8.9 | 2e-16 | 24/40 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +8.8 | 2e-16 | 26/40 (LS 180, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +8.7 | 4e-16 | 31/41 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +7.4 | 1e-11 | 24/39 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.2 | 5e-11 | 20/32 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +7.2 | 7e-11 | 27/40 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.29×** | +6.5 | 6e-09 | 28/40 (Hs 766T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 1e-05 | 20/40 (LS 180, KATO III, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 2e-05 | 18/40 (HOP62, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 1e-04 | 20/41 (HOP62, SW 900, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 19/40 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +4.7 | 1e-04 | 18/41 (HOP62, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 2e-04 | 20/40 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 2e-04 | 18/40 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 19/40 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 7e-04 | 20/39 (HOP62, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2812.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.612×** | -12.3 | 6e-32 | 26/40 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -9.5 | 9e-19 | 26/40 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -7.9 | 6e-13 | 23/40 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.732×** | -5.3 | 2e-05 | 21/40 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.750×** | -5.1 | 4e-05 | 23/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -4.9 | 9e-05 | 20/39 (C-33 A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.788×** | -4.2 | 0.002 | 18/40 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 0.003 | 17/40 (C-33 A, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.859× | -3.8 | 0.009 | 15/41 (COLO 205, BT-474, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.812×** | -3.5 | 0.029 | 10/40 (A498, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.816×** | -3.4 | 0.032 | 14/39 (LOX-IMVI, A549, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.032 | 15/40 (BT-474, COLO 205, …) | two highest doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.032 | 12/40 (C-33 A, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.696×** | -3.4 | 0.032 | 10/41 (J82, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.834× | -3.2 | 0.051 | 13/40 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.719×** | -3.1 | 0.080 | 13/41 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | 0.841× | -2.9 | 0.100 | 9/40 (CFPAC-1, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 62.7 | 13 (3 ⚠) | 0 | [[Cobimetinib (drug)]] 5 µM 4.54× (z +15.9) | — |
| [[COLO 205 (line)]] | alt | 266 | 1 | 7 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.93× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -26.4) |
| [[KATO III (line)]] | alt | 45.4 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.94× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 387 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -21.8) |
| [[LS 180 (line)]] | wt | 65.5 | 5 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.67× (z +20.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.393× (z -9.8) |
| [[BT-474 (line)]] | alt | 60.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.1) |
| [[HT-29 (line)]] | alt | 92.8 | 2 | 2 (1 ⚠) | [[Auranofin (drug)]] 0.5 µM 2.47× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.0) |
| [[A498 (line)]] | wt | 216 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.34× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.6) |
| [[A549 (line)]] | wt | 165 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.33× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 96.0 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.06× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 53.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -10.4) |
| [[SW 900 (line)]] | alt | 146 | 1 | 2 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.12× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 40.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.77× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.5) |
| [[C-33 A (line)]] | alt | 84.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -13.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.345× (z -8.7) |
| [[C32 (line)]] | wt | 39.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.2) |
| [[J82 (line)]] | alt | 124 | 2 (1 ⚠) | 0 | [[Cobimetinib (drug)]] 5 µM 2.13× (z +9.4) | — |
| [[RKO (line)]] | wt | 72.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 74.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.8) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 72.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 84.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 33.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 48.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 58.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.3) |
| [[SNU-423 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.0) |
| [[A-172 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1C1]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | STRING 587 |
| [[YWHAG]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[TXNRD1]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 | STRING 412 |
| [[AKR1C3]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 498 |
| [[NMRAL2P]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PSMA4]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.53 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[CAPS2]] | +0.53 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MGST1]] | +0.53 | +0.58 / +0.53 | both halves | 1e-05 | STRING 423 |
| [[EID3]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[GSR]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[ANXA1]] | +0.53 | +0.36 / +0.56 | both halves | 9e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP1]] | -0.48 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[FAM110A]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ICAM3]] | -0.44 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[TSPAN4]] | -0.44 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[SFXN2]] | -0.43 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[MIPEP]] | -0.42 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[ODF2]] | -0.41 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02057]] | B | LINC02057 activity raises PTGR1's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 2.31× lower at baseline in the lines without LINC02057 | 0.042 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[EFEMP1]] | B | EFEMP1 activity raises PTGR1's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 2.38× lower at baseline in the lines without EFEMP1 | 0.045 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[EYA4]] | B | EYA4 activity raises PTGR1's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without EYA4 | 0.063 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA |
| [[PALLD]] | B | PALLD activity raises PTGR1's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without PALLD | 0.070 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PTGR1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL2]] | B | PTGR1 activity raises SYTL2's level | lines that do not express PTGR1 (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without PTGR1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |
| [[RNASEL]] | B | PTGR1 activity raises RNASEL's level | lines that do not express PTGR1 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without PTGR1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | B | PTGR1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express PTGR1 (8) vs lines expressing it (40) | the lines without PTGR1: 0.80× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | B | PTGR1 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PTGR1 (8) vs lines expressing it (40) | the lines without PTGR1: 1.42× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | B | PTGR1 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express PTGR1 (8) vs lines expressing it (40) | the lines without PTGR1: 0.76× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.3, 46.7); signed map (51.9, -9.7). **Vector** length 113, 30.4% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.50 to 8); *Synthesis of bile acids and bile salts via 27-hydroxycholesterol* (reactome, mean cos +0.54 to 3); *Synthesis of bile acids and bile salts via 24-hydroxycholesterol* (reactome, mean cos +0.54 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +6.1 | +2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +8.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +7.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +4.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -12.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -4.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:111,549,722-111,599,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZADH3; previously LTB4DH |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 6 pathways, smallest: Biosynthesis of Lipoxins (LX); Synthesis of Leukotrienes (LT) and Eoxins (EX); Biosynthesis of specialized proresolving mediators (SPMs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14914](https://www.uniprot.org/uniprotkb/Q14914) (Prostaglandin reductase 1):

> NAD(P)H-dependent oxidoreductase involved in metabolic inactivation of pro- and anti-inflammatory eicosanoids: prostaglandins (PG), leukotrienes (LT) and lipoxins (LX). Catalyzes with high efficiency the reduction of the 13,14 double bond of 15-oxoPGs, including 15-oxo-PGE1, 15-oxo-PGE2, 15-oxo-PGF1-alpha and 15-oxo-PGF2-alpha. Catalyzes with lower efficiency the oxidation of the hydroxyl group at C12 of LTB4 and its derivatives, converting them into biologically less active 12-oxo-LTB4 …

**Summary**, from NCBI Gene [22949](https://www.ncbi.nlm.nih.gov/gene/22949):

> This gene encodes an enzyme that is involved in the inactivation of the chemotactic factor, leukotriene B4. The encoded protein specifically catalyzes the NADP+ dependent conversion of leukotriene B4 to 12-oxo-leukotriene B4. A pseudogene of this gene is found on chromosome 1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:18429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18429) · Entrez [22949](https://www.ncbi.nlm.nih.gov/gene/22949) · UniProt [Q14914](https://www.uniprot.org/uniprotkb/Q14914) · Ensembl [ENSG00000106853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106853)

## Data

Gene col 2812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2812); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2812]; `tensor/DDL_lfc|DDL_z.npy` [2812]; `embed/gene_vectors.npy` [2812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2812 or target_col == 2812). Every well: [[PTGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
