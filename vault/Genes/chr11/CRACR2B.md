---
symbol: "CRACR2B"
type: "gene"
col: 10852
ensembl_id: "ENSG00000177685"
name: "calcium release activated channel regulator 2B"
location: "11p15.5"
module: 58
arm: "+"
pooled_cpm: 6.48
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 19
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CRACR2B

*calcium release activated channel regulator 2B* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +11.4, q 3e-27, up in 14 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Entrectinib (drug)]] 5 µM: 1.56× (z +3.8, q 0.012, up in 4 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 5.24×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.424× (z -7.4, q 1e-10, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRXL2B]] (+0.60, fdr 1e-05), [[SSBP3]] (+0.55, fdr 3e-05), [[PAXX]] (+0.55, fdr 1e-04, ⚠ PAXX in the vector space only through flagged drug-doses), [[VWA1]] (+0.54, fdr 4e-05); moves opposite to [[PRR14L]] (-0.53, fdr 7e-05), [[RHBDD3]] (-0.46, fdr 0.002, ⚠ not reproduced), [[ZNF808]] (-0.45, fdr 3e-04), [[RNF14]] (-0.44, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[YBX2]] → it (grade B ⚠); 19 go from it, the strongest it → [[CHKA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10852.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 5.24×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +11.4 | 3e-27 | 14/17 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +8.8 | 5e-16 | 8/10 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +5.1 | 7e-05 | 7/14 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +4.7 | 5e-04 | 9/36 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.62×** | +4.1 | 0.004 | 9/24 (HT-29, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.012 | 4/34 (HOP62, PANC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.039 | 11/34 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | 1.99× | +3.1 | 0.16 | 1/26 (A498) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.424×** | -7.4 | 1e-10 | 20/33 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.563×** | -7.0 | 8e-10 | 20/31 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.480×** | -6.3 | 5e-08 | 17/29 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -5.7 | 2e-06 | 17/29 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -5.5 | 3e-06 | 18/33 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -5.3 | 1e-05 | 18/34 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.563×** | -4.9 | 7e-05 | 19/33 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.590×** | -4.5 | 4e-04 | 19/35 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.365×** | -4.5 | 5e-04 | 15/28 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.593×** | -4.2 | 0.001 | 18/31 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.422×** | -3.8 | 0.006 | 8/33 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.744×** | -3.6 | 0.015 | 16/35 (SW1417, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.666×** | -3.5 | 0.021 | 13/34 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -3.3 | 0.033 | 11/33 (Hs 766T, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.680×** | -3.3 | 0.035 | 11/34 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.6) |
| [[PANC-1 (line)]] | alt | 36.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 6.93 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0234× (z -11.4) |
| [[C-33 A (line)]] | alt | 5.70 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0941× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 4.44 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0735× (z -8.6) |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.8) |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.6) |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 6.92 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0595× (z -9.6) |
| [[SW480 (line)]] | alt | 4.90 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.879 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRXL2B]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SSBP3]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[PAXX]] ⚠ | +0.55 | +0.33 / +0.48 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[VWA1]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[RHPN1]] | +0.54 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[ENTPD2]] | +0.54 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[SLC37A4]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[NTHL1]] | +0.53 | +0.37 / +0.46 | both halves | 9e-05 |  |
| [[FOXO6]] | +0.53 | +0.34 / +0.32 | both halves | 1e-04 |  |
| [[CLDN3]] | +0.52 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[TJP3]] | +0.52 | +0.46 / +0.33 | both halves | 1e-04 |  |
| [[THEM6]] | +0.51 | +0.36 / +0.31 | both halves | 2e-04 |  |
| [[GCHFR]] | +0.51 | +0.39 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR14L]] | -0.53 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[RHBDD3]] | -0.46 | -0.44 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[ZNF808]] | -0.45 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[RNF14]] | -0.44 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[RCC1L]] | -0.44 | -0.35 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[MCF2]] | -0.44 | -0.35 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[STXBP5]] | -0.43 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[AVEN]] | -0.43 | -0.31 / -0.24 | both halves | 5e-04 |  |
| [[IREB2]] | -0.43 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[MFF-DT]] | -0.43 | -0.31 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[AP5M1]] | -0.43 | -0.35 / -0.19 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX2]] | B | YBX2 activity raises CRACR2B's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.24× lower at baseline in the lines without YBX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[ATAD3C]] | B | ATAD3C activity raises CRACR2B's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.34× lower at baseline in the lines without ATAD3C | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[SORL1]] | B | SORL1 activity raises CRACR2B's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without SORL1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[MUC3A]] | B | MUC3A activity raises CRACR2B's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.11× lower at baseline in the lines without MUC3A | 0.048 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[PADI2]] | B | PADI2 activity raises CRACR2B's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.98× lower at baseline in the lines without PADI2 | 0.048 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[ESPN]] | B | ESPN activity raises CRACR2B's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.86× lower at baseline in the lines without ESPN | 0.068 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises CRACR2B's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.06× lower at baseline in the lines without PLEKHG6 | 0.089 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHKA]] | B | CRACR2B activity raises CHKA's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.97× lower at baseline in the lines without CRACR2B | 0.005 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[PRXL2B]] | B | CRACR2B activity raises PRXL2B's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.77× lower at baseline in the lines without CRACR2B | 0.008 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[VWA1]] | B | CRACR2B activity raises VWA1's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without CRACR2B | 0.018 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ATAD3C]] | B | CRACR2B activity raises ATAD3C's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without CRACR2B | 0.027 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[SORL1]] | B | CRACR2B activity raises SORL1's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without CRACR2B | 0.028 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[EPHB3]] | B | CRACR2B activity raises EPHB3's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without CRACR2B | 0.029 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[GNA15]] | B | CRACR2B activity raises GNA15's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without CRACR2B | 0.034 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[CGN]] | B | CRACR2B activity raises CGN's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 3.95× lower at baseline in the lines without CRACR2B | 0.037 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ARHGAP45]] | B | CRACR2B activity raises ARHGAP45's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.11× lower at baseline in the lines without CRACR2B | 0.039 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[CLDN3]] | B | CRACR2B activity raises CLDN3's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without CRACR2B | 0.045 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ESPN]] | B | CRACR2B activity raises ESPN's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without CRACR2B | 0.046 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[ZNF808]] | B | CRACR2B activity raises ZNF808's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without CRACR2B | 0.047 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.393). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.4, 32.8); signed map (-24.5, 31.2). **Vector** length 53.2, 9.24% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.1 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +11.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | -1.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.0 | +0.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.8 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium release activated channel regulator 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:826,144-831,991 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45840; previously EFCAB4A |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4Y2](https://www.uniprot.org/uniprotkb/Q8N4Y2) (EF-hand calcium-binding domain-containing protein 4A):

> Plays a role in store-operated Ca(2+) entry (SOCE).

**Summary**, from NCBI Gene [283229](https://www.ncbi.nlm.nih.gov/gene/283229):

> Predicted to enable calcium ion binding activity. Involved in store-operated calcium entry. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28703) · Entrez [283229](https://www.ncbi.nlm.nih.gov/gene/283229) · UniProt [Q8N4Y2](https://www.uniprot.org/uniprotkb/Q8N4Y2) · Ensembl [ENSG00000177685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177685)

## Data

Gene col 10852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10852); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10852]; `tensor/DDL_lfc|DDL_z.npy` [10852]; `embed/gene_vectors.npy` [10852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10852 or target_col == 10852). Every well: [[CRACR2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRACR2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
