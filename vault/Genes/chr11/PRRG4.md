---
symbol: "PRRG4"
type: "gene"
col: 5694
ensembl_id: "ENSG00000135378"
name: "proline rich and Gla domain 4"
location: "11p13"
module: 8
arm: "+"
pooled_cpm: 17.22
n_lines_expressing: 34
n_dd_up: 41
n_dd_down: 5
n_dd_up_clean: 33
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 18
direction_downstream: 17
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PRRG4

*proline rich and Gla domain 4* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.99× (z +12.6, q 2e-33, up in 22 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.477× (z -9.6, q 6e-19, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf52]] (+0.64, fdr 1e-05), [[BTG3]] (+0.64, fdr 3e-05), [[CASP7]] (+0.62, fdr 1e-05); moves opposite to [[APEH]] (-0.57, fdr 4e-05), [[GNB1L]] (-0.56, fdr 6e-05), [[SLX4]] (-0.55, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[LINC02967]] → it (grade B ⚠); 17 go from it, the strongest it → [[LITAF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.99×** | +12.6 | 2e-33 | 22/32 (J82, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.83×** | +7.8 | 1e-12 | 23/32 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.80×** | +7.6 | 5e-12 | 21/29 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +7.5 | 6e-12 | 15/31 (SW48, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +7.5 | 6e-12 | 16/25 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +7.5 | 6e-12 | 18/29 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +7.4 | 2e-11 | 20/31 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +7.3 | 2e-11 | 17/31 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.76×** | +7.3 | 2e-11 | 22/31 (A498, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.0 | 2e-10 | 12/29 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +6.3 | 2e-08 | 15/30 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +5.0 | 2e-05 | 11/27 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.30×** | +4.9 | 5e-05 | 13/32 (NCI-H2347, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +4.8 | 7e-05 | 14/32 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.7 | 9e-05 | 18/30 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 1e-04 | 13/31 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 16/32 (AsPC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.477×** | -9.6 | 6e-19 | 21/31 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -8.5 | 7e-15 | 24/31 (Panc 03.27, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.528×** | -8.3 | 2e-14 | 22/31 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -4.9 | 1e-04 | 19/32 (Panc 03.27, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.503×** | -4.7 | 4e-04 | 16/30 (SW1417, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.633× | -3.1 | 0.18 | 5/32 (NCI-H1573, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.790× | -3.1 | 0.18 | 12/29 (RKO, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 35.6 | 6 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.13× (z +13.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0836× (z -16.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 60.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -14.0) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.187× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 88.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -16.4) |
| [[J82 (line)]] | alt | 22.7 | 2 | 1 | [[Selinexor (drug)]] 5 µM 2.75× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 72.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -13.6) |
| [[A-172 (line)]] | wt | 9.63 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.157× (z -9.0) |
| [[C32 (line)]] | wt | 6.10 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0677× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -9.1) |
| [[HCT15 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0972× (z -14.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -8.6) |
| [[SW480 (line)]] | alt | 11.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -10.1) |
| [[A-427 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf52]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[BTG3]] | +0.64 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[CASP7]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SPINK1]] | +0.61 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[MARVELD3]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RHBDL2]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CASP10]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[MR1]] | +0.59 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PDZK1IP1]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[BTN2A1]] | +0.59 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[TRIM31]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[APOL2]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APEH]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GNB1L]] | -0.56 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[SLX4]] | -0.55 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ARHGAP4]] | -0.52 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[NT5E]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RSU1]] | -0.50 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[NOMO1]] | -0.50 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[BLTP2]] | -0.50 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[TRAP1]] | -0.50 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[FLNB]] | -0.49 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[ATAD3A]] | -0.49 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[SCFD2]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 14, C 4. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02967]] | B | LINC02967 activity raises PRRG4's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 5.65× lower at baseline in the lines without LINC02967 | 8e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[LCN2]] | B | LCN2 activity raises PRRG4's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 4.75× lower at baseline in the lines without LCN2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises PRRG4's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 3.78× lower at baseline in the lines without PDZK1IP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[DAPP1]] | B | DAPP1 activity raises PRRG4's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.60× lower at baseline in the lines without DAPP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[VNN1]] | B | VNN1 activity raises PRRG4's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 1.99× lower at baseline in the lines without VNN1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[WFDC2]] | B | WFDC2 activity raises PRRG4's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.23× lower at baseline in the lines without WFDC2 | 0.008 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[TOP2A]] | B | TOP2A activity lowers PRRG4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MMP7]] | B | MMP7 activity raises PRRG4's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.82× lower at baseline in the lines without MMP7 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[C11orf52]] | B | C11orf52 activity raises PRRG4's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 3.00× lower at baseline in the lines without C11orf52 | 0.028 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[SULT1C2]] | B | SULT1C2 activity raises PRRG4's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without SULT1C2 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[ADGRF4]] | B | ADGRF4 activity raises PRRG4's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.35× lower at baseline in the lines without ADGRF4 | 0.055 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[RHBDL2]] | B | RHBDL2 activity raises PRRG4's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without RHBDL2 | 0.058 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 13, C 4. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LITAF]] | B | PRRG4 activity raises LITAF's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without PRRG4 | 0.042 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[SLC37A1]] | B | PRRG4 activity raises SLC37A1's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without PRRG4 | 0.043 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[LCN2]] | B | PRRG4 activity raises LCN2's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 3.50× lower at baseline in the lines without PRRG4 | 0.044 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[HNF4G]] | B | PRRG4 activity raises HNF4G's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 3.53× lower at baseline in the lines without PRRG4 | 0.049 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[LYN]] | B | PRRG4 activity raises LYN's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without PRRG4 | 0.056 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[C11orf52]] | B | PRRG4 activity raises C11orf52's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without PRRG4 | 0.067 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[CCDC73]] | B | PRRG4 activity raises CCDC73's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without PRRG4 | 0.074 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[PDZK1IP1]] | B | PRRG4 activity raises PDZK1IP1's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without PRRG4 | 0.080 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[DAPP1]] | B | PRRG4 activity raises DAPP1's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without PRRG4 | 0.081 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | PRRG4 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express PRRG4 (16) vs lines expressing it (32) | the lines without PRRG4: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[STAP2]] | B | PRRG4 activity raises STAP2's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without PRRG4 | 0.084 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[RASGEF1B]] | B | PRRG4 activity raises RASGEF1B's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without PRRG4 | 0.095 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.3, 52.7); signed map (54.6, 0.1). **Vector** length 90.6, 24.5% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.1 | +12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +3.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -4.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | proline rich and Gla domain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:32,829,927-32,858,120 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMG4 |
| Gene groups (HGNC) | Proline rich and Gla domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZD6](https://www.uniprot.org/uniprotkb/Q9BZD6) (Transmembrane gamma-carboxyglutamic acid protein 4):

> May control axon guidance across the CNS. Prevents the delivery of ROBO1 at the cell surface and down-regulates its expression.

**Summary**, from NCBI Gene [79056](https://www.ncbi.nlm.nih.gov/gene/79056):

> Enables WW domain binding activity. Predicted to be involved in blood coagulation and proteolysis. Located in plasma membrane. Biomarker of cholangiocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30799) · Entrez [79056](https://www.ncbi.nlm.nih.gov/gene/79056) · UniProt [Q9BZD6](https://www.uniprot.org/uniprotkb/Q9BZD6) · Ensembl [ENSG00000135378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135378)

## Data

Gene col 5694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5694); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5694]; `tensor/DDL_lfc|DDL_z.npy` [5694]; `embed/gene_vectors.npy` [5694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5694 or target_col == 5694). Every well: [[PRRG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
