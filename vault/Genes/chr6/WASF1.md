---
symbol: "WASF1"
type: "gene"
col: 3347
ensembl_id: "ENSG00000112290"
name: "WASP family member 1"
location: "6q21"
module: 30
arm: "+"
pooled_cpm: 52.2
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# WASF1

*WASP family member 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +8.0, q 5e-13, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.642× (z -8.9, q 3e-16, down in 31 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.761× (z -5.5, q 4e-06, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF125]] (+0.49, fdr 4e-05), [[C8orf88]] (+0.48, fdr 5e-05), [[FYN]] (+0.47, fdr 3e-05); moves opposite to [[PPP6R2]] (-0.46, fdr 1e-04), [[CHTOP]] (-0.43, fdr 4e-05), [[MTOR]] (-0.42, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +8.0 | 5e-13 | 31/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.9 | 1e-09 | 27/47 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.4 | 4e-08 | 23/47 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +6.0 | 3e-07 | 25/47 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +5.8 | 9e-07 | 27/47 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.6 | 3e-04 | 24/46 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.005 | 14/47 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.005 | 20/47 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +3.9 | 0.006 | 15/47 (LoVo, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.028 | 9/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.039 | 12/47 (LS 180, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.3 | 0.039 | 9/47 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.3 | 0.040 | 8/47 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.17× | +3.2 | 0.049 | 9/47 (HOP62, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3347.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.642×** | -8.9 | 3e-16 | 31/46 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.675×** | -6.6 | 1e-08 | 27/44 (LS 180, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.730×** | -6.1 | 2e-07 | 23/40 (HCT15, SNU-423, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.751×** | -5.8 | 1e-06 | 25/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.761×** | -5.5 | 4e-06 | 25/47 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.765×** | -5.4 | 7e-06 | 23/47 (SNU-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.628×** | -4.9 | 8e-05 | 22/48 (LOX-IMVI, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.810×** | -4.2 | 0.002 | 18/47 (C32, HEC-1-A, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **0.812×** | -4.2 | 0.002 | 22/46 (H4, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.813×** | -4.0 | 0.004 | 21/46 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.706×** | -3.7 | 0.013 | 16/47 (SNU-423, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.842× | -3.4 | 0.027 | 19/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.844× | -3.4 | 0.029 | 22/46 (SW 900, H4, …) | all doses, flat | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.719×** | -3.4 | 0.032 | 12/47 (A549, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.849× | -3.3 | 0.039 | 18/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -3.2 | 0.043 | 14/47 (PANC-1, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 76.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LS 180 (line)]] | wt | 46.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0654× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.445× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 106 | 0 | 3 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.211× (z -9.5) ⚠ toxic · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.458× (z -9.2) |
| [[SNU-423 (line)]] | alt | 131 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 67.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 38.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.413× (z -9.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SNU-1 (line)]] | wt | 55.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.220× (z -10.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 38.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 35.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.17× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 59.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 83.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 92.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF125]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[C8orf88]] | +0.48 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[FYN]] | +0.47 | +0.44 / +0.57 | both halves | 3e-05 | pathway: FCGR3A-mediated phagocytosis |
| [[CACNB3]] | +0.44 | +0.37 / +0.33 | both halves | 1e-04 |  |
| [[DCAF6]] | +0.44 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[STARD9]] | +0.42 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[SGTB]] | +0.42 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[DDHD2]] | +0.42 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[SERPINI1]] | +0.42 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[SLC39A6]] | +0.42 | +0.39 / +0.36 | both halves | 1e-04 |  |
| [[NTAN1]] | +0.42 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[ATF2]] | +0.41 | +0.41 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP6R2]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CHTOP]] | -0.43 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MTOR]] | -0.42 | -0.32 / -0.45 | both halves | 1e-04 | pathway: Signaling by VEGF |
| [[MARK2]] | -0.41 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[ATG7]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[MPPE1]] | -0.39 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[RAD54L2]] | -0.39 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[MCRS1]] | -0.38 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[SFSWAP]] | -0.38 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[ERCC4]] | -0.38 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[DOLPP1]] | -0.38 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[VPS45]] | -0.37 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises WASF1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.56× lower at baseline in the lines without STARD9 | 0.044 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SDK1]] | B | SDK1 activity weakens WASF1's drug response | lines that do not express SDK1 (21) vs lines expressing it (26) | the lines without SDK1 respond 1.33× as strongly (z diff -0.81); strongest at Belinostat 5 µM: 1.60x vs 1.14x (z diff -2.5) | 0.046 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; target measured in part of the lines; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers WASF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers WASF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SDK1]] | B | SDK1 activity raises WASF1's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without SDK1 | 0.096 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[LINC00662]] | C | LINC00662 activity raises WASF1's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without LINC00662 | 0.098 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.150). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-48.1, 6.0); signed map (-27.6, 27.8). **Vector** length 79.0, 15.9% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.0 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | +1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -2.8 | -8.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | WASP family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:110,099,819-110,180,004 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WAVE1, SCAR1, KIAA0269, WAVE, WAVE-1 |
| Gene groups (HGNC) | Wiskott-Aldrich Syndrome protein family; A-kinase anchoring proteins; SCAR/WAVE complex |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 18 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92558](https://www.uniprot.org/uniprotkb/Q92558) (Actin-binding protein WASF1):

> Downstream effector molecule involved in the transmission of signals from tyrosine kinase receptors and small GTPases to the actin cytoskeleton. Promotes formation of actin filaments. Part of the WAVE complex that regulates lamellipodia formation. The WAVE complex regulates actin filament reorganization via its interaction with the Arp2/3 complex (By similarity). As component of the WAVE1 complex, required for BDNF-NTRK2 endocytic trafficking and signaling from early endosomes (By similarity). …

**Summary**, from NCBI Gene [8936](https://www.ncbi.nlm.nih.gov/gene/8936):

> The protein encoded by this gene, a member of the Wiskott-Aldrich syndrome protein (WASP)-family, plays a critical role downstream of Rac, a Rho-family small GTPase, in regulating the actin cytoskeleton required for membrane ruffling. It has been shown to associate with an actin nucleation core Arp2/3 complex while enhancing actin polymerization in vitro. Wiskott-Aldrich syndrome is a disease of the immune system, likely due to defects in regulation of actin cytoskeleton. Multiple alternatively …

**Accessions** — [HGNC:12732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12732) · Entrez [8936](https://www.ncbi.nlm.nih.gov/gene/8936) · UniProt [Q92558](https://www.uniprot.org/uniprotkb/Q92558) · Ensembl [ENSG00000112290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112290)

## Data

Gene col 3347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3347); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3347]; `tensor/DDL_lfc|DDL_z.npy` [3347]; `embed/gene_vectors.npy` [3347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3347 or target_col == 3347). Every well: [[WASF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
