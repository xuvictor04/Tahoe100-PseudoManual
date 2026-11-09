---
symbol: "PKP3"
type: "gene"
col: 11525
ensembl_id: "ENSG00000184363"
name: "plakophilin 3"
location: "11p15.5"
module: 31
arm: "+"
pooled_cpm: 17.51
n_lines_expressing: 35
n_dd_up: 10
n_dd_down: 27
n_dd_up_clean: 6
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 36
direction_downstream: 19
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PKP3

*plakophilin 3* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.90× (z +7.7, q 6e-12, up in 15 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.49× (z +5.0, q 8e-05, up in 25 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.294× (z -15.4, q 0e+00, down in 33 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC13D]] (+0.71, fdr 7e-06), [[MISP]] (+0.58, fdr 1e-05), [[SEMA3B]] (+0.58, fdr 8e-06); moves opposite to [[CBX3]] (-0.45, fdr 2e-04), [[RCN2]] (-0.45, fdr 1e-04), [[MME]] (-0.43, fdr 4e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[C1orf116]] → it (grade B ⚠); 19 go from it, the strongest it → [[RFFL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.7 | 6e-12 | 15/24 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.5 | 2e-08 | 23/29 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +5.3 | 3e-05 | 18/32 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 8e-05 | 25/33 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.9 | 1e-04 | 17/33 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.7 | 2e-04 | 13/29 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.006 | 16/33 (SW480, A-172, …) | two highest doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.052 | 9/33 (MIA PaCa-2, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.052 | 10/33 (Hs 766T, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.085 | 16/33 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.12 | 7/33 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.294×** | -15.4 | 0e+00 | 33/33 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.303×** | -15.0 | 0e+00 | 32/33 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.308×** | -14.8 | 0e+00 | 33/33 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -10.6 | 7e-24 | 26/33 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.446×** | -10.1 | 4e-22 | 30/33 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.483×** | -9.1 | 6e-18 | 28/33 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.697×** | -6.4 | 1e-08 | 24/33 (MIA PaCa-2, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.610×** | -6.2 | 4e-08 | 20/33 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -5.7 | 7e-07 | 20/32 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.395×** | -5.5 | 2e-06 | 24/33 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -5.0 | 3e-05 | 18/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.459×** | -4.6 | 2e-04 | 21/33 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.460×** | -4.6 | 2e-04 | 23/33 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -4.5 | 3e-04 | 15/33 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.701×** | -4.5 | 3e-04 | 18/33 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.778×** | -4.5 | 3e-04 | 21/33 (HEC-1-A, NCI-H2347, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.6 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.196× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 54.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -17.2) |
| [[HEC-1-A (line)]] | alt | 32.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.282× (z -10.3) |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -10.6) |
| [[LoVo (line)]] | wt | 28.4 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.118× (z -14.2) |
| [[HT-29 (line)]] | alt | 33.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -14.2) |
| [[LS 180 (line)]] | wt | 31.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.1) |
| [[SW1417 (line)]] | alt | 47.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.6) |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.140× (z -10.6) |
| [[KATO III (line)]] | alt | 25.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 6.79 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -11.1) |
| [[A-172 (line)]] | wt | 9.75 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -9.7) |
| [[A498 (line)]] | wt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -13.8) |
| [[HS-578T (line)]] | alt | 4.55 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0717× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 52.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -11.5) |
| [[SW48 (line)]] | wt | 39.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -10.5) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13D]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MISP]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SEMA3B]] | +0.58 | +0.61 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[FAM83H]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TMEM184A]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP27]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PTK6]] | +0.54 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[GJB3]] | +0.51 | +0.58 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[EPS8L1]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[AUP1]] | +0.49 | +0.27 / +0.60 | both halves | 3e-04 |  |
| [[CLTB]] | +0.49 | +0.40 / +0.41 | both halves | 4e-05 |  |
| [[PSORS1C1]] | +0.49 | +0.53 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX3]] | -0.45 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[RCN2]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[MME]] | -0.43 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[G3BP2]] | -0.42 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[FOXJ3]] | -0.41 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[LINC00115]] | -0.41 | -0.29 / -0.33 | both halves | 3e-04 |  |
| [[ABI2]] | -0.40 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 28, C 8. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf116]] | B | C1orf116 activity raises PKP3's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.52× lower at baseline in the lines without C1orf116 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[LAD1]] | B | LAD1 activity raises PKP3's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.79× lower at baseline in the lines without LAD1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[FAM83B]] | B | FAM83B activity raises PKP3's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[GJB3]] | B | GJB3 activity raises PKP3's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 4.38× lower at baseline in the lines without GJB3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[ITGB4]] | B | ITGB4 activity raises PKP3's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.65× lower at baseline in the lines without ITGB4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[KRT16]] | B | KRT16 activity raises PKP3's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.51× lower at baseline in the lines without KRT16 | 0.007 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[DSC2]] | B | DSC2 activity raises PKP3's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 3.04× lower at baseline in the lines without DSC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[JUP]] | B | JUP activity raises PKP3's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without JUP | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[SDR16C5]] | B | SDR16C5 activity raises PKP3's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.13× lower at baseline in the lines without SDR16C5 | 0.015 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[TTC9]] | B | TTC9 activity raises PKP3's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without TTC9 | 0.019 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[CRYBG2]] | B | CRYBG2 activity raises PKP3's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without CRYBG2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[TOP2A]] | B | TOP2A activity raises PKP3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 11, C 8. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFFL]] | B | PKP3 activity raises RFFL's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without PKP3 | 0.014 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[ARHGAP27]] | B | PKP3 activity raises ARHGAP27's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without PKP3 | 0.022 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[TMBIM1]] | B | PKP3 activity raises TMBIM1's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.72× lower at baseline in the lines without PKP3 | 0.037 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[EZR]] | B | PKP3 activity raises EZR's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 2.27× lower at baseline in the lines without PKP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[PLCD3]] | B | PKP3 activity raises PLCD3's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without PKP3 | 0.047 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[ADAP1]] | B | PKP3 activity raises ADAP1's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 2.19× lower at baseline in the lines without PKP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[UNC13D]] | B | PKP3 activity raises UNC13D's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without PKP3 | 0.064 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[PLEC]] | B | PKP3 activity raises PLEC's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.72× lower at baseline in the lines without PKP3 | 0.069 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[FAM83B]] | B | PKP3 activity raises FAM83B's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 3.99× lower at baseline in the lines without PKP3 | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[SH3BP2]] | B | PKP3 activity raises SH3BP2's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without PKP3 | 0.081 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[INF2]] | B | PKP3 activity raises INF2's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without PKP3 | 0.098 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[PTK6]] | C | PKP3 activity raises PTK6's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 3.82× lower at baseline in the lines without PKP3 | 0.002 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, 56.6); signed map (-0.5, 35.9). **Vector** length 74.7, 18.8% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +7.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -2.8 | -6.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.7 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Hydroxyurea (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | plakophilin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:392,614-404,908 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo repeat containing; Plakophilins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y446](https://www.uniprot.org/uniprotkb/Q9Y446) (Plakophilin-3):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion. Required for the localization of DSG2, DSP and PKP2 to mature desmosome junctions. May also play a role in the maintenance of DSG3 protein abundance in keratinocytes (By similarity). Required for the formation of DSP-containing desmosome precursors in the cytoplasm during desmosome assembly. Also regulates the accumulation of CDH1 to mature desmosome junctions, via cAMP-dependent …

**Summary**, from NCBI Gene [11187](https://www.ncbi.nlm.nih.gov/gene/11187):

> This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This protein may act in cellular desmosome-dependent adhesion and signaling pathways. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:9025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9025) · Entrez [11187](https://www.ncbi.nlm.nih.gov/gene/11187) · UniProt [Q9Y446](https://www.uniprot.org/uniprotkb/Q9Y446) · Ensembl [ENSG00000184363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184363)

## Data

Gene col 11525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11525); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11525]; `tensor/DDL_lfc|DDL_z.npy` [11525]; `embed/gene_vectors.npy` [11525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11525 or target_col == 11525). Every well: [[PKP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
