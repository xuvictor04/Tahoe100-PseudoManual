---
symbol: "SKIL"
type: "gene"
col: 5882
ensembl_id: "ENSG00000136603"
name: "SKI like proto-oncogene"
location: "3q26.2"
module: 30
arm: "-"
pooled_cpm: 133.25
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 23
n_dd_up_clean: 18
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SKIL

*SKI like proto-oncogene* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.39× (z +36.0, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.538× (z -10.6, q 1e-23, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEZF1]] (+0.70, fdr 7e-06), [[PNRC2]] (+0.69, fdr 7e-06), [[ZC3H11A]] (+0.69, fdr 1e-05); moves opposite to [[MMS19]] (-0.74, fdr 7e-06), [[NDUFAF7]] (-0.73, fdr 7e-06), [[VDAC3]] (-0.70, fdr 1e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.39×** | +36.0 | 0e+00 | 45/46 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.30×** | +24.1 | 0e+00 | 45/46 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.85×** | +18.0 | 0e+00 | 41/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +12.3 | 2e-32 | 42/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +6.1 | 1e-07 | 25/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.8 | 5e-07 | 27/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 2e-06 | 36/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.24×** | +5.3 | 1e-05 | 27/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +4.9 | 5e-05 | 29/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 1e-04 | 30/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 27/46 (HEC-1-A, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 6e-04 | 24/46 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +3.8 | 0.007 | 25/46 (C-33 A, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.011 | 20/47 (A-172, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.016 | 20/47 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.025 | 22/46 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.15× | +3.4 | 0.027 | 13/47 (C-33 A, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.538×** | -10.6 | 1e-23 | 40/46 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.551×** | -10.2 | 5e-22 | 40/46 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.553×** | -10.2 | 5e-22 | 41/46 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[NG25 (drug)]] 5 µM |  | **0.347×** | -9.5 | 3e-19 | 44/45 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.627×** | -8.0 | 1e-13 | 35/46 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -6.3 | 3e-08 | 33/46 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.719×** | -5.6 | 1e-06 | 34/46 (NCI-H1573, SW48, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -5.6 | 2e-06 | 32/46 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -5.3 | 8e-06 | 27/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.571×** | -5.0 | 3e-05 | 21/36 (SW480, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.572×** | -5.0 | 3e-05 | 28/43 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.821×** | -4.8 | 8e-05 | 23/46 (AsPC-1, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.821×** | -4.8 | 8e-05 | 23/46 (COLO 205, HT-29, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.710×** | -4.2 | 0.001 | 25/46 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.792×** | -4.0 | 0.003 | 25/46 (HT-29, LS 180, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.728×** | -3.9 | 0.004 | 26/46 (SK-MEL-2, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.799×** | -3.8 | 0.004 | 22/47 (LS 180, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.663×** | -3.7 | 0.007 | 25/46 (PANC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 234 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.342× (z -13.3) |
| [[SW480 (line)]] | alt | 135 | 5 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +22.6) | [[Panobinostat (drug)]] 0.5 µM 0.507× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 52.4 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +32.1) | — |
| [[BT-474 (line)]] | alt | 74.1 | 4 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.267× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.356× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 275 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +30.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.285× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.435× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 183 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +25.1) | [[Ixazomib citrate (drug)]] 5 µM 0.336× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 188 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +18.5) | [[Belinostat (drug)]] 5 µM 0.316× (z -11.7) |
| [[A-172 (line)]] | wt | 139 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +26.9) | — |
| [[NCI-H2347 (line)]] | alt | 110 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +26.2) | — |
| [[SW 900 (line)]] | alt | 120 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.358× (z -9.6) |
| [[A498 (line)]] | wt | 144 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +28.2) | [[Bortezomib (drug)]] 0.05 µM 0.469× (z -9.1) |
| [[A549 (line)]] | wt | 175 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +24.7) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 131 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +21.4) | [[Panobinostat (drug)]] 5 µM 0.425× (z -9.4) |
| [[C32 (line)]] | wt | 43.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +19.5) | — |
| [[HEC-1-A (line)]] | alt | 152 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +25.1) | — |
| [[J82 (line)]] | alt | 179 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +34.5) | [[NG25 (drug)]] 5 µM 0.285× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 171 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.8) | [[Ixazomib citrate (drug)]] 5 µM 0.341× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 264 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +26.7) | [[Panobinostat (drug)]] 5 µM 0.491× (z -8.6) |
| [[PANC-1 (line)]] | alt | 150 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +35.0) | — |
| [[CFPAC-1 (line)]] | alt | 148 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +45.9) | — |
| [[HOP62 (line)]] | alt | 116 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +27.3) | — |
| [[HS-578T (line)]] | alt | 114 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 300 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.7) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.359× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 102 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 98.0 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 157 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +25.8) | — |
| [[SK-MEL-2 (line)]] | alt | 190 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +37.3) | — |
| [[H4 (line)]] | wt | 117 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +19.2) | [[Ixazomib citrate (drug)]] 5 µM 0.244× (z -10.1) |
| [[KATO III (line)]] | alt | 87.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +29.8) | — |
| [[LoVo (line)]] | wt | 84.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +21.4) | — |
| [[NCI-H2030 (line)]] | alt | 126 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +23.5) | — |
| [[NCI-H23 (line)]] | alt | 81.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +18.2) | [[Belinostat (drug)]] 5 µM 0.376× (z -9.0) |
| [[RKO (line)]] | wt | 74.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 147 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +24.0) | — |
| [[COLO 205 (line)]] | alt | 153 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +21.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.82× (z +25.5) | — |
| [[SW48 (line)]] | wt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +13.1) | — |
| [[AN3 CA (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -8.6) ⚠ cell-cycle shift, explains ~91% of this change |
| [[C-33 A (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0692× (z -9.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 61.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.9) | — |
| [[SW 1088 (line)]] | alt | 83.4 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.0743× (z -8.5) |
| [[SW 1271 (line)]] | alt | 243 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PNRC2]] | +0.69 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[ZC3H11A]] | +0.69 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ZNF641]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[LEKR1]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[FKRP]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.65 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[JUNB]] | +0.65 | +0.66 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[C21orf91]] | +0.64 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[HIVEP2]] | +0.64 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ST7L]] | +0.63 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[KLF10]] | +0.63 | +0.69 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMS19]] | -0.74 | -0.76 / -0.62 | both halves | 7e-06 |  |
| [[NDUFAF7]] | -0.73 | -0.74 / -0.70 | both halves | 7e-06 |  |
| [[VDAC3]] | -0.70 | -0.74 / -0.57 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.69 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[SHQ1]] | -0.68 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.68 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[ECI2]] | -0.67 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.67 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[KLHDC10]] | -0.67 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[SCAI]] | -0.67 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[ALG9]] | -0.67 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.67 | -0.67 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers SKIL's level | compounds that target MTOR: 4 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Temsirolimus) | 50% of the class's compounds vs 3.6% of all compounds | 0.058 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.9, -14.0); signed map (15.0, -10.3). **Vector** length 147, 48.2% of its response variance represented; |z| ≥ 3 in 1,574 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +15.5 | +24.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +12.0 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.6 | +36.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.8 | +18.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -8.7 | -8.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.3 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.8 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.6 | -5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.5 | -4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SKI like proto-oncogene |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:170,357,342-170,396,835 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNO, SnoN, SnoA |
| Gene groups (HGNC) | SKI transcriptional corepressors |
| Hallmark sets | TGF_BETA_SIGNALING, KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Downregulation of SMAD2/3:SMAD4 transcriptional activity; Transcriptional activity of SMAD2/SMAD3:SMAD4 heterotrimer; Signaling by TGF-beta Receptor Complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P12757](https://www.uniprot.org/uniprotkb/P12757) (Ski-like protein):

> May have regulatory role in cell division or differentiation in response to extracellular signals.

**Summary**, from NCBI Gene [6498](https://www.ncbi.nlm.nih.gov/gene/6498):

> The protein encoded by this gene is a component of the SMAD pathway, which regulates cell growth and differentiation through transforming growth factor-beta (TGFB). In the absence of ligand, the encoded protein binds to the promoter region of TGFB-responsive genes and recruits a nuclear repressor complex. TGFB signaling causes SMAD3 to enter the nucleus and degrade this protein, allowing these genes to be activated. Four transcript variants encoding three different isoforms have been found for …

**Accessions** — [HGNC:10897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10897) · Entrez [6498](https://www.ncbi.nlm.nih.gov/gene/6498) · UniProt [P12757](https://www.uniprot.org/uniprotkb/P12757) · Ensembl [ENSG00000136603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136603)

## Data

Gene col 5882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5882); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5882]; `tensor/DDL_lfc|DDL_z.npy` [5882]; `embed/gene_vectors.npy` [5882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5882 or target_col == 5882). Every well: [[SKIL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKIL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
