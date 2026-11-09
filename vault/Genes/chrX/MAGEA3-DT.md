---
symbol: "MAGEA3-DT"
type: "gene"
col: 16308
ensembl_id: "ENSG00000287394"
name: "MAGEA3 divergent transcript"
location: "Xq28"
module: 108
arm: "+"
pooled_cpm: 16.9
n_lines_expressing: 21
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 17
direction_downstream: 11
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# MAGEA3-DT

*MAGEA3 divergent transcript* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.77× (z +9.7, q 1e-19, up in 1 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.36× (z +5.3, q 2e-05, up in 0 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.598× (z -8.4, q 2e-14, down in 17 of 19 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABRA3]] (+0.84, fdr 7e-06), [[LINC01446]] (+0.66, fdr 7e-06), [[KC6]] (+0.65, fdr 7e-06); moves opposite to [[NEIL1]] (-0.43, fdr 0.001, ⚠ one half only (not replicated)), [[THRB]] (-0.43, fdr 1e-04), [[LINC00412]] (-0.42, fdr 3e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[GABRA3]] → it (grade C ⚠); 11 go from it, the strongest it → [[GABRA3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +9.7 | 1e-19 | 1/18 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.3 | 7e-08 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 2e-05 | 0/19 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 5e-04 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.003 | 2/19 (KATO III, Hs 766T) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.1 | 0.003 | 1/17 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.026 | 1/19 (NCI-H1792) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.041 | 0/19 | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.041 | 4/19 (LS 180, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.21×** | +3.3 | 0.046 | 6/19 (A-427, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.3 | 0.053 | 3/19 (KATO III, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.054 | 2/19 (SHP-77, NCI-H1573) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.598×** | -8.4 | 2e-14 | 17/19 (A-427, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -8.2 | 5e-14 | 12/19 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -7.4 | 2e-11 | 14/19 (RPMI-7951, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.756×** | -4.7 | 3e-04 | 1/19 (LS 180) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -4.0 | 0.006 | 13/18 (A-427, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.846× | -4.0 | 0.006 | 16/18 (NCI-H1573, RPMI-7951, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -3.5 | 0.045 | 13/19 (A-172, H4, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.807×** | -3.3 | 0.056 | 0/19 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.821×** | -3.3 | 0.056 | 8/19 (C32, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.704× | -3.1 | 0.11 | 8/19 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 78.5 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.243× (z -11.0) |
| [[HS-578T (line)]] | alt | 59.1 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.337× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0887× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -10.0) |
| [[A-427 (line)]] | wt | 98.6 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0919× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0963× (z -12.8) |
| [[H4 (line)]] | wt | 65.5 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.143× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 69.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -9.8) |
| [[A549 (line)]] | wt | 17.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 44.2 | 0 | 4 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 84.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0499× (z -24.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.7) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H23 (line)]] | alt | 66.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -19.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 35.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.264× (z -11.3) |
| [[SHP-77 (line)]] | alt | 63.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -18.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABRA3]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LINC01446]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[KC6]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[LINC01242]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[JAKMIP2]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[LINC02616]] | +0.56 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[GLYATL2]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[EVC2]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LINC02377]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ASNSP1]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[NETO1]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[LINC02109]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEIL1]] | -0.43 | -0.51 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[THRB]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[LINC00412]] | -0.42 | -0.45 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRA3]] | C | GABRA3 activity raises MAGEA3-DT's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 8.47× lower at baseline in the lines without GABRA3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises MAGEA3-DT's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 9.24× lower at baseline in the lines without LINC00648 | 6e-04 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[LINC00470]] | C | LINC00470 activity raises MAGEA3-DT's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 10.93× lower at baseline in the lines without LINC00470 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises MAGEA3-DT's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 8.05× lower at baseline in the lines without LINC02616 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[EPIC1]] | C | EPIC1 activity raises MAGEA3-DT's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 4.40× lower at baseline in the lines without EPIC1 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises MAGEA3-DT's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 5.28× lower at baseline in the lines without MGAT4C | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises MAGEA3-DT's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 5.48× lower at baseline in the lines without LINC01446 | 0.013 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises MAGEA3-DT's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 4.22× lower at baseline in the lines without LINC01518 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises MAGEA3-DT's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 5.51× lower at baseline in the lines without CDH12 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LINC01060]] | C | LINC01060 activity raises MAGEA3-DT's level | lines that do not express LINC01060 (29) vs lines expressing it (21) | 4.68× lower at baseline in the lines without LINC01060 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, ENSG00000287598, NTM; co-absent with the target |
| [[TPTE]] | C | TPTE activity raises MAGEA3-DT's level | lines that do not express TPTE (35) vs lines expressing it (15) | 4.91× lower at baseline in the lines without TPTE | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[MDGA2]] | C | MDGA2 activity raises MAGEA3-DT's level | lines that do not express MDGA2 (32) vs lines expressing it (18) | 4.93× lower at baseline in the lines without MDGA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZIC1, NLGN4X, TWIST1; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRA3]] | C | MAGEA3-DT activity raises GABRA3's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 6.92× lower at baseline in the lines without MAGEA3-DT | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LINC00648]] | C | MAGEA3-DT activity raises LINC00648's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 3.67× lower at baseline in the lines without MAGEA3-DT | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[EPIC1]] | C | MAGEA3-DT activity raises EPIC1's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 4.42× lower at baseline in the lines without MAGEA3-DT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LRRTM4]] | C | MAGEA3-DT activity raises LRRTM4's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 4.43× lower at baseline in the lines without MAGEA3-DT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[TPTE]] | C | MAGEA3-DT activity raises TPTE's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 4.16× lower at baseline in the lines without MAGEA3-DT | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LINC00470]] | C | MAGEA3-DT activity raises LINC00470's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 6.16× lower at baseline in the lines without MAGEA3-DT | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LINC02476]] | C | MAGEA3-DT activity raises LINC02476's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 3.97× lower at baseline in the lines without MAGEA3-DT | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LINC02616]] | C | MAGEA3-DT activity raises LINC02616's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 2.96× lower at baseline in the lines without MAGEA3-DT | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LINC01446]] | C | MAGEA3-DT activity raises LINC01446's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 3.89× lower at baseline in the lines without MAGEA3-DT | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[EVC2]] | C | MAGEA3-DT activity raises EVC2's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without MAGEA3-DT | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[CCDC144NL-AS1]] | C | MAGEA3-DT activity raises CCDC144NL-AS1's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without MAGEA3-DT | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.8, 25.7); signed map (32.5, 44.1). **Vector** length 61.5, 18.0% of its response variance represented; |z| ≥ 3 in 435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -0.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MAGEA3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq28 — chrX:152,574,677-152,698,700 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56247) · Entrez [105373370](https://www.ncbi.nlm.nih.gov/gene/105373370) · Ensembl [ENSG00000287394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000287394)

## Data

Gene col 16308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16308); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16308]; `tensor/DDL_lfc|DDL_z.npy` [16308]; `embed/gene_vectors.npy` [16308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16308 or target_col == 16308). Every well: [[MAGEA3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGEA3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
