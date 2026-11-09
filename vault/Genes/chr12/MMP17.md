---
symbol: "MMP17"
type: "gene"
col: 12626
ensembl_id: "ENSG00000198598"
name: "matrix metallopeptidase 17"
location: "12q24.33"
module: 84
arm: "+"
pooled_cpm: 5.59
n_lines_expressing: 33
n_dd_up: 14
n_dd_down: 29
n_dd_up_clean: 11
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# MMP17

*matrix metallopeptidase 17* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.72× (z +11.6, q 3e-28, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.422× (z -10.0, q 1e-20, down in 18 of 27 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC13A]] (+0.62, fdr 3e-05), [[STX1A]] (+0.61, fdr 3e-05), [[SCUBE1]] (+0.60, fdr 1e-05); moves opposite to [[C12orf60]] (-0.54, fdr 0.001, ⚠ not reproduced), [[DECR1]] (-0.53, fdr 9e-05), [[METTL6]] (-0.53, fdr 2e-04), [[NNT]] (-0.53, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[WASF3]] → it (grade B ⚠); 6 go from it, the strongest it → [[WBP11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.72×** | +11.6 | 3e-28 | 19/30 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +9.9 | 8e-21 | 18/29 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.21×** | +9.2 | 9e-18 | 15/29 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +8.7 | 5e-16 | 15/28 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +8.1 | 6e-14 | 18/28 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.0 | 3e-10 | 3/7 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +5.2 | 2e-05 | 7/23 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.1 | 2e-05 | 9/24 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.1 | 0.003 | 2/18 (A549, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.012 | 6/27 (C32, CHP-212, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +3.4 | 0.032 | 3/10 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.049 | 3/22 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.055 | 2/21 (HOP62, NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Fulvestrant (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.087 | 2/26 (HOP62, NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.422×** | -10.0 | 1e-20 | 18/27 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.439×** | -9.5 | 4e-19 | 18/24 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.482×** | -8.4 | 6e-15 | 14/29 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -7.7 | 1e-12 | 19/30 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.517×** | -7.6 | 3e-12 | 19/28 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -7.3 | 2e-11 | 14/24 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.537×** | -7.2 | 5e-11 | 17/26 (NCI-H23, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -6.0 | 2e-07 | 13/23 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.611×** | -5.7 | 7e-07 | 14/24 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -5.6 | 1e-06 | 11/22 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.630×** | -5.3 | 5e-06 | 14/28 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.639×** | -5.2 | 1e-05 | 10/24 (PANC-1, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -4.8 | 8e-05 | 13/26 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.752×** | -4.7 | 1e-04 | 10/28 (A-427, LOX-IMVI, …) | two highest doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.678×** | -4.5 | 3e-04 | 9/26 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -4.3 | 6e-04 | 14/26 (NCI-H2030, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.7 | 0 | 13 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0734× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.160× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 6.53 | 0 | 7 | — | [[Digitoxin (drug)]] 0.5 µM 0.0419× (z -13.9) |
| [[LoVo (line)]] | wt | 6.30 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.146× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0978× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 7.13 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0693× (z -11.0) |
| [[PANC-1 (line)]] | alt | 7.45 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 6.98× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 7.76 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0938× (z -13.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0902× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0945× (z -10.6) |
| [[SW480 (line)]] | alt | 3.75 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.107× (z -10.0) |
| [[A-172 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.572 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13A]] | +0.62 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[STX1A]] | +0.61 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SCUBE1]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[TMEM255B]] | +0.59 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[KCNN4]] | +0.59 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[CSNK1E]] | +0.59 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[TMEM170B]] | +0.59 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ST8SIA4]] | +0.57 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ATP2A3]] | +0.56 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[CACNG7]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[RASA3]] | +0.56 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[CADM4]] | +0.56 | +0.20 / +0.45 | ⚠ not reproduced | 8e-04 |  |
| [[ETHE1]] | +0.55 | +0.39 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf60]] | -0.54 | -0.37 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[DECR1]] | -0.53 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[METTL6]] | -0.53 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[NNT]] | -0.53 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[RNF146]] | -0.52 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[AHI1-DT]] | -0.52 | -0.35 / -0.24 | both halves | 4e-04 |  |
| [[VBP1]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[MAIP1]] | -0.51 | -0.32 / -0.34 | both halves | 1e-04 |  |
| [[SDHD]] | -0.51 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[DNAI4]] | -0.50 | -0.35 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[GIPC2]] | -0.49 | -0.40 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[PNISR-AS1]] | -0.49 | -0.30 / -0.23 | both halves | 5e-04 |  |
| [[DERA]] | -0.49 | -0.39 / -0.24 | both halves | 4e-04 |  |
| [[WBP11]] | -0.49 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[MRPL11]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WASF3]] | B | WASF3 activity raises MMP17's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without WASF3 | 0.017 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[EBF2]] | B | EBF2 activity raises MMP17's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without EBF2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[RASSF8]] | C | RASSF8 activity raises MMP17's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 2.98× lower at baseline in the lines without RASSF8 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1; co-absent with the target |
| [[RADIL]] | C | RADIL activity raises MMP17's level | lines that do not express RADIL (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without RADIL | 0.090 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WBP11]] | B | MMP17 activity strengthens WBP11's drug response | lines that do not express MMP17 (17) vs lines expressing it (32) | the lines without MMP17 respond 0.93× as strongly (z diff +0.61); strongest at Digitoxin 0.5 µM: 1.46x vs 1.86x (z diff +1.7) | 0.013 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB; target measured in part of the lines; artifact flags |
| [[NPAS1]] | B | MMP17 activity raises NPAS1's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 2.37× lower at baseline in the lines without MMP17 | 0.028 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB |
| [[FBXO27]] | B | MMP17 activity raises FBXO27's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 2.35× lower at baseline in the lines without MMP17 | 0.084 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB |
| [[PDGFA]] | B | MMP17 activity raises PDGFA's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without MMP17 | 0.093 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB |
| [[RASSF8]] | C | MMP17 activity raises RASSF8's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 3.86× lower at baseline in the lines without MMP17 | 0.015 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB; co-absent with the target |
| [[RADIL]] | C | MMP17 activity raises RADIL's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 2.39× lower at baseline in the lines without MMP17 | 0.086 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.5, 33.8); signed map (15.5, 56.6). **Vector** length 54.3, 10.2% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +9.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +11.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:131,828,393-131,851,783 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MT4-MMP |
| Gene groups (HGNC) | M10 matrix metallopeptidases |
| Reactome | 3 pathways, smallest: Activation of Matrix Metalloproteinases; Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULZ9](https://www.uniprot.org/uniprotkb/Q9ULZ9) (Matrix metalloproteinase-17):

> Endopeptidase that degrades various components of the extracellular matrix, such as fibrin. May be involved in the activation of membrane-bound precursors of growth factors or inflammatory mediators, such as tumor necrosis factor-alpha. May also be involved in tumoral process. Cleaves pro-TNF at the '74-Ala-|-Gln-75' site. Not obvious if able to proteolytically activate progelatinase A. Does not hydrolyze collagen types I, II, III, IV and V, gelatin, fibronectin, laminin, decorin nor …

**Summary**, from NCBI Gene [4326](https://www.ncbi.nlm.nih.gov/gene/4326):

> This gene encodes a member of the peptidase M10 family and membrane-type subfamily of matrix metalloproteinases (MMPs). Proteins in this family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. Members of this subfamily contain a transmembrane domain suggesting that these proteins are expressed at the cell surface rather …

**Accessions** — [HGNC:7163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7163) · Entrez [4326](https://www.ncbi.nlm.nih.gov/gene/4326) · UniProt [Q9ULZ9](https://www.uniprot.org/uniprotkb/Q9ULZ9) · Ensembl [ENSG00000198598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198598)

## Data

Gene col 12626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12626); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12626]; `tensor/DDL_lfc|DDL_z.npy` [12626]; `embed/gene_vectors.npy` [12626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12626 or target_col == 12626). Every well: [[MMP17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
