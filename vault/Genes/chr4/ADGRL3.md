---
symbol: "ADGRL3"
type: "gene"
col: 7438
ensembl_id: "ENSG00000150471"
name: "adhesion G protein-coupled receptor L3"
location: "4q13.1"
module: 9
arm: "+"
pooled_cpm: 16.4
n_lines_expressing: 25
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 19
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ADGRL3

*adhesion G protein-coupled receptor L3* — 4q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.14× (z +29.8, q 0e+00, up in 16 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM: 0.746× (z -3.8, q 0.049, down in 6 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAM2]] (+0.70, fdr 7e-06), [[CRISPLD1]] (+0.69, fdr 7e-06), [[ASXL3]] (+0.68, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[GNAI1]] → it (grade B ⚠); 11 go from it, the strongest it → [[SYT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.14×** | +29.8 | 0e+00 | 16/22 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +15.8 | 0e+00 | 17/23 (NCI-H23, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +10.5 | 3e-23 | 4/17 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.19×** | +10.1 | 8e-22 | 13/23 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +8.8 | 1e-16 | 14/22 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +8.1 | 5e-14 | 5/15 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +7.1 | 8e-11 | 3/12 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.9 | 9e-05 | 4/20 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.3 | 9e-04 | 6/22 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 6/22 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 3/23 (HOP62, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.011 | 13/21 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.056 | 6/22 (J82, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Allantoin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.078 | 2/23 (NCI-H23, HS-578T) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.26×** | +3.0 | 0.099 | 1/20 (A-172) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.746×** | -3.8 | 0.049 | 6/23 (SNU-423, AN3 CA, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -3.8 | 0.049 | 11/21 (SHP-77, CHP-212, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.062 | 3/22 (KATO III, CFPAC-1, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.838× | -3.2 | 0.15 | 1/24 (NCI-H460) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.784× | -3.1 | 0.15 | 11/22 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.1 | 0.15 | 0/23 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.785× | -3.1 | 0.15 | 7/23 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 435 | 0 | 7 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.266× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.271× (z -13.6) |
| [[J82 (line)]] | alt | 9.55 | 6 | 0 | [[Clobetasol propionate (drug)]] 5 µM 9.70× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0292× (z -20.0) ⚠ toxic; cell-cycle shift, explains ~1% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -9.7) |
| [[CHP-212 (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0993× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.141× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 12.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 4.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +13.4) | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.121× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 6.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 8.61 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.88× (z +9.7) | — |
| [[NCI-H661 (line)]] | alt | 533 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.212× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 6.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +10.3) | — |
| [[SW480 (line)]] | alt | 5.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +9.2) | — |
| [[A-172 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAM2]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CRISPLD1]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[ASXL3]] | +0.68 | +0.59 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PCDH9]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[RALYL]] | +0.67 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[PCDH15]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KCNH7]] | +0.66 | +0.55 / +0.79 | both halves | 1e-05 |  |
| [[IQCM]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP25]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[GRID2]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[KCNJ6]] | +0.65 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[NKAIN2]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 3, C 16. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAI1]] | B | GNAI1 activity lowers ADGRL3's level | lines that do not express GNAI1 (10) vs lines expressing it (40) | 1.62× higher at baseline in the lines without GNAI1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: ENSG00000250158, KLF12, ELL2 |
| [[SERPINF1]] | B | SERPINF1 activity raises ADGRL3's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without SERPINF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ADGRL3's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CSMD3]] | C | CSMD3 activity raises ADGRL3's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 4.18× lower at baseline in the lines without CSMD3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[RMST]] | C | RMST activity raises ADGRL3's level | lines that do not express RMST (35) vs lines expressing it (15) | 3.26× lower at baseline in the lines without RMST | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises ADGRL3's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 3.31× lower at baseline in the lines without BRINP3 | 0.025 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises ADGRL3's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 6.28× lower at baseline in the lines without FUT9 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises ADGRL3's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 4.66× lower at baseline in the lines without CDH10 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises ADGRL3's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 3.42× lower at baseline in the lines without CDH18 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises ADGRL3's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.54× lower at baseline in the lines without KCNH7 | 0.043 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises ADGRL3's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 2.80× lower at baseline in the lines without LINC02438 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises ADGRL3's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without CDH12 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT1]] | B | ADGRL3 activity raises SYT1's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without ADGRL3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[LSAMP]] | B | ADGRL3 activity raises LSAMP's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without ADGRL3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[LMNTD1]] | B | ADGRL3 activity raises LMNTD1's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 1.69× lower at baseline in the lines without ADGRL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[CSRNP3]] | B | ADGRL3 activity raises CSRNP3's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without ADGRL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent |
| [[BRINP3]] | C | ADGRL3 activity raises BRINP3's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without ADGRL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | ADGRL3 activity raises RMST's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without ADGRL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[POU6F2]] | C | ADGRL3 activity raises POU6F2's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.17× lower at baseline in the lines without ADGRL3 | 0.062 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[RBM20]] | C | ADGRL3 activity raises RBM20's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 3.22× lower at baseline in the lines without ADGRL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[CDH18]] | C | ADGRL3 activity raises CDH18's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 2.52× lower at baseline in the lines without ADGRL3 | 0.069 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[SEMA3D]] | C | ADGRL3 activity raises SEMA3D's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 3.05× lower at baseline in the lines without ADGRL3 | 0.074 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | ADGRL3 activity raises CDH10's level | lines that do not express ADGRL3 (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without ADGRL3 | 0.098 | ⚠ within organs, on part of the lines; also absent: CDH18, GRIA2, NTNG1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.6, 33.8); signed map (41.5, 35.5). **Vector** length 58.0, 13.7% of its response variance represented; |z| ≥ 3 in 575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +29.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +15.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor L3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.1 — chr4:61,200,326-62,078,335 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0768, LEC3; previously LPHN3 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily L; Olfactomedin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAR2](https://www.uniprot.org/uniprotkb/Q9HAR2) (Adhesion G protein-coupled receptor L3):

> Orphan adhesion G protein-coupled receptor (aGPCR), which mediates synapse specificity. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors. ADGRL3 is coupled with different classes of G alpha proteins, such as G(12)/G(13), G(s), G(i) or G(q), depending on the context. Coupling to G(12)/G(13) G proteins, which mediates the activation Rho small GTPases is the most efficient. …

**Summary**, from NCBI Gene [23284](https://www.ncbi.nlm.nih.gov/gene/23284):

> This gene encodes a member of the latrophilin subfamily of G-protein coupled receptors (GPCR). Latrophilins may function in both cell adhesion and signal transduction. In experiments with non-human species, endogenous proteolytic cleavage within a cysteine-rich GPS (G-protein-coupled-receptor proteolysis site) domain resulted in two subunits (a large extracellular N-terminal cell adhesion subunit and a subunit with substantial similarity to the secretin/calcitonin family of GPCRs) being …

**Accessions** — [HGNC:20974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20974) · Entrez [23284](https://www.ncbi.nlm.nih.gov/gene/23284) · UniProt [Q9HAR2](https://www.uniprot.org/uniprotkb/Q9HAR2) · Ensembl [ENSG00000150471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150471)

## Data

Gene col 7438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7438); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7438]; `tensor/DDL_lfc|DDL_z.npy` [7438]; `embed/gene_vectors.npy` [7438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7438 or target_col == 7438). Every well: [[ADGRL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
