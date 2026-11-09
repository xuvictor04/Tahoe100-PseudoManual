---
symbol: "FAM167A"
type: "gene"
col: 7799
ensembl_id: "ENSG00000154319"
name: "family with sequence similarity 167 member A"
location: "8p23.1"
module: 13
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 33
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 23
direction_downstream: 20
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FAM167A

*family with sequence similarity 167 member A* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.42× (z +12.3, q 5e-32, up in 14 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.549× (z -5.9, q 2e-06, down in 20 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.71, fdr 7e-06), [[TMEM200A]] (+0.71, fdr 7e-06), [[SYNDIG1]] (+0.68, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TMEM200A]] → it (grade B ⚠); 20 go from it, the strongest it → [[RFTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +12.3 | 5e-32 | 14/24 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +7.4 | 3e-11 | 12/30 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.3 | 2e-05 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.8 | 2e-04 | 5/28 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.2 | 0.003 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.008 | 4/31 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.023 | 4/30 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.042 | 8/22 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.042 | 2/29 (A-172, CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.047 | 6/26 (A-172, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.36× | +3.0 | 0.14 | 3/15 (NCI-H1792, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.549×** | -5.9 | 2e-06 | 20/30 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -5.2 | 5e-05 | 17/24 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -4.5 | 0.001 | 9/28 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | **0.663×** | -4.0 | 0.006 | 3/30 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.664×** | -4.0 | 0.006 | 9/30 (A-172, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.672×** | -3.9 | 0.009 | 10/25 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -3.8 | 0.011 | 9/28 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.694×** | -3.6 | 0.024 | 13/28 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.785×** | -3.4 | 0.049 | 3/30 (hTERT-HPNE, Panc 03.27, …) | rises with dose | position effect removed |
| [[Silodosin (drug)]] 5 µM |  | **0.708×** | -3.3 | 0.062 | 7/23 (Panc 03.27, CHP-212, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.721×** | -3.2 | 0.067 | 10/27 (HOP62, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 23.1 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 37.3 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.102× (z -12.4) |
| [[A498 (line)]] | wt | 6.72 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.161× (z -8.8) |
| [[H4 (line)]] | wt | 8.64 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0541× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0514× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 5.67 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0620× (z -9.3) |
| [[A-172 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.922 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.71 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SYNDIG1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RFX8]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[GPR68]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NOL4]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[SHANK1]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[COL6A2]] | +0.62 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CYTH4]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ADAMTS18]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[NLRP3]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 20, C 3. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM200A]] | B | TMEM200A activity raises FAM167A's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.56× lower at baseline in the lines without TMEM200A | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[TNS1]] | B | TNS1 activity raises FAM167A's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.49× lower at baseline in the lines without TNS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[SAMD3]] | B | SAMD3 activity raises FAM167A's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without SAMD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[ADAMTS12]] | B | ADAMTS12 activity raises FAM167A's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without ADAMTS12 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[NAV1]] | B | NAV1 activity raises FAM167A's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without NAV1 | 0.036 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[GPR68]] | B | GPR68 activity raises FAM167A's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without GPR68 | 0.037 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[NETO1]] | B | NETO1 activity raises FAM167A's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 3.87× lower at baseline in the lines without NETO1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |
| [[DSCAM]] | B | DSCAM activity raises FAM167A's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.48× lower at baseline in the lines without DSCAM | 0.051 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[LINC01615]] | B | LINC01615 activity raises FAM167A's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 2.55× lower at baseline in the lines without LINC01615 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC |
| [[SYNDIG1]] | B | SYNDIG1 activity raises FAM167A's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without SYNDIG1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[APCDD1L]] | B | APCDD1L activity raises FAM167A's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without APCDD1L | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[PGF]] | B | PGF activity raises FAM167A's level | lines that do not express PGF (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without PGF | 0.067 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 16, C 4. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFTN1]] | B | FAM167A activity raises RFTN1's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 4.04× lower at baseline in the lines without FAM167A | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[PDE4DIPP2]] | B | FAM167A activity raises PDE4DIPP2's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without FAM167A | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[SNPH]] | B | FAM167A activity raises SNPH's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without FAM167A | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[RAC2]] | B | FAM167A activity raises RAC2's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without FAM167A | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[SPEG]] | B | FAM167A activity raises SPEG's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.86× lower at baseline in the lines without FAM167A | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[LINC00702]] | B | FAM167A activity raises LINC00702's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.47× lower at baseline in the lines without FAM167A | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[GPR68]] | B | FAM167A activity raises GPR68's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without FAM167A | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[COL6A1]] | B | FAM167A activity raises COL6A1's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 3.22× lower at baseline in the lines without FAM167A | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[SAMD3]] | B | FAM167A activity raises SAMD3's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without FAM167A | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[ADAMTS12]] | B | FAM167A activity raises ADAMTS12's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 3.72× lower at baseline in the lines without FAM167A | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[METRNL]] | B | FAM167A activity raises METRNL's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 1.72× lower at baseline in the lines without FAM167A | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[CRMP1]] | B | FAM167A activity raises CRMP1's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.26× lower at baseline in the lines without FAM167A | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.7, 13.8); signed map (19.7, 47.5). **Vector** length 57.8, 11.4% of its response variance represented; |z| ≥ 3 in 696 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NCAM1 interactions* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.2 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -0.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 167 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:11,421,476-11,475,908 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIORA-1; previously C8orf13 |
| Matched by | ensembl_id |

UniProt [Q96KS9](https://www.uniprot.org/uniprotkb/Q96KS9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:15549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15549) · Entrez [83648](https://www.ncbi.nlm.nih.gov/gene/83648) · UniProt [Q96KS9](https://www.uniprot.org/uniprotkb/Q96KS9) · Ensembl [ENSG00000154319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154319)

## Data

Gene col 7799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7799); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7799]; `tensor/DDL_lfc|DDL_z.npy` [7799]; `embed/gene_vectors.npy` [7799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7799 or target_col == 7799). Every well: [[FAM167A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM167A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
