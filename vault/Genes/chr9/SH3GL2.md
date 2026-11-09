---
symbol: "SH3GL2"
type: "gene"
col: 2843
ensembl_id: "ENSG00000107295"
name: "SH3 domain containing GRB2 like 2, endophilin A1"
location: "9p22.2"
module: 61
arm: "+"
pooled_cpm: 5.24
n_lines_expressing: 32
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SH3GL2

*SH3 domain containing GRB2 like 2, endophilin A1* — 9p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 7.41× (z +31.9, q 0e+00, up in 24 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.149×, J82 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 0.144×, HEC-1-A 0.185×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 0.104×; ⚠ toxic; transcription drop); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H460 0.0628×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDLIM3]] (+0.66, fdr 7e-06), [[COLEC12]] (+0.64, fdr 1e-05), [[SLC35F1]] (+0.63, fdr 9e-06); moves opposite to [[KPNA6]] (-0.53, fdr 2e-05), [[PARG]] (-0.53, fdr 6e-05), [[IVD]] (-0.52, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[WIPF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **7.41×** | +31.9 | 0e+00 | 24/25 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **7.03×** | +31.1 | 0e+00 | 20/20 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **11.1×** | +27.2 | 0e+00 | 25/26 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.02×** | +24.8 | 0e+00 | 25/26 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.25×** | +23.0 | 0e+00 | 15/21 (A549, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.96×** | +20.1 | 0e+00 | 24/26 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.63×** | +17.3 | 0e+00 | 24/25 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.04×** | +15.7 | 0e+00 | 24/26 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.66×** | +14.6 | 0e+00 | 20/21 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +13.9 | 3e-42 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.82×** | +11.2 | 2e-27 | 21/23 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +9.0 | 1e-17 | 8/18 (HCT15, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.0 | 8e-14 | 8/21 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +7.5 | 2e-12 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.42×** | +7.2 | 2e-11 | 19/24 (LoVo, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.1 | 4e-08 | 7/22 (HCT15, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +5.9 | 1e-07 | 8/26 (HEC-1-A, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 1e-07 | 7/26 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 3e-05 | 10/25 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2843.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.149×, J82 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 0.144×, HEC-1-A 0.185×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 0.104×; ⚠ toxic; transcription drop); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H460 0.0628×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -3.5 | 0.31 | 5/28 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.750× | -3.0 | 0.58 | 4/25 (SNU-423, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.48 | 14 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 46.5× (z +17.4) | [[Benproperine (phosphate) (drug)]] 5 µM 0.0628× (z -8.6) |
| [[LoVo (line)]] | wt | 11.9 | 7 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 12.8× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 42.5 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 3.43 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 19.9× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.96× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 3.22 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.1× (z +15.3) | — |
| [[SW 900 (line)]] | alt | 20.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -9.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.4× (z +13.6) | — |
| [[A-172 (line)]] | wt | 3.28 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +12.2) | — |
| [[C32 (line)]] | wt | 7.01 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 9.54× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 1.68 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 68.1× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 1.41 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.0× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 2.46 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 15.1× (z +10.6) | — |
| [[SW480 (line)]] | alt | 1.65 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 34.0× (z +14.1) | — |
| [[HCT15 (line)]] | alt | 65.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.62 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 12.7× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 2.04 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 73.9× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 10.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.34× (z +10.5) | — |
| [[A498 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.889 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM3]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[COLEC12]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SLC35F1]] | +0.63 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[PCSK2]] | +0.63 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[SGCZ]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ELAVL2]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[C11orf96]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[STX11]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[HS6ST3]] | +0.60 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[STXBP5L]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SYN1]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 | STRING 543 |
| [[RGS7]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA6]] | -0.53 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[PARG]] | -0.53 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[IVD]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[TRMT61B]] | -0.50 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[NAGPA]] | -0.50 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[ZCCHC4]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[APTX]] | -0.49 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[PSKH1]] | -0.48 | -0.29 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SH3GL2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.6% of all compounds | 0.011 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[WIPF3]] | B | WIPF3 activity raises SH3GL2's level | lines that do not express WIPF3 (21) vs lines expressing it (29) | 2.17× lower at baseline in the lines without WIPF3 | 0.057 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3 |
| [[ARC]] | B | ARC activity lowers SH3GL2's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.65× higher at baseline in the lines without ARC | 0.069 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[KCNG3]] | B | KCNG3 activity raises SH3GL2's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without KCNG3 | 0.081 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |
| [[SLC16A10]] | C | SLC16A10 activity raises SH3GL2's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without SLC16A10 | 0.017 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2; co-absent with the target |
| [[SLAIN1]] | C | SLAIN1 activity raises SH3GL2's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without SLAIN1 | 0.092 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |
| [[NTN1]] | C | NTN1 activity raises SH3GL2's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without NTN1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WIPF3]] | B | SH3GL2 activity raises WIPF3's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without SH3GL2 | 0.045 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent |
| [[CA13]] | B | SH3GL2 activity lowers CA13's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 1.74× higher at baseline in the lines without SH3GL2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent |
| [[TBC1D9]] | B | SH3GL2 activity weakens TBC1D9's drug response | lines that do not express SH3GL2 (14) vs lines expressing it (28) | the lines without SH3GL2 respond 1.27× as strongly (z diff -0.71); strongest at Vinblastine (sulfate) 5 µM: 1.58x vs 1.38x (z diff -1.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CACNA2D2]] | C | SH3GL2 activity raises CACNA2D2's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 2.33× lower at baseline in the lines without SH3GL2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent; co-absent with the target |
| [[SLC16A10]] | C | SH3GL2 activity raises SLC16A10's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without SH3GL2 | 0.029 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent; co-absent with the target |
| [[NTN1]] | C | SH3GL2 activity raises NTN1's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 3.02× lower at baseline in the lines without SH3GL2 | 0.041 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent; co-absent with the target |
| [[OLFM1]] | C | SH3GL2 activity raises OLFM1's level | lines that do not express SH3GL2 (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without SH3GL2 | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.9, 32.7); signed map (33.2, 25.2). **Vector** length 61.0, 12.3% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +31.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.8 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +31.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +13.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +7.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing GRB2 like 2, endophilin A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.2 — chr9:17,579,066-17,797,124 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SH3P4, SH3D2A, CNSA2, EEN-B1 |
| Gene groups (HGNC) | N-BAR domain containing; SH3 domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 24 pathways, smallest: Retrograde neurotrophin signalling; InlB-mediated entry of Listeria monocytogenes into host cell; Listeria monocytogenes entry into host cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99962](https://www.uniprot.org/uniprotkb/Q99962) (Endophilin-A1):

> Implicated in endocytosis. Involved ultrafast endocytosis, by mediating, in a first step, neck formation and in a second step, aids in the removal of clathrin coats from the regenerated vesicles. May recruit other proteins to membranes with high curvature. Required for BDNF-dependent dendrite outgrowth. Cooperates with SH3GL2 to mediate BDNF-NTRK2 early endocytic trafficking and signaling from early endosomes.

**Summary**, from NCBI Gene [6456](https://www.ncbi.nlm.nih.gov/gene/6456):

> Enables identical protein binding activity. Involved in negative regulation of blood-brain barrier permeability; negative regulation of gene expression; and negative regulation of signal transduction. Located in perinuclear region of cytoplasm. Implicated in Parkinson's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10831) · Entrez [6456](https://www.ncbi.nlm.nih.gov/gene/6456) · UniProt [Q99962](https://www.uniprot.org/uniprotkb/Q99962) · Ensembl [ENSG00000107295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107295)

## Data

Gene col 2843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2843); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2843]; `tensor/DDL_lfc|DDL_z.npy` [2843]; `embed/gene_vectors.npy` [2843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2843 or target_col == 2843). Every well: [[SH3GL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3GL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
