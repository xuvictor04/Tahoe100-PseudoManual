---
symbol: "SPTBN2"
type: "gene"
col: 10440
ensembl_id: "ENSG00000173898"
name: "spectrin beta, non-erythrocytic 2"
location: "11q13.2"
module: 4
arm: "+"
pooled_cpm: 16.65
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SPTBN2

*spectrin beta, non-erythrocytic 2* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.01× (z +17.8, q 0e+00, up in 21 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.32× (z +4.7, q 4e-04, up in 18 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 6.56×, NCI-H1792 8.64×, SW480 2.46×, KATO III 3.63×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 3.38×, NCI-H1792 5.22×, LoVo 3.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1792 4.08×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.589× (z -12.5, q 2e-33, down in 28 of 38 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.668× (z -6.8, q 3e-09, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KAT2A]] (+0.70, fdr 7e-06), [[CRACR2A]] (+0.66, fdr 1e-05), [[NUP210]] (+0.66, fdr 7e-06); moves opposite to [[ARID4A]] (-0.64, fdr 1e-05), [[LGALS1]] (-0.64, fdr 1e-05), [[SELENOK]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC12A8]] → it (grade B ⚠); 7 go from it, the strongest it → [[DZIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 6.56×, NCI-H1792 8.64×, SW480 2.46×, KATO III 3.63×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 3.38×, NCI-H1792 5.22×, LoVo 3.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1792 4.08×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +17.8 | 0e+00 | 21/23 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +17.6 | 0e+00 | 28/32 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +13.4 | 6e-39 | 20/28 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.7 | 4e-04 | 18/39 (HOP62, NCI-H2347, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.4 | 0.001 | 14/39 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.9 | 0.008 | 10/36 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +3.6 | 0.030 | 6/39 (HOP62, A-427, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.035 | 10/38 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 7/39 (NCI-H460, SW48, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.589×** | -12.5 | 2e-33 | 28/38 (LOX-IMVI, SW48, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -8.3 | 3e-14 | 21/38 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.668×** | -6.8 | 3e-09 | 21/39 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.680×** | -6.2 | 8e-08 | 21/38 (LOX-IMVI, RKO, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.741×** | -5.0 | 6e-05 | 18/39 (LOX-IMVI, RKO, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.752×** | -4.8 | 2e-04 | 17/37 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.754×** | -4.7 | 2e-04 | 16/39 (LOX-IMVI, BT-474, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.757×** | -4.7 | 2e-04 | 16/39 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.767×** | -4.4 | 6e-04 | 17/39 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.773×** | -4.2 | 0.001 | 11/39 (A-427, LOX-IMVI, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.619×** | -4.2 | 0.001 | 13/38 (RKO, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.841× | -4.1 | 0.002 | 9/39 (BT-474, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.785×** | -4.0 | 0.002 | 21/39 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.697×** | -3.2 | 0.066 | 11/37 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.700×** | -3.1 | 0.068 | 11/38 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 56.6 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0877× (z -27.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.185× (z -13.4) |
| [[RKO (line)]] | wt | 54.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0993× (z -18.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -11.6) |
| [[SW48 (line)]] | wt | 40.8 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.219× (z -9.2) |
| [[SW480 (line)]] | alt | 34.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +11.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.251× (z -14.2) |
| [[LoVo (line)]] | wt | 24.4 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.56× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.320× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 24.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.64× (z +13.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.284× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 8.34 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0699× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.0998× (z -9.4) |
| [[SHP-77 (line)]] | alt | 55.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.287× (z -10.9) |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT2A]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CRACR2A]] | +0.66 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[NUP210]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[WDR77]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[EFTUD2]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ATIC]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[IPO5]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[PFAS]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RPSA]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4A]] | -0.64 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[LGALS1]] | -0.64 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[MED19]] | -0.63 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TMEM258]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[ZMYM5]] | -0.61 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[RNF181]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[SEC22A]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[WIPF2]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.60 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.59 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CDK2AP2]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A8]] | B | SLC12A8 activity raises SPTBN2's level | lines that do not express SLC12A8 (17) vs lines expressing it (33) | 2.09× lower at baseline in the lines without SLC12A8 | 0.031 | ⚠ within organs, on part of the lines; also absent: ANK3, LYPD6B, SAMD12-AS1; maybe low, not absent |
| [[EVPL]] | B | EVPL activity raises SPTBN2's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without EVPL | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[HOXA5]] | B | HOXA5 activity lowers SPTBN2's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.61× higher at baseline in the lines without HOXA5 | 0.086 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[DMKN]] | B | DMKN activity raises SPTBN2's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without DMKN | 0.097 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DZIP1]] | B | SPTBN2 activity lowers DZIP1's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.14× higher at baseline in the lines without SPTBN2 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[BOP1]] | B | SPTBN2 activity raises BOP1's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without SPTBN2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[LRP5]] | B | SPTBN2 activity raises LRP5's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.83× lower at baseline in the lines without SPTBN2 | 0.061 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| cells under [[Paclitaxel (drug)]] 5 µM | B | SPTBN2 activity lowers the cells' numbers under Paclitaxel 5 µM (makes them more sensitive) | lines that do not express SPTBN2 (9) vs lines expressing it (39) | the lines without SPTBN2: 1.31× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[EVPL]] | B | SPTBN2 activity raises EVPL's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.97× lower at baseline in the lines without SPTBN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[PGAM5]] | B | SPTBN2 activity raises PGAM5's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without SPTBN2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[KBTBD11]] | C | SPTBN2 activity raises KBTBD11's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without SPTBN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.3, -33.4); signed map (-7.3, -44.4). **Vector** length 83.4, 17.7% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +17.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | spectrin beta, non-erythrocytic 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,682,496-66,744,670 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SCA5 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Spectrins |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 19 pathways, smallest: Interaction between L1 and Ankyrins; NCAM signaling for neurite out-growth; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O15020](https://www.uniprot.org/uniprotkb/O15020) (Spectrin beta chain, non-erythrocytic 2):

> Probably plays an important role in neuronal membrane skeleton.

**Summary**, from NCBI Gene [6712](https://www.ncbi.nlm.nih.gov/gene/6712):

> Spectrins are principle components of a cell's membrane-cytoskeleton and are composed of two alpha and two beta spectrin subunits. The protein encoded by this gene (SPTBN2), is called spectrin beta non-erythrocytic 2 or beta-III spectrin. It is related to, but distinct from, the beta-II spectrin gene which is also known as spectrin beta non-erythrocytic 1 (SPTBN1). SPTBN2 regulates the glutamate signaling pathway by stabilizing the glutamate transporter EAAT4 at the surface of the plasma …

**Accessions** — [HGNC:11276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11276) · Entrez [6712](https://www.ncbi.nlm.nih.gov/gene/6712) · UniProt [O15020](https://www.uniprot.org/uniprotkb/O15020) · Ensembl [ENSG00000173898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173898)

## Data

Gene col 10440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10440); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10440]; `tensor/DDL_lfc|DDL_z.npy` [10440]; `embed/gene_vectors.npy` [10440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10440 or target_col == 10440). Every well: [[SPTBN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTBN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
