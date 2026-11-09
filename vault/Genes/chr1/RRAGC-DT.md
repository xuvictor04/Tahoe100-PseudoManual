---
symbol: "RRAGC-DT"
type: "gene"
col: 13644
ensembl_id: "ENSG00000228436"
name: "RRAGC divergent transcript"
location: "1p34.3"
module: 23
arm: "+"
pooled_cpm: 28.51
n_lines_expressing: 50
n_dd_up: 60
n_dd_down: 0
n_dd_up_clean: 44
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RRAGC-DT

*RRAGC divergent transcript* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 60 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.96× (z +24.1, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A549 0.0796×, A-172 0.134×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (A-172 0.232×, A549 0.221×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0811×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPS1]] (+0.74, fdr 7e-06), [[HSD17B14]] (+0.71, fdr 1e-05), [[CELF6]] (+0.70, fdr 7e-06); moves opposite to [[ATG4C]] (-0.61, fdr 1e-04), [[MRPL17]] (-0.59, fdr 8e-05), [[WASF3]] (-0.58, fdr 9e-04, ⚠ one half only (not replicated)), [[TUBG1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PKD1L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 60 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.96×** | +24.1 | 0e+00 | 47/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +16.8 | 0e+00 | 43/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.29×** | +14.7 | 0e+00 | 42/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.70×** | +12.3 | 2e-32 | 43/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +9.8 | 1e-20 | 34/47 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.17×** | +9.6 | 1e-19 | 38/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +9.3 | 1e-18 | 38/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +8.6 | 5e-16 | 34/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.9 | 2e-13 | 21/34 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.84×** | +7.5 | 4e-12 | 33/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.51×** | +7.2 | 4e-11 | 35/48 (LoVo, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.8 | 5e-10 | 29/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +6.7 | 7e-10 | 25/41 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +6.5 | 4e-09 | 33/44 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +6.4 | 5e-09 | 32/48 (J82, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.5 | 1e-06 | 31/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +5.4 | 2e-06 | 27/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.52×** | +5.2 | 7e-06 | 30/48 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 29/48 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +4.9 | 3e-05 | 25/46 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13644.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A549 0.0796×, A-172 0.134×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (A-172 0.232×, A549 0.221×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Esmolol (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0811×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.3 | 0.53 | 4/49 (SNU-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.2 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +26.2) | — |
| [[HOP62 (line)]] | alt | 33.2 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.7× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.58× (z +16.7) | — |
| [[HS-578T (line)]] | alt | 35.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.50× (z +19.0) | — |
| [[A-172 (line)]] | wt | 34.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -14.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 22.5 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 23.7× (z +15.4) | — |
| [[J82 (line)]] | alt | 46.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +23.7) | — |
| [[KATO III (line)]] | alt | 20.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +16.3) | — |
| [[Panc 03.27 (line)]] | alt | 45.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.1× (z +18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 35.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +22.4) | — |
| [[A-427 (line)]] | wt | 32.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.0) | — |
| [[A549 (line)]] | wt | 19.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0796× (z -15.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 14.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 49.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 45.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +20.6) | — |
| [[HT-29 (line)]] | alt | 45.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.27× (z +10.9) | — |
| [[LoVo (line)]] | wt | 19.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 25.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 35.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.6) | — |
| [[A498 (line)]] | wt | 17.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +12.6) | — |
| [[H4 (line)]] | wt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 49.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 10.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.8) | — |
| [[RKO (line)]] | wt | 21.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.03× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 53.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +15.0) | — |
| [[SNU-1 (line)]] | wt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 54.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.1) | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0811× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 8.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 68.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.95× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.0) | — |
| [[SW480 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPS1]] | +0.74 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[HSD17B14]] | +0.71 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CELF6]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[FLCN]] | +0.69 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[CDKL3]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[TMEM192]] | +0.67 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[GTF2H1]] | +0.67 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[MAFG]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[OSTM1]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[RNF103-CHMP3]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GTF2IRD2]] | +0.65 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[STX3]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | -0.61 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[MRPL17]] | -0.59 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[WASF3]] | -0.58 | -0.59 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[TUBG1]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[POMGNT2]] | -0.55 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[ELP1]] | -0.55 | -0.54 / -0.24 | both halves | 4e-04 |  |
| [[RNGTT]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKD1L2]] | B | PKD1L2 activity raises RRAGC-DT's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without PKD1L2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (11.6, 12.8); signed map (19.9, -4.0). **Vector** length 124, 37.6% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.9 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +12.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.5 | +9.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +9.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.4 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +6.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.4 | +3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.2 | +5.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +4.2 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | +2.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | +2.8 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RRAGC divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.3 — chr1:38,859,912-38,965,038 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LENGA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55793) · Entrez [105378663](https://www.ncbi.nlm.nih.gov/gene/105378663) · Ensembl [ENSG00000228436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228436)

## Data

Gene col 13644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13644); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13644]; `tensor/DDL_lfc|DDL_z.npy` [13644]; `embed/gene_vectors.npy` [13644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13644 or target_col == 13644). Every well: [[RRAGC-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAGC-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
