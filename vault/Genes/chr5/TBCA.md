---
symbol: "TBCA"
type: "gene"
col: 10127
ensembl_id: "ENSG00000171530"
name: "tubulin folding cofactor A"
location: "5q14.1"
module: 172
arm: "+"
pooled_cpm: 183.34
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# TBCA

*tubulin folding cofactor A* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.85× (z +14.2, q 5e-43, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.97× (z +8.7, q 6e-16, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEM1]] (+0.67, fdr 7e-06), [[MRPL45P2]] (+0.66, fdr 7e-06), [[LRSAM1]] (+0.63, fdr 1e-05); moves opposite to [[PYGO2]] (-0.56, fdr 1e-04), [[PGM2]] (-0.53, fdr 2e-05), [[C4orf46]] (-0.53, fdr 2e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +14.2 | 5e-43 | 49/49 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +9.9 | 1e-20 | 42/44 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.97×** | +8.7 | 6e-16 | 46/48 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.85×** | +8.4 | 8e-15 | 44/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +8.1 | 5e-14 | 46/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +6.9 | 5e-10 | 41/45 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.49×** | +5.4 | 4e-06 | 43/48 (COLO 205, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.33×** | +3.9 | 0.007 | 33/48 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.8 | 0.008 | 37/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.010 | 40/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.32×** | +3.7 | 0.013 | 31/48 (COLO 205, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.020 | 35/50 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.042 | 39/49 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.042 | 30/49 (NCI-H1573, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.061 | 30/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | 0.763× | -3.7 | 0.14 | 28/48 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 0.849× | -3.1 | 0.47 | 17/48 (HS-578T, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 162 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.17× (z +16.5) | — |
| [[COLO 205 (line)]] | alt | 117 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.84× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 234 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.57× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 216 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.30× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 178 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 132 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.18× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 146 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +9.6) | — |
| [[A549 (line)]] | wt | 206 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.43× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 148 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.31× (z +8.5) | — |
| [[H4 (line)]] | wt | 184 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.21× (z +13.0) | — |
| [[KATO III (line)]] | alt | 147 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.41× (z +8.8) | — |
| [[LoVo (line)]] | wt | 288 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 235 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 206 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.63× (z +9.0) | — |
| [[SW480 (line)]] | alt | 171 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.27× (z +8.5) | — |
| [[A498 (line)]] | wt | 191 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +12.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +12.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +11.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 139 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +14.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 207 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 166 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 255 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 224 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +14.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 185 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +12.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 198 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 158 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.59× (z +8.6) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +14.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 227 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 165 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 214 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 198 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 98.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 296 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 210 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEM1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MRPL45P2]] | +0.66 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[LRSAM1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PFDN4]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 | pathway: Protein folding; STRING 466 |
| [[PIN4]] | +0.62 | +0.67 / +0.66 | both halves | 7e-06 | STRING 497 |
| [[ACOT13]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ANKHD1-EIF4EBP3]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[RABEP1]] | +0.58 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[MAFG]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[LRRC37B]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGO2]] | -0.56 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[PGM2]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[C4orf46]] | -0.53 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[TCF19]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PTPN18]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TMEM214]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SPIN4]] | -0.52 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[SIGMAR1]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[FKBP1A]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[FAM234A]] | -0.51 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[DSCC1]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SSX2IP]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.3, -4.6); signed map (-0.1, -5.5). **Vector** length 99.8, 37.5% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.0 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.4 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.2 | +1.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +1.1 |
| fall | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | -4.4 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -3.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -0.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin folding cofactor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:77,691,166-77,868,780 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Post-chaperonin tubulin folding pathway; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [O75347](https://www.uniprot.org/uniprotkb/O75347) (Tubulin-specific chaperone A):

> Tubulin-folding protein; involved in the early step of the tubulin folding pathway.

**Summary**, from NCBI Gene [6902](https://www.ncbi.nlm.nih.gov/gene/6902):

> The product of this gene is one of four proteins (cofactors A, D, E, and C) involved in the pathway leading to correctly folded beta-tubulin from folding intermediates. Cofactors A and D are believed to play a role in capturing and stabilizing beta-tubulin intermediates in a quasi-native confirmation. Cofactor E binds to the cofactor D/beta-tubulin complex; interaction with cofactor C then causes the release of beta-tubulin polypeptides that are committed to the native state. This gene encodes …

**Accessions** — [HGNC:11579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11579) · Entrez [6902](https://www.ncbi.nlm.nih.gov/gene/6902) · UniProt [O75347](https://www.uniprot.org/uniprotkb/O75347) · Ensembl [ENSG00000171530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171530)

## Data

Gene col 10127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10127); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10127]; `tensor/DDL_lfc|DDL_z.npy` [10127]; `embed/gene_vectors.npy` [10127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10127 or target_col == 10127). Every well: [[TBCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
