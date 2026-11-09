---
symbol: "ILK"
type: "gene"
col: 9285
ensembl_id: "ENSG00000166333"
name: "integrin linked kinase"
location: "11p15.4"
module: 5
arm: "-"
pooled_cpm: 39.98
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ILK

*integrin linked kinase* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.25× (z +6.1, q 7e-07, up in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~97% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.62× (z +4.8, q 3e-04, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.624× (z -12.7, q 5e-34, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTR1B]] (+0.59, fdr 1e-05), [[HCFC2]] (+0.56, fdr 3e-05), [[PRR14]] (+0.55, fdr 4e-05); moves opposite to [[PRMT3]] (-0.57, fdr 2e-05), [[TMEM11-DT]] (-0.57, fdr 3e-05), [[TANGO6]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.25×** | +6.1 | 7e-07 | 22/47 (PANC-1, A549, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.32×** | +5.1 | 1e-04 | 27/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +4.8 | 3e-04 | 20/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.003 | 17/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.9 | 0.011 | 15/48 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.094 | 8/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.11 | 14/37 (LOX-IMVI, A498, …) | inconsistent across doses | composition shift; position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.19× | +3.1 | 0.12 | 13/48 (NCI-H2030, AsPC-1, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -12.7 | 5e-34 | 37/47 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.681×** | -7.0 | 7e-10 | 31/46 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.778×** | -6.7 | 3e-09 | 28/48 (HOP62, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.689×** | -6.7 | 4e-09 | 33/48 (A549, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.759×** | -5.2 | 2e-05 | 26/48 (A549, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.760×** | -5.2 | 2e-05 | 25/48 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.765×** | -5.1 | 3e-05 | 23/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -4.9 | 6e-05 | 25/48 (HEC-1-A, H4, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.778×** | -4.6 | 3e-04 | 23/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.806×** | -4.1 | 0.003 | 16/48 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.669×** | -4.0 | 0.004 | 19/43 (RPMI-7951, NCI-H1573, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.822×** | -3.7 | 0.010 | 17/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 64.3 | 8 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +25.1) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[A549 (line)]] | wt | 49.4 | 4 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +19.6) ⚠ cell-cycle shift, explains ~97% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.9) |
| [[LoVo (line)]] | wt | 26.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.36× (z +10.1) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 5 µM 0.174× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -8.9) |
| [[RKO (line)]] | wt | 39.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +17.4) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[A-172 (line)]] | wt | 71.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -11.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 31.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.33× (z +9.7) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 32.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.5) ⚠ cell-cycle shift, explains ~97% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 56.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.3) ⚠ cell-cycle shift, explains ~97% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -13.8) |
| [[HOP62 (line)]] | alt | 44.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.4) |
| [[HT-29 (line)]] | alt | 44.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.6) ⚠ cell-cycle shift, explains ~97% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.9) ⚠ cell-cycle shift, explains ~97% of this change |
| [[SNU-1 (line)]] | wt | 68.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -8.6) |
| [[KATO III (line)]] | alt | 15.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.5) |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 21.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.104× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 43.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.4) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[A498 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR1B]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[HCFC2]] | +0.56 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PRR14]] | +0.55 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[GPR108]] | +0.54 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[ALAD]] | +0.53 | +0.53 / +0.28 | both halves | 3e-04 |  |
| [[CRIP2]] | +0.52 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[RING1]] | +0.52 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[KIDINS220]] | +0.51 | +0.29 / +0.52 | both halves | 3e-04 | same gene group |
| [[ZNF205]] | +0.51 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[TMEM14A]] | +0.51 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[DDAH2]] | +0.50 | +0.40 / +0.44 | both halves | 4e-05 |  |
| [[CLIC1]] | +0.50 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT3]] | -0.57 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[TMEM11-DT]] | -0.57 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TANGO6]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[NSMAF]] | -0.55 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[MCM9]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[LYRM4]] | -0.54 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[EEF1AKMT1]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[KCNJ14]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TXN]] | -0.52 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SPOPL-DT]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SLFNL1-AS1]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ILK's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LGALS1]] | B | LGALS1 activity raises ILK's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 1.25× lower at baseline in the lines without LGALS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[PDLIM2]] | C | PDLIM2 activity raises ILK's level | lines that do not express PDLIM2 (4) vs lines expressing it (46) | 1.58× lower at baseline in the lines without PDLIM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FSTL3, BIRC3, BOK; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (2.3, -33.5); signed map (-11.2, 17.0). **Vector** length 97.0, 21.5% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +6.4 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +4.5 | +6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.6 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.6 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -3.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | -3.5 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -6.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | integrin linked kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,603,708-6,610,874 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Mixed lineage kinase family; ILK-PINCH-Parvin complex subunits |
| Reactome | 4 pathways, smallest: Localization of the PINCH-ILK-PARVIN complex to focal adhesions; Cell-extracellular matrix interactions; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13418](https://www.uniprot.org/uniprotkb/Q13418) (Scaffold protein ILK):

> Scaffold protein which mediates protein-protein interactions during a range of cellular events including focal adhesion assembly, cell adhesion and cell migration. Regulates integrin-mediated signal transduction by contributing to inside-out integrin activation (By similarity). Recruits PARVA and LIMS1/PITCH to form the heterotrimeric IPP (ILK-PINCH-PARVIN) complex which binds to F-actin via the C-terminal tail of LIMS1 and the N-terminal region of PARVA, promoting F-actin filament bundling, a …

**Summary**, from NCBI Gene [3611](https://www.ncbi.nlm.nih.gov/gene/3611):

> This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastasis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:6040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6040) · Entrez [3611](https://www.ncbi.nlm.nih.gov/gene/3611) · UniProt [Q13418](https://www.uniprot.org/uniprotkb/Q13418) · Ensembl [ENSG00000166333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166333)

## Data

Gene col 9285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9285); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9285]; `tensor/DDL_lfc|DDL_z.npy` [9285]; `embed/gene_vectors.npy` [9285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9285 or target_col == 9285). Every well: [[ILK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
