---
symbol: "KRT19"
type: "gene"
col: 10094
ensembl_id: "ENSG00000171345"
name: "keratin 19"
location: "17q21.2"
module: 31
arm: "+"
pooled_cpm: 167.97
n_lines_expressing: 28
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 51
direction_downstream: 60
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KRT19

*keratin 19* — 17q21.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.291× (z -14.4, q 4e-44, down in 26 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLDN4]] (+0.66, fdr 7e-06), [[PTK6]] (+0.62, fdr 7e-06), [[SERPINB1]] (+0.61, fdr 1e-05); moves opposite to [[STARD7-AS1]] (-0.55, fdr 3e-05), [[NAF1]] (-0.52, fdr 3e-05), [[GARS1-DT]] (-0.51, fdr 7e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[GPRC5A]] → it (grade B ⚠); 60 go from it, the strongest it → [[EZR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.96 | 14/27 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.291×** | -14.4 | 4e-44 | 26/27 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.326×** | -13.0 | 2e-36 | 23/26 (BT-474, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.274×** | -10.7 | 3e-24 | 26/26 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.297×** | -10.0 | 2e-21 | 23/26 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.335×** | -9.0 | 2e-17 | 24/26 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.399×** | -7.3 | 4e-11 | 23/26 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -7.1 | 1e-10 | 26/26 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.430×** | -6.9 | 3e-10 | 26/26 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.443×** | -6.7 | 1e-09 | 26/26 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -6.7 | 2e-09 | 22/26 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.463×** | -6.3 | 1e-08 | 20/26 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.454×** | -6.2 | 2e-08 | 24/26 (NCI-H460, SW480, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.569×** | -4.6 | 2e-04 | 25/26 (NCI-H1792, NCI-H460, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.574×** | -4.6 | 2e-04 | 22/26 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.371×** | -3.8 | 0.006 | 21/27 (BT-474, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.650×** | -3.5 | 0.013 | 18/26 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.674×** | -3.2 | 0.033 | 21/26 (BT-474, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -3.0 | 0.057 | 17/26 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.702×** | -2.9 | 0.079 | 13/26 (HT-29, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.58 per unit of S-phase module lfc, +0.87 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 331 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.2) |
| [[COLO 205 (line)]] | alt | 251 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -15.2) |
| [[HT-29 (line)]] | alt | 356 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 212 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 311 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0864× (z -18.7) |
| [[Hs 766T (line)]] | wt | 143 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -13.9) |
| [[KATO III (line)]] | alt | 411 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0948× (z -15.9) |
| [[LS 180 (line)]] | wt | 324 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.1) |
| [[SW 900 (line)]] | alt | 83.8 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -10.8) |
| [[LoVo (line)]] | wt | 210 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 878 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -17.9) |
| [[HOP62 (line)]] | alt | 53.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.174× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 802 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.4) |
| [[HCT15 (line)]] | alt | 448 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -17.1) |
| [[SNU-423 (line)]] | alt | 185 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 296 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.5) |
| [[PANC-1 (line)]] | alt | 156 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.2) |
| [[SW480 (line)]] | alt | 231 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -11.8) |
| [[SW1417 (line)]] | alt | 313 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -13.5) |
| [[SW48 (line)]] | wt | 75.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.265× (z -8.7) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A-172 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN4]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 | STRING 613 |
| [[PTK6]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SERPINB1]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LIPH]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TMEM92]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SULT2B1]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TMPRSS4]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ABHD11]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[JUP]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 | pathway: Formation of the cornified envelope; STRING 495 |
| [[SEMA3B]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[CRYBG2]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[EZR]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD7-AS1]] | -0.55 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NAF1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GARS1-DT]] | -0.51 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[RBBP4]] | -0.49 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[GTF3C2-AS2]] | -0.49 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ZNF460-AS1]] | -0.47 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[NUP42]] | -0.47 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[SNHG22]] | -0.47 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 13, C 38. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5A activity raises KRT19's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 5.14× lower at baseline in the lines without GPRC5A | 0.003 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[LYPD3]] | B | LYPD3 activity raises KRT19's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.77× lower at baseline in the lines without LYPD3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[KRT15]] | B | KRT15 activity raises KRT19's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 4.92× lower at baseline in the lines without KRT15 | 0.008 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[JUP]] | B | JUP activity raises KRT19's level | lines that do not express JUP (16) vs lines expressing it (34) | 4.74× lower at baseline in the lines without JUP | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[SEMA3B]] | B | SEMA3B activity raises KRT19's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without SEMA3B | 0.034 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises KRT19's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PCDH1]] | B | PCDH1 activity raises KRT19's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 3.47× lower at baseline in the lines without PCDH1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[MYH14]] | B | MYH14 activity raises KRT19's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 3.77× lower at baseline in the lines without MYH14 | 0.053 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[MYO1E]] | B | MYO1E activity raises KRT19's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 4.80× lower at baseline in the lines without MYO1E | 0.067 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[SERPINB1]] | B | SERPINB1 activity raises KRT19's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 4.43× lower at baseline in the lines without SERPINB1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[LINC00589]] | B | LINC00589 activity strengthens KRT19's drug response | lines that do not express LINC00589 (14) vs lines expressing it (13) | the lines without LINC00589 respond 0.79× as strongly (z diff +2.22); strongest at Belinostat 5 µM: 0.51x vs 0.25x (z diff +4.4) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; target measured in part of the lines; artifact flags |
| [[EPHA1]] | B | EPHA1 activity raises KRT19's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 3.58× lower at baseline in the lines without EPHA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |

### Downstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 29, C 31. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EZR]] | B | KRT19 activity raises EZR's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.78× lower at baseline in the lines without KRT19 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[GPRC5A]] | B | KRT19 activity raises GPRC5A's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 4.06× lower at baseline in the lines without KRT19 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[JUP]] | B | KRT19 activity raises JUP's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 4.28× lower at baseline in the lines without KRT19 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[RHPN2]] | B | KRT19 activity raises RHPN2's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without KRT19 | 0.013 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[EPHA1]] | B | KRT19 activity raises EPHA1's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.38× lower at baseline in the lines without KRT19 | 0.019 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[SERPINB1]] | B | KRT19 activity raises SERPINB1's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 3.91× lower at baseline in the lines without KRT19 | 0.021 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[RDH13]] | B | KRT19 activity raises RDH13's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without KRT19 | 0.022 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[KRT15]] | B | KRT19 activity raises KRT15's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without KRT19 | 0.026 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[TNIK]] | B | KRT19 activity raises TNIK's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without KRT19 | 0.034 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[ABHD11]] | B | KRT19 activity raises ABHD11's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without KRT19 | 0.036 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[ITPKC]] | B | KRT19 activity raises ITPKC's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without KRT19 | 0.039 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[BIK]] | B | KRT19 activity raises BIK's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.94× lower at baseline in the lines without KRT19 | 0.041 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, 56.1); signed map (-1.4, 37.7). **Vector** length 96.2, 37.8% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Afatinib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | keratin 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,523,617-41,528,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K19, CK19, K1CS, MGC15366 |
| Gene groups (HGNC) | Keratins, type I |
| Hallmark sets | ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P08727](https://www.uniprot.org/uniprotkb/P08727) (Keratin, type I cytoskeletal 19):

> Structural component of intermediate filaments in epithelial cells. Forms intermediate filaments by heterodimerizing with the type II keratin KRT8, providing mechanical integrity to epithelial cells. Integrates into the intermediate filament network of skeletal muscle fibers alongside desmin and KRT18, contributing to force transmission (By similarity). Specifically interacts with the actin-binding domain of dystrophin, helping to link the contractile apparatus to dystrophin at the costameres …

**Summary**, from NCBI Gene [3880](https://www.ncbi.nlm.nih.gov/gene/3880):

> The protein encoded by this gene is a member of the keratin family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. The type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains. Unlike its related family members, this smallest known acidic cytokeratin is not paired with a basic cytokeratin in epithelial cells. It is specifically …

**Accessions** — [HGNC:6436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6436) · Entrez [3880](https://www.ncbi.nlm.nih.gov/gene/3880) · UniProt [P08727](https://www.uniprot.org/uniprotkb/P08727) · Ensembl [ENSG00000171345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171345)

## Data

Gene col 10094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10094); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10094]; `tensor/DDL_lfc|DDL_z.npy` [10094]; `embed/gene_vectors.npy` [10094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10094 or target_col == 10094). Every well: [[KRT19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
