---
symbol: "HES6"
type: "gene"
col: 6887
ensembl_id: "ENSG00000144485"
name: "hes family bHLH transcription factor 6"
location: "2q37.3"
module: 24
arm: "+"
pooled_cpm: 4.35
n_lines_expressing: 42
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 22
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# HES6

*hes family bHLH transcription factor 6* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.68× (z +11.9, q 3e-30, up in 34 of 38 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 6.66× (z +11.9, q 3e-30, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.311× (z -3.8, q 0.041, down in 16 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (SHP-77 0.155×, SW480 0.112×; ⚠ cell-cycle shift, would explain all of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 0.0185×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (A498 0.0806×).
> Its strongest partners by |cos| (74 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORAI1]] (+0.60, fdr 2e-05), [[LAGE3]] (+0.60, fdr 5e-04), [[SLC25A4]] (+0.60, fdr 1e-04); moves opposite to [[EIF3F]] (-0.56, fdr 1e-04), [[MKRN5P]] (-0.53, fdr 1e-04), [[XRCC6]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 22 go from it, the strongest it → [[TMEM251]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **6.68×** | +11.9 | 3e-30 | 34/38 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.66×** | +11.9 | 3e-30 | 30/36 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **4.28×** | +9.1 | 1e-17 | 15/15 (SHP-77, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **4.24×** | +9.1 | 2e-17 | 28/36 (SW1417, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **4.44×** | +9.0 | 2e-17 | 4/5 (SHP-77, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.07×** | +8.5 | 2e-15 | 12/16 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.29×** | +7.3 | 2e-11 | 16/25 (AsPC-1, SW1417, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.75×** | +5.9 | 3e-07 | 3/7 (LS 180, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.80×** | +5.2 | 1e-05 | 13/26 (NCI-H460, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.05×** | +4.3 | 8e-04 | 18/34 (NCI-H2347, NCI-H460, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +4.3 | 9e-04 | 13/36 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **2.02×** | +4.3 | 1e-03 | 7/18 (LS 180, SHP-77, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.0 | 0.003 | 8/22 (SW48, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.89×** | +4.0 | 0.003 | 13/36 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.83×** | +3.8 | 0.006 | 11/36 (A-172, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +3.7 | 0.008 | 11/26 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.034 | 10/35 (A-172, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +3.2 | 0.037 | 8/35 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.041 | 8/31 (MIA PaCa-2, HepG2/C3A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.042 | 11/35 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6887.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (SHP-77 0.155×, SW480 0.112×; ⚠ cell-cycle shift, would explain all of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 0.0185×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (A498 0.0806×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -3.8 | 0.041 | 16/31 (SW480, C-33 A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.314×** | -3.8 | 0.041 | 15/28 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0185× (z -9.3) |
| [[A498 (line)]] | wt | 3.48 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0806× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 1.18 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.155× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.879 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 23 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORAI1]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[LAGE3]] | +0.60 | +0.24 / +0.64 | both halves | 5e-04 |  |
| [[SLC25A4]] | +0.60 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[RBM38]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[POLR2H]] | +0.57 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[NUDT8]] | +0.55 | +0.22 / +0.66 | both halves | 6e-04 |  |
| [[PAXX]] ⚠ | +0.54 | +0.26 / +0.61 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[AK1]] | +0.54 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[BCL11B]] | +0.53 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[FLVCR1-DT]] | +0.53 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[SURF2]] | +0.52 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[GLS2]] | +0.52 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[CDIP1]] | +0.52 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3F]] | -0.56 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[MKRN5P]] | -0.53 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[XRCC6]] | -0.49 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[IL18BP]] | -0.49 | -0.20 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[STX16]] | -0.49 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[COPB2-DT]] | -0.48 | -0.05 / -0.52 | ⚠ one half (not replicated) | 0.005 |  |
| [[L3HYPDH]] | -0.48 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[CSDE1]] | -0.47 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[UBQLN1]] | -0.47 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PPIP5K2]] | -0.46 | -0.21 / -0.49 | both halves | 7e-04 |  |
| [[ERH]] | -0.46 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[USP39]] | -0.45 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[AP2B1]] | -0.45 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[UGGT1]] | -0.45 | -0.36 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM251]] | B | HES6 activity raises TMEM251's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without HES6 | 0.005 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ERH]] | B | HES6 activity raises ERH's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without HES6 | 0.007 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MIEN1]] | B | HES6 activity raises MIEN1's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without HES6 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TXNDC17]] | B | HES6 activity raises TXNDC17's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without HES6 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RBM38]] | B | HES6 activity raises RBM38's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without HES6 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[USP39]] | B | HES6 activity raises USP39's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without HES6 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TM7SF2]] | B | HES6 activity raises TM7SF2's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without HES6 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FLVCR1-DT]] | B | HES6 activity raises FLVCR1-DT's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without HES6 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NTN1]] | B | HES6 activity raises NTN1's level | lines that do not express HES6 (8) vs lines expressing it (42) | 3.16× lower at baseline in the lines without HES6 | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LAGE3]] | B | HES6 activity raises LAGE3's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without HES6 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SURF2]] | B | HES6 activity raises SURF2's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.48× lower at baseline in the lines without HES6 | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PPP1R35]] | B | HES6 activity raises PPP1R35's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without HES6 | 0.057 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.4, -18.9); signed map (-30.4, 10.4). **Vector** length 49.3, 8.76% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.3 | +11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.2 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.3 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | hes family bHLH transcription factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:238,238,267-238,240,662 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHb41 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HZ4](https://www.uniprot.org/uniprotkb/Q96HZ4) (Transcription cofactor HES-6):

> Does not bind DNA itself but suppresses both HES1-mediated N box-dependent transcriptional repression and binding of HES1 to E box sequences. Also suppresses HES1-mediated inhibition of the heterodimer formed by ASCL1/MASH1 and TCF3/E47, allowing ASCL1 and TCF3 to up-regulate transcription in its presence. Promotes cell differentiation (By similarity).

**Summary**, from NCBI Gene [55502](https://www.ncbi.nlm.nih.gov/gene/55502):

> This gene encodes a member of a subfamily of basic helix-loop-helix transcription repressors that have homology to the Drosophila enhancer of split genes. Members of this gene family regulate cell differentiation in numerous cell types. The protein encoded by this gene functions as a cofactor, interacting with other transcription factors through a tetrapeptide domain in its C-terminus. Alternatively spliced transcript variants encoding different isoforms have been described.[provided by RefSeq, …

**Accessions** — [HGNC:18254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18254) · Entrez [55502](https://www.ncbi.nlm.nih.gov/gene/55502) · UniProt [Q96HZ4](https://www.uniprot.org/uniprotkb/Q96HZ4) · Ensembl [ENSG00000144485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144485)

## Data

Gene col 6887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6887); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6887]; `tensor/DDL_lfc|DDL_z.npy` [6887]; `embed/gene_vectors.npy` [6887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6887 or target_col == 6887). Every well: [[HES6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HES6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
