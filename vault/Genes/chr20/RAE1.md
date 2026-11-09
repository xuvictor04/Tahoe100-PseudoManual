---
symbol: "RAE1"
type: "gene"
col: 2078
ensembl_id: "ENSG00000101146"
name: "ribonucleic acid export 1"
location: "20q13.31"
module: 7
arm: "+"
pooled_cpm: 41.67
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RAE1

*ribonucleic acid export 1* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +22.2, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.660× (z -8.3, q 8e-14, down in 32 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 0.207×, NCI-H23 0.201×, NCI-H2030 0.332×, SHP-77 0.334×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.184×, C-33 A 0.277×, SHP-77 0.358×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.218×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAF1]] (+0.67, fdr 1e-05), [[THBS4]] (+0.67, fdr 2e-05), [[ZNF304]] (+0.66, fdr 1e-05); moves opposite to [[DOP1B]] (-0.57, fdr 4e-05), [[PPP1R13B]] (-0.56, fdr 1e-05), [[HABP4]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +22.2 | 0e+00 | 47/47 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.73×** | +19.8 | 0e+00 | 47/47 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.97×** | +16.6 | 0e+00 | 47/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **4.85×** | +16.3 | 0e+00 | 48/49 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +15.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +12.3 | 1e-32 | 41/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +10.8 | 4e-25 | 45/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +10.1 | 2e-22 | 42/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +10.0 | 7e-22 | 36/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +10.0 | 7e-22 | 35/48 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +9.6 | 4e-20 | 30/48 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +9.0 | 1e-17 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +8.1 | 3e-14 | 36/48 (Hs 766T, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +7.8 | 2e-13 | 35/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +7.6 | 1e-12 | 22/35 (NCI-H2030, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +6.6 | 2e-09 | 33/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 1e-07 | 26/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2078.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 0.207×, NCI-H23 0.201×, NCI-H2030 0.332×, SHP-77 0.334×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.184×, C-33 A 0.277×, SHP-77 0.358×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-1 0.218×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.660×** | -8.3 | 8e-14 | 32/47 (HEC-1-A, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -7.5 | 3e-11 | 24/41 (NCI-H460, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.847× | -3.3 | 0.17 | 8/48 (SW1417, NCI-H1792, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.861× | -3.0 | 0.38 | 10/48 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 55.9 | 13 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +18.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +16.7) | — |
| [[PANC-1 (line)]] | alt | 28.2 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.3) | — |
| [[NCI-H23 (line)]] | alt | 62.6 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -17.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 194 | 8 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 29.9 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -17.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.0) | — |
| [[LoVo (line)]] | wt | 25.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 34.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +20.4) | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 32.4 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.97× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 72.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 51.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.3) | — |
| [[A498 (line)]] | wt | 33.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +21.3) | — |
| [[HOP62 (line)]] | alt | 34.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 32.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 71.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 79.1 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.00× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +14.1) | — |
| [[A-172 (line)]] | wt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.5) | — |
| [[A-427 (line)]] | wt | 43.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.8) | — |
| [[A549 (line)]] | wt | 30.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +17.6) | — |
| [[C32 (line)]] | wt | 31.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +20.9) | — |
| [[HS-578T (line)]] | alt | 28.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +17.0) | — |
| [[HT-29 (line)]] | alt | 34.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 41.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 36.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 35.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.46× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.8) | — |
| [[J82 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAF1]] | +0.67 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[THBS4]] | +0.67 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ZNF304]] | +0.66 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PSMC2]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 | pathway: Disorders of transmembrane transporters |
| [[TMEM199]] | +0.66 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GTF3C4]] | +0.65 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ALKBH3]] | +0.65 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[SMG8]] | +0.65 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[MRPS22]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[OTUB1]] | +0.62 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[WDR73]] | +0.62 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[NAXD]] | +0.62 | +0.38 / +0.60 | both halves | 6e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1B]] | -0.57 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PPP1R13B]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[HABP4]] | -0.54 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[PI4KA]] | -0.53 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MAPK8]] | -0.53 | -0.40 / -0.32 | both halves | 1e-04 |  |
| [[ARPC1B]] | -0.53 | -0.45 / -0.43 | both halves | 3e-05 | same gene group |
| [[UNC13B]] | -0.53 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[BAIAP2L1]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SPAG9]] | -0.52 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.8, 12.3); signed map (-8.9, -23.6). **Vector** length 64.0, 13.6% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.0 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.2 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +16.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.4 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ribonucleic acid export 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:57,351,223-57,379,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mnrp41, Gle2 |
| Gene groups (HGNC) | WD repeat domain containing; Nucleoporins |
| Hallmark sets | DNA_REPAIR |
| Reactome | 69 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P78406](https://www.uniprot.org/uniprotkb/P78406) (mRNA export factor RAE1):

> Acts as a mRNA export factor involved in nucleocytoplasmic transport. Plays a role in mitotic bipolar spindle formation. May function in attaching cytoplasmic mRNPs to the cytoskeleton both directly or indirectly.

**Summary**, from NCBI Gene [8480](https://www.ncbi.nlm.nih.gov/gene/8480):

> Mutations in the Schizosaccharomyces pombe Rae1 and Saccharomyces cerevisiae Gle2 genes have been shown to result in accumulation of poly(A)-containing mRNA in the nucleus, suggesting that the encoded proteins are involved in RNA export. The protein encoded by this gene is a homolog of yeast Rae1. It contains four WD40 motifs, and has been shown to localize to distinct foci in the nucleoplasm, to the nuclear rim, and to meshwork-like structures throughout the cytoplasm. This gene is thought to …

**Accessions** — [HGNC:9828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9828) · Entrez [8480](https://www.ncbi.nlm.nih.gov/gene/8480) · UniProt [P78406](https://www.uniprot.org/uniprotkb/P78406) · Ensembl [ENSG00000101146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101146)

## Data

Gene col 2078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2078); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2078]; `tensor/DDL_lfc|DDL_z.npy` [2078]; `embed/gene_vectors.npy` [2078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2078 or target_col == 2078). Every well: [[RAE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
