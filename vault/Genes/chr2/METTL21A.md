---
symbol: "METTL21A"
type: "gene"
col: 6875
ensembl_id: "ENSG00000144401"
name: "methyltransferase 21A, HSPA lysine"
location: "2q33.3"
module: 16
arm: "-"
pooled_cpm: 29.48
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# METTL21A

*methyltransferase 21A, HSPA lysine* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.05× (z +32.1, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.588× (z -5.7, q 8e-06, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGKE]] (+0.61, fdr 1e-05), [[LHX1-DT]] (+0.59, fdr 5e-05), [[TPTEP2-CSNK1E]] (+0.55, fdr 5e-05); moves opposite to [[PABIR1]] (-0.59, fdr 5e-05), [[THRAP3]] (-0.59, fdr 1e-05), [[KAT5]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DUSP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +32.1 | 0e+00 | 43/47 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +20.3 | 0e+00 | 45/47 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.59×** | +18.6 | 0e+00 | 41/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +11.6 | 5e-29 | 35/47 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +9.9 | 5e-21 | 31/46 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.47×** | +7.8 | 5e-13 | 28/47 (AsPC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.43×** | +7.3 | 2e-11 | 27/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.40×** | +6.6 | 2e-09 | 20/36 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.2 | 4e-08 | 24/48 (HOP62, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.32×** | +5.6 | 1e-06 | 24/44 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +5.6 | 1e-06 | 21/47 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.2 | 8e-06 | 21/48 (C32, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +5.1 | 2e-05 | 21/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.28×** | +4.9 | 3e-05 | 20/45 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.29×** | +4.8 | 5e-05 | 19/41 (C32, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 3e-04 | 17/47 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 5e-04 | 13/48 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 5e-04 | 16/47 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.001 | 7/47 (HEC-1-A, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.010 | 7/48 (CFPAC-1, C32, …) | two highest doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.013 | 7/47 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.028 | 6/47 (H4, NCI-H1573, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.12× | +3.1 | 0.035 | 7/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.054 | 10/47 (A-172, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.588×** | -5.7 | 8e-06 | 19/48 (NCI-H23, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -5.5 | 1e-05 | 19/46 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.769×** | -5.2 | 5e-05 | 16/47 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.803×** | -4.5 | 1e-03 | 12/47 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -4.3 | 0.002 | 14/47 (HS-578T, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.800×** | -4.2 | 0.002 | 17/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.846× | -4.1 | 0.004 | 16/48 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.826×** | -3.9 | 0.006 | 14/47 (NCI-H1573, A498, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.698×** | -3.8 | 0.007 | 7/47 (NCI-H23, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.830×** | -3.8 | 0.007 | 16/47 (SNU-423, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.835× | -3.7 | 0.011 | 13/47 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.841× | -3.6 | 0.017 | 15/47 (NCI-H460, SW 1271, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.037 | 12/47 (A498, NCI-H2030, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -3.3 | 0.039 | 10/47 (HS-578T, NCI-H23, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.895× | -3.2 | 0.043 | 13/48 (Hs 766T, SW 1088, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.739×** | -3.2 | 0.043 | 9/47 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.859× | -3.1 | 0.057 | 7/48 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 106 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -20.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.142× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 38.7 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +14.1) | — |
| [[RKO (line)]] | wt | 37.7 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -12.3) ⚠ cell-cycle shift, explains ~6% of this change |
| [[HEC-1-A (line)]] | alt | 31.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +16.1) | — |
| [[HOP62 (line)]] | alt | 21.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +14.0) | — |
| [[SW480 (line)]] | alt | 25.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +15.2) | — |
| [[A-172 (line)]] | wt | 24.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 21.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +20.2) | — |
| [[C32 (line)]] | wt | 16.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 14.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 20.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +12.1) | — |
| [[J82 (line)]] | alt | 49.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +15.5) | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 16.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +13.2) | [[Selinexor (drug)]] 5 µM 0.292× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 13.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +15.5) | — |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 15.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 22.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +15.0) | — |
| [[A498 (line)]] | wt | 57.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -9.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 27.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +11.2) | — |
| [[KATO III (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +11.0) | — |
| [[LoVo (line)]] | wt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +16.4) | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 32.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 50.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -10.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.6) | — |
| [[SW48 (line)]] | wt | 28.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +9.5) | — |
| [[A-427 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKE]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[LHX1-DT]] | +0.59 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.55 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[PLPP5]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[DPY19L2P3]] | +0.53 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[DHX32]] | +0.53 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[MAP3K14-AS1]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ING2-DT]] | +0.51 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[BCL2L2-PABPN1]] | +0.51 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[SNX14]] | +0.51 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[SAP30L-AS1]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[PRDM10]] | +0.50 | +0.37 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PABIR1]] | -0.59 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[THRAP3]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[KAT5]] | -0.59 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[ZNF22]] | -0.56 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[ZNF205]] | -0.56 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RNF40]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[HARS2]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SMIM8]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ZNF180]] | -0.54 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[IFTAP]] | -0.54 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[WDR7]] | -0.54 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[RHOBTB2]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP1]] | B | DUSP1 activity strengthens METTL21A's drug response | lines that do not express DUSP1 (6) vs lines expressing it (42) | the lines without DUSP1 respond 0.67× as strongly (z diff +1.44); strongest at Dinaciclib 5 µM: 0.34x vs 1.38x (z diff +9.0) | 0.014 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers METTL21A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LBH]] | B | LBH activity lowers METTL21A's level | lines that do not express LBH (22) vs lines expressing it (28) | 1.46× higher at baseline in the lines without LBH | 0.032 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, PLAT |
| [[DUSP1]] | B | DUSP1 activity lowers METTL21A's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without DUSP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.422). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.8, -1.2); signed map (3.0, 11.6). **Vector** length 98.9, 22.8% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +32.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +20.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +18.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.4 | -5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -4.0 | +3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | +2.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.8 | -3.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.7 | -3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 21A, HSPA lysine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:207,580,631-207,625,928 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC151194, HCA557b, HSPA-KMT; previously FAM119A |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Reactome | 1 pathways, smallest: Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXB1](https://www.uniprot.org/uniprotkb/Q8WXB1) (Protein N-lysine methyltransferase METTL21A):

> Protein-lysine methyltransferase that selectively trimethylates residues in heat shock protein 70 (HSP70) family members. Contributes to the in vivo trimethylation of Lys residues in HSPA1 and HSPA8. In vitro methylates 'Lys-561' in HSPA1, 'Lys-564' in HSPA2, 'Lys-585' in HSPA5, 'Lys-563' in HSPA6 and 'Lys-561' in HSPA8.

**Summary**, from NCBI Gene [151194](https://www.ncbi.nlm.nih.gov/gene/151194):

> Enables ATPase binding activity; Hsp70 protein binding activity; and protein-lysine N-methyltransferase activity. Involved in negative regulation of protein folding and protein methylation. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30476) · Entrez [151194](https://www.ncbi.nlm.nih.gov/gene/151194) · UniProt [Q8WXB1](https://www.uniprot.org/uniprotkb/Q8WXB1) · Ensembl [ENSG00000144401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144401)

## Data

Gene col 6875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6875); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6875]; `tensor/DDL_lfc|DDL_z.npy` [6875]; `embed/gene_vectors.npy` [6875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6875 or target_col == 6875). Every well: [[METTL21A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL21A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
