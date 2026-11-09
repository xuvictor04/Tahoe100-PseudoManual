---
symbol: "MYEF2"
type: "gene"
col: 2424
ensembl_id: "ENSG00000104177"
name: "myelin expression factor 2"
location: "15q21.1"
module: 22
arm: "+"
pooled_cpm: 44.11
n_lines_expressing: 34
n_dd_up: 30
n_dd_down: 17
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MYEF2

*myelin expression factor 2* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.43× (z +35.3, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.570× (z -11.4, q 2e-27, down in 23 of 31 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHLRC2]] (+0.65, fdr 1e-05), [[CCDC50]] (+0.63, fdr 1e-05), [[DEPDC1]] (+0.61, fdr 1e-05); moves opposite to [[MED26]] (-0.59, fdr 3e-05), [[EIF1AD]] (-0.58, fdr 4e-05), [[MTF1]] (-0.57, fdr 6e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); 5 go from it, the strongest it → [[PRC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.43×** | +35.3 | 0e+00 | 31/32 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.05×** | +21.7 | 0e+00 | 28/31 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +16.3 | 0e+00 | 27/32 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +13.8 | 6e-41 | 19/29 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +13.3 | 2e-38 | 24/30 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +11.0 | 3e-26 | 21/32 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +10.6 | 2e-24 | 22/29 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.61×** | +9.7 | 3e-20 | 28/31 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +9.6 | 3e-20 | 25/32 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +8.8 | 6e-17 | 20/32 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.52×** | +8.6 | 6e-16 | 24/31 (A-172, HOP62, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.53×** | +8.3 | 5e-15 | 23/31 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +8.3 | 5e-15 | 21/31 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +8.3 | 5e-15 | 20/31 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.50×** | +8.2 | 8e-15 | 22/31 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +7.7 | 4e-13 | 21/31 (A549, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +7.3 | 7e-12 | 20/31 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.42×** | +7.2 | 2e-11 | 21/31 (A549, A-172, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 1e-10 | 19/31 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.20× | +5.1 | 8e-06 | 11/32 (HT-29, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.570×** | -11.4 | 2e-27 | 23/31 (SW480, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -10.9 | 4e-25 | 22/32 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.677×** | -7.9 | 6e-13 | 21/31 (NCI-H23, A549, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.684×** | -7.7 | 2e-12 | 19/32 (HEC-1-A, A549, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.493×** | -7.5 | 8e-12 | 18/26 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.755×** | -5.7 | 1e-06 | 14/32 (BT-474, CHP-212, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **0.757×** | -5.4 | 5e-06 | 16/31 (SW480, NCI-H23, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.609×** | -5.3 | 1e-05 | 17/31 (SW480, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.773×** | -5.2 | 1e-05 | 18/31 (C-33 A, A549, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.766×** | -5.2 | 1e-05 | 17/31 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.860× | -4.3 | 9e-04 | 12/32 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.811×** | -4.2 | 0.001 | 14/31 (SW480, PANC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.816×** | -4.1 | 0.002 | 13/31 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.825×** | -3.9 | 0.004 | 12/31 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.826×** | -3.9 | 0.004 | 11/31 (SNU-423, A-172, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | 0.838× | -3.6 | 0.011 | 10/31 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.839× | -3.5 | 0.012 | 13/31 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.841× | -3.5 | 0.013 | 14/31 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.842× | -3.5 | 0.014 | 10/31 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.832×** | -3.4 | 0.016 | 12/31 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.036 | 11/31 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 86.2 | 7 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +20.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -15.0) |
| [[SW480 (line)]] | alt | 40.0 | 5 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.1) | [[Auranofin (drug)]] 5 µM 0.309× (z -12.7) |
| [[A-172 (line)]] | wt | 63.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +24.7) | — |
| [[HOP62 (line)]] | alt | 21.9 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +18.6) | — |
| [[PANC-1 (line)]] | alt | 85.6 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +28.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -14.9) |
| [[A-427 (line)]] | wt | 53.0 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +18.7) | [[Auranofin (drug)]] 5 µM 0.372× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 44.3 | 4 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 6.36× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 49.7 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +22.7) | [[Auranofin (drug)]] 5 µM 0.321× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 19.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +18.4) | — |
| [[HEC-1-A (line)]] | alt | 156 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -13.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 94.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +20.0) | — |
| [[NCI-H2030 (line)]] | alt | 95.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +18.7) | — |
| [[SW 900 (line)]] | alt | 89.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 47.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.9 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 2.99× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -14.8) |
| [[SW1417 (line)]] | alt | 59.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +19.6) | — |
| [[BT-474 (line)]] | alt | 62.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.350× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[C-33 A (line)]] | alt | 132 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.395× (z -9.6) |
| [[CHP-212 (line)]] | wt | 46.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -10.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 60.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 41.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 39.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 51.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -13.9) |
| [[SNU-423 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.8) | — |
| [[A498 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.78 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.89 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CCDC50]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[DEPDC1]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SHTN1]] | +0.56 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[PPP1R9A]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[CEP135]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[PHF19]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[DNAH14]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SPDL1]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HYLS1]] | +0.55 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[CDH2]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | -0.59 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[EIF1AD]] | -0.58 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[MTF1]] | -0.57 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[QPCTL]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[MED31]] | -0.54 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[IL17RA]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SDF2]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[DPM1]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SLC35E1]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[SENP5]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MARK4]] | -0.53 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[DDX49]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers MYEF2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRC1]] | B | MYEF2 activity raises PRC1's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.27× lower at baseline in the lines without MYEF2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |
| [[TEX261]] | B | MYEF2 activity raises TEX261's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.08× lower at baseline in the lines without MYEF2 | 0.072 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |
| [[ARHGAP11A]] | B | MYEF2 activity raises ARHGAP11A's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.27× lower at baseline in the lines without MYEF2 | 0.082 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |
| [[KIF4A]] | B | MYEF2 activity raises KIF4A's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.50× lower at baseline in the lines without MYEF2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |
| [[TAF9B]] | B | MYEF2 activity raises TAF9B's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without MYEF2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.4, -51.1); signed map (15.3, -31.7). **Vector** length 114, 31.8% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +35.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +10.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +6.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.0 | +8.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -11.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.6 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -3.6 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | myelin expression factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:48,134,632-48,178,353 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEF-2, FLJ11213, KIAA1341, HsT18564 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2K5](https://www.uniprot.org/uniprotkb/Q9P2K5) (Myelin expression factor 2):

> Transcriptional repressor of the myelin basic protein gene (MBP). Binds to the proximal MB1 element 5'-TTGTCC-3' of the MBP promoter. Its binding to MB1 and function are inhibited by PURA (By similarity).

**Summary**, from NCBI Gene [50804](https://www.ncbi.nlm.nih.gov/gene/50804):

> Enables RNA binding activity. Involved in myotube differentiation and neuron differentiation. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17940) · Entrez [50804](https://www.ncbi.nlm.nih.gov/gene/50804) · UniProt [Q9P2K5](https://www.uniprot.org/uniprotkb/Q9P2K5) · Ensembl [ENSG00000104177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104177)

## Data

Gene col 2424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2424); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2424]; `tensor/DDL_lfc|DDL_z.npy` [2424]; `embed/gene_vectors.npy` [2424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2424 or target_col == 2424). Every well: [[MYEF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYEF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
