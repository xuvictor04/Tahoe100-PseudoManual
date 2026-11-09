---
symbol: "ANKH"
type: "gene"
col: 7772
ensembl_id: "ENSG00000154122"
name: "ANKH inorganic pyrophosphate transport regulator"
location: "5p15.2"
module: 92
arm: "+"
pooled_cpm: 85.05
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ANKH

*ANKH inorganic pyrophosphate transport regulator* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +5.8, q 5e-06, up in 20 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.447× (z -21.9, q 0e+00, down in 39 of 42 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.472× (z -13.9, q 2e-41, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF704]] (+0.57, fdr 1e-05), [[OSBPL10]] (+0.57, fdr 1e-05), [[SPRED2]] (+0.56, fdr 1e-05); moves opposite to [[TRAFD1]] (-0.47, fdr 6e-05), [[LRRC27]] (-0.45, fdr 1e-04), [[MYOF]] (-0.45, fdr 1e-04).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → [[RGS17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.8 | 5e-06 | 20/42 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +5.1 | 1e-04 | 18/43 (LoVo, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 0.002 | 19/43 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +3.8 | 0.018 | 17/42 (LoVo, A498, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.026 | 12/43 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.033 | 16/42 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.20× | +3.2 | 0.093 | 11/42 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.15 | 12/42 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.447×** | -21.9 | 0e+00 | 39/42 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -13.9 | 2e-41 | 39/42 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.495×** | -13.5 | 2e-39 | 36/42 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.669×** | -7.2 | 1e-10 | 24/39 (RKO, LS 180, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.497×** | -7.0 | 2e-10 | 27/43 (LOX-IMVI, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -6.8 | 1e-09 | 27/42 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.717×** | -6.4 | 1e-08 | 26/42 (NCI-H1792, HS-578T, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.730×** | -6.1 | 1e-07 | 30/41 (J82, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.735×** | -5.9 | 2e-07 | 29/42 (J82, HS-578T, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -5.2 | 9e-06 | 24/42 (NCI-H2030, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.763×** | -5.2 | 9e-06 | 23/42 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -5.1 | 1e-05 | 3/44 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.764×** | -5.0 | 2e-05 | 20/37 (Panc 03.27, SW480, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.779×** | -4.8 | 6e-05 | 25/42 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.799×** | -4.7 | 1e-04 | 19/43 (HOP62, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.800×** | -4.3 | 5e-04 | 19/43 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.860× | -4.1 | 0.001 | 19/43 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -4.0 | 0.002 | 22/42 (HOP62, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.812×** | -3.9 | 0.003 | 18/41 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.816×** | -3.8 | 0.004 | 19/41 (HOP62, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.007 | 16/42 (C32, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 271 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -25.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -18.6) |
| [[HS-578T (line)]] | alt | 293 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0717× (z -35.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -20.2) |
| [[SHP-77 (line)]] | alt | 349 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.320× (z -13.9) |
| [[SW480 (line)]] | alt | 153 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -15.2) |
| [[A-172 (line)]] | wt | 57.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -21.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 211 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -26.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.270× (z -14.6) |
| [[RKO (line)]] | wt | 108 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -23.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.136× (z -18.9) |
| [[Hs 766T (line)]] | wt | 182 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -10.0) |
| [[LoVo (line)]] | wt | 130 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.353× (z -11.1) |
| [[C32 (line)]] | wt | 96.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -11.0) |
| [[HOP62 (line)]] | alt | 61.1 | 0 | 5 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.588× (z -17.4) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.390× (z -9.7) |
| [[LS 180 (line)]] | wt | 116 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 47.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -20.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.183× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0613× (z -23.5) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 89.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -22.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.203× (z -16.6) |
| [[SW48 (line)]] | wt | 75.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -15.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -10.6) |
| [[A-427 (line)]] | wt | 121 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -17.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -16.0) |
| [[A549 (line)]] | wt | 48.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -12.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 201 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 43.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -18.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 77.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.405× (z -9.0) |
| [[SW 1271 (line)]] | alt | 89.7 | 0 | 3 (2 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0794× (z -9.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0774× (z -8.9) |
| [[SW1417 (line)]] | alt | 162 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.405× (z -9.9) |
| [[PANC-1 (line)]] | alt | 25.3 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 58.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CHP-212 (line)]] | wt | 51.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -12.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 72.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -12.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 58.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 71.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.108× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF704]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[OSBPL10]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SPRED2]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[FXYD5]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[KCNC4]] | +0.55 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ETV4]] | +0.55 | +0.52 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[LEF1]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[RGS17]] | +0.54 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[GLDC]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.54 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TRBC2]] | +0.53 | +0.50 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAFD1]] | -0.47 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[LRRC27]] | -0.45 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[MYOF]] | -0.45 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[C1RL]] | -0.44 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[RBMS3]] | -0.44 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ANKH's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 4.5% of all compounds | 0.014 | ⚠ off-target possible; 4 compounds |
| [[TBC1D4]] | B | TBC1D4 activity raises ANKH's level | lines that do not express TBC1D4 (5) vs lines expressing it (45) | 3.24× lower at baseline in the lines without TBC1D4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZC3H12C, ZNF827 |
| [[LAPTM5]] | B | LAPTM5 activity raises ANKH's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without LAPTM5 | 0.099 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS17]] | B | ANKH activity raises RGS17's level | lines that do not express ANKH (6) vs lines expressing it (44) | 4.24× lower at baseline in the lines without ANKH | 0.019 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |
| [[UBASH3B]] | B | ANKH activity raises UBASH3B's level | lines that do not express ANKH (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without ANKH | 0.027 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |
| [[KLHL29]] | B | ANKH activity raises KLHL29's level | lines that do not express ANKH (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without ANKH | 0.046 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |
| [[TSPAN5]] | B | ANKH activity raises TSPAN5's level | lines that do not express ANKH (6) vs lines expressing it (44) | 3.08× lower at baseline in the lines without ANKH | 0.058 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.4, 5.6); signed map (9.5, 49.5). **Vector** length 111, 30.9% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +9.5 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +7.1 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.5 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.7 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.3 | -4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ANKH inorganic pyrophosphate transport regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:14,704,800-14,871,778 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HANK, ANK, CPPDD, SLC62A1; previously CCAL2, CMDJ |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 62 |
| Hallmark sets | ANDROGEN_RESPONSE, APOPTOSIS, KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCJ1](https://www.uniprot.org/uniprotkb/Q9HCJ1) (Mineralization regulator ANKH):

> Transports adenosine triphosphate (ATP) and possibly other nucleoside triphosphates (NTPs) from cytosol to the extracellular space. Mainly regulates their levels locally in peripheral tissues while playing a minor systemic role. Prevents abnormal ectopic mineralization of the joints by regulating the extracellular levels of the calcification inhibitor inorganic pyrophosphate (PPi), which originates from the conversion of extracellular NTPs to NMPs and PPis by ENPP1. Regulates the release of the …

**Summary**, from NCBI Gene [56172](https://www.ncbi.nlm.nih.gov/gene/56172):

> This gene encodes a multipass transmembrane protein that is expressed in joints and other tissues and controls pyrophosphate levels in cultured cells. Progressive ankylosis-mediated control of pyrophosphate levels has been suggested as a possible mechanism regulating tissue calcification and susceptibility to arthritis in higher animals. Mutations in this gene have been associated with autosomal dominant craniometaphyseal dysplasia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15492) · Entrez [56172](https://www.ncbi.nlm.nih.gov/gene/56172) · UniProt [Q9HCJ1](https://www.uniprot.org/uniprotkb/Q9HCJ1) · Ensembl [ENSG00000154122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154122)

## Data

Gene col 7772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7772); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7772]; `tensor/DDL_lfc|DDL_z.npy` [7772]; `embed/gene_vectors.npy` [7772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7772 or target_col == 7772). Every well: [[ANKH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
