---
symbol: "MAK16"
type: "gene"
col: 12518
ensembl_id: "ENSG00000198042"
name: "MAK16 homolog"
location: "8p12"
module: 1
arm: "+"
pooled_cpm: 20.79
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 12
n_dd_up_clean: 31
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MAK16

*MAK16 homolog* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.42× (z +13.1, q 2e-36, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.661× (z -5.9, q 2e-06, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BYSL]] (+0.84, fdr 7e-06), [[LTV1]] (+0.80, fdr 7e-06), [[UTP14A]] (+0.80, fdr 7e-06); moves opposite to [[MPC2]] (-0.68, fdr 7e-06), [[TESK2]] (-0.68, fdr 1e-05), [[NARF]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +13.1 | 2e-36 | 40/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +11.6 | 9e-29 | 36/47 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.15×** | +10.9 | 3e-25 | 40/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.07×** | +10.8 | 5e-25 | 35/44 (NCI-H1792, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.08×** | +10.4 | 3e-23 | 23/32 (A549, HepG2/C3A, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.98×** | +10.1 | 5e-22 | 43/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.07×** | +10.0 | 2e-21 | 30/41 (A-172, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +9.9 | 5e-21 | 40/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.50×** | +9.7 | 2e-20 | 41/47 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.15×** | +8.9 | 4e-17 | 35/45 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +8.5 | 1e-15 | 35/45 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +8.0 | 7e-14 | 36/47 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +7.2 | 2e-11 | 31/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.7 | 7e-10 | 28/48 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.60×** | +6.7 | 7e-10 | 31/46 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +6.5 | 3e-09 | 31/46 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.23×** | +6.2 | 2e-08 | 32/45 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.21×** | +6.1 | 3e-08 | 27/46 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.19×** | +6.1 | 4e-08 | 28/46 (A498, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.06×** | +5.6 | 6e-07 | 27/47 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.661×** | -5.9 | 2e-06 | 25/46 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.703×** | -5.7 | 4e-06 | 27/48 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.766×** | -5.4 | 1e-05 | 25/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.736×** | -4.4 | 0.002 | 18/46 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.792×** | -4.2 | 0.003 | 21/47 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.769×** | -4.1 | 0.003 | 16/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.787×** | -4.0 | 0.004 | 20/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.764×** | -4.0 | 0.004 | 18/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.764×** | -4.0 | 0.004 | 17/46 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.776×** | -3.5 | 0.030 | 14/47 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.796×** | -3.4 | 0.037 | 15/46 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.792×** | -3.2 | 0.067 | 10/47 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.809× | -3.0 | 0.11 | 16/46 (LoVo, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 39.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0634× (z -20.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 10.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.11× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.52× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 8.70 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.93× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 7.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +9.9) | — |
| [[A549 (line)]] | wt | 19.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.5) | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.117× (z -9.5) |
| [[HOP62 (line)]] | alt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.84× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.41× (z +8.6) | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.359× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.499× (z -17.3) ⚠ position not correctable |
| [[RKO (line)]] | wt | 54.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 7.19 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0841× (z -9.4) |
| [[SW48 (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 30.6 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.58× (z +8.8) | — |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BYSL]] | +0.84 | +0.84 / +0.85 | both halves | 7e-06 | STRING 938 |
| [[LTV1]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | STRING 949 |
| [[UTP14A]] | +0.80 | +0.83 / +0.78 | both halves | 7e-06 | STRING 823 |
| [[RRP15]] | +0.79 | +0.75 / +0.83 | both halves | 7e-06 | STRING 972 |
| [[GPATCH4]] | +0.79 | +0.78 / +0.81 | both halves | 7e-06 | STRING 863 |
| [[RRS1]] | +0.79 | +0.84 / +0.74 | both halves | 7e-06 | STRING 957 |
| [[ZNF202]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[UTP15]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | STRING 586 |
| [[PNO1]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | STRING 705 |
| [[RBM28]] | +0.77 | +0.79 / +0.80 | both halves | 7e-06 | same gene group; STRING 941 |
| [[ZNF121]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[DDX31]] | +0.77 | +0.78 / +0.75 | both halves | 7e-06 | STRING 569 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.68 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[TESK2]] | -0.68 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[NARF]] | -0.67 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[SAP30-DT]] | -0.66 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.66 | -0.72 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MAK16's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises MAK16's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[NCR3LG1]] | B | NCR3LG1 activity raises MAK16's level | lines that do not express NCR3LG1 (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without NCR3LG1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000260196; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.887). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.1, -36.5); signed map (-0.7, -43.9). **Vector** length 107, 28.8% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.62 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.64 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.65 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +13.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.1 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +8.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +6.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.5 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | MAK16 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:33,485,182-33,501,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAK16L; previously RBM13 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q9BXY0](https://www.uniprot.org/uniprotkb/Q9BXY0) carries no function annotation.

**Summary**, from NCBI Gene [84549](https://www.ncbi.nlm.nih.gov/gene/84549):

> Enables RNA binding activity. Predicted to be involved in maturation of 5.8S rRNA and maturation of LSU-rRNA. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13703) · Entrez [84549](https://www.ncbi.nlm.nih.gov/gene/84549) · UniProt [Q9BXY0](https://www.uniprot.org/uniprotkb/Q9BXY0) · Ensembl [ENSG00000198042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198042)

## Data

Gene col 12518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12518); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12518]; `tensor/DDL_lfc|DDL_z.npy` [12518]; `embed/gene_vectors.npy` [12518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12518 or target_col == 12518). Every well: [[MAK16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAK16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
