---
symbol: "CNRIP1"
type: "gene"
col: 4127
ensembl_id: "ENSG00000119865"
name: "cannabinoid receptor interacting protein 1"
location: "2p14"
module: 13
arm: "+"
pooled_cpm: 6.36
n_lines_expressing: 25
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 27
direction_downstream: 43
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CNRIP1

*cannabinoid receptor interacting protein 1* — 2p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.90× (z +15.9, q 0e+00, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +6.6, q 4e-09, up in 2 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.497× (z -12.1, q 1e-30, down in 20 of 22 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAX3]] (+0.64, fdr 1e-05), [[APBB1IP]] (+0.60, fdr 1e-05), [[HS3ST3A1]] (+0.60, fdr 1e-05); moves opposite to [[DLEU1]] (-0.51, fdr 7e-05), [[KIF13B]] (-0.49, fdr 4e-05), [[ARHGEF3]] (-0.49, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[IQANK1]] → it (grade B ⚠); 43 go from it, the strongest it → cells under [[Methylthiouracil (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +15.9 | 0e+00 | 5/12 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +12.4 | 7e-33 | 1/15 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +9.9 | 1e-20 | 2/13 (C32, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.6 | 4e-09 | 2/23 (A549, NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +6.3 | 2e-08 | 11/22 (A-172, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +4.7 | 2e-04 | 6/23 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.7 | 2e-04 | 6/18 (NCI-H460, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 7/23 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.007 | 4/23 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.5 | 0.024 | 3/16 (A-172, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +3.5 | 0.025 | 4/22 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.4 | 0.035 | 3/20 (NCI-H460, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +3.1 | 0.088 | 1/23 (hTERT-HPNE) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.497×** | -12.1 | 1e-30 | 20/22 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.394×** | -11.3 | 2e-27 | 21/23 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.510×** | -8.2 | 4e-14 | 20/23 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -7.5 | 1e-11 | 20/23 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -6.2 | 8e-08 | 14/22 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.630×** | -5.6 | 2e-06 | 17/22 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -4.8 | 1e-04 | 12/22 (C-33 A, H4, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.693×** | -4.5 | 5e-04 | 14/23 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.550×** | -3.8 | 0.009 | 5/18 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.577×** | -3.5 | 0.025 | 14/22 (SHP-77, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.582×** | -3.5 | 0.028 | 6/23 (SHP-77, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 31.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -20.0) |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -16.1) |
| [[C32 (line)]] | wt | 20.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -18.7) |
| [[H4 (line)]] | wt | 43.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.8) |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 7.35 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -19.2) |
| [[SHP-77 (line)]] | alt | 33.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -16.0) |
| [[A-172 (line)]] | wt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -13.8) |
| [[J82 (line)]] | alt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.0) |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 3.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0481× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -8.6) |
| [[A-427 (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.477 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAX3]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[APBB1IP]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HS3ST3A1]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ADAM12]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[WNT5A]] | +0.56 | +0.61 / +0.34 | both halves | 1e-04 | **novel candidate** |
| [[PAPPA]] | +0.55 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[WIPF1]] | +0.55 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[KC6]] | +0.55 | +0.63 / +0.36 | both halves | 9e-05 |  |
| [[ZNF521]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[NETO1]] | +0.54 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[FLI1]] | +0.54 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[AK5]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | -0.51 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[KIF13B]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ARHGEF3]] | -0.49 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ITGB4]] | -0.49 | -0.51 / -0.32 | both halves | 1e-04 |  |
| [[MUC1]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[KCNQ1]] | -0.49 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[TJP2]] | -0.49 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[PATJ]] | -0.48 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[EPB41L1]] | -0.47 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[TMEM184A]] | -0.46 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[SPIRE2]] | -0.45 | -0.44 / -0.24 | both halves | 4e-04 |  |
| [[ASS1]] | -0.45 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 4, C 23. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQANK1]] | B | IQANK1 activity lowers CNRIP1's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 5.69× higher at baseline in the lines without IQANK1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[NOXA1]] | B | NOXA1 activity lowers CNRIP1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 6.61× higher at baseline in the lines without NOXA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[TMC4]] | B | TMC4 activity lowers CNRIP1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 4.11× higher at baseline in the lines without TMC4 | 0.066 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[PTK6]] | B | PTK6 activity lowers CNRIP1's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 3.91× higher at baseline in the lines without PTK6 | 0.090 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[BMPER]] | C | BMPER activity raises CNRIP1's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.65× lower at baseline in the lines without BMPER | 0.008 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises CNRIP1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 6.57× lower at baseline in the lines without GYPC | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises CNRIP1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 6.37× lower at baseline in the lines without MSC-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[DOCK2]] | C | DOCK2 activity raises CNRIP1's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 5.65× lower at baseline in the lines without DOCK2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises CNRIP1's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 5.72× lower at baseline in the lines without HS3ST3A1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises CNRIP1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.76× lower at baseline in the lines without PDE3A | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises CNRIP1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 5.24× lower at baseline in the lines without PAPPA | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[KC6]] | C | KC6 activity raises CNRIP1's level | lines that do not express KC6 (32) vs lines expressing it (18) | 5.88× lower at baseline in the lines without KC6 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 14, C 29. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Methylthiouracil (drug)]] 0.05 µM | B | CNRIP1 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.87× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Fulvestrant (drug)]] 5 µM | B | CNRIP1 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.88× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | CNRIP1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.37× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | CNRIP1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[CLDN14-AS1]] | B | CNRIP1 activity raises CLDN14-AS1's level | lines that do not express CNRIP1 (25) vs lines expressing it (25) | 2.93× lower at baseline in the lines without CNRIP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | B | CNRIP1 activity lowers the cells' numbers under Cabozantinib (S-malate) 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.12× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Macitentan (drug)]] 5 µM | B | CNRIP1 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.21× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 0.5 µM | B | CNRIP1 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.88× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Pemetrexed (drug)]] 5 µM | B | CNRIP1 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.15× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Sunitinib (drug)]] 5 µM | B | CNRIP1 activity lowers the cells' numbers under Sunitinib 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.15× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM | B | CNRIP1 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.13× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | CNRIP1 activity raises the cells' numbers under Lactate (calcium) 0.05 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.85× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 20.2); signed map (26.9, 48.2). **Vector** length 58.0, 14.1% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +15.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +12.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -1.6 | -12.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.3 | -7.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cannabinoid receptor interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p14 — chr2:68,284,171-68,320,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566K1924, CRIP1, CRIP1a, CRIP1b; previously C2orf32 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F85](https://www.uniprot.org/uniprotkb/Q96F85) (CB1 cannabinoid receptor-interacting protein 1):

> [Isoform 1]: Suppresses cannabinoid receptor CNR1-mediated tonic inhibition of voltage-gated calcium channels.; [Isoform 2]: Does not suppress cannabinoid receptor CNR1-mediated tonic inhibition of voltage-gated calcium channels.

**Summary**, from NCBI Gene [25927](https://www.ncbi.nlm.nih.gov/gene/25927):

> This gene encodes a protein that interacts with the C-terminal tail of cannabinoid receptor 1. Two transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:24546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24546) · Entrez [25927](https://www.ncbi.nlm.nih.gov/gene/25927) · UniProt [Q96F85](https://www.uniprot.org/uniprotkb/Q96F85) · Ensembl [ENSG00000119865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119865)

## Data

Gene col 4127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4127); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4127]; `tensor/DDL_lfc|DDL_z.npy` [4127]; `embed/gene_vectors.npy` [4127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4127 or target_col == 4127). Every well: [[CNRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
