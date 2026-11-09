---
symbol: "NIPBL"
type: "gene"
col: 8899
ensembl_id: "ENSG00000164190"
name: "NIPBL cohesin loading factor"
location: "5p13.2"
module: 74
arm: "+"
pooled_cpm: 476.17
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# NIPBL

*NIPBL cohesin loading factor* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.40× (z +48.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.494× (z -26.0, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.833× (z -10.2, q 2e-22, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP350]] (+0.77, fdr 7e-06), [[RSF1]] (+0.75, fdr 7e-06), [[SETD2]] (+0.74, fdr 7e-06); moves opposite to [[COLGALT1]] (-0.61, fdr 1e-05), [[TPD52L2]] (-0.61, fdr 3e-05), [[INTS11]] (-0.60, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LTBP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.40×** | +48.8 | 0e+00 | 48/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.35×** | +33.7 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +27.9 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +25.9 | 0e+00 | 45/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +24.5 | 0e+00 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +24.5 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +21.1 | 0e+00 | 48/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +18.7 | 0e+00 | 45/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.59×** | +17.9 | 0e+00 | 46/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +11.3 | 4e-28 | 33/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +8.9 | 4e-17 | 31/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +8.4 | 2e-15 | 28/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +7.7 | 9e-13 | 24/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.20×** | +7.3 | 1e-11 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.5 | 1e-06 | 23/38 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.10× | +3.8 | 0.004 | 7/48 (LoVo, A-427, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.09× | +3.5 | 0.013 | 10/48 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.09× | +3.3 | 0.025 | 15/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.18× | +3.2 | 0.042 | 14/49 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.09× | +3.1 | 0.057 | 8/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -26.0 | 0e+00 | 41/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.527×** | -25.3 | 0e+00 | 47/49 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.621×** | -18.8 | 0e+00 | 43/48 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.643×** | -17.4 | 0e+00 | 40/48 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.691×** | -14.6 | 0e+00 | 40/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.682×** | -14.2 | 2e-43 | 42/47 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.688×** | -13.6 | 2e-40 | 34/45 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.793×** | -12.9 | 2e-36 | 30/49 (A549, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -10.2 | 2e-22 | 23/48 (LOX-IMVI, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -9.1 | 4e-18 | 33/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.791×** | -8.6 | 3e-16 | 27/48 (NCI-H2030, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.818×** | -7.9 | 1e-13 | 29/48 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.842× | -6.8 | 5e-10 | 23/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -6.5 | 4e-09 | 20/49 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.853× | -5.9 | 2e-07 | 19/50 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.776×** | -4.8 | 6e-05 | 32/48 (CFPAC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.781×** | -4.6 | 1e-04 | 29/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.891× | -4.5 | 2e-04 | 14/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.787×** | -4.5 | 2e-04 | 30/48 (AsPC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.867× | -4.0 | 0.002 | 13/48 (SW480, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.906× | -3.9 | 0.003 | 4/48 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.009 | 20/49 (AsPC-1, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 0.898× | -3.0 | 0.055 | 4/49 (NCI-H1792, SW480, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.852× | -3.0 | 0.055 | 13/48 (NCI-H1792, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 477 | 9 (1 ⚠) | 10 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +24.3) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -16.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 594 | 12 (3 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +35.1) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -17.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 565 | 10 (2 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +27.1) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -16.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 549 | 9 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +29.8) | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -22.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 454 | 9 (1 ⚠) | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -19.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 414 | 14 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +36.3) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -21.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 578 | 12 (3 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -16.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 620 | 9 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +28.5) | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -18.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 415 | 8 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +28.6) | [[Dinaciclib (drug)]] 0.5 µM 0.523× (z -14.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 462 | 9 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +26.8) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -18.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 323 | 9 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +26.2) | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -19.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 506 | 9 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 559 | 8 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +34.0) | [[Panobinostat (drug)]] 5 µM 0.471× (z -17.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 394 | 8 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +39.6) | [[Dinaciclib (drug)]] 5 µM 0.485× (z -15.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 458 | 8 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +31.7) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -21.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 459 | 9 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +24.8) | [[Panobinostat (drug)]] 0.5 µM 0.548× (z -12.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 522 | 11 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +34.8) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -22.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 362 | 10 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +44.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -24.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 557 | 11 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +31.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -18.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 483 | 9 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +33.0) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -17.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 492 | 9 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +23.5) | [[Dinaciclib (drug)]] 5 µM 0.493× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 387 | 11 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +33.2) | [[Dinaciclib (drug)]] 0.5 µM 0.564× (z -14.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 373 | 8 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 498 | 7 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +35.2) | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 987 | 10 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +31.9) | [[Dinaciclib (drug)]] 5 µM 0.542× (z -13.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 314 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +44.7) | — |
| [[HepG2_C3A (line)]] | wt | 530 | 6 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +18.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.357× (z -16.8) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 558 | 6 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +25.4) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -20.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 423 | 9 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +45.3) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -18.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 365 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +30.4) | [[Dinaciclib (drug)]] 0.5 µM 0.596× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 379 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +33.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 597 | 7 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +23.5) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -19.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 393 | 7 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +21.9) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -13.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 525 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +28.1) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 407 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +23.0) | — |
| [[C-33 A (line)]] | alt | 391 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -12.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 338 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +23.5) | [[Dinaciclib (drug)]] 0.5 µM 0.606× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 381 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +36.8) | [[Panobinostat (drug)]] 0.5 µM 0.616× (z -11.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 451 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.617× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 775 | 2 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -20.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 375 | 7 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.58× (z +19.1) | — |
| [[CHP-212 (line)]] | wt | 458 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 495 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +23.4) | [[Dinaciclib (drug)]] 0.5 µM 0.580× (z -14.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 199 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +19.0) | — |
| [[AN3 CA (line)]] | alt | 747 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -14.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H661 (line)]] | alt | 758 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 401 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.7) | — |
| [[SW 1271 (line)]] | alt | 617 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +9.7) | — |
| [[NCI-H2122 (line)]] | alt | 535 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 492 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP350]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | STRING 683 |
| [[RSF1]] | +0.75 | +0.63 / +0.73 | both halves | 7e-06 | STRING 720 |
| [[SETD2]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 | STRING 771 |
| [[SCAF11]] | +0.74 | +0.65 / +0.69 | both halves | 7e-06 | STRING 730 |
| [[XRN1]] | +0.73 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[BPTF]] | +0.70 | +0.58 / +0.67 | both halves | 7e-06 | STRING 806 |
| [[LARP7]] | +0.70 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R12A]] | +0.70 | +0.60 / +0.65 | both halves | 7e-06 | STRING 409 |
| [[BOD1L1]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 | STRING 528 |
| [[SNW1]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ATRX]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 674 |
| [[NBR1]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLGALT1]] | -0.61 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.61 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[INTS11]] | -0.60 | -0.44 / -0.53 | both halves | 3e-05 | STRING 752 |
| [[PRR5]] | -0.60 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[LTBP4]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NOMO2]] | -0.59 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[PLCB3]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ABHD17A]] | -0.58 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PMPCA]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[LIMK1]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[AKT1]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TATDN2]] | -0.56 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBP4]] | B | LTBP4 activity lowers NIPBL's level | lines that do not express LTBP4 (6) vs lines expressing it (44) | 1.15× higher at baseline in the lines without LTBP4 | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM132B, STK31, DDX59-AS1 |
| [[SLC17A9]] | B | SLC17A9 activity lowers NIPBL's level | lines that do not express SLC17A9 (27) vs lines expressing it (23) | 1.15× higher at baseline in the lines without SLC17A9 | 0.095 | ⚠ within organs, on part of the lines; also absent: UGT1A9, MT1G, TTC22 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.8, 6.2); signed map (4.7, -15.0). **Vector** length 113, 46.2% of its response variance represented; |z| ≥ 3 in 1,807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +25.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +27.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +48.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +7.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.1 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.6 | -9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | -6.3 | -14.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.3 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.4 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | NIPBL cohesin loading factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:36,876,769-37,066,413 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IDN3, DKFZp434L1319, FLJ11203, FLJ12597, FLJ13354, FLJ13648, Scc2 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 5 pathways, smallest: Cohesin Loading onto Chromatin; Mitotic Telophase/Cytokinesis; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6KC79](https://www.uniprot.org/uniprotkb/Q6KC79) (Nipped-B-like protein):

