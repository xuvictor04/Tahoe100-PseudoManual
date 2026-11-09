---
symbol: "UGP2"
type: "gene"
col: 9855
ensembl_id: "ENSG00000169764"
name: "UDP-glucose pyrophosphorylase 2"
location: "2p15"
module: 106
arm: "+"
pooled_cpm: 127.52
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# UGP2

*UDP-glucose pyrophosphorylase 2* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +12.2, q 2e-31, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.445× (z -23.4, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSBP2]] (+0.63, fdr 7e-06), [[CLASP1]] (+0.60, fdr 9e-06), [[SEC14L2]] (+0.59, fdr 1e-05); moves opposite to [[IL11]] (-0.56, fdr 1e-05), [[PER3]] (-0.52, fdr 2e-05), [[ADAMTS16]] (-0.51, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +12.2 | 2e-31 | 40/49 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.0 | 6e-10 | 37/50 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.3 | 6e-08 | 32/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.6 | 4e-06 | 22/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 6e-05 | 22/48 (NCI-H1792, LOX-IMVI, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.7 | 2e-04 | 23/48 (NCI-H2347, hTERT-HPNE, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 2e-04 | 25/48 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 28/49 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +4.4 | 6e-04 | 20/48 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 6e-04 | 25/48 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.3 | 8e-04 | 0/50 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.003 | 23/48 (LOX-IMVI, NCI-H1792, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.008 | 21/50 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 1.19× | +3.5 | 0.020 | 22/48 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.026 | 21/48 (LOX-IMVI, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.033 | 21/48 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.060 | 21/47 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.445×** | -23.4 | 0e+00 | 43/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.427×** | -17.3 | 0e+00 | 42/48 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.491×** | -14.5 | 3e-45 | 44/48 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.482×** | -12.5 | 6e-34 | 42/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.550×** | -12.2 | 5e-32 | 39/48 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.551×** | -11.7 | 2e-29 | 43/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.635×** | -9.3 | 2e-18 | 39/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -7.3 | 2e-11 | 32/48 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -7.2 | 3e-11 | 29/47 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -5.5 | 3e-06 | 28/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -5.4 | 4e-06 | 33/47 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.777×** | -5.1 | 1e-05 | 30/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.785×** | -4.9 | 3e-05 | 27/48 (C32, A-172, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.652×** | -4.6 | 2e-04 | 34/49 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.800×** | -4.5 | 2e-04 | 25/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.809×** | -4.3 | 6e-04 | 25/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.892× | -3.3 | 0.029 | 12/49 (C32, SK-MEL-2, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.852× | -3.3 | 0.030 | 14/48 (HepG2/C3A, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.827×** | -3.2 | 0.035 | 16/47 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 286 | 17 | 6 (1 ⚠) | [[Dexamethasone (drug)]] 5 µM 2.72× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 142 | 15 | 7 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.78× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -23.1) |
| [[hTERT-HPNE (line)]] | wt | 110 | 18 | 1 | [[Triamcinolone (drug)]] 5 µM 3.10× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.376× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 104 | 15 | 2 | [[Triamcinolone (drug)]] 5 µM 2.32× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -14.2) |
| [[C32 (line)]] | wt | 292 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 140 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -27.3) |
| [[HS-578T (line)]] | alt | 116 | 7 | 5 | [[Triamcinolone (drug)]] 5 µM 2.09× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 299 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -26.5) |
| [[HOP62 (line)]] | alt | 126 | 5 | 5 | [[Triamcinolone (drug)]] 5 µM 1.76× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.7) |
| [[SW480 (line)]] | alt | 105 | 4 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +18.2) | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 133 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -14.6) |
| [[BT-474 (line)]] | alt | 104 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.0) |
| [[KATO III (line)]] | alt | 146 | 1 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -20.4) |
| [[A549 (line)]] | wt | 150 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -16.5) |
| [[SHP-77 (line)]] | alt | 106 | 6 | 0 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.50× (z +8.8) | — |
| [[A-172 (line)]] | wt | 135 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -22.4) |
| [[COLO 205 (line)]] | alt | 146 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -19.5) |
| [[PANC-1 (line)]] | alt | 85.6 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 147 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -20.5) |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 208 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -14.6) |
| [[H4 (line)]] | wt | 129 | 3 | 1 | [[Dexamethasone (drug)]] 0.05 µM 2.97× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.5) |
| [[HT-29 (line)]] | alt | 133 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -13.9) |
| [[J82 (line)]] | alt | 108 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 117 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.427× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 93.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -12.8) |
| [[Hs 766T (line)]] | wt | 77.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 102 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -16.7) |
| [[SNU-1 (line)]] | wt | 58.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.261× (z -10.0) |
| [[SNU-423 (line)]] | alt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -12.1) |
| [[HCT15 (line)]] | alt | 137 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.8) |
| [[LS 180 (line)]] | wt | 150 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -16.6) |
| [[SW 900 (line)]] | alt | 129 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.6) |
| [[A498 (line)]] | wt | 132 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +9.1) | — |
| [[LoVo (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -8.8) |
| [[RKO (line)]] | wt | 70.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 104 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +13.1) | — |
| [[A-427 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSBP2]] | +0.63 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[CLASP1]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[SEC14L2]] | +0.59 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.58 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TLR2]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[KLF9]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ACSL1]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[HELZ]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[LNPK]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PHF21A]] | +0.57 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SLC19A2]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[AK4]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL11]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PER3]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ADAMTS16]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SLAMF7]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[NAV3]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CHMP6]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LINC02154]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CREB5]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SYT14]] | -0.48 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[LINC01589]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[LINC01060]] | -0.48 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[GPR39]] | -0.48 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises UGP2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[LINC01589]] | B | LINC01589 activity raises UGP2's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.31× lower at baseline in the lines without LINC01589 | 0.057 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[TOP2A]] | B | TOP2A activity lowers UGP2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KLF9]] | B | KLF9 activity lowers UGP2's level | lines that do not express KLF9 (5) vs lines expressing it (45) | 1.41× higher at baseline in the lines without KLF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: NDC80, WDR54, ADGRB2; maybe low, not absent; its own permutation p |
| [[EVC]] | B | EVC activity lowers UGP2's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.12× higher at baseline in the lines without EVC | 0.089 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 14.9); signed map (15.7, 29.6). **Vector** length 140, 49.4% of its response variance represented; |z| ≥ 3 in 1,412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.4 | +12.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +6.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +7.0 | +4.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +7.0 | +4.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +7.0 | +5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +6.7 | +4.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +6.7 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.4 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.3 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -12.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -7.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.6 | -2.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -3.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | UDP-glucose pyrophosphorylase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:63,840,952-63,891,562 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UGPP1, SVUGP2; previously UGP1 |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 7 pathways, smallest: Formation of the active cofactor, UDP-glucuronate; Glucuronidation; Glycogen synthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16851](https://www.uniprot.org/uniprotkb/Q16851) (UTP--glucose-1-phosphate uridylyltransferase):

> UTP--glucose-1-phosphate uridylyltransferase catalyzing the conversion of glucose-1-phosphate into UDP-glucose, a crucial precursor for the production of glycogen.

**Summary**, from NCBI Gene [7360](https://www.ncbi.nlm.nih.gov/gene/7360):

> The enzyme encoded by this gene is an important intermediary in mammalian carbohydrate interconversions. It transfers a glucose moiety from glucose-1-phosphate to MgUTP and forms UDP-glucose and MgPPi. In liver and muscle tissue, UDP-glucose is a direct precursor of glycogen; in lactating mammary gland it is converted to UDP-galactose which is then converted to lactose. The eukaryotic enzyme has no significant sequence similarity to the prokaryotic enzyme. Two transcript variants encoding …

**Accessions** — [HGNC:12527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12527) · Entrez [7360](https://www.ncbi.nlm.nih.gov/gene/7360) · UniProt [Q16851](https://www.uniprot.org/uniprotkb/Q16851) · Ensembl [ENSG00000169764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169764)

## Data

Gene col 9855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9855); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9855]; `tensor/DDL_lfc|DDL_z.npy` [9855]; `embed/gene_vectors.npy` [9855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9855 or target_col == 9855). Every well: [[UGP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
