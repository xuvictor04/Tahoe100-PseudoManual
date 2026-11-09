---
symbol: "VWA2"
type: "gene"
col: 9194
ensembl_id: "ENSG00000165816"
name: "von Willebrand factor A domain containing 2"
location: "10q25.3"
module: 27
arm: "+"
pooled_cpm: 3.22
n_lines_expressing: 14
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 42
direction_downstream: 68
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# VWA2

*von Willebrand factor A domain containing 2* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.49× (z +10.2, q 1e-21, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.97× (z +6.8, q 2e-09, up in 5 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.516× (z -4.7, q 0.002, down in 5 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1]] (+0.87, fdr 7e-06), [[SKAP1]] (+0.81, fdr 7e-06), [[GJB1]] (+0.81, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[SKAP1]] → it (grade C ⚠); 68 go from it, the strongest it → [[ZNF860]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.49×** | +10.2 | 1e-21 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +9.5 | 6e-19 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +7.0 | 5e-10 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +6.8 | 2e-09 | 5/11 (SW1417, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.4 | 1e-08 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.28×** | +5.8 | 6e-07 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +5.3 | 1e-05 | 1/8 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.33×** | +4.3 | 0.002 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.8 | 0.009 | 0/9 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.7 | 0.010 | 1/5 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.72×** | +3.7 | 0.012 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.012 | 0/11 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.01×** | +3.5 | 0.020 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.023 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.046 | 2/9 (NCI-H2347, HCT15) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.52×** | +3.0 | 0.098 | 0/7 | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.52×** | +3.0 | 0.098 | 0/9 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -4.7 | 0.002 | 5/10 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.665×** | -4.1 | 0.013 | 4/11 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.594×** | -3.7 | 0.042 | 2/11 (HCT15, HT-29) | all doses, stronger at high dose | position effect removed |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | 0.644× | -3.1 | 0.25 | 3/11 (COLO 205, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.653× | -3.0 | 0.29 | 6/11 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.9 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0701× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.168× (z -14.8) |
| [[A-172 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1]] | +0.87 | +0.83 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[SKAP1]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.80 | +0.81 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ADGRG5]] | +0.80 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PROX1-AS1]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[IGFL4]] | +0.77 | +0.77 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[KCNH8]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[FGD5]] | +0.74 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NKD1]] | +0.74 | +0.66 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 0, C 42. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SKAP1]] | C | SKAP1 activity raises VWA2's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.72× lower at baseline in the lines without SKAP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises VWA2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.01× lower at baseline in the lines without SLC5A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises VWA2's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.30× lower at baseline in the lines without LINC03040 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[PSG1]] | C | PSG1 activity raises VWA2's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.45× lower at baseline in the lines without PSG1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[ABO]] | C | ABO activity raises VWA2's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without ABO | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises VWA2's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without TNFRSF14-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises VWA2's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without TNNT2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises VWA2's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.43× lower at baseline in the lines without MACC1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[TSPOAP1]] | C | TSPOAP1 activity raises VWA2's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.96× lower at baseline in the lines without TSPOAP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises VWA2's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 3.48× lower at baseline in the lines without KRT5 | 0.009 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[ILDR1]] | C | ILDR1 activity raises VWA2's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 2.21× lower at baseline in the lines without ILDR1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1; co-absent with the target |
| [[KCNE3]] | C | KCNE3 activity raises VWA2's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.87× lower at baseline in the lines without KCNE3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |

### Downstream of this gene

*68 arrows, 68 of them with an alert ⚠; grade A 0, B 14, C 54. Shown: the 12 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | VWA2 activity raises ZNF860's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 2.40× lower at baseline in the lines without VWA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[ZNRF3]] | B | VWA2 activity raises ZNRF3's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 3.04× lower at baseline in the lines without VWA2 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | VWA2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 0.71× the cells of the other lines | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | VWA2 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 0.86× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[TLDC2]] | B | VWA2 activity raises TLDC2's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 2.21× lower at baseline in the lines without VWA2 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[VILL]] | B | VWA2 activity raises VILL's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 2.05× lower at baseline in the lines without VWA2 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[SCN5A]] | B | VWA2 activity raises SCN5A's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 1.79× lower at baseline in the lines without VWA2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | VWA2 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 1.17× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| cells under [[Terfenadine (drug)]] 5 µM | B | VWA2 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 0.84× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM | B | VWA2 activity lowers the cells' numbers under Gallic acid (hydrate) 0.05 µM (makes them more sensitive) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 1.23× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| cells under [[Omeprazole (drug)]] 5 µM | B | VWA2 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 1.18× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | VWA2 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 0.71× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.1, 44.7); signed map (63.2, 14.2). **Vector** length 43.7, 16.3% of its response variance represented; |z| ≥ 3 in 306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +2.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.8 | +1.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -3.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | von Willebrand factor A domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:114,239,254-114,294,489 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45857, FLJ16213, CCSP-2, AMACO, NET42 |
| Matched by | ensembl_id |

UniProt [Q5GFL6](https://www.uniprot.org/uniprotkb/Q5GFL6) carries no function annotation.

**Summary**, from NCBI Gene [340706](https://www.ncbi.nlm.nih.gov/gene/340706):

> This gene encodes a member of the von Willebrand factor A-like domain protein superfamily. The encoded protein is localized to the extracellular matrix and may serve as a structural component in basement membranes or in anchoring structures on scaffolds of collagen VII or fibrillin. This gene has been linked to type 1A diabetes and is a candidate serological marker for colon cancer. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:24709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24709) · Entrez [340706](https://www.ncbi.nlm.nih.gov/gene/340706) · UniProt [Q5GFL6](https://www.uniprot.org/uniprotkb/Q5GFL6) · Ensembl [ENSG00000165816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165816)

## Data

Gene col 9194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9194); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9194]; `tensor/DDL_lfc|DDL_z.npy` [9194]; `embed/gene_vectors.npy` [9194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9194 or target_col == 9194). Every well: [[VWA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VWA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
