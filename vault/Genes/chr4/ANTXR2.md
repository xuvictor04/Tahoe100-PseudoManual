---
symbol: "ANTXR2"
type: "gene"
col: 8664
ensembl_id: "ENSG00000163297"
name: "ANTXR cell adhesion molecule 2"
location: "4q21.21"
module: 81
arm: "+"
pooled_cpm: 161.23
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 72
n_dd_up_clean: 0
n_dd_down_clean: 61
in_vector_space: true
direction_upstream: 27
direction_downstream: 31
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# ANTXR2

*ANTXR cell adhesion molecule 2* — 4q21.21

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 6.44×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 4.36×).
> Pooled over the cell lines (median), lowered significantly by 72 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.212× (z -19.7, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2]] (+0.84, fdr 7e-06), [[PRDM8]] (+0.79, fdr 7e-06), [[NT5E]] (+0.79, fdr 7e-06); moves opposite to [[PDLIM1]] (-0.60, fdr 1e-05), [[TSC22D3]] (-0.60, fdr 1e-05), [[CMKLR2]] (-0.56, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[CD44]] → it (grade B ⚠); 31 go from it, the strongest it → [[STX1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8664.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 6.44×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 4.36×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.22× | +3.6 | 0.12 | 19/38 (HepG2/C3A, Hs 766T, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 2.10× | +3.5 | 0.12 | 20/38 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 75 in all, 12 with an alert ⚠; shown: the 15 strongest. 72 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.212×** | -19.7 | 0e+00 | 38/38 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.377×** | -17.5 | 0e+00 | 34/38 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.252×** | -17.5 | 0e+00 | 38/38 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.376×** | -12.4 | 4e-33 | 37/38 (LS 180, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.426×** | -10.8 | 4e-25 | 34/39 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.511×** | -10.5 | 9e-24 | 34/38 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.521×** | -9.8 | 1e-20 | 32/38 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.464×** | -9.7 | 2e-20 | 36/38 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.467×** | -9.7 | 2e-20 | 33/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.481×** | -9.5 | 1e-19 | 34/40 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.480×** | -8.9 | 2e-17 | 29/38 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.484×** | -8.8 | 5e-17 | 33/38 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.530×** | -7.7 | 5e-13 | 30/37 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -7.6 | 9e-13 | 29/38 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.530×** | -7.6 | 1e-12 | 34/38 (HS-578T, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 291 | 0 | 33 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.522× (z -18.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.8) |
| [[LoVo (line)]] | wt | 209 | 0 | 25 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 76.8 | 0 | 24 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -20.9) |
| [[H4 (line)]] | wt | 339 | 0 | 19 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 366 | 0 | 16 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 72.3 | 0 | 16 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 227 | 0 | 14 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.5) |
| [[HS-578T (line)]] | alt | 358 | 0 | 14 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 254 | 0 | 10 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.406× (z -22.5) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.126× (z -15.1) |
| [[LS 180 (line)]] | wt | 695 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0424× (z -22.9) |
| [[NCI-H1792 (line)]] | alt | 519 | 0 | 9 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.480× (z -17.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -16.0) |
| [[BT-474 (line)]] | alt | 60.7 | 0 | 7 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.131× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 77.2 | 0 | 7 | — | [[Trametinib (drug)]] 0.5 µM 0.300× (z -10.4) |
| [[A-172 (line)]] | wt | 155 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -18.5) |
| [[PANC-1 (line)]] | alt | 154 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -15.2) |
| [[RKO (line)]] | wt | 608 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0857× (z -23.2) |
| [[KATO III (line)]] | alt | 79.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 308 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -16.2) |
| [[CHP-212 (line)]] | wt | 218 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.9) |
| [[Hs 766T (line)]] | wt | 184 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 227 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -13.3) |
| [[A549 (line)]] | wt | 46.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.4) |
| [[COLO 205 (line)]] | alt | 102 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 6.44× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.229× (z -11.1) |
| [[HT-29 (line)]] | alt | 102 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 385 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.3) |
| [[J82 (line)]] | alt | 78.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 54.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 129 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -16.0) |
| [[SW 900 (line)]] | alt | 195 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.6) |
| [[A498 (line)]] | wt | 93.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 87.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -14.4) |
| [[SNU-423 (line)]] | alt | 77.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -9.1) |
| [[SW48 (line)]] | wt | 68.8 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.36× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.191× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -8.5) |
| [[C32 (line)]] | wt | 77.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.6) |
| [[SW 1088 (line)]] | alt | 279 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.137× (z -8.6) |
| [[A-427 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 35.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 38.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 27.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2]] | +0.84 | +0.86 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[PRDM8]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | STRING 593 |
| [[NT5E]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[TMEM158]] | +0.72 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CDCP1]] | +0.71 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[MMP1]] | +0.70 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[B4GALT6]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[BCL2A1]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[STC1]] | +0.68 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ITGA2-AS1]] | +0.68 | +0.57 / +0.76 | both halves | 9e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM1]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[TSC22D3]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CMKLR2]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ALDH3B1]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[FLVCR2]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[STOM]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 25, C 2. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD44]] | B | CD44 activity raises ANTXR2's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.27× lower at baseline in the lines without CD44 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[TMEM156]] | B | TMEM156 activity raises ANTXR2's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.76× lower at baseline in the lines without TMEM156 | 0.022 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[MANCR]] | B | MANCR activity raises ANTXR2's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without MANCR | 0.028 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[MIR100HG]] | B | MIR100HG activity raises ANTXR2's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without MIR100HG | 0.035 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[PHLDA2]] | B | PHLDA2 activity raises ANTXR2's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 3.70× lower at baseline in the lines without PHLDA2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[PTGS2]] | B | PTGS2 activity raises ANTXR2's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without PTGS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[FAM107B]] | B | FAM107B activity raises ANTXR2's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without FAM107B | 0.044 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[RFX8]] | B | RFX8 activity raises ANTXR2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.71× lower at baseline in the lines without RFX8 | 0.044 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[BCL2A1]] | B | BCL2A1 activity raises ANTXR2's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without BCL2A1 | 0.047 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[STC1]] | B | STC1 activity raises ANTXR2's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without STC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[S100A16]] | B | S100A16 activity raises ANTXR2's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 3.73× lower at baseline in the lines without S100A16 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[NEBL]] | B | NEBL activity lowers ANTXR2's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.76× higher at baseline in the lines without NEBL | 0.054 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 28, C 3. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STX1A]] | B | ANTXR2 activity raises STX1A's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without ANTXR2 | 0.004 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[VEGFC]] | B | ANTXR2 activity raises VEGFC's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 4.62× lower at baseline in the lines without ANTXR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[JAK1]] | B | ANTXR2 activity raises JAK1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without ANTXR2 | 0.013 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[CD44]] | B | ANTXR2 activity raises CD44's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 5.11× lower at baseline in the lines without ANTXR2 | 0.014 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[TPBG]] | B | ANTXR2 activity raises TPBG's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 3.19× lower at baseline in the lines without ANTXR2 | 0.018 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[TIMP1]] | B | ANTXR2 activity raises TIMP1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without ANTXR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[TSC22D3]] | B | ANTXR2 activity raises TSC22D3's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.74× lower at baseline in the lines without ANTXR2 | 0.025 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[FAM107B]] | B | ANTXR2 activity raises FAM107B's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 3.85× lower at baseline in the lines without ANTXR2 | 0.025 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[PTGS2]] | B | ANTXR2 activity raises PTGS2's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 4.80× lower at baseline in the lines without ANTXR2 | 0.030 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[ITGA2]] | B | ANTXR2 activity raises ITGA2's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 4.16× lower at baseline in the lines without ANTXR2 | 0.036 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[THSD4]] | B | ANTXR2 activity raises THSD4's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 3.33× lower at baseline in the lines without ANTXR2 | 0.039 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[B4GALT1]] | B | ANTXR2 activity raises B4GALT1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without ANTXR2 | 0.043 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.0, 4.8); signed map (5.1, 46.4). **Vector** length 144, 55.2% of its response variance represented; |z| ≥ 3 in 1,970 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.64 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.1 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +7.0 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Vilanterol (drug)]] 0.05 µM |  | +3.0 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -0.2 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | +2.5 | -0.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -11.8 | -9.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -11.0 | -10.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -9.8 | -9.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -9.4 | -10.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -9.2 | -9.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -9.1 | -8.8 |

