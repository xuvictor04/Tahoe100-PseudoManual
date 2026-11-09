---
symbol: "TMEM107"
type: "gene"
col: 10990
ensembl_id: "ENSG00000179029"
name: "transmembrane protein 107"
location: "17p13.1"
module: 91
arm: "+"
pooled_cpm: 14.03
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# TMEM107

*transmembrane protein 107* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.34× (z +24.0, q 0e+00, up in 25 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 7.05× (z +21.0, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.468× (z -8.0, q 5e-13, down in 32 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.581× (z -6.1, q 3e-07, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMC2]] (+0.64, fdr 1e-05), [[REXO5]] (+0.56, fdr 1e-05), [[IFT81]] (+0.56, fdr 3e-05); moves opposite to [[C19orf12]] (-0.59, fdr 2e-05), [[CTU1]] (-0.56, fdr 3e-05), [[CCZ1P1]] (-0.55, fdr 2e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.34×** | +24.0 | 0e+00 | 25/25 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.45×** | +23.9 | 0e+00 | 38/38 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **7.05×** | +21.0 | 0e+00 | 38/46 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.84×** | +13.9 | 7e-42 | 32/34 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.06×** | +11.4 | 5e-28 | 27/45 (HEC-1-A, COLO 205, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +6.3 | 3e-08 | 24/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +5.2 | 2e-05 | 25/46 (A549, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.49×** | +4.5 | 5e-04 | 21/47 (SW480, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 0.05 µM |  | **1.47×** | +4.1 | 0.003 | 12/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.056 | 12/48 (SW480, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | 1.32× | +3.1 | 0.10 | 16/42 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.468×** | -8.0 | 5e-13 | 32/46 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.581×** | -6.1 | 3e-07 | 29/47 (HEC-1-A, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.776×** | -4.0 | 0.011 | 24/48 (H4, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -3.8 | 0.020 | 18/47 (NCI-H23, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -3.6 | 0.037 | 11/44 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.555×** | -3.5 | 0.052 | 18/46 (SNU-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Gallic acid (drug)]] 0.05 µM |  | **0.738×** | -3.4 | 0.052 | 14/47 (NCI-H661, H4, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.743×** | -3.3 | 0.061 | 17/47 (C-33 A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.746×** | -3.2 | 0.097 | 15/47 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.760× | -3.1 | 0.11 | 10/46 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.681× | -3.1 | 0.11 | 6/48 (hTERT-HPNE, SNU-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 14.1 | 6 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 44.3× (z +18.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 16.4× (z +13.6) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.178× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 14.9 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.8× (z +20.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 10.1× (z +14.8) | — |
| [[NCI-H23 (line)]] | alt | 34.5 | 1 (1 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -18.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.232× (z -9.7) |
| [[SW480 (line)]] | alt | 16.6 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.6× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 5.15× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +17.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 15.6× (z +16.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.1× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 11.0× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 17.6 | 5 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 22.8× (z +14.7) | — |
| [[A-427 (line)]] | wt | 43.7 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.03× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 8.86 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.4× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 6.10× (z +9.7) | — |
| [[C32 (line)]] | wt | 20.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.0× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 7.32× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 7.63 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +14.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 19.9× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 11.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.56× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 7.55× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 8.76 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.46× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 7.51× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 14.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.46× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 9.32× (z +12.8) | — |
| [[LoVo (line)]] | wt | 6.71 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +11.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.16× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 5.37 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 13.5× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 12.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.67× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 5.16× (z +10.5) | — |
| [[A-172 (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.3× (z +12.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 10.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +15.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 30.6× (z +13.2) | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.6× (z +9.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 14.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.4× (z +14.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.30× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 7.74× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 6.93 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.51× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 10.0× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.22× (z +10.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 12.2× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 5.97 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 13.8× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +9.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 8.01 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 28.1× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.85× (z +9.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 7.82 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 12.4× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 9.22 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.115× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 24.4× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC2]] | +0.64 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[REXO5]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[IFT81]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NASP]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PER2]] | +0.54 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TEX14]] | +0.52 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ESPL1]] | +0.52 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.52 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[HIRIP3]] | +0.52 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[UBR5]] | +0.52 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[CLASP1-AS1]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[AGL]] | +0.51 | +0.36 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf12]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CTU1]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CCZ1P1]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[C8orf76]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ZNF169]] | -0.54 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[LSP1P4]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZNF749]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[POP1]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.52 | -0.37 / -0.59 | both halves | 7e-05 |  |
| [[CCNY-AS1]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MIEF1]] | -0.51 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[MED10]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises TMEM107's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.05× lower at baseline in the lines without MYBL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[DUXAP10]] | B | DUXAP10 activity raises TMEM107's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without DUXAP10 | 0.054 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.413). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-44.9, -4.6); signed map (12.3, -14.9). **Vector** length 86.7, 18.3% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +21.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.7 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +23.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +24.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Furosemide (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.4 | -8.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -2.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | -3.5 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 107 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,172,457-8,176,399 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10744, JBTS29, MKS13 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX40](https://www.uniprot.org/uniprotkb/Q6UX40) (Transmembrane protein 107):

> Plays a role in cilia formation and embryonic patterning. Requires for normal Sonic hedgehog (Shh) signaling in the neural tube and acts in combination with GLI2 and GLI3 to pattern ventral and intermediate neuronal cell types (By similarity). During ciliogenesis regulates the ciliary transition zone localization of some MKS complex proteins.

**Summary**, from NCBI Gene [84314](https://www.ncbi.nlm.nih.gov/gene/84314):

> This gene encodes a transmembrane protein and component of the primary cilia transition zone. The encoded protein regulates ciliogenesis and ciliary protein composition. Human fibroblasts expressing a mutant allele of this gene exhibit reduced numbers of cilia, altered cilia length, and impaired sonic hedgehog signaling. In human patients, different mutations in this gene cause different ciliopathies, including Meckel-Gruber syndrome and orofaciodigital syndrome. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:28128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28128) · Entrez [84314](https://www.ncbi.nlm.nih.gov/gene/84314) · UniProt [Q6UX40](https://www.uniprot.org/uniprotkb/Q6UX40) · Ensembl [ENSG00000179029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179029)

## Data

Gene col 10990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10990); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10990]; `tensor/DDL_lfc|DDL_z.npy` [10990]; `embed/gene_vectors.npy` [10990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10990 or target_col == 10990). Every well: [[TMEM107 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM107.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
