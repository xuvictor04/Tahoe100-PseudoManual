---
symbol: "SULT2B1"
type: "gene"
col: 1517
ensembl_id: "ENSG00000088002"
name: "sulfotransferase family 2B member 1"
location: "19q13.33"
module: 31
arm: "+"
pooled_cpm: 7.78
n_lines_expressing: 22
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 80
direction_downstream: 120
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# SULT2B1

*sulfotransferase family 2B member 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.00× (z +14.0, q 9e-42, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +12.5, q 2e-33, up in 6 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.599× (z -5.4, q 4e-05, down in 8 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FA2H]] (+0.74, fdr 7e-06), [[TMPRSS4]] (+0.74, fdr 7e-06), [[ANKRD22]] (+0.69, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 80 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 120 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +14.0 | 9e-42 | 4/7 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +12.5 | 2e-33 | 6/18 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +11.5 | 1e-28 | 4/13 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +10.4 | 5e-23 | 2/18 (HEC-1-A, LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +10.2 | 2e-22 | 14/18 (SW1417, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +9.4 | 3e-19 | 2/10 (SW1417, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +6.7 | 2e-09 | 13/18 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.9 | 3e-07 | 3/18 (SW480, HEC-1-A, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.012 | 3/18 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.6 | 0.015 | 1/17 (SW1417) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.015 | 2/18 (BT-474, SW1417) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.4 | 0.035 | 3/18 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -5.4 | 4e-05 | 8/18 (LS 180, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.665×** | -4.3 | 0.005 | 8/18 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.693×** | -3.8 | 0.023 | 10/18 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.678×** | -3.8 | 0.023 | 5/18 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.782×** | -3.7 | 0.029 | 16/18 (SW48, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM |  | 0.726× | -3.2 | 0.11 | 6/19 (A549, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.555× | -3.2 | 0.12 | 9/18 (BT-474, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.814× | -3.1 | 0.14 | 5/18 (A549, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.750× | -3.0 | 0.14 | 4/18 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.751× | -3.0 | 0.14 | 1/18 (LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 22.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -13.8) |
| [[HT-29 (line)]] | alt | 128 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0597× (z -19.0) |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -10.6) |
| [[SW1417 (line)]] | alt | 27.1 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.56× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.9) |
| [[KATO III (line)]] | alt | 8.89 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.21× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0721× (z -10.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0649× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0914× (z -8.8) ⚠ cell-cycle shift, explains ~5% of this change |
| [[LoVo (line)]] | wt | 2.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 2.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FA2H]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ANKRD22]] | +0.69 | +0.56 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[SLC5A1]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[BAIAP2L1]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[KLK10]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RDH13]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CEACAM6]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LIPH]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[HS3ST1]] | +0.64 | +0.57 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[KLK11]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*80 arrows, 80 of them with an alert ⚠; grade A 0, B 9, C 71. Shown: the 12 strongest; 68 more arrows (68 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises SULT2B1's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without EPS8L1 | 0.014 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[CDA]] | B | CDA activity raises SULT2B1's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.55× lower at baseline in the lines without CDA | 0.023 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[LSMEM2]] | B | LSMEM2 activity raises SULT2B1's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.30× lower at baseline in the lines without LSMEM2 | 0.036 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[FAM83E]] | B | FAM83E activity raises SULT2B1's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.61× lower at baseline in the lines without FAM83E | 0.045 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[KRT15]] | B | KRT15 activity raises SULT2B1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.54× lower at baseline in the lines without KRT15 | 0.048 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[SEMA3B]] | B | SEMA3B activity raises SULT2B1's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without SEMA3B | 0.058 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises SULT2B1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without KPNA7 | 0.088 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity raises SULT2B1's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.61× lower at baseline in the lines without TMC6 | 0.090 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[XYLT1]] | B | XYLT1 activity raises SULT2B1's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without XYLT1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[B3GNT3]] | C | B3GNT3 activity raises SULT2B1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.02× lower at baseline in the lines without B3GNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises SULT2B1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.34× lower at baseline in the lines without TMPRSS4 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises SULT2B1's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 4.02× lower at baseline in the lines without P2RY2 | 1e-04 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |

