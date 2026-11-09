---
symbol: "ARL4C"
type: "gene"
col: 11972
ensembl_id: "ENSG00000188042"
name: "ARF like GTPase 4C"
location: "2q37.1"
module: 112
arm: "+"
pooled_cpm: 78.38
n_lines_expressing: 36
n_dd_up: 0
n_dd_down: 38
n_dd_up_clean: 0
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 14
direction_downstream: 8
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# ARL4C

*ARF like GTPase 4C* — 2q37.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 4.18×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 5.64×); [[Harringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 4.16×; ⚠ cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.314× (z -16.5, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHB]] (+0.71, fdr 7e-06), [[SYNJ2]] (+0.69, fdr 7e-06), [[IER3]] (+0.67, fdr 7e-06); moves opposite to [[SETD7]] (-0.61, fdr 3e-05), [[CMPK1]] (-0.60, fdr 5e-05), [[ADI1]] (-0.58, fdr 4e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[EVA1A-AS]] → it (grade B ⚠); 8 go from it, the strongest it → [[TMEM200A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 4.18×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 5.64×); [[Harringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 4.16×; ⚠ cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.30× | +3.7 | 0.10 | 17/34 (LS 180, HOP62, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.41× | +3.5 | 0.13 | 24/33 (A549, HEC-1-A, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.37× | +3.3 | 0.21 | 16/34 (AsPC-1, SNU-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.36× | +3.0 | 0.27 | 15/34 (MIA PaCa-2, NCI-H1573, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.27 | 17/34 (HOP62, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.314×** | -16.5 | 0e+00 | 33/34 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.451×** | -7.6 | 1e-11 | 31/34 (HS-578T, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -7.2 | 1e-10 | 29/34 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.510×** | -6.5 | 1e-08 | 24/34 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -6.2 | 6e-08 | 24/34 (HS-578T, HOP62, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.544×** | -6.1 | 8e-08 | 26/34 (A498, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.649×** | -6.1 | 8e-08 | 23/34 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.332×** | -5.8 | 5e-07 | 26/32 (HS-578T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -5.6 | 1e-06 | 24/35 (SNU-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.561×** | -5.6 | 1e-06 | 28/35 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.583×** | -5.4 | 3e-06 | 26/34 (HOP62, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.587×** | -5.3 | 4e-06 | 25/34 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.587×** | -4.9 | 3e-05 | 24/34 (HEC-1-A, LS 180, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.702×** | -4.3 | 6e-04 | 21/34 (A-172, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.733×** | -4.3 | 6e-04 | 23/34 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.663×** | -4.1 | 0.001 | 24/35 (A-172, HEC-1-A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 87.3 | 0 | 13 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -16.0) |
| [[A498 (line)]] | wt | 186 | 0 | 9 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -15.1) |
| [[SNU-1 (line)]] | wt | 547 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -23.8) |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -19.3) |
| [[A-172 (line)]] | wt | 196 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 59.0 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -13.0) |
| [[HS-578T (line)]] | alt | 206 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -23.1) |
| [[MIA PaCa-2 (line)]] | alt | 191 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -24.7) |
| [[RPMI-7951 (line)]] | alt | 284 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0974× (z -24.4) |
| [[SNU-423 (line)]] | alt | 219 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0969× (z -28.2) |
| [[AsPC-1 (line)]] | alt | 31.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +12.4) | — |
| [[A549 (line)]] | wt | 157 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -17.6) |
| [[CFPAC-1 (line)]] | alt | 89.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.9) |
| [[COLO 205 (line)]] | alt | 118 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 68.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.6) |
| [[PANC-1 (line)]] | alt | 82.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -18.2) |
| [[LoVo (line)]] | wt | 77.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -11.0) |
| [[LS 180 (line)]] | wt | 54.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -12.2) |
| [[H4 (line)]] | wt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -19.7) |
| [[NCI-H1573 (line)]] | alt | 67.1 | 0 | 1 | — | [[Triamcinolone (drug)]] 5 µM 0.388× (z -8.6) |
| [[SHP-77 (line)]] | alt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -8.5) |
| [[SW 1088 (line)]] | alt | 99.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -9.2) |
| [[SW 900 (line)]] | alt | 95.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -17.0) |
| [[SW1417 (line)]] | alt | 94.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -13.2) |
| [[SW48 (line)]] | wt | 29.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.128× (z -9.3) |
| [[SW480 (line)]] | alt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -10.5) |
| [[A-427 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.28 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHB]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SYNJ2]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[IER3]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[BCL11B]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RAC2]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CCDC85B]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[STC1]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[FAM43A]] | +0.62 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CLIP2]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.61 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[EHD1]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD7]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[CMPK1]] | -0.60 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[ADI1]] | -0.58 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[METTL4]] | -0.52 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[ATL3]] | -0.52 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[SAP30L-AS1]] | -0.52 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[DERA]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[MGST1]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVA1A-AS]] | B | EVA1A-AS activity raises ARL4C's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.29× lower at baseline in the lines without EVA1A-AS | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[ADAMTS16]] | B | ADAMTS16 activity raises ARL4C's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 3.38× lower at baseline in the lines without ADAMTS16 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[INSYN2B]] | B | INSYN2B activity raises ARL4C's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.15× lower at baseline in the lines without INSYN2B | 0.031 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[ADAMTS14]] | B | ADAMTS14 activity raises ARL4C's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.72× lower at baseline in the lines without ADAMTS14 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[IL1B]] | B | IL1B activity raises ARL4C's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without IL1B | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[TMEM200A]] | B | TMEM200A activity raises ARL4C's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 1.77× lower at baseline in the lines without TMEM200A | 0.041 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[KCNMA1]] | B | KCNMA1 activity raises ARL4C's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without KCNMA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[HIVEP3]] | B | HIVEP3 activity raises ARL4C's level | lines that do not express HIVEP3 (7) vs lines expressing it (43) | 5.97× lower at baseline in the lines without HIVEP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: CD82; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ARL4C's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CYTH4]] | B | CYTH4 activity raises ARL4C's level | lines that do not express CYTH4 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without CYTH4 | 0.067 | ⚠ within organs, on part of the lines; also absent: CSF3, ADTRP, ADAMTS16; maybe low, not absent |
| [[LINC01411]] | B | LINC01411 activity raises ARL4C's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.42× lower at baseline in the lines without LINC01411 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[KIRREL3]] | B | KIRREL3 activity strengthens ARL4C's drug response | lines that do not express KIRREL3 (24) vs lines expressing it (11) | the lines without KIRREL3 respond 0.61× as strongly (z diff +1.95); strongest at Homoharringtonine 5 µM: 0.72x vs 0.51x (z diff +3.3) | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; target measured in part of the lines; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM200A]] | B | ARL4C activity raises TMEM200A's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.32× lower at baseline in the lines without ARL4C | 0.036 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[PCGF5]] | B | ARL4C activity raises PCGF5's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 1.37× lower at baseline in the lines without ARL4C | 0.042 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[INSYN2B]] | B | ARL4C activity raises INSYN2B's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without ARL4C | 0.068 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[EVA1A-AS]] | B | ARL4C activity raises EVA1A-AS's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without ARL4C | 0.072 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[CFAP20DC]] | B | ARL4C activity raises CFAP20DC's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.55× lower at baseline in the lines without ARL4C | 0.082 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[WSCD1]] | B | ARL4C activity raises WSCD1's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without ARL4C | 0.086 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[SYNJ2]] | B | ARL4C activity raises SYNJ2's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without ARL4C | 0.090 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[FAM43A]] | B | ARL4C activity raises FAM43A's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without ARL4C | 0.098 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.5, 0.9); signed map (3.2, 44.4). **Vector** length 134, 42.0% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *inflammatory response* (hallmark, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.5 | +1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -0.0 |
|  | [[Omeprazole (sodium) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.7 | -7.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.3 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.1 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 4C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:234,493,041-234,497,081 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAK; previously ARL7 |
| Gene groups (HGNC) | ARF GTPase family |
| Reactome | 3 pathways, smallest: NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux; NR1H2 and NR1H3-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P56559](https://www.uniprot.org/uniprotkb/P56559) (ADP-ribosylation factor-like protein 4C):

> Small GTP-binding protein which cycles between an inactive GDP-bound and an active GTP-bound form, and the rate of cycling is regulated by guanine nucleotide exchange factors (GEF) and GTPase-activating proteins (GAP). GTP-binding protein that does not act as an allosteric activator of the cholera toxin catalytic subunit. May be involved in transport between a perinuclear compartment and the plasma membrane, apparently linked to the ABCA1-mediated cholesterol secretion pathway. Recruits CYTH1, …

**Summary**, from NCBI Gene [10123](https://www.ncbi.nlm.nih.gov/gene/10123):

> ADP-ribosylation factor-like 4C is a member of the ADP-ribosylation factor family of GTP-binding proteins. ARL4C is closely similar to ARL4A and ARL4D and each has a nuclear localization signal and an unusually high guanine nucleotide exchange rate. This protein may play a role in cholesterol transport. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:698) · Entrez [10123](https://www.ncbi.nlm.nih.gov/gene/10123) · UniProt [P56559](https://www.uniprot.org/uniprotkb/P56559) · Ensembl [ENSG00000188042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188042)

## Data

Gene col 11972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11972); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11972]; `tensor/DDL_lfc|DDL_z.npy` [11972]; `embed/gene_vectors.npy` [11972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11972 or target_col == 11972). Every well: [[ARL4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
