---
symbol: "PIP5K1A"
type: "gene"
col: 6736
ensembl_id: "ENSG00000143398"
name: "phosphatidylinositol-4-phosphate 5-kinase type 1 alpha"
location: "1q21.3"
module: 46
arm: "+"
pooled_cpm: 143.26
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PIP5K1A

*phosphatidylinositol-4-phosphate 5-kinase type 1 alpha* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.94× (z +25.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.676× (z -8.8, q 8e-16, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.784× (z -5.7, q 2e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN2]] (+0.61, fdr 1e-05), [[AKAP8L]] (+0.60, fdr 1e-05), [[STRN3]] (+0.60, fdr 5e-05); moves opposite to [[MLX]] (-0.54, fdr 1e-04), [[DTD1]] (-0.49, fdr 1e-04), [[AGO1]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.94×** | +25.0 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +21.9 | 0e+00 | 44/48 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +21.9 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.21×** | +18.4 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.50×** | +18.3 | 0e+00 | 46/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +15.5 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +15.4 | 0e+00 | 45/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.16×** | +13.9 | 2e-42 | 44/48 (SW480, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +11.4 | 4e-28 | 34/49 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +10.5 | 5e-24 | 37/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +7.3 | 2e-11 | 33/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.2 | 2e-08 | 33/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +5.9 | 2e-07 | 28/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.7 | 6e-07 | 29/48 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +5.7 | 6e-07 | 28/48 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +5.5 | 1e-06 | 31/48 (PANC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +5.1 | 1e-05 | 26/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -8.8 | 8e-16 | 30/44 (CHP-212, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.691×** | -8.6 | 2e-15 | 37/49 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.729×** | -6.8 | 2e-09 | 31/45 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.784×** | -5.7 | 2e-06 | 25/48 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.818×** | -4.7 | 2e-04 | 24/48 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.818×** | -4.7 | 2e-04 | 26/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -4.7 | 2e-04 | 24/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -3.6 | 0.019 | 17/48 (C32, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.911× | -3.1 | 0.11 | 6/48 (NCI-H2347, SHP-77, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.877× | -3.1 | 0.11 | 8/48 (HT-29, SW48, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 191 | 14 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.36× (z +27.8) | [[Dinaciclib (drug)]] 0.05 µM 0.398× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 123 | 15 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +21.4) | — |
| [[SW480 (line)]] | alt | 108 | 11 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +23.8) | — |
| [[BT-474 (line)]] | alt | 109 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 112 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +19.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 8 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.72× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.431× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 231 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +26.1) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -11.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 197 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -23.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 229 | 9 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 156 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +22.6) | [[Dinaciclib (drug)]] 0.05 µM 0.500× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 221 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.537× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 106 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +29.0) | — |
| [[HEC-1-A (line)]] | alt | 145 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 158 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 134 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +12.0) | [[Lonafarnib (drug)]] 5 µM 0.137× (z -14.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 217 | 5 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.39× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -12.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 203 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -14.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 126 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +20.4) | — |
| [[CFPAC-1 (line)]] | alt | 119 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.8) | — |
| [[HS-578T (line)]] | alt | 80.1 | 7 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.15× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 142 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.536× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 244 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.479× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 149 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.489× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 91.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.9) | — |
| [[HCT15 (line)]] | alt | 189 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.78× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 113 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 136 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +14.0) | — |
| [[KATO III (line)]] | alt | 102 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.09× (z +14.3) | — |
| [[LoVo (line)]] | wt | 99.3 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.99× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +18.8) | — |
| [[SNU-423 (line)]] | alt | 81.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.0) | — |
| [[C-33 A (line)]] | alt | 194 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -13.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 101 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +14.2) | — |
| [[H4 (line)]] | wt | 103 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 106 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 97.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 4 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.05× (z +11.8) | [[Lonafarnib (drug)]] 5 µM 0.0894× (z -13.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 149 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 128 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +16.3) | — |
| [[A498 (line)]] | wt | 162 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +22.0) | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -10.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 229 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 97.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 100 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -11.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 164 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +11.9) | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.301× (z -10.1) |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0923× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN2]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[AKAP8L]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[STRN3]] | +0.60 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[KIF9-AS1]] | +0.60 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[NDUFB1]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[C2orf42]] | +0.59 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[ZBTB8OS]] | +0.59 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[ATAD2B]] | +0.58 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[ARID1A]] | +0.58 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[SOCS3-DT]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[C2]] | +0.56 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[RBX1]] | +0.56 | +0.40 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLX]] | -0.54 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[DTD1]] | -0.49 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[AGO1]] | -0.49 | -0.35 / -0.38 | both halves | 1e-04 | pathway: Intracellular signaling by second messengers |
| [[GNAI3]] | -0.49 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[SUGT1P4-STRA6LP-CCDC180]] | -0.48 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[C13orf46]] | -0.48 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[RALB]] | -0.48 | -0.43 / -0.23 | both halves | 5e-04 |  |
| [[IL17RD]] | -0.47 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SACS]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[GLO1]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[PODXL]] | -0.47 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[TPM3]] | -0.47 | -0.49 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.0, 15.3); signed map (4.5, -3.7). **Vector** length 103, 34.0% of its response variance represented; |z| ≥ 3 in 1,335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.2 | +0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +1.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.0 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4-phosphate 5-kinase type 1 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,197,949-151,249,536 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphatidylinositol-4-phosphate 5-kinase type 1 family |
| Reactome | 8 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; PI5P, PP2A and IER3 Regulate PI3K/AKT Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99755](https://www.uniprot.org/uniprotkb/Q99755) (Phosphatidylinositol 4-phosphate 5-kinase type-1 alpha):

> Catalyzes the phosphorylation of phosphatidylinositol 4-phosphate (PtdIns(4)P/PI4P) to form phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2/PIP2), a lipid second messenger that regulates several cellular processes such as signal transduction, vesicle trafficking, actin cytoskeleton dynamics, cell adhesion, and cell motility. PtdIns(4,5)P2 can directly act as a second messenger or can be utilized as a precursor to generate other second messengers: inositol 1,4,5-trisphosphate (IP3), …

**Summary**, from NCBI Gene [8394](https://www.ncbi.nlm.nih.gov/gene/8394):

> Enables 1-phosphatidylinositol-4-phosphate 5-kinase activity and kinase binding activity. Involved in several processes, including activation of GTPase activity; focal adhesion assembly; and ruffle assembly. Located in several cellular components, including lamellipodium; nucleus; and ruffle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8994) · Entrez [8394](https://www.ncbi.nlm.nih.gov/gene/8394) · UniProt [Q99755](https://www.uniprot.org/uniprotkb/Q99755) · Ensembl [ENSG00000143398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143398)

## Data

Gene col 6736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6736); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6736]; `tensor/DDL_lfc|DDL_z.npy` [6736]; `embed/gene_vectors.npy` [6736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6736 or target_col == 6736). Every well: [[PIP5K1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP5K1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
