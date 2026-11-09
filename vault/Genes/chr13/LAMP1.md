---
symbol: "LAMP1"
type: "gene"
col: 11749
ensembl_id: "ENSG00000185896"
name: "lysosome associated membrane protein 1"
location: "13q34"
module: 50
arm: "+"
pooled_cpm: 52.12
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# LAMP1

*lysosome associated membrane protein 1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.07× (z +21.1, q 0e+00, up in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.00× (z +13.0, q 1e-36, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.630× (z -8.4, q 3e-14, down in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (RPMI-7951 0.118×; ⚠ toxic); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.102×); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNS]] (+0.83, fdr 7e-06), [[PIGT]] (+0.80, fdr 7e-06), [[ATP6AP1]] (+0.77, fdr 7e-06); moves opposite to [[NKAP]] (-0.64, fdr 3e-05), [[SMIM26]] (-0.61, fdr 5e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPL46]] (-0.61, fdr 2e-04), [[MRPS18C]] (-0.61, fdr 1e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[COL6A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +21.1 | 0e+00 | 44/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +18.8 | 0e+00 | 39/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +17.6 | 0e+00 | 43/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +13.0 | 1e-36 | 43/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +10.9 | 2e-25 | 40/48 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +9.6 | 1e-19 | 38/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.66×** | +9.6 | 1e-19 | 39/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.66×** | +9.5 | 2e-19 | 44/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +9.4 | 5e-19 | 44/49 (A498, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +8.3 | 7e-15 | 38/48 (HT-29, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.53×** | +8.0 | 8e-14 | 35/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.53×** | +8.0 | 8e-14 | 35/47 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +6.9 | 2e-10 | 26/48 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +6.8 | 5e-10 | 34/47 (Panc 03.27, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +6.5 | 4e-09 | 22/35 (HOP62, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 2e-08 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.7 | 5e-07 | 25/48 (A-172, NCI-H460, …) | top dose only | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.008 | 17/47 (RPMI-7951, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.048 | 8/48 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +2.9 | 0.063 | 12/48 (NCI-H1573, J82, …) | top dose only |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 1.16× | +2.8 | 0.082 | 8/48 (NCI-H2347, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11749.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (RPMI-7951 0.118×; ⚠ toxic); [[Saquinavir (drug)]] 0.05 µM in 1 line (CHP-212 0.102×); [[Thymol (drug)]] 0.5 µM in 1 line (CHP-212 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.630×** | -8.4 | 3e-14 | 43/48 (NCI-H460, J82, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -3.7 | 0.065 | 21/48 (A-172, SW48, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.727× | -3.1 | 0.29 | 9/48 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.1 | 0.29 | 17/48 (A-172, HT-29, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.853× | -3.0 | 0.29 | 13/48 (hTERT-HPNE, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.1 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +25.8) | — |
| [[SW480 (line)]] | alt | 47.4 | 10 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 73.7 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.90× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.7) | — |
| [[A498 (line)]] | wt | 65.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.94× (z +8.6) | — |
| [[KATO III (line)]] | alt | 62.9 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 45.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 29.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 65.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +17.7) | — |
| [[HT-29 (line)]] | alt | 75.9 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.03× (z +11.6) | — |
| [[J82 (line)]] | alt | 149 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 44.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.0) | — |
| [[A-427 (line)]] | wt | 52.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 38.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +12.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 29.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.75× (z +15.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 30.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 69.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.8) | — |
| [[A-172 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +10.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 70.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +11.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 43.4 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.102× (z -9.5) |
| [[COLO 205 (line)]] | alt | 23.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +11.4) | — |
| [[HCT15 (line)]] | alt | 30.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 55.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 65.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.0) | — |
| [[Panc 03.27 (line)]] | alt | 65.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 55.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.8) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.118× (z -9.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 64.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.38× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.02× (z +10.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.05× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.66× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.86× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 53.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.02× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +11.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNS]] | +0.83 | +0.80 / +0.81 | both halves | 7e-06 | STRING 433 |
| [[PIGT]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[ATP6AP1]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 | STRING 462 |
| [[PPT1]] | +0.74 | +0.63 / +0.75 | both halves | 7e-06 | STRING 449 |
| [[LAMP2]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 | same gene group; STRING 999 |
| [[FKBP9]] | +0.73 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[CTSZ]] | +0.73 | +0.59 / +0.70 | both halves | 7e-06 | STRING 578 |
| [[EMC1]] | +0.72 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[SELENON]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[DDOST]] | +0.69 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[TPP1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 | STRING 401 |
| [[NCSTN]] | +0.67 | +0.57 / +0.71 | both halves | 9e-06 | STRING 747 |

## Genes that move opposite

*22 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | -0.64 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | -0.61 | -0.40 / -0.68 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL46]] | -0.61 | -0.31 / -0.67 | both halves | 2e-04 |  |
| [[MRPS18C]] | -0.61 | -0.32 / -0.73 | both halves | 1e-04 |  |
| [[PPP1R35]] ⚠ | -0.60 | -0.33 / -0.69 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | -0.60 | -0.33 / -0.69 | both halves | 1e-04 |  |
| [[TIPRL]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[ZNF503]] | -0.59 | -0.37 / -0.66 | both halves | 8e-05 |  |
| [[CROCCP2-1]] | -0.59 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[RPP21]] | -0.58 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[LEO1]] | -0.58 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[PIGBOS1]] | -0.58 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[SNHG8]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[EIF5B]] | -0.57 | -0.40 / -0.62 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL6A1]] | B | COL6A1 activity raises LAMP1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without COL6A1 | 0.064 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[COL3A1]] | B | COL3A1 activity raises LAMP1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.39× lower at baseline in the lines without COL3A1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.0, -21.4); signed map (-24.0, -36.8). **Vector** length 107, 30.4% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.55 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +17.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +18.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +21.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.9 | +13.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.2 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.2 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.9 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.4 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -5.2 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | lysosome associated membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,297,239-113,323,672 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD107a |
| Gene groups (HGNC) | CD molecules; Lysosome associated membrane proteins |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P11279](https://www.uniprot.org/uniprotkb/P11279) (Lysosome-associated membrane glycoprotein 1):

> Lysosomal membrane glycoprotein which plays an important role in lysosome biogenesis, lysosomal pH regulation, autophagy and cholesterol homeostasis. Acts as an important regulator of lysosomal lumen pH regulation by acting as a direct inhibitor of the proton channel TMEM175, facilitating lysosomal acidification for optimal hydrolase activity. Also plays an important role in NK-cells cytotoxicity. Mechanistically, participates in cytotoxic granule movement to the cell surface and perforin …

**Summary**, from NCBI Gene [3916](https://www.ncbi.nlm.nih.gov/gene/3916):

> The protein encoded by this gene is a member of a family of membrane glycoproteins. This glycoprotein provides selectins with carbohydrate ligands. It may also play a role in tumor cell metastasis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6499) · Entrez [3916](https://www.ncbi.nlm.nih.gov/gene/3916) · UniProt [P11279](https://www.uniprot.org/uniprotkb/P11279) · Ensembl [ENSG00000185896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185896)

## Data

Gene col 11749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11749); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11749]; `tensor/DDL_lfc|DDL_z.npy` [11749]; `embed/gene_vectors.npy` [11749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11749 or target_col == 11749). Every well: [[LAMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
