---
symbol: "SH3BGRL2"
type: "gene"
col: 12599
ensembl_id: "ENSG00000198478"
name: "SH3 domain binding glutamate rich protein like 2"
location: "6q14.1"
module: 44
arm: "+"
pooled_cpm: 19.28
n_lines_expressing: 34
n_dd_up: 39
n_dd_down: 1
n_dd_up_clean: 32
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 36
direction_downstream: 13
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# SH3BGRL2

*SH3 domain binding glutamate rich protein like 2* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.05× (z +15.4, q 0e+00, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.759× (z -4.2, q 0.013, down in 13 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.445×, COLO 205 0.267×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H2030 0.0861×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0985×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.381×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.405×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPNT]] (+0.77, fdr 7e-06), [[SLC40A1]] (+0.72, fdr 7e-06), [[PIP5K1B]] (+0.65, fdr 1e-05); moves opposite to [[C19orf25]] (-0.53, fdr 2e-05), [[SLC10A3]] (-0.49, fdr 8e-05), [[CCM2]] (-0.48, fdr 4e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[MBNL3]] → it (grade B ⚠); 13 go from it, the strongest it → [[SELENOP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12599.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +15.4 | 0e+00 | 24/32 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +14.9 | 0e+00 | 14/29 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +13.7 | 4e-40 | 14/19 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +12.7 | 5e-35 | 18/32 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +12.0 | 5e-31 | 19/26 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +11.5 | 2e-28 | 16/32 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +9.9 | 4e-21 | 18/32 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +9.4 | 4e-19 | 15/32 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +8.9 | 5e-17 | 14/23 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +8.5 | 8e-16 | 20/30 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +6.0 | 9e-08 | 13/32 (KATO III, A-427, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +5.8 | 2e-07 | 10/31 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.7 | 4e-07 | 10/32 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.2 | 9e-06 | 7/31 (LOX-IMVI, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +5.1 | 1e-05 | 10/31 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 3e-05 | 12/31 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.9 | 3e-05 | 12/32 (AsPC-1, Panc 03.27, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 1e-04 | 6/29 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 3e-04 | 11/31 (AsPC-1, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12599.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.445×, COLO 205 0.267×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H2030 0.0861×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0985×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.381×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.405×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -4.2 | 0.013 | 13/31 (LoVo, SW48, …) | top dose only |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.817× | -3.1 | 0.50 | 3/31 (CHP-212, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 92.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 6.63 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0861× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 53.5 | 2 | 0 | [[Trametinib (drug)]] 5 µM 2.55× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 6.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +8.8) | — |
| [[KATO III (line)]] | alt | 81.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.9) |
| [[A-172 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPNT]] | +0.77 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SLC40A1]] | +0.72 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[PIP5K1B]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CDH17]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[A1CF]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MGAM2]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TM4SF4]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MUC13]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RASSF6]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[POF1B]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf25]] | -0.53 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[SLC10A3]] | -0.49 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[CCM2]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[LAT]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 31, C 5. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBNL3]] | B | MBNL3 activity raises SH3BGRL2's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 3.53× lower at baseline in the lines without MBNL3 | 0.001 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[AXIN2]] | B | AXIN2 activity raises SH3BGRL2's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 5.10× lower at baseline in the lines without AXIN2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[LINC00992]] | B | LINC00992 activity raises SH3BGRL2's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 3.09× lower at baseline in the lines without LINC00992 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises SH3BGRL2's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.46× lower at baseline in the lines without HNF1A-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[CLIC5]] | B | CLIC5 activity raises SH3BGRL2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.81× lower at baseline in the lines without CLIC5 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[LINC02331]] | B | LINC02331 activity raises SH3BGRL2's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 4.00× lower at baseline in the lines without LINC02331 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[MPP7]] | B | MPP7 activity raises SH3BGRL2's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.83× lower at baseline in the lines without MPP7 | 0.007 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[FAAH2]] | B | FAAH2 activity raises SH3BGRL2's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.17× lower at baseline in the lines without FAAH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[SELENOP]] | B | SELENOP activity raises SH3BGRL2's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.77× lower at baseline in the lines without SELENOP | 0.008 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[ERBB3]] | B | ERBB3 activity raises SH3BGRL2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.41× lower at baseline in the lines without ERBB3 | 0.012 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[TMPRSS2]] | B | TMPRSS2 activity raises SH3BGRL2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.42× lower at baseline in the lines without TMPRSS2 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TOX3]] | B | TOX3 activity raises SH3BGRL2's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.11× lower at baseline in the lines without TOX3 | 0.015 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SELENOP]] | B | SH3BGRL2 activity raises SELENOP's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without SH3BGRL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[MPP7]] | B | SH3BGRL2 activity raises MPP7's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without SH3BGRL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[SCIN]] | B | SH3BGRL2 activity raises SCIN's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without SH3BGRL2 | 0.023 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SH3BGRL2 activity raises SLC44A3-AS1's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.83× lower at baseline in the lines without SH3BGRL2 | 0.041 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[SHROOM3]] | B | SH3BGRL2 activity raises SHROOM3's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 3.06× lower at baseline in the lines without SH3BGRL2 | 0.047 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[CCSER1]] | B | SH3BGRL2 activity raises CCSER1's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 3.26× lower at baseline in the lines without SH3BGRL2 | 0.049 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[CXADR]] | B | SH3BGRL2 activity raises CXADR's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 3.97× lower at baseline in the lines without SH3BGRL2 | 0.059 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[MECOM]] | B | SH3BGRL2 activity raises MECOM's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.54× lower at baseline in the lines without SH3BGRL2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[FREM2]] | B | SH3BGRL2 activity raises FREM2's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without SH3BGRL2 | 0.082 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[MBNL3]] | B | SH3BGRL2 activity raises MBNL3's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without SH3BGRL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[SAMD12]] | C | SH3BGRL2 activity raises SAMD12's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 3.31× lower at baseline in the lines without SH3BGRL2 | 0.029 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent; co-absent with the target |
| [[EPCAM]] | C | SH3BGRL2 activity raises EPCAM's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 4.75× lower at baseline in the lines without SH3BGRL2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.0, 51.9); signed map (61.2, 3.2). **Vector** length 73.8, 16.7% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.57 to 4); *Aspirin ADME* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +8.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.7 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding glutamate rich protein like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:79,631,329-79,703,655 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

UniProt [Q9UJC5](https://www.uniprot.org/uniprotkb/Q9UJC5) carries no function annotation.

**Summary**, from NCBI Gene [83699](https://www.ncbi.nlm.nih.gov/gene/83699):

> Predicted to enable protein-macromolecule adaptor activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15567) · Entrez [83699](https://www.ncbi.nlm.nih.gov/gene/83699) · UniProt [Q9UJC5](https://www.uniprot.org/uniprotkb/Q9UJC5) · Ensembl [ENSG00000198478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198478)

## Data

Gene col 12599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12599); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12599]; `tensor/DDL_lfc|DDL_z.npy` [12599]; `embed/gene_vectors.npy` [12599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12599 or target_col == 12599). Every well: [[SH3BGRL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BGRL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
