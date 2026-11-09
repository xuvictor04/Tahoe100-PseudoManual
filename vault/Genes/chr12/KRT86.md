---
symbol: "KRT86"
type: "gene"
col: 9953
ensembl_id: "ENSG00000170442"
name: "keratin 86"
location: "12q13"
module: 47
arm: "+"
pooled_cpm: 14.33
n_lines_expressing: 31
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 17
direction_downstream: 16
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# KRT86

*keratin 86* — 12q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.31× (z +32.3, q 0e+00, up in 21 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.425× (z -9.8, q 9e-20, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTNR1A]] (+0.69, fdr 7e-06), [[TNNT2]] (+0.64, fdr 9e-06), [[MMP25]] (+0.64, fdr 1e-05); moves opposite to [[ECI2]] (-0.57, fdr 1e-05), [[NUDT2]] (-0.50, fdr 3e-05), [[SEC11A]] (-0.49, fdr 4e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[MROH3P]] → it (grade B ⚠); 16 go from it, the strongest it → [[KRT7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.31×** | +32.3 | 0e+00 | 21/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +10.8 | 1e-24 | 16/27 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +10.4 | 6e-23 | 17/27 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.7 | 4e-09 | 10/25 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.4 | 2e-08 | 7/16 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.7 | 9e-07 | 15/28 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.1 | 3e-05 | 14/28 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.004 | 8/28 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.32× | +3.1 | 0.12 | 4/24 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.30× | +3.0 | 0.13 | 3/23 (SNU-423, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.30× | +3.0 | 0.13 | 4/28 (NCI-H460, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.425×** | -9.8 | 9e-20 | 23/28 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.431×** | -9.6 | 2e-19 | 24/28 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.449×** | -9.1 | 1e-17 | 23/28 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -8.2 | 3e-14 | 22/28 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -6.3 | 3e-08 | 15/25 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -5.8 | 5e-07 | 12/28 (BT-474, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -5.6 | 2e-06 | 17/28 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.632×** | -5.2 | 1e-05 | 14/28 (A-172, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.650×** | -4.9 | 6e-05 | 15/27 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.650×** | -4.7 | 1e-04 | 10/28 (BT-474, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.665×** | -4.6 | 2e-04 | 9/28 (SHP-77, LoVo, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -4.2 | 0.001 | 14/28 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.678×** | -4.2 | 0.001 | 10/27 (BT-474, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.700×** | -4.0 | 0.002 | 12/28 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.686×** | -4.0 | 0.003 | 7/28 (SW480, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 125 | 0 | 19 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0400× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 9.67 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +23.1) | [[Belinostat (drug)]] 5 µM 0.185× (z -10.0) |
| [[KATO III (line)]] | alt | 56.9 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0332× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0777× (z -9.6) |
| [[LoVo (line)]] | wt | 21.4 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.0747× (z -14.7) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -10.7) |
| [[A-172 (line)]] | wt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +17.7) | — |
| [[NCI-H1573 (line)]] | alt | 39.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0344× (z -13.5) |
| [[A498 (line)]] | wt | 5.93 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 5.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.5× (z +17.6) | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -12.5) |
| [[HCT15 (line)]] | alt | 4.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0468× (z -8.6) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0656× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 4.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 5.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +8.5) | — |
| [[SW48 (line)]] | wt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +11.7) | — |
| [[A-427 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTNR1A]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TNNT2]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[MMP25]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[LSMEM2]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ADAP1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SH2D4B]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SEMA4A]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PITRM1-AS1]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CAPN8]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[FBXW10B]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SLC2A9]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[KRT7]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 | same gene group; pathway: Formation of the cornified envelope; STRING 504; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GRAMD2A]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECI2]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NUDT2]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SEC11A]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH3P]] | B | MROH3P activity raises KRT86's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.46× lower at baseline in the lines without MROH3P | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[KRT7]] | B | KRT7 activity raises KRT86's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 3.65× lower at baseline in the lines without KRT7 | 0.009 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[S100A9]] | B | S100A9 activity raises KRT86's level | lines that do not express S100A9 (42) vs lines expressing it (8) | 4.66× lower at baseline in the lines without S100A9 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, GSDMC, KRT20 |
| [[GSDMC]] | B | GSDMC activity raises KRT86's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 4.28× lower at baseline in the lines without GSDMC | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[IL1RN]] | B | IL1RN activity raises KRT86's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without IL1RN | 0.020 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[TNNT2]] | B | TNNT2 activity raises KRT86's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.79× lower at baseline in the lines without TNNT2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity raises KRT86's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 3.19× lower at baseline in the lines without EPHA1-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises KRT86's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.86× lower at baseline in the lines without LMO7 | 0.047 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[SDR16C5]] | B | SDR16C5 activity raises KRT86's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 2.70× lower at baseline in the lines without SDR16C5 | 0.048 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[KRT18]] | B | KRT18 activity raises KRT86's level | lines that do not express KRT18 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without KRT18 | 0.050 | ⚠ within organs, on part of the lines; also absent: MISP, SFN, GRB7; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises KRT86's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 3.02× lower at baseline in the lines without SEMA4A | 0.053 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[ABCC3]] | B | ABCC3 activity raises KRT86's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without ABCC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT7]] | B | KRT86 activity raises KRT7's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 4.49× lower at baseline in the lines without KRT86 | 0.004 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[SDR16C5]] | B | KRT86 activity raises SDR16C5's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without KRT86 | 0.007 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[PEBP4]] | B | KRT86 activity raises PEBP4's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without KRT86 | 0.008 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[ABCC3]] | B | KRT86 activity raises ABCC3's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 3.56× lower at baseline in the lines without KRT86 | 0.019 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[PITPNM3]] | B | KRT86 activity raises PITPNM3's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without KRT86 | 0.023 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[EPHA1-AS1]] | B | KRT86 activity raises EPHA1-AS1's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without KRT86 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[SEC11A]] | B | KRT86 activity raises SEC11A's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.20× lower at baseline in the lines without KRT86 | 0.040 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[LINC00592]] | B | KRT86 activity raises LINC00592's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without KRT86 | 0.043 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[LMO7]] | B | KRT86 activity raises LMO7's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.52× lower at baseline in the lines without KRT86 | 0.043 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[SEMA4A]] | B | KRT86 activity raises SEMA4A's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without KRT86 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[KRT8]] | B | KRT86 activity raises KRT8's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.76× lower at baseline in the lines without KRT86 | 0.057 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[KRT18]] | B | KRT86 activity raises KRT18's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without KRT86 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.1, -11.3); signed map (21.9, 14.9). **Vector** length 83.0, 20.8% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +32.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -5.8 |
|  | [[NG25 (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | keratin 86 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13 — chr12:52,249,300-52,309,163 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MNX, Hb6; previously KRTHB6 |
| Gene groups (HGNC) | Keratins, type II |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43790](https://www.uniprot.org/uniprotkb/O43790) (Keratin, type II cuticular Hb6):

> Structural component of intermediate filaments in the hair shaft. Forms obligate heterodimers with type I hair keratins, which assemble into keratin intermediate filaments that contribute to the structural integrity and mechanical strength of the hair shaft.

**Summary**, from NCBI Gene [3892](https://www.ncbi.nlm.nih.gov/gene/3892):

> This gene encodes a type II keratin protein, which heterodimerizes with type I keratins to form hair and nails. This gene is present in a cluster of related genes and pseudogenes on chromosome 12. Mutations in this gene have been observed in patients with the hair disease monilethrix. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:6463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6463) · Entrez [3892](https://www.ncbi.nlm.nih.gov/gene/3892) · UniProt [O43790](https://www.uniprot.org/uniprotkb/O43790) · Ensembl [ENSG00000170442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170442)

## Data

Gene col 9953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9953); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9953]; `tensor/DDL_lfc|DDL_z.npy` [9953]; `embed/gene_vectors.npy` [9953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9953 or target_col == 9953). Every well: [[KRT86 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT86.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
