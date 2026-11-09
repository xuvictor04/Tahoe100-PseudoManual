---
symbol: "FUT3"
type: "gene"
col: 10055
ensembl_id: "ENSG00000171124"
name: "fucosyltransferase 3 (Lewis blood group)"
location: "19p13.3"
module: 8
arm: "+"
pooled_cpm: 7.34
n_lines_expressing: 21
n_dd_up: 29
n_dd_down: 11
n_dd_up_clean: 21
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 70
direction_downstream: 88
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FUT3

*fucosyltransferase 3 (Lewis blood group)* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.40× (z +23.0, q 0e+00, up in 8 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.738× (z -4.8, q 0.001, down in 11 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A4]] (+0.72, fdr 7e-06), [[ESRP1]] (+0.71, fdr 7e-06), [[ADCY4]] (+0.71, fdr 7e-06); moves opposite to [[TTC28]] (-0.49, fdr 3e-05), [[BNC2]] (-0.47, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 70 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); 88 go from it, the strongest it → [[MUC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.40×** | +23.0 | 0e+00 | 8/15 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.20×** | +18.1 | 0e+00 | 4/15 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.58×** | +10.4 | 5e-23 | 4/15 (SW480, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +7.8 | 1e-12 | 4/14 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +7.8 | 1e-12 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +7.4 | 1e-11 | 6/18 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.3 | 2e-11 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.8 | 1e-09 | 5/18 (A498, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +5.9 | 2e-07 | 0/11 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.4 | 4e-06 | 1/14 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +5.3 | 6e-06 | 2/14 (A498, HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.8 | 9e-05 | 0/7 | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.6 | 2e-04 | 1/13 (A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.6 | 2e-04 | 5/19 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.54×** | +4.5 | 2e-04 | 4/13 (SW480, SW1417, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.002 | 3/14 (A498, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.75×** | +3.2 | 0.041 | 0/13 | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.041 | 4/18 (LS 180, KATO III, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.041 | 1/14 (CFPAC-1) | inconsistent across doses | position effect removed |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.048 | 0/17 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.063 | 4/14 (COLO 205, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.738×** | -4.8 | 0.001 | 11/17 (NCI-H1573, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adenine (drug)]] 5 µM |  | **0.753×** | -4.4 | 0.002 | 1/18 (CFPAC-1) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.661×** | -4.4 | 0.002 | 12/16 (NCI-H2347, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -3.6 | 0.039 | 9/17 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.705×** | -3.6 | 0.039 | 1/18 (HEC-1-A) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.718×** | -3.5 | 0.045 | 1/18 (SNU-1) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.045 | 11/15 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.739×** | -3.4 | 0.051 | 4/18 (LS 180, HCT15, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.739×** | -3.3 | 0.051 | 2/18 (HCT15, LS 180) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.746×** | -3.2 | 0.067 | 1/18 (SW48) | top dose only |  |
| [[Orlistat (drug)]] 5 µM |  | **0.739×** | -3.2 | 0.067 | 4/18 (H4, SNU-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 68.0 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0583× (z -25.8) |
| [[LS 180 (line)]] | wt | 136 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -20.6) |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0741× (z -24.6) |
| [[KATO III (line)]] | alt | 25.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -17.1) |
| [[HT-29 (line)]] | alt | 4.91 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0906× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 3.62 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0331× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.893 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A4]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ESRP1]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ADCY4]] | +0.71 | +0.70 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[TMEM125]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[TMC4]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[GALNT3]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[INAVA]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[RORC]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.66 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[FAM83E]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NECTIN4]] | +0.63 | +0.69 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC28]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[BNC2]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 10, C 60. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity lowers FUT3's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.22× higher at baseline in the lines without TTC28 | 0.027 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[ARHGAP30]] | B | ARHGAP30 activity raises FUT3's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.21× lower at baseline in the lines without ARHGAP30 | 0.040 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[DCLK2]] | B | DCLK2 activity lowers FUT3's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 2.83× higher at baseline in the lines without DCLK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[SPATA6L]] | B | SPATA6L activity raises FUT3's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without SPATA6L | 0.060 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises FUT3's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without EPS8L1 | 0.060 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FUT3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LPAR5]] | B | LPAR5 activity raises FUT3's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without LPAR5 | 0.073 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[MUC20]] | B | MUC20 activity raises FUT3's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without MUC20 | 0.094 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises FUT3's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.22× lower at baseline in the lines without PLEKHG1 | 0.097 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[SDCBP2]] | B | SDCBP2 activity raises FUT3's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.13× lower at baseline in the lines without SDCBP2 | 0.098 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[MAL2]] | C | MAL2 activity raises FUT3's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 3.79× lower at baseline in the lines without MAL2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises FUT3's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.11× lower at baseline in the lines without ATP2C2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |

