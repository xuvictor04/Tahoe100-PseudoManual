---
symbol: "TMPRSS4"
type: "gene"
col: 6043
ensembl_id: "ENSG00000137648"
name: "transmembrane serine protease 4"
location: "11q23.3"
module: 31
arm: "+"
pooled_cpm: 49.81
n_lines_expressing: 17
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 155
direction_downstream: 237
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TMPRSS4

*transmembrane serine protease 4* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +9.3, q 7e-18, up in 0 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.65× (z +7.0, q 4e-10, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.395× (z -9.2, q 2e-17, down in 15 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM45B]] (+0.83, fdr 7e-06), [[HS3ST1]] (+0.78, fdr 7e-06), [[TC2N]] (+0.77, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 155 arrows point to it, the strongest [[LINC03041]] → it (grade B ⚠); 237 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.3 | 7e-18 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.2 | 6e-14 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +7.0 | 4e-10 | 12/15 (Panc 03.27, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.6 | 5e-04 | 13/16 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.013 | 13/15 (SW48, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.039 | 0/15 | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.91×** | +3.5 | 0.039 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.90×** | +3.4 | 0.039 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +3.4 | 0.039 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.063 | 11/15 (SW48, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.081 | 4/15 (SW1417, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.395×** | -9.2 | 2e-17 | 15/15 (CFPAC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.440×** | -8.2 | 1e-13 | 14/15 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.457×** | -7.5 | 1e-11 | 15/15 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.492×** | -7.1 | 2e-10 | 15/15 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -6.8 | 9e-10 | 15/15 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.523×** | -6.5 | 1e-08 | 15/15 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.549×** | -6.0 | 2e-07 | 11/15 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.509×** | -5.8 | 5e-07 | 9/15 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.709×** | -4.8 | 8e-05 | 12/15 (NCI-H1573, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -4.5 | 4e-04 | 14/15 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.586×** | -4.5 | 4e-04 | 10/16 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.724×** | -4.5 | 4e-04 | 7/15 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.682×** | -3.8 | 0.006 | 0/15 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -3.8 | 0.007 | 11/15 (SW48, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.697×** | -3.6 | 0.012 | 5/15 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.676×** | -3.4 | 0.026 | 0/15 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 409 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -27.9) |
| [[SW48 (line)]] | wt | 76.7 | 1 | 12 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 5.68× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -18.9) |
| [[COLO 205 (line)]] | alt | 756 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0351× (z -37.6) |
| [[LoVo (line)]] | wt | 57.0 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -20.3) |
| [[KATO III (line)]] | alt | 453 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0380× (z -34.6) |
| [[Panc 03.27 (line)]] | alt | 90.7 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.61× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -20.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.0) |
| [[LS 180 (line)]] | wt | 107 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0457× (z -28.3) |
| [[HEC-1-A (line)]] | alt | 36.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.3) |
| [[HT-29 (line)]] | alt | 64.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0825× (z -22.7) |
| [[NCI-H2347 (line)]] | alt | 76.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.8) |
| [[SW1417 (line)]] | alt | 169 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 31.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.5) |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0867× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.79 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM45B]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.78 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[FAM83E]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLC5A1]] | +0.75 | +0.72 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[CRYBG2]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[FA2H]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[SULT2B1]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MPZL2]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[LIPH]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*155 arrows, 155 of them with an alert ⚠; grade A 0, B 16, C 139. Shown: the 12 strongest; 143 more arrows (143 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03041]] | B | LINC03041 activity lowers TMPRSS4's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 7.23× higher at baseline in the lines without LINC03041 | 0.024 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises TMPRSS4's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.61× lower at baseline in the lines without PLEKHG1 | 0.034 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[B4GALNT3]] | B | B4GALNT3 activity raises TMPRSS4's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 4.24× lower at baseline in the lines without B4GALNT3 | 0.038 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[SRMS]] | B | SRMS activity raises TMPRSS4's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without SRMS | 0.041 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[MYO1D]] | B | MYO1D activity raises TMPRSS4's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.34× lower at baseline in the lines without MYO1D | 0.042 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises TMPRSS4's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.75× lower at baseline in the lines without TJP2 | 0.043 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ABCC3]] | B | ABCC3 activity raises TMPRSS4's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.82× lower at baseline in the lines without ABCC3 | 0.043 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ZNF860]] | B | ZNF860 activity raises TMPRSS4's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 3.95× lower at baseline in the lines without ZNF860 | 0.051 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[JUP]] | B | JUP activity raises TMPRSS4's level | lines that do not express JUP (16) vs lines expressing it (34) | 4.06× lower at baseline in the lines without JUP | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[EPS8L1]] | B | EPS8L1 activity raises TMPRSS4's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.57× lower at baseline in the lines without EPS8L1 | 0.058 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises TMPRSS4's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 4.02× lower at baseline in the lines without GRHL3 | 0.083 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises TMPRSS4's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.72× lower at baseline in the lines without SEMA3B | 0.083 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |

