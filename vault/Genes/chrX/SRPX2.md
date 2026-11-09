---
symbol: "SRPX2"
type: "gene"
col: 2241
ensembl_id: "ENSG00000102359"
name: "sushi repeat containing protein X-linked 2"
location: "Xq22.1"
module: 151
arm: "+"
pooled_cpm: 9.75
n_lines_expressing: 26
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# SRPX2

*sushi repeat containing protein X-linked 2* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.52× (z +15.1, q 0e+00, up in 16 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.98× (z +11.6, q 1e-28, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.672× (z -4.6, q 0.003, down in 10 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE1C]] (+0.61, fdr 7e-06), [[PAK3]] (+0.60, fdr 1e-05), [[EHD3]] (+0.60, fdr 3e-05); moves opposite to [[LONRF1]] (-0.55, fdr 2e-05), [[ATXN3]] (-0.51, fdr 2e-05), [[HERPUD2]] (-0.51, fdr 1e-04).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CD44]] → it (grade B ⚠); 13 go from it, the strongest it → [[GALNT5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +15.1 | 0e+00 | 16/20 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +14.3 | 1e-43 | 11/14 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +11.6 | 1e-28 | 13/24 (SW1417, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +11.2 | 6e-27 | 13/17 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +8.4 | 3e-15 | 13/23 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.8 | 2e-04 | 7/23 (SNU-423, HOP62, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.74×** | +4.7 | 2e-04 | 4/18 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.7 | 0.013 | 12/23 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.027 | 7/23 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.042 | 6/23 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.045 | 1/23 (SW1417) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.672×** | -4.6 | 0.003 | 10/24 (Panc 03.27, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.722×** | -3.9 | 0.024 | 15/23 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.805×** | -3.7 | 0.040 | 3/24 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.749×** | -3.5 | 0.068 | 11/23 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.744×** | -3.4 | 0.068 | 9/23 (SNU-423, HepG2/C3A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.755× | -3.3 | 0.11 | 10/22 (Panc 03.27, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trifluridine (drug)]] 0.05 µM |  | 0.771× | -3.1 | 0.14 | 2/24 (HepG2/C3A, HOP62) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 22.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.208× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 32.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 65.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.876 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.996 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.921 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE1C]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PAK3]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[EHD3]] | +0.60 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[CDH6]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[F2RL2]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[F2R]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ASPH]] | +0.57 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[LINC02930]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[NF2]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[NCKAP5]] | +0.55 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TLR4]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.54 | +0.46 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LONRF1]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ATXN3]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[HERPUD2]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[NCOA1]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[SOS1]] | -0.47 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[TPRN]] | -0.47 | -0.22 / -0.55 | both halves | 6e-04 |  |
| [[RNF135]] | -0.47 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[CDK19]] | -0.45 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[RSRP1]] | -0.45 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[CHKB]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[FAM76B]] | -0.44 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[RAB11FIP3]] | -0.44 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD44]] | B | CD44 activity raises SRPX2's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.70× lower at baseline in the lines without CD44 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[FN1]] | C | FN1 activity raises SRPX2's level | lines that do not express FN1 (29) vs lines expressing it (21) | 4.27× lower at baseline in the lines without FN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[AMOTL1]] | C | AMOTL1 activity raises SRPX2's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 3.03× lower at baseline in the lines without AMOTL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN; co-absent with the target |
| [[LINC02742]] | C | LINC02742 activity raises SRPX2's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 3.47× lower at baseline in the lines without LINC02742 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227; co-absent with the target |
| [[PAK3]] | C | PAK3 activity raises SRPX2's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 3.45× lower at baseline in the lines without PAK3 | 0.033 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT5]] | B | SRPX2 activity raises GALNT5's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without SRPX2 | 0.019 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[RAB11FIP3]] | B | SRPX2 activity lowers RAB11FIP3's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.32× higher at baseline in the lines without SRPX2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[NHS]] | B | SRPX2 activity raises NHS's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 2.95× lower at baseline in the lines without SRPX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[STIP1]] | B | SRPX2 activity lowers STIP1's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.37× higher at baseline in the lines without SRPX2 | 0.064 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[RSRP1]] | B | SRPX2 activity raises RSRP1's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without SRPX2 | 0.070 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[PALLD]] | B | SRPX2 activity raises PALLD's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without SRPX2 | 0.079 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[TPRN]] | B | SRPX2 activity lowers TPRN's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.36× higher at baseline in the lines without SRPX2 | 0.092 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[AMOTL1]] | C | SRPX2 activity raises AMOTL1's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 3.28× lower at baseline in the lines without SRPX2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1; co-absent with the target |
| [[ADAMTS12]] | C | SRPX2 activity raises ADAMTS12's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 4.73× lower at baseline in the lines without SRPX2 | 0.029 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1; co-absent with the target |
| [[FN1]] | C | SRPX2 activity raises FN1's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 7.63× lower at baseline in the lines without SRPX2 | 0.030 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1; co-absent with the target |
| [[TLR4]] | C | SRPX2 activity raises TLR4's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without SRPX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1; co-absent with the target |
| [[LINC02742]] | C | SRPX2 activity raises LINC02742's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without SRPX2 | 0.069 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.2, 20.2); signed map (21.8, 41.1). **Vector** length 55.7, 13.0% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.4 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | sushi repeat containing protein X-linked 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:100,644,195-100,675,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRPUL |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O60687](https://www.uniprot.org/uniprotkb/O60687) (Sushi repeat-containing protein SRPX2):

> Acts as a ligand for the urokinase plasminogen activator surface receptor. Plays a role in angiogenesis by inducing endothelial cell migration and the formation of vascular network (cords). Involved in cellular migration and adhesion. Increases the phosphorylation levels of FAK. Interacts with and increases the mitogenic activity of HGF. Promotes synapse formation. May have a role in the perisylvian region, critical for language and cognitive development.

**Summary**, from NCBI Gene [27286](https://www.ncbi.nlm.nih.gov/gene/27286):

> This gene encodes a secreted protein that contains three sushi repeat motifs. The encoded protein may play a role in the development of speech and language centers in the brain. This protein may also be involved in angiogenesis. Mutations in this gene are the cause of bilateral perisylvian polymicrogyria, rolandic epilepsy, speech dyspraxia and cognitive disability. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:30668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30668) · Entrez [27286](https://www.ncbi.nlm.nih.gov/gene/27286) · UniProt [O60687](https://www.uniprot.org/uniprotkb/O60687) · Ensembl [ENSG00000102359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102359)

## Data

Gene col 2241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2241); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2241]; `tensor/DDL_lfc|DDL_z.npy` [2241]; `embed/gene_vectors.npy` [2241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2241 or target_col == 2241). Every well: [[SRPX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRPX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
