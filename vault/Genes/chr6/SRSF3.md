---
symbol: "SRSF3"
type: "gene"
col: 3319
ensembl_id: "ENSG00000112081"
name: "serine and arginine rich splicing factor 3"
location: "6p21.31-p21.2"
module: 3
arm: "-"
pooled_cpm: 106.62
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SRSF3

*serine and arginine rich splicing factor 3* — 6p21.31-p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.13× (z +39.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.776× (z -4.8, q 7e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YWHAE]] (+0.78, fdr 7e-06), [[SFPQ]] (+0.73, fdr 7e-06), [[SRSF6]] (+0.69, fdr 7e-06); moves opposite to [[MIR4458HG]] (-0.71, fdr 7e-06), [[ATOX1]] (-0.70, fdr 7e-06), [[ATP5MK]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.13×** | +39.7 | 0e+00 | 48/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.25×** | +22.4 | 0e+00 | 47/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +17.4 | 0e+00 | 46/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.89×** | +14.1 | 9e-43 | 49/49 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.91×** | +12.8 | 3e-35 | 39/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +12.7 | 4e-35 | 42/45 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.71×** | +10.6 | 4e-24 | 42/49 (A498, SW480, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +9.3 | 7e-19 | 43/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.7 | 2e-16 | 33/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.50×** | +8.0 | 6e-14 | 43/48 (RPMI-7951, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +7.7 | 5e-13 | 31/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.49×** | +7.6 | 1e-12 | 26/44 (SW480, A498, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.48×** | +7.4 | 6e-12 | 36/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.37×** | +6.2 | 3e-08 | 29/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.6 | 7e-07 | 33/48 (KATO III, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 26/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.003 | 26/48 (Panc 03.27, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.003 | 9/49 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.006 | 19/48 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.11× | +3.0 | 0.065 | 6/48 (HT-29, J82, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.068 | 15/49 (SW480, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.15× | +2.8 | 0.094 | 12/48 (SHP-77, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -4.8 | 7e-04 | 24/48 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.798×** | -4.5 | 0.002 | 27/48 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.829×** | -3.7 | 0.036 | 22/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.710×** | -3.6 | 0.052 | 19/49 (LoVo, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.898× | -3.0 | 0.24 | 8/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.808× | -3.0 | 0.24 | 13/48 (HepG2/C3A, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 74.6 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +30.2) | — |
| [[AsPC-1 (line)]] | alt | 74.5 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +32.1) | — |
| [[SW480 (line)]] | alt | 116 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +19.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 99.0 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +21.4) | — |
| [[PANC-1 (line)]] | alt | 111 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +30.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 117 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.8) | — |
| [[NCI-H1573 (line)]] | alt | 76.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +26.4) | — |
| [[A498 (line)]] | wt | 75.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +27.2) | — |
| [[A549 (line)]] | wt | 96.1 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +18.9) | — |
| [[HEC-1-A (line)]] | alt | 108 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +22.0) | — |
| [[HOP62 (line)]] | alt | 114 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +28.9) | — |
| [[HT-29 (line)]] | alt | 108 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +24.1) | — |
| [[LoVo (line)]] | wt | 113 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +28.5) | — |
| [[SW48 (line)]] | wt | 91.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 96.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +25.5) | — |
| [[KATO III (line)]] | alt | 124 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +23.6) | — |
| [[LOX-IMVI (line)]] | wt | 125 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +24.8) | — |
| [[NCI-H1792 (line)]] | alt | 62.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +25.6) | — |
| [[NCI-H23 (line)]] | alt | 142 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +16.3) | — |
| [[Hs 766T (line)]] | wt | 66.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +20.7) | — |
| [[NCI-H2030 (line)]] | alt | 135 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +20.6) | — |
| [[Panc 03.27 (line)]] | alt | 173 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +24.6) | — |
| [[RPMI-7951 (line)]] | alt | 95.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +19.9) | — |
| [[SK-MEL-2 (line)]] | alt | 73.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +23.7) | — |
| [[SW1417 (line)]] | alt | 108 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +22.4) | — |
| [[A-172 (line)]] | wt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +20.3) | — |
| [[BT-474 (line)]] | alt | 107 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.5) | — |
| [[C32 (line)]] | wt | 99.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +24.2) | — |
| [[COLO 205 (line)]] | alt | 64.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +20.7) | — |
| [[HepG2_C3A (line)]] | wt | 101 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.9) | — |
| [[hTERT-HPNE (line)]] | wt | 94.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +26.8) | — |
| [[J82 (line)]] | alt | 115 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.1) | — |
| [[RKO (line)]] | wt | 122 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +17.1) | — |
| [[A-427 (line)]] | wt | 133 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.61× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 145 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +21.1) | — |
| [[H4 (line)]] | wt | 94.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +15.8) | — |
| [[NCI-H2347 (line)]] | alt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +18.6) | — |
| [[SNU-1 (line)]] | wt | 90.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 141 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +23.4) | — |
| [[SW 900 (line)]] | alt | 73.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +18.4) | — |
| [[AN3 CA (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HCT15 (line)]] | alt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 87.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[SW 1088 (line)]] | alt | 86.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAE]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[SFPQ]] | +0.73 | +0.67 / +0.79 | both halves | 7e-06 | same gene group; STRING 881 |
| [[SRSF6]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 991 |
| [[TMEM185B]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[HNRNPL]] | +0.67 | +0.57 / +0.70 | both halves | 8e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 952 |
| [[HNRNPM]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 956 |
| [[EWSR1]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 | same gene group; STRING 728 |
| [[CEP41]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PRRC2A]] | +0.63 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[PIGO]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DDX3X]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 588 |
| [[BCLAF1]] | +0.63 | +0.69 / +0.61 | both halves | 7e-06 | STRING 615 |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4458HG]] | -0.71 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[ATOX1]] | -0.70 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[ATP5MK]] | -0.69 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[UBL5]] | -0.66 | -0.59 / -0.59 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[COMMD6]] | -0.65 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.64 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[NEDD8]] | -0.64 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SLC37A3]] | -0.64 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[SSR4]] | -0.64 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[NENF]] | -0.64 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[KLHL7]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[RNF149]] | -0.63 | -0.59 / -0.57 | both halves | 8e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.7, -24.0); signed map (14.9, -38.6). **Vector** length 94.2, 28.8% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.54 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +39.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +7.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +6.7 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +17.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -5.9 | +6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -5.6 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.9 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | +1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31-p21.2 — chr6:36,594,353-36,605,600 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRp20; previously SFRS3 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P84103](https://www.uniprot.org/uniprotkb/P84103) (Serine/arginine-rich splicing factor 3):

> Splicing factor, which binds the consensus motif 5'-C[ACU][AU]C[ACU][AC]C-3' within pre-mRNA and promotes specific exons inclusion during alternative splicing. Interaction with YTHDC1, a RNA-binding protein that recognizes and binds N6-methyladenosine (m6A)-containing RNAs, promotes recruitment of SRSF3 to its mRNA-binding elements adjacent to m6A sites within exons. Also functions as an adapter involved in mRNA nuclear export. Binds mRNA which is thought to be transferred to the NXF1-NXT1 …

**Summary**, from NCBI Gene [6428](https://www.ncbi.nlm.nih.gov/gene/6428):

> The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an RNA recognition motif (RRM) for binding RNA and an RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different SR splicing factors. In addition to being critical for mRNA splicing, the SR proteins have also been shown to be …

**Accessions** — [HGNC:10785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10785) · Entrez [6428](https://www.ncbi.nlm.nih.gov/gene/6428) · UniProt [P84103](https://www.uniprot.org/uniprotkb/P84103) · Ensembl [ENSG00000112081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112081)

## Data

Gene col 3319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3319); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3319]; `tensor/DDL_lfc|DDL_z.npy` [3319]; `embed/gene_vectors.npy` [3319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3319 or target_col == 3319). Every well: [[SRSF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
