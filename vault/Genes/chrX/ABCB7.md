---
symbol: "ABCB7"
type: "gene"
col: 5191
ensembl_id: "ENSG00000131269"
name: "ATP binding cassette subfamily B member 7"
location: "Xq13.3"
module: 51
arm: "+"
pooled_cpm: 61.73
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ABCB7

*ATP binding cassette subfamily B member 7* — Xq13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.62× (z +16.3, q 0e+00, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.709× (z -16.2, q 0e+00, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHIC1]] (+0.68, fdr 1e-05), [[NDUFS4]] (+0.68, fdr 1e-05), [[SCAF8]] (+0.64, fdr 1e-05); moves opposite to [[GOLGA3]] (-0.60, fdr 1e-05), [[DPP9]] (-0.59, fdr 3e-05), [[TPD52L2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC25A24P1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +16.3 | 0e+00 | 38/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +12.8 | 4e-35 | 26/47 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +12.8 | 4e-35 | 40/48 (SW480, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +10.0 | 2e-21 | 27/47 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +9.8 | 1e-20 | 30/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +9.7 | 3e-20 | 30/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +8.6 | 5e-16 | 22/47 (HT-29, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +7.1 | 1e-10 | 21/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +6.6 | 2e-09 | 22/47 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[NG25 (drug)]] 5 µM |  | **1.45×** | +6.5 | 4e-09 | 24/46 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.20×** | +6.2 | 4e-08 | 16/47 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +6.0 | 9e-08 | 23/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.1 | 2e-05 | 19/47 (BT-474, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.9 | 0.003 | 10/47 (BT-474, HOP62, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.004 | 10/45 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.11× | +3.6 | 0.013 | 4/47 (NCI-H2347, LS 180, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.11× | +3.5 | 0.017 | 8/47 (HepG2/C3A, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -16.2 | 0e+00 | 34/47 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -9.3 | 4e-18 | 26/47 (BT-474, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.776×** | -8.1 | 8e-14 | 24/42 (NCI-H1573, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -7.7 | 2e-12 | 1/49 (NCI-H2122) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.810×** | -7.0 | 3e-10 | 23/47 (SW480, SHP-77, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.841× | -5.8 | 8e-07 | 19/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -5.6 | 2e-06 | 22/46 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.849× | -5.4 | 4e-06 | 14/46 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.856× | -5.0 | 5e-05 | 20/49 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -4.8 | 1e-04 | 17/46 (HOP62, H4, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.764×** | -4.7 | 1e-04 | 13/47 (SNU-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.867× | -4.6 | 2e-04 | 14/47 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.876× | -4.4 | 5e-04 | 16/47 (SW480, SHP-77, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.888× | -3.9 | 0.003 | 16/46 (NCI-H2030, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.894× | -3.7 | 0.008 | 9/46 (PANC-1, MIA PaCa-2, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.031 | 11/47 (A-172, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.905× | -3.2 | 0.045 | 7/46 (MIA PaCa-2, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 133 | 4 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +16.3) | [[Panobinostat (drug)]] 0.5 µM 0.576× (z -12.1) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.657× (z -9.2) |
| [[BT-474 (line)]] | alt | 43.1 | 4 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +10.9) | [[Auranofin (drug)]] 5 µM 0.325× (z -10.2) |
| [[LoVo (line)]] | wt | 45.9 | 3 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.17× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -9.1) |
| [[PANC-1 (line)]] | alt | 76.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.6) | [[Bortezomib (drug)]] 5 µM 0.326× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~10% of this change |
| [[NCI-H1573 (line)]] | alt | 59.4 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -24.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 78.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.5) | — |
| [[A-427 (line)]] | wt | 59.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.3) | — |
| [[KATO III (line)]] | alt | 75.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 74.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -12.0) |
| [[RKO (line)]] | wt | 98.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 96.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SHP-77 (line)]] | alt | 88.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 73.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.8) |
| [[AN3 CA (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[CFPAC-1 (line)]] | alt | 65.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.44× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[HepG2_C3A (line)]] | wt | 39.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.186× (z -11.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 53.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 54.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.13× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 67.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -8.9) |
| [[SNU-423 (line)]] | alt | 91.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.6) |
| [[SW1417 (line)]] | alt | 67.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -10.5) |
| [[A498 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHIC1]] | +0.68 | +0.53 / +0.71 | both halves | 1e-05 | STRING 472 |
| [[NDUFS4]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SCAF8]] | +0.64 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[THUMPD2]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[EPC1]] | +0.64 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LINC01278]] | +0.62 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[ACBD6]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.61 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NFYC]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PGGT1B]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[BRAF]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CUL5]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA3]] | -0.60 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[DPP9]] | -0.59 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[TPD52L2]] | -0.56 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.53 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[SMG1P6]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[NPIPB11]] | -0.52 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[PLCB3]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CDR2L]] | -0.50 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[FBH1]] | -0.50 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ACLY]] | -0.50 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[EHBP1L1]] | -0.50 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[TMEM104]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises ABCB7's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 1.42× lower at baseline in the lines without SLC25A24P1 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[HMGN5]] | B | HMGN5 activity raises ABCB7's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without HMGN5 | 0.095 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.1, -2.2); signed map (-19.3, -21.8). **Vector** length 103, 23.4% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.0 | +8.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +12.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.4 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -16.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.3 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | -2.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.6 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily B member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.3 — chrX:75,051,048-75,156,732 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST140535, Atm1p, ASAT; previously ABC7 |
| Gene groups (HGNC) | ATP binding cassette subfamily B |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Mitochondrial ABC transporters; Cytosolic iron-sulfur cluster assembly; ABC-family protein mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75027](https://www.uniprot.org/uniprotkb/O75027) (Iron-sulfur clusters transporter ABCB7, mitochondrial):

> Exports glutathione-coordinated iron-sulfur clusters such as [2Fe-2S]-(GS)4 cluster from the mitochondria to the cytosol in an ATP-dependent manner allowing the assembly of the cytosolic iron-sulfur (Fe/S) cluster-containing proteins and participates in iron homeostasis. Moreover, through a functional complex formed of ABCB7, FECH and ABCB10, also plays a role in the cellular iron homeostasis, mitochondrial function and heme biosynthesis. In cardiomyocytes, regulates cellular iron homeostasis …

**Summary**, from NCBI Gene [22](https://www.ncbi.nlm.nih.gov/gene/22):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily are involved in multidrug resistance as well as antigen presentation. This gene encodes a …

**Accessions** — [HGNC:48](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48) · Entrez [22](https://www.ncbi.nlm.nih.gov/gene/22) · UniProt [O75027](https://www.uniprot.org/uniprotkb/O75027) · Ensembl [ENSG00000131269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131269)

## Data

Gene col 5191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5191); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5191]; `tensor/DDL_lfc|DDL_z.npy` [5191]; `embed/gene_vectors.npy` [5191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5191 or target_col == 5191). Every well: [[ABCB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
