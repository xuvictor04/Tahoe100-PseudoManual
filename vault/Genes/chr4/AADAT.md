---
symbol: "AADAT"
type: "gene"
col: 3062
ensembl_id: "ENSG00000109576"
name: "aminoadipate aminotransferase"
location: "4q33"
module: 33
arm: "+"
pooled_cpm: 6.81
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# AADAT

*aminoadipate aminotransferase* — 4q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +7.0, q 1e-09, up in 7 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.57× (z +6.0, q 4e-07, up in 16 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.733× (z -4.2, q 0.016, down in 16 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Thymol (drug)]] 5 µM: 0.812× (z -4.0, q 0.019, down in 10 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMSB15B]] (+0.70, fdr 7e-06), [[FXN]] (+0.66, fdr 7e-06), [[CHST10]] (+0.65, fdr 7e-06); moves opposite to [[TOM1L2]] (-0.59, fdr 1e-05), [[CATSPERG]] (-0.58, fdr 1e-05), [[TNXB]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MVB12B]] → it (grade B ⚠); 2 go from it, the strongest it → [[EXOG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.0 | 1e-09 | 7/12 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +6.4 | 5e-08 | 8/25 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +6.0 | 4e-07 | 16/42 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.55×** | +5.6 | 3e-06 | 12/27 (SW1417, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.32×** | +5.3 | 2e-05 | 16/42 (NCI-H460, LoVo, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.1 | 3e-05 | 15/42 (NCI-H2347, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +5.0 | 5e-05 | 16/42 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.0 | 5e-05 | 14/41 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.002 | 6/39 (NCI-H2030, RKO, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.1 | 0.002 | 4/42 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.005 | 7/40 (NCI-H1573, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.9 | 0.005 | 4/18 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.018 | 5/40 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.3 | 0.033 | 1/14 (SW480) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.31×** | +3.3 | 0.039 | 5/16 (SW1417, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.039 | 7/42 (A498, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.041 | 3/41 (NCI-H2347, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.044 | 3/42 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.068 | 6/40 (A-427, A498, …) | inconsistent across doses |  |
| [[Gallic acid (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.095 | 4/40 (NCI-H460, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.733×** | -4.2 | 0.016 | 16/37 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Thymol (drug)]] 5 µM |  | **0.812×** | -4.0 | 0.019 | 10/40 (CHP-212, PANC-1, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.753×** | -3.8 | 0.024 | 12/42 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.763×** | -3.6 | 0.037 | 5/42 (HOP62, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.767×** | -3.6 | 0.039 | 11/40 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.615×** | -3.4 | 0.058 | 11/34 (SW48, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.780×** | -3.2 | 0.098 | 14/40 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.853× | -3.1 | 0.16 | 7/40 (SW1417, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 21.5 | 0 | 3 (1 ⚠) | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0943× (z -10.5) |
| [[C32 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 6.86 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.115× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 3.50 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0757× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -17.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMSB15B]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[FXN]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[CHST10]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[RAD51D]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ALKBH8]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ZDHHC21]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[USP46]] | +0.61 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PTGFRN]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[HEATR3]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[XYLB]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOM1L2]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.58 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TNXB]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[GCC2]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[EOLA2-DT]] | -0.56 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[STX5]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TESK2]] | -0.55 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[RAB33B-AS1]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[HERC4]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ZNHIT1]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.53 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12B]] | B | MVB12B activity raises AADAT's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without MVB12B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[ZNF239]] | B | ZNF239 activity lowers AADAT's level | lines that do not express ZNF239 (8) vs lines expressing it (42) | 1.71× higher at baseline in the lines without ZNF239 | 0.051 | ⚠ within organs, on part of the lines |
| [[ZNF618]] | B | ZNF618 activity raises AADAT's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 2.27× lower at baseline in the lines without ZNF618 | 0.063 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[LEF1]] | B | LEF1 activity raises AADAT's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without LEF1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[SMBD1P]] | C | SMBD1P activity lowers AADAT's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.63× higher at baseline in the lines without SMBD1P | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXOG]] | B | AADAT activity raises EXOG's level | lines that do not express AADAT (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without AADAT | 0.072 | ⚠ within organs, on part of the lines; also absent: GGH, LINC01341, HHAT; maybe low, not absent |
| [[TTC39C]] | B | AADAT activity raises TTC39C's level | lines that do not express AADAT (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without AADAT | 0.073 | ⚠ within organs, on part of the lines; also absent: GGH, LINC01341, HHAT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.8, -36.4); signed map (-8.8, -53.7). **Vector** length 59.7, 9.14% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | +4.3 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +4.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | aminoadipate aminotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q33 — chr4:170,060,222-170,091,699 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KATII, KAT2, KYAT2 |
| Gene groups (HGNC) | Transaminases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Tryptophan catabolism; Lysine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5Z0](https://www.uniprot.org/uniprotkb/Q8N5Z0) (Kynurenine/alpha-aminoadipate aminotransferase, mitochondrial):

> Transaminase with broad substrate specificity. Has transaminase activity towards aminoadipate, kynurenine, methionine and glutamate. Shows activity also towards tryptophan, aspartate and hydroxykynurenine. Accepts a variety of oxo-acids as amino-group acceptors, with a preference for 2-oxoglutarate, 2-oxocaproic acid, phenylpyruvate and alpha-oxo-gamma-methiol butyric acid. Can also use glyoxylate as amino-group acceptor (in vitro).

**Summary**, from NCBI Gene [51166](https://www.ncbi.nlm.nih.gov/gene/51166):

> This gene encodes a protein that is highly similar to mouse and rat kynurenine aminotransferase II. The rat protein is a homodimer with two transaminase activities. One activity is the transamination of alpha-aminoadipic acid, a final step in the saccaropine pathway which is the major pathway for L-lysine catabolism. The other activity involves the transamination of kynurenine to produce kynurenine acid, the precursor of kynurenic acid which has neuroprotective properties. Several transcript …

**Accessions** — [HGNC:17929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17929) · Entrez [51166](https://www.ncbi.nlm.nih.gov/gene/51166) · UniProt [Q8N5Z0](https://www.uniprot.org/uniprotkb/Q8N5Z0) · Ensembl [ENSG00000109576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109576)

## Data

Gene col 3062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3062); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3062]; `tensor/DDL_lfc|DDL_z.npy` [3062]; `embed/gene_vectors.npy` [3062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3062 or target_col == 3062). Every well: [[AADAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AADAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
