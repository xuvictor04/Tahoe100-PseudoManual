---
symbol: "SNAI2"
type: "gene"
col: 314
ensembl_id: "ENSG00000019549"
name: "snail family transcriptional repressor 2"
location: "8q11.21"
module: 98
arm: "+"
pooled_cpm: 11.05
n_lines_expressing: 27
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 26
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 11
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# SNAI2

*snail family transcriptional repressor 2* — 8q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 4.64× (z +13.5, q 1e-38, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.535× (z -7.8, q 5e-12, down in 18 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RPMI-7951 0.0427×, hTERT-HPNE 0.0581×, HOP62 0.136×, LOX-IMVI 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0610×, HOP62 0.108×, hTERT-HPNE 0.121×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.122×, LOX-IMVI 0.142×, AsPC-1 0.265×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0647×, LOX-IMVI 0.128×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.111×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAFB]] (+0.65, fdr 7e-06), [[DUSP1]] (+0.63, fdr 7e-06), [[MAOA]] (+0.63, fdr 7e-06); moves opposite to [[DENND11]] (-0.48, fdr 3e-05), [[LINC02210-CRHR1]] (-0.46, fdr 4e-05), [[HAGH]] (-0.46, fdr 3e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ETS2]] → it (grade B ⚠); 11 go from it, the strongest it → [[BIRC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **4.64×** | +13.5 | 1e-38 | 23/25 (AsPC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.50×** | +11.3 | 4e-27 | 20/24 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **3.12×** | +10.4 | 4e-23 | 19/25 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.12×** | +10.4 | 4e-23 | 20/25 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.08×** | +7.8 | 1e-12 | 23/24 (AsPC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **2.27×** | +7.5 | 7e-12 | 16/25 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **2.23×** | +7.3 | 2e-11 | 17/24 (Hs 766T, HS-578T, …) | all doses, flat | position effect removed |
| [[Econazole (drug)]] 5 µM |  | **2.16×** | +7.0 | 1e-10 | 16/25 (Hs 766T, NCI-H2347, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.15×** | +7.0 | 2e-10 | 16/24 (Hs 766T, AsPC-1, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.18×** | +6.8 | 4e-10 | 17/25 (Hs 766T, HS-578T, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +6.8 | 7e-10 | 17/25 (NCI-H2347, Hs 766T, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **2.07×** | +6.6 | 2e-09 | 14/24 (Hs 766T, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.07×** | +6.6 | 2e-09 | 16/24 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.99×** | +6.3 | 1e-08 | 14/25 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.92×** | +6.0 | 1e-07 | 15/25 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.99×** | +5.8 | 2e-07 | 18/24 (Hs 766T, HS-578T, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.84×** | +5.6 | 9e-07 | 13/25 (Hs 766T, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 314.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RPMI-7951 0.0427×, hTERT-HPNE 0.0581×, HOP62 0.136×, LOX-IMVI 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0610×, HOP62 0.108×, hTERT-HPNE 0.121×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.122×, LOX-IMVI 0.142×, AsPC-1 0.265×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0647×, LOX-IMVI 0.128×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.111×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -7.8 | 5e-12 | 18/23 (hTERT-HPNE, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -3.7 | 0.054 | 10/17 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -3.6 | 0.054 | 15/24 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0581× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 36.5 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +21.1) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 15.5× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -10.0) |
| [[HOP62 (line)]] | alt | 26.8 | 2 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 5.91× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -12.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.21× (z +9.5) ⚠ position correction uncertain · without an alert: [[Dexamethasone (drug)]] 0.5 µM 6.22× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 42.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0610× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 14.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 13.3× (z +11.1) ⚠ position correction uncertain · without an alert: [[Harringtonine (drug)]] 5 µM 11.7× (z +10.2) | — |
| [[C32 (line)]] | wt | 23.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +9.9) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 5 µM 0.144× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 46.4 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 7.20× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0427× (z -17.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.07 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +11.2) ⚠ position correction uncertain | — |
| [[A-172 (line)]] | wt | 15.9 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 7.41× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +9.6) ⚠ position correction uncertain | — |
| [[H4 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0608× (z -10.1) ⚠ cell-cycle shift, explains ~74% of this change |
| [[HS-578T (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.7) ⚠ position correction uncertain | — |
| [[NCI-H460 (line)]] | wt | 9.32 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.85× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 32.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.69× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 3.88 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +10.4) ⚠ position correction uncertain | — |
| [[A-427 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFB]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DUSP1]] | +0.63 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[MAOA]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MT1E]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[KLF9]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions |
| [[TNFAIP3]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ZC3H12A]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[PID1]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[HIPK2]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[MT1M]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[IRX3]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.55 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND11]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LINC02210-CRHR1]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[HAGH]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS2]] | B | ETS2 activity raises SNAI2's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 3.78× lower at baseline in the lines without ETS2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[NR3C1]] | B | NR3C1 activity raises SNAI2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[WNT5A]] | C | WNT5A activity raises SNAI2's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.80× lower at baseline in the lines without WNT5A | 0.001 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[PRICKLE2]] | C | PRICKLE2 activity raises SNAI2's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 4.25× lower at baseline in the lines without PRICKLE2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973; co-absent with the target |
| [[IRAK3]] | C | IRAK3 activity raises SNAI2's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.87× lower at baseline in the lines without IRAK3 | 0.054 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[ABLIM3]] | C | ABLIM3 activity raises SNAI2's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 3.38× lower at baseline in the lines without ABLIM3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises SNAI2's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 3.85× lower at baseline in the lines without PRR16 | 0.069 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIRC3]] | B | SNAI2 activity lowers BIRC3's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 1.44× higher at baseline in the lines without SNAI2 | 0.034 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[TXNIP]] | B | SNAI2 activity raises TXNIP's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 2.07× lower at baseline in the lines without SNAI2 | 0.038 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[ITGA5]] | B | SNAI2 activity raises ITGA5's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 3.88× lower at baseline in the lines without SNAI2 | 0.044 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[IRS2]] | B | SNAI2 activity raises IRS2's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without SNAI2 | 0.067 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[MYO1B]] | B | SNAI2 activity raises MYO1B's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without SNAI2 | 0.071 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[ABLIM3]] | C | SNAI2 activity raises ABLIM3's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 4.19× lower at baseline in the lines without SNAI2 | 0.006 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[PRICKLE2]] | C | SNAI2 activity raises PRICKLE2's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 4.72× lower at baseline in the lines without SNAI2 | 0.009 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[WNT5A]] | C | SNAI2 activity raises WNT5A's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 5.81× lower at baseline in the lines without SNAI2 | 0.011 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[PID1]] | C | SNAI2 activity raises PID1's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 4.58× lower at baseline in the lines without SNAI2 | 0.039 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[TMTC1]] | C | SNAI2 activity raises TMTC1's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 3.74× lower at baseline in the lines without SNAI2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[DCLK1]] | C | SNAI2 activity raises DCLK1's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without SNAI2 | 0.078 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, 13.6); signed map (15.1, 30.5). **Vector** length 107, 34.8% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | +4.6 | +10.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.1 | +6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | +4.0 | +5.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.9 | +6.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.6 | +6.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.6 | +6.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | snail family transcriptional repressor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.21 — chr8:48,917,598-48,921,740 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLUGH1, SNAIL2, SLUGH; previously SLUG |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SNAG transcriptional repressors |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 15 pathways, smallest: Negative Regulation of CDH1 Gene Transcription; Transcriptional and post-translational regulation of MITF-M expression and activity; Regulation of CDH1 Gene Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [O43623](https://www.uniprot.org/uniprotkb/O43623) (Zinc finger protein SNAI2):

> Transcriptional repressor that modulates both activator-dependent and basal transcription. Involved in the generation and migration of neural crest cells. Plays a role in mediating RAF1-induced transcriptional repression of the TJ protein, occludin (OCLN) and subsequent oncogenic transformation of epithelial cells (By similarity). Represses BRCA2 expression by binding to its E2-box-containing silencer and recruiting CTBP1 and HDAC1 in breast cells. In epidermal keratinocytes, binds to the E-box …

**Summary**, from NCBI Gene [6591](https://www.ncbi.nlm.nih.gov/gene/6591):

> This gene encodes a member of the Snail family of C2H2-type zinc finger transcription factors. The encoded protein acts as a transcriptional repressor that binds to E-box motifs and is also likely to repress E-cadherin transcription in breast carcinoma. This protein is involved in epithelial-mesenchymal transitions and has antiapoptotic activity. Mutations in this gene may be associated with sporatic cases of neural tube defects. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11094) · Entrez [6591](https://www.ncbi.nlm.nih.gov/gene/6591) · UniProt [O43623](https://www.uniprot.org/uniprotkb/O43623) · Ensembl [ENSG00000019549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000019549)

## Data

Gene col 314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 314); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 314]; `tensor/DDL_lfc|DDL_z.npy` [314]; `embed/gene_vectors.npy` [314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 314 or target_col == 314). Every well: [[SNAI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
