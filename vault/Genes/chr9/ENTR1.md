---
symbol: "ENTR1"
type: "gene"
col: 9169
ensembl_id: "ENSG00000165689"
name: "endosome associated trafficking regulator 1"
location: "9q34.3"
module: 5
arm: "+"
pooled_cpm: 16.95
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 7
n_dd_up_clean: 23
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ENTR1

*endosome associated trafficking regulator 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.93× (z +15.5, q 0e+00, up in 26 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +12.0, q 6e-31, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.801× (z -4.7, q 0.002, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM65]] (+0.65, fdr 8e-06), [[ACTR3B]] (+0.64, fdr 7e-06), [[PUS1]] (+0.63, fdr 7e-06); moves opposite to [[SRP14]] (-0.67, fdr 9e-06), [[HSPB1]] (-0.60, fdr 1e-05), [[SOD1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 18 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.93×** | +15.5 | 0e+00 | 26/29 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.56×** | +14.1 | 1e-42 | 37/41 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +12.0 | 6e-31 | 37/46 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +11.3 | 1e-27 | 33/43 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.18×** | +10.8 | 4e-25 | 22/34 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.81×** | +8.9 | 7e-17 | 32/47 (Hs 766T, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +7.9 | 3e-13 | 33/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +7.1 | 1e-10 | 23/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.57×** | +6.7 | 1e-09 | 24/47 (Hs 766T, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.39×** | +4.9 | 7e-05 | 19/47 (J82, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.00×** | +4.8 | 9e-05 | 17/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.39×** | +4.7 | 1e-04 | 20/47 (A-172, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.6 | 2e-04 | 15/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.35×** | +4.5 | 3e-04 | 17/42 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 3e-04 | 22/46 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 4e-04 | 20/46 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.86×** | +4.3 | 6e-04 | 14/46 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.84×** | +4.2 | 8e-04 | 12/46 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.001 | 10/47 (A498, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.9 | 0.002 | 15/46 (A549, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.003 | 13/46 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.008 | 10/46 (SW1417, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.009 | 9/47 (A498, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.015 | 5/47 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.016 | 11/46 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.030 | 6/45 (LoVo, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.801×** | -4.7 | 0.002 | 18/48 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.777×** | -4.3 | 0.004 | 15/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.748×** | -4.2 | 0.004 | 18/48 (RKO, SW48, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.747×** | -4.1 | 0.004 | 18/47 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.753×** | -4.1 | 0.004 | 13/48 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.773×** | -3.8 | 0.013 | 17/47 (HT-29, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.781×** | -3.8 | 0.013 | 11/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.12 | 12/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.810× | -3.1 | 0.12 | 15/47 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.7) | — |
| [[SW480 (line)]] | alt | 20.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.46× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Lonafarnib (drug)]] 5 µM 0.107× (z -8.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 2 | — | [[Simotinib (drug)]] 0.05 µM 0.0696× (z -10.8) |
| [[KATO III (line)]] | alt | 18.2 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.06× (z +8.8) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0864× (z -10.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.651× (z -11.4) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 8.97 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.80× (z +8.6) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[A-427 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM65]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[ACTR3B]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PUS1]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[WDR4]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.61 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[RRP9]] | +0.59 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CPNE7]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SLC5A6]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[BRD9]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[SLC25A19]] | +0.58 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[DHX34]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP14]] | -0.67 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[HSPB1]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[SOD1]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[FXR1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ATP6V1A]] | -0.54 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[UBB]] | -0.53 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[FTL]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TXNL1]] | -0.51 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SARAF]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ARL6IP5]] | -0.50 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[CLU]] | -0.50 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[DSTN]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ENTR1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises ENTR1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.1, -30.7); signed map (0.9, -49.7). **Vector** length 76.3, 15.2% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.8 | +14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.5 | +15.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.8 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +4.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.4 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | endosome associated trafficking regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,401,922-136,410,614 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-3; previously SDCCAG3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C92](https://www.uniprot.org/uniprotkb/Q96C92) (Endosome-associated-trafficking regulator 1):

> Endosome-associated protein that plays a role in membrane receptor sorting, cytokinesis and ciliogenesis. Involved in the endosome-to-plasma membrane trafficking and recycling of SNX27-retromer-dependent cargo proteins, such as GLUT1. Involved in the regulation of cytokinesis; the function may involve PTPN13 and GIT1. Plays a role in the formation of cilia. Involved in cargo protein localization, such as PKD2, at primary cilia. Involved in the presentation of the tumor necrosis factor (TNF) …

**Summary**, from NCBI Gene [10807](https://www.ncbi.nlm.nih.gov/gene/10807):

> Involved in several processes, including endocytic recycling; positive regulation of cilium assembly; and positive regulation of protein localization to cilium. Located in several cellular components, including endosome; microtubule organizing center; and retromer complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10667) · Entrez [10807](https://www.ncbi.nlm.nih.gov/gene/10807) · UniProt [Q96C92](https://www.uniprot.org/uniprotkb/Q96C92) · Ensembl [ENSG00000165689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165689)

## Data

Gene col 9169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9169); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9169]; `tensor/DDL_lfc|DDL_z.npy` [9169]; `embed/gene_vectors.npy` [9169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9169 or target_col == 9169). Every well: [[ENTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
