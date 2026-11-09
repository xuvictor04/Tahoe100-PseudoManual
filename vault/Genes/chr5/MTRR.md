---
symbol: "MTRR"
type: "gene"
col: 4514
ensembl_id: "ENSG00000124275"
name: "5-methyltetrahydrofolate-homocysteine methyltransferase reductase"
location: "5p15.31"
module: 168
arm: "+"
pooled_cpm: 32.33
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# MTRR

*5-methyltetrahydrofolate-homocysteine methyltransferase reductase* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.55× (z +13.2, q 6e-37, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.286×, RKO 0.282×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.0943×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[4EGI-1 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0618×); [[vincristine (drug)]] 5 µM in 1 line (C32 0.0686×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSUN2]] (+0.71, fdr 7e-06), [[TSFM]] (+0.68, fdr 7e-06), [[RNPS1]] (+0.67, fdr 7e-06); moves opposite to [[MARCKS]] (-0.61, fdr 1e-05), [[JMJD1C]] (-0.61, fdr 1e-05), [[IER5]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CCDC88A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +13.2 | 6e-37 | 47/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +12.6 | 7e-34 | 46/48 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +12.0 | 6e-31 | 38/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +10.9 | 2e-25 | 46/48 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.33×** | +10.8 | 4e-25 | 45/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.30×** | +8.8 | 1e-16 | 39/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +6.5 | 8e-09 | 28/47 (SW480, HOP62, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.6 | 2e-06 | 29/47 (C-33 A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +5.4 | 5e-06 | 29/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +5.3 | 7e-06 | 27/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +4.8 | 8e-05 | 27/48 (Hs 766T, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +4.7 | 1e-04 | 28/48 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.7 | 1e-04 | 25/48 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.38×** | +4.4 | 5e-04 | 25/48 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.001 | 22/48 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.001 | 23/48 (HT-29, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.035 | 19/48 (Hs 766T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.053 | 10/48 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.072 | 12/48 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.076 | 15/47 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4514.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.286×, RKO 0.282×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.0943×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[4EGI-1 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0618×); [[vincristine (drug)]] 5 µM in 1 line (C32 0.0686×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 5 µM |  | 0.841× | -3.5 | 0.13 | 17/48 (SW 1088, HS-578T, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.786× | -3.4 | 0.13 | 19/48 (BT-474, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.788× | -3.4 | 0.13 | 17/44 (A-427, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 25.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.92× (z +10.8) | — |
| [[A-172 (line)]] | wt | 18.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 31.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 25.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.41× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 27.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.7) | — |
| [[SW480 (line)]] | alt | 43.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.26× (z +9.2) | — |
| [[A-427 (line)]] | wt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -11.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0943× (z -13.3) |
| [[C32 (line)]] | wt | 27.1 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0686× (z -9.5) |
| [[LoVo (line)]] | wt | 34.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.7) | — |
| [[NCI-H661 (line)]] | alt | 48.7 | 0 | 1 | — | [[4EGI-1 (drug)]] 0.05 µM 0.0618× (z -10.0) |
| [[RKO (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN2]] | +0.71 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[TSFM]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RNF4]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[WDR5]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GPD1L]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[FAR1]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ENOPH1]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[UBP1]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RPIA]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[RPSA]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives |
| [[WDR3]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCKS]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[JMJD1C]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[IER5]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TUBB2A]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SLC31A2]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[JUND]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[DYNLL1]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[ERVK3-1]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HDAC9]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[OFD1]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[JUN]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[LRCH3]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC88A]] | B | CCDC88A activity raises MTRR's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without CCDC88A | 0.012 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[CRYM]] | B | CRYM activity lowers MTRR's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without CRYM | 0.033 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[KIAA1217]] | B | KIAA1217 activity lowers MTRR's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 1.32× higher at baseline in the lines without KIAA1217 | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[DUSP10]] | B | DUSP10 activity lowers MTRR's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 1.25× higher at baseline in the lines without DUSP10 | 0.084 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[ATXN1]] | B | ATXN1 activity lowers MTRR's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.32× higher at baseline in the lines without ATXN1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[GPD1L]] | C | GPD1L activity raises MTRR's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without GPD1L | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-8.4, -16.1); signed map (-41.7, -15.7). **Vector** length 76.0, 16.8% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.9 | +6.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.2 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | 5-methyltetrahydrofolate-homocysteine methyltransferase reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:7,851,186-7,906,025 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cblE |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 12 pathways, smallest: Cobalamin (Cbl) metabolism; Methylation; Defects in cobalamin (B12) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBK8](https://www.uniprot.org/uniprotkb/Q9UBK8) (Methionine synthase reductase):

> Key enzyme in methionine and folate homeostasis responsible for the reactivation of methionine synthase (MTR/MS) activity by catalyzing the reductive methylation of MTR-bound cob(II)alamin. Cobalamin (vitamin B12) forms a complex with MTR to serve as an intermediary in methyl transfer reactions that cycles between MTR-bound methylcob(III)alamin and MTR bound-cob(I)alamin forms, and occasional oxidative escape of the cob(I)alamin intermediate during the catalytic cycle leads to the inactive …

**Summary**, from NCBI Gene [4552](https://www.ncbi.nlm.nih.gov/gene/4552):

> This gene encodes a member of the ferredoxin-NADP(+) reductase (FNR) family of electron transferases. This protein functions in the synthesis of methionine by regenerating methionine synthase to a functional state. Because methionine synthesis requires methyl-group transfer by a folate donor, activity of the encoded enzyme is important for folate metabolism and cellular methylation. Mutations in this gene can cause homocystinuria-megaloblastic anemia, cbl E type. Alternative splicing of this …

**Accessions** — [HGNC:7473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7473) · Entrez [4552](https://www.ncbi.nlm.nih.gov/gene/4552) · UniProt [Q9UBK8](https://www.uniprot.org/uniprotkb/Q9UBK8) · Ensembl [ENSG00000124275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124275)

## Data

Gene col 4514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4514); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4514]; `tensor/DDL_lfc|DDL_z.npy` [4514]; `embed/gene_vectors.npy` [4514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4514 or target_col == 4514). Every well: [[MTRR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTRR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
