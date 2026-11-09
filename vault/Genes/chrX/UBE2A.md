---
symbol: "UBE2A"
type: "gene"
col: 1197
ensembl_id: "ENSG00000077721"
name: "ubiquitin conjugating enzyme E2 A"
location: "Xq24"
module: 54
arm: "-"
pooled_cpm: 48.65
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# UBE2A

*ubiquitin conjugating enzyme E2 A* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.91× (z +23.6, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +23.3, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCRN1]] (+0.63, fdr 1e-05), [[WDR45]] (+0.61, fdr 3e-05), [[CYB5D2]] (+0.59, fdr 3e-05); moves opposite to [[SNU13]] (-0.69, fdr 7e-06), [[NPM3]] (-0.67, fdr 5e-05), [[RPL22L1]] (-0.66, fdr 4e-05, ⚠ RPL22L1 in the vector space only through flagged drug-doses), [[TSEN54]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +23.6 | 0e+00 | 47/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +23.3 | 0e+00 | 45/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +22.5 | 0e+00 | 38/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +16.9 | 0e+00 | 39/43 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +13.6 | 8e-40 | 42/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +12.3 | 2e-32 | 40/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.67×** | +10.9 | 1e-25 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.60×** | +10.4 | 2e-23 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.9 | 2e-17 | 30/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.8 | 7e-17 | 38/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.47×** | +8.5 | 7e-16 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.5 | 2e-12 | 32/48 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +7.3 | 9e-12 | 33/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 1e-11 | 34/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.40×** | +7.2 | 2e-11 | 31/47 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +7.1 | 5e-11 | 31/48 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +6.8 | 3e-10 | 26/48 (J82, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.7 | 5e-10 | 25/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +6.0 | 6e-08 | 29/48 (SNU-423, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.010 | 9/48 (A-427, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.018 | 9/46 (HCT15, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.022 | 17/48 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.4 | 0.006 | 0/49 | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 0.758× | -3.2 | 0.29 | 10/48 (Hs 766T, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.861× | -3.2 | 0.29 | 12/48 (NCI-H2347, J82, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.30 | 12/48 (SW48, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.7 | 12 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +23.5) | — |
| [[SW480 (line)]] | alt | 67.0 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +21.7) | — |
| [[HOP62 (line)]] | alt | 50.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.4) | — |
| [[LoVo (line)]] | wt | 40.0 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.9) | — |
| [[A498 (line)]] | wt | 61.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.8) | — |
| [[A549 (line)]] | wt | 51.5 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 42.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 74.0 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 45.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.2) | — |
| [[J82 (line)]] | alt | 67.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 57.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 47.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 54.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +11.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 38.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.2) | — |
| [[KATO III (line)]] | alt | 62.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 57.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.4) | — |
| [[AsPC-1 (line)]] | alt | 59.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 25.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 41.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +10.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 39.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 43.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.1) | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +16.7) | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 31.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 67.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.8) | — |
| [[A-172 (line)]] | wt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.34× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +10.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.24× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +10.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 46.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 39.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCRN1]] | +0.63 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[WDR45]] | +0.61 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CYB5D2]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[EIF4G2]] | +0.59 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[CROCC]] | +0.59 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TAX1BP3]] | +0.58 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[PRKAR1A]] | +0.58 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[DDX6]] | +0.58 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[AKT1S1]] | +0.58 | +0.58 / +0.36 | both halves | 9e-05 |  |
| [[SUCLG2-DT]] | +0.58 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[DVL3]] | +0.58 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[TIA1]] | +0.57 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNU13]] | -0.69 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[NPM3]] | -0.67 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[RPL22L1]] ⚠ | -0.66 | -0.41 / -0.63 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TSEN54]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[MRPS34]] | -0.64 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RMND1]] | -0.63 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NARS2]] | -0.61 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[UQCRH]] | -0.61 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[MMS19]] | -0.61 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[POP7]] | -0.60 | -0.37 / -0.58 | both halves | 9e-05 |  |
| [[DHX57]] | -0.60 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[WDR3]] | -0.60 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[DDX55]] | -0.59 | -0.37 / -0.62 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBE2A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF655]] | B | ZNF655 activity lowers UBE2A's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.25× higher at baseline in the lines without ZNF655 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-13.6, -43.5); signed map (21.0, -21.0). **Vector** length 72.0, 15.6% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +23.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +22.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +23.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +7.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,474,802-119,591,083 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBC2, HHR6A, RAD6A, HR6A |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 6 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [P49459](https://www.uniprot.org/uniprotkb/P49459) (Ubiquitin-conjugating enzyme E2 A):

> E2 ubiquitin-conjugating enzyme that accepts ubiquitin from the ubiquitin-activating enzyme E1 and transfers it to a E3 ubiquitin-protein ligase. In vitro catalyzes 'Lys-11', as well as 'Lys-48'-linked polyubiquitination. Together with the E3 enzyme BRE1 (RNF20 and/or RNF40), plays a role in transcription regulation by catalyzing the monoubiquitination of histone H2B at 'Lys-120' to form H2BK120ub1. H2BK120ub1 gives a specific tag for epigenetic transcriptional activation, elongation by RNA …

**Summary**, from NCBI Gene [7319](https://www.ncbi.nlm.nih.gov/gene/7319):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, ubiquitin-conjugating enzymes, and ubiquitin-protein ligases. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is required for post-replicative DNA damage repair, and may play a role in transcriptional regulation. Mutations in …

**Accessions** — [HGNC:12472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12472) · Entrez [7319](https://www.ncbi.nlm.nih.gov/gene/7319) · UniProt [P49459](https://www.uniprot.org/uniprotkb/P49459) · Ensembl [ENSG00000077721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077721)

## Data

Gene col 1197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1197); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1197]; `tensor/DDL_lfc|DDL_z.npy` [1197]; `embed/gene_vectors.npy` [1197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1197 or target_col == 1197). Every well: [[UBE2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
