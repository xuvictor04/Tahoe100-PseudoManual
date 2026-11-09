---
symbol: "ZNF83"
type: "gene"
col: 9534
ensembl_id: "ENSG00000167766"
name: "zinc finger protein 83"
location: "19q13.41"
module: 110
arm: "+"
pooled_cpm: 108.46
n_lines_expressing: 40
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# ZNF83

*zinc finger protein 83* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.44× (z +20.3, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.740× (z -6.6, q 2e-08, down in 21 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2B]] (+0.64, fdr 1e-05), [[LINC01589]] (+0.63, fdr 9e-06), [[TM4SF19-DYNLT2B]] (+0.63, fdr 1e-05); moves opposite to [[ATRAID]] (-0.61, fdr 7e-06), [[PHF21A]] (-0.57, fdr 1e-05), [[ATF2]] (-0.55, fdr 2e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF611]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9534.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +20.3 | 0e+00 | 37/38 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +8.6 | 3e-15 | 24/38 (LoVo, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +8.1 | 1e-13 | 24/38 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.6 | 6e-12 | 19/38 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +7.4 | 2e-11 | 22/38 (BT-474, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +6.0 | 2e-07 | 24/38 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.9 | 3e-07 | 0/40 | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.61×** | +5.7 | 1e-06 | 26/38 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.6 | 1e-06 | 17/39 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +5.4 | 3e-06 | 22/38 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.2 | 8e-06 | 18/35 (CFPAC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +5.0 | 3e-05 | 20/37 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 1e-04 | 18/37 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +4.4 | 5e-04 | 19/37 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 5e-04 | 17/39 (NCI-H1573, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +4.3 | 7e-04 | 17/38 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +4.2 | 9e-04 | 16/38 (SNU-423, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.001 | 16/39 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.003 | 18/38 (LoVo, BT-474, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.740×** | -6.6 | 2e-08 | 21/38 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.846× | -5.4 | 2e-05 | 18/39 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.788×** | -5.2 | 5e-05 | 19/38 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.817×** | -5.1 | 6e-05 | 20/38 (LoVo, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.852× | -4.4 | 0.001 | 17/38 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.848× | -4.1 | 0.004 | 15/39 (HOP62, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.843× | -3.9 | 0.008 | 19/38 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.841× | -3.8 | 0.009 | 18/40 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -3.3 | 0.063 | 11/40 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.863× | -3.3 | 0.063 | 14/38 (LoVo, HOP62, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.906× | -3.2 | 0.065 | 5/38 (AsPC-1, LoVo, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.866× | -3.2 | 0.066 | 11/39 (A-172, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.906× | -3.2 | 0.066 | 8/38 (NCI-H2347, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.085 | 13/39 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.871× | -3.0 | 0.087 | 10/38 (LoVo, HT-29, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.878× | -3.0 | 0.098 | 13/38 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.913× | -3.0 | 0.098 | 10/38 (AsPC-1, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 305 | 11 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +24.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.99× (z +19.9) | [[Radotinib (drug)]] 5 µM 0.615× (z -8.7) |
| [[BT-474 (line)]] | alt | 244 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.12× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 243 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.507× (z -10.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 83.9 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.71× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 108 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.79× (z +19.5) | — |
| [[SNU-423 (line)]] | alt | 193 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +23.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.3) ⚠ cell-cycle shift, explains ~10% of this change |
| [[CFPAC-1 (line)]] | alt | 97.2 | 5 | 0 | [[Auranofin (drug)]] 5 µM 5.42× (z +18.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 193 | 3 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.40× (z +16.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 94.9 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.355× (z -15.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.362× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 106 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.20× (z +21.4) | — |
| [[A-172 (line)]] | wt | 225 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +14.0) | — |
| [[A-427 (line)]] | wt | 148 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.477× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 311 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.44× (z +8.7) | [[Radotinib (drug)]] 5 µM 0.518× (z -9.1) |
| [[H4 (line)]] | wt | 223 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 108 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.21× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -11.7) ⚠ cell-cycle shift, explains ~10% of this change |
| [[PANC-1 (line)]] | alt | 105 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.04× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.619× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.507× (z -9.5) |
| [[RKO (line)]] | wt | 131 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.14× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0950× (z -28.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 75.7 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.95× (z +14.5) | — |
| [[SNU-1 (line)]] | wt | 244 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 95.9 | 0 | 2 | — | [[Dexamethasone (drug)]] 5 µM 0.0850× (z -9.4) |
| [[C32 (line)]] | wt | 61.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.65× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 107 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.66× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 80.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 56.2 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -9.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[NCI-H23 (line)]] | alt | 60.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.331× (z -13.2) |
| [[SW 900 (line)]] | alt | 92.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.89× (z +11.5) | — |
| [[A498 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.29 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2B]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[LINC01589]] | +0.63 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[TM4SF19-DYNLT2B]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TM4SF19]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[BICD1]] | +0.59 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CLCF1]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TBILA]] | +0.58 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[OSBP2]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ZNF165]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 | same gene group |
| [[ITGA2]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRAID]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[PHF21A]] | -0.57 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ATF2]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 | same gene group |
| [[ZMYM3]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[COPS4]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[CAND1]] | -0.52 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[RHOXF1]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF608]] | -0.51 | -0.41 / -0.59 | both halves | 4e-05 | same gene group |
| [[RCOR3]] | -0.50 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[RAB14]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ECH1]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[MDH1]] | -0.49 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity strengthens ZNF83's drug response | lines that do not express C6orf141 (18) vs lines expressing it (22) | the lines without C6orf141 respond 0.67× as strongly (z diff +1.41); strongest at Ixazomib citrate 0.5 µM: 1.18x vs 2.05x (z diff +4.6) | 0.094 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1; target measured in part of the lines; artifact flags |
| [[SSBP2]] | C | SSBP2 activity raises ZNF83's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 4.85× lower at baseline in the lines without SSBP2 | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF611]] | B | ZNF83 activity raises ZNF611's level | lines that do not express ZNF83 (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without ZNF83 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000269825, ZNF28, ZNF525 |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.9, 0.1); signed map (7.3, 41.5). **Vector** length 120, 31.7% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.6 | +20.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.9 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.5 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +8.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.6 | +4.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.6 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -4.4 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -3.0 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 83 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:52,594,060-52,690,559 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11015, HPF1; previously ZNF816B |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P51522](https://www.uniprot.org/uniprotkb/P51522) (Zinc finger protein 83):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [55769](https://www.ncbi.nlm.nih.gov/gene/55769):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nuclear lumen. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13158) · Entrez [55769](https://www.ncbi.nlm.nih.gov/gene/55769) · UniProt [P51522](https://www.uniprot.org/uniprotkb/P51522) · Ensembl [ENSG00000167766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167766)

## Data

Gene col 9534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9534); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9534]; `tensor/DDL_lfc|DDL_z.npy` [9534]; `embed/gene_vectors.npy` [9534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9534 or target_col == 9534). Every well: [[ZNF83 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF83.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
