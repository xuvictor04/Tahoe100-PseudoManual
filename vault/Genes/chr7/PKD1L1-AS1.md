---
symbol: "PKD1L1-AS1"
type: "gene"
col: 5850
ensembl_id: "ENSG00000136275"
name: "PKD1L1 antisense RNA 1"
location: "7p12.3"
module: 13
arm: "+"
pooled_cpm: 6.29
n_lines_expressing: 14
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 16
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PKD1L1-AS1

*PKD1L1 antisense RNA 1* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.36× (z +10.1, q 2e-21, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +6.3, q 5e-08, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.537× (z -4.5, q 0.004, down in 9 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.178×, SK-MEL-2 0.111×, J82 0.0646×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.0947×, SNU-423 0.146×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-423 0.0667×, J82 0.0590×); [[Harringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.104×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABI3BP]] (+0.65, fdr 1e-05), [[PTGFR]] (+0.57, fdr 1e-05), [[APBB1IP]] (+0.56, fdr 7e-06); moves opposite to [[ADAMTS9]] (-0.49, fdr 4e-05), [[PCAT1]] (-0.48, fdr 4e-04), [[ANK3]] (-0.47, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[THRB]] → it (grade B ⚠); 16 go from it, the strongest it → [[THBS2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.36×** | +10.1 | 2e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.08×** | +8.1 | 2e-13 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +7.2 | 1e-10 | 1/6 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +6.3 | 5e-08 | 0/9 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.1 | 5e-05 | 1/11 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.7 | 2e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.79×** | +4.2 | 0.003 | 6/11 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.1 | 0.003 | 2/8 (SK-MEL-2, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.75×** | +3.9 | 0.007 | 10/11 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.014 | 7/12 (SNU-423, hTERT-HPNE, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.00×** | +3.5 | 0.020 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.50×** | +3.4 | 0.028 | 1/5 (SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Posaconazole (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.028 | 1/11 (LOX-IMVI) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.063 | 2/11 (SK-MEL-2, AN3 CA) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.063 | 6/10 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.075 | 8/12 (A-172, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.178×, SK-MEL-2 0.111×, J82 0.0646×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 0.0947×, SNU-423 0.146×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-423 0.0667×, J82 0.0590×); [[Harringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.537×** | -4.5 | 0.004 | 9/11 (SNU-423, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.609×** | -3.6 | 0.091 | 7/11 (hTERT-HPNE, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.647× | -3.2 | 0.31 | 6/11 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Malotilate (drug)]] 5 µM |  | 0.660× | -3.0 | 0.31 | 0/11 | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 156 | 1 (1 ⚠) | 6 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +10.4) ⚠ position not correctable | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.104× (z -14.5) |
| [[J82 (line)]] | alt | 7.64 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0947× (z -11.0) |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 3.73 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0438× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.603 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.666 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABI3BP]] | +0.65 | +0.56 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[PTGFR]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[APBB1IP]] | +0.56 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[LINC01411]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ARHGEF6]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[C5orf46]] | +0.55 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[LINC01615]] | +0.54 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[EML1]] | +0.53 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[COL5A1]] | +0.52 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[GRIN2A]] | +0.52 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[PKIG]] | +0.51 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[P2RX7]] | +0.51 | +0.33 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS9]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PCAT1]] | -0.48 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[ANK3]] | -0.47 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[SLC26A2]] | -0.45 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[MYO5C]] | -0.45 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[POU5F1B]] | -0.45 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[LINC02343]] | -0.44 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[SRGN]] | -0.44 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[KIAA0040]] | -0.44 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[THRB]] | -0.44 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[XDH]] | -0.43 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[FOXC2]] | -0.43 | -0.38 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | B | THRB activity lowers PKD1L1-AS1's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.97× higher at baseline in the lines without THRB | 0.062 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[MYO5C]] | B | MYO5C activity lowers PKD1L1-AS1's level | lines that do not express MYO5C (20) vs lines expressing it (30) | 3.34× higher at baseline in the lines without MYO5C | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, EVPL, NCMAP; maybe low, not absent |
| [[COL1A2]] | C | COL1A2 activity raises PKD1L1-AS1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 4.20× lower at baseline in the lines without COL1A2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 4, C 12. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS2-AS1]] | B | PKD1L1-AS1 activity raises THBS2-AS1's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 1.79× lower at baseline in the lines without PKD1L1-AS1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2 |
| [[GXYLT2]] | B | PKD1L1-AS1 activity raises GXYLT2's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 3.05× lower at baseline in the lines without PKD1L1-AS1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2 |
| [[DLG1]] | B | PKD1L1-AS1 activity raises DLG1's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 1.62× lower at baseline in the lines without PKD1L1-AS1 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2 |
| [[ZNF883]] | B | PKD1L1-AS1 activity raises ZNF883's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 2.15× lower at baseline in the lines without PKD1L1-AS1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2 |
| [[COL1A2]] | C | PKD1L1-AS1 activity raises COL1A2's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 14.82× lower at baseline in the lines without PKD1L1-AS1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[APBB1IP]] | C | PKD1L1-AS1 activity raises APBB1IP's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 3.72× lower at baseline in the lines without PKD1L1-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[PDGFRB]] | C | PKD1L1-AS1 activity raises PDGFRB's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 6.33× lower at baseline in the lines without PKD1L1-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[SRGN]] | C | PKD1L1-AS1 activity raises SRGN's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 5.03× lower at baseline in the lines without PKD1L1-AS1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[ADAMTS2]] | C | PKD1L1-AS1 activity raises ADAMTS2's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 3.76× lower at baseline in the lines without PKD1L1-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[SLC8A1]] | C | PKD1L1-AS1 activity raises SLC8A1's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 5.53× lower at baseline in the lines without PKD1L1-AS1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[COL5A2]] | C | PKD1L1-AS1 activity raises COL5A2's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 5.05× lower at baseline in the lines without PKD1L1-AS1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |
| [[KCNE4]] | C | PKD1L1-AS1 activity raises KCNE4's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 4.05× lower at baseline in the lines without PKD1L1-AS1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.386). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.1, 21.0); signed map (29.1, 46.7). **Vector** length 38.6, 11.3% of its response variance represented; |z| ≥ 3 in 360 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.2 | +2.9 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.3 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -0.8 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -0.8 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.7 | -2.3 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -0.7 | -0.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -0.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | PKD1L1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p12.3 — chr7:47,795,291-47,819,847 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ21075; previously C7orf69 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q9H7B7](https://www.uniprot.org/uniprotkb/Q9H7B7) carries no function annotation.

**Summary**, from NCBI Gene [80099](https://www.ncbi.nlm.nih.gov/gene/80099):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21911) · Entrez [80099](https://www.ncbi.nlm.nih.gov/gene/80099) · UniProt [Q9H7B7](https://www.uniprot.org/uniprotkb/Q9H7B7) · Ensembl [ENSG00000136275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136275)

## Data

Gene col 5850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5850); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5850]; `tensor/DDL_lfc|DDL_z.npy` [5850]; `embed/gene_vectors.npy` [5850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5850 or target_col == 5850). Every well: [[PKD1L1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD1L1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
