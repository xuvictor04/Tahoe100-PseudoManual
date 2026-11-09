---
symbol: "NDUFA9"
type: "gene"
col: 6273
ensembl_id: "ENSG00000139180"
name: "NADH:ubiquinone oxidoreductase subunit A9"
location: "12p13.3"
module: 220
arm: "+"
pooled_cpm: 42.14
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# NDUFA9

*NADH:ubiquinone oxidoreductase subunit A9* — 12p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.15× (z +18.9, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.832× (z -5.9, q 2e-06, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAF5]] (+0.66, fdr 7e-06), [[MRPS14]] (+0.63, fdr 2e-05), [[C12orf4]] (+0.61, fdr 1e-05); moves opposite to [[TPT1-AS1]] (-0.56, fdr 3e-05), [[ERN1]] (-0.53, fdr 1e-05), [[LRP2BP-AS1]] (-0.52, fdr 2e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.15×** | +18.9 | 0e+00 | 48/49 (SW480, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +12.3 | 1e-32 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.75×** | +11.6 | 4e-29 | 39/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +9.6 | 1e-19 | 32/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +7.1 | 1e-10 | 27/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +6.9 | 6e-10 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +6.8 | 9e-10 | 26/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.3 | 2e-08 | 27/47 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +5.9 | 3e-07 | 22/48 (SW480, A-427, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.53×** | +4.9 | 7e-05 | 19/47 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[LJI308 (drug)]] 0.05 µM |  | **1.25×** | +4.7 | 1e-04 | 21/48 (Hs 766T, NCI-H23, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.7 | 1e-04 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 2e-04 | 20/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.6 | 2e-04 | 16/36 (HOP62, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 18/47 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.002 | 11/47 (LOX-IMVI, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.008 | 12/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.010 | 5/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.012 | 10/48 (LOX-IMVI, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.017 | 13/47 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.832×** | -5.9 | 2e-06 | 23/48 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -5.3 | 3e-05 | 23/48 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.799×** | -5.1 | 7e-05 | 20/48 (AN3 CA, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.838× | -4.0 | 0.009 | 20/48 (SHP-77, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.8 | 0.018 | 16/47 (HOP62, SW 1271, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.731×** | -3.6 | 0.028 | 10/48 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.854× | -3.6 | 0.029 | 10/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.031 | 15/48 (H4, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.739×** | -3.5 | 0.031 | 6/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.852× | -3.4 | 0.039 | 8/48 (NCI-H2347, H4, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.900× | -3.4 | 0.039 | 11/48 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.3 | 0.043 | 20/48 (NCI-H460, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.3 | 0.043 | 16/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.754×** | -3.3 | 0.045 | 6/48 (AN3 CA, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.875× | -3.0 | 0.093 | 11/48 (hTERT-HPNE, LoVo, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.093 | 11/48 (Panc 03.27, C32, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 71.2 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.94× (z +15.7) | — |
| [[LS 180 (line)]] | wt | 57.8 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 6.61× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 34.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.0× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H23 (line)]] | alt | 79.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[PANC-1 (line)]] | alt | 30.9 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 45.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.32× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HOP62 (line)]] | alt | 39.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.10× (z +11.9) | — |
| [[KATO III (line)]] | alt | 44.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 32.1 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.99× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 64.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.07× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[RKO (line)]] | wt | 50.5 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.48× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.5) |
| [[A-427 (line)]] | wt | 72.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.29× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.8) |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.116× (z -9.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.273× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 53.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.33× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0622× (z -9.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.307× (z -9.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SW1417 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF5]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 707 |
| [[MRPS14]] | +0.63 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[C12orf4]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[EMC7]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[NDUFS4]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[ALKBH3]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MRPL22]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SNRPC]] | +0.58 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ABCB7]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[FASTKD3]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PGGT1B]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPT1-AS1]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[ERN1]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[LRP2BP-AS1]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[POU2F2]] | -0.52 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CPNE9]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CCNYL1]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HBEGF]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MIR9-1HG]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[AGO2]] | -0.50 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[HMGA1]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ARG2]] | -0.49 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[JOSD1]] | -0.49 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.6, -2.3); signed map (-11.7, -16.9). **Vector** length 95.4, 21.9% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +18.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.1 |
|  | [[NG25 (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.0 | +0.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -0.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | +1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.3 — chr12:4,649,095-4,694,317 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR22E1, CI-39k, COQ11; previously NDUFS2L |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; NADH:ubiquinone oxidoreductase supernumerary subunits; Flavoproteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16795](https://www.uniprot.org/uniprotkb/Q16795) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Required for proper complex I assembly. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4704](https://www.ncbi.nlm.nih.gov/gene/4704):

> The encoded protein is a subunit of the hydrophobic protein fraction of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. A pseudogene has been identified on chromosome 12. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:7693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7693) · Entrez [4704](https://www.ncbi.nlm.nih.gov/gene/4704) · UniProt [Q16795](https://www.uniprot.org/uniprotkb/Q16795) · Ensembl [ENSG00000139180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139180)

## Data

Gene col 6273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6273); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6273]; `tensor/DDL_lfc|DDL_z.npy` [6273]; `embed/gene_vectors.npy` [6273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6273 or target_col == 6273). Every well: [[NDUFA9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
