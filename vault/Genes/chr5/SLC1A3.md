---
symbol: "SLC1A3"
type: "gene"
col: 1244
ensembl_id: "ENSG00000079215"
name: "solute carrier family 1 member 3"
location: "5p13.2"
module: 104
arm: "+"
pooled_cpm: 13.69
n_lines_expressing: 29
n_dd_up: 58
n_dd_down: 9
n_dd_up_clean: 41
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# SLC1A3

*solute carrier family 1 member 3* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 58 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.46× (z +36.8, q 0e+00, up in 24 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.677× (z -5.1, q 2e-04, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTX3]] (+0.65, fdr 7e-06), [[STOM]] (+0.58, fdr 1e-05), [[FNDC3A]] (+0.58, fdr 2e-05); moves opposite to [[MYO9B]] (-0.54, fdr 2e-05), [[ARID3B]] (-0.49, fdr 2e-04), [[DPP9]] (-0.48, fdr 3e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[CAV1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 58 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.46×** | +36.8 | 0e+00 | 24/27 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.52×** | +16.9 | 0e+00 | 22/26 (A498, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.47×** | +16.1 | 0e+00 | 22/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.46×** | +15.4 | 0e+00 | 22/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.88×** | +13.2 | 1e-37 | 21/24 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.51×** | +11.0 | 3e-26 | 16/18 (NCI-H460, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.35×** | +10.6 | 2e-24 | 10/17 (Panc 03.27, HS-578T, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +10.5 | 8e-24 | 20/26 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.77×** | +10.4 | 1e-23 | 12/25 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.02×** | +8.7 | 1e-16 | 15/26 (NCI-H460, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.88×** | +8.1 | 2e-14 | 15/27 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +7.8 | 4e-13 | 18/27 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.82×** | +7.7 | 6e-13 | 14/27 (A498, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.81×** | +7.6 | 9e-13 | 11/23 (HS-578T, Panc 03.27, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +7.3 | 1e-11 | 17/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.3 | 1e-11 | 13/27 (HOP62, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +6.7 | 6e-10 | 14/27 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.2 | 1e-08 | 14/27 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +5.8 | 2e-07 | 8/26 (SNU-1, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.55×** | +5.7 | 4e-07 | 11/25 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +5.5 | 8e-07 | 13/27 (A498, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +5.1 | 9e-06 | 14/26 (NCI-H23, SW480, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.42×** | +4.4 | 3e-04 | 11/26 (NCI-H1573, SNU-423, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -5.1 | 2e-04 | 16/26 (NCI-H23, SNU-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.720×** | -4.3 | 0.005 | 9/25 (C32, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.009 | 13/26 (SNU-423, HOP62, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.806×** | -4.0 | 0.009 | 8/27 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.043 | 13/27 (HS-578T, Panc 03.27, …) | rises with dose |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.755×** | -3.5 | 0.043 | 7/26 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.767×** | -3.5 | 0.043 | 11/25 (SNU-1, HCT15, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **0.772×** | -3.4 | 0.051 | 9/26 (SNU-1, C32, …) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **0.779×** | -3.3 | 0.068 | 7/25 (SNU-423, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.843× | -3.2 | 0.084 | 10/27 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.851× | -3.0 | 0.14 | 7/27 (A498, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.5 | 16 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +25.6) | — |
| [[HOP62 (line)]] | alt | 12.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +23.0) | — |
| [[J82 (line)]] | alt | 33.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +19.2) | — |
| [[LoVo (line)]] | wt | 16.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +19.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +15.9) | [[AZD2858 (drug)]] 0.5 µM 0.0827× (z -9.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 220 | 2 (1 ⚠) | 2 (2 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 5.83× (z +11.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.29× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.215× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 18.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +15.0) | — |
| [[H4 (line)]] | wt | 15.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +11.4) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.104× (z -8.5) |
| [[HS-578T (line)]] | alt | 3.75 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 6.20× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 5.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +9.3) | — |
| [[C32 (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +13.8) | — |
| [[HCT15 (line)]] | alt | 7.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 3.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 1 | 0 | [[Clobetasol propionate (drug)]] 5 µM 8.51× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +12.6) | — |
| [[A-172 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTX3]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[STOM]] | +0.58 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[FNDC3A]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TMTC1]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SRGN]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[PDZD2]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MYO3B]] | +0.56 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[ETS2]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[RIPOR2]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[EBI3]] | +0.55 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[BCL6]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CEBPD]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[ARID3B]] | -0.49 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[DPP9]] | -0.48 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.47 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[TPST2]] | -0.47 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[UBA6]] | -0.46 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[TANGO2]] | -0.46 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[FAM131A]] | -0.45 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[WNT7B]] | -0.45 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[TPD52L2]] | -0.45 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.44 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[MTMR12]] | -0.44 | -0.47 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC1A3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.0% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CAV1]] | B | CAV1 activity raises SLC1A3's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without CAV1 | 0.062 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[PTX3]] | B | PTX3 activity raises SLC1A3's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 2.26× lower at baseline in the lines without PTX3 | 0.081 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1 |
| [[RIPOR2]] | B | RIPOR2 activity raises SLC1A3's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 3.01× lower at baseline in the lines without RIPOR2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV1]] | B | SLC1A3 activity raises CAV1's level | lines that do not express SLC1A3 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without SLC1A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: LRP2, SLIT2, CHSY3 |
| [[SAMSN1]] | B | SLC1A3 activity raises SAMSN1's level | lines that do not express SLC1A3 (21) vs lines expressing it (29) | 1.68× lower at baseline in the lines without SLC1A3 | 0.075 | ⚠ within organs, on part of the lines; also absent: LRP2, SLIT2, CHSY3 |
| [[LINC01551]] | C | SLC1A3 activity raises LINC01551's level | lines that do not express SLC1A3 (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without SLC1A3 | 0.063 | ⚠ within organs, on part of the lines; also absent: LRP2, SLIT2, CHSY3; co-absent with the target |
| [[FOXG1]] | C | SLC1A3 activity raises FOXG1's level | lines that do not express SLC1A3 (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without SLC1A3 | 0.077 | ⚠ within organs, on part of the lines; also absent: LRP2, SLIT2, CHSY3; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.9, 14.5); signed map (18.8, 29.6). **Vector** length 89.0, 23.2% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +36.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.7 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +16.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +7.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +5.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.4 | +8.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.0 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -1.8 | +7.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 1 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:36,596,588-36,688,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EAAT1, GLAST, EA6, GLAST1, GLAST-1 |
| Gene groups (HGNC) | Solute carrier family 1 |
| Reactome | 13 pathways, smallest: Astrocytic Glutamate-Glutamine Uptake And Metabolism; Neurotransmitter uptake and metabolism In glial cells; Glutamate Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P43003](https://www.uniprot.org/uniprotkb/P43003) (Excitatory amino acid transporter 1):

> Sodium-dependent, high-affinity amino acid transporter that mediates the uptake of L-glutamate and also L-aspartate and D-aspartate. Functions as a symporter that transports one amino acid molecule together with two or three Na(+) ions and one proton, in parallel with the counter-transport of one K(+) ion. Mediates Cl(-) flux that is not coupled to amino acid transport; this avoids the accumulation of negative charges due to aspartate and Na(+) symport. Plays a redundant role in the rapid …

**Summary**, from NCBI Gene [6507](https://www.ncbi.nlm.nih.gov/gene/6507):

> This gene encodes a member of a member of a high affinity glutamate transporter family. This gene functions in the termination of excitatory neurotransmission in central nervous system. Mutations are associated with episodic ataxia, Type 6. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:10941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10941) · Entrez [6507](https://www.ncbi.nlm.nih.gov/gene/6507) · UniProt [P43003](https://www.uniprot.org/uniprotkb/P43003) · Ensembl [ENSG00000079215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079215)

## Data

Gene col 1244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1244); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1244]; `tensor/DDL_lfc|DDL_z.npy` [1244]; `embed/gene_vectors.npy` [1244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1244 or target_col == 1244). Every well: [[SLC1A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC1A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
