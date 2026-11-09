---
symbol: "NOP2"
type: "gene"
col: 3248
ensembl_id: "ENSG00000111641"
name: "NOP2 nucleolar protein"
location: "12p13.31"
module: 5
arm: "+"
pooled_cpm: 31.75
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 17
n_dd_up_clean: 27
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NOP2

*NOP2 nucleolar protein* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +17.1, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.683× (z -5.9, q 2e-06, down in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.724× (z -4.8, q 2e-04, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP16]] (+0.86, fdr 7e-06), [[WDR4]] (+0.81, fdr 7e-06), [[MRTO4]] (+0.81, fdr 7e-06); moves opposite to [[OPTN]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 21 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +17.1 | 0e+00 | 37/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +14.1 | 7e-43 | 39/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **5.36×** | +13.4 | 8e-39 | 46/48 (SW480, A-427, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **5.32×** | +13.4 | 1e-38 | 43/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.38×** | +13.2 | 1e-37 | 42/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +12.5 | 5e-34 | 46/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +12.1 | 2e-31 | 38/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +12.0 | 2e-31 | 37/47 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.16×** | +11.8 | 3e-30 | 39/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +11.7 | 6e-30 | 40/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +11.0 | 2e-26 | 39/47 (C32, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **2.08×** | +10.7 | 4e-25 | 41/46 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.00×** | +10.5 | 3e-24 | 39/47 (NCI-H2347, HOP62, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +10.1 | 3e-22 | 39/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.92×** | +9.9 | 1e-21 | 39/47 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.36×** | +6.8 | 2e-10 | 35/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 1e-08 | 29/47 (NCI-H23, HCT15, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.07×** | +5.8 | 2e-07 | 35/47 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +5.8 | 2e-07 | 30/48 (NCI-H2347, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.00×** | +5.5 | 8e-07 | 27/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.94×** | +5.3 | 3e-06 | 26/47 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.683×** | -5.9 | 2e-06 | 26/48 (LoVo, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.722×** | -4.9 | 2e-04 | 26/47 (NCI-H2030, H4, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.724×** | -4.8 | 2e-04 | 23/47 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.726×** | -4.8 | 2e-04 | 25/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.768×** | -4.7 | 3e-04 | 19/48 (A-427, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.722×** | -4.7 | 3e-04 | 18/47 (LoVo, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.812×** | -4.5 | 5e-04 | 24/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.583×** | -4.4 | 9e-04 | 18/48 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.756×** | -4.3 | 9e-04 | 23/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.766×** | -4.1 | 0.002 | 22/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.833×** | -3.9 | 0.005 | 15/48 (MIA PaCa-2, SW480, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.792×** | -3.9 | 0.005 | 19/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.817×** | -3.8 | 0.006 | 19/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.010 | 17/47 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.797×** | -3.5 | 0.015 | 18/47 (NCI-H2030, A498, …) | rises with dose | low cells (technical?) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.818×** | -3.0 | 0.098 | 11/48 (SW480, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[AZD-8055 (drug)]] 5 µM |  | **0.693×** | -3.0 | 0.098 | 6/48 (NCI-H23, A498, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 61.0 | 6 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.15× (z +11.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.90× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.01× (z +9.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.65× (z +8.8) | [[Adagrasib (drug)]] 0.05 µM 0.658× (z -10.1) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 31.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +14.7) | — |
| [[A-427 (line)]] | wt | 107 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.53× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.539× (z -9.0) |
| [[A498 (line)]] | wt | 30.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +19.8) | — |
| [[LOX-IMVI (line)]] | wt | 32.5 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +11.1) | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.8) | — |
| [[RKO (line)]] | wt | 70.6 | 1 | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 10.1× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -9.5) |
| [[HOP62 (line)]] | alt | 17.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.7) | — |
| [[LoVo (line)]] | wt | 48.8 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.84× (z +8.6) ⚠ toxic; cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.67× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 25.5 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.32× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 46.8 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 8.98× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 90.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 28.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.91× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 37.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0793× (z -14.7) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 0.0608× (z -8.8) |
| [[A549 (line)]] | wt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 46.2 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0932× (z -9.2) |
| [[C32 (line)]] | wt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 8.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +11.7) | — |
| [[H4 (line)]] | wt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.77× (z +9.8) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.2) | — |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP16]] | +0.86 | +0.86 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 422 |
| [[WDR4]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 | STRING 689 |
| [[MRTO4]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 988 |
| [[TBRG4]] | +0.81 | +0.76 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 590 |
| [[PPRC1]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 536 |
| [[BYSL]] | +0.79 | +0.80 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 915 |
| [[TWNK]] | +0.79 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[PUS1]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 723 |
| [[URB2]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 | STRING 993 |
| [[DDX31]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | STRING 756 |
| [[DHX33]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPTN]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NOP2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers NOP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CPLX1]] | B | CPLX1 activity raises NOP2's level | lines that do not express CPLX1 (9) vs lines expressing it (41) | 1.71× lower at baseline in the lines without CPLX1 | 0.079 | ⚠ within organs, on part of the lines; also absent: LLGL2, CASZ1, MNX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.8, -36.6); signed map (-1.9, -46.9). **Vector** length 96.7, 29.2% of its response variance represented; |z| ≥ 3 in 1,421 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.62 to 16); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.61 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +12.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +13.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +5.1 | +10.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.8 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +5.3 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.8 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | NOP2 nucleolar protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,556,863-6,568,691 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOP120, NSUN1, p120; previously NOL1 |
| Gene groups (HGNC) | NOP2/Sun RNA methyltransferase family; DNA/RNA methyltransferases |
| Hallmark sets | MYC_TARGETS_V2, IL2_STAT5_SIGNALING |
| Reactome | 6 pathways, smallest: TFAP2A acts as a transcriptional repressor during retinoic acid induced cell differentiation; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors; rRNA modification in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P46087](https://www.uniprot.org/uniprotkb/P46087) (28S rRNA):

> S-adenosyl-L-methionine-dependent methyltransferase that specifically methylates the C(5) position of cytosine 4447 in 28S rRNA. Required for efficient rRNA processing and 60S ribosomal subunit biogenesis. Regulates pre-rRNA processing through non-catalytic complex formation with box C/D snoRNAs and facilitates the recruitment of U3 and U8 snoRNAs to pre-90S ribosomal particles and their stable assembly into snoRNP complexes. May play a role in the regulation of the cell cycle and the increased …

**Summary**, from NCBI Gene [4839](https://www.ncbi.nlm.nih.gov/gene/4839):

> Enables rRNA (cytosine-C5-)-methyltransferase activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosome biogenesis. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7867) · Entrez [4839](https://www.ncbi.nlm.nih.gov/gene/4839) · UniProt [P46087](https://www.uniprot.org/uniprotkb/P46087) · Ensembl [ENSG00000111641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111641)

## Data

Gene col 3248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3248); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3248]; `tensor/DDL_lfc|DDL_z.npy` [3248]; `embed/gene_vectors.npy` [3248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3248 or target_col == 3248). Every well: [[NOP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
