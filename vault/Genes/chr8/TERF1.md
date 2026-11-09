---
symbol: "TERF1"
type: "gene"
col: 7203
ensembl_id: "ENSG00000147601"
name: "telomeric repeat binding factor 1"
location: "8q21.11"
module: 45
arm: "+"
pooled_cpm: 39.69
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TERF1

*telomeric repeat binding factor 1* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.08× (z +8.6, q 4e-15, up in 33 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.716× (z -7.5, q 4e-11, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.351×, SHP-77 0.446×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.308×); [[PF-06260933 (drug)]] 5 µM in 1 line (SNU-1 0.0426×); [[OTS514 (drug)]] 5 µM in 1 line (SNU-1 0.0887×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED30]] (+0.76, fdr 7e-06), [[USP30]] (+0.69, fdr 1e-05), [[METTL14]] (+0.67, fdr 7e-06); moves opposite to [[SSUH2]] (-0.63, fdr 9e-06), [[ALDH8A1]] (-0.61, fdr 1e-05), [[SLC2A9]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02977]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +8.6 | 4e-15 | 33/49 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +8.3 | 2e-14 | 38/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +8.2 | 4e-14 | 30/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +7.8 | 1e-12 | 31/48 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +7.7 | 1e-12 | 26/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +5.1 | 3e-05 | 17/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.15× | +4.6 | 4e-04 | 22/48 (A498, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.6 | 4e-04 | 17/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +4.5 | 4e-04 | 19/47 (J82, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.001 | 16/48 (NCI-H2030, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 21/48 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.2 | 0.001 | 19/48 (H4, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.007 | 17/48 (H4, SNU-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +3.7 | 0.007 | 16/48 (HT-29, J82, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.024 | 9/48 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.025 | 9/47 (SW48, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.030 | 14/48 (SW48, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7203.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.351×, SHP-77 0.446×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.308×); [[PF-06260933 (drug)]] 5 µM in 1 line (SNU-1 0.0426×); [[OTS514 (drug)]] 5 µM in 1 line (SNU-1 0.0887×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.716×** | -7.5 | 4e-11 | 29/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -6.8 | 3e-09 | 3/49 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -5.9 | 5e-07 | 19/39 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.787×** | -5.4 | 1e-05 | 20/44 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -4.7 | 3e-04 | 17/48 (KATO III, SW 900, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.834× | -4.1 | 0.005 | 12/47 (AN3 CA, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.780×** | -4.0 | 0.006 | 20/47 (C32, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.842× | -3.8 | 0.009 | 13/48 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.844× | -3.8 | 0.009 | 9/47 (HOP62, hTERT-HPNE, …) | two highest doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -3.6 | 0.019 | 16/48 (SNU-1, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.855× | -3.5 | 0.024 | 14/48 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.871× | -3.1 | 0.093 | 4/48 (COLO 205, SW480, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.873× | -3.0 | 0.10 | 6/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 45.7 | 0 | 4 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.308× (z -11.3) |
| [[A498 (line)]] | wt | 56.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.287× (z -10.1) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H1573 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 96.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 38.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +8.6) | — |
| [[A-172 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED30]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[USP30]] | +0.69 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[METTL14]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[COPS4]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SNX4]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[CDADC1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ALG9]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[KCTD6]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[REPS1]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[EHMT2]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 | pathway: Cellular Senescence |
| [[RHOT1]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSUH2]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[ALDH8A1]] | -0.61 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SLC2A9]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TBILA]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZDHHC11]] | -0.60 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[ADAM32]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[MMP25]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[IDI2-AS1]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[FBXW10B]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[OGDH]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[LINC02977]] | -0.56 | -0.40 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02977]] | B | LINC02977 activity lowers TERF1's level | lines that do not express LINC02977 (8) vs lines expressing it (42) | 1.42× higher at baseline in the lines without LINC02977 | 0.099 | ⚠ within organs, on part of the lines; also absent: SUSD1, FAM83G; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-2.1, -10.3); signed map (-31.0, -10.2). **Vector** length 88.2, 18.3% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +5.1 |
|  | [[NG25 (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +8.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | telomeric repeat binding factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:73,008,856-73,048,123 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIN2, TRF1, TRF; previously TRBF1 |
| Gene groups (HGNC) | Myb/SANT domain containing; Shelterin complex |
| Reactome | 28 pathways, smallest: Telomere C-strand synthesis initiation; Removal of the Flap Intermediate from the C-strand; Packaging Of Telomere Ends |
| Matched by | ensembl_id |

**Function**, from UniProt [P54274](https://www.uniprot.org/uniprotkb/P54274) (Telomeric repeat-binding factor 1):

> Binds the telomeric double-stranded 5'-TTAGGG-3' repeat and negatively regulates telomere length. Involved in the regulation of the mitotic spindle. Component of the shelterin complex (telosome) that is involved in the regulation of telomere length and protection. Shelterin associates with arrays of double-stranded 5'-TTAGGG-3' repeats added by telomerase and protects chromosome ends; without its protective activity, telomeres are no longer hidden from the DNA damage surveillance and chromosome …

**Summary**, from NCBI Gene [7013](https://www.ncbi.nlm.nih.gov/gene/7013):

> This gene encodes a telomere specific protein which is a component of the telomere nucleoprotein complex. This protein is present at telomeres throughout the cell cycle and functions as an inhibitor of telomerase, acting in cis to limit the elongation of individual chromosome ends. The protein structure contains a C-terminal Myb motif, a dimerization domain near its N-terminus and an acidic N-terminus. Multiple transcripts of this gene are alternatively spliced products. [provided by RefSeq, …

**Accessions** — [HGNC:11728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11728) · Entrez [7013](https://www.ncbi.nlm.nih.gov/gene/7013) · UniProt [P54274](https://www.uniprot.org/uniprotkb/P54274) · Ensembl [ENSG00000147601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147601)

## Data

Gene col 7203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7203); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7203]; `tensor/DDL_lfc|DDL_z.npy` [7203]; `embed/gene_vectors.npy` [7203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7203 or target_col == 7203). Every well: [[TERF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TERF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
