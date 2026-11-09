---
symbol: "HMGCR"
type: "gene"
col: 3435
ensembl_id: "ENSG00000113161"
name: "3-hydroxy-3-methylglutaryl-CoA reductase"
location: "5q13.3"
module: 86
arm: "+"
pooled_cpm: 57.06
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 17
n_dd_up_clean: 32
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# HMGCR

*3-hydroxy-3-methylglutaryl-CoA reductase* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (10 with an alert ⚠); the strongest is [[Berbamine (drug)]] 5 µM: 2.60× (z +19.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.523× (z -9.4, q 4e-18, down in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Temsirolimus (drug)]] 0.05 µM: 0.693× (z -5.3, q 2e-05, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSMO1]] (+0.93, fdr 7e-06), [[FDFT1]] (+0.91, fdr 7e-06), [[DHCR7]] (+0.85, fdr 7e-06); moves opposite to [[ZC3H7B]] (-0.43, fdr 1e-04), [[ITPA]] (-0.42, fdr 8e-05), [[TRMT13]] (-0.42, fdr 2e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[PMP22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 5 µM |  | **2.60×** | +19.5 | 0e+00 | 48/49 (LoVo, HOP62, …) | rises with dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **2.25×** | +16.6 | 0e+00 | 47/48 (HOP62, LoVo, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.74×** | +11.7 | 2e-29 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +10.8 | 5e-25 | 45/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +10.2 | 3e-22 | 43/47 (LoVo, C-33 A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.01×** | +9.5 | 2e-19 | 43/48 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +9.4 | 3e-19 | 40/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.6 | 4e-16 | 32/48 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.90×** | +8.0 | 6e-14 | 36/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +7.9 | 2e-13 | 39/48 (SNU-423, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +7.8 | 3e-13 | 38/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +6.6 | 2e-09 | 38/43 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.6 | 2e-09 | 28/48 (HOP62, HS-578T, …) | top dose only | plate-row cell shift |
| [[Terfenadine (drug)]] 5 µM |  | **1.34×** | +6.0 | 7e-08 | 35/48 (NCI-H2030, HT-29, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.54×** | +6.0 | 7e-08 | 34/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.50×** | +5.8 | 2e-07 | 27/48 (C-33 A, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 3e-07 | 30/48 (SK-MEL-2, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.523×** | -9.4 | 4e-18 | 36/49 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -8.5 | 7e-15 | 32/42 (KATO III, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.693×** | -5.3 | 2e-05 | 36/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.705×** | -5.1 | 6e-05 | 32/48 (RKO, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.715×** | -4.9 | 1e-04 | 28/48 (A-427, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.698×** | -4.8 | 1e-04 | 31/47 (NCI-H1792, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -4.7 | 2e-04 | 26/48 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -4.5 | 4e-04 | 24/45 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Quinestrol (drug)]] 5 µM |  | **0.802×** | -4.5 | 4e-04 | 26/49 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.746×** | -4.2 | 0.001 | 26/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.744×** | -4.1 | 0.002 | 26/48 (KATO III, COLO 205, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.783×** | -3.5 | 0.018 | 19/48 (C32, KATO III, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.022 | 21/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.800×** | -3.2 | 0.050 | 16/48 (HS-578T, LS 180, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 5 µM |  | **0.811×** | -3.0 | 0.086 | 15/48 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 0.5 µM |  | **0.813×** | -3.0 | 0.089 | 16/47 (KATO III, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.7 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +10.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.31× (z +10.2) | — |
| [[KATO III (line)]] | alt | 93.5 | 2 | 4 (2 ⚠) | [[Berbamine (drug)]] 5 µM 2.57× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.342× (z -9.1) |
| [[SW480 (line)]] | alt | 44.9 | 6 | 0 | [[TAK-901 (drug)]] 5 µM 7.80× (z +11.0) | — |
| [[LoVo (line)]] | wt | 66.3 | 4 (2 ⚠) | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 4.42× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.6 | 4 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.31× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 59.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 5.24× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 67.8 | 4 | 0 | [[Berbamine (drug)]] 5 µM 2.51× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 66.7 | 4 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 3.68× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 74.7 | 3 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 4.13× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 52.1 | 2 | 2 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 4.34× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 107 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0956× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.406× (z -8.6) |
| [[A498 (line)]] | wt | 45.2 | 2 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 2.84× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 75.3 | 2 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 3.18× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 52.3 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 3.69× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 48.0 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 5.23× (z +19.1) | — |
| [[HT-29 (line)]] | alt | 76.5 | 2 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 3.68× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 78.8 | 2 | 1 | [[Berbamine (drug)]] 5 µM 2.34× (z +11.2) | [[Harringtonine (drug)]] 0.5 µM 0.403× (z -8.5) |
| [[SNU-1 (line)]] | wt | 79.7 | 2 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 3.44× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 40.7 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.40× (z +14.6) | — |
| [[C32 (line)]] | wt | 46.5 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.52× (z +11.1) | — |
| [[H4 (line)]] | wt | 28.3 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.48× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 56.6 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.91× (z +15.0) | — |
| [[hTERT-HPNE (line)]] | wt | 48.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.72× (z +11.3) | — |
| [[J82 (line)]] | alt | 39.9 | 2 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 93.7 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.45× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 33.1 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.43× (z +17.5) | — |
| [[NCI-H2347 (line)]] | alt | 89.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 58.2 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.42× (z +8.9) ⚠ toxic | [[XRK3F2 (drug)]] 0.5 µM 0.121× (z -11.2) |
| [[SNU-423 (line)]] | alt | 33.3 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.61× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 49.8 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.23× (z +12.7) | — |
| [[SW48 (line)]] | wt | 59.6 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.18× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 99.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -12.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[BT-474 (line)]] | alt | 123 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.299× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 36.2 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.40× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 54.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.29× (z +8.6) ⚠ toxic | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0876× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 45.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[CHP-212 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSMO1]] | +0.93 | +0.91 / +0.90 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 902 |
| [[FDFT1]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 954 |
| [[DHCR7]] | +0.85 | +0.89 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 904 |
| [[FDPS]] | +0.84 | +0.84 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 967 |
| [[IDI1]] | +0.83 | +0.84 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 926 |
| [[SCD]] | +0.82 | +0.87 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 747 |
| [[SQLE]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 973 |
| [[MVD]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 896 |
| [[HMGCS1]] | +0.79 | +0.83 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 999 |
| [[CYP51A1]] | +0.77 | +0.87 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 948 |
| [[ERG28]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 | STRING 550 |
| [[ACSS2]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 588 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | -0.43 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[ITPA]] | -0.42 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[TRMT13]] | -0.42 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ANKRD18A]] | -0.41 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMP22]] | B | HMGCR activity lowers PMP22's level | compounds that target HMGCR: 2 of 2 raise it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[IQCD]] | B | HMGCR activity raises IQCD's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NDRG1]] | B | HMGCR activity lowers NDRG1's level | compounds that target HMGCR: 2 of 2 raise it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds |
| [[SLC35G1]] | B | HMGCR activity raises SLC35G1's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.935). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, -49.1); signed map (-52.8, 32.5). **Vector** length 137, 48.6% of its response variance represented; |z| ≥ 3 in 1,611 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.76 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.72 to 7); *SREBP1 lipogenesis* (control, mean cos +0.65 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +11.3 | +16.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +10.3 | +19.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +7.0 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.7 | +10.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +2.0 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +5.6 | +5.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.7 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxy-3-methylglutaryl-CoA reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:75,336,329-75,364,001 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, ANDROGEN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: Lanosterol biosynthesis; EGR2 and SOX10-mediated initiation of Schwann cell myelination; Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P04035](https://www.uniprot.org/uniprotkb/P04035) (3-hydroxy-3-methylglutaryl-coenzyme A reductase):

> Catalyzes the conversion of (3S)-hydroxy-3-methylglutaryl-CoA (HMG-CoA) to mevalonic acid, the rate-limiting step in the synthesis of cholesterol and other isoprenoids, thus plays a critical role in cellular cholesterol homeostasis. HMGCR is the main target of statins, a class of cholesterol-lowering drugs.

**Summary**, from NCBI Gene [3156](https://www.ncbi.nlm.nih.gov/gene/3156):

> HMG-CoA reductase is the rate-limiting enzyme for cholesterol synthesis and is regulated via a negative feedback mechanism mediated by sterols and non-sterol metabolites derived from mevalonate, the product of the reaction catalyzed by reductase. Normally in mammalian cells this enzyme is suppressed by cholesterol derived from the internalization and degradation of low density lipoprotein (LDL) via the LDL receptor. Competitive inhibitors of the reductase induce the expression of LDL receptors …

**Accessions** — [HGNC:5006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5006) · Entrez [3156](https://www.ncbi.nlm.nih.gov/gene/3156) · UniProt [P04035](https://www.uniprot.org/uniprotkb/P04035) · Ensembl [ENSG00000113161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113161)

## Data

Gene col 3435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3435); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3435]; `tensor/DDL_lfc|DDL_z.npy` [3435]; `embed/gene_vectors.npy` [3435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3435 or target_col == 3435). Every well: [[HMGCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