### Downstream of this gene

*237 arrows, 237 of them with an alert ⚠; grade A 0, B 94, C 143. Shown: the 12 strongest; 225 more arrows (225 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | TMPRSS4 activity raises EPS8L1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.63× lower at baseline in the lines without TMPRSS4 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[JUP]] | B | TMPRSS4 activity raises JUP's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 7.31× lower at baseline in the lines without TMPRSS4 | 5e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ITPKC]] | B | TMPRSS4 activity raises ITPKC's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.77× lower at baseline in the lines without TMPRSS4 | 6e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[KPNA7]] | B | TMPRSS4 activity raises KPNA7's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.43× lower at baseline in the lines without TMPRSS4 | 8e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[FAM83E]] | B | TMPRSS4 activity raises FAM83E's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 5.16× lower at baseline in the lines without TMPRSS4 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[PTK2B]] | B | TMPRSS4 activity raises PTK2B's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.98× lower at baseline in the lines without TMPRSS4 | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TMC6]] | B | TMPRSS4 activity raises TMC6's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.50× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TJP2]] | B | TMPRSS4 activity raises TJP2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.10× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[RDH13]] | B | TMPRSS4 activity raises RDH13's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without TMPRSS4 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ELMO3]] | B | TMPRSS4 activity raises ELMO3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.87× lower at baseline in the lines without TMPRSS4 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ARHGAP27]] | B | TMPRSS4 activity raises ARHGAP27's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.12× lower at baseline in the lines without TMPRSS4 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ABHD11]] | B | TMPRSS4 activity raises ABHD11's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.38× lower at baseline in the lines without TMPRSS4 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.878). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 55.3); signed map (58.2, 8.2). **Vector** length 99.7, 47.9% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +3.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -4.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane serine protease 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,077,012-118,125,510 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMPRSS3, MT-SP2, CAP2 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRS4](https://www.uniprot.org/uniprotkb/Q9NRS4) (Transmembrane protease serine 4):

> Plasma membrane-anchored serine protease that directly induces processing of pro-uPA/PLAU into the active form through proteolytic activity. Involved in necroptotic cell death by mediating cleavage and maturation of SIGLEC12, the effector protein that mediates plasma membrane rupture (cytolysis). Seems to be capable of activating ENaC (By similarity).; (Microbial infection) In gut epithelial cells, facilitates human coronavirus SARS-CoV-2 infection through, at least, the cleavage of coronavirus …

**Summary**, from NCBI Gene [56649](https://www.ncbi.nlm.nih.gov/gene/56649):

> This gene encodes a member of the serine protease family. Serine proteases are known to be involved in a variety of biological processes, whose malfunction often leads to human diseases and disorders. This gene was identified as a gene overexpressed in pancreatic carcinoma. The encoded protein is membrane bound with a N-terminal anchor sequence and a glycosylated extracellular region containing the serine protease domain. The protein has been found to promote SARS-CoV-2 entry into host cells. …

**Accessions** — [HGNC:11878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11878) · Entrez [56649](https://www.ncbi.nlm.nih.gov/gene/56649) · UniProt [Q9NRS4](https://www.uniprot.org/uniprotkb/Q9NRS4) · Ensembl [ENSG00000137648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137648)

## Data

Gene col 6043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6043); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6043]; `tensor/DDL_lfc|DDL_z.npy` [6043]; `embed/gene_vectors.npy` [6043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6043 or target_col == 6043). Every well: [[TMPRSS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMPRSS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
