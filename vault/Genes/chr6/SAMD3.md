---
symbol: "SAMD3"
type: "gene"
col: 8953
ensembl_id: "ENSG00000164483"
name: "sterile alpha motif domain containing 3"
location: "6q23.1"
module: 13
arm: "+"
pooled_cpm: 27.41
n_lines_expressing: 18
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 37
direction_downstream: 44
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SAMD3

*sterile alpha motif domain containing 3* — 6q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.95× (z +9.1, q 7e-17, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +6.6, q 9e-09, up in 2 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 12.0×; ⚠ cell-cycle shift, explains ~48% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.525× (z -5.6, q 1e-05, down in 13 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM200A]] (+0.93, fdr 7e-06, ⚠ same locus), [[GPR68]] (+0.81, fdr 7e-06), [[SHANK1]] (+0.78, fdr 7e-06), [[SIGLEC15]] (+0.78, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[STING1]] → it (grade B ⚠); 44 go from it, the strongest it → [[RFTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8953.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 12.0×; ⚠ cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.1 | 7e-17 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +8.2 | 6e-14 | 2/15 (LS 180, RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.6 | 9e-09 | 2/15 (SW1417, LoVo) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +5.8 | 1e-06 | 1/13 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +3.9 | 0.011 | 5/16 (LoVo, RPMI-7951, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -5.6 | 1e-05 | 13/15 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.645×** | -5.4 | 2e-05 | 14/16 (HOP62, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.551×** | -5.2 | 4e-05 | 11/16 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -4.7 | 4e-04 | 15/16 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.588×** | -4.6 | 4e-04 | 11/15 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.595×** | -4.3 | 0.002 | 10/16 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.730×** | -3.8 | 0.011 | 7/16 (HOP62, J82, …) | all doses, flat | position effect removed |
| [[Retinoic acid (drug)]] 5 µM |  | **0.740×** | -3.7 | 0.015 | 10/16 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.655×** | -3.7 | 0.015 | 13/16 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.647×** | -3.5 | 0.025 | 8/16 (J82, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.684×** | -3.3 | 0.046 | 8/16 (Panc 03.27, J82, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.685×** | -3.3 | 0.046 | 9/16 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.690×** | -3.2 | 0.052 | 12/16 (HOP62, J82, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.052 | 6/16 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.698×** | -3.1 | 0.065 | 8/16 (LOX-IMVI, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 65.2 | 0 | 25 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.361× (z -16.0) ⚠ position not correctable · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0443× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 567 | 0 | 23 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0681× (z -20.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0742× (z -20.2) |
| [[hTERT-HPNE (line)]] | wt | 202 | 0 | 12 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0668× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 32.5 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0665× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0834× (z -10.6) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 2 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0948× (z -9.7) |
| [[LoVo (line)]] | wt | 23.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 12.0× (z +12.2) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0766× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 8.24 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.0656× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0424× (z -10.8) |
| [[SHP-77 (line)]] | alt | 85.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0873× (z -14.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 13.6 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.0736× (z -8.5) |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.140× (z -9.4) |
| [[A-427 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM200A]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | STRING 441; ⚠ same locus (0.6 kb: neighbours can correlate without regulation) |
| [[GPR68]] | +0.81 | +0.73 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SHANK1]] | +0.78 | +0.66 / +0.75 | both halves | 7e-06 | same gene group |
| [[SIGLEC15]] | +0.78 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RFX8]] | +0.77 | +0.64 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.74 | +0.64 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS6]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GDNF]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[FAM167A]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[VEPH1]] | +0.71 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ADAMTS18]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NLRP3]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 5, C 32. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STING1]] | B | STING1 activity raises SAMD3's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without STING1 | 0.034 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[NR3C1]] | B | NR3C1 activity lowers SAMD3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[CMKLR2]] | B | CMKLR2 activity raises SAMD3's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.73× lower at baseline in the lines without CMKLR2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[FAM167A]] | B | FAM167A activity raises SAMD3's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without FAM167A | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[GPR68]] | B | GPR68 activity raises SAMD3's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without GPR68 | 0.085 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[TMEM200A]] | C | TMEM200A activity raises SAMD3's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 6.89× lower at baseline in the lines without TMEM200A | 8e-05 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises SAMD3's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 4.90× lower at baseline in the lines without ADAMTS12 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises SAMD3's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 7.00× lower at baseline in the lines without NETO1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises SAMD3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.29× lower at baseline in the lines without APCDD1L | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[NLRP1]] | C | NLRP1 activity raises SAMD3's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 3.02× lower at baseline in the lines without NLRP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises SAMD3's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.35× lower at baseline in the lines without TCF4 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises SAMD3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.44× lower at baseline in the lines without ITGA11 | 0.014 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 11, C 33. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFTN1]] | B | SAMD3 activity raises RFTN1's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 3.70× lower at baseline in the lines without SAMD3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[FAM167A]] | B | SAMD3 activity raises FAM167A's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without SAMD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[STING1]] | B | SAMD3 activity raises STING1's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without SAMD3 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[DOCK2]] | B | SAMD3 activity raises DOCK2's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.32× lower at baseline in the lines without SAMD3 | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[GPR68]] | B | SAMD3 activity raises GPR68's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.07× lower at baseline in the lines without SAMD3 | 0.030 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[TSHZ3]] | B | SAMD3 activity strengthens TSHZ3's drug response | lines that do not express SAMD3 (13) vs lines expressing it (10) | the lines without SAMD3 respond 0.68× as strongly (z diff +1.18); strongest at Dinaciclib 0.05 µM: 0.46x vs 0.20x (z diff +4.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; target measured in part of the lines; artifact flags |
| [[NTNG2]] | B | SAMD3 activity raises NTNG2's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 1.97× lower at baseline in the lines without SAMD3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[RAC2]] | B | SAMD3 activity raises RAC2's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 3.43× lower at baseline in the lines without SAMD3 | 0.071 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[SNCAIP]] | B | SAMD3 activity raises SNCAIP's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without SAMD3 | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[PDE4DIPP2]] | B | SAMD3 activity raises PDE4DIPP2's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.31× lower at baseline in the lines without SAMD3 | 0.085 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[SHC3]] | B | SAMD3 activity raises SHC3's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without SAMD3 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[TMEM200A]] | C | SAMD3 activity raises TMEM200A's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 9.12× lower at baseline in the lines without SAMD3 | 5e-06 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.3, 13.9); signed map (19.6, 47.5). **Vector** length 90.6, 35.3% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective B3GALTL causes PpS* (reactome, mean cos +0.54 to 8); *O-glycosylation of TSR domain-containing proteins* (reactome, mean cos +0.54 to 8); *Degradation of the extracellular matrix* (reactome, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.8 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.1 — chr6:130,144,315-130,365,425 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA73O6.2, FLJ34032 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

UniProt [Q8N6K7](https://www.uniprot.org/uniprotkb/Q8N6K7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21574) · Entrez [154075](https://www.ncbi.nlm.nih.gov/gene/154075) · UniProt [Q8N6K7](https://www.uniprot.org/uniprotkb/Q8N6K7) · Ensembl [ENSG00000164483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164483)

## Data

Gene col 8953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8953); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8953]; `tensor/DDL_lfc|DDL_z.npy` [8953]; `embed/gene_vectors.npy` [8953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8953 or target_col == 8953). Every well: [[SAMD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
