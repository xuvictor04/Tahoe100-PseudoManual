---
symbol: "SPIDR"
type: "gene"
col: 9008
ensembl_id: "ENSG00000164808"
name: "scaffold protein involved in DNA repair"
location: "8q11.21"
module: 4
arm: "+"
pooled_cpm: 250.98
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SPIDR

*scaffold protein involved in DNA repair* — 8q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.20× (z +12.3, q 7e-32, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -18.5, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.517× (z -14.5, q 6e-45, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSRC1]] (+0.65, fdr 7e-06), [[FAF1]] (+0.65, fdr 2e-05), [[SPATA5]] (+0.65, fdr 7e-06); moves opposite to [[ZNF425]] (-0.69, fdr 2e-05), [[THAP2]] (-0.66, fdr 3e-05), [[MALINC1]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[WWOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +12.3 | 7e-32 | 47/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +9.7 | 1e-19 | 41/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.2 | 3e-14 | 40/48 (AsPC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 7e-04 | 34/48 (SHP-77, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.5 | 7e-04 | 31/47 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 0.002 | 38/48 (SHP-77, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.007 | 28/48 (RKO, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.022 | 26/48 (SHP-77, NCI-H2347, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.025 | 28/50 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.096 | 24/48 (hTERT-HPNE, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.096 | 20/48 (AsPC-1, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.430×** | -18.5 | 0e+00 | 44/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -14.5 | 6e-45 | 48/49 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -13.5 | 5e-39 | 46/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.440×** | -12.7 | 6e-35 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.451×** | -12.4 | 5e-33 | 41/48 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.495×** | -10.9 | 1e-25 | 46/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.485×** | -10.8 | 3e-25 | 44/48 (NCI-H23, NCI-H2030, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.303×** | -9.7 | 2e-20 | 48/49 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -7.9 | 1e-13 | 43/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.605×** | -7.8 | 4e-13 | 43/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -7.3 | 2e-11 | 43/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -7.2 | 3e-11 | 39/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -6.3 | 1e-08 | 33/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.651×** | -5.6 | 8e-07 | 32/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.708×** | -5.1 | 1e-05 | 27/44 (HCT15, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -4.8 | 6e-05 | 30/49 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -4.7 | 9e-05 | 34/50 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.003 | 26/48 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.860× | -3.3 | 0.028 | 14/49 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.863× | -3.2 | 0.035 | 6/49 (KATO III, HCT15, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.817×** | -3.1 | 0.042 | 23/48 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 365 | 0 | 16 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -18.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 405 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -35.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -23.8) |
| [[SHP-77 (line)]] | alt | 396 | 13 | 1 | [[Triamcinolone (drug)]] 0.5 µM 2.10× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 192 | 2 | 10 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -19.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -14.4) |
| [[RKO (line)]] | wt | 368 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -12.5) |
| [[SW48 (line)]] | wt | 251 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -11.5) |
| [[SW480 (line)]] | alt | 288 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -15.9) |
| [[C32 (line)]] | wt | 282 | 1 | 8 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -23.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 206 | 2 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -22.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -15.8) |
| [[PANC-1 (line)]] | alt | 297 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -23.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -16.8) |
| [[A-427 (line)]] | wt | 353 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -17.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 202 | 1 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -9.7) |
| [[HT-29 (line)]] | alt | 218 | 1 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -11.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -10.9) |
| [[KATO III (line)]] | alt | 334 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -18.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -15.3) |
| [[LoVo (line)]] | wt | 278 | 1 | 7 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.402× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 131 | 1 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -24.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 246 | 1 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 241 | 1 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -18.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 428 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -21.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -19.1) |
| [[SK-MEL-2 (line)]] | alt | 219 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -16.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.8) |
| [[SW 900 (line)]] | alt | 257 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.313× (z -12.4) |
| [[A549 (line)]] | wt | 296 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -15.4) |
| [[C-33 A (line)]] | alt | 344 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.8) |
| [[HOP62 (line)]] | alt | 197 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -10.4) |
| [[LS 180 (line)]] | wt | 216 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -15.4) |
| [[SW1417 (line)]] | alt | 153 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -13.8) |
| [[A498 (line)]] | wt | 370 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 168 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.16× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.396× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.443× (z -8.6) |
| [[COLO 205 (line)]] | alt | 322 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -18.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -14.2) |
| [[HCT15 (line)]] | alt | 430 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -13.7) |
| [[J82 (line)]] | alt | 240 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -12.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.4) |
| [[HS-578T (line)]] | alt | 183 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 135 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.21× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.4) |
| [[SNU-1 (line)]] | wt | 319 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -10.9) |
| [[AN3 CA (line)]] | alt | 361 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -20.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 161 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 169 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.7) |
| [[Hs 766T (line)]] | wt | 126 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 112 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +13.3) | — |
| [[A-172 (line)]] | wt | 155 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 211 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -9.3) |
| [[CHP-212 (line)]] | wt | 168 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 219 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.411× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 136 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +10.6) | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.185× (z -9.9) |
| [[NCI-H661 (line)]] | alt | 245 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -8.7) |
| [[SNU-423 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 1271 (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.178× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H2122 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 201 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRC1]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[FAF1]] | +0.65 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[SPATA5]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[CDIN1]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[STK3]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[HERC2]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |
| [[TTLL5]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MIPOL1]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[RABGAP1L]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MSH3]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF425]] | -0.69 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[THAP2]] | -0.66 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[MALINC1]] | -0.64 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[UPP2]] | -0.64 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CFAP53]] | -0.63 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZNF547]] | -0.62 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[LRP2BP]] | -0.62 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZSWIM3]] | -0.61 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[HLA-DMA]] | -0.60 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[HAVCR2]] | -0.60 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[C14orf28]] | -0.59 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWOX]] | B | WWOX activity raises SPIDR's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without WWOX | 0.060 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SPIDR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WWOX]] | B | WWOX activity strengthens SPIDR's drug response | lines that do not express WWOX (5) vs lines expressing it (44) | the lines without WWOX respond 0.79× as strongly (z diff +2.09); strongest at Homoharringtonine 0.5 µM: 0.84x vs 0.44x (z diff +6.5) | 0.093 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.5, 17.1); signed map (-12.9, -52.4). **Vector** length 114, 50.7% of its response variance represented; |z| ≥ 3 in 1,511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.3 | +12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +9.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.4 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +4.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -14.0 | -14.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | scaffold protein involved in DNA repair |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.21 — chr8:47,260,878-47,736,306 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0146 |
| Gene groups (HGNC) | Shu complex |
| Reactome | 7 pathways, smallest: Resolution of D-loop Structures through Holliday Junction Intermediates; Resolution of D-Loop Structures; HDR through Homologous Recombination (HRR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14159](https://www.uniprot.org/uniprotkb/Q14159) (DNA repair-scaffolding protein):

> Involved in early stages DNA double-strand break (DSB) repair via homologous recombination (HR). As part of the Shu complex, promotes HR by regulating replication protein-A (RPA) dynamics on single-stranded DNA, thereby stabilizing RAD51 and DMC1 filaments on DNA. The Shu complex is essential during meiosis by stabilizing DMC1 filaments. In contrast, it is critical for only certain types of homologous-directed DNA repair, such as inter-homolog homologous recombination (IR-HR). IR-HR is a DNA …

**Summary**, from NCBI Gene [23514](https://www.ncbi.nlm.nih.gov/gene/23514):

> Involved in several processes, including cellular response to camptothecin; cellular response to hydroxyurea; and regulation of double-strand break repair. Located in nuclear chromosome and nucleoplasm. Implicated in ovarian dysgenesis 9. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28971) · Entrez [23514](https://www.ncbi.nlm.nih.gov/gene/23514) · UniProt [Q14159](https://www.uniprot.org/uniprotkb/Q14159) · Ensembl [ENSG00000164808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164808)

## Data

Gene col 9008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9008); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9008]; `tensor/DDL_lfc|DDL_z.npy` [9008]; `embed/gene_vectors.npy` [9008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9008 or target_col == 9008). Every well: [[SPIDR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPIDR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
