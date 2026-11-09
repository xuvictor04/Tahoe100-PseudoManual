---
symbol: "TEP1"
type: "gene"
col: 4989
ensembl_id: "ENSG00000129566"
name: "telomerase associated protein 1"
location: "14q11.2"
module: 101
arm: "+"
pooled_cpm: 39.37
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# TEP1

*telomerase associated protein 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.34× (z +4.4, q 0.008, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 2.50×, NCI-H460 2.56×, C32 2.51×, LS 180 2.18×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 2.80×, NCI-H2030 2.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 2.76×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.515× (z -10.0, q 9e-21, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AEN]] (+0.58, fdr 1e-05), [[EPHA2]] (+0.57, fdr 1e-05), [[ITGA2-AS1]] (+0.56, fdr 1e-05); moves opposite to [[MAP2K6]] (-0.51, fdr 5e-05), [[KIF13A]] (-0.49, fdr 6e-05), [[MID1]] (-0.49, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LACC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4989.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 2.50×, NCI-H460 2.56×, C32 2.51×, LS 180 2.18×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 2.80×, NCI-H2030 2.56×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 2.76×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 0.008 | 23/47 (NCI-H2030, HOP62, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.26× | +3.3 | 0.19 | 19/47 (NCI-H2030, RPMI-7951, …) | two highest doses |  |
| [[Cytarabine (drug)]] 5 µM |  | 1.26× | +3.3 | 0.19 | 17/48 (LS 180, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.515×** | -10.0 | 9e-21 | 42/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -9.5 | 4e-19 | 42/48 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.623×** | -7.1 | 2e-10 | 38/48 (HT-29, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -6.3 | 4e-08 | 32/48 (C32, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.706×** | -5.3 | 2e-05 | 26/48 (Panc 03.27, SK-MEL-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.710×** | -5.2 | 2e-05 | 24/48 (SW 1271, J82, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.719×** | -4.8 | 1e-04 | 26/46 (SK-MEL-2, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -4.3 | 0.001 | 21/47 (hTERT-HPNE, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.761×** | -4.1 | 0.002 | 22/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.773×** | -3.9 | 0.006 | 18/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.766×** | -3.9 | 0.006 | 22/48 (SW 1088, KATO III, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.635×** | -3.6 | 0.016 | 22/49 (PANC-1, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.790×** | -3.6 | 0.016 | 20/48 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.643×** | -3.5 | 0.019 | 20/47 (H4, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Aliskiren (drug)]] 0.5 µM |  | **0.794×** | -3.5 | 0.019 | 22/49 (CHP-212, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.025 | 23/49 (NCI-H1573, C32, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.662×** | -3.3 | 0.035 | 16/48 (Hs 766T, A549, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.051 | 20/48 (NCI-H23, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.060 | 18/47 (NCI-H1573, C32, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.812×** | -3.0 | 0.077 | 16/48 (HCT15, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 33.8 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.254× (z -9.7) |
| [[HT-29 (line)]] | alt | 42.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -12.1) |
| [[J82 (line)]] | alt | 21.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -8.6) |
| [[LS 180 (line)]] | wt | 67.8 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -10.1) |
| [[BT-474 (line)]] | alt | 70.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -10.3) |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.142× (z -9.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.297× (z -8.6) |
| [[KATO III (line)]] | alt | 25.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -9.8) |
| [[LoVo (line)]] | wt | 53.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 77.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 34.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 46.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0431× (z -26.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.310× (z -9.8) |
| [[A498 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 38.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 64.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -8.6) |
| [[PANC-1 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 29.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.66× (z +8.6) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.241× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[SW 1271 (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0731× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.333× (z -8.7) ⚠ toxic |
| [[SW480 (line)]] | alt | 28.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.380× (z -8.7) |
| [[A-172 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AEN]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.57 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ITGA2-AS1]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[KHNYN]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GMIP]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NOP14-AS1]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[RHBDF1]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[BTBD10]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[TRIM8]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SLC12A4]] | +0.51 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZNF641]] | +0.51 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[TAF12]] | +0.51 | +0.48 / +0.35 | both halves | 1e-04 | STRING 926 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K6]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[KIF13A]] | -0.49 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[MID1]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[C1QTNF3-AMACR]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CDKAL1]] | -0.48 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[TTLL5]] | -0.47 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PPP1CC]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[LRBA]] | -0.46 | -0.39 / -0.39 | both halves | 5e-05 | same gene group |
| [[DYNC2H1]] | -0.45 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[SLC5A4-AS1]] | -0.45 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[PPP1R12B]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[LDHB]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity raises TEP1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without LACC1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises TEP1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.24× lower at baseline in the lines without SLC5A4-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.5, 34.5); signed map (-2.6, 32.1). **Vector** length 96.9, 23.4% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.0 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +1.7 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -10.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | telomerase associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,365,667-20,413,501 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TP1, TLP1, VAULT2, p240, TROVE1 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99973](https://www.uniprot.org/uniprotkb/Q99973) (Telomerase protein component 1):

> Component of the telomerase ribonucleoprotein complex that is essential for the replication of chromosome termini. Component of the vault particle, which is a massive ribonucleoprotein complex that may play a role in cargo transport and signal transduction (By similarity). Responsible for the localizing and stabilizing vault RNA (vRNA) association in the vault ribonucleoprotein particle. Binds to TERC (By similarity).

**Summary**, from NCBI Gene [7011](https://www.ncbi.nlm.nih.gov/gene/7011):

> This gene product is a component of the ribonucleoprotein complex responsible for telomerase activity which catalyzes the addition of new telomeres on the chromosome ends. The telomerase-associated proteins are conserved from ciliates to humans. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:11726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11726) · Entrez [7011](https://www.ncbi.nlm.nih.gov/gene/7011) · UniProt [Q99973](https://www.uniprot.org/uniprotkb/Q99973) · Ensembl [ENSG00000129566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129566)

## Data

Gene col 4989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4989); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4989]; `tensor/DDL_lfc|DDL_z.npy` [4989]; `embed/gene_vectors.npy` [4989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4989 or target_col == 4989). Every well: [[TEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
