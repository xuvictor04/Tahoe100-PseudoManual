---
symbol: "LAG3"
type: "gene"
col: 1595
ensembl_id: "ENSG00000089692"
name: "lymphocyte activating 3"
location: "12p13.31"
module: 53
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 42
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# LAG3

*lymphocyte activating 3* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.46× (z +9.1, q 4e-17, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 2.16× (z +5.9, q 1e-06, up in 17 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.402× (z -6.9, q 2e-09, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AZU1]] (+0.70, fdr 7e-06), [[SMIM41]] (+0.67, fdr 7e-06), [[MIR9-1HG]] (+0.65, fdr 7e-06); moves opposite to [[EIF2B1]] (-0.49, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PDGFA]] → it (grade B ⚠); 9 go from it, the strongest it → [[PRX]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.46×** | +9.1 | 4e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **2.16×** | +5.9 | 1e-06 | 17/38 (SW480, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +5.6 | 5e-06 | 1/3 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +4.5 | 8e-04 | 8/26 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.021 | 7/33 (A549, NCI-H23, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.4 | 0.054 | 2/9 (NCI-H2030, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.065 | 4/21 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.52×** | +3.2 | 0.089 | 1/17 (PANC-1) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.402×** | -6.9 | 2e-09 | 19/30 (A-427, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.414×** | -6.7 | 5e-09 | 21/36 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.443×** | -6.2 | 1e-07 | 21/38 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -5.7 | 2e-06 | 19/34 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Erlotinib (drug)]] 5 µM |  | **0.541×** | -4.5 | 8e-04 | 11/27 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.574×** | -4.2 | 0.002 | 14/29 (NCI-H23, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.348×** | -4.2 | 0.002 | 14/27 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.586×** | -4.1 | 0.003 | 14/33 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -4.0 | 0.005 | 12/17 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.586×** | -3.9 | 0.005 | 15/31 (C32, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.608×** | -3.8 | 0.008 | 14/33 (SW480, H4, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.610×** | -3.8 | 0.008 | 13/34 (SW480, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.613×** | -3.7 | 0.009 | 10/37 (NCI-H23, A-427, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.616×** | -3.5 | 0.016 | 11/31 (SW480, H4, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.643×** | -3.4 | 0.030 | 3/37 (C-33 A, SW48, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.631×** | -3.2 | 0.041 | 11/38 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -3.2 | 0.044 | 11/37 (A-427, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.657×** | -3.0 | 0.093 | 3/36 (hTERT-HPNE, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.28 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.131× (z -9.2) |
| [[A-172 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.670 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.713 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.827 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.783 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AZU1]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.67 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CSPG5]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PYGM]] | +0.64 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[CPT1C]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PILRA]] | +0.64 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[MYLK2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[DLG4]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[LRRC23]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SIDT2]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ASGR1]] | +0.62 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B1]] | -0.49 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFA]] | B | PDGFA activity raises LAG3's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without PDGFA | 0.016 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises LAG3's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without ASGR1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[SSC5D]] | B | SSC5D activity raises LAG3's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.93× lower at baseline in the lines without SSC5D | 0.032 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[HCN2]] | B | HCN2 activity raises LAG3's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.11× lower at baseline in the lines without HCN2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[MRC2]] | B | MRC2 activity raises LAG3's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without MRC2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[SPOCK2]] | B | SPOCK2 activity raises LAG3's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without SPOCK2 | 0.078 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRX]] | B | LAG3 activity raises PRX's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without LAG3 | 0.025 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[HCN2]] | B | LAG3 activity raises HCN2's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without LAG3 | 0.029 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[SSC5D]] | B | LAG3 activity raises SSC5D's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 2.42× lower at baseline in the lines without LAG3 | 0.042 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[NCKAP5L]] | B | LAG3 activity raises NCKAP5L's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 2.04× lower at baseline in the lines without LAG3 | 0.047 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[CPNE9]] | B | LAG3 activity raises CPNE9's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without LAG3 | 0.053 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[LRRC23]] | B | LAG3 activity raises LRRC23's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without LAG3 | 0.059 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[MRC2]] | B | LAG3 activity raises MRC2's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 5.51× lower at baseline in the lines without LAG3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[KIF17]] | B | LAG3 activity raises KIF17's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without LAG3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[SCN1B]] | B | LAG3 activity raises SCN1B's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without LAG3 | 0.083 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.2, -17.7); signed map (15.8, 13.2). **Vector** length 55.7, 8.91% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | lymphocyte activating 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,772,512-6,778,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD223 |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing |
| Reactome | 2 pathways, smallest: MHC class II antigen presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P18627](https://www.uniprot.org/uniprotkb/P18627) (Lymphocyte activation gene 3 protein):

> [Lymphocyte activation gene 3 protein]: Inhibitory receptor on antigen activated T-cells. Delivers inhibitory signals upon binding to ligands, such as MHC class II, its main ligand present at the surface of antigen-presenting cells (APCs), and FGL1, which is secreted by hepatocytes and certain types of tumor cells. Ligand-binding initiates a signaling that inhibits the T-cell receptor (TCR) in the immunological synapse, preventing T-cell activation. Mechanistically, ligand-binding promotes (1) …

**Summary**, from NCBI Gene [3902](https://www.ncbi.nlm.nih.gov/gene/3902):

> Lymphocyte-activation protein 3 belongs to Ig superfamily and contains 4 extracellular Ig-like domains. The LAG3 gene contains 8 exons. The sequence data, exon/intron organization, and chromosomal localization all indicate a close relationship of LAG3 to CD4. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6476) · Entrez [3902](https://www.ncbi.nlm.nih.gov/gene/3902) · UniProt [P18627](https://www.uniprot.org/uniprotkb/P18627) · Ensembl [ENSG00000089692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089692)

## Data

Gene col 1595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1595); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1595]; `tensor/DDL_lfc|DDL_z.npy` [1595]; `embed/gene_vectors.npy` [1595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1595 or target_col == 1595). Every well: [[LAG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
