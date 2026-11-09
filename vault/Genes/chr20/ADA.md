---
symbol: "ADA"
type: "gene"
col: 12291
ensembl_id: "ENSG00000196839"
name: "adenosine deaminase"
location: "20q13.12"
module: 77
arm: "+"
pooled_cpm: 14.91
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# ADA

*adenosine deaminase* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +16.8, q 0e+00, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.568× (z -14.3, q 2e-43, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASF3]] (+0.57, fdr 2e-05), [[LPCAT1]] (+0.55, fdr 3e-05), [[TENT4A]] (+0.55, fdr 2e-05); moves opposite to [[LARP7]] (-0.61, fdr 2e-05), [[LINC00174]] (-0.60, fdr 1e-05), [[BCDIN3D]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR155]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +16.8 | 0e+00 | 32/45 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.72×** | +9.7 | 1e-19 | 28/45 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +9.4 | 1e-18 | 27/45 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +9.0 | 3e-17 | 24/46 (BT-474, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.62×** | +8.6 | 9e-16 | 28/45 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +7.4 | 1e-11 | 26/45 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +6.3 | 3e-08 | 20/43 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.6 | 2e-06 | 14/35 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.30×** | +4.5 | 5e-04 | 9/24 (NCI-H2030, MIA PaCa-2, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +4.3 | 1e-03 | 12/46 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.047 | 5/40 (NCI-H23, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.1 | 0.078 | 2/29 (SK-MEL-2, J82) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.19× | +3.0 | 0.10 | 9/44 (LS 180, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.568×** | -14.3 | 2e-43 | 31/45 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -12.1 | 3e-31 | 34/44 (NCI-H23, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -8.5 | 3e-15 | 27/45 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -7.9 | 3e-13 | 24/45 (SW480, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -7.9 | 4e-13 | 29/45 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.643×** | -7.6 | 4e-12 | 22/44 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -7.1 | 8e-11 | 22/45 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -7.0 | 1e-10 | 24/44 (SW480, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.481×** | -6.8 | 6e-10 | 22/46 (NCI-H1792, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -6.4 | 1e-08 | 24/45 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.508×** | -6.3 | 1e-08 | 18/42 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.589×** | -4.9 | 4e-05 | 13/44 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.816×** | -3.6 | 0.012 | 12/45 (RKO, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.867× | -3.6 | 0.013 | 13/46 (SW 900, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 43.7 | 11 (2 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 2.08× (z +15.9) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 6.52× (z +12.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -14.4) |
| [[SW480 (line)]] | alt | 16.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.187× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.294× (z -10.9) |
| [[A498 (line)]] | wt | 35.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.3) | [[Homoharringtonine (drug)]] 0.05 µM 0.441× (z -8.6) |
| [[LoVo (line)]] | wt | 8.36 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -10.6) |
| [[A-172 (line)]] | wt | 8.39 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +16.1) | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.8) |
| [[C32 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 10.5 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.5 µM 0.0534× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 9.12 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.344× (z -9.2) ⚠ cell-cycle shift, explains ~6% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.61 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0772× (z -9.8) |
| [[J82 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 6.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 9.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +14.9) | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.1) |
| [[RKO (line)]] | wt | 16.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.202× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -15.1) |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.3) |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -11.4) |
| [[SW48 (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -10.2) |
| [[A-427 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LPCAT1]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[TENT4A]] | +0.55 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[PRR5-ARHGAP8]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[EVL]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PRR5]] | +0.54 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[EBPL]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ARHGAP44]] | +0.54 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PLEKHA8]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[CDON]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SMG1P2]] | +0.53 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[TPST2]] | +0.53 | +0.46 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | -0.61 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[LINC00174]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[BCDIN3D]] | -0.59 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[STAMBP]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[RC3H2]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[CHMP4A]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[MAPK1IP1L]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[METTL6]] | -0.54 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[CHURC1]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | GPR155 activity raises ADA's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without GPR155 | 0.008 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[ADGRL1]] | B | ADGRL1 activity raises ADA's level | lines that do not express ADGRL1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without ADGRL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3BP5, DSCC1, NDC80; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-2.7, 2.9); signed map (-43.1, 18.8). **Vector** length 81.9, 15.1% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +16.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +9.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.3 | +5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +7.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.7 | +9.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -12.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -8.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -14.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | adenosine deaminase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,584,896-44,652,252 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADA1 |
| Gene groups (HGNC) | Adenosine deaminase family |
| Hallmark sets | DNA_REPAIR, P53_PATHWAY |
| Reactome | 8 pathways, smallest: Nucleotide salvage defects; Diseases of nucleotide metabolism; Ribavirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P00813](https://www.uniprot.org/uniprotkb/P00813) (Adenosine deaminase):

> Catalyzes the hydrolytic deamination of adenosine and 2-deoxyadenosine. Plays an important role in purine metabolism and in adenosine homeostasis. Modulates signaling by extracellular adenosine, and so contributes indirectly to cellular signaling events. Acts as a positive regulator of T-cell coactivation, by binding DPP4. Its interaction with DPP4 regulates lymphocyte-epithelial cell adhesion. Enhances dendritic cell immunogenicity by affecting dendritic cell costimulatory molecule expression …

**Summary**, from NCBI Gene [100](https://www.ncbi.nlm.nih.gov/gene/100):

> This gene encodes an enzyme that catalyzes the hydrolysis of adenosine to inosine in the purine catabolic pathway. Various mutations have been described for this gene and have been linked to human diseases related to impaired immune function such as severe combined immunodeficiency disease (SCID) which is the result of a deficiency in the ADA enzyme. In ADA-deficient individuals there is a marked depletion of T, B, and NK lymphocytes, and consequently, a lack of both humoral and cellular …

**Accessions** — [HGNC:186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:186) · Entrez [100](https://www.ncbi.nlm.nih.gov/gene/100) · UniProt [P00813](https://www.uniprot.org/uniprotkb/P00813) · Ensembl [ENSG00000196839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196839)

## Data

Gene col 12291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12291); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12291]; `tensor/DDL_lfc|DDL_z.npy` [12291]; `embed/gene_vectors.npy` [12291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12291 or target_col == 12291). Every well: [[ADA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