> Plays an important role in the loading of the cohesin complex on to DNA. Forms a heterodimeric complex (also known as cohesin loading complex) with MAU2/SCC4 which mediates the loading of the cohesin complex onto chromatin. Plays a role in cohesin loading at sites of DNA damage. Its recruitment to double-strand breaks (DSBs) sites occurs in a CBX3-, RNF8- and RNF168-dependent manner whereas its recruitment to UV irradiation-induced DNA damage sites occurs in a ATM-, ATR-, RNF8- and …

**Summary**, from NCBI Gene [25836](https://www.ncbi.nlm.nih.gov/gene/25836):

> This gene encodes the homolog of the Drosophila melanogaster Nipped-B gene product and fungal Scc2-type sister chromatid cohesion proteins. The Drosophila protein facilitates enhancer-promoter communication of remote enhancers and plays a role in developmental regulation. It is also homologous to a family of chromosomal adherins with broad roles in sister chromatid cohesion, chromosome condensation, and DNA repair. The human protein has a bipartite nuclear targeting sequence and a putative HEAT …

**Accessions** — [HGNC:28862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28862) · Entrez [25836](https://www.ncbi.nlm.nih.gov/gene/25836) · UniProt [Q6KC79](https://www.uniprot.org/uniprotkb/Q6KC79) · Ensembl [ENSG00000164190](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164190)

## Data

Gene col 8899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8899); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8899]; `tensor/DDL_lfc|DDL_z.npy` [8899]; `embed/gene_vectors.npy` [8899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8899 or target_col == 8899). Every well: [[NIPBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
