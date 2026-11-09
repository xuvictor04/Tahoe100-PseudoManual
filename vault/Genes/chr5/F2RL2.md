---
symbol: "F2RL2"
type: "gene"
col: 8905
ensembl_id: "ENSG00000164220"
name: "coagulation factor II thrombin receptor like 2"
location: "5q13.3"
module: 19
arm: "+"
pooled_cpm: 2.15
n_lines_expressing: 18
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# F2RL2

*coagulation factor II thrombin receptor like 2* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.01× (z +11.6, q 2e-28, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.05× (z +5.9, q 6e-07, up in 8 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Asciminib (drug)]] 0.5 µM: 0.518× (z -3.8, q 0.048, down in 3 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0823×, H4 0.155×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.187×, NCI-H460 0.260×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.337×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCKAP5]] (+0.62, fdr 1e-05), [[PAK3]] (+0.59, fdr 1e-05), [[COL4A6]] (+0.59, fdr 1e-05); moves opposite to [[RAB27A]] (-0.48, fdr 2e-04), [[FAM76B]] (-0.45, fdr 2e-04), [[UGP2]] (-0.45, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SIRLNT]] → it (grade C ⚠); 12 go from it, the strongest it → [[CREB5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.01×** | +11.6 | 2e-28 | 1/4 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.26×** | +11.5 | 3e-28 | 5/9 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.49×** | +9.1 | 1e-17 | 3/6 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +5.9 | 6e-07 | 8/15 (PANC-1, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.58×** | +5.5 | 4e-06 | 8/12 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +5.3 | 8e-06 | 2/9 (A498, NCI-H2030) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.57×** | +5.3 | 1e-05 | 2/10 (NCI-H1792, A498) | top dose only | cell-cycle shift (explains ~6% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.84×** | +4.8 | 1e-04 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +4.3 | 9e-04 | 0/15 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +4.3 | 0.001 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.07×** | +4.2 | 0.001 | 1/11 (LOX-IMVI) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +4.1 | 0.002 | 1/10 (LOX-IMVI) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.04×** | +4.1 | 0.002 | 3/10 (A498, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +3.6 | 0.011 | 5/12 (H4, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.5 | 0.019 | 1/11 (A549) | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.87×** | +3.4 | 0.025 | 1/11 (A498) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.063 | 0/13 | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.68×** | +3.0 | 0.075 | 2/11 (NCI-H460, NCI-H1573) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.72×** | +2.9 | 0.097 | 0/10 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8905.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0823×, H4 0.155×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LOX-IMVI 0.187×, NCI-H460 0.260×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.337×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Asciminib (drug)]] 0.5 µM |  | **0.518×** | -3.8 | 0.048 | 3/15 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.525×** | -3.8 | 0.048 | 8/15 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.553× | -3.5 | 0.10 | 2/15 (hTERT-HPNE, PANC-1) | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.551× | -3.3 | 0.12 | 1/15 (HS-578T) | rises with dose | plate-row cell shift |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.591× | -3.1 | 0.24 | 4/14 (NCI-H2030, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0823× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -9.5) |
| [[H4 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 9.15 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 4.97 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.337× (z -10.6) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.577 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.206 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP5]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[PAK3]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[COL4A6]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PTPN20]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SRPX2]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SLITRK4]] | +0.57 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ANOS1]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PLCXD2]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NCKAP5-AS2]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[GAP43]] | +0.54 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[CNTN1]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 | pathway: GPCR ligand binding |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB27A]] | -0.48 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[FAM76B]] | -0.45 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[UGP2]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[NABP2]] | -0.44 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRLNT]] | C | SIRLNT activity raises F2RL2's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.53× lower at baseline in the lines without SIRLNT | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[GRAMD1B]] | C | GRAMD1B activity raises F2RL2's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without GRAMD1B | 0.021 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises F2RL2's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without ESM1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[STEAP1B-AS1]] | C | STEAP1B-AS1 activity raises F2RL2's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without STEAP1B-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB5]] | B | F2RL2 activity raises CREB5's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without F2RL2 | 0.049 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| cells under [[Arbutin (drug)]] 5 µM | B | F2RL2 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 0.77× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[ROBO3]] | B | F2RL2 activity raises ROBO3's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without F2RL2 | 0.053 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | F2RL2 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 0.80× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| cells under [[Darolutamide (drug)]] 0.05 µM | B | F2RL2 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 0.78× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[F2R]] | B | F2RL2 activity strengthens F2R's drug response | lines that do not express F2RL2 (21) vs lines expressing it (15) | the lines without F2RL2 respond 0.58× as strongly (z diff +1.83); strongest at Harringtonine 5 µM: 0.62x vs 0.31x (z diff +3.4) | 0.090 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; target measured in part of the lines; artifact flags |
| cells under [[Neratinib (drug)]] 5 µM | B | F2RL2 activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 1.31× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | B | F2RL2 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 1.43× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[GRAMD1B]] | C | F2RL2 activity raises GRAMD1B's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 4.83× lower at baseline in the lines without F2RL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; co-absent with the target |
| [[RSPO3]] | C | F2RL2 activity raises RSPO3's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 3.50× lower at baseline in the lines without F2RL2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; co-absent with the target |
| [[MEG3]] | C | F2RL2 activity raises MEG3's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 3.93× lower at baseline in the lines without F2RL2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; co-absent with the target |
| [[MEG8]] | C | F2RL2 activity raises MEG8's level | lines that do not express F2RL2 (32) vs lines expressing it (18) | 3.51× lower at baseline in the lines without F2RL2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 33.8); signed map (40.7, 45.0). **Vector** length 31.6, 7.32% of its response variance represented; |z| ≥ 3 in 338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +1.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.8 | +4.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +2.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -3.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.0 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | coagulation factor II thrombin receptor like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:76,615,482-76,623,413 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAR3 |
| Gene groups (HGNC) | F2R receptors |
| Hallmark sets | COAGULATION, IL2_STAT5_SIGNALING |
| Reactome | 9 pathways, smallest: Thrombin signalling through proteinase activated receptors (PARs); Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [O00254](https://www.uniprot.org/uniprotkb/O00254) (Proteinase-activated receptor 3):

> Receptor for activated thrombin coupled to G proteins that stimulate phosphoinositide hydrolysis.

**Summary**, from NCBI Gene [2151](https://www.ncbi.nlm.nih.gov/gene/2151):

> This gene encodes a member of the protease-activated receptor (PAR) family which is a subfamily of the seven transmembrane G protein-coupled cell surface receptor family. The encoded protein acts as a cofactor in the thrombin-mediated cleavage and activation of the protease-activated receptor family member PAR4. The encoded protein plays an essential role in hemostasis and thrombosis. Alternate splicing results in multiple transcript variants that encode different isoforms. [provided by RefSeq, …

**Accessions** — [HGNC:3539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3539) · Entrez [2151](https://www.ncbi.nlm.nih.gov/gene/2151) · UniProt [O00254](https://www.uniprot.org/uniprotkb/O00254) · Ensembl [ENSG00000164220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164220)

## Data

Gene col 8905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8905); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8905]; `tensor/DDL_lfc|DDL_z.npy` [8905]; `embed/gene_vectors.npy` [8905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8905 or target_col == 8905). Every well: [[F2RL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/F2RL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
