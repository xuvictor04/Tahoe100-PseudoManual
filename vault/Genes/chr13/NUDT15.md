---
symbol: "NUDT15"
type: "gene"
col: 5827
ensembl_id: "ENSG00000136159"
name: "nudix hydrolase 15"
location: "13q14.2"
module: 6
arm: "+"
pooled_cpm: 12.74
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NUDT15

*nudix hydrolase 15* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +17.4, q 0e+00, up in 33 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.22× (z +3.7, q 0.015, up in 8 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 5.30×, SW480 4.29×, LoVo 4.45×, NCI-H460 4.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.02×, SW480 3.48×, SW1417 4.77×, HT-29 4.57×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 2.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.712× (z -6.2, q 3e-07, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSE1L]] (+0.67, fdr 8e-06), [[TIMELESS]] (+0.67, fdr 7e-06), [[DSCC1]] (+0.63, fdr 7e-06); moves opposite to [[RRAGC]] (-0.59, fdr 3e-05), [[UBXN1]] (-0.56, fdr 3e-05), [[ZMYM5]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5827.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 5.30×, SW480 4.29×, LoVo 4.45×, NCI-H460 4.70×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.02×, SW480 3.48×, SW1417 4.77×, HT-29 4.57×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 2.99×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.83×** | +17.4 | 0e+00 | 33/35 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.58×** | +15.9 | 0e+00 | 21/23 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.57×** | +11.3 | 3e-27 | 26/29 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +9.2 | 8e-18 | 36/42 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.58×** | +5.9 | 3e-07 | 25/42 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.57×** | +5.6 | 2e-06 | 22/39 (LoVo, SNU-423, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +3.8 | 0.010 | 16/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.015 | 8/48 (HEC-1-A, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.13 | 9/47 (SW480, H4, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 1.18× | +3.0 | 0.13 | 7/48 (Hs 766T, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.712×** | -6.2 | 3e-07 | 27/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -4.7 | 7e-04 | 21/45 (C-33 A, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -4.5 | 0.001 | 18/46 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.794×** | -4.2 | 0.004 | 18/48 (LoVo, H4, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.718×** | -4.0 | 0.006 | 17/48 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.751×** | -3.7 | 0.020 | 13/45 (SW 900, RKO, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.744×** | -3.7 | 0.020 | 18/45 (LS 180, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.759×** | -3.5 | 0.027 | 13/48 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.606×** | -3.4 | 0.041 | 11/48 (RKO, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.4 | 0.041 | 6/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.771×** | -3.3 | 0.041 | 12/47 (SW 1271, A-427, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.772×** | -3.3 | 0.041 | 1/47 (A-427) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.835× | -3.2 | 0.065 | 12/48 (SW480, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.628×** | -3.1 | 0.068 | 6/46 (MIA PaCa-2, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.756×** | -3.0 | 0.093 | 14/48 (SW480, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.6) |
| [[HT-29 (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 10.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 13.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 7.79 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0780× (z -12.1) |
| [[A-427 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -8.5) |
| [[A549 (line)]] | wt | 8.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 7.53 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.3) |
| [[SW1417 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSE1L]] | +0.67 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[TIMELESS]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[TRIP13]] | +0.63 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[TFDP1]] | +0.63 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[RFC5]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TYMS]] | +0.61 | +0.67 / +0.50 | both halves | 1e-05 | pathway: Metabolism of nucleotides; STRING 882 |
| [[CENPH]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PRPS2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TOPBP1]] | +0.60 | +0.72 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGC]] | -0.59 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[UBXN1]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ZMYM5]] | -0.55 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.55 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[LRSAM1]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.53 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[GABARAP]] ⚠ | -0.52 | -0.56 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG32]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD49]] | -0.51 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[PRRC2C]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[BOD1L1]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises NUDT15's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without CDCA7 | 0.023 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.0, -40.5); signed map (-34.2, -46.1). **Vector** length 68.2, 11.9% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Transcriptional Regulation by E2F6* (reactome, mean cos +0.50 to 10); *Transcription of E2F targets under negative control by DREAM complex* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.7 | +17.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.3 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.1 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.1 | +0.0 |
|  | [[Irinotecan (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:48,037,726-48,047,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTH2, FLJ10956 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 6 pathways, smallest: Phosphate bond hydrolysis by NUDT proteins; Purine catabolism; Azathioprine ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV35](https://www.uniprot.org/uniprotkb/Q9NV35) (Nucleotide triphosphate diphosphatase NUDT15):

> Catalyzes the hydrolysis of nucleoside triphosphates including dGTP, dTTP, dCTP, their oxidized forms like 8-oxo-dGTP and the prodrug thiopurine derivatives 6-thio-dGTP and 6-thio-GTP. Could also catalyze the hydrolysis of some nucleoside diphosphate derivatives. Hydrolyzes oxidized nucleosides triphosphates like 8-oxo-dGTP in vitro, but the specificity and efficiency towards these substrates are low. Therefore, the potential in vivo sanitizing role of this enzyme, that would consist in …

**Summary**, from NCBI Gene [55270](https://www.ncbi.nlm.nih.gov/gene/55270):

> This gene encodes an enzyme that belongs to the Nudix hydrolase superfamily. Members of this superfamily catalyze the hydrolysis of nucleoside diphosphates, including substrates like 8-oxo-dGTP, which are a result of oxidative damage, and can induce base mispairing during DNA replication, causing transversions. The encoded enzyme is a negative regulator of thiopurine activation and toxicity. Mutations in this gene result in poor metabolism of thiopurines, and are associated with …

**Accessions** — [HGNC:23063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23063) · Entrez [55270](https://www.ncbi.nlm.nih.gov/gene/55270) · UniProt [Q9NV35](https://www.uniprot.org/uniprotkb/Q9NV35) · Ensembl [ENSG00000136159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136159)

## Data

Gene col 5827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5827); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5827]; `tensor/DDL_lfc|DDL_z.npy` [5827]; `embed/gene_vectors.npy` [5827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5827 or target_col == 5827). Every well: [[NUDT15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
