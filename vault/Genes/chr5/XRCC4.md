---
symbol: "XRCC4"
type: "gene"
col: 7625
ensembl_id: "ENSG00000152422"
name: "X-ray repair cross complementing 4"
location: "5q14.2"
module: 7
arm: "+"
pooled_cpm: 97.58
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# XRCC4

*X-ray repair cross complementing 4* — 5q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.57× (z +12.9, q 3e-35, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.700× (z -9.7, q 1e-19, down in 26 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.749× (z -8.2, q 5e-14, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTN-AS1]] (+0.59, fdr 3e-05), [[DNTTIP2]] (+0.56, fdr 1e-05), [[NSMCE2]] (+0.54, fdr 2e-05); moves opposite to [[RNF138]] (-0.53, fdr 1e-05), [[SNX30]] (-0.49, fdr 3e-05), [[SLC25A23]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +12.9 | 3e-35 | 33/48 (LoVo, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +8.9 | 2e-16 | 29/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +8.8 | 3e-16 | 32/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +6.7 | 3e-09 | 17/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +6.2 | 8e-08 | 26/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +5.6 | 2e-06 | 24/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.13 | 3/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.08× | +3.1 | 0.13 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7625.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.700×** | -9.7 | 1e-19 | 26/44 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -8.8 | 5e-16 | 33/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.749×** | -8.2 | 5e-14 | 28/48 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.741×** | -8.0 | 2e-13 | 29/49 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -7.7 | 1e-12 | 25/49 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.610×** | -7.3 | 2e-11 | 30/48 (LS 180, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.783×** | -6.9 | 3e-10 | 24/48 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.786×** | -6.8 | 6e-10 | 30/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.792×** | -6.6 | 3e-09 | 26/48 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.788×** | -6.5 | 4e-09 | 27/47 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -5.5 | 2e-06 | 24/50 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.878× | -5.2 | 9e-06 | 9/48 (NCI-H2030, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | **0.820×** | -5.2 | 9e-06 | 23/45 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -4.5 | 3e-04 | 15/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.747×** | -4.3 | 6e-04 | 19/49 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.856× | -4.2 | 0.001 | 13/48 (A549, NCI-H2030, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.867× | -4.1 | 0.002 | 13/49 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.915× | -3.5 | 0.011 | 5/48 (HS-578T, A-427, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.806×** | -3.2 | 0.033 | 11/48 (SW 900, A-427, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 106 | 8 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.11× (z +23.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.0759× (z -32.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 134 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +41.3) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.98× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 146 | 3 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +47.6) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.409× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 144 | 4 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +33.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.73× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -10.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.531× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.408× (z -14.4) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 0.641× (z -10.5) |
| [[LoVo (line)]] | wt | 88.4 | 2 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.41× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 120 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +27.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.08× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[LS 180 (line)]] | wt | 126 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.90× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.9) |
| [[PANC-1 (line)]] | alt | 110 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.484× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.607× (z -8.9) |
| [[C32 (line)]] | wt | 88.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -18.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.73× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -14.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[J82 (line)]] | alt | 80.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -16.3) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LOX-IMVI (line)]] | wt | 162 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.9) ⚠ cell-cycle shift, explains ~66% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 82.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +18.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.27× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 107 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 121 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -10.4) |
| [[A498 (line)]] | wt | 97.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.6) |
| [[HT-29 (line)]] | alt | 90.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.25× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -10.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 61.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[RKO (line)]] | wt | 111 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +22.7) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 2 | — | [[Drospirenone (drug)]] 0.5 µM 0.0734× (z -10.8) |
| [[SW 1271 (line)]] | alt | 140 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.155× (z -10.0) |
| [[SW 900 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -12.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SW480 (line)]] | alt | 129 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.82× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.586× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -9.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[BT-474 (line)]] | alt | 25.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.249× (z -9.0) |
| [[H4 (line)]] | wt | 94.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HCT15 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.6) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HOP62 (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.463× (z -8.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.478× (z -10.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -8.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Panc 03.27 (line)]] | alt | 87.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.26× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 80.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -12.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SHP-77 (line)]] | alt | 85.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.16× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 72.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 55.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +8.5) | — |
| [[A-172 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTN-AS1]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[DNTTIP2]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NSMCE2]] | +0.54 | +0.46 / +0.61 | both halves | 2e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[RPTOR]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[FAF2]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SLC38A6]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[POP4]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SETX]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[UTP11]] | +0.52 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ALOX12P2-1]] | +0.52 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[IFT43]] | +0.52 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CWF19L2]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF138]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SNX30]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SLC25A23]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TRIM36]] | -0.47 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ACO1]] | -0.47 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[RTN4R]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SLC25A30]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PAIP2B]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[LONRF1]] | -0.46 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SSBP4]] | -0.45 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[FAM76A]] | -0.45 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[HABP4]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers XRCC4's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.388). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-42.0, 1.8); signed map (-4.1, -23.1). **Vector** length 113, 29.0% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.6 | +8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +8.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.4 | +2.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | X-ray repair cross complementing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.2 — chr5:83,077,498-83,353,787 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hXRCC4 |
| Reactome | 12 pathways, smallest: 2-LTR circle formation; Integration of provirus; Early Phase of HIV Life Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13426](https://www.uniprot.org/uniprotkb/Q13426) (DNA repair protein XRCC4):

> [DNA repair protein XRCC4]: DNA non-homologous end joining (NHEJ) core factor, required for double-strand break repair and V(D)J recombination. Acts as a scaffold protein that regulates recruitment of other proteins to DNA double-strand breaks (DSBs). Associates with NHEJ1/XLF to form alternating helical filaments that bridge DNA and act like a bandage, holding together the broken DNA until it is repaired. The XRCC4-NHEJ1/XLF subcomplex binds to the DNA fragments of a DSB in a highly diffusive …

**Summary**, from NCBI Gene [7518](https://www.ncbi.nlm.nih.gov/gene/7518):

> The protein encoded by this gene functions together with DNA ligase IV and the DNA-dependent protein kinase in the repair of DNA double-strand breaks. This protein plays a role in both non-homologous end joining and the completion of V(D)J recombination. Mutations in this gene can cause short stature, microcephaly, and endocrine dysfunction (SSMED). Alternate transcript variants such as NM_022406 are unlikely to be expressed in some individuals due to a polymorphism (rs1805377) in the last …

**Accessions** — [HGNC:12831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12831) · Entrez [7518](https://www.ncbi.nlm.nih.gov/gene/7518) · UniProt [Q13426](https://www.uniprot.org/uniprotkb/Q13426) · Ensembl [ENSG00000152422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152422)

## Data

Gene col 7625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7625); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7625]; `tensor/DDL_lfc|DDL_z.npy` [7625]; `embed/gene_vectors.npy` [7625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7625 or target_col == 7625). Every well: [[XRCC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRCC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
