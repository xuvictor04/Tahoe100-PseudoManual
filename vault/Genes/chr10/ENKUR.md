---
symbol: "ENKUR"
type: "gene"
col: 7478
ensembl_id: "ENSG00000151023"
name: "enkurin, TRPC channel interacting protein"
location: "10p12.1"
module: 70
arm: "+"
pooled_cpm: 26.85
n_lines_expressing: 30
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 9
direction_downstream: 20
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# ENKUR

*enkurin, TRPC channel interacting protein* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Amsacrine (drug)]] 5 µM: 1.45× (z +5.7, q 9e-06, up in 19 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.558× (z -5.9, q 2e-06, down in 18 of 26 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.583× (z -5.7, q 2e-06, down in 20 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01285]] (+0.58, fdr 1e-05), [[VNN1]] (+0.58, fdr 2e-05), [[ISG20]] (+0.57, fdr 2e-05); moves opposite to [[PYGB]] (-0.48, fdr 6e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC01605]] → it (grade B ⚠); 20 go from it, the strongest it → [[MAST4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Amsacrine (drug)]] 5 µM |  | **1.45×** | +5.7 | 9e-06 | 19/28 (RKO, HOP62, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.63×** | +5.4 | 2e-05 | 18/26 (HEC-1-A, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.3 | 2e-05 | 9/28 (A498, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +5.1 | 6e-05 | 16/28 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +4.6 | 4e-04 | 17/26 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.6 | 4e-04 | 18/27 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +4.4 | 0.001 | 14/28 (A549, RKO, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.005 | 11/28 (LoVo, A549, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.016 | 11/27 (A549, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +3.6 | 0.016 | 10/28 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.5 | 0.027 | 10/26 (H4, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.027 | 9/28 (RKO, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.031 | 12/29 (A549, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.034 | 11/26 (A549, LoVo, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +3.2 | 0.060 | 11/27 (H4, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.558×** | -5.9 | 2e-06 | 18/26 (LOX-IMVI, COLO 205, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.576×** | -5.8 | 2e-06 | 23/27 (COLO 205, HepG2/C3A, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.583×** | -5.7 | 2e-06 | 20/27 (LOX-IMVI, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.586×** | -5.6 | 2e-06 | 15/27 (HOP62, H4, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.606×** | -5.3 | 1e-05 | 16/27 (H4, COLO 205, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.657×** | -4.4 | 9e-04 | 18/27 (LOX-IMVI, COLO 205, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.456×** | -4.3 | 0.001 | 16/25 (HepG2/C3A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.664×** | -4.3 | 0.001 | 11/29 (LoVo, COLO 205, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.671×** | -4.2 | 0.002 | 14/27 (H4, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.679×** | -4.1 | 0.003 | 16/26 (H4, LOX-IMVI, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.519×** | -3.6 | 0.015 | 14/26 (Hs 766T, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.786×** | -3.6 | 0.017 | 17/29 (COLO 205, HepG2/C3A, …) | two highest doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.716×** | -3.5 | 0.019 | 14/27 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.718×** | -3.5 | 0.020 | 10/27 (HOP62, Hs 766T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.792×** | -3.4 | 0.022 | 19/27 (LOX-IMVI, COLO 205, …) | rises with dose | composition shift |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.744×** | -3.1 | 0.064 | 9/27 (HOP62, H4, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.746×** | -3.1 | 0.067 | 14/27 (HOP62, H4, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.077 | 15/29 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.714×** | -2.9 | 0.091 | 8/26 (H4, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.758×** | -2.9 | 0.091 | 12/27 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.592×** | -2.9 | 0.091 | 12/25 (Hs 766T, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 521 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0291× (z -37.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0455× (z -23.3) |
| [[COLO 205 (line)]] | alt | 44.4 | 0 | 12 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0209× (z -19.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0341× (z -16.8) |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 10 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0716× (z -17.2) ⚠ toxic; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.114× (z -14.7) |
| [[H4 (line)]] | wt | 50.7 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0256× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.116× (z -8.5) |
| [[HOP62 (line)]] | alt | 34.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -11.1) |
| [[A549 (line)]] | wt | 18.0 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -9.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1573 (line)]] | alt | 50.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.82× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 20.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -12.4) |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SHP-77 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0950× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01285]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[VNN1]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ISG20]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MAST4]] | +0.55 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[PTPN22]] | +0.54 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[CTSS]] | +0.54 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[SNCAIP]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[GBP3]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[PDZK1IP1]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[STEAP4]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[NKX3-1]] | +0.51 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[CASP4]] | +0.51 | +0.40 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGB]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01605]] | B | LINC01605 activity raises ENKUR's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 2.32× lower at baseline in the lines without LINC01605 | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR |
| [[CA3]] | B | CA3 activity raises ENKUR's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.78× lower at baseline in the lines without CA3 | 0.044 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[MAST4]] | B | MAST4 activity raises ENKUR's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.49× lower at baseline in the lines without MAST4 | 0.050 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers ENKUR's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | B | MAP2K1 activity lowers ENKUR's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers ENKUR's level | compounds that target TOP2A: 3 of 5 raise it (Amsacrine, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MX2]] | B | MX2 activity raises ENKUR's level | lines that do not express MX2 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without MX2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[VNN1]] | C | VNN1 activity raises ENKUR's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.95× lower at baseline in the lines without VNN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises ENKUR's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.04× lower at baseline in the lines without STEAP4 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 19, C 1. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAST4]] | B | ENKUR activity raises MAST4's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without ENKUR | 0.001 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[CA3]] | B | ENKUR activity raises CA3's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without ENKUR | 0.007 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[MX2]] | B | ENKUR activity raises MX2's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without ENKUR | 0.014 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[HSD11B1-AS1]] | B | ENKUR activity raises HSD11B1-AS1's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without ENKUR | 0.018 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[RASGRP3]] | B | ENKUR activity raises RASGRP3's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without ENKUR | 0.018 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[STING1]] | B | ENKUR activity raises STING1's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without ENKUR | 0.026 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[KIAA1217]] | B | ENKUR activity raises KIAA1217's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 1.86× lower at baseline in the lines without ENKUR | 0.026 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[CFB]] | B | ENKUR activity raises CFB's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 1.87× lower at baseline in the lines without ENKUR | 0.038 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[MOB3B]] | B | ENKUR activity raises MOB3B's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without ENKUR | 0.039 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[SNCAIP]] | B | ENKUR activity raises SNCAIP's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without ENKUR | 0.045 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[CASP4]] | B | ENKUR activity raises CASP4's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without ENKUR | 0.047 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[TMC5]] | B | ENKUR activity raises TMC5's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without ENKUR | 0.054 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.3, 49.4); signed map (60.6, 25.8). **Vector** length 96.1, 26.5% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.6 | +1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.1 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.8 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.5 | +5.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -5.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.4 | -4.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | enkurin, TRPC channel interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:24,981,979-25,062,279 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26778, enkurin, CFAP106; previously C10orf63 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC29](https://www.uniprot.org/uniprotkb/Q8TC29) (Enkurin):

> Adapter that functions to localize a calcium-sensitive signal transduction machinery in sperm to a calcium-permeable ion channel (By similarity). Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating.

**Summary**, from NCBI Gene [219670](https://www.ncbi.nlm.nih.gov/gene/219670):

> This gene encodes a protein that interacts with calmodulin and several transient receptor potential canonical cation channel proteins. The encoded protein may function as an adaptor to localize signal transduction machinery to calcium channels. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:28388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28388) · Entrez [219670](https://www.ncbi.nlm.nih.gov/gene/219670) · UniProt [Q8TC29](https://www.uniprot.org/uniprotkb/Q8TC29) · Ensembl [ENSG00000151023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151023)

## Data

Gene col 7478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7478); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7478]; `tensor/DDL_lfc|DDL_z.npy` [7478]; `embed/gene_vectors.npy` [7478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7478 or target_col == 7478). Every well: [[ENKUR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENKUR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
