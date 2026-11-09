---
symbol: "GJB2"
type: "gene"
col: 9124
ensembl_id: "ENSG00000165474"
name: "gap junction protein beta 2"
location: "13q12.11"
module: 109
arm: "+"
pooled_cpm: 5.18
n_lines_expressing: 29
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 21
direction_downstream: 13
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# GJB2

*gap junction protein beta 2* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +8.9, q 3e-16, up in 12 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.458× (z -6.1, q 6e-07, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXN2]] (+0.56, fdr 1e-05), [[SLC22A3]] (+0.55, fdr 9e-05), [[LAMA3]] (+0.53, fdr 3e-05); moves opposite to [[UBXN6]] (-0.51, fdr 6e-05), [[VPS41]] (-0.50, fdr 3e-05), [[MED28]] (-0.47, fdr 7e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[KLK10]] → it (grade B ⚠); 13 go from it, the strongest it → [[ABCC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +8.9 | 3e-16 | 12/22 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.55×** | +7.0 | 7e-10 | 2/8 (A498, LoVo) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.03×** | +5.5 | 6e-06 | 3/16 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +5.5 | 6e-06 | 11/25 (PANC-1, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +4.3 | 0.002 | 4/15 (HCT15, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +4.0 | 0.006 | 7/25 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.72×** | +3.9 | 0.007 | 1/11 (A498) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.69×** | +3.8 | 0.011 | 7/21 (HCT15, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.59×** | +3.6 | 0.021 | 6/25 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +3.5 | 0.027 | 14/26 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.094 | 6/25 (NCI-H1573, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -6.1 | 6e-07 | 18/26 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -4.2 | 0.007 | 15/26 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.578×** | -4.0 | 0.013 | 13/25 (HT-29, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.639×** | -3.5 | 0.063 | 8/25 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.623×** | -3.5 | 0.063 | 10/26 (SW48, HT-29, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -3.3 | 0.077 | 9/22 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -3.3 | 0.079 | 10/25 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.663×** | -3.2 | 0.090 | 11/26 (RPMI-7951, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.679× | -3.0 | 0.15 | 11/22 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 15.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -10.5) |
| [[SW48 (line)]] | wt | 45.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.189× (z -9.0) |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0514× (z -8.6) |
| [[Hs 766T (line)]] | wt | 4.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0709× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.134× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 3.34 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0426× (z -12.3) |
| [[A-172 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXN2]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SLC22A3]] | +0.55 | +0.48 / +0.37 | both halves | 9e-05 |  |
| [[LAMA3]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[TNS4]] | +0.53 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[TIAM1]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[FUT4]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[EFNB2]] | +0.51 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[RAPH1]] | +0.51 | +0.60 / +0.36 | both halves | 9e-05 |  |
| [[SGMS2]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[LRCH1]] | +0.51 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[GFOD1]] | +0.50 | +0.50 / +0.43 | both halves | 4e-05 |  |
| [[ANO1]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN6]] | -0.51 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[VPS41]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MED28]] | -0.47 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[C11orf54]] | -0.47 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[PPP1R3E]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ATF6B]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PFDN5]] | -0.44 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[ATG14]] | -0.44 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[EXOC3]] | -0.44 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[ADAM20P1]] | -0.43 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SPATA24]] | -0.43 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[C8orf44-SGK3]] | -0.43 | -0.35 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 14, C 7. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLK10]] | B | KLK10 activity raises GJB2's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.83× lower at baseline in the lines without KLK10 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[TRIM15]] | B | TRIM15 activity raises GJB2's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 3.88× lower at baseline in the lines without TRIM15 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[GJB3]] | B | GJB3 activity raises GJB2's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.34× lower at baseline in the lines without GJB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[LAD1]] | B | LAD1 activity raises GJB2's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without LAD1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises GJB2's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 2.39× lower at baseline in the lines without SEPTIN9-DT | 0.049 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[ABCC3]] | B | ABCC3 activity raises GJB2's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without ABCC3 | 0.049 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[KRT19]] | B | KRT19 activity raises GJB2's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.27× lower at baseline in the lines without KRT19 | 0.078 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[PDE9A]] | B | PDE9A activity raises GJB2's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.00× lower at baseline in the lines without PDE9A | 0.086 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[SERPINB5]] | B | SERPINB5 activity strengthens GJB2's drug response | lines that do not express SERPINB5 (14) vs lines expressing it (12) | the lines without SERPINB5 respond 0.91× as strongly (z diff +0.04); strongest at Panobinostat 0.5 µM: 0.78x vs 0.28x (z diff +4.4) | 0.086 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; target measured in part of the lines; both ways; artifact flags |
| [[SLC22A3]] | B | SLC22A3 activity strengthens GJB2's drug response | lines that do not express SLC22A3 (13) vs lines expressing it (13) | the lines without SLC22A3 respond 0.51× as strongly (z diff +0.98); strongest at Panobinostat 0.5 µM: 0.79x vs 0.30x (z diff +3.5) | 0.089 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA; target measured in part of the lines; artifact flags |
| [[TGFA]] | B | TGFA activity raises GJB2's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without TGFA | 0.094 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[HDAC6]] | B | HDAC6 activity raises GJB2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC3]] | B | GJB2 activity raises ABCC3's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 2.46× lower at baseline in the lines without GJB2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[SH3YL1]] | B | GJB2 activity raises SH3YL1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without GJB2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[KRT18]] | B | GJB2 activity raises KRT18's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without GJB2 | 0.031 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[CNKSR2]] | B | GJB2 activity lowers CNKSR2's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.69× higher at baseline in the lines without GJB2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[SEPTIN9-DT]] | B | GJB2 activity raises SEPTIN9-DT's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without GJB2 | 0.039 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[S100A11]] | B | GJB2 activity raises S100A11's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without GJB2 | 0.043 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[HSDL1]] | B | GJB2 activity lowers HSDL1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.21× higher at baseline in the lines without GJB2 | 0.052 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[DLX1]] | B | GJB2 activity lowers DLX1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.80× higher at baseline in the lines without GJB2 | 0.055 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[PLEK2]] | B | GJB2 activity raises PLEK2's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 3.43× lower at baseline in the lines without GJB2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[KLF13]] | B | GJB2 activity raises KLF13's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without GJB2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[PLEKHA6]] | B | GJB2 activity raises PLEKHA6's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without GJB2 | 0.094 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[LRCH1]] | B | GJB2 activity raises LRCH1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without GJB2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.358). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 48.5); signed map (5.4, 35.6). **Vector** length 56.1, 13.1% of its response variance represented; |z| ≥ 3 in 621 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.1 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +3.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +3.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | gap junction protein beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:20,187,463-20,192,938 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CX26, NSRD1; previously DFNB1, DFNA3 |
| Gene groups (HGNC) | Gap junction proteins |
| Reactome | 8 pathways, smallest: Oligomerization of connexins into connexons; Transport of connexins along the secretory pathway; Transport of connexons to the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P29033](https://www.uniprot.org/uniprotkb/P29033) (Gap junction beta-2 protein):

> Structural component of gap junctions. Gap junctions are dodecameric channels that connect the cytoplasm of adjoining cells. They are formed by the docking of two hexameric hemichannels, one from each cell membrane. Small molecules and ions diffuse from one cell to a neighboring cell via the central pore.

**Summary**, from NCBI Gene [2706](https://www.ncbi.nlm.nih.gov/gene/2706):

> This gene encodes a member of the gap junction protein family (gap junction beta 2) but is more commonly known as connexin 26. The gap junctions were first characterized by electron microscopy as regionally specialized structures on plasma membranes of contacting adherent cells. These structures were shown to consist of cell-to-cell channels that facilitate the transfer of ions and small molecules between cells. Connexins form hexameric channels in the plasma membrane which regulate passage of …

**Accessions** — [HGNC:4284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4284) · Entrez [2706](https://www.ncbi.nlm.nih.gov/gene/2706) · UniProt [P29033](https://www.uniprot.org/uniprotkb/P29033) · Ensembl [ENSG00000165474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165474)

## Data

Gene col 9124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9124); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9124]; `tensor/DDL_lfc|DDL_z.npy` [9124]; `embed/gene_vectors.npy` [9124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9124 or target_col == 9124). Every well: [[GJB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GJB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
