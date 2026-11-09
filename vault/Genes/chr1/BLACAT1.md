---
symbol: "BLACAT1"
type: "gene"
col: 15983
ensembl_id: "ENSG00000281406"
name: "BLACAT1 overlapping LEMD1 locus"
location: "1q32.1"
module: 31
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 29
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 53
direction_downstream: 55
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# BLACAT1

*BLACAT1 overlapping LEMD1 locus* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.88× (z +4.2, q 0.016, up in 0 of 8 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.200× (z -15.7, q 0e+00, down in 23 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEMD1]] (+0.91, fdr 7e-06, ⚠ same locus), [[LCK]] (+0.75, fdr 7e-06), [[B3GNT3]] (+0.75, fdr 7e-06), [[PADI1]] (+0.73, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[B4GALNT3]] → it (grade B ⚠); 55 go from it, the strongest it → [[RDH13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +4.2 | 0.016 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.200×** | -15.7 | 0e+00 | 23/23 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.178×** | -11.5 | 5e-28 | 23/25 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.342×** | -10.5 | 2e-23 | 22/22 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.268×** | -9.1 | 2e-17 | 20/21 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.312×** | -8.0 | 1e-13 | 22/26 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.360×** | -7.0 | 2e-10 | 19/26 (SW480, COLO 205, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.362×** | -6.7 | 1e-09 | 18/24 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.377×** | -6.7 | 1e-09 | 17/26 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.392×** | -6.5 | 6e-09 | 16/26 (SW480, LoVo, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.399×** | -6.3 | 1e-08 | 21/26 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.529×** | -5.4 | 3e-06 | 15/26 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.609×** | -4.7 | 1e-04 | 15/26 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.505×** | -4.7 | 1e-04 | 16/26 (SK-MEL-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.514×** | -4.6 | 2e-04 | 15/26 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.289×** | -4.5 | 3e-04 | 16/23 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.612×** | -4.4 | 3e-04 | 14/26 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.597×** | -4.4 | 4e-04 | 15/26 (HEC-1-A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.530×** | -4.2 | 8e-04 | 14/26 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.615×** | -4.0 | 0.002 | 11/26 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.0 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0384× (z -26.5) |
| [[KATO III (line)]] | alt | 14.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0248× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 9.43 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0656× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -17.8) |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0524× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 4.09 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0610× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0357× (z -13.1) |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0700× (z -17.9) |
| [[LS 180 (line)]] | wt | 6.50 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0652× (z -13.0) |
| [[SW48 (line)]] | wt | 12.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0407× (z -14.8) |
| [[A-172 (line)]] | wt | 3.00 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -9.4) |
| [[C32 (line)]] | wt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 7.13 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 6.38 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -8.5) |
| [[A498 (line)]] | wt | 4.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0946× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 7.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0266× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0398× (z -13.4) |
| [[A-427 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.000 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEMD1]] | +0.91 | +0.92 / +0.86 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LCK]] | +0.75 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.75 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[PADI1]] | +0.73 | +0.73 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[EPHA2-AS1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[INPP5D]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TLDC2]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CEACAM1]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GPR35]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[HS3ST1]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 19, C 34. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT3]] | B | B4GALNT3 activity raises BLACAT1's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without B4GALNT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[CARD11]] | B | CARD11 activity raises BLACAT1's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.72× lower at baseline in the lines without CARD11 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[SEMA3B]] | B | SEMA3B activity raises BLACAT1's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without SEMA3B | 0.013 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[ANO1]] | B | ANO1 activity raises BLACAT1's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.42× lower at baseline in the lines without ANO1 | 0.019 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[LAMA3]] | B | LAMA3 activity raises BLACAT1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without LAMA3 | 0.026 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[LINC00659]] | B | LINC00659 activity raises BLACAT1's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without LINC00659 | 0.035 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[PRAG1]] | B | PRAG1 activity raises BLACAT1's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without PRAG1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[MDFI]] | B | MDFI activity raises BLACAT1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.24× lower at baseline in the lines without MDFI | 0.048 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[LINC02474]] | B | LINC02474 activity raises BLACAT1's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 2.23× lower at baseline in the lines without LINC02474 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[LCK]] | B | LCK activity raises BLACAT1's level | lines that do not express LCK (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without LCK | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[MALL]] | B | MALL activity raises BLACAT1's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.01× lower at baseline in the lines without MALL | 0.070 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises BLACAT1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without FKBP9P1-1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |

### Downstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 26, C 29. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDH13]] | B | BLACAT1 activity raises RDH13's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.85× lower at baseline in the lines without BLACAT1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[C3orf18]] | B | BLACAT1 activity lowers C3orf18's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.56× higher at baseline in the lines without BLACAT1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[DEF6]] | B | BLACAT1 activity raises DEF6's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without BLACAT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[B4GALNT3]] | B | BLACAT1 activity raises B4GALNT3's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 3.00× lower at baseline in the lines without BLACAT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[SEMA3B]] | B | BLACAT1 activity raises SEMA3B's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 3.13× lower at baseline in the lines without BLACAT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[SHROOM4]] | B | BLACAT1 activity raises SHROOM4's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without BLACAT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[EPS8L1]] | B | BLACAT1 activity raises EPS8L1's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.86× lower at baseline in the lines without BLACAT1 | 0.025 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[FKBP9P1-1]] | B | BLACAT1 activity raises FKBP9P1-1's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without BLACAT1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[TMC6]] | B | BLACAT1 activity raises TMC6's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.55× lower at baseline in the lines without BLACAT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[RAPGEF5]] | B | BLACAT1 activity raises RAPGEF5's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 3.38× lower at baseline in the lines without BLACAT1 | 0.034 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[FKBP9P1]] | B | BLACAT1 activity raises FKBP9P1's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without BLACAT1 | 0.043 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[TGFA]] | B | BLACAT1 activity raises TGFA's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 3.94× lower at baseline in the lines without BLACAT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 52.3); signed map (3.6, 38.9). **Vector** length 79.7, 22.5% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -0.9 |
|  | [[vincristine (drug)]] 5 µM |  | +1.5 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -11.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | BLACAT1 overlapping LEMD1 locus |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,434,885-205,457,091 (-) |
| Ensembl biotype | protein_coding |
| Also known as | linc-UBC1, LINC00912, onco-lncRNA-30 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48597) · Entrez [101669762](https://www.ncbi.nlm.nih.gov/gene/101669762) · Ensembl [ENSG00000281406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281406)

## Data

Gene col 15983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15983); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15983]; `tensor/DDL_lfc|DDL_z.npy` [15983]; `embed/gene_vectors.npy` [15983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15983 or target_col == 15983). Every well: [[BLACAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLACAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
