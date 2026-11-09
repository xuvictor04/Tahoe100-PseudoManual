---
symbol: "SNUPN"
type: "gene"
col: 9798
ensembl_id: "ENSG00000169371"
name: "snurportin 1"
location: "15q24.2"
module: 20
arm: "+"
pooled_cpm: 18.23
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SNUPN

*snurportin 1* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.92× (z +16.5, q 0e+00, up in 26 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +8.8, q 3e-16, up in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LoVo 9.99×, HOP62 5.59×, A549 5.53×, KATO III 6.08×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 10.2×, NCI-H460 5.47×, HOP62 4.83×, C32 5.96×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 4.83×, HOP62 4.45×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 2.42×, A498 2.16×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.617× (z -10.9, q 6e-25, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2]] (+0.48, fdr 4e-05), [[RNPS1]] (+0.46, fdr 8e-05), [[NUDT13]] (+0.46, fdr 1e-04); moves opposite to [[AHI1]] (-0.47, fdr 3e-05), [[HES4]] (-0.44, fdr 2e-04), [[GNG5]] (-0.44, fdr 4e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (LoVo 9.99×, HOP62 5.59×, A549 5.53×, KATO III 6.08×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 10.2×, NCI-H460 5.47×, HOP62 4.83×, C32 5.96×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 4.83×, HOP62 4.45×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 2.42×, A498 2.16×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +16.5 | 0e+00 | 26/27 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +14.2 | 1e-43 | 35/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +10.9 | 1e-25 | 24/32 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +8.8 | 3e-16 | 24/46 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.45×** | +5.9 | 3e-07 | 23/43 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.78×** | +4.8 | 1e-04 | 25/44 (RKO, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.3 | 0.001 | 15/41 (CFPAC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.15× | +3.3 | 0.076 | 4/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.086 | 7/46 (NCI-H1573, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -10.9 | 6e-25 | 30/46 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.552×** | -9.5 | 7e-19 | 37/46 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -7.0 | 4e-10 | 24/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -5.8 | 8e-07 | 23/47 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -5.8 | 9e-07 | 20/46 (LS 180, HCT15, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.730×** | -5.0 | 5e-05 | 20/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.751×** | -4.4 | 9e-04 | 17/46 (HOP62, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.778×** | -3.8 | 0.009 | 18/46 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.017 | 15/46 (HOP62, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.805×** | -3.4 | 0.032 | 19/46 (HOP62, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.808×** | -3.4 | 0.038 | 18/46 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.811×** | -3.2 | 0.067 | 15/43 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.823×** | -3.1 | 0.090 | 18/46 (HOP62, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.59× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.9) |
| [[LoVo (line)]] | wt | 16.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +18.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 15.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[C32 (line)]] | wt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 13.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +12.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 38.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -10.0) |
| [[A-172 (line)]] | wt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.6) | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -11.7) |
| [[A549 (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +10.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.46× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.5) |
| [[J82 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.8) |
| [[KATO III (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.08× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.81× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -12.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2]] | +0.48 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[RNPS1]] | +0.46 | +0.43 / +0.37 | both halves | 8e-05 |  |
| [[NUDT13]] | +0.46 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[THOC5]] | +0.46 | +0.42 / +0.36 | both halves | 1e-04 |  |
| [[SEPHS1]] | +0.46 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[STK35]] | +0.45 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[TRMU]] | +0.43 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[TMEM94]] | +0.43 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[ELAVL1]] | +0.43 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[AK4]] | +0.42 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[C1D]] | +0.41 | +0.31 / +0.40 | both halves | 2e-04 |  |
| [[CD302]] | +0.41 | +0.22 / +0.38 | both halves | 6e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[HES4]] | -0.44 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[GNG5]] | -0.44 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[TRAPPC4]] | -0.42 | -0.34 / -0.32 | both halves | 1e-04 |  |
| [[ARFGAP3]] | -0.40 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[YIF1A]] | -0.40 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[ERVK3-1]] | -0.38 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[HEATR5A]] | -0.37 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[TUBB2A]] | -0.37 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | -0.37 | -0.27 / -0.28 | both halves | 3e-04 |  |
| [[ID3]] | -0.36 | -0.22 / -0.35 | both halves | 6e-04 |  |
| [[MRTFA]] | -0.36 | -0.21 / -0.32 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SNUPN's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.287). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.5, -28.7); signed map (-23.8, -46.1). **Vector** length 59.2, 9.49% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +16.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +14.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.4 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -9.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.6 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.5 | -10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.0 | +0.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -0.8 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -0.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | snurportin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,598,083-75,626,469 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNURPORTIN-1, Snurportin1; previously RNUT1 |
| Reactome | 3 pathways, smallest: Metabolism of non-coding RNA; snRNP Assembly; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O95149](https://www.uniprot.org/uniprotkb/O95149) (Snurportin-1):

> Functions as an U snRNP-specific nuclear import adapter. Involved in the trimethylguanosine (m3G)-cap-dependent nuclear import of U snRNPs. Binds specifically to the terminal m3G-cap U snRNAs.

**Summary**, from NCBI Gene [10073](https://www.ncbi.nlm.nih.gov/gene/10073):

> The nuclear import of the spliceosomal snRNPs U1, U2, U4 and U5, is dependent on the presence of a complex nuclear localization signal. The latter is composed of the 5'-2,2,7-terminal trimethylguanosine (m3G) cap structure of the U snRNA and the Sm core domain. The protein encoded by this gene interacts specifically with m3G-cap and functions as an snRNP-specific nuclear import receptor. Alternatively spliced transcript variants encoding the same protein have been identified for this gene. …

**Accessions** — [HGNC:14245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14245) · Entrez [10073](https://www.ncbi.nlm.nih.gov/gene/10073) · UniProt [O95149](https://www.uniprot.org/uniprotkb/O95149) · Ensembl [ENSG00000169371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169371)

## Data

Gene col 9798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9798); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9798]; `tensor/DDL_lfc|DDL_z.npy` [9798]; `embed/gene_vectors.npy` [9798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9798 or target_col == 9798). Every well: [[SNUPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNUPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
