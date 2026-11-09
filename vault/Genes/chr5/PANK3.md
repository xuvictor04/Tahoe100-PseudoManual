---
symbol: "PANK3"
type: "gene"
col: 4160
ensembl_id: "ENSG00000120137"
name: "pantothenate kinase 3"
location: "5q34"
module: 216
arm: "+"
pooled_cpm: 104.71
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# PANK3

*pantothenate kinase 3* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.79× (z +9.7, q 2e-19, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.443× (z -7.1, q 6e-10, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACSL4]] (+0.61, fdr 7e-06), [[SACS]] (+0.60, fdr 1e-05), [[EFR3A]] (+0.60, fdr 1e-05); moves opposite to [[ISY1]] (-0.62, fdr 7e-06), [[DCAF5]] (-0.59, fdr 1e-05), [[IGBP1]] (-0.55, fdr 1e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +9.7 | 2e-19 | 45/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +9.6 | 3e-19 | 42/48 (LoVo, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +8.7 | 8e-16 | 33/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.4 | 1e-11 | 34/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.0 | 3e-10 | 36/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +6.9 | 5e-10 | 35/48 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.31×** | +6.4 | 1e-08 | 33/48 (HS-578T, C-33 A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +6.3 | 2e-08 | 42/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +6.2 | 5e-08 | 33/48 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.8 | 5e-07 | 34/48 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +5.6 | 1e-06 | 31/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | **1.25×** | +5.3 | 5e-06 | 28/49 (HS-578T, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.7 | 1e-04 | 34/48 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 5e-04 | 29/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.3 | 6e-04 | 30/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.9 | 0.003 | 19/48 (A-172, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.003 | 26/47 (NCI-H460, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 32/48 (HOP62, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.443×** | -7.1 | 6e-10 | 42/49 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -6.4 | 5e-08 | 31/49 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.557×** | -5.1 | 6e-05 | 33/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -4.2 | 0.004 | 26/50 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.849× | -3.9 | 0.009 | 21/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.849× | -3.9 | 0.009 | 16/48 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.641×** | -3.5 | 0.033 | 26/48 (NCI-H23, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.034 | 25/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.041 | 23/48 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 103 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.0) | — |
| [[NCI-H23 (line)]] | alt | 97.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.06× (z +11.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 64.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 76.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.9) | — |
| [[LoVo (line)]] | wt | 134 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 118 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 142 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.8) | [[TAK-901 (drug)]] 5 µM 0.257× (z -8.7) |
| [[RKO (line)]] | wt | 151 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 133 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SNU-423 (line)]] | alt | 100 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.2) | — |
| [[A-427 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A549 (line)]] | wt | 85.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.146× (z -12.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -9.0) |
| [[Hs 766T (line)]] | wt | 66.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 88.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 99.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 116 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.94× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 85.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 89.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL4]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SACS]] | +0.60 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[EFR3A]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SC5D]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PTAR1]] | +0.56 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[OCRL]] | +0.56 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ELK4]] | +0.55 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[RFK]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 | pathway: Metabolism of vitamins and cofactors |
| [[HUS1]] | +0.53 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[DNAH14]] | +0.53 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[RBM12]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[NANP]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISY1]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[DCAF5]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[IGBP1]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[COG7]] | -0.54 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[CWC15]] | -0.54 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[APPBP2]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TOGARAM1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NUP54]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CWC25]] | -0.51 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[SMPD4BP]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[CIR1]] | -0.50 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ARID4B]] | -0.50 | -0.43 / -0.57 | both halves | 4e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.2, -12.6); signed map (-11.5, -39.4). **Vector** length 128, 42.1% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.5 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +6.0 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +6.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +5.3 | +6.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.0 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +3.2 | +3.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.9 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -10.0 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | pantothenate kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:168,548,495-168,579,368 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12899 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Pantothenate kinase family |
| Reactome | 4 pathways, smallest: Coenzyme A biosynthesis; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H999](https://www.uniprot.org/uniprotkb/Q9H999) (Pantothenate kinase 3):

> Catalyzes the phosphorylation of pantothenate to generate 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) synthesis.

**Summary**, from NCBI Gene [79646](https://www.ncbi.nlm.nih.gov/gene/79646):

> This gene encodes a protein belonging to the pantothenate kinase family. Pantothenate kinase is a key regulatory enzyme in the biosynthesis of coenzyme A (CoA) in bacteria and mammalian cells. It catalyzes the first committed step in the universal biosynthetic pathway leading to CoA and is itself subject to regulation through feedback inhibition by CoA. This family member is expressed most abundantly in the liver. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19365) · Entrez [79646](https://www.ncbi.nlm.nih.gov/gene/79646) · UniProt [Q9H999](https://www.uniprot.org/uniprotkb/Q9H999) · Ensembl [ENSG00000120137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120137)

## Data

Gene col 4160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4160); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4160]; `tensor/DDL_lfc|DDL_z.npy` [4160]; `embed/gene_vectors.npy` [4160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4160 or target_col == 4160). Every well: [[PANK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PANK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
