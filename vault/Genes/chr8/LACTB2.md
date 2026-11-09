---
symbol: "LACTB2"
type: "gene"
col: 7202
ensembl_id: "ENSG00000147592"
name: "lactamase beta 2"
location: "8q13.3"
module: 68
arm: "+"
pooled_cpm: 14.34
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# LACTB2

*lactamase beta 2* — 8q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.40× (z +14.6, q 1e-45, up in 33 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +10.9, q 1e-25, up in 36 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.201×, LoVo 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ivermectin (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0756×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.286×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0681×).
> Its strongest partners by |cos| (63 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 37 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD2B]] (+0.74, fdr 1e-05), [[PATL2]] (+0.71, fdr 1e-04), [[TSGA10]] (+0.70, fdr 5e-05); moves opposite to [[GFOD2]] (-0.67, fdr 2e-04), [[GNAI2]] (-0.65, fdr 2e-04), [[TAF5L]] (-0.65, fdr 1e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.40×** | +14.6 | 1e-45 | 33/35 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.06×** | +13.3 | 7e-38 | 22/23 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +10.9 | 1e-25 | 36/43 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +10.4 | 5e-23 | 26/28 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +9.5 | 3e-19 | 28/44 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +7.5 | 9e-12 | 34/41 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +7.4 | 1e-11 | 37/48 (J82, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.08×** | +7.2 | 4e-11 | 38/47 (HOP62, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +6.4 | 1e-08 | 33/39 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +6.3 | 2e-08 | 28/43 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.9 | 2e-07 | 35/45 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.80×** | +5.6 | 1e-06 | 28/45 (J82, NCI-H1573, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.7 | 9e-05 | 23/47 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.7 | 1e-04 | 25/46 (J82, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.002 | 21/46 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.032 | 13/46 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.040 | 11/46 (A-172, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.054 | 13/47 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.201×, LoVo 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ivermectin (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0756×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.286×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (A-427 0.0681×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.882× | -3.9 | 0.063 | 15/48 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.730× | -3.1 | 0.34 | 11/47 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.732× | -3.1 | 0.34 | 10/48 (SW480, SW 1088, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 12.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 16.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.78× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.201× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 31.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 12.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.3× (z +13.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 17.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 9.76 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +13.9) | — |
| [[A-427 (line)]] | wt | 24.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.3) | [[PH-797804 (drug)]] 5 µM 0.0681× (z -9.0) |
| [[HT-29 (line)]] | alt | 39.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 16.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +8.5) | — |
| [[SW480 (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +11.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.06 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.104× (z -8.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[CFPAC-1 (line)]] | alt | 6.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0756× (z -9.6) |
| [[LoVo (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 29 of them with an alert (⚠; 29 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD2B]] | +0.74 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[PATL2]] | +0.71 | +0.78 / +0.35 | both halves | 1e-04 |  |
| [[TSGA10]] | +0.70 | +0.78 / +0.40 | both halves | 5e-05 |  |
| [[RIPK2-DT]] | +0.69 | +0.77 / +0.31 | both halves | 2e-04 |  |
| [[PLBD1-AS1]] | +0.68 | +0.73 / +0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[IQCH-AS1]] | +0.67 | +0.80 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[TMEM35B]] | +0.67 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[PHACTR2]] | +0.66 | +0.68 / +0.29 | both halves | 3e-04 |  |
| [[TIA1]] | +0.66 | +0.76 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[WAC-AS1]] | +0.66 | +0.74 / +0.24 | both halves | 4e-04 |  |
| [[TCEAL1]] | +0.66 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[ANKRD18B]] | +0.65 | +0.65 / +0.23 | both halves | 5e-04 |  |
| [[ZNF462]] | +0.65 | +0.62 / +0.36 | both halves | 1e-04 |  |
| [[ARRDC3-AS1]] | +0.64 | +0.72 / +0.24 | both halves | 5e-04 |  |
| [[GYG1]] | +0.64 | +0.72 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFOD2]] | -0.67 | -0.72 / -0.29 | both halves | 2e-04 |  |
| [[GNAI2]] | -0.65 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[TAF5L]] | -0.65 | -0.71 / -0.35 | both halves | 1e-04 |  |
| [[PBX4]] | -0.64 | -0.65 / -0.22 | both halves | 6e-04 |  |
| [[OGG1]] | -0.63 | -0.56 / -0.24 | both halves | 5e-04 |  |
| [[SLC27A1]] | -0.62 | -0.68 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[GET1]] | -0.62 | -0.71 / -0.22 | both halves | 6e-04 |  |
| [[PCMT1]] | -0.62 | -0.73 / -0.03 | ⚠ one half (not replicated) | 0.007 |  |
| [[IGSF8]] | -0.62 | -0.64 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ANKRD27]] | -0.61 | -0.72 / -0.03 | ⚠ one half (not replicated) | 0.006 |  |
| [[MINK1]] | -0.61 | -0.71 / -0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[PI4KAP2]] | -0.61 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[FHIP1B]] | -0.60 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[PHKA2]] | -0.60 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[ABHD17A]] | -0.60 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[E4F1]] | -0.59 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[CROCCP3]] | -0.59 | -0.61 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LACTB2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL28A1]] | C | COL28A1 activity lowers LACTB2's level | lines that do not express COL28A1 (3) vs lines expressing it (47) | 1.63× higher at baseline in the lines without COL28A1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC6, KIFC3, MLLT3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.9, 12.3); signed map (22.9, -15.5). **Vector** length 66.2, 12.9% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.6 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -3.6 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | +0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | lactamase beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.3 — chr8:70,635,318-70,669,185 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-83 |
| Gene groups (HGNC) | MBL domain containing glyoxalase 2 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53H82](https://www.uniprot.org/uniprotkb/Q53H82) (Endoribonuclease LACTB2):

> Endoribonuclease; cleaves preferentially 3' to purine-pyrimidine dinucleotide motifs in single-stranded RNA. The cleavage product contains a free 3' -OH group. Has no activity with double-stranded RNA or DNA. Required for normal mitochondrial function and cell viability.

**Summary**, from NCBI Gene [51110](https://www.ncbi.nlm.nih.gov/gene/51110):

> Enables RNA endonuclease activity; single-stranded RNA binding activity; and zinc ion binding activity. Located in several cellular components, including Golgi apparatus; mitochondrial matrix; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18512) · Entrez [51110](https://www.ncbi.nlm.nih.gov/gene/51110) · UniProt [Q53H82](https://www.uniprot.org/uniprotkb/Q53H82) · Ensembl [ENSG00000147592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147592)

## Data

Gene col 7202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7202); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7202]; `tensor/DDL_lfc|DDL_z.npy` [7202]; `embed/gene_vectors.npy` [7202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7202 or target_col == 7202). Every well: [[LACTB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LACTB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
