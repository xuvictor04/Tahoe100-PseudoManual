---
symbol: "MSANTD3"
type: "gene"
col: 836
ensembl_id: "ENSG00000066697"
name: "Myb/SANT DNA binding domain containing 3"
location: "9q31.1"
module: 112
arm: "+"
pooled_cpm: 123.73
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 23
n_dd_up_clean: 15
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 15
direction_downstream: 2
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# MSANTD3

*Myb/SANT DNA binding domain containing 3* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.26× (z +28.4, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.302× (z -20.4, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSANTD3-TMEFF1]] (+0.72, fdr 7e-06, ⚠ read-through risk), [[TRAF1]] (+0.72, fdr 7e-06), [[TMEFF1]] (+0.67, fdr 1e-05, ⚠ same locus), [[AMPD3]] (+0.66, fdr 9e-06), [[HDAC9]] (+0.66, fdr 7e-06); moves opposite to [[ADAM15]] (-0.59, fdr 2e-05), [[ATP1A1]] (-0.58, fdr 2e-05), [[PPT2]] (-0.55, fdr 6e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[KCNMA1]] → it (grade B ⚠); 2 go from it, the strongest it → [[MSANTD3-TMEFF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.26×** | +28.4 | 0e+00 | 43/46 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.75×** | +16.5 | 0e+00 | 43/46 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.92×** | +13.4 | 1e-38 | 44/47 (RPMI-7951, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +12.4 | 3e-33 | 39/46 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +8.2 | 4e-14 | 34/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +8.0 | 1e-13 | 38/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +7.0 | 3e-10 | 37/46 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +6.0 | 2e-07 | 28/46 (LS 180, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.39×** | +5.5 | 2e-06 | 31/46 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +5.3 | 7e-06 | 29/45 (LS 180, HT-29, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +4.5 | 4e-04 | 29/46 (C32, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 4e-04 | 22/46 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 4e-04 | 25/45 (LS 180, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +4.3 | 8e-04 | 24/45 (LS 180, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.28×** | +4.2 | 9e-04 | 22/46 (KATO III, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.017 | 26/46 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.032 | 19/46 (COLO 205, KATO III, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.047 | 20/46 (A498, SNU-423, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.077 | 18/46 (HT-29, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.302×** | -20.4 | 0e+00 | 45/46 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.322×** | -19.3 | 0e+00 | 46/46 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.360×** | -17.4 | 0e+00 | 45/46 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.622×** | -8.1 | 8e-14 | 38/46 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.748×** | -7.0 | 3e-10 | 25/47 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.506×** | -5.7 | 9e-07 | 32/47 (HEC-1-A, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.717×** | -5.7 | 1e-06 | 32/46 (HOP62, A549, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.724×** | -5.5 | 3e-06 | 34/46 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.740×** | -5.1 | 2e-05 | 28/46 (NCI-H1792, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.818×** | -4.9 | 6e-05 | 26/46 (J82, RKO, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.770×** | -4.5 | 4e-04 | 23/46 (A549, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.771×** | -4.5 | 4e-04 | 25/46 (SNU-423, NCI-H1792, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -4.2 | 0.001 | 22/46 (J82, hTERT-HPNE, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.767×** | -4.2 | 0.001 | 23/45 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.784×** | -4.0 | 0.002 | 22/46 (NCI-H23, hTERT-HPNE, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.798×** | -3.9 | 0.004 | 23/46 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.855× | -3.8 | 0.005 | 18/46 (NCI-H1792, H4, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.642×** | -3.7 | 0.006 | 22/47 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 178 | 6 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +24.7) | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 228 | 6 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.287× (z -17.4) |
| [[A-172 (line)]] | wt | 281 | 7 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +34.5) | [[Panobinostat (drug)]] 5 µM 0.189× (z -19.1) |
| [[HEC-1-A (line)]] | alt | 203 | 3 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.59× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -24.3) |
| [[J82 (line)]] | alt | 215 | 4 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +36.6) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -24.3) |
| [[RKO (line)]] | wt | 272 | 5 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +23.0) | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -16.1) |
| [[A498 (line)]] | wt | 88.3 | 7 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +24.0) | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 174 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -20.5) |
| [[RPMI-7951 (line)]] | alt | 202 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +21.0) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -19.4) |
| [[SNU-423 (line)]] | alt | 216 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +29.9) | [[Panobinostat (drug)]] 5 µM 0.195× (z -19.7) |
| [[HS-578T (line)]] | alt | 130 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.165× (z -20.0) |
| [[PANC-1 (line)]] | alt | 109 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +25.5) | [[Panobinostat (drug)]] 5 µM 0.250× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 157 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.264× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 328 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.4) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -21.6) |
| [[NCI-H1792 (line)]] | alt | 153 | 2 | 5 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.48× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.197× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 138 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -14.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.295× (z -13.9) |
| [[H4 (line)]] | wt | 193 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.167× (z -15.9) |
| [[HOP62 (line)]] | alt | 236 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +18.1) | [[Panobinostat (drug)]] 5 µM 0.145× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 136 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.283× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 72.3 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.368× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 87.2 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +18.1) | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -16.8) |
| [[SW 900 (line)]] | alt | 102 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +22.3) | [[Panobinostat (drug)]] 5 µM 0.237× (z -12.3) |
| [[COLO 205 (line)]] | alt | 54.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +28.1) | — |
| [[HepG2_C3A (line)]] | wt | 122 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +19.8) | [[Panobinostat (drug)]] 5 µM 0.230× (z -14.3) |
| [[KATO III (line)]] | alt | 42.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +22.0) | — |
| [[AsPC-1 (line)]] | alt | 68.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.344× (z -9.9) |
| [[C32 (line)]] | wt | 172 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.321× (z -12.4) |
| [[Hs 766T (line)]] | wt | 93.5 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.272× (z -11.1) |
| [[HT-29 (line)]] | alt | 48.4 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.268× (z -10.3) |
| [[LS 180 (line)]] | wt | 48.2 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.311× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 59.3 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +18.6) | [[Panobinostat (drug)]] 5 µM 0.286× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 49.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.313× (z -8.8) |
| [[SW1417 (line)]] | alt | 52.3 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.363× (z -9.6) |
| [[SW480 (line)]] | alt | 69.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -13.5) |
| [[A-427 (line)]] | wt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.5) | — |
| [[NCI-H2030 (line)]] | alt | 76.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.9) | — |
| [[SW 1271 (line)]] | alt | 217 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -9.9) |
| [[SW48 (line)]] | wt | 54.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +13.7) | — |
| [[AN3 CA (line)]] | alt | 81.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 46.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 28.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD3-TMEFF1]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 | ⚠ **readthrough risk**: MSANTD3-TMEFF1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[TRAF1]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[TMEFF1]] | +0.67 | +0.72 / +0.52 | both halves | 1e-05 | STRING 693; ⚠ same locus (21.4 kb, same strand: neighbours can correlate without regulation) |
| [[AMPD3]] | +0.66 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[HDAC9]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MAST4]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[HMGN2P46]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[AFF3]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ADTRP]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[KIAA1217]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CAVIN4]] | +0.61 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ALOXE3]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[LINC00973]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZNF267]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM15]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ATP1A1]] | -0.58 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PPT2]] | -0.55 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[CMPK1]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[CPD]] | -0.54 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[IFNGR1]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[STT3B]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ABHD2]] | -0.52 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[ATL2]] | -0.51 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[TECR]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMA1]] | B | KCNMA1 activity raises MSANTD3's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without KCNMA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises MSANTD3's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without CLDN14-AS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[TRAF1]] | B | TRAF1 activity raises MSANTD3's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without TRAF1 | 0.005 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[HRH1]] | B | HRH1 activity raises MSANTD3's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without HRH1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[AXL]] | B | AXL activity raises MSANTD3's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.64× lower at baseline in the lines without AXL | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[ETS1]] | B | ETS1 activity raises MSANTD3's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without ETS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[ADTRP]] | B | ADTRP activity raises MSANTD3's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without ADTRP | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[AFF3]] | B | AFF3 activity raises MSANTD3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without AFF3 | 0.039 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[ROBO4]] | B | ROBO4 activity raises MSANTD3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without ROBO4 | 0.047 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[RUNX1]] | B | RUNX1 activity raises MSANTD3's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without RUNX1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers MSANTD3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[LINC02934]] | B | LINC02934 activity lowers MSANTD3's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 1.95× higher at baseline in the lines without LINC02934 | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSANTD3-TMEFF1]] | C | MSANTD3's natural level strengthens MSANTD3-TMEFF1's drug response | MSANTD3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.50; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[Docetaxel (drug)]] 5 µM | C | MSANTD3's natural level lowers the cells' numbers under Docetaxel 5 µM (makes them more sensitive) | MSANTD3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.334 over the table, 0.050 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.4, -0.2); signed map (40.2, 12.5). **Vector** length 117, 42.9% of its response variance represented; |z| ≥ 3 in 1,621 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.53 to 11); *KRAS signaling up* (hallmark, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.5 | +28.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.3 | +12.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +16.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +13.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +8.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +4.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.6 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -5.0 | +4.2 |
|  | [[NG25 (drug)]] 5 µM |  | -4.6 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -4.0 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.9 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Myb/SANT DNA binding domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:100,427,143-100,451,734 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17337; previously C9orf30 |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Matched by | ensembl_id |

UniProt [Q96H12](https://www.uniprot.org/uniprotkb/Q96H12) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23370) · Entrez [91283](https://www.ncbi.nlm.nih.gov/gene/91283) · UniProt [Q96H12](https://www.uniprot.org/uniprotkb/Q96H12) · Ensembl [ENSG00000066697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066697)

## Data

Gene col 836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 836); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 836]; `tensor/DDL_lfc|DDL_z.npy` [836]; `embed/gene_vectors.npy` [836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 836 or target_col == 836). Every well: [[MSANTD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSANTD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
