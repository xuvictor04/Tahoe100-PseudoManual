---
symbol: "SUPV3L1"
type: "gene"
col: 7988
ensembl_id: "ENSG00000156502"
name: "Suv3 like RNA helicase"
location: "10q22.1"
module: 107
arm: "+"
pooled_cpm: 40.85
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 19
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# SUPV3L1

*Suv3 like RNA helicase* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 9.12× (z +15.6, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.609× (z -9.5, q 1e-18, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A38]] (+0.69, fdr 7e-06), [[PMS2]] (+0.67, fdr 1e-05), [[MRPS30]] (+0.65, fdr 7e-06); moves opposite to [[CCDC88A]] (-0.63, fdr 1e-05), [[SRSF9]] (-0.62, fdr 1e-05, ⚠ SRSF9 in the vector space only through flagged drug-doses), [[IER2]] (-0.59, fdr 2e-05), [[GOLT1A]] (-0.57, fdr 2e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **9.12×** | +15.6 | 0e+00 | 49/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **7.08×** | +13.8 | 8e-41 | 47/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +9.3 | 3e-18 | 43/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +7.8 | 9e-13 | 35/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +7.7 | 2e-12 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +7.5 | 5e-12 | 32/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +7.4 | 1e-11 | 39/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 1e-09 | 36/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +6.6 | 2e-09 | 29/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.9 | 2e-07 | 27/48 (A-427, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 3e-06 | 34/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 9e-06 | 29/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.9 | 4e-05 | 20/35 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 2e-04 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 24/48 (Panc 03.27, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 6e-04 | 25/48 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 21/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.005 | 22/48 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7988.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.609×** | -9.5 | 1e-18 | 45/48 (SW1417, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.564×** | -7.8 | 2e-12 | 33/46 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -6.8 | 3e-09 | 29/38 (AN3 CA, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.684×** | -5.2 | 3e-05 | 31/48 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.718×** | -4.5 | 8e-04 | 30/47 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.723×** | -4.1 | 0.004 | 25/45 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.760×** | -3.7 | 0.016 | 24/48 (NCI-H1792, SW1417, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.686×** | -3.7 | 0.018 | 20/48 (HOP62, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.771×** | -3.5 | 0.025 | 20/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.777×** | -3.4 | 0.034 | 24/48 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.781×** | -3.4 | 0.039 | 15/48 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -3.3 | 0.041 | 23/43 (C-33 A, J82, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.791×** | -3.2 | 0.060 | 17/48 (PANC-1, HS-578T, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.797×** | -3.1 | 0.078 | 14/48 (NCI-H2030, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 50.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +12.6) | — |
| [[A-172 (line)]] | wt | 35.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 38.8 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +14.1) | — |
| [[NCI-H1573 (line)]] | alt | 29.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 40.7 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.52× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 49.7 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.39× (z +12.6) | — |
| [[A549 (line)]] | wt | 33.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0605× (z -19.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 30.3 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 11.1× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 39.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.0× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 42.6 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 36.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.4× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 48.4 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 9.09× (z +10.5) | [[Tucidinostat (drug)]] 5 µM 0.505× (z -8.9) |
| [[KATO III (line)]] | alt | 30.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 31.0 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.72× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 21.8× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 40.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +10.7) | — |
| [[RKO (line)]] | wt | 49.6 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 12.0× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 53.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.92× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 32.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.65× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 89.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -12.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 41.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 41.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.41× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 26.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 31.1× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -12.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 38.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.2× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 28.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.3× (z +9.4) | — |
| [[J82 (line)]] | alt | 31.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.54× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.8× (z +9.6) | — |
| [[SW48 (line)]] | wt | 60.0 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.43× (z +9.9) | — |
| [[A498 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A38]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[PMS2]] | +0.67 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[MRPS30]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[EIF2A]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[DDX49]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 | STRING 406 |
| [[TSN]] | +0.61 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TMEM68]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[EIF3E]] | +0.60 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[ZNF343]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CNPY2]] | +0.60 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[ATP6V1H]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[TFB2M]] | +0.58 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 400 |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC88A]] | -0.63 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[SRSF9]] ⚠ | -0.62 | -0.53 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IER2]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[GOLT1A]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[GDPD5]] | -0.56 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[EIF5A2]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PICALM]] | -0.55 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[TUBB4B]] | -0.54 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[AREG]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TNFRSF12A]] | -0.54 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MYL12A]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CALM2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[BMAL1]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.1, -12.7); signed map (-32.3, -21.0). **Vector** length 79.7, 21.2% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | +4.1 | +2.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +15.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.8 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +13.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +1.7 | +0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.6 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | Suv3 like RNA helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:69,180,234-69,209,099 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUV3 |
| Hallmark sets | MYC_TARGETS_V2, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYB8](https://www.uniprot.org/uniprotkb/Q8IYB8) (ATP-dependent RNA helicase SUPV3L1, mitochondrial):

> Major helicase player in mitochondrial RNA metabolism. Component of the mitochondrial degradosome (mtEXO) complex, that degrades 3' overhang double-stranded RNA with a 3'-to-5' directionality in an ATP-dependent manner. Involved in the degradation of non-coding mitochondrial transcripts (MT-ncRNA) and tRNA-like molecules. ATPase and ATP-dependent multisubstrate helicase, able to unwind double-stranded (ds) DNA and RNA, and RNA/DNA heteroduplexes in the 5'-to-3' direction. Plays a role in the …

**Summary**, from NCBI Gene [6832](https://www.ncbi.nlm.nih.gov/gene/6832):

> Enables several functions, including double-stranded RNA binding activity; helicase activity; and protein homodimerization activity. Contributes to 3'-5'-RNA exonuclease activity. Involved in several processes, including mitochondrial RNA metabolic process; positive regulation of cell growth; and positive regulation of mitochondrial RNA catabolic process. Located in mitochondrial nucleoid and nucleus. Part of mitochondrial degradosome. Is active in mitochondrial matrix. [provided by Alliance of …

**Accessions** — [HGNC:11471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11471) · Entrez [6832](https://www.ncbi.nlm.nih.gov/gene/6832) · UniProt [Q8IYB8](https://www.uniprot.org/uniprotkb/Q8IYB8) · Ensembl [ENSG00000156502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156502)

## Data

Gene col 7988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7988); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7988]; `tensor/DDL_lfc|DDL_z.npy` [7988]; `embed/gene_vectors.npy` [7988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7988 or target_col == 7988). Every well: [[SUPV3L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPV3L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
