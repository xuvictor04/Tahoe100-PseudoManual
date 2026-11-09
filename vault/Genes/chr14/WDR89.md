---
symbol: "WDR89"
type: "gene"
col: 6365
ensembl_id: "ENSG00000140006"
name: "WD repeat domain 89"
location: "14q23.2"
module: 170
arm: "+"
pooled_cpm: 20.85
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# WDR89

*WD repeat domain 89* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.79× (z +12.2, q 2e-31, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.572× (z -11.2, q 2e-26, down in 21 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.763× (z -5.7, q 2e-06, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP3]] (+0.66, fdr 7e-06), [[HDHD5]] (+0.64, fdr 1e-05), [[DET1]] (+0.60, fdr 1e-05); moves opposite to [[NID1]] (-0.52, fdr 3e-05), [[UBE2A]] (-0.50, fdr 2e-04), [[MC1R]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +12.2 | 2e-31 | 35/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +11.9 | 2e-30 | 34/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +11.5 | 2e-28 | 41/48 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.79×** | +11.2 | 8e-27 | 36/46 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +10.6 | 5e-24 | 29/48 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +7.7 | 2e-12 | 26/45 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +7.7 | 2e-12 | 27/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.2 | 5e-11 | 22/47 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.1 | 7e-11 | 23/48 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +6.2 | 4e-08 | 19/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 5e-07 | 16/47 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.9 | 6e-05 | 19/48 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.7 | 1e-04 | 8/48 (NCI-H2347, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 12/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 9/47 (C-33 A, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.004 | 8/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.043 | 8/48 (NCI-H460, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -11.2 | 2e-26 | 21/31 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -10.7 | 4e-24 | 28/43 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.689×** | -7.2 | 1e-10 | 22/38 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -5.7 | 2e-06 | 21/47 (SW48, PANC-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.784×** | -5.1 | 4e-05 | 18/47 (C32, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.6 | 4e-04 | 3/48 (SW 1271, CHP-212, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.816×** | -4.2 | 0.002 | 16/47 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.811×** | -4.2 | 0.002 | 17/46 (PANC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.821×** | -4.1 | 0.003 | 15/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.815×** | -4.0 | 0.003 | 14/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.037 | 10/47 (A549, BT-474, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.893× | -3.4 | 0.038 | 8/48 (H4, SW1417, …) | all doses, stronger at high dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.072 | 6/48 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.753×** | -3.1 | 0.079 | 12/40 (J82, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 0.865× | -3.0 | 0.090 | 8/48 (LS 180, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.816×** | -3.0 | 0.090 | 7/48 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 67.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.73× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 28.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 17.9 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0850× (z -13.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -15.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 8.66 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.240× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A549 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -13.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 20.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.108× (z -10.0) |
| [[HCT15 (line)]] | alt | 28.5 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.119× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP3]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[HDHD5]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[DET1]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[NARS2]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.57 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PEX7]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[FASTKD3]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TUT1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PMS2CL]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[FBXO45]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NID1]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[UBE2A]] | -0.50 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[MC1R]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DVL3]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PEPD]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[IGF2R]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LIMS1]] | -0.46 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[RNF32-AS1]] | -0.45 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[UBR4]] | -0.45 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity lowers WDR89's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.72× higher at baseline in the lines without RAB20 | 0.013 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[RAB20]] | B | RAB20 activity weakens WDR89's drug response | lines that do not express RAB20 (8) vs lines expressing it (40) | the lines without RAB20 respond 1.05× as strongly (z diff -0.34); rises at some drug-doses, falls at others (56% from rises): Dinaciclib 0.5 µM: 0.28x vs 0.60x (z diff -4.5); Dinaciclib 0.05 µM: 0.50x vs 0.70x (z diff -2.7); TAK-901 5 µM: 3.89x vs 3.06x (z diff -1.5) | 0.065 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises WDR89's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.322). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-49.2, 7.0); signed map (-12.7, -15.9). **Vector** length 84.1, 16.1% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +11.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.0 | +7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -5.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 89 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:63,597,039-63,641,871 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9907; previously C14orf150 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q96FK6](https://www.uniprot.org/uniprotkb/Q96FK6) carries no function annotation.

**Summary**, from NCBI Gene [112840](https://www.ncbi.nlm.nih.gov/gene/112840):

> Predicted to act upstream of or within corpus callosum development and ventricular system development. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20489) · Entrez [112840](https://www.ncbi.nlm.nih.gov/gene/112840) · UniProt [Q96FK6](https://www.uniprot.org/uniprotkb/Q96FK6) · Ensembl [ENSG00000140006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140006)

## Data

Gene col 6365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6365); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6365]; `tensor/DDL_lfc|DDL_z.npy` [6365]; `embed/gene_vectors.npy` [6365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6365 or target_col == 6365). Every well: [[WDR89 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR89.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
