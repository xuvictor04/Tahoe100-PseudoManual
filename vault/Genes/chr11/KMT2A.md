---
symbol: "KMT2A"
type: "gene"
col: 3962
ensembl_id: "ENSG00000118058"
name: "lysine methyltransferase 2A"
location: "11q23.3"
module: 74
arm: "+"
pooled_cpm: 281.52
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# KMT2A

*lysine methyltransferase 2A* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +33.2, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.636× (z -14.3, q 1e-43, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.783× (z -8.0, q 9e-14, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSF1]] (+0.76, fdr 7e-06), [[PNRC1]] (+0.70, fdr 7e-06), [[RRAGC]] (+0.69, fdr 7e-06); moves opposite to [[URB1]] (-0.66, fdr 7e-06), [[ADAT2]] (-0.63, fdr 9e-06), [[ZNF587B]] (-0.62, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MARCKS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +33.2 | 0e+00 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +18.2 | 0e+00 | 41/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.47×** | +12.6 | 3e-34 | 34/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +10.2 | 2e-22 | 30/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +9.9 | 4e-21 | 30/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +4.4 | 1e-03 | 16/48 (KATO III, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.14× | +4.4 | 1e-03 | 11/49 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.14× | +4.2 | 0.002 | 12/47 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 24/49 (HEC-1-A, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +4.1 | 0.002 | 4/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.006 | 15/48 (Hs 766T, NCI-H1792, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.12× | +3.8 | 0.006 | 6/50 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.007 | 24/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.12× | +3.7 | 0.008 | 17/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.08× | +3.6 | 0.012 | 3/48 (SNU-1, RKO, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.023 | 9/48 (LS 180, HOP62, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.09× | +3.2 | 0.031 | 4/48 (MIA PaCa-2, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.049 | 12/47 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.07× | +3.1 | 0.055 | 3/48 (RKO, CHP-212, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -14.3 | 1e-43 | 36/44 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.659×** | -13.7 | 5e-40 | 37/49 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -12.6 | 6e-34 | 42/45 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.721×** | -10.7 | 1e-24 | 41/48 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.715×** | -10.6 | 4e-24 | 34/47 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -8.0 | 9e-14 | 29/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.638×** | -7.7 | 1e-12 | 39/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.842× | -5.6 | 1e-06 | 21/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | 0.857× | -5.1 | 2e-05 | 21/48 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.897× | -5.0 | 2e-05 | 10/48 (A549, SNU-423, …) | top dose only | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.745×** | -5.0 | 2e-05 | 33/48 (PANC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.746×** | -5.0 | 2e-05 | 34/48 (PANC-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.808×** | -5.0 | 3e-05 | 24/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.829×** | -4.4 | 4e-04 | 18/49 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.839× | -4.1 | 0.001 | 21/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.796×** | -3.9 | 0.003 | 22/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.800×** | -3.8 | 0.004 | 24/48 (CFPAC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.897× | -3.4 | 0.017 | 9/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[Saquinavir (drug)]] 0.5 µM |  | 0.906× | -3.3 | 0.032 | 5/48 (hTERT-HPNE, COLO 205, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.907× | -3.0 | 0.074 | 7/48 (SW 900, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | 0.846× | -2.9 | 0.099 | 15/47 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 237 | 5 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +29.1) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 336 | 5 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +18.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -17.8) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.526× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 253 | 4 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +24.0) | [[Dinaciclib (drug)]] 5 µM 0.516× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.647× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 178 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +25.5) | — |
| [[PANC-1 (line)]] | alt | 496 | 7 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +40.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.616× (z -11.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.493× (z -8.6) |
| [[A498 (line)]] | wt | 278 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +34.2) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 286 | 3 | 5 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.70× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.553× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 221 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +27.1) | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -11.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 329 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 354 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.588× (z -11.1) |
| [[HS-578T (line)]] | alt | 275 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 410 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +31.3) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -17.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 344 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -17.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 417 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +18.6) | [[Auranofin (drug)]] 5 µM 0.552× (z -10.5) |
| [[H4 (line)]] | wt | 301 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +26.9) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -10.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 308 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +20.2) | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -13.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 198 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +23.0) | — |
| [[SNU-423 (line)]] | alt | 301 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +18.9) | [[Dinaciclib (drug)]] 0.05 µM 0.507× (z -12.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 190 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.3) | — |
| [[J82 (line)]] | alt | 216 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +29.8) | — |
| [[KATO III (line)]] | alt | 409 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -24.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 231 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.536× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 149 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.78× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 5 µM 0.427× (z -12.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 299 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +26.6) | [[Dinaciclib (drug)]] 0.5 µM 0.607× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 301 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +22.7) | — |
| [[HOP62 (line)]] | alt | 200 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +22.9) | — |
| [[HT-29 (line)]] | alt | 309 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.583× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 341 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 213 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +17.3) | — |
| [[Panc 03.27 (line)]] | alt | 304 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +12.3) | [[Lonafarnib (drug)]] 5 µM 0.258× (z -13.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 177 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.4) | — |
| [[HepG2_C3A (line)]] | wt | 182 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +25.8) | — |
| [[LS 180 (line)]] | wt | 211 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +11.4) | — |
| [[SW48 (line)]] | wt | 213 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -10.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 264 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -12.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 246 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 337 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 291 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.511× (z -11.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 192 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 233 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.619× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 238 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -13.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 270 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 288 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.629× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 320 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +13.6) | — |
| [[AN3 CA (line)]] | alt | 368 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 320 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSF1]] | +0.76 | +0.68 / +0.79 | both halves | 7e-06 | same gene group |
| [[PNRC1]] | +0.70 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.69 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[CEP350]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CIR1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[WDR48]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[PHF3]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 | same gene group |
| [[OPTN]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZBTB20]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 | STRING 407 |
| [[NBR1]] | +0.64 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[OTUD1]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | -0.66 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[ADAT2]] | -0.63 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[ZNF587B]] | -0.62 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.62 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[RNPS1]] | -0.62 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[TRNT1]] | -0.61 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[WDR4]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.60 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[CHID1]] | -0.60 | -0.62 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCKS]] | B | MARCKS activity raises KMT2A's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without MARCKS | 0.004 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.9, -44.8); signed map (-7.4, 10.5). **Vector** length 141, 46.3% of its response variance represented; |z| ≥ 3 in 1,288 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +18.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +33.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.8 | +12.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.7 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.2 | +4.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.1 | +3.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +4.9 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.8 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.6 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -12.6 |
|  | [[EX229 (drug)]] 5 µM |  | -7.1 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.8 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.8 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | lysine methyltransferase 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,436,456-118,526,832 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRX1, HRX, ALL-1, HTRX1, CXXC7, MLL1A, MLL1, ALL1; previously MLL |
| Gene groups (HGNC) | PHD finger proteins; Zinc fingers CXXC-type; Histone lysine methyltransferases; Bromodomain containing; SET domain containing |
| Reactome | 23 pathways, smallest: Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex; Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03164](https://www.uniprot.org/uniprotkb/Q03164) (Histone-lysine N-methyltransferase 2A):

> Histone methyltransferase that plays an essential role in early development and hematopoiesis. Catalytic subunit of the MLL1/MLL complex, a multiprotein complex that mediates both methylation of 'Lys-4' of histone H3 (H3K4me) complex and acetylation of 'Lys-16' of histone H4 (H4K16ac). Catalyzes methyl group transfer from S-adenosyl-L-methionine to the epsilon-amino group of 'Lys-4' of histone H3 (H3K4) via a non-processive mechanism. Part of chromatin remodeling machinery predominantly forms …

**Summary**, from NCBI Gene [4297](https://www.ncbi.nlm.nih.gov/gene/4297):

> This gene encodes a transcriptional coactivator that plays an essential role in regulating gene expression during early development and hematopoiesis. The encoded protein contains multiple conserved functional domains. One of these domains, the SET domain, is responsible for its histone H3 lysine 4 (H3K4) methyltransferase activity which mediates chromatin modifications associated with epigenetic transcriptional activation. This protein is processed by the enzyme Taspase 1 into two fragments, …

**Accessions** — [HGNC:7132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7132) · Entrez [4297](https://www.ncbi.nlm.nih.gov/gene/4297) · UniProt [Q03164](https://www.uniprot.org/uniprotkb/Q03164) · Ensembl [ENSG00000118058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118058)

## Data

Gene col 3962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3962); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3962]; `tensor/DDL_lfc|DDL_z.npy` [3962]; `embed/gene_vectors.npy` [3962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3962 or target_col == 3962). Every well: [[KMT2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KMT2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
