---
symbol: "RAB3B"
type: "gene"
col: 9772
ensembl_id: "ENSG00000169213"
name: "RAB3B, member RAS oncogene family"
location: "1p32.3"
module: 116
arm: "+"
pooled_cpm: 50.18
n_lines_expressing: 33
n_dd_up: 34
n_dd_down: 43
n_dd_up_clean: 22
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# RAB3B

*RAB3B, member RAS oncogene family* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.79× (z +21.5, q 0e+00, up in 23 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 3.04× (z +18.0, q 0e+00, up in 27 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.668× (z -6.4, q 4e-08, down in 17 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK4]] (+0.65, fdr 1e-05), [[LCP1]] (+0.63, fdr 1e-05), [[PLCXD2]] (+0.62, fdr 1e-05); moves opposite to [[RBKS]] (-0.52, fdr 6e-05), [[WTAP]] (-0.50, fdr 2e-04), [[RAF1]] (-0.50, fdr 1e-04).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CCN2]] → it (grade B ⚠); 8 go from it, the strongest it → [[CORO2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +21.5 | 0e+00 | 23/28 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +19.7 | 0e+00 | 22/25 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.04×** | +18.0 | 0e+00 | 27/31 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.94×** | +17.4 | 0e+00 | 29/31 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +15.2 | 0e+00 | 20/28 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +13.3 | 2e-38 | 19/31 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.18×** | +12.6 | 2e-34 | 23/31 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.76×** | +9.1 | 7e-18 | 19/30 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +9.0 | 1e-17 | 19/31 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +8.4 | 2e-15 | 23/31 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.72×** | +8.4 | 2e-15 | 22/30 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.44×** | +8.3 | 5e-15 | 20/31 (HOP62, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +8.2 | 1e-14 | 19/31 (LoVo, C-33 A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.66×** | +8.2 | 1e-14 | 19/31 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.57×** | +7.3 | 1e-11 | 19/30 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +6.9 | 2e-10 | 18/30 (SW1417, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.52×** | +6.7 | 5e-10 | 20/30 (HOP62, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 4e-06 | 14/31 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.1 | 7e-06 | 15/30 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +5.1 | 9e-06 | 15/31 (PANC-1, HOP62, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 4e-04 | 10/31 (LoVo, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 2 with an alert ⚠; shown: the 15 strongest. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.668×** | -6.4 | 4e-08 | 17/32 (NCI-H460, NCI-H596, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.676×** | -6.4 | 4e-08 | 17/31 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.665×** | -6.4 | 4e-08 | 19/30 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.680×** | -5.8 | 1e-06 | 14/31 (NCI-H460, HepG2/C3A, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.783×** | -5.6 | 2e-06 | 15/31 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.787×** | -5.4 | 7e-06 | 12/31 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.0 | 6e-05 | 18/31 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.727×** | -4.9 | 6e-05 | 18/31 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.763×** | -4.9 | 7e-05 | 15/31 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.742×** | -4.8 | 8e-05 | 15/31 (A498, SHP-77, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.814×** | -4.7 | 1e-04 | 14/31 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.745×** | -4.5 | 3e-04 | 15/31 (HepG2/C3A, NCI-H460, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.577×** | -4.5 | 4e-04 | 11/31 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.763×** | -4.4 | 5e-04 | 13/31 (A-172, HCT15, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.768×** | -4.3 | 7e-04 | 15/30 (HepG2/C3A, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 419 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -25.2) |
| [[HepG2_C3A (line)]] | wt | 209 | 0 | 11 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -21.5) |
| [[LoVo (line)]] | wt | 17.0 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.04× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 17.8 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.71× (z +14.5) | — |
| [[RKO (line)]] | wt | 104 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -16.3) |
| [[SW480 (line)]] | alt | 23.2 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.18× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.98× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 96.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.12× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 160 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 72.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +14.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 71.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +14.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 56.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +10.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 30.2 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.06× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 21.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 47.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 21.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.00× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 66.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.12× (z +9.5) | — |
| [[A-172 (line)]] | wt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 42.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 18.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.87× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.40× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 45.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.9) |
| [[NCI-H596 (line)]] | alt | 66.8 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.173× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.95 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.88 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.57 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.37 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK4]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[LCP1]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PLCXD2]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ESM1]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[SERPIND1]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[PKIA]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[NRIP3]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[MMP1]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[UNC5D]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[IL31RA]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ANOS1]] | +0.57 | +0.40 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBKS]] | -0.52 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[WTAP]] | -0.50 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[RAF1]] | -0.50 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[CEBPD]] | -0.50 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[MAIP1]] | -0.50 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[PUS10]] | -0.49 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CDKN1B]] | -0.48 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[APOLD1]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN2]] | B | CCN2 activity raises RAB3B's level | lines that do not express CCN2 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without CCN2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, CPEB1, TRIML2 |
| [[LAMA1]] | B | LAMA1 activity raises RAB3B's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without LAMA1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[ESM1]] | B | ESM1 activity raises RAB3B's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.10× lower at baseline in the lines without ESM1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CORO2B]] | B | RAB3B activity raises CORO2B's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 2.72× lower at baseline in the lines without RAB3B | 0.011 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[PIK3CD]] | B | RAB3B activity raises PIK3CD's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 2.31× lower at baseline in the lines without RAB3B | 0.051 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[EIF5A2]] | B | RAB3B activity raises EIF5A2's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without RAB3B | 0.054 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[MAPK8]] | B | RAB3B activity raises MAPK8's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.28× lower at baseline in the lines without RAB3B | 0.063 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[CSGALNACT2]] | B | RAB3B activity raises CSGALNACT2's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without RAB3B | 0.064 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[CCN2]] | B | RAB3B activity raises CCN2's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 2.54× lower at baseline in the lines without RAB3B | 0.069 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[SEMA4F]] | B | RAB3B activity raises SEMA4F's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without RAB3B | 0.075 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[C3orf52]] | B | RAB3B activity lowers C3orf52's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.33× higher at baseline in the lines without RAB3B | 0.092 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.0, 13.6); signed map (3.7, 53.8). **Vector** length 107, 28.4% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +21.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +19.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +13.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +18.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +8.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +8.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.2 | +5.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -5.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.7 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -4.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.7 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB3B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:51,907,956-51,990,700 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P20337](https://www.uniprot.org/uniprotkb/P20337) (Ras-related protein Rab-3B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion.

**Summary**, from NCBI Gene [5865](https://www.ncbi.nlm.nih.gov/gene/5865):

> Enables G protein activity; GDP binding activity; and myosin V binding activity. Involved in several processes, including positive regulation of dopamine uptake involved in synaptic transmission; regulation of synaptic vesicle cycle; and regulation of vesicle size. Located in perinuclear region of cytoplasm and vesicle. Is active in dopaminergic synapse and synaptic vesicle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9778) · Entrez [5865](https://www.ncbi.nlm.nih.gov/gene/5865) · UniProt [P20337](https://www.uniprot.org/uniprotkb/P20337) · Ensembl [ENSG00000169213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169213)

## Data

Gene col 9772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9772); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9772]; `tensor/DDL_lfc|DDL_z.npy` [9772]; `embed/gene_vectors.npy` [9772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9772 or target_col == 9772). Every well: [[RAB3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
