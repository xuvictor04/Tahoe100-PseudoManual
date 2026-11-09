---
symbol: "ABHD11"
type: "gene"
col: 2718
ensembl_id: "ENSG00000106077"
name: "abhydrolase domain containing 11"
location: "7q11.23"
module: 31
arm: "+"
pooled_cpm: 6.51
n_lines_expressing: 42
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 82
direction_downstream: 2
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ABHD11

*abhydrolase domain containing 11* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +9.8, q 5e-20, up in 12 of 19 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +8.5, q 2e-15, up in 16 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.514× (z -6.6, q 2e-08, down in 19 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP3A5]] (+0.67, fdr 7e-06), [[LINC01559]] (+0.65, fdr 1e-05), [[SLC52A3]] (+0.64, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 82 arrows point to it, the strongest [[ST14]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZDHHC11B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.70×** | +9.8 | 5e-20 | 12/19 (KATO III, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.59×** | +9.1 | 4e-17 | 8/12 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.37×** | +8.6 | 2e-15 | 19/37 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.5 | 2e-15 | 16/29 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.35×** | +7.8 | 6e-13 | 4/15 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.07×** | +7.2 | 5e-11 | 18/36 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +7.2 | 5e-11 | 19/32 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.4 | 5e-06 | 14/35 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.39×** | +4.6 | 2e-04 | 11/30 (A498, SW1417, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.60×** | +4.4 | 5e-04 | 6/28 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.56×** | +4.4 | 5e-04 | 5/22 (NCI-H2347, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.55×** | +4.4 | 6e-04 | 9/37 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.043 | 6/27 (A498, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.11 | 6/30 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.514×** | -6.6 | 2e-08 | 19/38 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -5.0 | 2e-04 | 18/35 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.679×** | -3.7 | 0.037 | 11/31 (NCI-H2030, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.692×** | -3.7 | 0.037 | 11/34 (LS 180, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.725× | -3.2 | 0.13 | 11/35 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.709× | -3.2 | 0.13 | 6/38 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.545× | -3.1 | 0.13 | 14/26 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | 0.559× | -3.0 | 0.18 | 10/26 (BT-474, SW1417, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 25.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -10.5) |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0788× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.114× (z -11.9) |
| [[A-172 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP3A5]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[LINC01559]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SLC52A3]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SHH]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MISP]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[KRT18]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KRT20]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[IL1RN]] | +0.61 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[CLIC5]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[C1orf116]] | +0.61 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 81, C 1. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST14]] | B | ST14 activity raises ABHD11's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.34× lower at baseline in the lines without ST14 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ABHD11's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.38× lower at baseline in the lines without TMPRSS4 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CLDN7]] | B | CLDN7 activity raises ABHD11's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 3.10× lower at baseline in the lines without CLDN7 | 0.001 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises ABHD11's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[C1orf116]] | B | C1orf116 activity raises ABHD11's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CLDN3]] | B | CLDN3 activity raises ABHD11's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without CLDN3 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[LAD1]] | B | LAD1 activity raises ABHD11's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.92× lower at baseline in the lines without LAD1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[BSPRY]] | B | BSPRY activity raises ABHD11's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without BSPRY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[TMEM30B]] | B | TMEM30B activity raises ABHD11's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.19× lower at baseline in the lines without TMEM30B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[SLC5A1]] | B | SLC5A1 activity raises ABHD11's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.07× lower at baseline in the lines without SLC5A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[MYH14]] | B | MYH14 activity raises ABHD11's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.24× lower at baseline in the lines without MYH14 | 0.003 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[KIAA0040]] | B | KIAA0040 activity raises ABHD11's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.49× lower at baseline in the lines without KIAA0040 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC11B]] | B | ABHD11 activity raises ZDHHC11B's level | lines that do not express ABHD11 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without ABHD11 | 0.017 | ⚠ within organs, on part of the lines; also absent: E2F2, CXCL16, ABLIM2; maybe low, not absent |
| [[NRARP]] | B | ABHD11 activity raises NRARP's level | lines that do not express ABHD11 (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without ABHD11 | 0.064 | ⚠ within organs, on part of the lines; also absent: E2F2, CXCL16, ABLIM2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.2, 51.2); signed map (61.8, 7.1). **Vector** length 60.6, 11.4% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.9 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.6 | +9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,736,094-73,738,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP1226; previously WBSCR21 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFV4](https://www.uniprot.org/uniprotkb/Q8NFV4) (sn-1-specific diacylglycerol lipase ABHD11):

> Catalyzes the hydrolysis of diacylglycerol in vitro and may function as a key regulator in lipid metabolism, namely by regulating the intracellular levels of diacylglycerol. 1,2-diacyl-sn-glycerols are the preferred substrate over 1,3-diacyl-sn-glycerols (By similarity). The enzyme hydrolyzes stearate in preference to palmitate from the sn-1 position of 1,2-diacyl-sn-glycerols (By similarity). Maintains the functional lipoylation of the 2-oxoglutarate dehydrogenase complex (OGDHc) through its …

**Summary**, from NCBI Gene [83451](https://www.ncbi.nlm.nih.gov/gene/83451):

> This gene encodes a protein containing an alpha/beta hydrolase fold domain. This gene is deleted in Williams syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at 7q11.23. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:16407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16407) · Entrez [83451](https://www.ncbi.nlm.nih.gov/gene/83451) · UniProt [Q8NFV4](https://www.uniprot.org/uniprotkb/Q8NFV4) · Ensembl [ENSG00000106077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106077)

## Data

Gene col 2718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2718); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2718]; `tensor/DDL_lfc|DDL_z.npy` [2718]; `embed/gene_vectors.npy` [2718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2718 or target_col == 2718). Every well: [[ABHD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
