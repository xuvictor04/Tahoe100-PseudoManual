---
symbol: "ARHGAP39"
type: "gene"
col: 7221
ensembl_id: "ENSG00000147799"
name: "Rho GTPase activating protein 39"
location: "8q24.3"
module: 190
arm: "+"
pooled_cpm: 35.37
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# ARHGAP39

*Rho GTPase activating protein 39* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.88× (z +28.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.634× (z -6.7, q 1e-08, down in 27 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.695× (z -5.3, q 3e-05, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCA4]] (+0.55, fdr 1e-05), [[CCDC57]] (+0.52, fdr 4e-05), [[PPRC1]] (+0.50, fdr 1e-05); moves opposite to [[SLC18B1]] (-0.55, fdr 3e-05), [[TFG]] (-0.55, fdr 1e-05), [[COX15]] (-0.53, fdr 3e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.88×** | +28.0 | 0e+00 | 45/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.34×** | +17.6 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +15.2 | 0e+00 | 46/47 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.72×** | +14.6 | 0e+00 | 48/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +11.9 | 1e-30 | 41/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +8.6 | 6e-16 | 38/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +8.3 | 1e-14 | 33/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +8.2 | 2e-14 | 39/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +7.2 | 4e-11 | 29/48 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.8 | 6e-10 | 31/47 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +5.1 | 1e-05 | 29/48 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 28/47 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +5.0 | 2e-05 | 22/46 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 3e-05 | 23/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.6 | 2e-04 | 23/46 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.5 | 2e-04 | 28/48 (NCI-H460, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.634×** | -6.7 | 1e-08 | 27/42 (HCT15, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.695×** | -5.3 | 3e-05 | 27/47 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -4.7 | 4e-04 | 24/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -3.6 | 0.040 | 19/39 (HS-578T, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.786×** | -3.5 | 0.044 | 17/47 (Hs 766T, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +22.2) | — |
| [[HOP62 (line)]] | alt | 31.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 24.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +19.1) | — |
| [[A498 (line)]] | wt | 15.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +14.1) | — |
| [[LoVo (line)]] | wt | 45.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 37.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 25.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +12.3) | — |
| [[SW1417 (line)]] | alt | 59.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +18.8) | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.57× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 33.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +15.1) | — |
| [[LS 180 (line)]] | wt | 49.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +16.8) | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 38.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.9) | — |
| [[RKO (line)]] | wt | 86.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -11.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 13.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +12.2) | [[Tucidinostat (drug)]] 0.5 µM 0.118× (z -8.9) |
| [[SW 900 (line)]] | alt | 31.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +15.1) | — |
| [[A549 (line)]] | wt | 47.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 40.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 74.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -11.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +19.3) | — |
| [[HCT15 (line)]] | alt | 47.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 54.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +15.2) | — |
| [[Hs 766T (line)]] | wt | 27.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +9.7) | [[Ferulic acid (drug)]] 0.5 µM 0.0659× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +17.5) | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 64.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +10.3) | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.176× (z -8.7) ⚠ transcription drop; unreliable plate only |
| [[A-427 (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -13.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.113× (z -9.5) |
| [[COLO 205 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +12.3) | — |
| [[H4 (line)]] | wt | 8.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 41.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.6) | — |
| [[KATO III (line)]] | alt | 53.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +18.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +14.1) | — |
| [[NCI-H1573 (line)]] | alt | 34.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +15.4) | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +10.9) | — |
| [[A-172 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA4]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CCDC57]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[PPRC1]] | +0.50 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[REXO1]] | +0.50 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DMWD]] | +0.50 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TET3]] | +0.50 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R37]] | +0.50 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[RNF213-AS1]] | +0.49 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[GATAD2A]] | +0.49 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[KATNIP]] | +0.49 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[RNF123]] | +0.49 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[KLF16]] | +0.48 | +0.55 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC18B1]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[TFG]] | -0.55 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[COX15]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SDHAF4]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TSNAX]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MRPS30-DT]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[CISD2]] | -0.49 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[TBPL1]] | -0.49 | -0.21 / -0.50 | both halves | 7e-04 |  |
| [[GSTA4]] | -0.48 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[EPHX2]] | -0.48 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[CIAO2A]] | -0.48 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[BPNT1]] | -0.48 | -0.28 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | ARHGAP39's natural level lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | ARHGAP39's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.029 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction -0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.3, -38.8); signed map (8.7, -47.9). **Vector** length 91.4, 23.5% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +28.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.0 | +8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.6 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +1.8 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.9 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.0 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,529,179-144,685,846 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1688, Vilse, CrGAP |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 17 pathways, smallest: Inactivation of CDC42 and RAC1; RHOF GTPase cycle; RHOD GTPase cycle |
| Matched by | ensembl_id |

UniProt [Q9C0H5](https://www.uniprot.org/uniprotkb/Q9C0H5) carries no function annotation.

**Summary**, from NCBI Gene [80728](https://www.ncbi.nlm.nih.gov/gene/80728):

> Predicted to enable GTPase activator activity. Involved in postsynapse organization. Is active in glutamatergic synapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29351) · Entrez [80728](https://www.ncbi.nlm.nih.gov/gene/80728) · UniProt [Q9C0H5](https://www.uniprot.org/uniprotkb/Q9C0H5) · Ensembl [ENSG00000147799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147799)

## Data

Gene col 7221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7221); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7221]; `tensor/DDL_lfc|DDL_z.npy` [7221]; `embed/gene_vectors.npy` [7221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7221 or target_col == 7221). Every well: [[ARHGAP39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
