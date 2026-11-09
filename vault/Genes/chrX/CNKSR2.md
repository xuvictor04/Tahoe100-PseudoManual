---
symbol: "CNKSR2"
type: "gene"
col: 7422
ensembl_id: "ENSG00000149970"
name: "connector enhancer of kinase suppressor of Ras 2"
location: "Xp22.12"
module: 19
arm: "+"
pooled_cpm: 10.66
n_lines_expressing: 18
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CNKSR2

*connector enhancer of kinase suppressor of Ras 2* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.76× (z +19.2, q 0e+00, up in 7 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.279×, NCI-H2030 0.338×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.217×; ⚠ cell-cycle shift, explains ~64% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.283×; ⚠ cell-cycle shift, explains ~14% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBF2]] (+0.66, fdr 7e-06), [[CNTN1]] (+0.62, fdr 8e-06), [[SLC35F3]] (+0.60, fdr 1e-05); moves opposite to [[HOMEZ]] (-0.48, fdr 6e-05), [[DNAJC27-AS1]] (-0.44, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[TMEM170B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +19.2 | 0e+00 | 7/13 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.64×** | +13.0 | 5e-36 | 0/11 | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +9.7 | 7e-20 | 14/15 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.08×** | +9.4 | 7e-19 | 0/8 | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +7.4 | 2e-11 | 10/15 (NCI-H460, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +6.8 | 1e-09 | 12/15 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.7 | 9e-07 | 10/14 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +5.4 | 5e-06 | 11/15 (H4, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.31×** | +5.0 | 3e-05 | 2/13 (SHP-77, C32) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.7 | 2e-04 | 8/15 (NCI-H460, BT-474, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.2 | 0.001 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +4.2 | 0.002 | 2/12 (H4, BT-474) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +4.0 | 0.002 | 13/15 (NCI-H23, H4, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.47×** | +3.8 | 0.005 | 2/9 (SK-MEL-2, C32) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.005 | 1/14 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.030 | 2/15 (NCI-H1792, NCI-H661) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.034 | 2/14 (A-427, SK-MEL-2) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.039 | 2/15 (NCI-H460, A549) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.053 | 1/15 (SHP-77) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.091 | 0/15 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7422.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.279×, NCI-H2030 0.338×; ⚠ cell-cycle shift, explains ~50% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.217×; ⚠ cell-cycle shift, explains ~64% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.283×; ⚠ cell-cycle shift, explains ~14% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.765× | -3.6 | 0.11 | 0/15 | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.605× | -3.5 | 0.11 | 2/14 (NCI-H460, C-33 A) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.766× | -3.2 | 0.19 | 4/16 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.790× | -3.2 | 0.19 | 0/16 | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.849× | -3.1 | 0.19 | 3/15 (NCI-H460, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.4 | 1 (1 ⚠) | 5 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.43× (z +10.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H2030 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBF2]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CNTN1]] | +0.62 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[SLC35F3]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SLITRK4]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GABBR2]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[EPB41L3]] | +0.58 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[PDE1C]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RTN1]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[RIMS1]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 | same gene group |
| [[ANO5]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[UNC5D]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[B3GALT1]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOMEZ]] | -0.48 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[DNAJC27-AS1]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CNKSR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GJB2]] | B | GJB2 activity lowers CNKSR2's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.69× higher at baseline in the lines without GJB2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[LINC02864]] | C | LINC02864 activity raises CNKSR2's level | lines that do not express LINC02864 (36) vs lines expressing it (14) | 3.92× lower at baseline in the lines without LINC02864 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC00824, LINC01205; co-absent with the target |
| [[ELOVL2]] | C | ELOVL2 activity raises CNKSR2's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 3.77× lower at baseline in the lines without ELOVL2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |
| [[ANO5]] | C | ANO5 activity raises CNKSR2's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 3.67× lower at baseline in the lines without ANO5 | 0.072 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM170B]] | B | CNKSR2 activity raises TMEM170B's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without CNKSR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent |
| [[GLRB]] | B | CNKSR2 activity weakens GLRB's drug response | lines that do not express CNKSR2 (16) vs lines expressing it (12) | the lines without CNKSR2 respond 1.22× as strongly (z diff -0.29); strongest at Dinaciclib 5 µM: 1.42x vs 0.49x (z diff -5.0) | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ANO5]] | C | CNKSR2 activity raises ANO5's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 5.81× lower at baseline in the lines without CNKSR2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[SNCA]] | C | CNKSR2 activity raises SNCA's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 6.56× lower at baseline in the lines without CNKSR2 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[LINC02864]] | C | CNKSR2 activity raises LINC02864's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 4.37× lower at baseline in the lines without CNKSR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[UNC13A]] | C | CNKSR2 activity raises UNC13A's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 2.31× lower at baseline in the lines without CNKSR2 | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[MED12L]] | C | CNKSR2 activity raises MED12L's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 4.13× lower at baseline in the lines without CNKSR2 | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[RADIL]] | C | CNKSR2 activity raises RADIL's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 2.54× lower at baseline in the lines without CNKSR2 | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[FAM110B]] | C | CNKSR2 activity raises FAM110B's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 4.41× lower at baseline in the lines without CNKSR2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.2, 38.7); signed map (41.0, 46.3). **Vector** length 42.9, 12.2% of its response variance represented; |z| ≥ 3 in 346 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.8 | +13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.3 | -3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -0.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | connector enhancer of kinase suppressor of Ras 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:21,372,801-21,654,695 (+) |
| Ensembl biotype | protein_coding |
| Also known as | maguin, KIAA0902, CNK2, KSR2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Sterile alpha motif domain containing; PDZ domain containing |
| Reactome | 13 pathways, smallest: Signaling by high-kinase activity BRAF mutants; MAP2K and MAPK activation; Signaling by RAF1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXI2](https://www.uniprot.org/uniprotkb/Q8WXI2) (Connector enhancer of kinase suppressor of ras 2):

> May function as an adapter protein or regulator of Ras signaling pathways.

**Summary**, from NCBI Gene [22866](https://www.ncbi.nlm.nih.gov/gene/22866):

> This gene encodes a multidomain protein that functions as a scaffold protein to mediate the mitogen-activated protein kinase pathways downstream from Ras. This gene product is induced by vitamin D and inhibits apoptosis in certain cancer cells. It may also play a role in ternary complex assembly of synaptic proteins at the postsynaptic membrane and coupling of signal transduction to membrane/cytoskeletal remodeling. Multiple transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:19701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19701) · Entrez [22866](https://www.ncbi.nlm.nih.gov/gene/22866) · UniProt [Q8WXI2](https://www.uniprot.org/uniprotkb/Q8WXI2) · Ensembl [ENSG00000149970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149970)

## Data

Gene col 7422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7422); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7422]; `tensor/DDL_lfc|DDL_z.npy` [7422]; `embed/gene_vectors.npy` [7422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7422 or target_col == 7422). Every well: [[CNKSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNKSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
