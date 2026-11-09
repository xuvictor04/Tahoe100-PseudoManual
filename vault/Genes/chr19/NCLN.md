---
symbol: "NCLN"
type: "gene"
col: 4692
ensembl_id: "ENSG00000125912"
name: "nicalin"
location: "19p13.3"
module: 4
arm: "+"
pooled_cpm: 21.29
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NCLN

*nicalin* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.16× (z +12.8, q 1e-34, up in 39 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.91× (z +10.8, q 5e-25, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.721× (z -7.8, q 4e-12, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOC2L]] (+0.68, fdr 7e-06), [[CHID1]] (+0.66, fdr 7e-06), [[ANKS6]] (+0.66, fdr 7e-06); moves opposite to [[CDKN1B]] (-0.61, fdr 1e-05), [[FBXO8]] (-0.59, fdr 1e-05), [[PHF3]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.16×** | +12.8 | 1e-34 | 39/43 (SK-MEL-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.01×** | +11.2 | 2e-26 | 26/35 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.95×** | +11.1 | 2e-26 | 43/47 (A-172, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.93×** | +10.9 | 1e-25 | 43/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +10.8 | 5e-25 | 40/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.89×** | +10.5 | 5e-24 | 42/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +10.2 | 3e-22 | 43/47 (SW480, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.88×** | +10.1 | 4e-22 | 39/44 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.78×** | +9.6 | 4e-20 | 34/46 (PANC-1, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +8.7 | 3e-16 | 37/48 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +8.6 | 3e-16 | 38/47 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.60×** | +7.2 | 2e-11 | 26/41 (J82, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +6.9 | 2e-10 | 28/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +6.8 | 5e-10 | 27/47 (A-172, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.41×** | +5.5 | 2e-06 | 22/46 (SNU-423, HS-578T, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.94×** | +5.2 | 7e-06 | 19/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.90×** | +5.0 | 1e-05 | 19/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +5.0 | 2e-05 | 19/47 (PANC-1, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 2e-05 | 15/48 (A498, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.85×** | +4.8 | 4e-05 | 20/44 (SNU-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 4e-05 | 19/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.49×** | +4.7 | 5e-05 | 18/48 (A-172, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.73×** | +4.3 | 4e-04 | 16/46 (NCI-H460, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 6e-04 | 14/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +4.2 | 6e-04 | 15/45 (A498, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.003 | 12/44 (HS-578T, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.721×** | -7.8 | 4e-12 | 27/47 (LoVo, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.783×** | -4.0 | 0.021 | 21/47 (SW48, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.770×** | -3.8 | 0.030 | 15/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.845× | -3.4 | 0.075 | 13/48 (MIA PaCa-2, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.075 | 16/47 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.846× | -3.3 | 0.086 | 15/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.660×** | -3.3 | 0.086 | 6/47 (Hs 766T, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | 0.771× | -3.1 | 0.13 | 6/48 (A498, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.882× | -3.0 | 0.15 | 16/48 (SNU-423, A549, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.837× | -3.0 | 0.15 | 13/47 (SNU-423, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +9.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A498 (line)]] | wt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[PANC-1 (line)]] | alt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.3) |
| [[A549 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.313× (z -9.7) ⚠ cell-cycle shift, explains ~73% of this change |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.113× (z -8.5) |
| [[HS-578T (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.98× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[LoVo (line)]] | wt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.0) |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.313× (z -10.6) ⚠ cell-cycle shift, explains ~73% of this change |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOC2L]] | +0.68 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CHID1]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PPM1F]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[WDR5]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[TCOF1]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[DFFA]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[POP1]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[EIPR1]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN1B]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FBXO8]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PHF3]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[RBM7]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB10]] | -0.57 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PNRC1]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[THAP1]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.57 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[OSER1-DT]] | -0.57 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.56 | -0.64 / -0.32 | both halves | 2e-04 |  |
| [[N4BP2L1]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[CREBRF]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity raises NCLN's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without NCS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[ADCY3]] | B | ADCY3 activity raises NCLN's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without ADCY3 | 0.082 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[GARNL3]] | C | GARNL3 activity raises NCLN's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[ANKRD13B]] | C | ANKRD13B activity raises NCLN's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without ANKRD13B | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.6, -39.0); signed map (-10.2, -55.8). **Vector** length 85.9, 19.1% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +10.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +4.1 | +11.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +4.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.3 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | nicalin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,185,563-3,209,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NICALIN, NET59 |
| Gene groups (HGNC) | M28 metallopeptidases; BOS complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969V3](https://www.uniprot.org/uniprotkb/Q969V3) (BOS complex subunit NCLN):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions. May antagonize Nodal signaling and subsequent organization of axial …

**Summary**, from NCBI Gene [56926](https://www.ncbi.nlm.nih.gov/gene/56926):

> Enables ribosome binding activity. Involved in several processes, including multi-pass transmembrane protein insertion into ER membrane; protein stabilization; and regulation of protein complex stability. Located in endoplasmic reticulum membrane. Part of multi-pass translocon complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26923) · Entrez [56926](https://www.ncbi.nlm.nih.gov/gene/56926) · UniProt [Q969V3](https://www.uniprot.org/uniprotkb/Q969V3) · Ensembl [ENSG00000125912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125912)

## Data

Gene col 4692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4692); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4692]; `tensor/DDL_lfc|DDL_z.npy` [4692]; `embed/gene_vectors.npy` [4692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4692 or target_col == 4692). Every well: [[NCLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
