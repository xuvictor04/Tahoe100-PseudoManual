---
symbol: "IGFBP6"
type: "gene"
col: 9541
ensembl_id: "ENSG00000167779"
name: "insulin like growth factor binding protein 6"
location: "12q13.13"
module: 13
arm: "+"
pooled_cpm: 31.66
n_lines_expressing: 34
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 11
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# IGFBP6

*insulin like growth factor binding protein 6* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.50× (z +10.2, q 8e-22, up in 27 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.60× (z +4.1, q 0.005, up in 18 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 5.55×, HEC-1-A 4.48×, A498 4.69×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 7.80×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.399× (z -11.4, q 4e-27, down in 26 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MORC3]] (+0.55, fdr 1e-05), [[PTPRN]] (+0.54, fdr 1e-05), [[CNPY4]] (+0.52, fdr 1e-04); moves opposite to [[ASB13]] (-0.50, fdr 1e-04), [[AFG3L2]] (-0.47, fdr 5e-05), [[DBF4]] (-0.45, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SIRLNT]] → it (grade B ⚠); 11 go from it, the strongest it → [[C18orf32]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9541.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 5.55×, HEC-1-A 4.48×, A498 4.69×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 7.80×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.50×** | +10.2 | 8e-22 | 27/30 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.5 | 4e-15 | 24/26 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +6.6 | 9e-09 | 20/26 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +5.3 | 1e-05 | 15/32 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.60×** | +4.1 | 0.005 | 18/32 (CFPAC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.007 | 18/32 (LOX-IMVI, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.399×** | -11.4 | 4e-27 | 26/31 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -7.5 | 1e-11 | 25/30 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.521×** | -5.7 | 2e-06 | 26/32 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.527×** | -5.6 | 3e-06 | 25/32 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.550×** | -5.2 | 2e-05 | 22/32 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.589×** | -4.6 | 3e-04 | 21/32 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.605×** | -4.4 | 9e-04 | 25/32 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.720×** | -4.1 | 0.003 | 22/32 (A498, NCI-H1792, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.642×** | -3.7 | 0.012 | 19/32 (A-172, SW 900, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.446×** | -3.7 | 0.013 | 19/31 (LOX-IMVI, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.658×** | -3.7 | 0.013 | 19/30 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.504×** | -3.1 | 0.082 | 15/32 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 89.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -14.3) |
| [[SW480 (line)]] | alt | 13.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.80× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.0) |
| [[HOP62 (line)]] | alt | 26.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -14.7) |
| [[HS-578T (line)]] | alt | 47.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 36.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 47.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -14.6) |
| [[A498 (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.6) |
| [[H4 (line)]] | wt | 49.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.8) |
| [[RKO (line)]] | wt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.8) |
| [[A-427 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 184 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORC3]] | +0.55 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PTPRN]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CNPY4]] | +0.52 | +0.41 / +0.34 | both halves | 1e-04 |  |
| [[KALRN]] | +0.52 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[DKK3]] | +0.52 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[SCUBE3]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[LMO2]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CERCAM]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ECM1]] | +0.50 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[RTL8C]] | +0.50 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ULBP2]] | +0.49 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[L1CAM]] | +0.48 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB13]] | -0.50 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[AFG3L2]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[DBF4]] | -0.45 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ACSF3]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[ANGEL1]] | -0.43 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[ZNF839]] | -0.42 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[TSEN2]] | -0.42 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[WDR75]] | -0.42 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[MPHOSPH6]] | -0.41 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[SNHG17]] | -0.41 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[G2E3]] | -0.41 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[TMEM177]] | -0.40 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRLNT]] | B | SIRLNT activity raises IGFBP6's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.33× lower at baseline in the lines without SIRLNT | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C18orf32]] | B | IGFBP6 activity lowers C18orf32's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 1.38× higher at baseline in the lines without IGFBP6 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[ACSF3]] | B | IGFBP6 activity lowers ACSF3's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 1.37× higher at baseline in the lines without IGFBP6 | 0.024 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[PTHLH]] | B | IGFBP6 activity raises PTHLH's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without IGFBP6 | 0.049 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[LINC01411]] | B | IGFBP6 activity raises LINC01411's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 3.48× lower at baseline in the lines without IGFBP6 | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[TMEM177]] | B | IGFBP6 activity lowers TMEM177's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without IGFBP6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[MORC3]] | B | IGFBP6 activity raises MORC3's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without IGFBP6 | 0.074 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[PRSS23]] | B | IGFBP6 activity raises PRSS23's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without IGFBP6 | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[NID2]] | B | IGFBP6 activity raises NID2's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without IGFBP6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[COL1A1]] | B | IGFBP6 activity raises COL1A1's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without IGFBP6 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[TMOD3]] | B | IGFBP6 activity strengthens TMOD3's drug response | lines that do not express IGFBP6 (16) vs lines expressing it (33) | the lines without IGFBP6 respond 0.65× as strongly (z diff +1.75); strongest at Panobinostat 0.5 µM: 0.83x vs 0.70x (z diff +3.1) | 0.083 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1; target measured in part of the lines; artifact flags |
| [[FBN1]] | B | IGFBP6 activity raises FBN1's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without IGFBP6 | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.351). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (57.1, 17.5); signed map (52.8, -16.8). **Vector** length 65.0, 17.4% of its response variance represented; |z| ≥ 3 in 554 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -5.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -7.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor binding protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,097,436-53,102,345 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Insulin like growth factor binding proteins |
| Hallmark sets | APOPTOSIS |
| Reactome | 1 pathways, smallest: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P24592](https://www.uniprot.org/uniprotkb/P24592) (Insulin-like growth factor-binding protein 6):

> IGF-binding proteins prolong the half-life of the IGFs and have been shown to either inhibit or stimulate the growth promoting effects of the IGFs on cell culture. They alter the interaction of IGFs with their cell surface receptors. Activates the MAPK signaling pathway and induces cell migration.

**Summary**, from NCBI Gene [3489](https://www.ncbi.nlm.nih.gov/gene/3489):

> Enables identical protein binding activity and insulin-like growth factor II binding activity. Involved in cell migration and positive regulation of stress-activated MAPK cascade. Part of insulin-like growth factor binary complex. Implicated in obesity. Biomarker of breast cancer; in situ carcinoma; leiomyoma; and neovascular inflammatory vitreoretinopathy. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5475) · Entrez [3489](https://www.ncbi.nlm.nih.gov/gene/3489) · UniProt [P24592](https://www.uniprot.org/uniprotkb/P24592) · Ensembl [ENSG00000167779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167779)

## Data

Gene col 9541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9541); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9541]; `tensor/DDL_lfc|DDL_z.npy` [9541]; `embed/gene_vectors.npy` [9541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9541 or target_col == 9541). Every well: [[IGFBP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGFBP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
