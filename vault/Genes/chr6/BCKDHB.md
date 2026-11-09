---
symbol: "BCKDHB"
type: "gene"
col: 1363
ensembl_id: "ENSG00000083123"
name: "branched chain keto acid dehydrogenase E1 subunit beta"
location: "6q14.1"
module: 99
arm: "+"
pooled_cpm: 152.19
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 37
n_dd_up_clean: 9
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# BCKDHB

*branched chain keto acid dehydrogenase E1 subunit beta* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.92× (z +13.7, q 9e-40, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -25.0, q 0e+00, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.295× (z -24.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CABIN1]] (+0.71, fdr 7e-06), [[UBE2Q2P2]] (+0.67, fdr 1e-05), [[KIAA1328]] (+0.64, fdr 2e-05); moves opposite to [[CARD6]] (-0.62, fdr 3e-05), [[SPTY2D1OS]] (-0.58, fdr 1e-04), [[ZSCAN29]] (-0.57, fdr 4e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZNF594]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +13.7 | 9e-40 | 42/48 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +12.8 | 5e-35 | 41/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +12.4 | 8e-33 | 43/48 (KATO III, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.4 | 2e-08 | 31/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +5.5 | 4e-06 | 34/49 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.61×** | +5.2 | 1e-05 | 30/48 (SNU-423, A498, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +5.2 | 2e-05 | 31/49 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +4.8 | 1e-04 | 27/50 (RKO, SW480, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 24/49 (SNU-423, SHP-77, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.003 | 23/47 (SW480, LS 180, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.013 | 21/48 (HOP62, SHP-77, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.020 | 13/48 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.028 | 18/47 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.16× | +3.2 | 0.052 | 20/48 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.066 | 10/49 (LoVo, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.430×** | -25.0 | 0e+00 | 41/48 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.295×** | -24.6 | 0e+00 | 45/48 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.348×** | -22.1 | 0e+00 | 45/48 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.368×** | -20.9 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -20.2 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.395×** | -19.5 | 0e+00 | 41/49 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.428×** | -17.1 | 0e+00 | 46/47 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.232×** | -16.0 | 0e+00 | 48/49 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.470×** | -15.8 | 0e+00 | 44/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.476×** | -15.5 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.480×** | -14.8 | 0e+00 | 40/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -14.7 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.265×** | -14.5 | 0e+00 | 46/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -13.0 | 3e-37 | 36/44 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.533×** | -12.2 | 2e-32 | 37/45 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -9.8 | 2e-21 | 36/48 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.629×** | -9.7 | 1e-20 | 39/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.656×** | -8.8 | 4e-17 | 40/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -8.2 | 1e-14 | 37/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -7.0 | 8e-11 | 33/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.740×** | -6.3 | 8e-09 | 39/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.740×** | -6.3 | 8e-09 | 30/48 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 178 | 0 | 20 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -20.2) |
| [[PANC-1 (line)]] | alt | 205 | 0 | 20 (11 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -29.3) |
| [[A-172 (line)]] | wt | 135 | 3 | 16 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -25.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.146× (z -22.0) |
| [[J82 (line)]] | alt | 157 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -26.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -18.7) |
| [[SW480 (line)]] | alt | 126 | 5 (2 ⚠) | 13 (6 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.8) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.08× (z +10.5) | [[Digitoxin (drug)]] 0.5 µM 0.190× (z -23.6) |
| [[MIA PaCa-2 (line)]] | alt | 348 | 0 | 17 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -19.0) |
| [[SNU-423 (line)]] | alt | 171 | 3 | 14 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -35.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.155× (z -23.5) |
| [[NCI-H1573 (line)]] | alt | 101 | 3 | 13 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -23.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -21.2) |
| [[NCI-H23 (line)]] | alt | 206 | 0 | 16 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0683× (z -34.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -20.8) |
| [[SNU-1 (line)]] | wt | 226 | 0 | 16 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -19.2) |
| [[C32 (line)]] | wt | 164 | 0 | 15 (9 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.191× (z -18.6) |
| [[HS-578T (line)]] | alt | 136 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -22.2) |
| [[KATO III (line)]] | alt | 122 | 3 | 12 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -14.2) |
| [[LS 180 (line)]] | wt | 448 | 0 | 15 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 219 | 2 (2 ⚠) | 12 (6 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.8) ⚠ cell-cycle shift, explains ~20% of this change | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.313× (z -16.1) |
| [[HOP62 (line)]] | alt | 143 | 2 | 12 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -21.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.226× (z -19.9) |
| [[Hs 766T (line)]] | wt | 184 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.225× (z -17.0) |
| [[NCI-H1792 (line)]] | alt | 168 | 3 | 11 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -20.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.250× (z -18.6) |
| [[HT-29 (line)]] | alt | 230 | 0 | 13 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -19.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -12.4) |
| [[LoVo (line)]] | wt | 149 | 0 | 13 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -18.9) |
| [[RPMI-7951 (line)]] | alt | 213 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -24.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.125× (z -24.0) |
| [[HCT15 (line)]] | alt | 168 | 0 | 12 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.203× (z -15.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 164 | 3 | 9 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.276× (z -13.3) |
| [[C-33 A (line)]] | alt | 229 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -14.8) |
| [[SW 900 (line)]] | alt | 85.5 | 3 | 8 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +11.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.212× (z -16.1) |
| [[SW48 (line)]] | wt | 169 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 243 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -20.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -15.0) |
| [[A498 (line)]] | wt | 45.6 | 4 (1 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +11.7) | [[Harringtonine (drug)]] 0.5 µM 0.242× (z -14.4) |
| [[SHP-77 (line)]] | alt | 221 | 1 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.91× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -15.5) |
| [[AN3 CA (line)]] | alt | 261 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0837× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.290× (z -10.6) |
| [[SW1417 (line)]] | alt | 96.1 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -14.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.311× (z -11.3) |
| [[A549 (line)]] | wt | 58.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -17.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.198× (z -15.6) |
| [[H4 (line)]] | wt | 119 | 1 | 5 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.68× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.264× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 113 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.7) | [[Harringtonine (drug)]] 5 µM 0.278× (z -11.7) |
| [[RKO (line)]] | wt | 112 | 2 (2 ⚠) | 4 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.9) ⚠ cell-cycle shift, explains ~20% of this change | [[PH-797804 (drug)]] 5 µM 0.119× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 5 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.160× (z -10.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.173× (z -9.7) |
| [[A-427 (line)]] | wt | 88.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.342× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 61.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.296× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 40.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[PH-797804 (drug)]] 5 µM 0.0575× (z -10.2) |
| [[SW 1271 (line)]] | alt | 279 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -11.2) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 235 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 49.1 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.380× (z -9.5) |
| [[BT-474 (line)]] | alt | 148 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.441× (z -8.6) |
| [[SW 1088 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CABIN1]] | +0.71 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[UBE2Q2P2]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[KIAA1328]] | +0.64 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PRELID2]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NBAS]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PDK3]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[KIAA1958]] | +0.60 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[RALGAPA2]] | +0.59 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[HACE1]] | +0.58 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[GLG1]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[SMYD3]] | +0.58 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[LNPK]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD6]] | -0.62 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SPTY2D1OS]] | -0.58 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[ZSCAN29]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[KCNMB3]] | -0.55 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[ANKLE2]] | -0.55 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MOB3C]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZNF702P]] | -0.55 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[CFLAR]] | -0.54 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[LRRC37A3]] | -0.54 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[ZNF594]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[EIF5]] | -0.54 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[FEM1A]] | -0.54 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594]] | B | ZNF594 activity raises BCKDHB's level | lines that do not express ZNF594 (6) vs lines expressing it (44) | 1.94× lower at baseline in the lines without ZNF594 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: ZNF594-DT, MIR3659HG, SYNGR1 |
| [[ZNF594]] | B | ZNF594 activity strengthens BCKDHB's drug response | lines that do not express ZNF594 (6) vs lines expressing it (43) | the lines without ZNF594 respond 0.78× as strongly (z diff +2.15); strongest at Dinaciclib 0.5 µM: 0.77x vs 0.39x (z diff +5.2) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: ZNF594-DT, MIR3659HG, SYNGR1; target measured in part of the lines; artifact flags |
| [[EPIC1]] | B | EPIC1 activity raises BCKDHB's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without EPIC1 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[GPR155]] | B | GPR155 activity raises BCKDHB's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without GPR155 | 0.077 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[CARD6]] | B | CARD6 activity lowers BCKDHB's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.66× higher at baseline in the lines without CARD6 | 0.081 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[GPR155]] | B | GPR155 activity strengthens BCKDHB's drug response | lines that do not express GPR155 (6) vs lines expressing it (43) | the lines without GPR155 respond 0.74× as strongly (z diff +2.40); strongest at Dinaciclib 0.5 µM: 0.90x vs 0.38x (z diff +6.2) | 0.091 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SSBP2]] | C | SSBP2 activity raises BCKDHB's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without SSBP2 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.1, -14.7); signed map (-36.7, 20.0). **Vector** length 115, 44.2% of its response variance represented; |z| ≥ 3 in 1,989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.0 | +12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +13.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +12.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.0 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.0 | +0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.6 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -13.3 | -17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -11.5 | -13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.1 | -12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -10.0 | -9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.7 | -19.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.4 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -8.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.5 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | branched chain keto acid dehydrogenase E1 subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:80,106,647-80,346,270 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OVD1B |
| Gene groups (HGNC) | Branched chain alpha-keto acid dehydrogenase complex subunits; Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, UV_RESPONSE_DN |
| Reactome | 11 pathways, smallest: Loss-of-function mutations in BCKDHA or BCKDHB cause MSUD; BCKDH synthesizes BCAA-CoA from KIC, KMVA, KIV; Loss-of-function mutations in DBT cause MSUD2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P21953](https://www.uniprot.org/uniprotkb/P21953) (2-oxoisovalerate dehydrogenase subunit beta, mitochondrial):

> Together with BCKDHA forms the heterotetrameric E1 subunit of the mitochondrial branched-chain alpha-ketoacid dehydrogenase (BCKD) complex. The BCKD complex catalyzes the multi-step oxidative decarboxylation of alpha-ketoacids derived from the branched-chain amino-acids valine, leucine and isoleucine producing CO2 and acyl-CoA which is subsequently utilized to produce energy. The E1 subunit catalyzes the first step with the decarboxylation of the alpha-ketoacid forming an enzyme-product …

**Summary**, from NCBI Gene [594](https://www.ncbi.nlm.nih.gov/gene/594):

> This gene encodes the E1 beta subunit of branched-chain keto acid dehydrogenase, which is a multienzyme complex associated with the inner membrane of mitochondria. This enzyme complex functions in the catabolism of branched-chain amino acids. Mutations in this gene have been associated with maple syrup urine disease (MSUD), type 1B, a disease characterized by a maple syrup odor to the urine in addition to mental and physical retardation and feeding problems. Alternative splicing at this locus …

**Accessions** — [HGNC:987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:987) · Entrez [594](https://www.ncbi.nlm.nih.gov/gene/594) · UniProt [P21953](https://www.uniprot.org/uniprotkb/P21953) · Ensembl [ENSG00000083123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083123)

## Data

Gene col 1363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1363); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1363]; `tensor/DDL_lfc|DDL_z.npy` [1363]; `embed/gene_vectors.npy` [1363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1363 or target_col == 1363). Every well: [[BCKDHB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCKDHB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
