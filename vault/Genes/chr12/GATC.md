---
symbol: "GATC"
type: "gene"
col: 15024
ensembl_id: "ENSG00000257218"
name: "glutamyl-tRNA amidotransferase subunit C"
location: "12q24.31"
module: 124
arm: "+"
pooled_cpm: 24.74
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# GATC

*glutamyl-tRNA amidotransferase subunit C* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +12.8, q 7e-35, up in 35 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.71× (z +8.1, q 7e-14, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.905× (z -4.9, q 6e-04, down in 1 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.571× (z -4.4, q 0.003, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.308×, RKO 0.346×, NCI-H460 0.487×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.136×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN10]] (+0.63, fdr 2e-05), [[ITPA]] (+0.59, fdr 3e-05), [[NSD1]] (+0.56, fdr 4e-05); moves opposite to [[RAB3A]] (-0.60, fdr 8e-05), [[DMBX1]] (-0.55, fdr 3e-05), [[FHIP1B]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02057]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.33×** | +12.8 | 7e-35 | 35/42 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +12.7 | 2e-34 | 27/36 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +9.4 | 7e-19 | 33/41 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +8.1 | 7e-14 | 36/47 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +7.3 | 5e-11 | 38/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.3 | 2e-08 | 30/46 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.3 | 2e-08 | 29/47 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +5.9 | 3e-07 | 32/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.42×** | +5.1 | 2e-05 | 24/48 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-05 | 27/48 (A498, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 2e-05 | 22/47 (A498, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.41×** | +5.0 | 3e-05 | 28/47 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.38×** | +4.9 | 5e-05 | 24/45 (A-427, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +4.5 | 3e-04 | 22/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.32×** | +4.3 | 8e-04 | 22/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 22/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.002 | 21/48 (A498, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.005 | 12/47 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.021 | 18/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.030 | 10/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15024.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.308×, RKO 0.346×, NCI-H460 0.487×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.9 | 6e-04 | 1/48 (HOP62) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.571×** | -4.4 | 0.003 | 28/48 (C32, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.603×** | -4.0 | 0.013 | 21/48 (SW48, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Baicalin (drug)]] 5 µM |  | 0.855× | -3.3 | 0.13 | 10/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.816× | -3.0 | 0.27 | 14/47 (hTERT-HPNE, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 19.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 32.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.26× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 39.1 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.136× (z -11.2) |
| [[A-172 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN10]] | +0.63 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ITPA]] | +0.59 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[NSD1]] | +0.56 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[UTP20]] | +0.56 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[TRMT10A]] | +0.55 | +0.55 / +0.37 | both halves | 7e-05 |  |
| [[SMIM15]] | +0.55 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[CRPPA]] | +0.54 | +0.59 / +0.24 | both halves | 5e-04 |  |
| [[PAK2]] | +0.53 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[AVEN]] | +0.53 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[FTX]] | +0.52 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[RXYLT1]] | +0.52 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[C17orf80]] | +0.51 | +0.56 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.60 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[DMBX1]] | -0.55 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[FHIP1B]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[EFEMP2]] | -0.53 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[KMT5C]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[POGLUT2]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[GBF1]] | -0.52 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[LTBP4]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ADGRB2]] | -0.52 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[ETHE1]] | -0.51 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[AHDC1]] | -0.51 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[ANO8]] | -0.51 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02057]] | B | LINC02057 activity lowers GATC's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.36× higher at baseline in the lines without LINC02057 | 0.001 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[TOP2A]] | B | TOP2A activity lowers GATC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (6.6, -7.0); signed map (20.9, -29.1). **Vector** length 64.1, 11.5% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.3 | +12.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Pimitespib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | glutamyl-tRNA amidotransferase subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,446,444-120,463,749 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37000, 15E1.2 |
| Gene groups (HGNC) | Glutamyl-tRNA amidotransferase subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O43716](https://www.uniprot.org/uniprotkb/O43716) (Glutamyl-tRNA(Gln) amidotransferase subunit C, mitochondrial):

> Structural subunit of the mitochondrial Glu-tRNA(Gln) amidotransferase complex GatCAB. GatCAB allows the formation of correctly charged Gln-tRNA(Gln) through the transamidation of misacylated Glu-tRNA(Gln) in the mitochondria. The reaction takes place in the presence of glutamine and ATP through an activated gamma-phospho-Glu-tRNA(Gln) (By similarity). This subunit probably forms a belt that wraps around the interface of the catalytic subunits A and B to stabilize the complex (Probable).

**Summary**, from NCBI Gene [283459](https://www.ncbi.nlm.nih.gov/gene/283459):

> Predicted to enable ATP binding activity and glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity. Involved in glutaminyl-tRNAGln biosynthesis via transamidation and mitochondrial translation. Located in mitochondrion. Part of glutamyl-tRNA(Gln) amidotransferase complex. Implicated in combined oxidative phosphorylation deficiency 42. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25068) · Entrez [283459](https://www.ncbi.nlm.nih.gov/gene/283459) · UniProt [O43716](https://www.uniprot.org/uniprotkb/O43716) · Ensembl [ENSG00000257218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257218)

## Data

Gene col 15024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15024); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15024]; `tensor/DDL_lfc|DDL_z.npy` [15024]; `embed/gene_vectors.npy` [15024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15024 or target_col == 15024). Every well: [[GATC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
