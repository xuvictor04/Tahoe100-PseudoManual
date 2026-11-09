---
symbol: "MYT1L"
type: "gene"
col: 11822
ensembl_id: "ENSG00000186487"
name: "myelin transcription factor 1 like"
location: "2p25.3"
module: 90
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 21
direction_downstream: 7
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# MYT1L

*myelin transcription factor 1 like* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.58× (z +15.8, q 0e+00, up in 19 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.277×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.169×; ⚠ cell-cycle shift, explains ~76% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.183×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.330×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHRM5]] (+0.84, fdr 7e-06), [[VENTXP1]] (+0.83, fdr 7e-06), [[CLVS1]] (+0.79, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 7 go from it, the strongest it → [[GCNT7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.58×** | +15.8 | 0e+00 | 19/21 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.44×** | +13.2 | 2e-37 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.35×** | +10.8 | 5e-25 | 2/3 (HOP62, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.91×** | +9.3 | 2e-18 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.93×** | +7.9 | 3e-13 | 15/24 (SW480, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +7.4 | 1e-11 | 12/22 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.18×** | +5.7 | 9e-07 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.03×** | +5.2 | 2e-05 | 10/32 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.2 | 2e-05 | 6/35 (HEC-1-A, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.003 | 0/22 | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.86×** | +4.0 | 0.003 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.007 | 4/34 (SW480, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.016 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.97×** | +3.5 | 0.016 | 2/7 (SW480, HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +3.5 | 0.018 | 0/6 | top dose only | cell-cycle shift (explains ~13% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +3.2 | 0.046 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.052 | 1/14 (HEC-1-A) | all doses, flat | position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.054 | 1/10 (A-172) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.068 | 2/35 (COLO 205, RKO) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Naproxen (drug)]] 0.05 µM |  | **1.53×** | +2.9 | 0.095 | 0/5 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.277×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.169×; ⚠ cell-cycle shift, explains ~76% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.183×; ⚠ cell-cycle shift, explains ~10% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.330×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.629× | -3.2 | 0.40 | 7/31 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.742× | -3.2 | 0.40 | 5/36 (CFPAC-1, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 139 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.2) |
| [[SW480 (line)]] | alt | 1.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.72× (z +9.1) | — |
| [[A-172 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.929 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.964 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.923 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.952 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.933 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.966 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRM5]] | +0.84 | +0.79 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[VENTXP1]] | +0.83 | +0.80 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[CLVS1]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.79 | +0.58 / +0.78 | both halves | 8e-06 |  |
| [[GLRA3]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP5]] | +0.77 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.77 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[CNTNAP4]] | +0.76 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.76 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[NELL1]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.75 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[LINC02306]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 16, C 5. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises MYT1L's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.58× lower at baseline in the lines without CALCA | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[RIT2]] | B | RIT2 activity raises MYT1L's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.57× lower at baseline in the lines without RIT2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[SYT4]] | B | SYT4 activity raises MYT1L's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.57× lower at baseline in the lines without SYT4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[KCNB2]] | B | KCNB2 activity raises MYT1L's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.00× lower at baseline in the lines without KCNB2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[ASCL1]] | B | ASCL1 activity raises MYT1L's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.35× lower at baseline in the lines without ASCL1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[CGA]] | B | CGA activity raises MYT1L's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.55× lower at baseline in the lines without CGA | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[NAA11]] | B | NAA11 activity raises MYT1L's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.00× lower at baseline in the lines without NAA11 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MYT1L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AK4P3]] | B | AK4P3 activity raises MYT1L's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without AK4P3 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[SRRM4]] | B | SRRM4 activity raises MYT1L's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.37× lower at baseline in the lines without SRRM4 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[LINC02492]] | B | LINC02492 activity raises MYT1L's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without LINC02492 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[PCSK1]] | B | PCSK1 activity raises MYT1L's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.15× lower at baseline in the lines without PCSK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCNT7]] | B | MYT1L activity raises GCNT7's level | lines that do not express MYT1L (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without MYT1L | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC01811, XIRP2, ENSG00000232855; maybe low, not absent |
| [[CTDSPL2-DT]] | B | MYT1L activity raises CTDSPL2-DT's level | lines that do not express MYT1L (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without MYT1L | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01811, XIRP2, ENSG00000232855; maybe low, not absent |
| [[CLVS1]] | C | MYT1L's natural level weakens CLVS1's drug response | MYT1L's natural level across 39 lines (lineage-adjusted; a glimpse) | r -0.86, reverse -0.75; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CHRM5]] | C | MYT1L's natural level weakens CHRM5's drug response | MYT1L's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.87, reverse -0.74; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[LINC01250]] | C | MYT1L's natural level weakens LINC01250's drug response | MYT1L's natural level across 33 lines (lineage-adjusted; a glimpse) | r -0.89, reverse -0.68; direction clear | 0.001 | ⚠ tissue can mimic it; precision caveat |
| [[NOS1]] | C | MYT1L's natural level weakens NOS1's drug response | MYT1L's natural level across 39 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.81; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SLC4A10]] | C | MYT1L's natural level weakens SLC4A10's drug response | MYT1L's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.68; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.0, 30.0); signed map (34.2, 15.5). **Vector** length 33.7, 4.35% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | myelin transcription factor 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:1,789,113-2,331,664 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1106, NZF1, ZC2HC4B, ZC2H2C2 |
| Gene groups (HGNC) | Zinc fingers C2H2C-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL68](https://www.uniprot.org/uniprotkb/Q9UL68) (Myelin transcription factor 1-like protein):

> Transcription factor that plays a key role in neuronal differentiation by specifically repressing expression of non-neuronal genes during neuron differentiation. In contrast to other transcription repressors that inhibit specific lineages, mediates repression of multiple differentiation programs. Also represses expression of negative regulators of neurogenesis, such as members of the Notch signaling pathway, including HES1. The combination of three transcription factors, ASCL1, POU3F2/BRN2 and …

**Summary**, from NCBI Gene [23040](https://www.ncbi.nlm.nih.gov/gene/23040):

> This gene encodes a member of the zinc finger superfamily of transcription factors whose expression, thus far, has been found only in neuronal tissues. The encoded protein belongs to a novel class of cystein-cystein-histidine-cystein zinc finger proteins that function in the developing mammalian central nervous system. Forced expression of this gene in combination with the basic helix-loop-helix transcription factor NeuroD1 and the transcription factors POU class 3 homeobox 2 and achaete-scute …

**Accessions** — [HGNC:7623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7623) · Entrez [23040](https://www.ncbi.nlm.nih.gov/gene/23040) · UniProt [Q9UL68](https://www.uniprot.org/uniprotkb/Q9UL68) · Ensembl [ENSG00000186487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186487)

## Data

Gene col 11822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11822); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11822]; `tensor/DDL_lfc|DDL_z.npy` [11822]; `embed/gene_vectors.npy` [11822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11822 or target_col == 11822). Every well: [[MYT1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYT1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
