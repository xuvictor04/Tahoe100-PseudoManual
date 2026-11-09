---
symbol: "PRSS22"
type: "gene"
col: 60
ensembl_id: "ENSG00000005001"
name: "serine protease 22"
location: "16p13.3"
module: 73
arm: "+"
pooled_cpm: 17.22
n_lines_expressing: 22
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 55
direction_downstream: 73
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# PRSS22

*serine protease 22* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.12× (z +10.6, q 2e-23, up in 6 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.13× (z +5.4, q 5e-06, up in 5 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.534× (z -6.4, q 1e-07, down in 14 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8L1]] (+0.61, fdr 1e-05), [[VPS37B]] (+0.57, fdr 1e-05), [[MUC17]] (+0.57, fdr 1e-05); moves opposite to [[SPRYD7]] (-0.50, fdr 4e-05), [[WHAMMP3]] (-0.47, fdr 5e-04), [[POLK]] (-0.45, fdr 6e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 73 go from it, the strongest it → [[TMC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 60.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +10.6 | 2e-23 | 6/15 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.9 | 1e-16 | 15/20 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +7.6 | 4e-12 | 14/18 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.13×** | +7.5 | 1e-11 | 9/12 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +7.0 | 3e-10 | 4/15 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.9 | 4e-10 | 2/19 (Panc 03.27, PANC-1) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.13×** | +5.4 | 5e-06 | 5/20 (NCI-H2347, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +4.6 | 4e-04 | 8/20 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.3 | 0.001 | 2/20 (AsPC-1, PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 3/20 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.020 | 14/20 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.4 | 0.028 | 3/20 (AsPC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.036 | 5/20 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.52× | +3.0 | 0.11 | 1/20 (PANC-1) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 60.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.534×** | -6.4 | 1e-07 | 14/20 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.561×** | -5.9 | 1e-06 | 18/20 (SW48, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.598×** | -5.2 | 3e-05 | 14/20 (SW48, SW1417, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.581×** | -5.1 | 5e-05 | 4/20 (SW48, SW480, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.422×** | -4.6 | 5e-04 | 9/21 (SW1417, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.658×** | -4.3 | 0.002 | 16/20 (SW48, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.665×** | -4.1 | 0.003 | 9/21 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.721×** | -3.3 | 0.057 | 5/20 (LoVo, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.792×** | -3.3 | 0.057 | 4/20 (SW48, SW480, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.726×** | -3.3 | 0.062 | 5/20 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.733×** | -3.2 | 0.078 | 10/20 (SW1417, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.811× | -3.0 | 0.11 | 8/20 (SW1417, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 60. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 58.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0751× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 36.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.54× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 46.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 24.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -10.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 68.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0986× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.39× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 75.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -11.4) |
| [[SW1417 (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.389× (z -9.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 60), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8L1]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[VPS37B]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MUC17]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ST14]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[EPHA2]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[XYLT1]] | +0.55 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[KLK10]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MYO5B]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PADI1]] | +0.53 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MAP2K3]] | +0.53 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[EPS8L3]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRYD7]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[WHAMMP3]] | -0.47 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[POLK]] | -0.45 | -0.43 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 4, C 51. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises PRSS22's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.61× lower at baseline in the lines without EPS8L1 | 0.023 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[PLEKHA6]] | B | PLEKHA6 activity raises PRSS22's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 3.78× lower at baseline in the lines without PLEKHA6 | 0.050 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises PRSS22's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.40× lower at baseline in the lines without SEMA3B | 0.080 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[LRATD2]] | B | LRATD2 activity raises PRSS22's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 3.47× lower at baseline in the lines without LRATD2 | 0.091 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[TMPRSS4]] | C | TMPRSS4 activity raises PRSS22's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 11.58× lower at baseline in the lines without TMPRSS4 | 8e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises PRSS22's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 11.44× lower at baseline in the lines without TMEM30B | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[ST14]] | C | ST14 activity raises PRSS22's level | lines that do not express ST14 (32) vs lines expressing it (18) | 10.99× lower at baseline in the lines without ST14 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises PRSS22's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 9.23× lower at baseline in the lines without LAD1 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[TNFSF15]] | C | TNFSF15 activity raises PRSS22's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 9.99× lower at baseline in the lines without TNFSF15 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises PRSS22's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 8.59× lower at baseline in the lines without TNNT2 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[INAVA]] | C | INAVA activity raises PRSS22's level | lines that do not express INAVA (29) vs lines expressing it (21) | 6.80× lower at baseline in the lines without INAVA | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises PRSS22's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 9.53× lower at baseline in the lines without ANKRD22 | 1e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |

### Downstream of this gene

*73 arrows, 73 of them with an alert ⚠; grade A 0, B 19, C 54. Shown: the 12 strongest; 61 more arrows (61 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC6]] | B | PRSS22 activity raises TMC6's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 4.57× lower at baseline in the lines without PRSS22 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[KRT8]] | B | PRSS22 activity raises KRT8's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 5.01× lower at baseline in the lines without PRSS22 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[EPS8L1]] | B | PRSS22 activity raises EPS8L1's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 4.02× lower at baseline in the lines without PRSS22 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[RHOF]] | B | PRSS22 activity raises RHOF's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without PRSS22 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[PLEKHA6]] | B | PRSS22 activity raises PLEKHA6's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 4.32× lower at baseline in the lines without PRSS22 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[TNFRSF21]] | B | PRSS22 activity raises TNFRSF21's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 3.83× lower at baseline in the lines without PRSS22 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[EPHA2]] | B | PRSS22 activity raises EPHA2's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 3.87× lower at baseline in the lines without PRSS22 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[VPS37B]] | B | PRSS22 activity raises VPS37B's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without PRSS22 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[RTKN]] | B | PRSS22 activity raises RTKN's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without PRSS22 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[RDH13]] | B | PRSS22 activity raises RDH13's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.20× lower at baseline in the lines without PRSS22 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[SEMA3B]] | B | PRSS22 activity raises SEMA3B's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.98× lower at baseline in the lines without PRSS22 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[PHLDA2]] | B | PRSS22 activity raises PHLDA2's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without PRSS22 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.3, 52.3); signed map (67.6, 11.9). **Vector** length 64.3, 19.7% of its response variance represented; |z| ≥ 3 in 501 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -0.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,852,730-2,858,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TPSE1, hBSSP-4, BSSP-4, SP001LA |
| Gene groups (HGNC) | Serine proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZN4](https://www.uniprot.org/uniprotkb/Q9GZN4) (Brain-specific serine protease 4):

> Preferentially cleaves the synthetic substrate H-D-Leu-Thr-Arg-pNA compared to tosyl-Gly-Pro-Arg-pNA.

**Summary**, from NCBI Gene [64063](https://www.ncbi.nlm.nih.gov/gene/64063):

> This gene encodes a member of the trypsin family of serine proteases. The enzyme is expressed in the airways in a developmentally regulated manner. The gene is part of a cluster of serine protease genes on chromosome 16. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14368) · Entrez [64063](https://www.ncbi.nlm.nih.gov/gene/64063) · UniProt [Q9GZN4](https://www.uniprot.org/uniprotkb/Q9GZN4) · Ensembl [ENSG00000005001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005001)

## Data

Gene col 60: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 60); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 60, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 60]; `tensor/DDL_lfc|DDL_z.npy` [60]; `embed/gene_vectors.npy` [60]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 60 or target_col == 60). Every well: [[PRSS22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
