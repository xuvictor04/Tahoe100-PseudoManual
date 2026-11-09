---
symbol: "PDLIM2"
type: "gene"
col: 4236
ensembl_id: "ENSG00000120913"
name: "PDZ and LIM domain 2"
location: "8p21.3"
module: 12
arm: "+"
pooled_cpm: 16.06
n_lines_expressing: 46
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PDLIM2

*PDZ and LIM domain 2* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +5.3, q 7e-05, up in 21 of 42 measured lines) ⚠ cell-cycle shift, would explain all of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (AsPC-1 4.78×, KATO III 4.96×, CFPAC-1 3.85×, LoVo 3.89×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 5.62×, SW480 4.09×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.299× (z -12.9, q 2e-35, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1H]] (+0.62, fdr 7e-06), [[OVOL1]] (+0.59, fdr 1e-05), [[MED19]] (+0.57, fdr 2e-05); moves opposite to [[ZNF731P]] (-0.54, fdr 3e-05), [[CHCHD3]] (-0.52, fdr 2e-05), [[M6PR]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TNFRSF10C]] → it (grade B ⚠); 2 go from it, the strongest it → [[ILK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4236.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (AsPC-1 4.78×, KATO III 4.96×, CFPAC-1 3.85×, LoVo 3.89×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 5.62×, SW480 4.09×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +5.3 | 7e-05 | 21/42 (AsPC-1, KATO III, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.50×** | +4.3 | 0.004 | 17/38 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Erythromycin (drug)]] 5 µM |  | 1.34× | +3.2 | 0.29 | 11/43 (NCI-H2347, A-427, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 1.34× | +3.0 | 0.31 | 20/42 (AsPC-1, KATO III, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.299×** | -12.9 | 2e-35 | 42/44 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.311×** | -12.5 | 3e-33 | 41/44 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.396×** | -9.9 | 8e-21 | 36/44 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.655×** | -6.4 | 3e-08 | 23/40 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.705×** | -5.3 | 2e-05 | 23/44 (J82, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.618×** | -5.1 | 3e-05 | 24/44 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.651×** | -4.6 | 4e-04 | 20/42 (HS-578T, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.642×** | -4.5 | 4e-04 | 20/42 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -4.5 | 5e-04 | 21/43 (H4, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.674×** | -4.2 | 0.001 | 20/44 (NCI-H460, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.678×** | -4.1 | 0.002 | 19/44 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -4.1 | 0.002 | 14/43 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.670×** | -4.0 | 0.002 | 21/41 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.702×** | -3.8 | 0.007 | 20/43 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.511×** | -3.7 | 0.007 | 18/43 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.512×** | -3.7 | 0.007 | 16/42 (RPMI-7951, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -3.6 | 0.009 | 14/42 (AsPC-1, SW 1088, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -3.6 | 0.010 | 20/44 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -3.3 | 0.029 | 17/43 (LS 180, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 22.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -13.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -9.8) |
| [[SW480 (line)]] | alt | 15.0 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.236× (z -9.7) |
| [[A-172 (line)]] | wt | 40.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 20.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -11.1) |
| [[H4 (line)]] | wt | 14.2 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0300× (z -13.4) |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -11.4) |
| [[HS-578T (line)]] | alt | 49.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -12.1) |
| [[KATO III (line)]] | alt | 15.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 14.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.172× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 6.61 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -9.4) |
| [[RKO (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0549× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 6.60 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0963× (z -8.8) |
| [[SW48 (line)]] | wt | 23.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1H]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[OVOL1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MED19]] | +0.57 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ACTR1B]] | +0.55 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[TMEM265]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZNF555]] | +0.54 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[GLIS2]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CBR3]] | +0.53 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[C2orf74]] | +0.53 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[BIK]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[LTB]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SNHG11]] | +0.52 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.54 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[CHCHD3]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[M6PR]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PROM2]] | -0.49 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[TMX3]] | -0.49 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[APP]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[USB1]] | -0.48 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[TRRAP]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[NAA50]] | -0.47 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[FAM91A1]] | -0.47 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[UBAC2]] | -0.46 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[LRPPRC]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF10C]] | B | TNFRSF10C activity raises PDLIM2's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.87× lower at baseline in the lines without TNFRSF10C | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[OVOL1]] | B | OVOL1 activity weakens PDLIM2's drug response | lines that do not express OVOL1 (30) vs lines expressing it (14) | the lines without OVOL1 respond 1.16× as strongly (z diff -0.52); strongest at Digitoxin 0.5 µM: 0.54x vs 1.13x (z diff -3.2) | 0.092 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ILK]] | C | PDLIM2 activity raises ILK's level | lines that do not express PDLIM2 (4) vs lines expressing it (46) | 1.58× lower at baseline in the lines without PDLIM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FSTL3, BIRC3, BOK; maybe low, not absent; its own permutation p |
| [[DYNLL1]] | C | PDLIM2 activity raises DYNLL1's level | lines that do not express PDLIM2 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without PDLIM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FSTL3, BIRC3, BOK; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (28.8, -34.7); signed map (-0.6, 12.3). **Vector** length 86.3, 19.5% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.8 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +6.5 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | +0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | PDZ and LIM domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,578,279-22,598,025 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JY6](https://www.uniprot.org/uniprotkb/Q96JY6) (PDZ and LIM domain protein 2):

> Probable adapter protein located at the actin cytoskeleton that promotes cell attachment. Necessary for the migratory capacity of epithelial cells. Overexpression enhances cell adhesion to collagen and fibronectin and suppresses anchorage independent growth. May contribute to tumor cell migratory capacity.

**Summary**, from NCBI Gene [64236](https://www.ncbi.nlm.nih.gov/gene/64236):

> This gene encodes a member of the ALP subfamily of PDZ-LIM domain proteins. The encoded protein suppresses anchorage-dependent growth and promotes cell migration and adhesion through interactions with the actin cytoskeleton via the PDZ domain. The encoded protein is also a putative tumor suppressor protein, and decreased expression of this gene is associated with several malignancies including breast cancer and adult T-cell leukemia. Alternatively spliced transcript variants encoding multiple …

**Accessions** — [HGNC:13992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13992) · Entrez [64236](https://www.ncbi.nlm.nih.gov/gene/64236) · UniProt [Q96JY6](https://www.uniprot.org/uniprotkb/Q96JY6) · Ensembl [ENSG00000120913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120913)

## Data

Gene col 4236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4236); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4236]; `tensor/DDL_lfc|DDL_z.npy` [4236]; `embed/gene_vectors.npy` [4236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4236 or target_col == 4236). Every well: [[PDLIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDLIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
