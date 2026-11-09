---
symbol: "VPS26A"
type: "gene"
col: 4388
ensembl_id: "ENSG00000122958"
name: "VPS26 retromer complex component A"
location: "10q22.1"
module: 122
arm: "+"
pooled_cpm: 111.11
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# VPS26A

*VPS26 retromer complex component A* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +20.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.852× (z -4.9, q 5e-04, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.390×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC13]] (+0.63, fdr 1e-05), [[BROX]] (+0.61, fdr 9e-06), [[UBQLN1]] (+0.60, fdr 1e-05); moves opposite to [[LSM7]] (-0.56, fdr 1e-05), [[PILRB]] (-0.55, fdr 1e-05), [[PPRC1]] (-0.53, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MATR3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +20.8 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +12.3 | 5e-32 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +11.4 | 5e-28 | 36/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +11.3 | 1e-27 | 45/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.69×** | +11.3 | 2e-27 | 40/49 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +10.7 | 1e-24 | 41/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.0 | 1e-21 | 34/49 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +9.1 | 4e-18 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +9.0 | 2e-17 | 38/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.3 | 4e-15 | 39/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +8.3 | 5e-15 | 36/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.2 | 1e-14 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +7.9 | 1e-13 | 40/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +7.8 | 2e-13 | 37/48 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +7.4 | 5e-12 | 33/48 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +7.0 | 8e-11 | 30/48 (A-172, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +6.6 | 2e-09 | 32/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.9 | 1e-07 | 32/48 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 6e-07 | 26/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4388.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.390×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -4.9 | 5e-04 | 16/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.822×** | -4.1 | 0.012 | 23/49 (AsPC-1, SW1417, …) | top dose only | plate-row cell shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.855× | -3.4 | 0.12 | 10/48 (NCI-H2030, A498, …) | top dose only |  |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 0.860× | -3.2 | 0.18 | 10/49 (BT-474, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.815× | -3.2 | 0.18 | 18/48 (HCT15, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.0 | 0.23 | 15/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 130 | 15 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +24.2) | — |
| [[NCI-H460 (line)]] | wt | 101 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +25.5) | — |
| [[NCI-H1573 (line)]] | alt | 115 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -11.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.9 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.8) | — |
| [[KATO III (line)]] | alt | 83.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 73.7 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.7) | — |
| [[A-172 (line)]] | wt | 132 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.9) | — |
| [[A498 (line)]] | wt | 128 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.9) | — |
| [[A549 (line)]] | wt | 92.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 146 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +15.5) | — |
| [[COLO 205 (line)]] | alt | 83.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +18.3) | — |
| [[NCI-H2030 (line)]] | alt | 102 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 106 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.4) | — |
| [[A-427 (line)]] | wt | 113 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.27× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 134 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.3) | — |
| [[HT-29 (line)]] | alt | 107 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.7) | — |
| [[J82 (line)]] | alt | 79.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.8) | — |
| [[LoVo (line)]] | wt | 77.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 137 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.1) | — |
| [[SW480 (line)]] | alt | 133 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.99× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 94.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 82.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +15.5) | — |
| [[SNU-423 (line)]] | alt | 182 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.1) | — |
| [[SW48 (line)]] | wt | 130 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 77.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.2) | — |
| [[H4 (line)]] | wt | 69.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 98.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 206 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 88.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 156 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.2) | — |
| [[RKO (line)]] | wt | 96.6 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 95.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 104 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.29× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 229 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC13]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 | STRING 676 |
| [[BROX]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[UBQLN1]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[VPS35]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Signaling by WNT; STRING 999 |
| [[WASHC2C]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 | STRING 713 |
| [[NCKAP1]] | +0.58 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[FRG1BP]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 | STRING 588 |
| [[STAG2]] | +0.57 | +0.40 / +0.71 | both halves | 5e-05 |  |
| [[BLTP1]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ATP6V1H]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM7]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PILRB]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[PPRC1]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[DDX19A]] | -0.52 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[DMPK]] | -0.52 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[FBXL18]] | -0.52 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ISG20L2]] | -0.50 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[SEC16A]] | -0.49 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[KCNJ14]] | -0.49 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ZNF544]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[P3H4]] | -0.48 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[TASOR2]] | -0.47 | -0.33 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MATR3]] | C | MATR3's natural level weakens VPS26A's drug response | MATR3's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.31; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-23.8, -16.3); signed map (-17.5, -34.7). **Vector** length 93.7, 29.6% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.8 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.9 | +7.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.2 | +0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | +8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.4 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | VPS26 retromer complex component A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,123,512-69,174,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hbeta58, PEP8A; previously VPS26 |
| Reactome | 2 pathways, smallest: WNT ligand biogenesis and trafficking; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [O75436](https://www.uniprot.org/uniprotkb/O75436) (Vacuolar protein sorting-associated protein 26A):

> Acts as a component of the retromer cargo-selective complex (CSC). The CSC is believed to be the core functional component of retromer or respective retromer complex variants acting to prevent missorting of selected transmembrane cargo proteins into the lysosomal degradation pathway. The recruitment of the CSC to the endosomal membrane involves RAB7A and SNX3. The SNX-BAR retromer mediates retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN) and is involved in …

**Summary**, from NCBI Gene [9559](https://www.ncbi.nlm.nih.gov/gene/9559):

> This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studies in yeast and mammalian cells indicate that this protein interacts directly with VPS35, which …

**Accessions** — [HGNC:12711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12711) · Entrez [9559](https://www.ncbi.nlm.nih.gov/gene/9559) · UniProt [O75436](https://www.uniprot.org/uniprotkb/O75436) · Ensembl [ENSG00000122958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122958)

## Data

Gene col 4388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4388); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4388]; `tensor/DDL_lfc|DDL_z.npy` [4388]; `embed/gene_vectors.npy` [4388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4388 or target_col == 4388). Every well: [[VPS26A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS26A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
