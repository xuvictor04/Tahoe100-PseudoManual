---
symbol: "SLC30A1"
type: "gene"
col: 9945
ensembl_id: "ENSG00000170385"
name: "solute carrier family 30 member 1"
location: "1q32.3"
module: 7
arm: "+"
pooled_cpm: 51.48
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SLC30A1

*solute carrier family 30 member 1* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.59× (z +34.4, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.603× (z -7.2, q 3e-10, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEZF1]] (+0.66, fdr 7e-06), [[C21orf91]] (+0.65, fdr 1e-05), [[SKIL]] (+0.63, fdr 1e-05); moves opposite to [[UQCRH]] (-0.59, fdr 2e-05), [[PHKA2]] (-0.58, fdr 2e-05), [[WRN]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.59×** | +34.4 | 0e+00 | 46/46 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.67×** | +21.8 | 0e+00 | 45/46 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.93×** | +14.6 | 0e+00 | 40/46 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +11.0 | 7e-26 | 35/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.73×** | +11.0 | 7e-26 | 38/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +9.1 | 9e-18 | 32/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +8.8 | 1e-16 | 35/45 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +8.5 | 2e-15 | 34/47 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +8.2 | 2e-14 | 36/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +8.1 | 2e-14 | 33/47 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +8.0 | 8e-14 | 30/47 (LoVo, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +7.8 | 3e-13 | 32/47 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.6 | 8e-07 | 27/47 (NCI-H460, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.1 | 1e-05 | 2/47 (MIA PaCa-2, Panc 03.27) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.8 | 6e-05 | 23/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.3 | 6e-04 | 21/45 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 7e-04 | 23/47 (A-172, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.603×** | -7.2 | 3e-10 | 33/47 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -4.9 | 3e-04 | 29/47 (SW 900, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.701×** | -4.8 | 3e-04 | 25/47 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.015 | 19/47 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.790×** | -3.4 | 0.072 | 14/47 (NCI-H1573, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.783×** | -3.4 | 0.072 | 18/46 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.723×** | -3.3 | 0.078 | 16/45 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.731×** | -3.2 | 0.092 | 16/47 (COLO 205, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.092 | 16/47 (HCT15, RPMI-7951, …) | top dose only |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.857× | -3.1 | 0.093 | 19/47 (SNU-1, LoVo, …) | top dose only |  |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.860× | -3.1 | 0.11 | 10/47 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.665× | -3.0 | 0.11 | 18/42 (HepG2/C3A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 73.1 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +30.2) | — |
| [[A-172 (line)]] | wt | 56.9 | 11 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 22.1× (z +20.4) | — |
| [[SW480 (line)]] | alt | 37.7 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +36.5) | — |
| [[LOX-IMVI (line)]] | wt | 40.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +38.1) | — |
| [[C32 (line)]] | wt | 20.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +22.6) | — |
| [[HEC-1-A (line)]] | alt | 49.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +29.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +26.8) | — |
| [[RKO (line)]] | wt | 29.4 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 48.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.1× (z +38.8) | — |
| [[PANC-1 (line)]] | alt | 63.2 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 17.2 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 23.6× (z +19.8) | — |
| [[A549 (line)]] | wt | 59.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 66.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.7× (z +39.8) | — |
| [[J82 (line)]] | alt | 35.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.6× (z +33.2) | — |
| [[KATO III (line)]] | alt | 29.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +19.2) | — |
| [[NCI-H23 (line)]] | alt | 38.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[A498 (line)]] | wt | 144 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 34.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.2× (z +29.5) | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.4× (z +25.4) | — |
| [[NCI-H2030 (line)]] | alt | 28.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 125× (z +39.1) | — |
| [[NCI-H2347 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.1) | — |
| [[SW48 (line)]] | wt | 26.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +15.5) | — |
| [[COLO 205 (line)]] | alt | 84.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0997× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.312× (z -8.8) |
| [[H4 (line)]] | wt | 62.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +20.9) | — |
| [[HS-578T (line)]] | alt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +13.2) | — |
| [[LoVo (line)]] | wt | 88.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.29× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 79.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 53.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +26.1) | — |
| [[SNU-1 (line)]] | wt | 50.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.8) | [[Ciclopirox (drug)]] 5 µM 0.281× (z -10.1) |
| [[SNU-423 (line)]] | alt | 40.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 58.5× (z +27.7) | — |
| [[C-33 A (line)]] | alt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +14.3) | — |
| [[HCT15 (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 54.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.7) | — |
| [[NCI-H1573 (line)]] | alt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +15.0) | — |
| [[NCI-H661 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 66.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +10.4) | — |
| [[SW 1088 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.0× (z +11.5) | — |
| [[SW 1271 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 67.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -9.5) |
| [[SW1417 (line)]] | alt | 60.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[C21orf91]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SKIL]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[BBS10]] | +0.60 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ZBTB33]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[RBM22]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[BTG2]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[ZNF436]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TUG1]] | +0.58 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[RRM2B]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ZNF564]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.59 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[PHKA2]] | -0.58 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[WRN]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NMRAL1]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PPIH]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[TOMM5]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[IQCB1]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[EEF1AKMT2]] | -0.53 | -0.68 / -0.36 | both halves | 9e-05 |  |
| [[TYW1]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[EIF3CL]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NUP85]] | -0.53 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ARMH3]] | -0.52 | -0.59 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC30A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises SLC30A1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.351). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (27.2, -28.1); signed map (14.1, -4.1). **Vector** length 115, 31.4% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.3 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +21.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +34.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +8.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.7 | +1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -8.6 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.5 | -4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.2 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 30 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:211,571,568-211,579,161 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZRC1; previously ZNT1 |
| Gene groups (HGNC) | Solute carrier family 30 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: Zinc transporters; Metal ion SLC transporters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6M5](https://www.uniprot.org/uniprotkb/Q9Y6M5) (Proton-coupled zinc antiporter SLC30A1):

> Zinc ion:proton antiporter that could function at the plasma membrane mediating zinc efflux from cells against its electrochemical gradient protecting them from intracellular zinc accumulation and toxicity. Alternatively, could prevent the transport to the plasma membrane of CACNB2, the L-type calcium channels regulatory subunit, through a yet to be defined mechanism. By modulating the expression of these channels at the plasma membrane, could prevent calcium and zinc influx into cells. By the …

**Summary**, from NCBI Gene [7779](https://www.ncbi.nlm.nih.gov/gene/7779):

> Enables calcium:monoatomic cation antiporter activity and zinc:proton antiporter activity. Involved in defense response to bacterium; intracellular zinc ion homeostasis; and transition metal ion transport. Located in several cellular components, including Golgi apparatus; basolateral plasma membrane; and nuclear membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11012) · Entrez [7779](https://www.ncbi.nlm.nih.gov/gene/7779) · UniProt [Q9Y6M5](https://www.uniprot.org/uniprotkb/Q9Y6M5) · Ensembl [ENSG00000170385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170385)

## Data

Gene col 9945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9945); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9945]; `tensor/DDL_lfc|DDL_z.npy` [9945]; `embed/gene_vectors.npy` [9945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9945 or target_col == 9945). Every well: [[SLC30A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC30A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
