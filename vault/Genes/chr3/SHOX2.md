---
symbol: "SHOX2"
type: "gene"
col: 9697
ensembl_id: "ENSG00000168779"
name: "SHOX homeobox 2"
location: "3q25.32"
module: 46
arm: "+"
pooled_cpm: 15.07
n_lines_expressing: 36
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# SHOX2

*SHOX homeobox 2* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +14.8, q 0e+00, up in 28 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.414× (z -10.3, q 3e-22, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXD11]] (+0.67, fdr 1e-05), [[HOXB-AS1]] (+0.66, fdr 8e-05), [[GNAS]] (+0.61, fdr 2e-05); moves opposite to [[FARSB]] (-0.59, fdr 3e-05), [[MRPL24]] (-0.56, fdr 5e-05), [[COG2]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 8 go from it, the strongest it → [[CNPY4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +14.8 | 0e+00 | 28/32 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.5 | 2e-08 | 18/30 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.1 | 8e-05 | 12/28 (Panc 03.27, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 0.001 | 10/33 (HOP62, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.002 | 12/31 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.007 | 13/32 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.010 | 12/34 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.043 | 11/30 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.073 | 8/32 (MIA PaCa-2, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.414×** | -10.3 | 3e-22 | 25/33 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.464×** | -9.0 | 7e-17 | 23/32 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.604×** | -8.3 | 2e-14 | 19/33 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.496×** | -8.2 | 3e-14 | 19/33 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -7.1 | 2e-10 | 18/31 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.396×** | -5.7 | 1e-06 | 20/30 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -4.4 | 1e-03 | 16/34 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -4.0 | 0.004 | 15/33 (NCI-H460, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.568×** | -3.5 | 0.034 | 9/20 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -3.3 | 0.048 | 10/32 (C-33 A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -3.2 | 0.077 | 4/34 (A549, C32, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.772× | -3.0 | 0.12 | 4/33 (A498, A-172, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 73.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -20.7) |
| [[HS-578T (line)]] | alt | 55.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -18.4) |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 0 | 4 | — | [[vincristine (drug)]] 0.05 µM 0.151× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 13.9 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.4) |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -12.7) |
| [[A498 (line)]] | wt | 33.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -11.6) |
| [[HOP62 (line)]] | alt | 35.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0694× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 41.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.202× (z -10.9) |
| [[H4 (line)]] | wt | 32.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 17.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -11.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -9.4) |
| [[A549 (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.0) | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -9.2) |
| [[LoVo (line)]] | wt | 9.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +14.2) | — |
| [[SW480 (line)]] | alt | 5.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +12.0) | — |
| [[A-427 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXD11]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HOXB-AS1]] | +0.66 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[GNAS]] | +0.61 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[HOXC9]] | +0.60 | +0.35 / +0.48 | both halves | 1e-04 | STRING 541 |
| [[HOXD10]] | +0.58 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[KIF9-AS1]] | +0.58 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[ACOT2]] | +0.57 | +0.27 / +0.46 | both halves | 3e-04 |  |
| [[ARID4B]] | +0.57 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[BTN2A1]] | +0.56 | +0.37 / +0.51 | both halves | 7e-05 |  |
| [[FLT3LG]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZNF821]] | +0.56 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[C2]] | +0.55 | +0.38 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARSB]] | -0.59 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[MRPL24]] | -0.56 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[COG2]] | -0.55 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[TRAP1]] | -0.54 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[CLYBL]] | -0.54 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ATIC]] | -0.53 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[RUVBL1]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[CCT2]] | -0.52 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[LAS1L]] | -0.52 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[TSEN2]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[SMYD3]] | -0.51 | -0.36 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SHOX2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers SHOX2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises SHOX2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DZIP1L]] | C | DZIP1L activity raises SHOX2's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 4.56× lower at baseline in the lines without DZIP1L | 0.015 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNPY4]] | B | SHOX2 activity raises CNPY4's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without SHOX2 | 0.020 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[KIF9-AS1]] | B | SHOX2 activity raises KIF9-AS1's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without SHOX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[NCOA1]] | B | SHOX2 activity raises NCOA1's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.33× lower at baseline in the lines without SHOX2 | 0.046 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[WDR35]] | B | SHOX2 activity raises WDR35's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 2.41× lower at baseline in the lines without SHOX2 | 0.062 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[WBP4]] | B | SHOX2 activity raises WBP4's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.16× lower at baseline in the lines without SHOX2 | 0.085 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[LAS1L]] | B | SHOX2 activity raises LAS1L's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without SHOX2 | 0.089 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[TSTD3]] | B | SHOX2 activity raises TSTD3's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without SHOX2 | 0.092 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[DZIP1L]] | C | SHOX2 activity raises DZIP1L's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 2.72× lower at baseline in the lines without SHOX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (4.2, 25.7); signed map (35.9, -4.2). **Vector** length 75.9, 18.5% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +14.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | SHOX homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,095,905-158,106,420 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SHOT, OG12X, OG12 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Hallmark sets | KRAS_SIGNALING_DN, UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [O60902](https://www.uniprot.org/uniprotkb/O60902) (Short stature homeobox protein 2):

> May be a growth regulator and have a role in specifying neural systems involved in processing somatosensory information, as well as in face and body structure formation.

**Summary**, from NCBI Gene [6474](https://www.ncbi.nlm.nih.gov/gene/6474):

> This gene is a member of the homeobox family of genes that encode proteins containing a 60-amino acid residue motif that represents a DNA binding domain. Homeobox genes have been characterized extensively as transcriptional regulators involved in pattern formation in both invertebrate and vertebrate species. Several human genetic disorders are caused by aberrations in human homeobox genes. This locus represents a pseudoautosomal homeobox gene that is thought to be responsible for idiopathic …

**Accessions** — [HGNC:10854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10854) · Entrez [6474](https://www.ncbi.nlm.nih.gov/gene/6474) · UniProt [O60902](https://www.uniprot.org/uniprotkb/O60902) · Ensembl [ENSG00000168779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168779)

## Data

Gene col 9697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9697); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9697]; `tensor/DDL_lfc|DDL_z.npy` [9697]; `embed/gene_vectors.npy` [9697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9697 or target_col == 9697). Every well: [[SHOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
