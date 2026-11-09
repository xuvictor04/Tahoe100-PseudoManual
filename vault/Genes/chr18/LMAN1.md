---
symbol: "LMAN1"
type: "gene"
col: 1088
ensembl_id: "ENSG00000074695"
name: "lectin, mannose binding 1"
location: "18q21.32"
module: 42
arm: "+"
pooled_cpm: 270.02
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# LMAN1

*lectin, mannose binding 1* — 18q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.49× (z +6.7, q 2e-08, up in 33 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 2.55×, PANC-1 2.16×, SHP-77 2.27×, NCI-H2030 2.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 2.04×, NCI-H2030 2.03×, SW480 1.85×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 2.16×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.443× (z -20.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90B1]] (+0.83, fdr 7e-06), [[P4HB]] (+0.79, fdr 7e-06), [[PDIA4]] (+0.79, fdr 7e-06); moves opposite to [[TET3]] (-0.63, fdr 1e-05), [[SLC25A13]] (-0.61, fdr 1e-05), [[ITPA]] (-0.61, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FKBP10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1088.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 2.55×, PANC-1 2.16×, SHP-77 2.27×, NCI-H2030 2.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 2.04×, NCI-H2030 2.03×, SW480 1.85×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 2.16×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.7 | 2e-08 | 33/49 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.4 | 0.003 | 27/44 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.21× | +3.5 | 0.10 | 24/48 (SHP-77, HT-29, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.19 | 23/48 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.20 | 19/48 (NCI-H2347, LS 180, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.19× | +3.0 | 0.20 | 22/48 (SW480, SW48, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.443×** | -20.7 | 0e+00 | 47/48 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.482×** | -13.1 | 1e-36 | 41/48 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.564×** | -9.9 | 1e-20 | 43/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.606×** | -9.0 | 4e-17 | 41/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -7.0 | 4e-10 | 30/49 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.685×** | -6.4 | 2e-08 | 41/47 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -6.3 | 2e-08 | 31/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.705×** | -6.3 | 2e-08 | 33/48 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -5.7 | 6e-07 | 32/47 (HCT15, H4, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.712×** | -5.7 | 8e-07 | 38/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.819×** | -5.1 | 2e-05 | 25/48 (J82, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.769×** | -4.7 | 1e-04 | 31/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -4.7 | 1e-04 | 31/48 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.779×** | -4.5 | 3e-04 | 33/48 (HOP62, A549, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.778×** | -4.3 | 6e-04 | 27/47 (H4, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.798×** | -3.9 | 0.003 | 31/49 (SW 1088, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.8 | 0.005 | 29/47 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 284 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -20.7) |
| [[H4 (line)]] | wt | 675 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -25.0) |
| [[HS-578T (line)]] | alt | 559 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -24.5) |
| [[NCI-H1792 (line)]] | alt | 636 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -23.2) |
| [[RPMI-7951 (line)]] | alt | 358 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -25.3) |
| [[CFPAC-1 (line)]] | alt | 279 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -24.1) |
| [[HCT15 (line)]] | alt | 460 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -18.6) |
| [[HOP62 (line)]] | alt | 310 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -23.0) |
| [[hTERT-HPNE (line)]] | wt | 539 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -22.9) |
| [[NCI-H2347 (line)]] | alt | 370 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 98.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -19.5) |
| [[C32 (line)]] | wt | 227 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -15.4) |
| [[J82 (line)]] | alt | 377 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -20.6) |
| [[KATO III (line)]] | alt | 277 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -27.4) |
| [[LS 180 (line)]] | wt | 208 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 241 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 173 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -13.1) |
| [[A498 (line)]] | wt | 354 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 312 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 286 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -16.2) |
| [[SHP-77 (line)]] | alt | 229 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.16× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 200 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.9) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.431× (z -9.5) |
| [[SNU-423 (line)]] | alt | 232 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -18.4) |
| [[SW 900 (line)]] | alt | 199 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -20.1) |
| [[SW480 (line)]] | alt | 135 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.85× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -13.0) |
| [[A549 (line)]] | wt | 239 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.4) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.2) |
| [[BT-474 (line)]] | alt | 283 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.374× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 248 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 312 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -20.1) |
| [[PANC-1 (line)]] | alt | 168 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 220 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +12.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 175 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.3) |
| [[Hs 766T (line)]] | wt | 318 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.2) |
| [[HT-29 (line)]] | alt | 148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 353 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 188 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.2) |
| [[RKO (line)]] | wt | 225 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -12.1) |
| [[SW 1088 (line)]] | alt | 553 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.8) |
| [[SW 1271 (line)]] | alt | 241 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.1) |
| [[SW1417 (line)]] | alt | 160 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -12.0) |
| [[C-33 A (line)]] | alt | 233 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 254 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 318 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90B1]] | +0.83 | +0.85 / +0.76 | both halves | 7e-06 | STRING 581 |
| [[P4HB]] | +0.79 | +0.82 / +0.74 | both halves | 7e-06 | STRING 520 |
| [[PDIA4]] | +0.79 | +0.80 / +0.71 | both halves | 7e-06 | STRING 556 |
| [[SEC24D]] | +0.78 | +0.81 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 785 |
| [[COPA]] | +0.76 | +0.79 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 402 |
| [[HSPA5]] | +0.75 | +0.76 / +0.68 | both halves | 7e-06 | STRING 588 |
| [[COG6]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPB1]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 920 |
| [[SLC31A1]] | +0.74 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[SUCO]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[P3H1]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[TTC3]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TET3]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[ITPA]] | -0.61 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[MARK2]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[RNF115]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[DDX28]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP10]] | B | FKBP10 activity raises LMAN1's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without FKBP10 | 0.022 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[SNHG18]] | B | SNHG18 activity strengthens LMAN1's drug response | lines that do not express SNHG18 (29) vs lines expressing it (20) | the lines without SNHG18 respond 0.71× as strongly (z diff +1.89); strongest at Homoharringtonine 0.5 µM: 0.64x vs 0.39x (z diff +3.9) | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930; target measured in part of the lines; artifact flags |
| [[SLC6A6]] | C | SLC6A6 activity raises LMAN1's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without SLC6A6 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, -31.1); signed map (-53.7, 7.9). **Vector** length 144, 55.4% of its response variance represented; |z| ≥ 3 in 1,286 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.69 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.63 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.63 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -2.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +2.9 | +3.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.8 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.0 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.5 | -9.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.6 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.5 | -5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.8 | -6.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.5 | -4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | lectin, mannose binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.32 — chr18:59,327,823-59,359,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MR60, ERGIC-53, ERGIC53, gp58, MCFD1, FMFD1; previously F5F8D |
| Hallmark sets | PROTEIN_SECRETION, ANDROGEN_RESPONSE |
| Reactome | 16 pathways, smallest: Cargo concentration in the ER; RHOD GTPase cycle; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P49257](https://www.uniprot.org/uniprotkb/P49257) (Protein ERGIC-53):

> Mannose-specific lectin. May recognize sugar residues of glycoproteins, glycolipids, or glycosylphosphatidyl inositol anchors and may be involved in the sorting or recycling of proteins, lipids, or both. The LMAN1-MCFD2 complex forms a specific cargo receptor for the ER-to-Golgi transport of selected proteins.

**Summary**, from NCBI Gene [3998](https://www.ncbi.nlm.nih.gov/gene/3998):

> The protein encoded by this gene is a membrane mannose-specific lectin that cycles between the endoplasmic reticulum, endoplasmic reticulum-Golgi intermediate compartment, and cis-Golgi, functioning as a cargo receptor for glycoprotein transport. The protein has an N-terminal signal sequence, a calcium-dependent and pH-sensitive carbohydrate recognition domain, a stalk region that functions in oligomerization, a transmembrane domain, and a short cytoplasmic domain required for organelle …

**Accessions** — [HGNC:6631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6631) · Entrez [3998](https://www.ncbi.nlm.nih.gov/gene/3998) · UniProt [P49257](https://www.uniprot.org/uniprotkb/P49257) · Ensembl [ENSG00000074695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074695)

## Data

Gene col 1088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1088); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1088]; `tensor/DDL_lfc|DDL_z.npy` [1088]; `embed/gene_vectors.npy` [1088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1088 or target_col == 1088). Every well: [[LMAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
