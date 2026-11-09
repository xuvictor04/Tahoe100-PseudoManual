---
symbol: "MROH3P"
type: "gene"
col: 13894
ensembl_id: "ENSG00000233217"
name: "maestro heat like repeat family member 3, pseudogene"
location: "1q32.1"
module: 47
arm: "+"
pooled_cpm: 6.65
n_lines_expressing: 21
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 72
direction_downstream: 127
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MROH3P

*maestro heat like repeat family member 3, pseudogene* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +12.9, q 4e-35, up in 7 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.476× (z -6.0, q 9e-07, down in 16 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf38]] (+0.72, fdr 7e-06), [[FAM83E]] (+0.70, fdr 7e-06), [[LSMEM2]] (+0.67, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 72 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 127 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +12.9 | 4e-35 | 7/19 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.35×** | +11.4 | 1e-27 | 2/9 (LoVo, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +6.7 | 4e-09 | 1/11 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +6.6 | 6e-09 | 2/16 (A498, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +6.3 | 4e-08 | 4/19 (RPMI-7951, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +5.5 | 3e-06 | 4/19 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.5 | 4e-04 | 4/18 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.68×** | +4.2 | 0.002 | 17/19 (HT-29, KATO III, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.012 | 2/19 (NCI-H2347, KATO III) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.6 | 0.018 | 0/18 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.3 | 0.058 | 2/17 (A498, NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | 1.48× | +3.0 | 0.12 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.476×** | -6.0 | 9e-07 | 16/19 (KATO III, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -4.6 | 0.001 | 14/19 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.626×** | -3.8 | 0.025 | 12/19 (HT-29, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[NG25 (drug)]] 5 µM |  | **0.428×** | -3.6 | 0.044 | 13/17 (KATO III, SW48, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.663×** | -3.4 | 0.088 | 2/19 (NCI-H2347, CFPAC-1) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.675× | -3.2 | 0.12 | 11/19 (COLO 205, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.679× | -3.2 | 0.13 | 11/19 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.685× | -3.1 | 0.13 | 10/19 (LS 180, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Mozavaptan (drug)]] 0.5 µM |  | 0.686× | -3.1 | 0.13 | 4/19 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.689× | -3.0 | 0.13 | 14/19 (HepG2/C3A, KATO III, …) | two highest doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 32.6 | 0 | 10 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0243× (z -15.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.1) |
| [[KATO III (line)]] | alt | 21.2 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0297× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 36.3 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0405× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.113× (z -10.6) |
| [[LoVo (line)]] | wt | 29.9 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -10.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.147× (z -8.8) |
| [[COLO 205 (line)]] | alt | 37.6 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0437× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0423× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0581× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0680× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.186× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 8.39 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0553× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 7.20 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0568× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0615× (z -8.7) |
| [[A498 (line)]] | wt | 1.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.25× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0354× (z -9.8) |
| [[LS 180 (line)]] | wt | 5.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0559× (z -9.1) |
| [[A-172 (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf38]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[FAM83E]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LSMEM2]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[INAVA]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 | ⚠ same locus (1.7 kb, same strand: neighbours can correlate without regulation) |
| [[C1orf116]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[TNNT2]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[OIT3]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SLC22A20P]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 | same gene group |
| [[ARHGAP30]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[HPN]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[LMO7DN]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CDH1]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*72 arrows, 72 of them with an alert ⚠; grade A 0, B 15, C 57. Shown: the 12 strongest; 60 more arrows (60 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises MROH3P's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.91× lower at baseline in the lines without EPS8L1 | 0.013 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises MROH3P's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without LMO7DN | 0.019 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[SPATA6L]] | B | SPATA6L activity raises MROH3P's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 3.10× lower at baseline in the lines without SPATA6L | 0.022 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises MROH3P's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without NOSTRIN | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[MUC20]] | B | MUC20 activity raises MROH3P's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.79× lower at baseline in the lines without MUC20 | 0.033 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises MROH3P's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without LMO7 | 0.036 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[LSMEM2]] | B | LSMEM2 activity raises MROH3P's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without LSMEM2 | 0.036 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[PTPRB]] | B | PTPRB activity raises MROH3P's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without PTPRB | 0.052 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[MAPK13]] | B | MAPK13 activity raises MROH3P's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without MAPK13 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises MROH3P's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.08× lower at baseline in the lines without SRMS | 0.060 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[FBLIM1]] | B | FBLIM1 activity raises MROH3P's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without FBLIM1 | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[TOP2A]] | B | TOP2A activity lowers MROH3P's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*127 arrows, 127 of them with an alert ⚠; grade A 0, B 68, C 59. Shown: the 12 strongest; 115 more arrows (115 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | [[INAVA]], MROH3P activity raises EPS8L1's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.97× lower at baseline in the lines without INAVA, MROH3P | 8e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[KPNA7]] | B | MROH3P activity raises KPNA7's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 3.47× lower at baseline in the lines without MROH3P | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TLDC2]] | B | [[INAVA]], MROH3P activity raises TLDC2's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 2.52× lower at baseline in the lines without INAVA, MROH3P | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[ARHGAP27]] | B | MROH3P activity raises ARHGAP27's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.79× lower at baseline in the lines without MROH3P | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[PATJ]] | B | [[INAVA]], MROH3P activity raises PATJ's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.35× lower at baseline in the lines without INAVA, MROH3P | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[ITPKC]] | B | [[INAVA]], MROH3P activity raises ITPKC's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 2.96× lower at baseline in the lines without INAVA, MROH3P | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[LMO7]] | B | MROH3P activity raises LMO7's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 4.45× lower at baseline in the lines without MROH3P | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[MUC20]] | B | MROH3P activity raises MUC20's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 3.61× lower at baseline in the lines without MROH3P | 7e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[FAM83E]] | B | [[INAVA]], MROH3P activity raises FAM83E's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.44× lower at baseline in the lines without INAVA, MROH3P | 8e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[SDCBP2]] | B | [[INAVA]], MROH3P activity raises SDCBP2's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 4.00× lower at baseline in the lines without INAVA, MROH3P | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[UNC13D]] | B | MROH3P activity raises UNC13D's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without MROH3P | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[HAP1]] | B | MROH3P activity raises HAP1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.14× lower at baseline in the lines without MROH3P | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.5, 56.0); signed map (57.2, 6.7). **Vector** length 71.3, 21.4% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | +0.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.7 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.6 |
|  | [[NG25 (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -6.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | maestro heat like repeat family member 3, pseudogene |
| Locus type | pseudogene |
| Location | 1q32.1 — chr1:200,917,460-200,966,536 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ; previously C1orf81 |
| Gene groups (HGNC) | Maestro heat like repeat containing; Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33122) · Entrez [647215](https://www.ncbi.nlm.nih.gov/gene/647215) · Ensembl [ENSG00000233217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233217)

## Data

Gene col 13894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13894); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13894]; `tensor/DDL_lfc|DDL_z.npy` [13894]; `embed/gene_vectors.npy` [13894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13894 or target_col == 13894). Every well: [[MROH3P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MROH3P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
