---
symbol: "TAPBP"
type: "gene"
col: 13824
ensembl_id: "ENSG00000231925"
name: "TAP binding protein"
location: "6p21.32"
module: 70
arm: "+"
pooled_cpm: 138.78
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 20
n_dd_up_clean: 15
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TAPBP

*TAP binding protein* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.88× (z +10.6, q 2e-23, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.353× (z -17.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAP1]] (+0.75, fdr 7e-06), [[TAPBPL]] (+0.74, fdr 1e-05), [[HLA-H]] (+0.73, fdr 1e-05); moves opposite to [[RBAK-RBAKDN]] (-0.70, fdr 1e-05), [[RNF216P1]] (-0.59, fdr 6e-05), [[PWWP3A]] (-0.59, fdr 4e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CTSO]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +10.6 | 2e-23 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.9 | 6e-13 | 44/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +6.5 | 2e-08 | 36/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 1e-07 | 39/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +5.8 | 6e-07 | 40/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.33×** | +4.8 | 1e-04 | 40/49 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +4.6 | 3e-04 | 25/48 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +4.2 | 0.001 | 21/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +4.2 | 0.001 | 30/50 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 29/49 (AsPC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.9 | 0.006 | 26/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.006 | 21/49 (AsPC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.006 | 27/47 (AsPC-1, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.009 | 29/49 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.012 | 23/48 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.016 | 26/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.033 | 11/48 (C-33 A, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.035 | 20/48 (AsPC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.035 | 26/48 (AsPC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.036 | 25/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.353×** | -17.5 | 0e+00 | 48/48 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -17.5 | 0e+00 | 47/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.372×** | -16.6 | 0e+00 | 48/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.580×** | -9.2 | 7e-18 | 46/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -8.2 | 2e-14 | 43/48 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.625×** | -7.5 | 8e-12 | 43/48 (SNU-423, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.664×** | -6.9 | 5e-10 | 46/48 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -6.9 | 5e-10 | 37/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.502×** | -6.1 | 9e-08 | 38/45 (NCI-H23, SW48, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.709×** | -5.6 | 2e-06 | 41/49 (HS-578T, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.581×** | -4.8 | 9e-05 | 41/49 (COLO 205, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.754×** | -4.8 | 9e-05 | 37/49 (NCI-H23, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.831×** | -4.4 | 4e-04 | 24/49 (H4, SW 900, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.838× | -4.2 | 0.001 | 25/49 (COLO 205, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.816×** | -3.4 | 0.022 | 24/49 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.024 | 22/48 (BT-474, KATO III, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.9 | 7 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 4.07× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +15.5) | [[Belinostat (drug)]] 5 µM 0.377× (z -11.0) |
| [[BT-474 (line)]] | alt | 154 | 5 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 3.70× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +12.8) | [[Belinostat (drug)]] 5 µM 0.332× (z -11.0) |
| [[HOP62 (line)]] | alt | 123 | 4 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 189 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -9.5) |
| [[PANC-1 (line)]] | alt | 175 | 3 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -13.3) |
| [[COLO 205 (line)]] | alt | 121 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -16.0) |
| [[A-172 (line)]] | wt | 204 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.348× (z -13.4) |
| [[KATO III (line)]] | alt | 134 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.220× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 186 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.165× (z -18.2) |
| [[SW 900 (line)]] | alt | 114 | 2 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.404× (z -9.5) |
| [[A-427 (line)]] | wt | 112 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 106 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -13.1) |
| [[H4 (line)]] | wt | 177 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -12.5) |
| [[HS-578T (line)]] | alt | 250 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.14× (z +8.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.392× (z -10.7) |
| [[HT-29 (line)]] | alt | 163 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -15.0) |
| [[LoVo (line)]] | wt | 115 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.197× (z -19.2) |
| [[LS 180 (line)]] | wt | 82.4 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.395× (z -10.7) |
| [[RKO (line)]] | wt | 85.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.333× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 172 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 2.27× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.361× (z -11.9) |
| [[SNU-423 (line)]] | alt | 276 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -12.5) |
| [[SW1417 (line)]] | alt | 105 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -15.4) |
| [[SW48 (line)]] | wt | 92.5 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.288× (z -10.1) |
| [[SW480 (line)]] | alt | 62.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.225× (z -17.7) |
| [[A498 (line)]] | wt | 126 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.2) |
| [[A549 (line)]] | wt | 138 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 246 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -11.6) |
| [[HCT15 (line)]] | alt | 162 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -18.1) |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -10.2) |
| [[Hs 766T (line)]] | wt | 170 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 154 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.371× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 97.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 219 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 129 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 265 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 140 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.327× (z -11.5) |
| [[C-33 A (line)]] | alt | 69.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 149 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.490× (z -9.0) |
| [[J82 (line)]] | alt | 145 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.5) | — |
| [[SNU-1 (line)]] | wt | 135 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.302× (z -9.6) |
| [[C32 (line)]] | wt | 97.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.411× (z -8.6) |
| [[SHP-77 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAP1]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 995 |
| [[TAPBPL]] | +0.74 | +0.55 / +0.73 | both halves | 1e-05 | same gene group; STRING 661 |
| [[HLA-H]] | +0.73 | +0.54 / +0.70 | both halves | 1e-05 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| [[ERAP1]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 827 |
| [[CTSS]] | +0.69 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 430 |
| [[C5orf15]] | +0.69 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[HLA-C]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 981 |
| [[SLC39A1]] | +0.67 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RNF213]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[LINC02605]] | +0.66 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CTSO]] | +0.66 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TRIM69]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBAK-RBAKDN]] | -0.70 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[RNF216P1]] | -0.59 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[PWWP3A]] | -0.59 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[WASF3]] | -0.59 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[DHX57]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[GPR89B]] | -0.57 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[SNU13]] | -0.57 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NEIL2]] | -0.57 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[EIF4EBP1]] | -0.57 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[GTF2H2]] | -0.57 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TECPR1]] | -0.56 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[BICD2]] | -0.56 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSO]] | B | CTSO activity raises TAPBP's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without CTSO | 0.008 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |
| [[HLA-F]] | B | HLA-F activity raises TAPBP's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without HLA-F | 0.077 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TAPBP's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.9, 4.1); signed map (24.6, -20.3). **Vector** length 157, 56.8% of its response variance represented; |z| ≥ 3 in 1,585 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.57 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.63 to 8); *Interferon alpha/beta signaling* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +10.2 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.9 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.4 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +7.4 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.6 | +4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +6.4 | +3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +6.0 | +4.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.1 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.9 | -8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.6 | -16.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.9 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.8 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -3.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.2 | -4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TAP binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,299,694-33,314,284 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAPA, TPN, TPSN, NGS17 |
| Gene groups (HGNC) | C1-set domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; ER-Phagosome pathway; Antigen processing-Cross presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15533](https://www.uniprot.org/uniprotkb/O15533) (Tapasin):

> Involved in the association of MHC class I with transporter associated with antigen processing (TAP) and in the assembly of MHC class I with peptide (peptide loading).

**Summary**, from NCBI Gene [6892](https://www.ncbi.nlm.nih.gov/gene/6892):

> This gene encodes a transmembrane glycoprotein which mediates interaction between newly assembled major histocompatibility complex (MHC) class I molecules and the transporter associated with antigen processing (TAP), which is required for the transport of antigenic peptides across the endoplasmic reticulum membrane. This interaction is essential for optimal peptide loading on the MHC class I molecule. Up to four complexes of MHC class I and this protein may be bound to a single TAP molecule. …

**Accessions** — [HGNC:11566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11566) · Entrez [6892](https://www.ncbi.nlm.nih.gov/gene/6892) · UniProt [O15533](https://www.uniprot.org/uniprotkb/O15533) · Ensembl [ENSG00000231925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231925)

## Data

Gene col 13824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13824); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13824]; `tensor/DDL_lfc|DDL_z.npy` [13824]; `embed/gene_vectors.npy` [13824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13824 or target_col == 13824). Every well: [[TAPBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAPBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
