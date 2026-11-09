---
symbol: "AKR1C1"
type: "gene"
col: 11892
ensembl_id: "ENSG00000187134"
name: "aldo-keto reductase family 1 member C1"
location: "10p15.1"
module: 117
arm: "+"
pooled_cpm: 48.72
n_lines_expressing: 25
n_dd_up: 38
n_dd_down: 3
n_dd_up_clean: 29
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# AKR1C1

*aldo-keto reductase family 1 member C1* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.57× (z +12.7, q 2e-34, up in 14 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.45× (z +9.0, q 9e-17, up in 18 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.514× (z -9.5, q 2e-18, down in 19 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1C2]] (+0.81, fdr 7e-06, ⚠ same locus), [[AKR1C3]] (+0.73, fdr 7e-06), [[PIR]] (+0.68, fdr 7e-06), [[MGST1]] (+0.66, fdr 7e-06); moves opposite to [[FAM110A]] (-0.54, fdr 2e-05), [[RIN1]] (-0.52, fdr 2e-05), [[TMEM158]] (-0.52, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MGST1]] → it (grade B ⚠); 13 go from it, the strongest it → [[PGD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +12.7 | 2e-34 | 14/22 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +9.0 | 9e-17 | 18/22 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +8.5 | 4e-15 | 12/20 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.28×** | +7.8 | 8e-13 | 19/23 (HT-29, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.6 | 4e-12 | 12/20 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.69×** | +6.8 | 8e-10 | 13/19 (CFPAC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +6.4 | 1e-08 | 15/22 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.0 | 2e-07 | 14/22 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.73×** | +5.9 | 3e-07 | 17/23 (A549, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.71×** | +5.6 | 1e-06 | 20/24 (A549, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.78×** | +5.5 | 2e-06 | 17/22 (A549, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.72×** | +5.4 | 2e-06 | 17/23 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.73×** | +5.3 | 6e-06 | 18/22 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 11/23 (AN3 CA, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +5.0 | 2e-05 | 18/22 (A549, HS-578T, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **2.61×** | +5.0 | 2e-05 | 12/21 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 9e-05 | 16/23 (NCI-H460, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.40×** | +4.6 | 1e-04 | 12/24 (NCI-H460, A549, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 1e-04 | 9/24 (AN3 CA, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.57×** | +4.5 | 2e-04 | 15/22 (HS-578T, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -9.5 | 2e-18 | 19/23 (SHP-77, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -5.0 | 1e-04 | 21/23 (SHP-77, AN3 CA, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.020 | 11/23 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.725× | -3.0 | 0.33 | 7/23 (A498, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 123 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 8.01× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.202× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 140 | 4 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 11.5× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.8) |
| [[HT-29 (line)]] | alt | 29.5 | 4 | 1 | [[Bortezomib (drug)]] 0.05 µM 8.81× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.95× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 97.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.57× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 134 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -17.4) |
| [[AsPC-1 (line)]] | alt | 23.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 35.8× (z +15.7) | — |
| [[LS 180 (line)]] | wt | 14.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 21.3× (z +14.0) | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 446 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 7.30× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 194 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.5) |
| [[A-172 (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.69 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.72 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1C2]] | +0.81 | +0.83 / +0.81 | both halves | 7e-06 | same gene group; pathway: Bile acid and bile salt metabolism; STRING 998; ⚠ same locus (4.5 kb: neighbours can correlate without regulation) |
| [[AKR1C3]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 | same gene group; pathway: Bile acid and bile salt metabolism; STRING 995 |
| [[PIR]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MGST1]] | +0.66 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[GSR]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.64 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Drug ADME |
| [[EID3]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[TXNRD1]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 | STRING 581 |
| [[NMRAL2P-1]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[NMRAL2P]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[VEGFD]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[CYP4F3]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[GCLC]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 | STRING 743 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM110A]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RIN1]] | -0.52 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TMEM158]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PRDM8]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ANTXR2]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SPRED1]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ARHGAP1]] | -0.46 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[COL13A1]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ADAM8]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ICAM3]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[NT5E]] | -0.46 | -0.49 / -0.34 | both halves | 1e-04 | pathway: Metabolism of vitamins and cofactors |
| [[MYEOV]] | -0.45 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGST1]] | B | MGST1 activity raises AKR1C1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 3.39× lower at baseline in the lines without MGST1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[NMRAL2P]] | B | NMRAL2P activity raises AKR1C1's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.87× lower at baseline in the lines without NMRAL2P | 0.050 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[LINC01564]] | B | LINC01564 activity raises AKR1C1's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 2.79× lower at baseline in the lines without LINC01564 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[LURAP1L]] | B | LURAP1L activity raises AKR1C1's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 3.23× lower at baseline in the lines without LURAP1L | 0.079 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises AKR1C1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without NMRAL2P-1 | 0.090 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[AKR1C2]] | C | AKR1C2 activity raises AKR1C1's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 8.05× lower at baseline in the lines without AKR1C2 | 1e-04 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[AKR1C3]] | C | AKR1C3 activity raises AKR1C1's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 4.77× lower at baseline in the lines without AKR1C3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises AKR1C1's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.29× lower at baseline in the lines without CYP4F11 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGD]] | B | AKR1C1 activity raises PGD's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without AKR1C1 | 0.006 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[LARP4]] | B | AKR1C1 activity lowers LARP4's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.39× higher at baseline in the lines without AKR1C1 | 0.009 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[NMRAL2P]] | B | AKR1C1 activity raises NMRAL2P's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without AKR1C1 | 0.012 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[UBE2K]] | B | AKR1C1 activity lowers UBE2K's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.21× higher at baseline in the lines without AKR1C1 | 0.020 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[NMRAL2P-1]] | B | AKR1C1 activity raises NMRAL2P-1's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without AKR1C1 | 0.026 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[LINC01564]] | B | AKR1C1 activity raises LINC01564's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without AKR1C1 | 0.030 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[RSRC1]] | B | AKR1C1 activity lowers RSRC1's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.35× higher at baseline in the lines without AKR1C1 | 0.032 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[ZSCAN31]] | B | AKR1C1 activity raises ZSCAN31's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without AKR1C1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[GCLC]] | B | AKR1C1 activity raises GCLC's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without AKR1C1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[AKR1C3]] | C | AKR1C1 activity raises AKR1C3's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 4.44× lower at baseline in the lines without AKR1C1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU; co-absent with the target |
| [[AKR1C2]] | C | AKR1C1 activity raises AKR1C2's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 4.90× lower at baseline in the lines without AKR1C1 | 0.001 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU; co-absent with the target |
| [[AKR1B10]] | C | AKR1C1 activity raises AKR1B10's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without AKR1C1 | 0.018 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.4, 48.0); signed map (51.9, -9.8). **Vector** length 82.2, 23.4% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.55 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.55 to 7); *NFE2L2 regulating anti-oxidant/detoxification enzymes* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +7.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.1 | -9.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.2 | -3.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 1 member C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:4,963,253-4,983,283 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DDH, MBAB, DD1, HAKRC; previously DDH1 |
| Gene groups (HGNC) | Aldo-keto reductases |
| Reactome | 14 pathways, smallest: Prednisone ADME; Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Synthesis of bile acids and bile salts via 24-hydroxycholesterol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04828](https://www.uniprot.org/uniprotkb/Q04828) (Aldo-keto reductase family 1 member C1):

> Cytosolic aldo-keto reductase that catalyzes NADPH-dependent reduction of ketosteroids to hydroxysteroids. Displays broad substrate specificity with distinct positional and stereochemistry, primarily generating 20alpha-hydroxysteroids, but also 3alpha/beta- and 17beta-hydroxysteroids. Involved in neurosteroid metabolism. Reduces 5alpha-dihydrodeoxycorticosterone (5-alpha-DHDOC) to neuroactive steroid 3alpha,5alpha-tetrahydrodeoxycorticosterone (3alpha,5alpha-THDOC) known to alter neural …

**Summary**, from NCBI Gene [1645](https://www.ncbi.nlm.nih.gov/gene/1645):

> This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. These enzymes catalyze the conversion of aldehydes and ketones to their corresponding alcohols by utilizing NADH and/or NADPH as cofactors. The enzymes display overlapping but distinct substrate specificity. This enzyme catalyzes the reaction of progesterone to the inactive form 20-alpha-hydroxy-progesterone. This gene shares high sequence identity with three other gene …

**Accessions** — [HGNC:384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:384) · Entrez [1645](https://www.ncbi.nlm.nih.gov/gene/1645) · UniProt [Q04828](https://www.uniprot.org/uniprotkb/Q04828) · Ensembl [ENSG00000187134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187134)

## Data

Gene col 11892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11892); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11892]; `tensor/DDL_lfc|DDL_z.npy` [11892]; `embed/gene_vectors.npy` [11892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11892 or target_col == 11892). Every well: [[AKR1C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR1C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
