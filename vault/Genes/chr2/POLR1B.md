---
symbol: "POLR1B"
type: "gene"
col: 4634
ensembl_id: "ENSG00000125630"
name: "RNA polymerase I subunit B"
location: "2q14.1"
module: 33
arm: "+"
pooled_cpm: 29.27
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# POLR1B

*RNA polymerase I subunit B* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.13× (z +13.6, q 4e-39, up in 44 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.11× (z +13.3, q 6e-38, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.566× (z -9.9, q 2e-20, down in 26 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.727× (z -5.6, q 5e-06, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR3]] (+0.90, fdr 7e-06), [[URB2]] (+0.82, fdr 7e-06), [[NLE1]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.13×** | +13.6 | 4e-39 | 44/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.11×** | +13.3 | 6e-38 | 43/48 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.09×** | +13.2 | 1e-37 | 38/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **4.00×** | +13.0 | 1e-36 | 37/46 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.90×** | +11.5 | 2e-28 | 35/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.70×** | +9.5 | 1e-19 | 35/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.74×** | +9.5 | 1e-19 | 31/46 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.36×** | +8.1 | 5e-14 | 33/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.9 | 3e-10 | 25/47 (NCI-H1792, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +6.7 | 1e-09 | 27/47 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.02×** | +6.6 | 2e-09 | 31/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.1 | 5e-08 | 25/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.40×** | +6.0 | 1e-07 | 22/47 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +6.0 | 1e-07 | 14/29 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +5.4 | 3e-06 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.76×** | +5.3 | 4e-06 | 21/46 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 9e-05 | 14/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 4e-04 | 19/47 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +4.2 | 7e-04 | 13/45 (SNU-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.001 | 16/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.003 | 10/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.005 | 6/48 (KATO III, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.20× | +3.2 | 0.029 | 11/48 (NCI-H1573, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -9.9 | 2e-20 | 26/40 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.589×** | -9.6 | 3e-19 | 28/45 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.727×** | -5.6 | 5e-06 | 23/47 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.788×** | -5.0 | 1e-04 | 20/48 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.769×** | -4.6 | 5e-04 | 15/47 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.772×** | -4.5 | 5e-04 | 15/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.789×** | -4.3 | 0.001 | 14/47 (Panc 03.27, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.2 | 0.002 | 18/46 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.799×** | -4.2 | 0.002 | 22/48 (C32, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.798×** | -4.1 | 0.002 | 13/47 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -4.1 | 0.002 | 21/48 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.827×** | -4.0 | 0.003 | 16/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.863× | -3.7 | 0.009 | 17/48 (SW48, SW480, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.835× | -3.3 | 0.038 | 13/47 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.830×** | -3.2 | 0.049 | 13/48 (SK-MEL-2, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 0.842× | -3.2 | 0.056 | 13/46 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 62.6 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.03× (z +9.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 29.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.25× (z +10.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.217× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +9.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 37.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -16.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 43.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -11.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 13.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 27.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 13.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -13.0) |
| [[PANC-1 (line)]] | alt | 42.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 56.0 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.92× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 19.0 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0600× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -19.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR3]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | STRING 958 |
| [[URB2]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | STRING 638 |
| [[NLE1]] | +0.82 | +0.81 / +0.80 | both halves | 7e-06 | STRING 784 |
| [[PDCD11]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 | STRING 977 |
| [[DDX31]] | +0.77 | +0.75 / +0.83 | both halves | 7e-06 | STRING 765 |
| [[WDR36]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 | STRING 951 |
| [[NOP16]] | +0.77 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 | same gene group; STRING 906 |
| [[DHX33]] | +0.76 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[WDR43]] | +0.75 | +0.79 / +0.77 | both halves | 7e-06 | STRING 831 |
| [[RIOK1]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises POLR1B's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without FAM78B | 0.012 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[ATXN1]] | B | ATXN1 activity lowers POLR1B's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 2.09× higher at baseline in the lines without ATXN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[MAP2K1]] | B | MAP2K1 activity raises POLR1B's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[MCOLN2]] | B | MCOLN2 activity raises POLR1B's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without MCOLN2 | 0.040 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[NT5M]] | B | NT5M activity raises POLR1B's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without NT5M | 0.048 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[MANEAL]] | B | MANEAL activity raises POLR1B's level | lines that do not express MANEAL (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without MANEAL | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.905). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.0, -39.6); signed map (-6.9, -51.0). **Vector** length 126, 36.7% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.65 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.69 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.69 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.7 | +13.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +13.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +5.6 | +9.5 |
|  | [[EX229 (drug)]] 5 µM |  | +5.2 | +8.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.9 | +6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.4 | +5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +5.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,541,915-112,579,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Rpo1-2, FLJ21921, FLJ10816, RPA2, RPA135 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 9 pathways, smallest: RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression; RNA Polymerase I Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9Y6](https://www.uniprot.org/uniprotkb/Q9H9Y6) (DNA-directed RNA polymerase I subunit RPA2):

> Catalytic core component of RNA polymerase I (Pol I), a DNA-dependent RNA polymerase which synthesizes ribosomal RNA precursors using the four ribonucleoside triphosphates as substrates. Transcribes 47S pre-rRNAs from multicopy rRNA gene clusters, giving rise to 5.8S, 18S and 28S ribosomal RNAs. Pol I-mediated transcription cycle proceeds through transcription initiation, transcription elongation and transcription termination stages. During transcription initiation, Pol I pre-initiation complex …

**Summary**, from NCBI Gene [84172](https://www.ncbi.nlm.nih.gov/gene/84172):

> Eukaryotic RNA polymerase I (pol I) is responsible for the transcription of ribosomal RNA (rRNA) genes and production of rRNA, the primary component of ribosomes. Pol I is a multisubunit enzyme composed of 6 to 14 polypeptides, depending on the species. Most of the mass of the pol I complex derives from the 2 largest subunits, Rpa1 and Rpa2 in yeast. POLR1B is homologous to Rpa2 (Seither and Grummt, 1996 [PubMed 8921381]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20454) · Entrez [84172](https://www.ncbi.nlm.nih.gov/gene/84172) · UniProt [Q9H9Y6](https://www.uniprot.org/uniprotkb/Q9H9Y6) · Ensembl [ENSG00000125630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125630)

## Data

Gene col 4634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4634); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4634]; `tensor/DDL_lfc|DDL_z.npy` [4634]; `embed/gene_vectors.npy` [4634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4634 or target_col == 4634). Every well: [[POLR1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
