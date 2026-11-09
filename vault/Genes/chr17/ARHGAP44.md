---
symbol: "ARHGAP44"
type: "gene"
col: 127
ensembl_id: "ENSG00000006740"
name: "Rho GTPase activating protein 44"
location: "17p12"
module: 115
arm: "+"
pooled_cpm: 24.82
n_lines_expressing: 34
n_dd_up: 15
n_dd_down: 30
n_dd_up_clean: 12
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 7
direction_downstream: 24
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# ARHGAP44

*Rho GTPase activating protein 44* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +22.8, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.404× (z -29.1, q 0e+00, down in 28 of 31 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.361× (z -23.2, q 0e+00, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00937]] (+0.70, fdr 7e-06), [[CAMK2G]] (+0.68, fdr 1e-05), [[TSPAN33]] (+0.67, fdr 1e-05); moves opposite to [[PCF11]] (-0.61, fdr 3e-05), [[RFX3-DT]] (-0.60, fdr 5e-05), [[METTL6]] (-0.60, fdr 3e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FRMPD3]] → it (grade B ⚠); 24 go from it, the strongest it → [[PACC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +22.8 | 0e+00 | 30/32 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.49×** | +20.8 | 0e+00 | 31/32 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +18.3 | 0e+00 | 24/32 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +17.9 | 0e+00 | 20/32 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +17.0 | 0e+00 | 29/30 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +16.4 | 0e+00 | 26/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +11.7 | 7e-30 | 24/29 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.35×** | +10.2 | 2e-22 | 22/32 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.36×** | +6.6 | 3e-09 | 10/29 (KATO III, A549, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.34×** | +6.5 | 5e-09 | 12/30 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +5.9 | 2e-07 | 12/32 (RKO, LS 180, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.43×** | +5.8 | 3e-07 | 12/32 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.62×** | +5.7 | 5e-07 | 11/27 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 4/30 (SHP-77, NCI-H2030, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.002 | 11/30 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.6 | 0.012 | 8/31 (LS 180, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.4 | 0.021 | 8/32 (LS 180, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.022 | 12/31 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.404×** | -29.1 | 0e+00 | 28/31 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -23.8 | 0e+00 | 29/30 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.361×** | -23.2 | 0e+00 | 27/30 (HS-578T, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.369×** | -22.7 | 0e+00 | 31/32 (NCI-H2030, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.383×** | -21.0 | 0e+00 | 26/31 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.424×** | -19.5 | 0e+00 | 29/32 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.460×** | -17.7 | 0e+00 | 28/31 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.484×** | -16.5 | 0e+00 | 25/31 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.497×** | -15.9 | 0e+00 | 27/32 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -9.9 | 2e-21 | 20/28 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.648×** | -9.9 | 3e-21 | 20/31 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -9.8 | 7e-21 | 23/31 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.679×** | -8.8 | 6e-17 | 24/32 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.715×** | -7.7 | 8e-13 | 21/32 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -7.5 | 2e-12 | 17/29 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.782×** | -5.6 | 6e-07 | 11/32 (LS 180, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -5.4 | 2e-06 | 14/32 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.803×** | -4.6 | 1e-04 | 13/29 (AN3 CA, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 56.7 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -21.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.165× (z -18.4) |
| [[HS-578T (line)]] | alt | 58.7 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -23.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -21.2) |
| [[LoVo (line)]] | wt | 31.1 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -27.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.120× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -20.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 53.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -36.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.164× (z -15.9) |
| [[SNU-1 (line)]] | wt | 53.7 | 0 | 11 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0292× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0753× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 13.7 | 6 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.63× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.245× (z -9.8) |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -17.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -12.4) |
| [[KATO III (line)]] | alt | 64.2 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -15.9) |
| [[SW480 (line)]] | alt | 16.0 | 3 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.48× (z +15.0) | [[Auranofin (drug)]] 5 µM 0.202× (z -13.6) |
| [[A549 (line)]] | wt | 23.2 | 1 (1 ⚠) | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 5 µM 0.131× (z -13.7) |
| [[A-427 (line)]] | wt | 87.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -22.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -20.5) |
| [[A498 (line)]] | wt | 24.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -20.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -15.1) |
| [[LS 180 (line)]] | wt | 67.2 | 3 (3 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.198× (z -8.7) |
| [[RKO (line)]] | wt | 34.6 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.140× (z -13.1) |
| [[C-33 A (line)]] | alt | 84.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -12.1) |
| [[HCT15 (line)]] | alt | 69.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -25.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 50.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -14.4) |
| [[PANC-1 (line)]] | alt | 6.78 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.18× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 79.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -10.7) |
| [[SW48 (line)]] | wt | 77.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0526× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -11.0) |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -9.9) |
| [[A-172 (line)]] | wt | 7.62 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -9.6) |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0828× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 8.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00937]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[CAMK2G]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[PRKCQ]] | +0.66 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[ARHGEF26]] | +0.65 | +0.48 / +0.70 | both halves | 2e-05 | pathway: CDC42 GTPase cycle |
| [[REPS1]] | +0.65 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[HACE1]] | +0.64 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SBK1]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[WASF3]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 | pathway: RAC1 GTPase cycle |
| [[CMTM8]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[L2HGDH]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCF11]] | -0.61 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[RFX3-DT]] | -0.60 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[METTL6]] | -0.60 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[INO80D]] | -0.59 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | -0.59 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[TRMT13]] | -0.59 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LINC01004]] | -0.59 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[THAP2]] | -0.58 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[UBE3B]] | -0.57 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[CHD1-DT]] | -0.57 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ERCC6L2-AS1]] | -0.57 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[DNAI4]] | -0.57 | -0.38 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMPD3]] | B | FRMPD3 activity lowers ARHGAP44's level | lines that do not express FRMPD3 (18) vs lines expressing it (32) | 1.79× higher at baseline in the lines without FRMPD3 | 0.028 | ⚠ within organs, on part of the lines; also absent: CACNG4, NSUN7, GYG2; maybe low, not absent |
| [[PARM1]] | B | PARM1 activity raises ARHGAP44's level | lines that do not express PARM1 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without PARM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A |
| [[PAX2]] | B | PAX2 activity raises ARHGAP44's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without PAX2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[REEP1]] | B | REEP1 activity raises ARHGAP44's level | lines that do not express REEP1 (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without REEP1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[RIMS3]] | B | RIMS3 activity raises ARHGAP44's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without RIMS3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[SEMA6B]] | B | SEMA6B activity raises ARHGAP44's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without SEMA6B | 0.080 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[CECR2]] | B | CECR2 activity raises ARHGAP44's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without CECR2 | 0.098 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 24, C 0. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PACC1]] | B | ARHGAP44 activity raises PACC1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.65× lower at baseline in the lines without ARHGAP44 | 0.005 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[ADGRL1]] | B | ARHGAP44 activity raises ADGRL1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without ARHGAP44 | 0.007 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[SSBP4]] | B | ARHGAP44 activity raises SSBP4's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without ARHGAP44 | 0.021 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[KIF26A]] | B | ARHGAP44 activity raises KIF26A's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.89× lower at baseline in the lines without ARHGAP44 | 0.025 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[RNF130]] | B | ARHGAP44 activity raises RNF130's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.29× lower at baseline in the lines without ARHGAP44 | 0.032 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[LINC00937]] | B | ARHGAP44 activity raises LINC00937's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without ARHGAP44 | 0.035 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[STOX2]] | B | ARHGAP44 activity raises STOX2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without ARHGAP44 | 0.038 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[ASIC1]] | B | ARHGAP44 activity raises ASIC1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without ARHGAP44 | 0.038 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[SEPTIN3]] | B | ARHGAP44 activity raises SEPTIN3's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without ARHGAP44 | 0.039 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[STRBP]] | B | ARHGAP44 activity raises STRBP's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without ARHGAP44 | 0.047 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[TFDP2]] | B | ARHGAP44 activity raises TFDP2's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without ARHGAP44 | 0.053 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[SLC29A2]] | B | ARHGAP44 activity strengthens SLC29A2's drug response | lines that do not express ARHGAP44 (9) vs lines expressing it (25) | the lines without ARHGAP44 respond 0.56× as strongly (z diff +2.04); strongest at Homoharringtonine 5 µM: 0.35x vs 0.26x (z diff +3.1) | 0.058 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.5, 37.7); signed map (-22.4, 37.6). **Vector** length 90.1, 20.9% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +22.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +17.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +20.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | +4.0 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +5.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -23.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.9 | -29.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -21.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -16.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -7.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:12,789,498-12,991,643 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0672, RICH-2, RICH2 |
| Gene groups (HGNC) | N-BAR domain containing; AH/BAR family Rho GTPase activating proteins |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17R89](https://www.uniprot.org/uniprotkb/Q17R89) (Rho GTPase-activating protein 44):

> GTPase-activating protein (GAP) that stimulates the GTPase activity of Rho-type GTPases. Thereby, controls Rho-type GTPases cycling between their active GTP-bound and inactive GDP-bound states. Acts as a GAP at least for CDC42 and RAC1. In neurons, is involved in dendritic spine formation and synaptic plasticity in a specific RAC1-GAP activity (By similarity). Limits the initiation of exploratory dendritic filopodia. Recruited to actin-patches that seed filopodia, binds specifically to plasma …

**Summary**, from NCBI Gene [9912](https://www.ncbi.nlm.nih.gov/gene/9912):

> Enables phospholipid binding activity. Predicted to be involved in negative regulation of Rac protein signal transduction; regulation of actin cytoskeleton organization; and regulation of plasma membrane bounded cell projection organization. Located in leading edge membrane. Implicated in acquired immunodeficiency syndrome and skin melanoma. Biomarker of hepatocellular carcinoma and lung carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29096) · Entrez [9912](https://www.ncbi.nlm.nih.gov/gene/9912) · UniProt [Q17R89](https://www.uniprot.org/uniprotkb/Q17R89) · Ensembl [ENSG00000006740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006740)

## Data

Gene col 127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 127); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 127]; `tensor/DDL_lfc|DDL_z.npy` [127]; `embed/gene_vectors.npy` [127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 127 or target_col == 127). Every well: [[ARHGAP44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
