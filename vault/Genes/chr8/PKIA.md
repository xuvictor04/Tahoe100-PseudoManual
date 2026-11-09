---
symbol: "PKIA"
type: "gene"
col: 10041
ensembl_id: "ENSG00000171033"
name: "cAMP-dependent protein kinase inhibitor alpha"
location: "8q21.13"
module: 81
arm: "+"
pooled_cpm: 32.56
n_lines_expressing: 28
n_dd_up: 22
n_dd_down: 41
n_dd_up_clean: 14
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 14
direction_downstream: 14
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# PKIA

*cAMP-dependent protein kinase inhibitor alpha* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.51× (z +26.1, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (4 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.623× (z -8.2, q 2e-13, down in 17 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2A1]] (+0.72, fdr 7e-06), [[WSCD1]] (+0.69, fdr 1e-05), [[WNT7B]] (+0.69, fdr 7e-06); moves opposite to [[ADGRG2]] (-0.58, fdr 3e-05), [[NNMT]] (-0.57, fdr 2e-05), [[KLF9]] (-0.56, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TSPAN5]] → it (grade B ⚠); 14 go from it, the strongest it → [[IL33]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.51×** | +26.1 | 0e+00 | 26/26 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.43×** | +25.8 | 0e+00 | 26/26 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +24.0 | 0e+00 | 25/26 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.80×** | +23.1 | 0e+00 | 25/26 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.67×** | +17.0 | 0e+00 | 25/26 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +14.7 | 0e+00 | 24/25 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.67×** | +8.5 | 1e-15 | 13/25 (J82, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.90×** | +6.8 | 9e-10 | 19/26 (A498, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +6.3 | 2e-08 | 15/25 (A498, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 3e-07 | 14/26 (A498, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **1.39×** | +5.3 | 5e-06 | 9/25 (NCI-H1792, A-427, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.32×** | +4.8 | 7e-05 | 13/26 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 2e-04 | 10/26 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +4.2 | 9e-04 | 10/25 (LS 180, HS-578T, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +4.2 | 9e-04 | 13/26 (J82, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 10/25 (LS 180, A498, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 12/26 (A498, HOP62, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +3.6 | 0.011 | 7/25 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.011 | 7/26 (NCI-H2347, Hs 766T, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.041 | 8/25 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.050 | 8/26 (LS 180, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.623×** | -8.2 | 2e-13 | 17/26 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.631×** | -7.9 | 5e-13 | 18/26 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.639×** | -7.7 | 2e-12 | 19/25 (HOP62, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.649×** | -7.5 | 1e-11 | 18/25 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.653×** | -7.3 | 2e-11 | 19/25 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.741×** | -7.3 | 2e-11 | 20/26 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.659×** | -7.2 | 5e-11 | 16/25 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.638×** | -7.2 | 5e-11 | 17/25 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.670×** | -6.9 | 3e-10 | 19/25 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.889× | -6.9 | 3e-10 | 6/26 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.680×** | -6.7 | 1e-09 | 18/25 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.614×** | -6.6 | 2e-09 | 16/26 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.687×** | -6.5 | 4e-09 | 19/26 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -6.4 | 5e-09 | 17/26 (NCI-H1573, A498, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.695×** | -6.3 | 1e-08 | 18/26 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.692×** | -6.1 | 4e-08 | 15/25 (NCI-H1573, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 47.6 | 1 | 19 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.36× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.272× (z -12.0) |
| [[HOP62 (line)]] | alt | 60.8 | 5 | 6 | [[Panobinostat (drug)]] 5 µM 6.19× (z +14.3) | [[Clobetasol propionate (drug)]] 0.05 µM 0.205× (z -12.4) |
| [[J82 (line)]] | alt | 51.6 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.27× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 38.5 | 1 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.81× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 0.0923× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 28.0 | 1 | 6 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.54× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.0664× (z -21.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 39.1 | 7 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.14× (z +18.9) | — |
| [[LOX-IMVI (line)]] | wt | 202 | 4 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.73× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.385× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 123 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +12.4) | [[Clobetasol propionate (drug)]] 0.5 µM 0.371× (z -10.0) |
| [[A498 (line)]] | wt | 50.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.21× (z +18.9) | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 5.22× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 96.8 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.73× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 7.22× (z +18.7) | — |
| [[SNU-423 (line)]] | alt | 38.5 | 4 | 0 | [[Belinostat (drug)]] 5 µM 6.08× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 75.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 15.2 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.54× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 41.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.00× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 40.2 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.71× (z +9.0) ⚠ unreliable plate only | [[Clobetasol propionate (drug)]] 0.05 µM 0.258× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 5.36× (z +9.5) | — |
| [[LoVo (line)]] | wt | 22.2 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.96× (z +9.2) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.273× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 37.8 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.612× (z -13.0) ⚠ position not correctable · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -9.1) |
| [[LS 180 (line)]] | wt | 46.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.48× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 84.2 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.96× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 86.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 92.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 10.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.86× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2A1]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[WSCD1]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.69 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[C3orf52]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[STC1]] | +0.68 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[FAM107B]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[GALNT12]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[NRIP3]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[TFPI2]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TMEM158]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SLC9A7]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PTHLH]] | +0.64 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRG2]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[NNMT]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[KLF9]] | -0.56 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[EFCAB2]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TNS2]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN5]] | B | TSPAN5 activity raises PKIA's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 4.62× lower at baseline in the lines without TSPAN5 | 0.020 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[MIR155HG]] | B | MIR155HG activity raises PKIA's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without MIR155HG | 0.040 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[SERPINB9]] | B | SERPINB9 activity lowers PKIA's level | lines that do not express SERPINB9 (24) vs lines expressing it (26) | 2.07× higher at baseline in the lines without SERPINB9 | 0.042 | ⚠ within organs, on part of the lines; also absent: MT1A, SHH, LINC02086 |
| [[KHDRBS3]] | B | KHDRBS3 activity raises PKIA's level | lines that do not express KHDRBS3 (11) vs lines expressing it (39) | 3.80× lower at baseline in the lines without KHDRBS3 | 0.052 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |
| [[MAST4]] | B | MAST4 activity raises PKIA's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 3.18× lower at baseline in the lines without MAST4 | 0.057 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers PKIA's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[CAMK1D]] | B | CAMK1D activity raises PKIA's level | lines that do not express CAMK1D (9) vs lines expressing it (41) | 2.77× lower at baseline in the lines without CAMK1D | 0.090 | ⚠ within organs, on part of the lines; also absent: OBSCN |
| [[PRDM8]] | B | PRDM8 activity raises PKIA's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.59× lower at baseline in the lines without PRDM8 | 0.097 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[SERPINB2]] | C | SERPINB2 activity raises PKIA's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 3.66× lower at baseline in the lines without SERPINB2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[PTGS2]] | C | PTGS2 activity raises PKIA's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 3.85× lower at baseline in the lines without PTGS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |
| [[INHBA]] | C | INHBA activity raises PKIA's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without INHBA | 0.054 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[DTNA]] | C | DTNA activity raises PKIA's level | lines that do not express DTNA (22) vs lines expressing it (28) | 3.86× lower at baseline in the lines without DTNA | 0.067 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL33]] | B | PKIA activity raises IL33's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without PKIA | 0.014 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[TSPAN5]] | B | PKIA activity raises TSPAN5's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without PKIA | 0.019 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[NMNAT2]] | B | PKIA activity raises NMNAT2's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.26× lower at baseline in the lines without PKIA | 0.044 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[VAT1L]] | B | PKIA activity raises VAT1L's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without PKIA | 0.047 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[RAC2]] | B | PKIA activity raises RAC2's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without PKIA | 0.074 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[SRD5A3]] | B | PKIA activity raises SRD5A3's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.64× lower at baseline in the lines without PKIA | 0.084 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[APBB2]] | B | PKIA activity raises APBB2's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without PKIA | 0.086 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[BCL11B]] | B | PKIA activity raises BCL11B's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without PKIA | 0.089 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[ANTXR2]] | B | PKIA activity raises ANTXR2's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without PKIA | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[MIR155HG]] | B | PKIA activity raises MIR155HG's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without PKIA | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[SLC14A1]] | B | PKIA activity raises SLC14A1's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without PKIA | 0.098 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[INHBA]] | C | PKIA activity raises INHBA's level | lines that do not express PKIA (22) vs lines expressing it (28) | 3.68× lower at baseline in the lines without PKIA | 0.054 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, -0.0); signed map (2.1, 46.7). **Vector** length 115, 34.4% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.9 | +24.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.4 | +14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +17.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +23.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +25.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +4.6 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.2 | +2.8 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -5.5 | -7.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.4 | -6.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.3 | -7.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.1 | -7.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.9 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | cAMP-dependent protein kinase inhibitor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:78,516,340-78,605,267 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRKACN1 |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P61925](https://www.uniprot.org/uniprotkb/P61925) (cAMP-dependent protein kinase inhibitor alpha):

> Extremely potent competitive inhibitor of cAMP-dependent protein kinase activity, this protein interacts with the catalytic subunit of the enzyme after the cAMP-induced dissociation of its regulatory chains.

**Summary**, from NCBI Gene [5569](https://www.ncbi.nlm.nih.gov/gene/5569):

> The protein encoded by this gene is a member of the cAMP-dependent protein kinase (PKA) inhibitor family. This protein was demonstrated to interact with and inhibit the activities of both C alpha and C beta catalytic subunits of the PKA. Alternatively spliced transcript variants encoding the same protein have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9017) · Entrez [5569](https://www.ncbi.nlm.nih.gov/gene/5569) · UniProt [P61925](https://www.uniprot.org/uniprotkb/P61925) · Ensembl [ENSG00000171033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171033)

## Data

Gene col 10041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10041); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10041]; `tensor/DDL_lfc|DDL_z.npy` [10041]; `embed/gene_vectors.npy` [10041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10041 or target_col == 10041). Every well: [[PKIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
