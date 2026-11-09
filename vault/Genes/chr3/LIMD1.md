---
symbol: "LIMD1"
type: "gene"
col: 6928
ensembl_id: "ENSG00000144791"
name: "LIM domain containing 1"
location: "3p21.31"
module: 5
arm: "+"
pooled_cpm: 82.32
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# LIMD1

*LIM domain containing 1* — 3p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 1.76×, LS 180 1.74×, NCI-H460 1.54×; ⚠ cell-cycle shift, explains ~6% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (PANC-1 4.29×, SNU-1 6.60×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 2.68×; ⚠ cell-cycle shift, explains ~25% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.625× (z -15.7, q 0e+00, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.525× (z -15.2, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD16]] (+0.52, fdr 5e-05), [[PRDM15]] (+0.52, fdr 3e-05), [[RPTOR]] (+0.51, fdr 2e-05); moves opposite to [[RAB3GAP2]] (-0.54, fdr 2e-05), [[KIDINS220]] (-0.49, fdr 3e-05), [[JAK1]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6928.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LoVo 1.76×, LS 180 1.74×, NCI-H460 1.54×; ⚠ cell-cycle shift, explains ~6% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (PANC-1 4.29×, SNU-1 6.60×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 2.68×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 1.32× | +3.4 | 0.32 | 22/49 (PANC-1, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.3 | 0.32 | 19/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.37 | 11/47 (SW48, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6928.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.625×** | -15.7 | 0e+00 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.525×** | -15.2 | 0e+00 | 36/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.546×** | -14.3 | 3e-44 | 41/49 (SNU-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.548×** | -14.2 | 8e-44 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.570×** | -12.8 | 3e-35 | 35/48 (NCI-H460, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -10.5 | 1e-23 | 35/45 (C-33 A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -9.8 | 1e-20 | 31/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.688×** | -8.5 | 1e-15 | 25/44 (A-172, SNU-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.715×** | -7.6 | 2e-12 | 29/47 (C-33 A, SHP-77, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.729×** | -7.5 | 5e-12 | 30/48 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.818×** | -4.8 | 1e-04 | 23/48 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.829×** | -4.4 | 4e-04 | 22/48 (LS 180, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.839× | -4.1 | 0.001 | 22/48 (HT-29, LOX-IMVI, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -4.0 | 0.002 | 17/48 (J82, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.843× | -3.9 | 0.004 | 14/48 (C-33 A, SNU-423, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.876× | -3.1 | 0.056 | 17/48 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.873× | -3.1 | 0.062 | 14/49 (HS-578T, HOP62, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.065 | 19/48 (HOP62, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 98.4 | 1 (1 ⚠) | 9 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.8) ⚠ cell-cycle shift, explains ~6% of this change | [[Harringtonine (drug)]] 5 µM 0.195× (z -22.9) |
| [[PANC-1 (line)]] | alt | 130 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -21.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -13.6) |
| [[SNU-423 (line)]] | alt | 111 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.336× (z -11.8) |
| [[C-33 A (line)]] | alt | 109 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 94.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.356× (z -12.6) |
| [[SHP-77 (line)]] | alt | 109 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.263× (z -10.5) |
| [[SW48 (line)]] | wt | 109 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.3) |
| [[SW480 (line)]] | alt | 102 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -17.8) |
| [[A-172 (line)]] | wt | 62.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 116 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -13.3) |
| [[C32 (line)]] | wt | 62.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.388× (z -9.2) |
| [[KATO III (line)]] | alt | 57.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -11.2) |
| [[LoVo (line)]] | wt | 84.5 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +11.1) ⚠ cell-cycle shift, explains ~6% of this change | [[Panobinostat (drug)]] 5 µM 0.442× (z -11.4) |
| [[LS 180 (line)]] | wt | 72.7 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.6) ⚠ cell-cycle shift, explains ~6% of this change | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.440× (z -9.7) |
| [[SW1417 (line)]] | alt | 69.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.429× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 96.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.436× (z -10.7) |
| [[SNU-1 (line)]] | wt | 220 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.60× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -18.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 89.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0885× (z -14.5) |
| [[COLO 205 (line)]] | alt | 51.4 | 1 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.84× (z +8.6) ⚠ cell-cycle shift, explains ~39% of this change | [[Harringtonine (drug)]] 5 µM 0.254× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 80.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 68.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.391× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 86.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.354× (z -10.7) |
| [[A-427 (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -12.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CHP-212 (line)]] | wt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 43.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -12.0) |
| [[Hs 766T (line)]] | wt | 68.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HS-578T (line)]] | alt | 84.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -9.9) |
| [[J82 (line)]] | alt | 98.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 81.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.438× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 52.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.323× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 90.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -13.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 1271 (line)]] | alt | 85.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0735× (z -10.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD16]] | +0.52 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[PRDM15]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RPTOR]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[BANP]] | +0.51 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[ABCC1]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[MFHAS1]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[XXYLT1]] | +0.50 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[TLCD3A]] | +0.49 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ZNF544]] | +0.48 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MED27]] | +0.48 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PRR7-AS1]] | +0.47 | +0.26 / +0.54 | both halves | 4e-04 |  |
| [[MGAT5]] | +0.47 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3GAP2]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[KIDINS220]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[JAK1]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[DENND3]] | -0.48 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[SH3GLB1]] | -0.47 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[MMUT]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SF3B1]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[AASS]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SENP2]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[NUDT16]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PRSS16]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[PKN2]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.387). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (2.2, -34.9); signed map (-7.5, -40.4). **Vector** length 94.5, 22.5% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +6.8 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.5 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -12.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -7.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.1 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,555,394-45,686,341 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ajuba family |
| Reactome | 4 pathways, smallest: Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha; Cellular response to hypoxia; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGP4](https://www.uniprot.org/uniprotkb/Q9UGP4) (LIM domain-containing protein 1):

> Adapter or scaffold protein which participates in the assembly of numerous protein complexes and is involved in several cellular processes such as cell fate determination, cytoskeletal organization, repression of gene transcription, cell-cell adhesion, cell differentiation, proliferation and migration. Positively regulates microRNA (miRNA)-mediated gene silencing and is essential for P-body formation and integrity. Acts as a hypoxic regulator by bridging an association between the prolyl …

**Summary**, from NCBI Gene [8994](https://www.ncbi.nlm.nih.gov/gene/8994):

> Predicted to enable transcription corepressor activity. Involved in several processes, including negative regulation of hippo signaling; regulation of gene expression; and response to hypoxia. Acts upstream of or within P-body assembly and miRNA-mediated post-transcriptional gene silencing. Located in several cellular components, including P-body; adherens junction; and focal adhesion. Part of RISC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6612) · Entrez [8994](https://www.ncbi.nlm.nih.gov/gene/8994) · UniProt [Q9UGP4](https://www.uniprot.org/uniprotkb/Q9UGP4) · Ensembl [ENSG00000144791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144791)

## Data

Gene col 6928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6928); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6928]; `tensor/DDL_lfc|DDL_z.npy` [6928]; `embed/gene_vectors.npy` [6928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6928 or target_col == 6928). Every well: [[LIMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
