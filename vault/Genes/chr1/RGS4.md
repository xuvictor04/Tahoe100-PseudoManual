---
symbol: "RGS4"
type: "gene"
col: 3880
ensembl_id: "ENSG00000117152"
name: "regulator of G protein signaling 4"
location: "1q23.3"
module: 116
arm: "+"
pooled_cpm: 12.27
n_lines_expressing: 15
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 37
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# RGS4

*regulator of G protein signaling 4* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.84× (z +9.3, q 8e-18, up in 3 of 11 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +4.4, q 0.001, up in 4 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.450× (z -5.1, q 2e-04, down in 8 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC190]] (+0.66, fdr 7e-06), [[RDUR]] (+0.66, fdr 1e-05), [[MARCHF4]] (+0.65, fdr 7e-06); moves opposite to [[CD109]] (-0.51, fdr 5e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); 37 go from it, the strongest it → [[RGMB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.84×** | +9.3 | 8e-18 | 3/11 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.64×** | +8.6 | 3e-15 | 1/7 (SNU-423) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.43×** | +5.7 | 3e-06 | 4/9 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +4.4 | 0.001 | 4/13 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +4.2 | 0.003 | 8/13 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.79×** | +3.9 | 0.010 | 6/13 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.67×** | +3.6 | 0.030 | 0/12 | inconsistent across doses | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.93×** | +3.2 | 0.083 | 4/13 (MIA PaCa-2, C-33 A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.083 | 4/13 (CHP-212, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.450×** | -5.1 | 2e-04 | 8/13 (MIA PaCa-2, Hs 766T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.497×** | -4.9 | 3e-04 | 13/13 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.508×** | -4.8 | 3e-04 | 12/13 (LOX-IMVI, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.618×** | -3.9 | 0.011 | 10/13 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.601×** | -3.4 | 0.062 | 11/13 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.701×** | -3.4 | 0.062 | 7/13 (MIA PaCa-2, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.623×** | -3.3 | 0.080 | 6/13 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.670× | -3.0 | 0.16 | 10/13 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.649× | -3.0 | 0.16 | 10/13 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 143 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0870× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 219 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.351× (z -19.4) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -16.1) |
| [[CHP-212 (line)]] | wt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0487× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -8.8) |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.942 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.857 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC190]] | +0.66 | +0.62 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[RDUR]] | +0.66 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[HHIP]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[LNCOG]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[AMOTL1]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.61 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[LINC01592]] | +0.61 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[NTNG1]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FGF1]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[HGF]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SCHIP1]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD109]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity raises RGS4's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[CCDC190]] | C | CCDC190 activity raises RGS4's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 7.20× lower at baseline in the lines without CCDC190 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[LINC02509]] | C | LINC02509 activity raises RGS4's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 3.11× lower at baseline in the lines without LINC02509 | 0.002 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises RGS4's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without ROBO4 | 0.006 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[LINC01812]] | C | LINC01812 activity raises RGS4's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without LINC01812 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[AK5]] | C | AK5 activity raises RGS4's level | lines that do not express AK5 (25) vs lines expressing it (25) | 3.20× lower at baseline in the lines without AK5 | 0.013 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[CFAP299]] | C | CFAP299 activity raises RGS4's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without CFAP299 | 0.024 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2; co-absent with the target |
| [[ADAMTSL1]] | C | ADAMTSL1 activity raises RGS4's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 3.20× lower at baseline in the lines without ADAMTSL1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | HGF activity raises RGS4's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.05× lower at baseline in the lines without HGF | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises RGS4's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.27× lower at baseline in the lines without DSCAM | 0.034 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises RGS4's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.21× lower at baseline in the lines without ESM1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises RGS4's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without ADTRP | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 12, C 25. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGMB]] | B | RGS4 activity raises RGMB's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.36× lower at baseline in the lines without RGS4 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[NEMP2]] | B | RGS4 activity raises NEMP2's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without RGS4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[FGF1]] | B | RGS4 activity raises FGF1's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 1.77× lower at baseline in the lines without RGS4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[RGMB]] | B | RGS4 activity weakens RGMB's drug response | lines that do not express RGS4 (34) vs lines expressing it (13) | the lines without RGS4 respond 4.23× as strongly (z diff -2.33); strongest at Idarubicin (hydrochloride) 5 µM: 1.90x vs 0.82x (z diff -6.5) | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; target measured in part of the lines; artifact flags |
| [[KBTBD8]] | B | RGS4 activity raises KBTBD8's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 1.57× lower at baseline in the lines without RGS4 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | RGS4 activity lowers the cells' numbers under Aliskiren 0.5 µM (makes them more sensitive) | lines that do not express RGS4 (35) vs lines expressing it (13) | the lines without RGS4: 1.27× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[FXYD5]] | B | RGS4 activity strengthens FXYD5's drug response | lines that do not express RGS4 (32) vs lines expressing it (11) | the lines without RGS4 respond 0.82× as strongly (z diff +0.87); strongest at Belinostat 5 µM: 0.64x vs 0.49x (z diff +2.3) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; target measured in part of the lines; artifact flags |
| cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM | B | RGS4 activity raises the cells' numbers under Gallic acid (hydrate) 0.05 µM (protects the cells) | lines that do not express RGS4 (35) vs lines expressing it (13) | the lines without RGS4: 0.87× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[PODXL]] | B | RGS4 activity raises PODXL's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.43× lower at baseline in the lines without RGS4 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| cells under [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM | B | RGS4 activity lowers the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (makes them more sensitive) | lines that do not express RGS4 (35) vs lines expressing it (13) | the lines without RGS4: 1.14× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | RGS4 activity lowers the cells' numbers under Terfenadine 0.5 µM (makes them more sensitive) | lines that do not express RGS4 (35) vs lines expressing it (13) | the lines without RGS4: 1.33× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[ENG]] | B | RGS4 activity raises ENG's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.51× lower at baseline in the lines without RGS4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.7, 11.6); signed map (15.8, 45.8). **Vector** length 64.6, 23.8% of its response variance represented; |z| ≥ 3 in 497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.1 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.0 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.9 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.3 | +3.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:163,068,775-163,076,802 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SCZD9 |
| Gene groups (HGNC) | Regulators of G-protein signaling |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: G alpha (z) signalling events; G alpha (q) signalling events; G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P49798](https://www.uniprot.org/uniprotkb/P49798) (Regulator of G protein signaling 4):

> Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits thereby driving them into their inactive GDP-bound form. Activity on G(z)-alpha is inhibited by phosphorylation of the G protein. Activity on G(z)-alpha and G(i)-alpha-1 is inhibited by palmitoylation of the G protein.

**Summary**, from NCBI Gene [5999](https://www.ncbi.nlm.nih.gov/gene/5999):

> Regulator of G protein signaling (RGS) family members are regulatory molecules that act as GTPase activating proteins (GAPs) for G alpha subunits of heterotrimeric G proteins. RGS proteins are able to deactivate G protein subunits of the Gi alpha, Go alpha and Gq alpha subtypes. They drive G proteins into their inactive GDP-bound forms. Regulator of G protein signaling 4 belongs to this family. All RGS proteins share a conserved 120-amino acid sequence termed the RGS domain. Regulator of G …

**Accessions** — [HGNC:10000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10000) · Entrez [5999](https://www.ncbi.nlm.nih.gov/gene/5999) · UniProt [P49798](https://www.uniprot.org/uniprotkb/P49798) · Ensembl [ENSG00000117152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117152)

## Data

Gene col 3880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3880); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3880]; `tensor/DDL_lfc|DDL_z.npy` [3880]; `embed/gene_vectors.npy` [3880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3880 or target_col == 3880). Every well: [[RGS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
