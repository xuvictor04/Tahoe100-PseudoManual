---
symbol: "ARL5B"
type: "gene"
col: 9221
ensembl_id: "ENSG00000165997"
name: "ARF like GTPase 5B"
location: "10p12.31"
module: 172
arm: "+"
pooled_cpm: 141.3
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# ARL5B

*ARF like GTPase 5B* — 10p12.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.85× (z +16.8, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.713× (z -4.4, q 0.006, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R15B]] (+0.67, fdr 7e-06), [[ATP7A]] (+0.65, fdr 7e-06), [[JUNB]] (+0.63, fdr 7e-06); moves opposite to [[SELENOO]] (-0.62, fdr 1e-05), [[NCOA6]] (-0.61, fdr 1e-05), [[RILPL1]] (-0.59, fdr 1e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +16.8 | 0e+00 | 40/48 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.29×** | +9.4 | 2e-18 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.9 | 7e-17 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.14×** | +8.4 | 5e-15 | 47/49 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +7.5 | 7e-12 | 31/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.91×** | +7.3 | 2e-11 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +7.3 | 2e-11 | 39/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +6.4 | 1e-08 | 30/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +6.0 | 1e-07 | 35/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.7 | 1e-04 | 29/47 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 26/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.8 | 0.007 | 24/38 (HEC-1-A, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +3.7 | 0.008 | 29/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +3.7 | 0.009 | 28/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.060 | 29/48 (LoVo, LS 180, …) | two highest doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.713×** | -4.4 | 0.006 | 35/48 (SW48, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.708×** | -3.9 | 0.022 | 36/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.022 | 33/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.714×** | -3.7 | 0.027 | 30/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.639×** | -3.6 | 0.027 | 33/48 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.728×** | -3.6 | 0.027 | 31/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.646×** | -3.5 | 0.032 | 30/48 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.047 | 29/48 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.062 | 24/48 (Panc 03.27, NCI-H1573, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.754×** | -3.2 | 0.071 | 23/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.756×** | -3.2 | 0.071 | 24/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.759×** | -3.2 | 0.076 | 30/47 (A-427, NCI-H23, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.076 | 24/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.762×** | -3.1 | 0.076 | 28/48 (A549, H4, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **0.763×** | -3.1 | 0.076 | 28/48 (RKO, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 107 | 15 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +26.2) | — |
| [[PANC-1 (line)]] | alt | 82.3 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +23.2) | — |
| [[A-172 (line)]] | wt | 132 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +28.1) | — |
| [[HS-578T (line)]] | alt | 63.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 158 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +19.2) | — |
| [[BT-474 (line)]] | alt | 133 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 92.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 81.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.29× (z +19.3) | — |
| [[NCI-H1573 (line)]] | alt | 215 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.6) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.305× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 180 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +17.7) | — |
| [[NCI-H2347 (line)]] | alt | 177 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +18.0) | — |
| [[SNU-1 (line)]] | wt | 97.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.90× (z +12.5) | — |
| [[A498 (line)]] | wt | 117 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +25.9) | — |
| [[A549 (line)]] | wt | 212 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +17.4) | — |
| [[HEC-1-A (line)]] | alt | 94.4 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.34× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 303 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +12.3) | — |
| [[J82 (line)]] | alt | 112 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +22.3) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +28.8) | — |
| [[SW 900 (line)]] | alt | 157 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +22.3) | — |
| [[SW480 (line)]] | alt | 120 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.6) | — |
| [[A-427 (line)]] | wt | 178 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.49× (z +8.8) ⚠ toxic | [[Ponatinib (drug)]] 5 µM 0.391× (z -9.4) |
| [[Hs 766T (line)]] | wt | 112 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +22.1) | — |
| [[LOX-IMVI (line)]] | wt | 94.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 160 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +20.5) | — |
| [[RPMI-7951 (line)]] | alt | 186 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +18.1) | — |
| [[SNU-423 (line)]] | alt | 140 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +29.0) | — |
| [[C32 (line)]] | wt | 61.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 238 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +16.7) | — |
| [[H4 (line)]] | wt | 73.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 277 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 165 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.6) | — |
| [[RKO (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 154 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 125 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 146 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 225 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R15B]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ATP7A]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[JUNB]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SLC12A2]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[EDEM1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FOS]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[EPB41L2]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CD83]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[KBTBD2]] | +0.55 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CD164]] | +0.54 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[NAB1]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[EXTL2]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOO]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[NCOA6]] | -0.61 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RILPL1]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ARL8A]] | -0.59 | -0.46 / -0.58 | both halves | 2e-05 | same gene group |
| [[C19orf12]] | -0.57 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MRPS5]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[MRPL32]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[TM2D2]] | -0.54 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[ECSIT]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[PARGP1]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction -0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.9, 13.9); signed map (7.4, 27.6). **Vector** length 124, 47.6% of its response variance represented; |z| ≥ 3 in 1,441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +9.0 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.8 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.6 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.8 | +1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -10.0 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -9.3 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.3 | -1.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.6 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.0 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.3 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.31 — chr10:18,659,431-18,681,639 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARL8 |
| Gene groups (HGNC) | ARF GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KC2](https://www.uniprot.org/uniprotkb/Q96KC2) (ADP-ribosylation factor-like protein 5B):

> Binds and exchanges GTP and GDP.

**Summary**, from NCBI Gene [221079](https://www.ncbi.nlm.nih.gov/gene/221079):

> ARL5B (ARL8) belongs to a family of proteins that are structurally similar to ADP-ribosylation factors (ARFs; see MIM 103180). ARLs and ARFs are part of the RAS superfamily of regulatory GTPases.[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:23052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23052) · Entrez [221079](https://www.ncbi.nlm.nih.gov/gene/221079) · UniProt [Q96KC2](https://www.uniprot.org/uniprotkb/Q96KC2) · Ensembl [ENSG00000165997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165997)

## Data

Gene col 9221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9221); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9221]; `tensor/DDL_lfc|DDL_z.npy` [9221]; `embed/gene_vectors.npy` [9221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9221 or target_col == 9221). Every well: [[ARL5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
