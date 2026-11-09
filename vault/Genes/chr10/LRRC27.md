---
symbol: "LRRC27"
type: "gene"
col: 7315
ensembl_id: "ENSG00000148814"
name: "leucine rich repeat containing 27"
location: "10q26.3"
module: 130
arm: "+"
pooled_cpm: 9.51
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 12
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# LRRC27

*leucine rich repeat containing 27* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.43× (z +4.8, q 4e-04, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.383× (z -13.5, q 1e-38, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSCP1]] (+0.64, fdr 7e-06), [[DNAJC27]] (+0.63, fdr 7e-06), [[YY1AP1]] (+0.60, fdr 3e-05); moves opposite to [[TIAM1]] (-0.60, fdr 1e-05), [[ACOT7]] (-0.60, fdr 7e-06), [[MED12L]] (-0.59, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +4.8 | 4e-04 | 16/45 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 4e-04 | 11/46 (A-427, LS 180, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 4e-04 | 16/47 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +4.4 | 0.001 | 13/45 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.002 | 9/47 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.002 | 15/47 (KATO III, A-427, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.003 | 11/45 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +3.9 | 0.006 | 10/47 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.008 | 12/47 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.012 | 9/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.012 | 11/47 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.020 | 6/44 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.043 | 5/46 (A-427, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7315.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.383×** | -13.5 | 1e-38 | 37/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.407×** | -12.6 | 4e-34 | 32/44 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.442×** | -11.5 | 3e-28 | 33/45 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.459×** | -10.5 | 9e-24 | 24/40 (HCT15, C-33 A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.486×** | -10.1 | 4e-22 | 29/46 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -10.0 | 1e-21 | 30/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.348×** | -7.8 | 7e-13 | 29/46 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.399×** | -6.8 | 1e-09 | 23/42 (SNU-423, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -6.6 | 3e-09 | 25/46 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.626×** | -6.2 | 3e-08 | 21/45 (SNU-423, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -6.2 | 3e-08 | 18/46 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.647×** | -5.9 | 2e-07 | 10/15 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -5.8 | 3e-07 | 21/47 (C-33 A, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.664×** | -5.7 | 4e-07 | 20/45 (SNU-1, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.777×** | -5.0 | 2e-05 | 22/46 (SNU-423, SK-MEL-2, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.716×** | -4.5 | 2e-04 | 15/45 (HT-29, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.728×** | -4.5 | 2e-04 | 20/44 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -4.1 | 9e-04 | 16/45 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.747×** | -4.1 | 1e-03 | 11/46 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.818×** | -4.0 | 0.001 | 14/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -12.7) |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -9.6) |
| [[HOP62 (line)]] | alt | 6.42 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0762× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -11.6) |
| [[PANC-1 (line)]] | alt | 18.2 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -10.0) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 9.72 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0721× (z -9.0) |
| [[SW480 (line)]] | alt | 6.13 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -8.8) |
| [[A498 (line)]] | wt | 5.43 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0896× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.169× (z -9.6) ⚠ toxic |
| [[H4 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0640× (z -9.4) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0739× (z -10.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[J82 (line)]] | alt | 5.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.133× (z -9.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H1792 (line)]] | alt | 8.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0921× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 6.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -8.5) ⚠ cell-cycle shift, explains ~91% of this change |
| [[A-172 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSCP1]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC27]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[YY1AP1]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[THAP8]] | +0.59 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SPACA9]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LINC02256]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[YJU2B]] | +0.57 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CFAP43]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[MORN2]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PARP16]] | +0.57 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CCDC191]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DRC3]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIAM1]] | -0.60 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[ACOT7]] | -0.60 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[MED12L]] | -0.59 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[GALNT10]] | -0.57 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[RAPGEF5]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.55 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MTAP]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[FABP5]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[MAN2A1]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ACTN1]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[OSBPL10]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[FARP1]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers LRRC27's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[GFOD1]] | B | GFOD1 activity lowers LRRC27's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without GFOD1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers LRRC27's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[RAPGEF5]] | B | RAPGEF5 activity lowers LRRC27's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.46× higher at baseline in the lines without RAPGEF5 | 0.082 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[MAGEA1]] | B | MAGEA1 activity strengthens LRRC27's drug response | lines that do not express MAGEA1 (36) vs lines expressing it (11) | the lines without MAGEA1 respond 0.64× as strongly (z diff +1.52); strongest at Niclosamide (olamine) 5 µM: 0.50x vs 0.26x (z diff +3.5) | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01242, LINC02484, MIR548XHG; target measured in part of the lines; artifact flags |
| [[DAB2IP]] | C | DAB2IP activity weakens LRRC27's drug response | lines that do not express DAB2IP (4) vs lines expressing it (43) | the lines without DAB2IP respond 2.20× as strongly (z diff -2.91); strongest at Ouabain (Octahydrate) 5 µM: 0.18x vs 0.39x (z diff -4.6) | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DAB2IP]] | C | DAB2IP activity lowers LRRC27's level | lines that do not express DAB2IP (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without DAB2IP | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22; maybe low, not absent |
| [[CLIP3]] | C | CLIP3 activity raises LRRC27's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |
| [[ZNF449]] | C | ZNF449's natural level strengthens LRRC27's drug response | ZNF449's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.15; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.0, -29.0); signed map (-8.1, -0.3). **Vector** length 61.2, 9.64% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +1.8 | +3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.5 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.5 | -2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -4.2 | -5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:132,332,154-132,381,508 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1674 |
| Matched by | ensembl_id |

UniProt [Q9C0I9](https://www.uniprot.org/uniprotkb/Q9C0I9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29346) · Entrez [80313](https://www.ncbi.nlm.nih.gov/gene/80313) · UniProt [Q9C0I9](https://www.uniprot.org/uniprotkb/Q9C0I9) · Ensembl [ENSG00000148814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148814)

## Data

Gene col 7315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7315); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7315]; `tensor/DDL_lfc|DDL_z.npy` [7315]; `embed/gene_vectors.npy` [7315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7315 or target_col == 7315). Every well: [[LRRC27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