### Downstream of this gene

*120 arrows, 120 of them with an alert ⚠; grade A 0, B 46, C 74. Shown: the 12 strongest; 108 more arrows (108 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | SULT2B1 activity raises EPS8L1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 4.36× lower at baseline in the lines without SULT2B1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[PLS1]] | B | SULT2B1 activity raises PLS1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 4.07× lower at baseline in the lines without SULT2B1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[KPNA7]] | B | SULT2B1 activity raises KPNA7's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without SULT2B1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[TLDC2]] | B | SULT2B1 activity raises TLDC2's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without SULT2B1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[CDA]] | B | SULT2B1 activity raises CDA's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.68× lower at baseline in the lines without SULT2B1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[TMC6]] | B | SULT2B1 activity raises TMC6's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 3.76× lower at baseline in the lines without SULT2B1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[LSMEM2]] | B | SULT2B1 activity raises LSMEM2's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.07× lower at baseline in the lines without SULT2B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[FAM83E]] | B | SULT2B1 activity raises FAM83E's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 3.70× lower at baseline in the lines without SULT2B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[LYPD3]] | B | SULT2B1 activity raises LYPD3's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without SULT2B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[BAIAP2L1]] | B | SULT2B1 activity raises BAIAP2L1's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without SULT2B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[SEMA3B]] | B | SULT2B1 activity raises SEMA3B's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 3.15× lower at baseline in the lines without SULT2B1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[ABHD11]] | B | SULT2B1 activity raises ABHD11's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.68× lower at baseline in the lines without SULT2B1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, 55.1); signed map (-0.5, 38.2). **Vector** length 62.1, 18.4% of its response variance represented; |z| ≥ 3 in 497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +14.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.8 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | sulfotransferase family 2B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,552,172-48,599,425 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSST2 |
| Gene groups (HGNC) | Sulfotransferases, cytosolic |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ESTROGEN_RESPONSE_LATE, HYPOXIA, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Cytosolic sulfonation of small molecules; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [O00204](https://www.uniprot.org/uniprotkb/O00204) (Sulfotransferase 2B1):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) as sulfonate donor to catalyze the sulfate conjugation. Responsible for the sulfation of cholesterol. Catalyzes sulfation of the 3beta-hydroxyl groups of steroids, such as, pregnenolone and dehydroepiandrosterone (DHEA). Preferentially sulfonates cholesterol, while it also has significant activity with pregnenolone and DHEA. Plays a role in epidermal cholesterol metabolism and in the regulation of epidermal proliferation and …

**Summary**, from NCBI Gene [6820](https://www.ncbi.nlm.nih.gov/gene/6820):

> Sulfotransferase enzymes catalyze the sulfate conjugation of many hormones, neurotransmitters, drugs, and xenobiotic compounds. These cytosolic enzymes are different in their tissue distributions and substrate specificities. The gene structure (number and length of exons) is similar among family members. This gene sulfates dehydroepiandrosterone but not 4-nitrophenol, a typical substrate for the phenol and estrogen sulfotransferase subfamilies. Two alternatively spliced variants that encode …

**Accessions** — [HGNC:11459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11459) · Entrez [6820](https://www.ncbi.nlm.nih.gov/gene/6820) · UniProt [O00204](https://www.uniprot.org/uniprotkb/O00204) · Ensembl [ENSG00000088002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088002)

## Data

Gene col 1517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1517); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1517]; `tensor/DDL_lfc|DDL_z.npy` [1517]; `embed/gene_vectors.npy` [1517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1517 or target_col == 1517). Every well: [[SULT2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SULT2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
