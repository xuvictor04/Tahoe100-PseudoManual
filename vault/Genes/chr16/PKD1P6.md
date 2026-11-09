---
symbol: "PKD1P6"
type: "gene"
col: 14675
ensembl_id: "ENSG00000250251"
name: "polycystin 1, transient receptor potential channel interacting pseudogene 6"
location: "16p13.11"
module: 3
arm: "+"
pooled_cpm: 8.55
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PKD1P6

*polycystin 1, transient receptor potential channel interacting pseudogene 6* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.56× (z +7.0, q 2e-09, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.808× (z -11.8, q 4e-29, down in 33 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.494× (z -10.6, q 9e-24, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKD1]] (+0.87, fdr 7e-06), [[STK32C]] (+0.67, fdr 1e-05), [[GIT1]] (+0.65, fdr 1e-05); moves opposite to [[ITGB8]] (-0.62, fdr 1e-05), [[ANAPC13]] (-0.59, fdr 2e-05), [[DECR1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest KIT → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +7.0 | 2e-09 | 22/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 2e-05 | 18/44 (NCI-H1792, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.1 | 7e-05 | 18/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.7 | 3e-04 | 11/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 5e-04 | 16/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.006 | 12/48 (NCI-H2030, Hs 766T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.012 | 8/48 (HepG2/C3A, SW48, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.065 | 6/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.10 | 10/44 (H4, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.22× | +3.1 | 0.12 | 6/45 (NCI-H460, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.808×** | -11.8 | 4e-29 | 33/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -10.6 | 9e-24 | 31/46 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -7.8 | 1e-12 | 27/47 (HOP62, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.621×** | -7.5 | 1e-11 | 21/34 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -7.4 | 1e-11 | 24/47 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.608×** | -7.2 | 6e-11 | 14/23 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.755×** | -4.4 | 9e-04 | 14/48 (H4, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.819×** | -4.2 | 0.002 | 17/45 (MIA PaCa-2, A-172, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.755×** | -4.2 | 0.002 | 8/14 (A498, J82, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.601×** | -4.2 | 0.002 | 12/43 (LS 180, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.003 | 16/48 (H4, KATO III, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.060 | 9/46 (SNU-423, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.079 | 6/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.818× | -3.0 | 0.10 | 10/38 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.4) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.101× (z -10.9) |
| [[A498 (line)]] | wt | 13.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 6.57 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0988× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.106× (z -11.1) |
| [[A-172 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.7) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A549 (line)]] | wt | 7.28 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0719× (z -11.9) |
| [[BT-474 (line)]] | alt | 7.39 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0789× (z -8.9) |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0968× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 8.17 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0981× (z -8.9) |
| [[HOP62 (line)]] | alt | 7.89 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0258× (z -11.5) |
| [[J82 (line)]] | alt | 8.60 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 4.65 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0933× (z -9.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H2030 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -9.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 7.05 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.14 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD1]] | +0.87 | +0.83 / +0.84 | both halves | 7e-06 |  |
| [[STK32C]] | +0.67 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[GIT1]] | +0.65 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SS18L1]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PTDSS2]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CORO7]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[XYLT2]] | +0.62 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[CDC34]] | +0.62 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MIGA2]] | +0.62 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PLA2G15]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB8]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC13]] | -0.59 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[DECR1]] | -0.59 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[CASC9]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[LEPROT]] | -0.58 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[NFKB1]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.56 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[NCOA4]] | -0.56 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[MCTS1]] | -0.55 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LIG4]] | -0.55 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[RAP2C-AS1]] | -0.55 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| KIT | B | KIT activity lowers PKD1P6's level | compounds that target KIT: 3 of 4 raise it (Pexidartinib, Ponatinib, c-Kit-IN-1) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[STARD9]] | B | STARD9 activity raises PKD1P6's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without STARD9 | 0.046 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SEMA3C]] | B | SEMA3C activity lowers PKD1P6's level | lines that do not express SEMA3C (8) vs lines expressing it (42) | 1.41× higher at baseline in the lines without SEMA3C | 0.067 | ⚠ within organs, on part of the lines; also absent: IKZF2, ANTXR2 |
| [[HDAC6]] | B | HDAC6 activity lowers PKD1P6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARAP2]] | B | ARAP2 activity lowers PKD1P6's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 1.40× higher at baseline in the lines without ARAP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.6, -2.6); signed map (-41.5, 2.5). **Vector** length 62.9, 8.85% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +7.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.9 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -10.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | polycystin 1, transient receptor potential channel interacting pseudogene 6 |
| Locus type | pseudogene |
| Location | 16p13.11 — chr16:15,125,242-15,154,564 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30070) · Entrez [353511](https://www.ncbi.nlm.nih.gov/gene/353511) · Ensembl [ENSG00000250251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250251)

## Data

Gene col 14675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14675); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14675]; `tensor/DDL_lfc|DDL_z.npy` [14675]; `embed/gene_vectors.npy` [14675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14675 or target_col == 14675). Every well: [[PKD1P6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD1P6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
