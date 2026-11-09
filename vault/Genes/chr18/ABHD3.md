---
symbol: "ABHD3"
type: "gene"
col: 8143
ensembl_id: "ENSG00000158201"
name: "abhydrolase domain containing 3, phospholipase"
location: "18q11.2"
module: 72
arm: "+"
pooled_cpm: 83.57
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ABHD3

*abhydrolase domain containing 3, phospholipase* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.41× (z +25.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.523× (z -10.4, q 2e-22, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.441× (z -7.4, q 4e-11, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NQO2]] (+0.67, fdr 1e-05), [[RAD9A]] (+0.63, fdr 1e-05), [[SLC25A29]] (+0.62, fdr 1e-05); moves opposite to [[UTP15]] (-0.63, fdr 7e-06), [[SRFBP1]] (-0.61, fdr 1e-05), [[HNRNPD]] (-0.60, fdr 2e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[S100A14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.41×** | +25.7 | 0e+00 | 48/48 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.20×** | +23.4 | 0e+00 | 48/48 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.85×** | +23.3 | 0e+00 | 48/48 (A-427, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.80×** | +23.1 | 0e+00 | 48/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +16.5 | 0e+00 | 37/48 (COLO 205, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.09×** | +13.9 | 4e-42 | 48/49 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.14×** | +13.2 | 7e-38 | 46/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.13×** | +13.1 | 2e-37 | 44/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.07×** | +12.6 | 2e-34 | 44/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.54×** | +11.4 | 1e-28 | 43/44 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +10.6 | 1e-24 | 38/47 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +10.2 | 1e-22 | 46/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +9.6 | 3e-20 | 44/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.72×** | +9.0 | 9e-18 | 36/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.70×** | +8.8 | 5e-17 | 40/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +8.2 | 9e-15 | 33/48 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Infigratinib (drug)]] 5 µM |  | **2.04×** | +6.5 | 3e-09 | 42/47 (SW1417, A-427, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.95×** | +6.0 | 4e-08 | 36/48 (SW480, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.6 | 5e-07 | 25/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 7e-07 | 26/48 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 1e-06 | 29/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.7 | 4e-05 | 27/48 (COLO 205, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.523×** | -10.4 | 2e-22 | 35/44 (RKO, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -7.4 | 4e-11 | 35/49 (AsPC-1, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.713×** | -5.6 | 3e-06 | 31/48 (J82, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -5.6 | 3e-06 | 27/41 (SW48, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.678×** | -5.6 | 3e-06 | 28/49 (AsPC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.711×** | -5.2 | 2e-05 | 29/48 (SNU-1, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.757×** | -4.4 | 7e-04 | 25/47 (HS-578T, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -4.1 | 0.003 | 26/48 (LS 180, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.005 | 21/48 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.878× | -3.2 | 0.086 | 9/48 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 5 µM |  | 0.712× | -3.1 | 0.10 | 14/45 (MIA PaCa-2, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.819× | -3.1 | 0.10 | 21/48 (A549, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 45.2 | 12 (6 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.61× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.9 | 12 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.6× (z +21.7) | — |
| [[LoVo (line)]] | wt | 96.4 | 10 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.24× (z +18.9) | — |
| [[LS 180 (line)]] | wt | 115 | 9 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.51× (z +18.7) | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 69.9 | 9 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.60× (z +17.0) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 64.9 | 10 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.93× (z +19.8) | — |
| [[SW480 (line)]] | alt | 108 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 253 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -13.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 58.0 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.26× (z +20.4) | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 54.9 | 9 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.85× (z +15.4) | — |
| [[SW1417 (line)]] | alt | 118 | 9 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.73× (z +19.7) | — |
| [[A-172 (line)]] | wt | 78.4 | 7 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 6.17× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 128 | 5 (1 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 5.74× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 101 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.80× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.397× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 87.2 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 12.3× (z +22.3) | — |
| [[Panc 03.27 (line)]] | alt | 214 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +19.0) | [[Lonafarnib (drug)]] 5 µM 0.0608× (z -15.2) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 97.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +16.2) | — |
| [[COLO 205 (line)]] | alt | 69.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +19.3) | — |
| [[HEC-1-A (line)]] | alt | 66.5 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.87× (z +18.9) | — |
| [[RKO (line)]] | wt | 70.3 | 6 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.75× (z +17.7) | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -13.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 96.2 | 4 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.37× (z +25.4) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.9) |
| [[A498 (line)]] | wt | 94.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.6) | — |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.17× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 110 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.32× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 45.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.85× (z +16.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 117 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.32× (z +12.5) | — |
| [[C32 (line)]] | wt | 53.9 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.60× (z +13.3) | — |
| [[H4 (line)]] | wt | 39.9 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.2× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 106 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.79× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 97.5 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.91× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 113 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.93× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 73.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 59.5 | 5 | 0 | [[Auranofin (drug)]] 5 µM 4.32× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 38.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.22× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 48.3 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.51× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 34.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.31× (z +14.3) | — |
| [[SNU-1 (line)]] | wt | 60.5 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.25× (z +11.9) | — |
| [[A549 (line)]] | wt | 67.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.74× (z +13.6) | — |
| [[HepG2_C3A (line)]] | wt | 96.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 44.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.64× (z +14.4) | — |
| [[SW48 (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.82× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0555× (z -18.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 57.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.53× (z +15.9) | — |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NQO2]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[RAD9A]] | +0.63 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SLC25A29]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[FTL]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KLHL25]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[HSPA1B]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ZNF823]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.58 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[HSPA1A]] | +0.57 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[LDAF1]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[DEDD2]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[GPR89B]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP15]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[SRFBP1]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.60 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[SF3B3]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[MTPAP]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[FAM174A-DT]] | -0.57 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[ANAPC13]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CPNE1]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 | pathway: Glycerophospholipid biosynthesis |
| [[ERLIN2]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SYNCRIP]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ZNF252P]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ZNF252P-1]] | -0.55 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A14]] | B | S100A14 activity raises ABHD3's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.84× lower at baseline in the lines without S100A14 | 0.005 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.7, -6.3); signed map (-25.0, 10.2). **Vector** length 133, 48.4% of its response variance represented; |z| ≥ 3 in 1,769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.9 | +23.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.8 | +25.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.9 | +23.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.7 | +23.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.0 | +11.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.7 | +13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.6 |
|  | [[Infigratinib (drug)]] 5 µM |  | +4.0 | +6.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -13.7 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -10.9 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.5 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.6 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.3 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 3, phospholipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:21,650,901-21,704,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LABH3 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU67](https://www.uniprot.org/uniprotkb/Q8WU67) (Phospholipase ABHD3):

> Phospholipase that may play a role in phospholipids remodeling. May selectively cleave myristate (C14)-containing phosphatidylcholines through its predominant phospholipase 1 activity, cleaving preferentially acyl groups in sn1 position. In parallel, may have a minor phospholipase 2 activity acting on acyl groups in position sn2. In addition to (C14)-containing phosphatidylcholines, may also act on other medium-chain-containing and oxidatively truncated phospholipids.

**Summary**, from NCBI Gene [171586](https://www.ncbi.nlm.nih.gov/gene/171586):

> This gene encodes a protein containing an alpha/beta hydrolase fold, which is a catalytic domain found in a very wide range of enzymes. The function of this protein has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18718) · Entrez [171586](https://www.ncbi.nlm.nih.gov/gene/171586) · UniProt [Q8WU67](https://www.uniprot.org/uniprotkb/Q8WU67) · Ensembl [ENSG00000158201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158201)

## Data

Gene col 8143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8143); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8143]; `tensor/DDL_lfc|DDL_z.npy` [8143]; `embed/gene_vectors.npy` [8143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8143 or target_col == 8143). Every well: [[ABHD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
