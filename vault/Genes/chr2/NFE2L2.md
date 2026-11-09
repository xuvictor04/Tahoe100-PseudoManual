---
symbol: "NFE2L2"
type: "gene"
col: 3755
ensembl_id: "ENSG00000116044"
name: "NFE2 like bZIP transcription factor 2"
location: "2q31.2"
module: 57
arm: "-"
pooled_cpm: 287.92
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# NFE2L2

*NFE2 like bZIP transcription factor 2* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +19.8, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.468× (z -20.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00963]] (+0.66, fdr 7e-06), [[CUX1]] (+0.65, fdr 1e-05), [[SKIL]] (+0.60, fdr 1e-05); moves opposite to [[PMS2P3-1]] (-0.62, fdr 1e-05), [[APAF1]] (-0.62, fdr 1e-05), [[DDHD2]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC25A13]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +19.8 | 0e+00 | 38/48 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +19.3 | 0e+00 | 42/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +10.4 | 7e-23 | 33/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +8.1 | 1e-13 | 30/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.8 | 8e-10 | 29/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +6.0 | 2e-07 | 32/49 (HS-578T, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.17× | +5.6 | 2e-06 | 20/48 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +5.4 | 5e-06 | 26/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.43×** | +5.1 | 3e-05 | 30/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +4.7 | 2e-04 | 23/47 (A-172, HCT15, …) | rises with dose |  |
| [[Menadione (drug)]] 5 µM |  | 1.20× | +4.6 | 2e-04 | 21/47 (A498, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 2e-04 | 23/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.12× | +4.3 | 7e-04 | 6/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.0 | 0.002 | 27/46 (C32, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.002 | 17/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.9 | 0.003 | 16/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | 1.10× | +3.7 | 0.007 | 7/49 (NCI-H460, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.009 | 18/48 (LoVo, MIA PaCa-2, …) | two highest doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.009 | 13/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.031 | 18/48 (PANC-1, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.468×** | -20.6 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.534×** | -17.0 | 0e+00 | 47/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -16.4 | 0e+00 | 47/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -12.7 | 5e-35 | 37/44 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.650×** | -11.7 | 2e-29 | 37/49 (RKO, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.743×** | -11.4 | 3e-28 | 33/49 (A498, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.757×** | -10.7 | 1e-24 | 36/48 (SW480, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.726×** | -8.4 | 4e-15 | 36/47 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.764×** | -6.8 | 8e-10 | 26/45 (A-427, RKO, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.652×** | -6.1 | 8e-08 | 38/47 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.808×** | -5.8 | 3e-07 | 25/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.817×** | -5.5 | 2e-06 | 27/48 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.845× | -4.6 | 2e-04 | 22/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.840× | -4.6 | 2e-04 | 24/50 (NCI-H23, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.841× | -4.5 | 2e-04 | 22/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.018 | 22/49 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.878× | -3.4 | 0.021 | 13/48 (PANC-1, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 412 | 10 (4 ⚠) | 6 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 3.53× (z +22.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -16.5) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.574× (z -10.1) |
| [[A498 (line)]] | wt | 445 | 4 (1 ⚠) | 8 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.44× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -18.9) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.512× (z -12.8) |
| [[SW 900 (line)]] | alt | 411 | 5 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.464× (z -10.7) |
| [[A-427 (line)]] | wt | 316 | 1 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.87× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -26.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.399× (z -17.4) |
| [[SW480 (line)]] | alt | 255 | 4 (2 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.95× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.401× (z -19.1) |
| [[HOP62 (line)]] | alt | 240 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +24.3) | [[Belinostat (drug)]] 5 µM 0.545× (z -9.8) |
| [[HT-29 (line)]] | alt | 334 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -17.5) |
| [[LoVo (line)]] | wt | 222 | 3 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.44× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.379× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 318 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.400× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 372 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.423× (z -12.8) |
| [[PANC-1 (line)]] | alt | 412 | 2 | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.52× (z +17.8) | [[Panobinostat (drug)]] 5 µM 0.395× (z -18.7) |
| [[A-172 (line)]] | wt | 218 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +16.5) | [[Panobinostat (drug)]] 0.5 µM 0.629× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 387 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.350× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 238 | 4 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 2.88× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.533× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 372 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -15.2) |
| [[HS-578T (line)]] | alt | 188 | 7 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.67× (z +17.8) | — |
| [[LS 180 (line)]] | wt | 276 | 2 (1 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.08× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.405× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 481 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.369× (z -17.4) |
| [[RKO (line)]] | wt | 212 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 377 | 4 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.03× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.488× (z -8.9) |
| [[SNU-1 (line)]] | wt | 527 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.458× (z -10.0) |
| [[SW48 (line)]] | wt | 313 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -14.8) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.405× (z -12.2) |
| [[A549 (line)]] | wt | 268 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[KATO III (line)]] | alt | 242 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.409× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 240 | 3 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.89× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -12.8) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.563× (z -9.5) |
| [[C32 (line)]] | wt | 221 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.44× (z +17.3) | — |
| [[hTERT-HPNE (line)]] | wt | 194 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 207 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +19.7) | [[Panobinostat (drug)]] 5 µM 0.567× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 281 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 3.46× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.465× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 144 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 224 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -10.0) |
| [[SNU-423 (line)]] | alt | 217 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.373× (z -10.5) |
| [[BT-474 (line)]] | alt | 198 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -10.1) |
| [[HCT15 (line)]] | alt | 180 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.33× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 229 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.540× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 255 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.3) | — |
| [[SW1417 (line)]] | alt | 284 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -16.6) |
| [[C-33 A (line)]] | alt | 249 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.447× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 226 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +19.2) | — |
| [[CHP-212 (line)]] | wt | 296 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -9.7) |
| [[NCI-H661 (line)]] | alt | 302 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.7) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -8.6) |
| [[SHP-77 (line)]] | alt | 188 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 217 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.1) | — |
| [[H4 (line)]] | wt | 305 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.7) | — |
| [[SW 1088 (line)]] | alt | 217 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 179 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 495 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00963]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CUX1]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SKIL]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TRIM16L]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TRIM16L-1]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ID4]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TENM3]] | +0.57 | +0.55 / +0.46 | both halves | 3e-05 | same gene group |
| [[WARS2-AS1]] | +0.57 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[GGPS1]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TSC22D1]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NMRAL2P-1]] | +0.56 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[BRAF]] | +0.55 | +0.46 / +0.44 | both halves | 3e-05 | STRING 449 |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[APAF1]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 | STRING 552 |
| [[DDHD2]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[RPA1]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[NAP1L4]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[NTAN1]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[USP48]] | -0.58 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[VDAC3]] | -0.58 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[POGLUT2]] | -0.57 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ECI2]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A13]] | C | SLC25A13's natural level strengthens NFE2L2's drug response | SLC25A13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.09; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.8, -15.8); signed map (14.5, -11.0). **Vector** length 140, 46.5% of its response variance represented; |z| ≥ 3 in 1,584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +12.6 | +19.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +19.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.7 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.3 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.9 | +0.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.8 | +1.0 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +3.7 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.6 | -10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -20.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -4.5 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -17.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -16.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | NFE2 like bZIP transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:177,218,667-177,392,756 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRF2, NRF-2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; NFE2 family bZIP transcription factors |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 30 pathways, smallest: NFE2L2 regulating TCA cycle genes; NFE2L2 regulating ER-stress associated genes; Regulation of HMOX1 expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16236](https://www.uniprot.org/uniprotkb/Q16236) (Nuclear factor erythroid 2-related factor 2):

> Transcription factor that plays a key role in the response to oxidative stress: binds to antioxidant response (ARE) elements present in the promoter region of many cytoprotective genes, such as phase 2 detoxifying enzymes, and promotes their expression, thereby neutralizing reactive electrophiles. In normal conditions, ubiquitinated and degraded in the cytoplasm by the BCR(KEAP1) complex. In response to oxidative stress, electrophile metabolites inhibit activity of the BCR(KEAP1) complex, …

**Summary**, from NCBI Gene [4780](https://www.ncbi.nlm.nih.gov/gene/4780):

> This gene encodes a transcription factor which is a member of a small family of basic leucine zipper (bZIP) proteins. The encoded transcription factor regulates genes which contain antioxidant response elements (ARE) in their promoters; many of these genes encode proteins involved in response to injury and inflammation which includes the production of free radicals. Multiple transcript variants encoding different isoforms have been characterized for this gene. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:7782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7782) · Entrez [4780](https://www.ncbi.nlm.nih.gov/gene/4780) · UniProt [Q16236](https://www.uniprot.org/uniprotkb/Q16236) · Ensembl [ENSG00000116044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116044)

## Data

Gene col 3755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3755); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3755]; `tensor/DDL_lfc|DDL_z.npy` [3755]; `embed/gene_vectors.npy` [3755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3755 or target_col == 3755). Every well: [[NFE2L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFE2L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
