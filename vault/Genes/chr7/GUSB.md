---
symbol: "GUSB"
type: "gene"
col: 9875
ensembl_id: "ENSG00000169919"
name: "glucuronidase beta"
location: "7q11.21"
module: 6
arm: "+"
pooled_cpm: 23.87
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GUSB

*glucuronidase beta* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +16.0, q 0e+00, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (PANC-1 3.35×, KATO III 4.42×, SHP-77 3.48×, NCI-H460 3.28×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 8.76×, NCI-H460 3.07×, HOP62 3.43×, MIA PaCa-2 3.45×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 2.75×; ⚠ cell-cycle shift, explains ~33% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.654× (z -7.1, q 8e-10, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGH]] (+0.70, fdr 7e-06), [[SHMT1]] (+0.70, fdr 7e-06), [[CLSTN1]] (+0.69, fdr 7e-06); moves opposite to [[ZNF286B]] (-0.63, fdr 2e-05), [[NSRP1]] (-0.63, fdr 7e-06), [[MRPL45P2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[BCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9875.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (PANC-1 3.35×, KATO III 4.42×, SHP-77 3.48×, NCI-H460 3.28×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1573 8.76×, NCI-H460 3.07×, HOP62 3.43×, MIA PaCa-2 3.45×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 2.75×; ⚠ cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.61×** | +16.0 | 0e+00 | 41/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.62×** | +15.4 | 0e+00 | 32/34 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.01×** | +11.6 | 5e-29 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.95×** | +11.1 | 2e-26 | 45/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.96×** | +10.3 | 6e-23 | 31/39 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.74×** | +9.2 | 5e-18 | 39/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.33×** | +4.6 | 4e-04 | 21/43 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +4.1 | 0.003 | 18/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.6 | 0.017 | 13/48 (SHP-77, SW 900, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.023 | 9/48 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.24×** | +3.5 | 0.023 | 22/46 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.15× | +3.3 | 0.052 | 10/48 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.43×** | +3.1 | 0.084 | 8/48 (HEC-1-A, SHP-77, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.654×** | -7.1 | 8e-10 | 29/47 (NCI-H2030, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.695×** | -6.1 | 3e-07 | 29/48 (SNU-1, SW 900, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.687×** | -5.8 | 1e-06 | 27/48 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.730×** | -5.3 | 2e-05 | 27/48 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.742×** | -4.6 | 5e-04 | 21/46 (NCI-H1792, SNU-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.832×** | -4.3 | 0.001 | 25/47 (NCI-H23, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.774×** | -4.1 | 0.003 | 21/48 (A-427, SW 1088, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.038 | 13/48 (KATO III, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.3 | 0.056 | 17/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.078 | 7/48 (J82, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 23.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.5) |
| [[SW480 (line)]] | alt | 24.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 17.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 19.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 23.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 42.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.76× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.4) |
| [[PANC-1 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 36.0 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.296× (z -8.9) |
| [[A-427 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGH]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SHMT1]] | +0.70 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CLSTN1]] | +0.69 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TMEM245]] | +0.69 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CALM3]] | +0.67 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[CASP2]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[HDAC1]] | +0.67 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SKP2]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HADH]] | +0.66 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[APMAP]] | +0.66 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.66 | +0.56 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF286B]] | -0.63 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.63 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[MRPL45P2]] | -0.62 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CCDC59]] | -0.60 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[NOXRED1]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CCDC122]] | -0.60 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[GATAD1]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ATE1OSP]] | -0.59 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PBDC1]] | -0.59 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[SRP19]] | -0.58 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TRIP11]] | -0.57 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[LRIF1]] | -0.57 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAM]] | B | BCAM activity raises GUSB's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without BCAM | 0.007 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[PODXL2]] | B | PODXL2 activity raises GUSB's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without PODXL2 | 0.020 | ⚠ within organs, on part of the lines |
| [[TCF19]] | B | TCF19 activity raises GUSB's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without TCF19 | 0.064 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[SORT1]] | B | SORT1 activity raises GUSB's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without SORT1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers GUSB's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises GUSB's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises GUSB's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without PBK | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[TK1]] | C | TK1 activity raises GUSB's level | lines that do not express TK1 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises GUSB's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.4, -39.0); signed map (-29.7, -38.1). **Vector** length 83.6, 17.5% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Resolution of AP sites via the multiple-nucleotide patch replacement pathway* (reactome, mean cos +0.51 to 14); *Resolution of Abasic Sites (AP sites)* (reactome, mean cos +0.51 to 15); *Base Excision Repair* (reactome, mean cos +0.51 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.7 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.3 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.1 | +16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.1 | +15.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | glucuronidase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:65,960,684-65,982,215 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, GLYCOLYSIS |
| Reactome | 13 pathways, smallest: Mucopolysaccharidoses; Hyaluronan degradation; Heme degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P08236](https://www.uniprot.org/uniprotkb/P08236) (Beta-glucuronidase):

> Plays an important role in the degradation of dermatan and keratan sulfates.

**Summary**, from NCBI Gene [2990](https://www.ncbi.nlm.nih.gov/gene/2990):

> This gene encodes a hydrolase that degrades glycosaminoglycans, including heparan sulfate, dermatan sulfate, and chondroitin-4,6-sulfate. The enzyme forms a homotetramer that is localized to the lysosome. Mutations in this gene result in mucopolysaccharidosis type VII. Alternative splicing results in multiple transcript variants. There are many pseudogenes of this locus in the human genome.[provided by RefSeq, May 2014]

**Accessions** — [HGNC:4696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4696) · Entrez [2990](https://www.ncbi.nlm.nih.gov/gene/2990) · UniProt [P08236](https://www.uniprot.org/uniprotkb/P08236) · Ensembl [ENSG00000169919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169919)

## Data

Gene col 9875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9875); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9875]; `tensor/DDL_lfc|DDL_z.npy` [9875]; `embed/gene_vectors.npy` [9875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9875 or target_col == 9875). Every well: [[GUSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
