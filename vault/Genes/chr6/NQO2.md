---
symbol: "NQO2"
type: "gene"
col: 4547
ensembl_id: "ENSG00000124588"
name: "N-ribosyldihydronicotinamide:quinone dehydrogenase 2"
location: "6p25.2"
module: 72
arm: "+"
pooled_cpm: 39.49
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# NQO2

*N-ribosyldihydronicotinamide:quinone dehydrogenase 2* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.17× (z +16.9, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.555× (z -12.8, q 7e-35, down in 33 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.309× (z -12.5, q 1e-33, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD3]] (+0.67, fdr 1e-05), [[NGLY1]] (+0.66, fdr 7e-06), [[NDRG1]] (+0.64, fdr 1e-05); moves opposite to [[ITGB8]] (-0.65, fdr 1e-05), [[HNRNPD]] (-0.62, fdr 3e-05), [[ZNF644]] (-0.62, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HSPA1A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +16.9 | 0e+00 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +16.6 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +15.3 | 0e+00 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +14.2 | 7e-44 | 42/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +12.4 | 5e-33 | 29/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +9.1 | 1e-17 | 34/48 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +8.9 | 4e-17 | 28/48 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +8.1 | 3e-14 | 30/48 (COLO 205, KATO III, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +7.9 | 2e-13 | 29/48 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +6.5 | 4e-09 | 25/47 (COLO 205, KATO III, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +6.0 | 1e-07 | 22/47 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 3e-06 | 27/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +5.4 | 3e-06 | 21/47 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +4.7 | 1e-04 | 19/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.24×** | +4.6 | 2e-04 | 20/46 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +4.3 | 5e-04 | 16/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.1 | 0.001 | 6/48 (LoVo, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -12.8 | 7e-35 | 33/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -12.5 | 1e-33 | 40/49 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.590×** | -11.5 | 3e-28 | 36/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.395×** | -9.9 | 4e-21 | 38/48 (HOP62, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.647×** | -9.5 | 3e-19 | 33/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -9.2 | 3e-18 | 30/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.647×** | -9.1 | 6e-18 | 28/47 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -9.1 | 6e-18 | 28/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.685×** | -7.9 | 1e-13 | 30/48 (A-172, SK-MEL-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.809×** | -6.5 | 4e-09 | 26/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -6.5 | 6e-09 | 25/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[EX229 (drug)]] 5 µM |  | **0.613×** | -5.2 | 8e-06 | 19/48 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.779×** | -5.0 | 2e-05 | 19/41 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.792×** | -4.9 | 4e-05 | 20/38 (HEC-1-A, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.792×** | -4.9 | 4e-05 | 23/48 (NCI-H1573, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.819×** | -4.1 | 0.001 | 19/47 (A-172, C32, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.824×** | -4.0 | 0.002 | 16/48 (LoVo, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -3.7 | 0.006 | 14/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Folic acid (drug)]] 5 µM |  | 0.904× | -3.1 | 0.051 | 6/48 (RPMI-7951, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.870× | -3.0 | 0.061 | 11/47 (SK-MEL-2, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 57.7 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -24.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -14.3) |
| [[PANC-1 (line)]] | alt | 40.5 | 5 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.34× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.300× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -13.4) |
| [[SW480 (line)]] | alt | 26.8 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.71× (z +11.7) | [[Digitoxin (drug)]] 0.05 µM 0.449× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.200× (z -9.2) |
| [[KATO III (line)]] | alt | 54.7 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.320× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.414× (z -9.0) |
| [[LoVo (line)]] | wt | 65.6 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.02× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 41.0 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.19× (z +10.0) | [[TAK-901 (drug)]] 5 µM 0.109× (z -9.3) |
| [[COLO 205 (line)]] | alt | 35.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.80× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.261× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.3 | 2 | 2 | [[Belinostat (drug)]] 5 µM 2.50× (z +8.8) | [[PH-797804 (drug)]] 5 µM 0.0754× (z -12.2) |
| [[HT-29 (line)]] | alt | 24.0 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.92× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 89.3 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0581× (z -11.6) |
| [[SNU-423 (line)]] | alt | 68.5 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.7) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -18.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 53.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.399× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.192× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 61.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 49.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.61× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 50.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Thymol (drug)]] 0.5 µM 0.299× (z -8.9) |
| [[J82 (line)]] | alt | 56.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.21× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 48.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 49.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 25.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.5) | — |
| [[A498 (line)]] | wt | 22.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.32× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -11.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[Hs 766T (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.217× (z -9.8) ⚠ toxic |
| [[HS-578T (line)]] | alt | 42.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0863× (z -20.8) |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 25.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.261× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A-427 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD3]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[NGLY1]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[NDRG1]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[AZIN2]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[FAM219A]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[P4HA2]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MED31]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[UBA6]] | +0.61 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[GIPR]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PWWP3A]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[FLYWCH1]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ZNF823]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB8]] | -0.65 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.62 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[ZNF644]] | -0.62 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[HNRNPH3]] | -0.58 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[POGLUT1]] | -0.58 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PARVA]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TBCEL]] | -0.55 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SCAF8]] | -0.55 | -0.24 / -0.61 | both halves | 5e-04 |  |
| [[ZMYND11]] | -0.55 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ZFP91]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DPY19L1P2]] | -0.55 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[TCF12]] | -0.55 | -0.36 / -0.57 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSPA1A]] | B | HSPA1A activity lowers NQO2's level | lines that do not express HSPA1A (13) vs lines expressing it (37) | 1.30× higher at baseline in the lines without HSPA1A | 0.060 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ATP13A3-DT, ZNF569, GCAWKR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.6, -15.5); signed map (-39.6, 30.0). **Vector** length 103, 26.1% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.9 | +6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +14.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +1.3 |
|  | [[Infigratinib (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +2.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.3 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -5.9 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -9.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.5 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.7 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | N-ribosyldihydronicotinamide:quinone dehydrogenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:2,987,987-3,019,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | QR2, DHQV, DIA6; previously NMOR2 |
| Gene groups (HGNC) | Flavoproteins; Quinone dehydrogenase family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P16083](https://www.uniprot.org/uniprotkb/P16083) (Ribosyldihydronicotinamide dehydrogenase):

> The enzyme apparently serves as a quinone reductase in connection with conjugation reactions of hydroquinones involved in detoxification pathways as well as in biosynthetic processes such as the vitamin K-dependent gamma-carboxylation of glutamate residues in prothrombin synthesis.

**Summary**, from NCBI Gene [4835](https://www.ncbi.nlm.nih.gov/gene/4835):

> This gene encodes a member of the thioredoxin family of enzymes. It is a cytosolic and ubiquitously expressed flavoprotein that catalyzes the two-electron reduction of quinone substrates and uses dihydronicotinamide riboside as a reducing coenzyme. Mutations in this gene have been associated with neurodegenerative diseases and several cancers. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:7856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7856) · Entrez [4835](https://www.ncbi.nlm.nih.gov/gene/4835) · UniProt [P16083](https://www.uniprot.org/uniprotkb/P16083) · Ensembl [ENSG00000124588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124588)

## Data

Gene col 4547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4547); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4547]; `tensor/DDL_lfc|DDL_z.npy` [4547]; `embed/gene_vectors.npy` [4547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4547 or target_col == 4547). Every well: [[NQO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NQO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
