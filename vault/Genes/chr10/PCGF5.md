---
symbol: "PCGF5"
type: "gene"
col: 11121
ensembl_id: "ENSG00000180628"
name: "polycomb group ring finger 5"
location: "10q23.32"
module: 29
arm: "+"
pooled_cpm: 104.78
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PCGF5

*polycomb group ring finger 5* — 10q23.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 1.22× (z +4.2, q 0.018, up in 20 of 50 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 1.40× (z +3.7, q 0.061, up in 21 of 50 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 2.46×); [[Harringtonine (drug)]] 0.5 µM in 1 line (PANC-1 2.28×; ⚠ cell-cycle shift, explains ~0% of this change); [[NG25 (drug)]] 5 µM in 1 line (A549 3.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 1.95×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.530× (z -13.2, q 7e-37, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.721× (z -9.1, q 9e-18, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRADB]] (+0.64, fdr 1e-05), [[CHPT1]] (+0.58, fdr 1e-05), [[SETD7]] (+0.56, fdr 5e-05); moves opposite to [[ADAM8]] (-0.52, fdr 5e-05), [[ATAT1]] (-0.52, fdr 7e-05), [[PRDM8]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARL4C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 2.46×); [[Harringtonine (drug)]] 0.5 µM in 1 line (PANC-1 2.28×; ⚠ cell-cycle shift, explains ~0% of this change); [[NG25 (drug)]] 5 µM in 1 line (A549 3.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 1.95×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +4.2 | 0.018 | 20/50 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.061 | 21/50 (NCI-H1573, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.082 | 15/48 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.3 | 0.12 | 17/49 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.12 | 16/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.12× | +3.2 | 0.12 | 4/48 (SW 900, NCI-H460, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.2 | 0.12 | 9/48 (NCI-H2347, A498, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.17 | 3/48 (NCI-H2030, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.530×** | -13.2 | 7e-37 | 40/48 (RKO, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.548×** | -12.5 | 2e-33 | 42/48 (A549, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.562×** | -12.0 | 1e-30 | 42/48 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.721×** | -9.1 | 9e-18 | 31/48 (NCI-H1792, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.673×** | -7.9 | 4e-13 | 29/48 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.760×** | -5.5 | 5e-06 | 34/47 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.797×** | -4.7 | 2e-04 | 25/48 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.4 | 6e-04 | 2/50 (SW 1088, CHP-212) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.855× | -4.3 | 9e-04 | 8/48 (RPMI-7951, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.816×** | -4.2 | 0.001 | 23/48 (A549, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.808×** | -4.1 | 0.003 | 21/45 (RKO, SNU-1, …) | inconsistent across doses | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.709×** | -3.7 | 0.009 | 23/47 (SW 900, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -3.4 | 0.029 | 21/45 (HCT15, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.051 | 15/49 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.891× | -3.2 | 0.056 | 13/48 (SNU-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.065 | 10/48 (HS-578T, SHP-77, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.071 | 13/48 (A-427, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.857× | -3.0 | 0.083 | 14/48 (PANC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 185 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.8) |
| [[A549 (line)]] | wt | 159 | 1 (1 ⚠) | 5 (5 ⚠) | [[NG25 (drug)]] 5 µM 3.16× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -16.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 166 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 286 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.333× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -20.8) |
| [[SNU-1 (line)]] | wt | 205 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[C32 (line)]] | wt | 133 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 90.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -13.9) |
| [[HS-578T (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.3) |
| [[LoVo (line)]] | wt | 146 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.470× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.604× (z -8.5) |
| [[SW480 (line)]] | alt | 80.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.473× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 65.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 105 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 34.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 95.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.489× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 138 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 205 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.468× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 86.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.95× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.182× (z -8.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 85.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -16.2) |
| [[PANC-1 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.28× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SW48 (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRADB]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CHPT1]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SETD7]] | +0.56 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[TRAM1]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[UBE2Q2]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ABCB10]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DUSP22]] | +0.53 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PM20D2]] | +0.52 | +0.26 / +0.52 | both halves | 4e-04 |  |
| [[MID2]] | +0.51 | +0.51 / +0.46 | both halves | 3e-05 | same gene group |
| [[TMEM38B]] | +0.51 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[SCARB2]] | +0.51 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM8]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ATAT1]] | -0.52 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[PRDM8]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[IER2]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SLC25A51]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[NME7]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[IFT88]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DNTTIP1]] | -0.49 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DUSP6]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[RIN1]] | -0.47 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[SRSF9]] ⚠ | -0.47 | -0.46 / -0.39 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KCNN4]] | -0.47 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ENDOV]] | -0.47 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL4C]] | B | ARL4C activity raises PCGF5's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 1.37× lower at baseline in the lines without ARL4C | 0.042 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[C11orf91]] | B | C11orf91 activity raises PCGF5's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without C11orf91 | 0.094 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-12.0, 15.0); signed map (-20.0, -28.3). **Vector** length 121, 34.7% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.4 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.9 | +3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.5 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.2 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +4.0 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -9.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.7 | -2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +0.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | polycomb group ring finger 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.32 — chr10:91,163,012-91,284,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16202; previously RNF159 |
| Gene groups (HGNC) | Ring finger proteins; Polycomb group ring fingers |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 2 pathways, smallest: RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SE9](https://www.uniprot.org/uniprotkb/Q86SE9) (Polycomb group RING finger protein 5):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Within the PRC1-like complex, regulates RNF2 ubiquitin ligase activity. Plays a redundant role with …

**Summary**, from NCBI Gene [84333](https://www.ncbi.nlm.nih.gov/gene/84333):

> Predicted to enable histone H2AK119 ubiquitin ligase activity. Acts upstream of or within positive regulation of transcription by RNA polymerase II. Located in centrosome and nucleoplasm. Part of PcG protein complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28264) · Entrez [84333](https://www.ncbi.nlm.nih.gov/gene/84333) · UniProt [Q86SE9](https://www.uniprot.org/uniprotkb/Q86SE9) · Ensembl [ENSG00000180628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180628)

## Data

Gene col 11121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11121); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11121]; `tensor/DDL_lfc|DDL_z.npy` [11121]; `embed/gene_vectors.npy` [11121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11121 or target_col == 11121). Every well: [[PCGF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCGF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
