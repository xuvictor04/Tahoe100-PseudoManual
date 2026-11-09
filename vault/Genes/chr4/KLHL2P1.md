---
symbol: "KLHL2P1"
type: "gene"
col: 14693
ensembl_id: "ENSG00000250412"
name: "kelch like family member 2 pseudogene 1"
location: "4q26"
module: 8
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 21
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# KLHL2P1

*kelch like family member 2 pseudogene 1* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +7.8, q 5e-12, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +6.3, q 9e-08, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.410× (z -8.6, q 5e-15, down in 28 of 45 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.426× (z -8.2, q 6e-14, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POU5F1B]] (+0.63, fdr 3e-05), [[STEAP2-AS1]] (+0.63, fdr 3e-05), [[MAMDC2-AS1]] (+0.62, fdr 3e-05); moves opposite to [[LIX1L]] (-0.52, fdr 2e-04), [[DENND6A]] (-0.50, fdr 3e-04), [[PCBP3]] (-0.49, fdr 3e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[FAM83B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +7.8 | 5e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.3 | 9e-08 | 14/33 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.69×** | +5.1 | 8e-05 | 7/39 (NCI-H1573, NCI-H2347, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +4.8 | 2e-04 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.016 | 12/32 (NCI-H1573, NCI-H2347, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.30×** | +3.6 | 0.034 | 6/41 (NCI-H460, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.5 | 0.035 | 2/46 (MIA PaCa-2, AsPC-1) | inconsistent across doses |  |
| [[Valdecoxib (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.037 | 7/38 (RKO, SW1417, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.072 | 2/25 (PANC-1, C32) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.12 | 3/38 (KATO III, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Finasteride (drug)]] 5 µM |  | 1.39× | +3.0 | 0.12 | 2/40 (AsPC-1, SHP-77) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.82× | +3.0 | 0.12 | 4/19 (LS 180, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.410×** | -8.6 | 5e-15 | 28/45 (NCI-H1573, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.426×** | -8.2 | 6e-14 | 21/39 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.465×** | -7.4 | 3e-11 | 26/38 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.499×** | -6.4 | 2e-08 | 18/38 (NCI-H1573, KATO III, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.533×** | -6.1 | 2e-07 | 20/43 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.601×** | -4.9 | 1e-04 | 18/41 (LoVo, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.624×** | -4.5 | 5e-04 | 16/27 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.617×** | -4.5 | 6e-04 | 9/42 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.640×** | -4.3 | 0.001 | 15/43 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.666×** | -3.9 | 0.005 | 16/41 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.666×** | -3.9 | 0.005 | 11/43 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 0.05 µM |  | **0.689×** | -3.6 | 0.015 | 5/37 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.690×** | -3.6 | 0.015 | 13/40 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.701×** | -3.4 | 0.027 | 12/40 (MIA PaCa-2, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -12.6) |
| [[LoVo (line)]] | wt | 9.59 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.0985× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.152× (z -9.6) |
| [[HT-29 (line)]] | alt | 5.87 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0806× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[KATO III (line)]] | alt | 3.99 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0562× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 6.27 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0492× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 4.75 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0481× (z -9.7) |
| [[A-172 (line)]] | wt | 0.910 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.909 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.854 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU5F1B]] | +0.63 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[STEAP2-AS1]] | +0.63 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[MAMDC2-AS1]] | +0.62 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SLC44A3-AS1]] | +0.62 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[ATXN7L3-AS1]] | +0.61 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[ST8SIA6]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[LINC00571]] | +0.59 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[PCAT1]] | +0.58 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[TTC39A]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[GNA14]] | +0.58 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[DNASE1]] | +0.57 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[PRRG2]] | +0.57 | +0.66 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIX1L]] | -0.52 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[DENND6A]] | -0.50 | -0.52 / -0.29 | both halves | 3e-04 |  |
| [[PCBP3]] | -0.49 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[ACTR5]] | -0.49 | -0.47 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83B]] | B | FAM83B activity raises KLHL2P1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[LIX1L]] | B | LIX1L activity lowers KLHL2P1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.16× higher at baseline in the lines without LIX1L | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[STARD9]] | B | STARD9 activity lowers KLHL2P1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.99× higher at baseline in the lines without STARD9 | 0.009 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[TMC4]] | B | TMC4 activity raises KLHL2P1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 1.49× lower at baseline in the lines without TMC4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[SLC28A3]] | B | SLC28A3 activity raises KLHL2P1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.60× lower at baseline in the lines without SLC28A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[MROH3P]] | B | MROH3P activity raises KLHL2P1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without MROH3P | 0.023 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[THRB]] | B | THRB activity raises KLHL2P1's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without THRB | 0.025 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[FUT3]] | B | FUT3 activity raises KLHL2P1's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without FUT3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[PCAT1]] | B | PCAT1 activity strengthens KLHL2P1's drug response | lines that do not express PCAT1 (10) vs lines expressing it (35) | the lines without PCAT1 respond 0.64× as strongly (z diff +1.14); strongest at Ouabain (Octahydrate) 5 µM: 0.78x vs 0.29x (z diff +3.4) | 0.032 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CATSPERB]] | B | CATSPERB activity raises KLHL2P1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.60× lower at baseline in the lines without CATSPERB | 0.036 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[ST8SIA6]] | B | ST8SIA6 activity raises KLHL2P1's level | lines that do not express ST8SIA6 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without ST8SIA6 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRKCH-AS1, TCN1, MUC2 |
| [[RNF220]] | B | RNF220 activity lowers KLHL2P1's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 1.53× higher at baseline in the lines without RNF220 | 0.044 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.2, 51.5); signed map (58.1, -0.3). **Vector** length 54.4, 7.46% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.1 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.0 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.6 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 4q26 — chr4:119,334,329-119,378,233 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | MAVP1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44046) · Entrez [729249](https://www.ncbi.nlm.nih.gov/gene/729249) · Ensembl [ENSG00000250412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250412)

## Data

Gene col 14693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14693); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14693]; `tensor/DDL_lfc|DDL_z.npy` [14693]; `embed/gene_vectors.npy` [14693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14693 or target_col == 14693). Every well: [[KLHL2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
