---
symbol: "ABHD17C"
type: "gene"
col: 5858
ensembl_id: "ENSG00000136379"
name: "abhydrolase domain containing 17C, depalmitoylase"
location: "15q25.1"
module: 235
arm: "+"
pooled_cpm: 68.81
n_lines_expressing: 42
n_dd_up: 1
n_dd_down: 40
n_dd_up_clean: 1
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 35
direction_downstream: 31
tags: ["gene", "module/235"]
generated_by: "tahoemap"
---

# ABHD17C

*abhydrolase domain containing 17C, depalmitoylase* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.93× (z +5.2, q 1e-04, up in 18 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.70×, HEC-1-A 2.12×; ⚠ cell-cycle shift, explains ~52% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (C32 14.0×).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.272× (z -27.2, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEMIP]] (+0.72, fdr 7e-06, ⚠ same locus), [[DUSP4]] (+0.65, fdr 7e-06), [[GDPGP1]] (+0.61, fdr 1e-05), [[CEACAM1]] (+0.56, fdr 1e-05); moves opposite to [[SYNE1]] (-0.51, fdr 1e-05), [[TRIM16L-1]] (-0.48, fdr 4e-05), [[DCLK2]] (-0.47, fdr 3e-05).
> It is in [[Module 235]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[CEACAM1]] → it (grade B ⚠); 31 go from it, the strongest it → [[DUSP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 2.70×, HEC-1-A 2.12×; ⚠ cell-cycle shift, explains ~52% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (C32 14.0×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +5.2 | 1e-04 | 18/41 (C32, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.272×** | -27.2 | 0e+00 | 37/39 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.255×** | -19.6 | 0e+00 | 38/40 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.337×** | -16.2 | 0e+00 | 38/39 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.460×** | -11.6 | 1e-28 | 34/40 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.475×** | -11.1 | 2e-26 | 30/40 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.489×** | -10.7 | 1e-24 | 33/40 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.510×** | -10.0 | 1e-21 | 30/40 (BT-474, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.540×** | -9.2 | 4e-18 | 30/40 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.532×** | -8.7 | 3e-16 | 30/34 (SW48, KATO III, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.616×** | -7.2 | 3e-11 | 30/40 (C32, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -7.0 | 1e-10 | 25/39 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.634×** | -6.8 | 6e-10 | 27/40 (LS 180, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.645×** | -6.5 | 3e-09 | 25/40 (LoVo, KATO III, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.633×** | -6.4 | 6e-09 | 25/40 (C32, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.657×** | -6.2 | 2e-08 | 25/38 (COLO 205, A549, …) | all doses, flat | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.718×** | -6.2 | 3e-08 | 30/40 (C32, CHP-212, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.765×** | -5.6 | 9e-07 | 21/40 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.711×** | -5.0 | 1e-05 | 25/41 (C32, A549, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.741×** | -5.0 | 1e-05 | 26/41 (C32, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.753×** | -5.0 | 2e-05 | 23/40 (C32, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 123 | 1 | 24 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.0× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.0620× (z -24.2) |
| [[BT-474 (line)]] | alt | 159 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -20.5) |
| [[LS 180 (line)]] | wt | 235 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -29.3) |
| [[LoVo (line)]] | wt | 346 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -29.3) |
| [[KATO III (line)]] | alt | 216 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -26.2) |
| [[A549 (line)]] | wt | 148 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0477× (z -36.0) |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -21.1) |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.8) |
| [[COLO 205 (line)]] | alt | 160 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -18.4) |
| [[NCI-H1573 (line)]] | alt | 99.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -29.9) |
| [[Panc 03.27 (line)]] | alt | 83.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 96.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -20.3) |
| [[AsPC-1 (line)]] | alt | 132 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -20.2) |
| [[Hs 766T (line)]] | wt | 120 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -19.3) |
| [[SHP-77 (line)]] | alt | 95.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 51.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 69.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.0) |
| [[SW 900 (line)]] | alt | 49.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.0) |
| [[SW480 (line)]] | alt | 40.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 25.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.6) |
| [[RKO (line)]] | wt | 26.0 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.3) ⚠ cell-cycle shift, explains ~52% of this change | [[Harringtonine (drug)]] 5 µM 0.117× (z -13.7) |
| [[A-172 (line)]] | wt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.0) |
| [[HOP62 (line)]] | alt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.0) |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0815× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0997× (z -14.0) |
| [[SW48 (line)]] | wt | 39.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.5) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.5) |
| [[J82 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.1) |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -8.9) |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A-427 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEMIP]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 | ⚠ same locus (23.7 kb, same strand: neighbours can correlate without regulation) |
| [[DUSP4]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[GDPGP1]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CEACAM1]] | +0.56 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[BACE2]] | +0.55 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FRMD8]] | +0.55 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[ANTXR2]] | +0.55 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.54 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SEMA4B]] | +0.54 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ITGB5]] | +0.53 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CLDN10-AS1]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TMEM51]] | +0.52 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNE1]] | -0.51 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TRIM16L-1]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[DCLK2]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NEK1]] | -0.46 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CPLANE1]] | -0.46 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ATG10]] | -0.45 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ANKS1B]] | -0.44 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SHTN1]] | -0.43 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CFL2]] | -0.43 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[POLK]] | -0.43 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[USP40]] | -0.42 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[LARS1]] | -0.42 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 34, C 1. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM1]] | B | CEACAM1 activity raises ABHD17C's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.57× lower at baseline in the lines without CEACAM1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[DUSP4]] | B | DUSP4 activity raises ABHD17C's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 3.71× lower at baseline in the lines without DUSP4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[TFF1]] | B | TFF1 activity raises ABHD17C's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.58× lower at baseline in the lines without TFF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[CEMIP]] | B | CEMIP activity raises ABHD17C's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.96× lower at baseline in the lines without CEMIP | 0.001 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[HS3ST1]] | B | HS3ST1 activity raises ABHD17C's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.04× lower at baseline in the lines without HS3ST1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[CEACAM5]] | B | CEACAM5 activity raises ABHD17C's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.35× lower at baseline in the lines without CEACAM5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[CEACAM6]] | B | CEACAM6 activity raises ABHD17C's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without CEACAM6 | 0.006 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises ABHD17C's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.00× lower at baseline in the lines without TNFRSF21 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[SYTL5]] | B | SYTL5 activity raises ABHD17C's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without SYTL5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ABHD17C's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.06× lower at baseline in the lines without TMPRSS4 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[SDR16C5]] | B | SDR16C5 activity raises ABHD17C's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.14× lower at baseline in the lines without SDR16C5 | 0.009 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[KCNK1]] | B | KCNK1 activity raises ABHD17C's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without KCNK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 30, C 1. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP4]] | B | ABHD17C activity raises DUSP4's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 5.75× lower at baseline in the lines without ABHD17C | 4e-04 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[CEMIP]] | B | ABHD17C activity raises CEMIP's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 5.17× lower at baseline in the lines without ABHD17C | 0.004 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[ST3GAL1]] | B | ABHD17C activity raises ST3GAL1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 3.62× lower at baseline in the lines without ABHD17C | 0.007 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[PLEKHM1P1]] | B | ABHD17C activity raises PLEKHM1P1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without ABHD17C | 0.013 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[NIBAN2]] | B | ABHD17C activity raises NIBAN2's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without ABHD17C | 0.023 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[PTPRE]] | B | ABHD17C activity raises PTPRE's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 3.59× lower at baseline in the lines without ABHD17C | 0.024 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[MAP3K5]] | B | ABHD17C activity raises MAP3K5's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without ABHD17C | 0.029 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[BACE2]] | B | ABHD17C activity raises BACE2's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.64× lower at baseline in the lines without ABHD17C | 0.036 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[WRAP53]] | B | ABHD17C activity lowers WRAP53's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without ABHD17C | 0.041 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[SMOX]] | B | ABHD17C activity raises SMOX's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without ABHD17C | 0.043 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[SYTL5]] | B | ABHD17C activity raises SYTL5's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without ABHD17C | 0.043 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[KCNK1]] | B | ABHD17C activity raises KCNK1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 3.98× lower at baseline in the lines without ABHD17C | 0.049 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 235]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.2, 5.3); signed map (8.8, 49.7). **Vector** length 120, 37.9% of its response variance represented; |z| ≥ 3 in 1,432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +8.7 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.2 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +4.2 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.1 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | -3.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.4 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -19.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.3 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.9 | -5.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 17C, depalmitoylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:80,679,684-80,755,621 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM108C1 |
| Gene groups (HGNC) | Abhydrolase domain containing; Depalmitoylases; Thioester hydrolases |
| Reactome | 4 pathways, smallest: RAS processing; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCB6](https://www.uniprot.org/uniprotkb/Q6PCB6) (Alpha/beta hydrolase domain-containing protein 17C):

> Hydrolyzes fatty acids from S-acylated cysteine residues in proteins. Has depalmitoylating activity towards NRAS and DLG4/PSD95.

**Summary**, from NCBI Gene [58489](https://www.ncbi.nlm.nih.gov/gene/58489):

> Enables palmitoyl-(protein) hydrolase activity. Involved in protein depalmitoylation. Predicted to be located in dendritic spine; postsynaptic density membrane; and recycling endosome membrane. Predicted to be active in endosome membrane and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26925) · Entrez [58489](https://www.ncbi.nlm.nih.gov/gene/58489) · UniProt [Q6PCB6](https://www.uniprot.org/uniprotkb/Q6PCB6) · Ensembl [ENSG00000136379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136379)

## Data

Gene col 5858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5858); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5858]; `tensor/DDL_lfc|DDL_z.npy` [5858]; `embed/gene_vectors.npy` [5858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5858 or target_col == 5858). Every well: [[ABHD17C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD17C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
