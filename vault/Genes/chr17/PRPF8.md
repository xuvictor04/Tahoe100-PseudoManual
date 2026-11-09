---
symbol: "PRPF8"
type: "gene"
col: 10475
ensembl_id: "ENSG00000174231"
name: "pre-mRNA processing factor 8"
location: "17p13.3"
module: 127
arm: "+"
pooled_cpm: 138.02
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# PRPF8

*pre-mRNA processing factor 8* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.42× (z +17.4, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.935× (z -3.6, q 0.062, down in 0 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.793× (z -3.6, q 0.062, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP200]] (+0.90, fdr 7e-06), [[STT3A]] (+0.75, fdr 7e-06), [[TAF6]] (+0.75, fdr 7e-06); moves opposite to [[ERVK3-1]] (-0.72, fdr 7e-06), [[MSX1]] (-0.69, fdr 2e-05), [[EIF1B]] (-0.67, fdr 7e-06).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RNF223]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.42×** | +17.4 | 0e+00 | 49/49 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **6.95×** | +15.8 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.4 | 9e-19 | 39/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +8.6 | 9e-16 | 44/49 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.52×** | +6.1 | 1e-07 | 35/47 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +5.7 | 8e-07 | 31/45 (SNU-423, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.011 | 30/49 (A-172, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.012 | 33/49 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.020 | 33/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +3.2 | 0.079 | 26/48 (SW480, SNU-423, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.1 | 0.085 | 19/38 (A-172, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.6 | 0.062 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.793×** | -3.6 | 0.062 | 27/48 (SW 900, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.794×** | -3.6 | 0.062 | 28/48 (SW 900, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.100 | 24/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | 0.816× | -3.0 | 0.24 | 22/47 (hTERT-HPNE, SNU-423, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.0 | 0.24 | 20/49 (LoVo, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 139 | 5 (2 ⚠) | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.25× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -9.3) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.442× (z -9.2) |
| [[A498 (line)]] | wt | 164 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +11.2) | — |
| [[A549 (line)]] | wt | 202 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +15.8) | — |
| [[LoVo (line)]] | wt | 142 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.8× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 129 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +16.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 173 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.3× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 114 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 54.3 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 10.0× (z +10.4) | [[Harringtonine (drug)]] 5 µM 0.355× (z -8.6) |
| [[SNU-423 (line)]] | alt | 119 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 7.03× (z +11.1) | — |
| [[A-427 (line)]] | wt | 95.9 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 95.5 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 9.89× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 125 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 6.42× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 124 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +12.7) | — |
| [[KATO III (line)]] | alt | 170 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.42× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 90.8 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 135 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.1× (z +16.9) | — |
| [[SW480 (line)]] | alt | 230 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 174 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.27× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 123 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 25.9× (z +15.2) | — |
| [[H4 (line)]] | wt | 169 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.5× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 165 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.25× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 104 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 19.2× (z +15.3) | — |
| [[Hs 766T (line)]] | wt | 104 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 18.1× (z +15.3) | — |
| [[HT-29 (line)]] | alt | 73.8 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.01× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 9.32× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 145 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 12.2× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 66.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 213 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.09× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 96.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.37× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 89.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.27× (z +12.0) | — |
| [[RKO (line)]] | wt | 177 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.5× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 118 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.09× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 134 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.23× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 241 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.97× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 119 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.59× (z +9.8) | — |
| [[SW48 (line)]] | wt | 208 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.36× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 78.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.41× (z +11.2) | — |
| [[C32 (line)]] | wt | 132 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.84× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 65.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.84× (z +11.8) | — |
| [[CHP-212 (line)]] | wt | 225 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 112 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.53× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 195 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.57× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 260 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.48× (z +11.3) | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0840× (z -9.5) |
| [[AN3 CA (line)]] | alt | 176 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 203 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP200]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[STT3A]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[TAF6]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[EMC1]] | +0.73 | +0.61 / +0.78 | both halves | 7e-06 | STRING 415 |
| [[RPSA]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 | STRING 427 |
| [[ATP13A1]] | +0.70 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[ATP5F1B]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.70 | +0.52 / +0.79 | both halves | 1e-05 |  |
| [[DDOST]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[AGO1]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK3-1]] | -0.72 | -0.62 / -0.76 | both halves | 7e-06 |  |
| [[MSX1]] | -0.69 | -0.47 / -0.76 | both halves | 2e-05 |  |
| [[EIF1B]] | -0.67 | -0.67 / -0.67 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.63 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[AK6]] | -0.61 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[MRPS18C]] | -0.61 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.61 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[FDX2]] | -0.60 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[ZNF593]] | -0.60 | -0.31 / -0.72 | both halves | 2e-04 |  |
| [[YBEY]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.60 | -0.36 / -0.70 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MAFG]] | -0.59 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[COX17]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF223]] | B | RNF223 activity lowers PRPF8's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 1.26× higher at baseline in the lines without RNF223 | 0.051 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[MARVELD3]] | B | MARVELD3 activity lowers PRPF8's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.18× higher at baseline in the lines without MARVELD3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[CRTAP]] | C | CRTAP activity raises PRPF8's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without CRTAP | 0.030 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.3, -23.5); signed map (-21.8, -36.6). **Vector** length 139, 45.7% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +9.6 | +15.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.3 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +5.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +6.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,650,629-1,684,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRPC8, Prp8, hPrp8, SNRNP220; previously RP13 |
| Gene groups (HGNC) | JAMM/MPN+ metallopeptidase family; U5 small nuclear ribonucleoprotein; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 8 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2Q9](https://www.uniprot.org/uniprotkb/Q6P2Q9) (Pre-mRNA-processing-splicing factor 8):

> Plays a role in pre-mRNA splicing as core component of precatalytic, catalytic and postcatalytic spliceosomal complexes, both of the predominant U2-type spliceosome and the minor U12-type spliceosome. Functions as a scaffold that mediates the ordered assembly of spliceosomal proteins and snRNAs. Required for the assembly of the U4/U6-U5 tri-snRNP complex, a building block of the spliceosome. Functions as a scaffold that positions spliceosomal U2, U5 and U6 snRNAs at splice sites on pre-mRNA …

**Summary**, from NCBI Gene [10594](https://www.ncbi.nlm.nih.gov/gene/10594):

> Pre-mRNA splicing occurs in 2 sequential transesterification steps. The protein encoded by this gene is a component of both U2- and U12-dependent spliceosomes, and found to be essential for the catalytic step II in pre-mRNA splicing process. It contains several WD repeats, which function in protein-protein interactions. This protein has a sequence similarity to yeast Prp8 protein. This gene is a candidate gene for autosomal dominant retinitis pigmentosa. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17340) · Entrez [10594](https://www.ncbi.nlm.nih.gov/gene/10594) · UniProt [Q6P2Q9](https://www.uniprot.org/uniprotkb/Q6P2Q9) · Ensembl [ENSG00000174231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174231)

## Data

Gene col 10475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10475); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10475]; `tensor/DDL_lfc|DDL_z.npy` [10475]; `embed/gene_vectors.npy` [10475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10475 or target_col == 10475). Every well: [[PRPF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
