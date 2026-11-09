---
symbol: "CDC42BPG"
type: "gene"
col: 10074
ensembl_id: "ENSG00000171219"
name: "CDC42 binding protein kinase gamma"
location: "11q13.1"
module: 189
arm: "+"
pooled_cpm: 7.92
n_lines_expressing: 31
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 12
direction_downstream: 24
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# CDC42BPG

*CDC42 binding protein kinase gamma* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +14.4, q 4e-44, up in 20 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.663× (z -4.9, q 5e-04, down in 18 of 28 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.685× (z -4.5, q 0.002, down in 12 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAP1GAP]] (+0.60, fdr 2e-05), [[ACAP3]] (+0.60, fdr 1e-05), [[FOXO6]] (+0.59, fdr 1e-05); moves opposite to [[EXOC4]] (-0.53, fdr 3e-05), [[RPUSD4]] (-0.50, fdr 3e-05), [[TOMM22]] (-0.49, fdr 5e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CGN]] → it (grade B ⚠); 24 go from it, the strongest it → [[NAF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +14.4 | 4e-44 | 20/26 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +14.0 | 8e-42 | 8/25 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +12.2 | 1e-31 | 11/21 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +11.9 | 2e-30 | 25/28 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +10.5 | 7e-24 | 2/10 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +9.8 | 1e-20 | 25/27 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +9.1 | 8e-18 | 21/28 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +8.5 | 1e-15 | 8/15 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.2 | 3e-11 | 15/27 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +7.1 | 5e-11 | 13/25 (SW48, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +6.5 | 5e-09 | 16/28 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.8 | 4e-07 | 5/27 (SW48, LoVo, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.86×** | +3.8 | 0.006 | 6/22 (LoVo, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 10/27 (SW48, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +3.8 | 0.006 | 8/28 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.007 | 12/28 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.041 | 9/27 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.079 | 9/26 (LS 180, Panc 03.27, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -4.9 | 5e-04 | 18/28 (HT-29, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -4.5 | 0.002 | 12/28 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.723×** | -3.7 | 0.046 | 13/27 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD-8055 (drug)]] 0.05 µM |  | **0.734×** | -3.5 | 0.065 | 7/27 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.769× | -3.2 | 0.18 | 9/28 (HepG2/C3A, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0779× (z -10.7) |
| [[LoVo (line)]] | wt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.2) | — |
| [[A-172 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.000 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP1GAP]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ACAP3]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.59 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[EPS8L2]] | +0.58 | +0.27 / +0.56 | both halves | 3e-04 |  |
| [[CBX8]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[BAIAP3]] | +0.56 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[PLXNB2]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MAPK11]] | +0.54 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[CCDC88B]] | +0.54 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[ANO8]] | +0.54 | +0.40 / +0.42 | both halves | 4e-05 |  |
| [[AGRN]] | +0.53 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RPUSD4]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TOMM22]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[INVS]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[DIAPH2]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[FTX]] | -0.46 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[LYRM4]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[IMMP2L]] | -0.45 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[QRSL1]] | -0.45 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[NAF1]] | -0.45 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[POP1]] | -0.45 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[PDS5A]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGN]] | B | CGN activity raises CDC42BPG's level | lines that do not express CGN (21) vs lines expressing it (29) | 3.31× lower at baseline in the lines without CGN | 0.008 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[EPHB3]] | B | EPHB3 activity raises CDC42BPG's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without EPHB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[MFNG]] | B | MFNG activity raises CDC42BPG's level | lines that do not express MFNG (12) vs lines expressing it (38) | 2.64× lower at baseline in the lines without MFNG | 0.012 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[SYTL1]] | B | SYTL1 activity raises CDC42BPG's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.93× lower at baseline in the lines without SYTL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[BIK]] | B | BIK activity raises CDC42BPG's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without BIK | 0.064 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[PLCH2]] | B | PLCH2 activity raises CDC42BPG's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without PLCH2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |
| [[CAMSAP3]] | B | CAMSAP3 activity raises CDC42BPG's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 2.83× lower at baseline in the lines without CAMSAP3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[EPPK1]] | C | EPPK1 activity raises CDC42BPG's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 3.41× lower at baseline in the lines without EPPK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3; co-absent with the target |
| [[ATAD3C]] | C | ATAD3C activity raises CDC42BPG's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 3.31× lower at baseline in the lines without ATAD3C | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1; co-absent with the target |
| [[PPL]] | C | PPL activity raises CDC42BPG's level | lines that do not express PPL (19) vs lines expressing it (31) | 3.33× lower at baseline in the lines without PPL | 0.005 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6; co-absent with the target |
| [[LSR]] | C | LSR activity raises CDC42BPG's level | lines that do not express LSR (19) vs lines expressing it (31) | 3.34× lower at baseline in the lines without LSR | 0.011 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN; co-absent with the target |
| [[EPS8L2]] | C | EPS8L2 activity raises CDC42BPG's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 3.03× lower at baseline in the lines without EPS8L2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 19, C 5. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAF1]] | B | CDC42BPG activity lowers NAF1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.36× higher at baseline in the lines without CDC42BPG | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[BIK]] | B | CDC42BPG activity raises BIK's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without CDC42BPG | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[SYTL1]] | B | CDC42BPG activity raises SYTL1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 2.47× lower at baseline in the lines without CDC42BPG | 0.015 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[CGN]] | B | CDC42BPG activity raises CGN's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 3.81× lower at baseline in the lines without CDC42BPG | 0.016 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[MYO15B]] | B | CDC42BPG activity raises MYO15B's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without CDC42BPG | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[ELFN2]] | B | CDC42BPG activity raises ELFN2's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.98× lower at baseline in the lines without CDC42BPG | 0.023 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[BCAM]] | B | CDC42BPG activity raises BCAM's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without CDC42BPG | 0.029 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[AGRN]] | B | CDC42BPG activity raises AGRN's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.48× lower at baseline in the lines without CDC42BPG | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[INVS]] | B | CDC42BPG activity lowers INVS's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.48× higher at baseline in the lines without CDC42BPG | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[LYRM4]] | B | CDC42BPG activity lowers LYRM4's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.37× higher at baseline in the lines without CDC42BPG | 0.038 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[PDK2]] | B | CDC42BPG activity raises PDK2's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.43× lower at baseline in the lines without CDC42BPG | 0.040 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[AHDC1]] | B | CDC42BPG activity raises AHDC1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.22× lower at baseline in the lines without CDC42BPG | 0.050 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -2.9); signed map (-22.5, 26.2). **Vector** length 51.0, 9.80% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +14.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.9 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 binding protein kinase gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,823,052-64,844,653 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSMDPKIN, MRCKgamma, DMPK2, kappa-200 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; CDC42 binding protein kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DT37](https://www.uniprot.org/uniprotkb/Q6DT37) (Serine/threonine-protein kinase MRCK gamma):

> May act as a downstream effector of CDC42 in cytoskeletal reorganization. Contributes to the actomyosin contractility required for cell invasion, through the regulation of MYPT1 and thus MLC2 phosphorylation (By similarity).

**Summary**, from NCBI Gene [55561](https://www.ncbi.nlm.nih.gov/gene/55561):

> Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in protein phosphorylation. Located in cell leading edge and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29829) · Entrez [55561](https://www.ncbi.nlm.nih.gov/gene/55561) · UniProt [Q6DT37](https://www.uniprot.org/uniprotkb/Q6DT37) · Ensembl [ENSG00000171219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171219)

## Data

Gene col 10074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10074); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10074]; `tensor/DDL_lfc|DDL_z.npy` [10074]; `embed/gene_vectors.npy` [10074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10074 or target_col == 10074). Every well: [[CDC42BPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42BPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