## What is on record

|  |  |
|---|---|
| Name | ANTXR cell adhesion molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:79,901,146-80,125,454 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CMG2, CMG-2, FLJ31074 |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 3 pathways, smallest: Uptake and function of anthrax toxins; Uptake and actions of bacterial toxins; Bacterial Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [P58335](https://www.uniprot.org/uniprotkb/P58335) (Anthrax toxin receptor 2):

> Necessary for cellular interactions with laminin and the extracellular matrix.; (Microbial infection) Receptor for the protective antigen (PA) of B.anthracis. Binding of PA leads to heptamerization of the receptor-PA complex. Upon binding of the PA of B.anthracis, the complex moves to glycosphingolipid-rich lipid rafts, where it is internalized via a clathrin-dependent pathway. In the endosomal membrane, at pH under 7, the complex then rearranges and forms a pore allowing the other components …

**Summary**, from NCBI Gene [118429](https://www.ncbi.nlm.nih.gov/gene/118429):

> This gene encodes a receptor for anthrax toxin. The protein binds to collagen IV and laminin, suggesting that it may be involved in extracellular matrix adhesion. Mutations in this gene cause juvenile hyaline fibromatosis and infantile systemic hyalinosis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:21732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21732) · Entrez [118429](https://www.ncbi.nlm.nih.gov/gene/118429) · UniProt [P58335](https://www.uniprot.org/uniprotkb/P58335) · Ensembl [ENSG00000163297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163297)

## Data

Gene col 8664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8664); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8664]; `tensor/DDL_lfc|DDL_z.npy` [8664]; `embed/gene_vectors.npy` [8664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8664 or target_col == 8664). Every well: [[ANTXR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANTXR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
