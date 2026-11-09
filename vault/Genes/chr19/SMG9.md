---
symbol: "SMG9"
type: "gene"
col: 2663
ensembl_id: "ENSG00000105771"
name: "SMG9 nonsense mediated mRNA decay factor"
location: "19q13.31"
module: 29
arm: "-"
pooled_cpm: 31.2
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SMG9

*SMG9 nonsense mediated mRNA decay factor* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.57× (z +8.2, q 1e-13, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A549 3.50×, PANC-1 2.81×, A-172 3.09×, A498 2.45×, …; ⚠ cell-cycle shift, explains ~68% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A498 3.19×, A549 3.03×, PANC-1 2.41×, A-172 2.75×; ⚠ cell-cycle shift, explains ~24% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 3.50×, A-172 4.15×, A549 3.73×, NCI-H460 2.51×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -17.9, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGXB4]] (+0.56, fdr 1e-04), [[ORAI1]] (+0.55, fdr 4e-05), [[TRAF2]] (+0.54, fdr 2e-05); moves opposite to [[SLC39A6]] (-0.60, fdr 6e-05), [[LAPTM4A]] (-0.58, fdr 5e-05), [[DDOST]] (-0.55, fdr 7e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BRSK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2663.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A549 3.50×, PANC-1 2.81×, A-172 3.09×, A498 2.45×, …; ⚠ cell-cycle shift, explains ~68% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A498 3.19×, A549 3.03×, PANC-1 2.41×, A-172 2.75×; ⚠ cell-cycle shift, explains ~24% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (PANC-1 3.50×, A-172 4.15×, A549 3.73×, NCI-H460 2.51×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +8.2 | 1e-13 | 30/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.17× | +4.7 | 7e-04 | 21/47 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +4.6 | 7e-04 | 21/47 (A498, A549, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.8 | 0.024 | 12/40 (SW 900, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.080 | 9/48 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.20× | +3.3 | 0.099 | 2/48 (HS-578T, A-427) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.16× | +3.0 | 0.18 | 14/48 (A-172, A549, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.18 | 14/47 (A-427, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -17.9 | 0e+00 | 44/47 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.492×** | -14.7 | 0e+00 | 43/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.522×** | -13.5 | 4e-39 | 43/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.526×** | -13.3 | 2e-38 | 39/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.541×** | -12.7 | 5e-35 | 31/45 (A-172, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.554×** | -11.3 | 8e-28 | 30/42 (MIA PaCa-2, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.717×** | -9.7 | 2e-20 | 34/48 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -9.3 | 1e-18 | 24/37 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -8.7 | 2e-16 | 33/47 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -8.1 | 5e-14 | 28/48 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -8.0 | 7e-14 | 31/47 (NCI-H460, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.683×** | -7.9 | 1e-13 | 33/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.698×** | -7.5 | 4e-12 | 31/47 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.758×** | -5.7 | 4e-07 | 22/48 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.627×** | -4.8 | 8e-05 | 24/48 (A498, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.785×** | -4.4 | 4e-04 | 17/47 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.845× | -4.2 | 7e-04 | 15/48 (C32, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.855× | -4.0 | 0.002 | 17/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.4 | 0.020 | 13/48 (A-172, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 37.3 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.15× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -13.4) |
| [[A549 (line)]] | wt | 34.5 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +15.9) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.73× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.5) |
| [[A498 (line)]] | wt | 27.9 | 2 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.0) ⚠ cell-cycle shift, explains ~68% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -12.1) |
| [[HOP62 (line)]] | alt | 48.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 42.1 | 0 | 5 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.600× (z -15.8) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 33.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 25.9 | 2 (1 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.51× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.7) |
| [[PANC-1 (line)]] | alt | 26.8 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +15.7) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.50× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.367× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 39.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -10.7) |
| [[RKO (line)]] | wt | 62.9 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.3) |
| [[A-427 (line)]] | wt | 42.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -13.9) |
| [[J82 (line)]] | alt | 27.5 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.5) ⚠ cell-cycle shift, explains ~68% of this change | [[Selinexor (drug)]] 5 µM 0.273× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 33.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -11.2) |
| [[C32 (line)]] | wt | 39.7 | 0 | 2 | — | [[Binimetinib (drug)]] 5 µM 0.273× (z -8.5) |
| [[H4 (line)]] | wt | 52.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -13.0) |
| [[HCT15 (line)]] | alt | 60.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.0840× (z -9.3) |
| [[HS-578T (line)]] | alt | 48.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -14.9) |
| [[SW48 (line)]] | wt | 31.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.2) |
| [[SW480 (line)]] | alt | 34.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.482× (z -8.9) |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0665× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -11.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.329× (z -10.4) |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -14.7) |
| [[SNU-423 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGXB4]] | +0.56 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[ORAI1]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TRAF2]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[FBXL6]] | +0.53 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[IKBKB]] | +0.53 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[POC5]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PRR7]] | +0.52 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[THG1L]] | +0.51 | +0.28 / +0.58 | both halves | 3e-04 |  |
| [[EXOC6]] | +0.51 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[UQCC2]] | +0.51 | +0.43 / +0.47 | both halves | 4e-05 |  |
| [[NT5C]] | +0.50 | +0.26 / +0.54 | both halves | 3e-04 |  |
| [[CEP295]] | +0.50 | +0.37 / +0.51 | both halves | 8e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A6]] | -0.60 | -0.38 / -0.66 | both halves | 6e-05 |  |
| [[LAPTM4A]] | -0.58 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[DDOST]] | -0.55 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[TMEM30A]] | -0.55 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[LAMP2]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[REEP5]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[OS9]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[VDAC2]] | -0.52 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[ILRUN]] | -0.51 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[SNX3]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ATP6AP2]] | -0.51 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[PDIA3]] | -0.51 | -0.36 / -0.51 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK1]] | B | BRSK1 activity raises SMG9's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without BRSK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[FJX1]] | B | FJX1 activity raises SMG9's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.23× lower at baseline in the lines without FJX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[BRSK1]] | B | BRSK1 activity strengthens SMG9's drug response | lines that do not express BRSK1 (13) vs lines expressing it (35) | the lines without BRSK1 respond 0.68× as strongly (z diff +1.82); strongest at Dinaciclib 0.5 µM: 0.71x vs 0.50x (z diff +3.2) | 0.092 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-18.8, -18.1); signed map (-0.4, -8.7). **Vector** length 92.3, 20.8% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.6 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +7.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.8 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.5 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +1.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.4 | -9.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.1 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -17.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | SMG9 nonsense mediated mRNA decay factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,727,983-43,754,962 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12886; previously C19orf61 |
| Gene groups (HGNC) | SMG1 complex |
| Reactome | 3 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0W8](https://www.uniprot.org/uniprotkb/Q9H0W8) (Nonsense-mediated mRNA decay factor SMG9):

> Involved in nonsense-mediated decay (NMD) of mRNAs containing premature stop codons. Is recruited by release factors to stalled ribosomes together with SMG1 and SMG8 (forming the SMG1C protein kinase complex) and, in the SMG1C complex, is required for the efficient association between SMG1 and SMG8. Plays a role in brain, heart, and eye development (By similarity).

**Summary**, from NCBI Gene [56006](https://www.ncbi.nlm.nih.gov/gene/56006):

> This gene encodes a regulatory subunit of the SMG1 complex, which plays a critical role in nonsense-mediated mRNA decay (NMD). Binding of the encoded protein to the SMG1 complex kinase scaffold protein results in the inhibition of its kinase activity. Mutations in this gene cause a multiple congenital anomaly syndrome in human patients, characterized by brain malformation, congenital heart disease and other features. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:25763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25763) · Entrez [56006](https://www.ncbi.nlm.nih.gov/gene/56006) · UniProt [Q9H0W8](https://www.uniprot.org/uniprotkb/Q9H0W8) · Ensembl [ENSG00000105771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105771)

## Data

Gene col 2663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2663); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2663]; `tensor/DDL_lfc|DDL_z.npy` [2663]; `embed/gene_vectors.npy` [2663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2663 or target_col == 2663). Every well: [[SMG9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
