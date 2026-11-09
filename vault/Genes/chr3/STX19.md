---
symbol: "STX19"
type: "gene"
col: 10956
ensembl_id: "ENSG00000178750"
name: "syntaxin 19"
location: "3q11.2"
module: 8
arm: "+"
pooled_cpm: 2.61
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# STX19

*syntaxin 19* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +11.0, q 2e-25, up in 16 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (LS 180 0.0756×, NCI-H1573 0.142×, HT-29 0.157×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LS 180 0.0608×, KATO III 0.0536×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LS 180 0.0912×, NCI-H1573 0.144×; ⚠ cell-cycle shift, explains ~87% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.239×); [[Rosiglitazone (drug)]] 5 µM in 1 line (LoVo 0.0534×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASSF6]] (+0.68, fdr 7e-06), [[MTUS1-DT]] (+0.65, fdr 1e-05), [[HLA-V-1]] (+0.61, fdr 4e-05); moves opposite to [[BLTP2]] (-0.56, fdr 3e-05), [[GLB1L2]] (-0.55, fdr 8e-05), [[PAQR4]] (-0.55, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[GRHL2]], [[LINC02967]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.59×** | +11.0 | 2e-25 | 16/26 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +9.5 | 9e-19 | 11/22 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +8.0 | 4e-13 | 2/9 (HOP62, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +6.6 | 6e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +6.1 | 1e-07 | 10/23 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +5.4 | 6e-06 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.5 | 6e-04 | 1/13 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.0 | 0.005 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.007 | 4/22 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.8 | 0.008 | 2/14 (HOP62, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.6 | 0.016 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.4 | 0.033 | 1/15 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.033 | 1/16 (COLO 205) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +3.3 | 0.040 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.084 | 3/25 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.097 | 1/9 (NCI-H1573) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10956.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (LS 180 0.0756×, NCI-H1573 0.142×, HT-29 0.157×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LS 180 0.0608×, KATO III 0.0536×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LS 180 0.0912×, NCI-H1573 0.144×; ⚠ cell-cycle shift, explains ~87% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.239×); [[Rosiglitazone (drug)]] 5 µM in 1 line (LoVo 0.0534×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pimozide (drug)]] 5 µM |  | 0.674× | -3.2 | 0.69 | 8/39 (LOX-IMVI, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 26.1 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.0608× (z -16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 16.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.142× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 11.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.157× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 2.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0892× (z -9.1) ⚠ toxic |
| [[KATO III (line)]] | alt | 3.29 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0536× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 3.64 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0534× (z -9.6) |
| [[A-172 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.717 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.982 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.785 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.922 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.827 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.900 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.859 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.769 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.776 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.867 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.830 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.787 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.823 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF6]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MTUS1-DT]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[HLA-V-1]] | +0.61 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[LINC02967]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[C11orf52]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FMO5]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GRHL2]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FAAH2]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[FAM151B-DT]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LGALSL-DT]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[A1CF]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP2]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[GLB1L2]] | -0.55 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[PAQR4]] | -0.55 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[ARHGAP4]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[LRRC20]] | -0.55 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[RNGTT]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[COLGALT1]] | -0.53 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[TUBG1]] | -0.53 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[AP3M2]] | -0.52 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[PPM1F]] | -0.52 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[TATDN2]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL2]], [[LINC02967]] | B | GRHL2, LINC02967 activity raises STX19's level | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (16) | 2.66× lower at baseline in the lines without GRHL2, LINC02967 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[ARHGEF38]] | B | ARHGEF38 activity raises STX19's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 2.75× lower at baseline in the lines without ARHGEF38 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[BCAS1]] | B | BCAS1 activity raises STX19's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 1.95× lower at baseline in the lines without BCAS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[MACC1]] | B | MACC1 activity raises STX19's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without MACC1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[MARVELD3]] | B | MARVELD3 activity raises STX19's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without MARVELD3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[SMIM31]] | B | SMIM31 activity raises STX19's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SMIM31 | 0.019 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[MPZL3]] | B | MPZL3 activity raises STX19's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without MPZL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[RASSF6]] | B | RASSF6 activity raises STX19's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without RASSF6 | 0.028 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[TOX3]] | B | TOX3 activity raises STX19's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without TOX3 | 0.030 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[MGC32805]] | B | MGC32805 activity raises STX19's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 1.93× lower at baseline in the lines without MGC32805 | 0.034 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[LINC00992]] | B | LINC00992 activity raises STX19's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without LINC00992 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[LNX1]] | B | LNX1 activity raises STX19's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without LNX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.9, 7.9); signed map (56.0, 2.2). **Vector** length 51.7, 8.01% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:94,014,365-94,028,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21382 |
| Gene groups (HGNC) | Syntaxins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4C7](https://www.uniprot.org/uniprotkb/Q8N4C7) (Syntaxin-19):

> Plays a role in endosomal trafficking of the epidermal growth factor receptor (EGFR).

**Summary**, from NCBI Gene [415117](https://www.ncbi.nlm.nih.gov/gene/415117):

> Predicted to enable SNAP receptor activity and SNARE binding activity. Predicted to be involved in intracellular protein transport; synaptic vesicle fusion to presynaptic active zone membrane; and vesicle docking. Predicted to be located in cytoplasm and membrane. Predicted to be part of SNARE complex. Predicted to be active in endomembrane system and presynaptic active zone membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19300) · Entrez [415117](https://www.ncbi.nlm.nih.gov/gene/415117) · UniProt [Q8N4C7](https://www.uniprot.org/uniprotkb/Q8N4C7) · Ensembl [ENSG00000178750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178750)

## Data

Gene col 10956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10956); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10956]; `tensor/DDL_lfc|DDL_z.npy` [10956]; `embed/gene_vectors.npy` [10956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10956 or target_col == 10956). Every well: [[STX19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
