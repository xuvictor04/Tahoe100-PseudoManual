---
symbol: "BRSK2"
type: "gene"
col: 10513
ensembl_id: "ENSG00000174672"
name: "BR serine/threonine kinase 2"
location: "11p15.5"
module: 132
arm: "+"
pooled_cpm: 3.3
n_lines_expressing: 36
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 13
direction_downstream: 29
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# BRSK2

*BR serine/threonine kinase 2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.67× (z +9.9, q 2e-20, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.84× (z +9.1, q 4e-17, up in 14 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.576× (z -5.8, q 5e-06, down in 17 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZD4]] (+0.78, fdr 7e-06), [[KIF26A]] (+0.73, fdr 7e-06), [[SHANK3]] (+0.72, fdr 7e-06); moves opposite to [[USP49]] (-0.50, fdr 2e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 29 go from it, the strongest it → [[JAG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.9 | 2e-20 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +9.1 | 4e-17 | 14/32 (HT-29, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.6 | 4e-06 | 1/5 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +5.6 | 4e-06 | 9/27 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.36× | +3.1 | 0.21 | 3/25 (LoVo, SHP-77, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.34× | +3.1 | 0.22 | 2/13 (PANC-1, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.576×** | -5.8 | 5e-06 | 17/31 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.585×** | -5.6 | 6e-06 | 20/28 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.607×** | -5.2 | 3e-05 | 12/30 (A-427, A-172, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -4.6 | 5e-04 | 9/28 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.640×** | -4.5 | 8e-04 | 12/29 (A-427, LOX-IMVI, …) | two highest doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -4.4 | 0.001 | 14/29 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.687×** | -3.9 | 0.007 | 9/32 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.728×** | -3.3 | 0.065 | 10/23 (SW48, LoVo, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.2 | 0.088 | 5/34 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 16.8 | 0 | 3 (2 ⚠) | — | [[Naproxen (drug)]] 0.05 µM 0.0833× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 5.65 | 0 | 3 (1 ⚠) | — | [[Simotinib (drug)]] 0.05 µM 0.0840× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 9.89 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 14.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -14.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 5.11 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.217× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -8.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 2.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.834 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZD4]] | +0.78 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[KIF26A]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SHANK3]] | +0.72 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[GNAZ]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[SEPTIN5]] | +0.70 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[SULT4A1]] | +0.68 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[B4GALNT4]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CHD5]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[PRR5]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[KCNQ2]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[CACNA1H]] | +0.64 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RASGEF1C]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP49]] | -0.50 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises BRSK2's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.21× lower at baseline in the lines without GNAZ | 0.002 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[PAX2]] | B | PAX2 activity raises BRSK2's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without PAX2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[MCOLN2]] | B | MCOLN2 activity raises BRSK2's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without MCOLN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[EBF4]] | B | EBF4 activity raises BRSK2's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without EBF4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[SEPTIN5]] | B | SEPTIN5 activity raises BRSK2's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without SEPTIN5 | 0.014 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[SLC4A3]] | B | SLC4A3 activity raises BRSK2's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.29× lower at baseline in the lines without SLC4A3 | 0.016 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[ELFN1]] | B | ELFN1 activity raises BRSK2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without ELFN1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[MSI1]] | B | MSI1 activity raises BRSK2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.06× lower at baseline in the lines without MSI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[LINC02643]] | B | LINC02643 activity raises BRSK2's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 2.47× lower at baseline in the lines without LINC02643 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530 |
| [[SEPTIN3]] | B | SEPTIN3 activity raises BRSK2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without SEPTIN3 | 0.044 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[BEGAIN]] | B | BEGAIN activity raises BRSK2's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without BEGAIN | 0.053 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[KIF26A]] | C | KIF26A activity raises BRSK2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.48× lower at baseline in the lines without KIF26A | 0.001 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 27, C 2. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | BRSK2 activity raises JAG2's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without BRSK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[ANKRD13B]] | B | BRSK2 activity raises ANKRD13B's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without BRSK2 | 0.014 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[GNAZ]] | B | BRSK2 activity raises GNAZ's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without BRSK2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[ADCY3]] | B | BRSK2 activity raises ADCY3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.74× lower at baseline in the lines without BRSK2 | 0.029 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[KIF3C]] | B | BRSK2 activity raises KIF3C's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without BRSK2 | 0.031 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[GARNL3]] | B | BRSK2 activity raises GARNL3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without BRSK2 | 0.034 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[TMEM201]] | B | BRSK2 activity raises TMEM201's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without BRSK2 | 0.037 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[FAM78B]] | B | BRSK2 activity raises FAM78B's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without BRSK2 | 0.043 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[MAPK12]] | B | BRSK2 activity raises MAPK12's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without BRSK2 | 0.046 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[SEPTIN3]] | B | BRSK2 activity raises SEPTIN3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.68× lower at baseline in the lines without BRSK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[PHF21B]] | B | BRSK2 activity raises PHF21B's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 3.33× lower at baseline in the lines without BRSK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[LRP3]] | B | BRSK2 activity raises LRP3's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without BRSK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 40.9); signed map (-23.9, 36.4). **Vector** length 42.5, 5.93% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +5.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.0 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.6 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | BR serine/threonine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,389,899-1,462,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEN11B, SAD-A; previously C11orf7, STK29 |
| Gene groups (HGNC) | BR serine/threonine kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWQ3](https://www.uniprot.org/uniprotkb/Q8IWQ3) (Serine/threonine-protein kinase BRSK2):

> Serine/threonine-protein kinase that plays a key role in polarization of neurons and axonogenesis, cell cycle progress and insulin secretion. Phosphorylates CDK16, CDC25C, MAPT/TAU, PAK1 and WEE1. Following phosphorylation and activation by STK11/LKB1, acts as a key regulator of polarization of cortical neurons, probably by mediating phosphorylation of microtubule-associated proteins such as MAPT/TAU at 'Thr-529' and 'Ser-579'. Also regulates neuron polarization by mediating phosphorylation of …

**Summary**, from NCBI Gene [9024](https://www.ncbi.nlm.nih.gov/gene/9024):

> Enables several functions, including ATP binding activity; ATPase binding activity; and magnesium ion binding activity. Involved in several processes, including G2/M transition of mitotic cell cycle; intrinsic apoptotic signaling pathway in response to endoplasmic reticulum stress; and regulation of insulin secretion involved in cellular response to glucose stimulus. Located in centrosome and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11405) · Entrez [9024](https://www.ncbi.nlm.nih.gov/gene/9024) · UniProt [Q8IWQ3](https://www.uniprot.org/uniprotkb/Q8IWQ3) · Ensembl [ENSG00000174672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174672)

## Data

Gene col 10513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10513); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10513]; `tensor/DDL_lfc|DDL_z.npy` [10513]; `embed/gene_vectors.npy` [10513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10513 or target_col == 10513). Every well: [[BRSK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRSK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
