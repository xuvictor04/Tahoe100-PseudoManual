---
symbol: "MYB"
type: "gene"
col: 3998
ensembl_id: "ENSG00000118513"
name: "MYB proto-oncogene, transcription factor"
location: "6q23.3"
module: 44
arm: "+"
pooled_cpm: 5.94
n_lines_expressing: 26
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 32
direction_downstream: 11
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MYB

*MYB proto-oncogene, transcription factor* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.29× (z +22.8, q 0e+00, up in 10 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.709× (z -4.7, q 0.001, down in 11 of 24 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Dihydroartemisinin (drug)]] 5 µM: 0.641× (z -4.3, q 0.003, down in 6 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHDH]] (+0.77, fdr 7e-06), [[KCNE3]] (+0.72, fdr 7e-06), [[CLRN3]] (+0.70, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[RNF128]] → it (grade B ⚠); 11 go from it, the strongest it → [[JPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.29×** | +22.8 | 0e+00 | 10/18 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.72×** | +18.0 | 0e+00 | 12/19 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.15×** | +10.7 | 2e-24 | 11/22 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.98×** | +10.2 | 4e-22 | 1/4 (HT-29) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.84×** | +10.1 | 5e-22 | 7/18 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.70×** | +9.6 | 6e-20 | 8/23 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.67×** | +9.5 | 2e-19 | 9/24 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.49×** | +8.8 | 7e-17 | 7/24 (NCI-H23, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **2.40×** | +8.5 | 1e-15 | 3/13 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.26×** | +7.6 | 2e-12 | 7/17 (SW48, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.22×** | +7.2 | 4e-11 | 1/7 (HT-29) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.98×** | +6.4 | 8e-09 | 6/18 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.95×** | +6.2 | 2e-08 | 3/10 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.73×** | +5.3 | 4e-06 | 8/24 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +5.0 | 2e-05 | 6/24 (LoVo, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.0 | 2e-05 | 5/23 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.007 | 3/23 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.046 | 4/24 (BT-474, HEC-1-A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +2.9 | 0.092 | 1/16 (C-33 A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3998.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.709×** | -4.7 | 0.001 | 11/24 (COLO 205, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.641×** | -4.3 | 0.003 | 6/24 (NCI-H23, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.627×** | -4.3 | 0.003 | 15/22 (COLO 205, SHP-77, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.674×** | -3.8 | 0.018 | 7/23 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.702×** | -3.4 | 0.068 | 6/24 (COLO 205, LoVo, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | **0.710×** | -3.3 | 0.083 | 0/24 | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.721× | -3.2 | 0.12 | 13/22 (COLO 205, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 52.5 | 0 | 13 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0200× (z -14.7) |
| [[LS 180 (line)]] | wt | 44.7 | 0 | 10 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0843× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.4) |
| [[SW480 (line)]] | alt | 24.6 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.152× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.171× (z -8.9) |
| [[LoVo (line)]] | wt | 22.2 | 0 | 2 (1 ⚠) | — | [[vincristine (drug)]] 5 µM 0.0279× (z -10.6) |
| [[J82 (line)]] | alt | 2.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.37× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0615× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.136× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHDH]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[VIL1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[VSNL1]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PHGR1]] | +0.68 | +0.57 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[ST6GALNAC1]] | +0.67 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CFTR]] | +0.66 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[IL20RA]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[LGR5]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[IL17RB]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 6, C 26. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF128]] | B | RNF128 activity raises MYB's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.93× lower at baseline in the lines without RNF128 | 0.015 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[PCK1]] | B | PCK1 activity raises MYB's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.85× lower at baseline in the lines without PCK1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[TOP2A]] | B | TOP2A activity lowers MYB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOX3]] | B | TOX3 activity raises MYB's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without TOX3 | 0.064 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[ASB4]] | B | ASB4 activity raises MYB's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 2.18× lower at baseline in the lines without ASB4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D |
| [[MBNL3]] | B | MBNL3 activity raises MYB's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without MBNL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[LGR5]] | C | LGR5 activity raises MYB's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.80× lower at baseline in the lines without LGR5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises MYB's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.00× lower at baseline in the lines without HNF1A-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[LINC01814]] | C | LINC01814 activity raises MYB's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 3.36× lower at baseline in the lines without LINC01814 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises MYB's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.30× lower at baseline in the lines without TFF3 | 0.005 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises MYB's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 3.80× lower at baseline in the lines without AXIN2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[SMOC2]] | C | SMOC2 activity raises MYB's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without SMOC2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH1]] | B | MYB activity raises JPH1's level | lines that do not express MYB (24) vs lines expressing it (26) | 3.01× lower at baseline in the lines without MYB | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748 |
| [[CHDH]] | B | MYB activity raises CHDH's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without MYB | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748 |
| [[IL17RB]] | B | MYB activity raises IL17RB's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.09× lower at baseline in the lines without MYB | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748 |
| [[RNF128]] | B | MYB activity raises RNF128's level | lines that do not express MYB (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without MYB | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748 |
| [[TFF3]] | C | MYB activity raises TFF3's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.74× lower at baseline in the lines without MYB | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[SYK]] | C | MYB activity raises SYK's level | lines that do not express MYB (24) vs lines expressing it (26) | 4.33× lower at baseline in the lines without MYB | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[PPP1R1B]] | C | MYB activity raises PPP1R1B's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.51× lower at baseline in the lines without MYB | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[CDX2]] | C | MYB activity raises CDX2's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without MYB | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[KLK7]] | C | MYB activity raises KLK7's level | lines that do not express MYB (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without MYB | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[GPA33]] | C | MYB activity raises GPA33's level | lines that do not express MYB (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without MYB | 0.077 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[VIL1]] | C | MYB activity raises VIL1's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without MYB | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, 46.8); signed map (62.9, 12.8). **Vector** length 72.3, 20.2% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +18.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +4.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | +4.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +4.0 | +7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | +3.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +5.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.8 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.8 | -4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | MYB proto-oncogene, transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:135,181,308-135,219,173 (+) |
| Ensembl biotype | protein_coding |
| Also known as | c-myb |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 18 pathways, smallest: Specification of the neural plate border; Assembly of the 9+2 motile cilia; Transcriptional regulation of multiciliogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P10242](https://www.uniprot.org/uniprotkb/P10242) (Transcriptional activator Myb):

> Transcriptional activator; DNA-binding protein that specifically recognize the sequence 5'-YAAC[GT]G-3'. Plays an important role in the control of proliferation and differentiation of hematopoietic progenitor cells.

**Summary**, from NCBI Gene [4602](https://www.ncbi.nlm.nih.gov/gene/4602):

> This gene encodes a protein with three HTH DNA-binding domains that functions as a transcription regulator. This protein plays an essential role in the regulation of hematopoiesis. This gene may be aberrently expressed or rearranged or undergo translocation in leukemias and lymphomas, and is considered to be an oncogene. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:7545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7545) · Entrez [4602](https://www.ncbi.nlm.nih.gov/gene/4602) · UniProt [P10242](https://www.uniprot.org/uniprotkb/P10242) · Ensembl [ENSG00000118513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118513)

## Data

Gene col 3998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3998); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3998]; `tensor/DDL_lfc|DDL_z.npy` [3998]; `embed/gene_vectors.npy` [3998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3998 or target_col == 3998). Every well: [[MYB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
