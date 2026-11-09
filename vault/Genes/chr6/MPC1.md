---
symbol: "MPC1"
type: "gene"
col: 695
ensembl_id: "ENSG00000060762"
name: "mitochondrial pyruvate carrier 1"
location: "6q27"
module: 49
arm: "+"
pooled_cpm: 20.43
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# MPC1

*mitochondrial pyruvate carrier 1* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.48× (z +24.6, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.613× (z -9.3, q 6e-18, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL1]] (+0.63, fdr 1e-05), [[OSBP]] (+0.62, fdr 1e-05), [[GOLPH3]] (+0.60, fdr 1e-05); moves opposite to [[ANO7]] (-0.55, fdr 2e-05), [[ZNF300]] (-0.50, fdr 2e-04), [[PUM1]] (-0.49, fdr 7e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CADPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +24.6 | 0e+00 | 40/47 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +17.5 | 0e+00 | 41/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +16.4 | 0e+00 | 38/44 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +15.8 | 0e+00 | 34/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +15.5 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +15.5 | 0e+00 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +11.7 | 2e-29 | 37/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +9.8 | 6e-21 | 35/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.3 | 1e-18 | 23/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.44×** | +7.0 | 1e-10 | 17/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.41×** | +6.3 | 2e-08 | 16/33 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +5.9 | 1e-07 | 18/48 (RKO, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +5.8 | 4e-07 | 20/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.59×** | +4.7 | 1e-04 | 12/45 (PANC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.014 | 7/46 (BT-474, COLO 205, …) | top dose only |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 1.12× | +3.1 | 0.061 | 6/47 (SHP-77, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -9.3 | 6e-18 | 31/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.697×** | -6.9 | 2e-09 | 21/47 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.548×** | -6.0 | 3e-07 | 20/36 (Hs 766T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -5.9 | 6e-07 | 22/47 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -5.6 | 3e-06 | 21/45 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.613×** | -4.9 | 9e-05 | 22/46 (SK-MEL-2, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.767×** | -4.7 | 2e-04 | 18/46 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.797×** | -4.3 | 0.001 | 16/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.659×** | -4.2 | 0.002 | 16/48 (RKO, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.820×** | -3.8 | 0.009 | 9/48 (J82, SW 1088, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.7 | 0.011 | 16/48 (NCI-H1573, HS-578T, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.815×** | -3.7 | 0.011 | 13/47 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.022 | 6/47 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 0.843× | -3.3 | 0.045 | 4/47 (SW48, C-33 A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.2 | 0.054 | 18/48 (PANC-1, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.895× | -3.0 | 0.098 | 13/47 (KATO III, A498, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.851× | -3.0 | 0.098 | 8/46 (SNU-423, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.20× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 37.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.260× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 9.88 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 24.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 9.78 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.8) | — |
| [[SW480 (line)]] | alt | 28.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +22.9) | — |
| [[A498 (line)]] | wt | 34.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.251× (z -12.2) |
| [[HCT15 (line)]] | alt | 29.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0883× (z -9.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 28.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 16.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.41× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 33.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +16.2) | — |
| [[A-427 (line)]] | wt | 8.80 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +8.6) | — |
| [[A549 (line)]] | wt | 5.95 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0769× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 9.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.7) | — |
| [[KATO III (line)]] | alt | 59.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 8.59 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.239× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +17.4) | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.0) | — |
| [[RKO (line)]] | wt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL1]] | +0.63 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[OSBP]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GOLPH3]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PDXDC2P-NPIPB14P]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PDXDC1]] | +0.59 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[FAM177A1]] | +0.57 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[GOLGA2]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[UBE2J1]] | +0.57 | +0.44 / +0.42 | both halves | 4e-05 | **novel candidate** |
| [[BBOF1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SEC23B]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[GCAT]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SELENOS]] | +0.54 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO7]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZNF300]] | -0.50 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PUM1]] | -0.49 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[PTK2]] | -0.47 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[JRK]] | -0.47 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[LINC00958]] | -0.47 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[LARS2]] | -0.44 | -0.46 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADPS2]] | B | CADPS2 activity raises MPC1's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without CADPS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -39.3); signed map (-52.8, 15.4). **Vector** length 91.8, 20.1% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +15.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +24.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +9.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +11.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +5.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | +1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial pyruvate carrier 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:166,364,919-166,383,013 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ68L15.3, CGI-129, SLC54A1; previously BRP44L |
| Gene groups (HGNC) | Solute carrier family 54, mitochondrial pyruvate carriers |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5U8](https://www.uniprot.org/uniprotkb/Q9Y5U8) (Mitochondrial pyruvate carrier 1):

> Mediates the uptake of pyruvate into mitochondria to maintain the balance between glycolysis and oxidative phosphorylation. Plays an essential role in cellular metabolism.

**Summary**, from NCBI Gene [51660](https://www.ncbi.nlm.nih.gov/gene/51660):

> The protein encoded by this gene is part of an MPC1/MPC2 heterodimer that is responsible for transporting pyruvate into mitochondria. The encoded protein is found in the inner mitochondrial membrane. Defects in this gene are a cause of mitochondrial pyruvate carrier deficiency. Several transcript variants, some protein coding and one non-protein coding, have been found for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:21606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21606) · Entrez [51660](https://www.ncbi.nlm.nih.gov/gene/51660) · UniProt [Q9Y5U8](https://www.uniprot.org/uniprotkb/Q9Y5U8) · Ensembl [ENSG00000060762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060762)

## Data

Gene col 695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 695); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 695]; `tensor/DDL_lfc|DDL_z.npy` [695]; `embed/gene_vectors.npy` [695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 695 or target_col == 695). Every well: [[MPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
