---
symbol: "DUS3L"
type: "gene"
col: 6589
ensembl_id: "ENSG00000141994"
name: "dihydrouridine synthase 3 like"
location: "19p13.3"
module: 1
arm: "+"
pooled_cpm: 8.25
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DUS3L

*dihydrouridine synthase 3 like* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.00× (z +9.5, q 1e-18, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.331× (z -15.1, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QTRT1]] (+0.76, fdr 7e-06), [[ARMC6]] (+0.73, fdr 7e-06), [[DHX37]] (+0.72, fdr 7e-06); moves opposite to [[ARL3]] (-0.62, fdr 1e-05), [[SPAG9]] (-0.62, fdr 3e-05), [[OSTF1]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RALGPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +9.5 | 1e-18 | 36/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +8.4 | 1e-14 | 28/45 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +8.0 | 2e-13 | 26/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +7.8 | 6e-13 | 31/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +7.5 | 7e-12 | 26/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +6.9 | 7e-10 | 20/39 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.37×** | +6.1 | 8e-08 | 21/46 (A-172, A498, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +5.8 | 5e-07 | 19/44 (RPMI-7951, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.6 | 2e-06 | 19/46 (A-172, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +5.4 | 4e-06 | 8/21 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +5.3 | 5e-06 | 14/46 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.48×** | +5.3 | 5e-06 | 14/35 (NCI-H460, LoVo, …) | inconsistent across doses | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.0 | 2e-05 | 19/43 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 3e-04 | 13/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.83×** | +4.3 | 6e-04 | 8/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.3 | 7e-04 | 10/47 (NCI-H2347, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.003 | 8/47 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.016 | 5/40 (SW480, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.017 | 5/42 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.019 | 5/45 (SW1417, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.036 | 3/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.331×** | -15.1 | 0e+00 | 46/47 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.399×** | -12.6 | 8e-34 | 41/47 (RPMI-7951, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.450×** | -10.9 | 2e-25 | 37/47 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -10.1 | 7e-22 | 39/47 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.684×** | -7.4 | 2e-11 | 25/47 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.375×** | -7.0 | 2e-10 | 26/47 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.625×** | -6.4 | 1e-08 | 23/45 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.639×** | -6.1 | 6e-08 | 21/46 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -5.4 | 4e-06 | 20/44 (H4, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -4.2 | 0.002 | 8/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.856× | -3.0 | 0.13 | 11/47 (CFPAC-1, SHP-77, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Afatinib (drug)]] 5 µM 0.185× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 3.35 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM 0.0745× (z -8.6) |
| [[H4 (line)]] | wt | 8.98 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0584× (z -8.8) |
| [[Hs 766T (line)]] | wt | 4.78 | 0 | 1 | — | [[APTO-253 (drug)]] 0.05 µM 0.0674× (z -8.5) |
| [[KATO III (line)]] | alt | 5.63 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0974× (z -8.9) |
| [[RKO (line)]] | wt | 12.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -8.6) |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0802× (z -10.4) |
| [[A-172 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QTRT1]] | +0.76 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[DHX37]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[SLC5A6]] | +0.72 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[GRWD1]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 | STRING 447 |
| [[TRMT1]] | +0.68 | +0.58 / +0.68 | both halves | 7e-06 | same gene group; STRING 709 |
| [[UTP20]] | +0.67 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.66 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[HSPBP1]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ZZZ3]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[WARS2]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ATXN7L2]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | -0.62 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SPAG9]] | -0.62 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[OSTF1]] | -0.62 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PJA2]] | -0.61 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[LGALS1]] | -0.59 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ATP11B]] | -0.57 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[WDR44]] | -0.57 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[PCMT1]] | -0.57 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[SH3BGRL3]] | -0.56 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[CIB1]] | -0.56 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[CAST]] | -0.56 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MACO1]] | -0.56 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | RALGPS2 activity lowers DUS3L's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without RALGPS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DUS3L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DUS3L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.8, -33.2); signed map (0.8, -46.3). **Vector** length 67.4, 10.8% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -12.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -15.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +0.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | dihydrouridine synthase 3 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,784,832-5,791,225 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DUS3, FLJ13896 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Dihydrouridine synthase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G46](https://www.uniprot.org/uniprotkb/Q96G46) (tRNA-dihydrouridine(47) synthase):

> Catalyzes the synthesis of dihydrouridine, a modified base, in various RNAs, such as tRNAs, mRNAs and some long non-coding RNAs (lncRNAs). Mainly modifies the uridine in position 47 (U47) in the D-loop of most cytoplasmic tRNAs. Also able to mediate the formation of dihydrouridine in some mRNAs, thereby regulating their translation.

**Summary**, from NCBI Gene [56931](https://www.ncbi.nlm.nih.gov/gene/56931):

> Enables mRNA dihydrouridine synthase activity and tRNA-dihydrouridine47 synthase activity. Involved in regulation of translation and tRNA dihydrouridine synthesis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26920) · Entrez [56931](https://www.ncbi.nlm.nih.gov/gene/56931) · UniProt [Q96G46](https://www.uniprot.org/uniprotkb/Q96G46) · Ensembl [ENSG00000141994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141994)

## Data

Gene col 6589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6589); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6589]; `tensor/DDL_lfc|DDL_z.npy` [6589]; `embed/gene_vectors.npy` [6589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6589 or target_col == 6589). Every well: [[DUS3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUS3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
