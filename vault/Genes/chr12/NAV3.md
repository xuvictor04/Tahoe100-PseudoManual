---
symbol: "NAV3"
type: "gene"
col: 869
ensembl_id: "ENSG00000067798"
name: "neuron navigator 3"
location: "12q21.2"
module: 116
arm: "+"
pooled_cpm: 119.43
n_lines_expressing: 34
n_dd_up: 48
n_dd_down: 52
n_dd_up_clean: 34
n_dd_down_clean: 48
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# NAV3

*neuron navigator 3* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.55× (z +25.2, q 0e+00, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 52 drug-doses (4 with an alert ⚠); the strongest is [[Triamcinolone (drug)]] 5 µM: 0.686× (z -7.5, q 4e-11, down in 21 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADTRP]] (+0.78, fdr 7e-06), [[MARCHF4]] (+0.73, fdr 7e-06), [[ITGB1-DT]] (+0.71, fdr 7e-06); moves opposite to [[TSC22D3]] (-0.54, fdr 1e-05), [[PACSIN2]] (-0.53, fdr 2e-05), [[MED25]] (-0.51, fdr 1e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GLIPR1]] → it (grade B ⚠); 14 go from it, the strongest it → [[LINC01151]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 869.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.55×** | +25.2 | 0e+00 | 27/32 (hTERT-HPNE, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.49×** | +21.2 | 0e+00 | 29/32 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.11×** | +19.2 | 0e+00 | 26/32 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.64×** | +13.7 | 2e-40 | 24/32 (A-172, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.71×** | +12.3 | 2e-32 | 22/32 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.24×** | +11.4 | 6e-28 | 24/32 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +9.0 | 2e-17 | 21/32 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.88×** | +8.9 | 4e-17 | 24/31 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.30×** | +8.6 | 5e-16 | 22/33 (A549, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.87×** | +8.5 | 1e-15 | 22/31 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.72×** | +7.6 | 1e-12 | 23/32 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.64×** | +6.5 | 5e-09 | 18/29 (NCI-H460, A549, …) | all doses, flat | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.61×** | +5.9 | 2e-07 | 21/31 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.8 | 2e-07 | 19/32 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +5.8 | 3e-07 | 16/25 (A549, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +5.3 | 3e-06 | 17/33 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.2 | 7e-06 | 16/32 (A498, Hs 766T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 1e-05 | 16/32 (A498, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 1e-05 | 14/33 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.86×** | +4.5 | 2e-04 | 17/32 (A549, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 4 with an alert ⚠; shown: the 15 strongest. 52 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 869.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 5 µM |  | **0.686×** | -7.5 | 4e-11 | 21/32 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.607×** | -7.0 | 7e-10 | 20/32 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.615×** | -6.8 | 2e-09 | 20/32 (A549, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.675×** | -6.3 | 4e-08 | 19/32 (RKO, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.620×** | -6.2 | 7e-08 | 16/32 (RKO, NCI-H23, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.607×** | -6.1 | 8e-08 | 19/32 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.647×** | -6.1 | 8e-08 | 22/33 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.648×** | -6.1 | 8e-08 | 20/32 (A549, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.638×** | -6.1 | 8e-08 | 19/33 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.649×** | -6.1 | 8e-08 | 21/32 (RKO, A-427, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.653×** | -6.0 | 1e-07 | 19/32 (A549, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.655×** | -5.9 | 2e-07 | 16/34 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.699×** | -5.8 | 2e-07 | 18/32 (RKO, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.668×** | -5.7 | 6e-07 | 19/32 (RKO, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.674×** | -5.5 | 1e-06 | 17/32 (A549, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 1,905 | 0 | 33 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0483× (z -34.8) |
| [[A549 (line)]] | wt | 154 | 7 (1 ⚠) | 18 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +26.7) | [[Betamethasone dipropionate (drug)]] 5 µM 0.221× (z -13.6) |
| [[HOP62 (line)]] | alt | 163 | 5 (1 ⚠) | 14 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +14.0) | [[Adagrasib (drug)]] 0.05 µM 0.436× (z -22.8) ⚠ position not correctable · without an alert: [[Budesonide (drug)]] 0.05 µM 0.218× (z -12.2) |
| [[A-427 (line)]] | wt | 187 | 3 | 12 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +10.2) | [[Trametinib (drug)]] 5 µM 0.168× (z -16.2) |
| [[A498 (line)]] | wt | 136 | 5 | 9 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +23.6) | [[Clobetasol propionate (drug)]] 0.5 µM 0.283× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 81.1 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 8.42× (z +18.3) | — |
| [[A-172 (line)]] | wt | 108 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +23.7) | — |
| [[NCI-H2030 (line)]] | alt | 355 | 2 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.7) | [[Adagrasib (drug)]] 0.05 µM 0.436× (z -22.6) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 84.1 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +22.6) | [[Adagrasib (drug)]] 0.05 µM 0.383× (z -23.0) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.235× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 97.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +30.0) | — |
| [[H4 (line)]] | wt | 348 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 369 | 3 (3 ⚠) | 3 | [[Digitoxin (drug)]] 0.5 µM 3.65× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -10.9) |
| [[LS 180 (line)]] | wt | 67.5 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.82× (z +17.6) | — |
| [[NCI-H1792 (line)]] | alt | 157 | 4 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 17.1× (z +19.9) | [[Adagrasib (drug)]] 0.05 µM 0.533× (z -15.9) ⚠ position not correctable · without an alert: [[Retinoic acid (drug)]] 5 µM 0.408× (z -9.3) |
| [[SW 900 (line)]] | alt | 34.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 13.4× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 116 | 2 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.02× (z +9.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 3.98× (z +9.8) | [[Trametinib (drug)]] 5 µM 0.252× (z -9.8) |
| [[HS-578T (line)]] | alt | 150 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +17.1) | [[Trametinib (drug)]] 5 µM 0.261× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 55.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +19.3) | — |
| [[NCI-H1573 (line)]] | alt | 47.7 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.82× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 54.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +25.6) | — |
| [[J82 (line)]] | alt | 73.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.8) | [[Selinexor (drug)]] 5 µM 0.373× (z -9.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2347 (line)]] | alt | 30.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +14.1) | — |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.57× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 115 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.50× (z +10.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -9.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.8) |
| [[SW48 (line)]] | wt | 33.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +15.1) | — |
| [[C32 (line)]] | wt | 506 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 31.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.07× (z +13.4) | — |
| [[Hs 766T (line)]] | wt | 55.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.96× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 195 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 28.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADTRP]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[MARCHF4]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[FRMD6]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[AJAP1]] | +0.70 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[FGF5]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CXCL8]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CREB5]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LINC00707]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PACSIN2]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MED25]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.51 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ABHD12]] | -0.51 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[SSBP2]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIPR1]] | B | GLIPR1 activity raises NAV3's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 4.12× lower at baseline in the lines without GLIPR1 | 0.019 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[FRMD4A]] | B | FRMD4A activity raises NAV3's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.76× lower at baseline in the lines without FRMD4A | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[BCL2A1]] | B | BCL2A1 activity raises NAV3's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 3.63× lower at baseline in the lines without BCL2A1 | 0.040 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[CCDC190]] | B | CCDC190 activity raises NAV3's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 2.57× lower at baseline in the lines without CCDC190 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[XKR6]] | B | XKR6 activity raises NAV3's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without XKR6 | 0.050 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |
| [[ROBO4]] | B | ROBO4 activity raises NAV3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.35× lower at baseline in the lines without ROBO4 | 0.055 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[SFTA1P]] | B | SFTA1P activity raises NAV3's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.01× lower at baseline in the lines without SFTA1P | 0.085 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[FRMD6]] | C | FRMD6 activity raises NAV3's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 4.92× lower at baseline in the lines without FRMD6 | 0.005 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises NAV3's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 4.04× lower at baseline in the lines without LNCOG | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[ADAMTS1]] | C | ADAMTS1 activity raises NAV3's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 3.10× lower at baseline in the lines without ADAMTS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |
| [[LAMA1]] | C | LAMA1 activity raises NAV3's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 4.22× lower at baseline in the lines without LAMA1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01151]] | B | NAV3 activity raises LINC01151's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without NAV3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[ABL2]] | B | NAV3 activity raises ABL2's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without NAV3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[RPSAP52]] | B | NAV3 activity raises RPSAP52's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without NAV3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[CD44]] | B | NAV3 activity raises CD44's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.57× lower at baseline in the lines without NAV3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[ADAMTS16]] | B | NAV3 activity raises ADAMTS16's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.07× lower at baseline in the lines without NAV3 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[MAMLD1]] | B | NAV3 activity raises MAMLD1's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without NAV3 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[ETS1]] | B | NAV3 activity raises ETS1's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without NAV3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| cells under [[Tucatinib (drug)]] 5 µM | B | NAV3 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express NAV3 (16) vs lines expressing it (32) | the lines without NAV3: 0.82× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[MSANTD3]] | B | NAV3 activity raises MSANTD3's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without NAV3 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| cells under [[Amsacrine (drug)]] 5 µM | B | NAV3 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express NAV3 (16) vs lines expressing it (32) | the lines without NAV3: 1.17× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[ARHGAP31]] | B | NAV3 activity raises ARHGAP31's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.18× lower at baseline in the lines without NAV3 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| cells under [[Carbamazepine (drug)]] 0.5 µM | B | NAV3 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express NAV3 (16) vs lines expressing it (32) | the lines without NAV3: 1.15× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.9, 11.5); signed map (14.6, 44.1). **Vector** length 145, 46.7% of its response variance represented; |z| ≥ 3 in 1,659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.1 | +21.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +25.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +19.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +13.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.1 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.8 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -5.4 | -7.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -5.2 | -7.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.0 | -4.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -4.9 | -6.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.8 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | neuron navigator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:77,324,641-78,213,010 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0938, POMFIL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVL0](https://www.uniprot.org/uniprotkb/Q8IVL0) (Neuron navigator 3):

> Is involved in microtubule cytoskeleton organization and plays a role in cell migration.

**Summary**, from NCBI Gene [89795](https://www.ncbi.nlm.nih.gov/gene/89795):

> This gene belongs to the neuron navigator family and is expressed predominantly in the nervous system. The encoded protein contains coiled-coil domains and a conserved AAA domain characteristic for ATPases associated with a variety of cellular activities. This gene is similar to unc-53, a Caenorhabditis elegans gene involved in axon guidance. Multiple alternatively spliced transcript variants for this gene have been described but only one has had its full-length nature determined. [provided by …

**Accessions** — [HGNC:15998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15998) · Entrez [89795](https://www.ncbi.nlm.nih.gov/gene/89795) · UniProt [Q8IVL0](https://www.uniprot.org/uniprotkb/Q8IVL0) · Ensembl [ENSG00000067798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067798)

## Data

Gene col 869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 869); `tables/drug_effects.parquet` (104 rows, flagged included); `relations/gene_relations.parquet` (col_a == 869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 869]; `tensor/DDL_lfc|DDL_z.npy` [869]; `embed/gene_vectors.npy` [869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 869 or target_col == 869). Every well: [[NAV3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAV3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