### Downstream of this gene

*88 arrows, 88 of them with an alert ⚠; grade A 0, B 29, C 59. Shown: the 12 strongest; 76 more arrows (76 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | FUT3 activity raises MUC20's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.90× lower at baseline in the lines without FUT3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[FAM83E]] | B | FUT3 activity raises FAM83E's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.52× lower at baseline in the lines without FUT3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[EPS8L1]] | B | FUT3 activity raises EPS8L1's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.81× lower at baseline in the lines without FUT3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[PRRG2]] | B | FUT3 activity raises PRRG2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.53× lower at baseline in the lines without FUT3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[OCLN]] | B | FUT3 activity raises OCLN's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 4.14× lower at baseline in the lines without FUT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[IL17RE]] | B | FUT3 activity raises IL17RE's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without FUT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[ELMO3]] | B | FUT3 activity raises ELMO3's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.31× lower at baseline in the lines without FUT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[SYTL1]] | B | FUT3 activity raises SYTL1's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without FUT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[DCLK2]] | B | FUT3 activity lowers DCLK2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.05× higher at baseline in the lines without FUT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[MAPK13]] | B | FUT3 activity raises MAPK13's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.53× lower at baseline in the lines without FUT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[TMEM51-AS1]] | B | FUT3 activity raises TMEM51-AS1's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without FUT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[BNC2]] | B | FUT3 activity lowers BNC2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.83× higher at baseline in the lines without FUT3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.5, 55.8); signed map (58.1, 6.4). **Vector** length 57.8, 17.1% of its response variance represented; |z| ≥ 3 in 469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +23.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +6.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | fucosyltransferase 3 (Lewis blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,842,888-5,851,471 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD174; previously LE |
| Gene groups (HGNC) | Fucosyltransferases; Blood group antigens; CD molecules |
| Reactome | 7 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; Lewis blood group biosynthesis; Blood group systems biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P21217](https://www.uniprot.org/uniprotkb/P21217) (3-galactosyl-N-acetylglucosaminide 4-alpha-L-fucosyltransferase FUT3):

> Catalyzes the transfer of L-fucose, from a guanosine diphosphate-beta-L-fucose, to both the subterminal N-acetyl glucosamine (GlcNAc) of type 1 chain (beta-D-Gal-(1->3)-beta-D-GlcNAc) glycolipids and oligosaccharides via an alpha(1,4) linkage, and the subterminal glucose (Glc) or GlcNAc of type 2 chain (beta-D-Gal-(1->4)-beta-D-GlcNAc) oligosaccharides via an alpha(1,3) linkage, independently of the presence of terminal alpha-L-fucosyl-(1,2) moieties on the terminal galactose of these …

**Summary**, from NCBI Gene [2525](https://www.ncbi.nlm.nih.gov/gene/2525):

> The Lewis histo-blood group system comprises a set of fucosylated glycosphingolipids that are synthesized by exocrine epithelial cells and circulate in body fluids. The glycosphingolipids function in embryogenesis, tissue differentiation, tumor metastasis, inflammation, and bacterial adhesion. They are secondarily absorbed to red blood cells giving rise to their Lewis phenotype. This gene is a member of the fucosyltransferase family, which catalyzes the addition of fucose to precursor …

**Accessions** — [HGNC:4014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4014) · Entrez [2525](https://www.ncbi.nlm.nih.gov/gene/2525) · UniProt [P21217](https://www.uniprot.org/uniprotkb/P21217) · Ensembl [ENSG00000171124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171124)

## Data

Gene col 10055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10055); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10055]; `tensor/DDL_lfc|DDL_z.npy` [10055]; `embed/gene_vectors.npy` [10055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10055 or target_col == 10055). Every well: [[FUT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
