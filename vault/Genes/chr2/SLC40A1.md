---
symbol: "SLC40A1"
type: "gene"
col: 6180
ensembl_id: "ENSG00000138449"
name: "solute carrier family 40 member 1"
location: "2q32.2"
module: 44
arm: "+"
pooled_cpm: 7.7
n_lines_expressing: 22
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 49
direction_downstream: 84
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# SLC40A1

*solute carrier family 40 member 1* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.73× (z +12.8, q 6e-35, up in 17 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.532× (z -5.7, q 7e-06, down in 16 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM31]] (+0.75, fdr 7e-06), [[BCL2L15]] (+0.75, fdr 7e-06), [[PRR15]] (+0.74, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[TRIM2]] → it (grade B ⚠); 84 go from it, the strongest it → [[PELI1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.73×** | +12.8 | 6e-35 | 17/19 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +11.2 | 1e-26 | 2/7 (NCI-H2347, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.34×** | +10.9 | 3e-25 | 4/15 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +9.4 | 9e-19 | 2/12 (BT-474, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.75×** | +9.1 | 7e-18 | 16/19 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +7.6 | 2e-12 | 12/20 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +7.1 | 1e-10 | 12/19 (SW 900, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +6.2 | 3e-08 | 9/20 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +6.0 | 2e-07 | 11/20 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.7 | 7e-07 | 4/18 (A549, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.57×** | +4.9 | 6e-05 | 9/19 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **2.66×** | +4.6 | 2e-04 | 8/18 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.65×** | +4.3 | 6e-04 | 12/19 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.001 | 3/19 (AsPC-1, LoVo, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.006 | 10/18 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.032 | 8/19 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.041 | 9/19 (AsPC-1, LoVo, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.066 | 1/14 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -5.7 | 7e-06 | 16/19 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -4.9 | 3e-04 | 11/20 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.667×** | -3.7 | 0.046 | 12/19 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -3.5 | 0.066 | 8/19 (NCI-H1792, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -3.4 | 0.076 | 8/19 (SW 900, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.708× | -3.1 | 0.15 | 10/20 (HT-29, KATO III, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.706× | -3.1 | 0.15 | 7/20 (SW 900, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 68.3 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.193× (z -11.0) |
| [[KATO III (line)]] | alt | 67.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -13.7) |
| [[COLO 205 (line)]] | alt | 86.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -15.8) |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 5.97 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.43× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0576× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 6.73 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.88× (z +10.2) | — |
| [[LoVo (line)]] | wt | 6.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 5.34 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.76× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 6.03 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0857× (z -9.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM31]] | +0.75 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.75 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[PRR15]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MUC13]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SH3BGRL2]] | +0.72 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[PLEKHG6]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[POF1B]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[TJP3]] | +0.69 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[C4orf19]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[BCAS1]] | +0.68 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[UGT1A6]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TMPRSS3]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 6, C 43. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM2]] | B | TRIM2 activity raises SLC40A1's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without TRIM2 | 0.023 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[PLCH1]] | B | PLCH1 activity raises SLC40A1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.31× lower at baseline in the lines without PLCH1 | 0.035 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HNMT]] | B | HNMT activity raises SLC40A1's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.98× lower at baseline in the lines without HNMT | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[BDKRB2]] | B | BDKRB2 activity raises SLC40A1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without BDKRB2 | 0.076 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[SELENOP]] | B | SELENOP activity raises SLC40A1's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without SELENOP | 0.079 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers SLC40A1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[TOX3]] | C | TOX3 activity raises SLC40A1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.54× lower at baseline in the lines without TOX3 | 0.013 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[RGCC]] | C | RGCC activity raises SLC40A1's level | lines that do not express RGCC (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without RGCC | 0.016 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises SLC40A1's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.30× lower at baseline in the lines without MMP7 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[RASSF6]] | C | RASSF6 activity raises SLC40A1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without RASSF6 | 0.019 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6; co-absent with the target |
| [[ALDH1A1]] | C | ALDH1A1 activity raises SLC40A1's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 3.48× lower at baseline in the lines without ALDH1A1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[BCAS1]] | C | BCAS1 activity raises SLC40A1's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.96× lower at baseline in the lines without BCAS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ; co-absent with the target |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 33, C 51. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PELI1]] | B | SLC40A1 activity raises PELI1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without SLC40A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[FGD3]] | B | SLC40A1 activity raises FGD3's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without SLC40A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[FMO5]] | B | SLC40A1 activity raises FMO5's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without SLC40A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[GCOM1]] | B | SLC40A1 activity raises GCOM1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without SLC40A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[HNMT]] | B | SLC40A1 activity raises HNMT's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without SLC40A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[DYRK2]] | B | SLC40A1 activity raises DYRK2's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.39× lower at baseline in the lines without SLC40A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[GALM]] | B | SLC40A1 activity raises GALM's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without SLC40A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[ELF3-AS1]] | B | SLC40A1 activity raises ELF3-AS1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without SLC40A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[SCIN]] | B | SLC40A1 activity raises SCIN's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without SLC40A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[PLCH1]] | B | SLC40A1 activity raises PLCH1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without SLC40A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[LNX1]] | B | SLC40A1 activity raises LNX1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.59× lower at baseline in the lines without SLC40A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[PLEKHA7]] | B | SLC40A1 activity raises PLEKHA7's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.23× lower at baseline in the lines without SLC40A1 | 0.015 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.9, 52.1); signed map (61.1, 3.4). **Vector** length 60.0, 17.6% of its response variance represented; |z| ≥ 3 in 514 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.55 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.55 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +9.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -2.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 40 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,560,590-189,583,758 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MTP1, IREG1, FPN1, HFE4, FPN; previously SLC11A3 |
| Gene groups (HGNC) | Solute carrier family 40 |
| Reactome | 6 pathways, smallest: Metal ion SLC transporters; Iron uptake and transport; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP59](https://www.uniprot.org/uniprotkb/Q9NP59) (Ferroportin):

> Transports Fe(2+) from the inside of a cell to the outside of the cell, playing a key role for maintaining systemic iron homeostasis. Transports iron from intestinal, splenic, hepatic cells, macrophages and erythrocytes into the blood to provide iron to other tissues (By similarity). Controls therefore dietary iron uptake, iron recycling by macrophages and erythrocytes, and release of iron stores in hepatocytes (By similarity). When iron is in excess in serum, circulating HAMP/hepcidin levels …

**Summary**, from NCBI Gene [30061](https://www.ncbi.nlm.nih.gov/gene/30061):

> The protein encoded by this gene is a cell membrane protein that may be involved in iron export from duodenal epithelial cells. Defects in this gene are a cause of hemochromatosis type 4 (HFE4). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10909) · Entrez [30061](https://www.ncbi.nlm.nih.gov/gene/30061) · UniProt [Q9NP59](https://www.uniprot.org/uniprotkb/Q9NP59) · Ensembl [ENSG00000138449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138449)

## Data

Gene col 6180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6180); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6180]; `tensor/DDL_lfc|DDL_z.npy` [6180]; `embed/gene_vectors.npy` [6180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6180 or target_col == 6180). Every well: [[SLC40A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC40A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
