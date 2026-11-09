---
symbol: "TANK"
type: "gene"
col: 5880
ensembl_id: "ENSG00000136560"
name: "TRAF family member associated NFKB activator"
location: "2q24.2"
module: 219
arm: "+"
pooled_cpm: 180.49
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# TANK

*TRAF family member associated NFKB activator* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +20.1, q 0e+00, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.445× (z -16.1, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.724× (z -9.4, q 6e-19, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUT7]] (+0.69, fdr 7e-06), [[RBMXL1]] (+0.65, fdr 1e-05), [[ZC3H12C]] (+0.63, fdr 1e-05); moves opposite to [[SEC61A2]] (-0.60, fdr 1e-05), [[C2CD2L]] (-0.57, fdr 2e-05), [[NAP1L4]] (-0.56, fdr 2e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CCL20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +20.1 | 0e+00 | 35/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +13.6 | 8e-40 | 36/48 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +6.5 | 2e-08 | 29/49 (A-172, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.017 | 23/48 (HepG2/C3A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.069 | 21/48 (Hs 766T, HS-578T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.076 | 22/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.076 | 19/48 (HepG2/C3A, BT-474, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.086 | 20/48 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.1 | 0.11 | 14/48 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.15 | 16/48 (HS-578T, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -16.1 | 0e+00 | 38/44 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.464×** | -15.9 | 0e+00 | 45/49 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -10.0 | 2e-21 | 38/45 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -9.4 | 6e-19 | 35/49 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.710×** | -7.1 | 1e-10 | 40/48 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.799×** | -4.6 | 3e-04 | 26/48 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.810×** | -4.4 | 0.001 | 24/48 (HepG2/C3A, NCI-H1792, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.867× | -4.2 | 0.002 | 15/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.830×** | -3.7 | 0.013 | 23/50 (HOP62, RKO, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.779×** | -3.7 | 0.013 | 23/47 (HCT15, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | 0.837× | -3.5 | 0.021 | 23/47 (HT-29, RKO, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.029 | 24/48 (HT-29, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.845× | -3.3 | 0.034 | 23/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.850× | -3.3 | 0.034 | 24/48 (NCI-H1792, COLO 205, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.738×** | -3.3 | 0.037 | 24/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.037 | 19/48 (HCT15, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.866× | -3.0 | 0.096 | 19/48 (COLO 205, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 177 | 6 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +36.2) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -10.5) |
| [[HT-29 (line)]] | alt | 435 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 278 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.6) |
| [[A498 (line)]] | wt | 221 | 4 (2 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.43× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -12.2) |
| [[Hs 766T (line)]] | wt | 214 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +28.0) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 332 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -17.8) |
| [[HOP62 (line)]] | alt | 205 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 180 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +26.9) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 276 | 3 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.17× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 150 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +28.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -16.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 294 | 2 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.32× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.09× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.440× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 213 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -9.9) |
| [[PANC-1 (line)]] | alt | 159 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +31.0) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 205 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -14.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 170 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 184 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -8.9) |
| [[LoVo (line)]] | wt | 136 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.96× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 93.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +28.9) | — |
| [[RKO (line)]] | wt | 190 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -8.6) |
| [[SNU-1 (line)]] | wt | 145 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +23.4) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -18.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 108 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.474× (z -8.6) |
| [[HS-578T (line)]] | alt | 111 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 170 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 180 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.36× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 194 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 136 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -11.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 180 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 97.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 287 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +17.0) | — |
| [[CFPAC-1 (line)]] | alt | 125 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +20.9) | — |
| [[H4 (line)]] | wt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +15.6) | — |
| [[KATO III (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -10.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -11.6) |
| [[LS 180 (line)]] | wt | 170 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -16.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 128 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.1) | — |
| [[CHP-212 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 234 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -8.9) |
| [[HCT15 (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.459× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[RBMXL1]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[ZC3H12C]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ZBTB38]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[IL4R]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ZNF281]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LINC00460]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[IRAK2]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 | pathway: MyD88-independent TLR4 cascade; STRING 421 |
| [[TNIP3]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SETX]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ZNF274]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[EBI3]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[C2CD2L]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[NAP1L4]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PMS2P3-1]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NAPB]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ALG9]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[FHIP2A]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ABCB10]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RPA1]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[VDAC3]] | -0.51 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[KDM1A]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[SCAI]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises TANK's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.37× lower at baseline in the lines without CCL20 | 0.038 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TFPI]] | B | TFPI activity raises TANK's level | lines that do not express TFPI (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without TFPI | 0.040 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |
| [[PI3]] | B | PI3 activity raises TANK's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.24× lower at baseline in the lines without PI3 | 0.051 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[ZC3H12A]] | B | ZC3H12A activity raises TANK's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.5, 8.1); signed map (9.2, 25.1). **Vector** length 116, 36.7% of its response variance represented; |z| ≥ 3 in 1,244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +20.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.3 | +1.7 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -3.0 | -4.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | TRAF family member associated NFKB activator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:161,136,908-161,236,230 (+) |
| Ensembl biotype | protein_coding |
| Also known as | I-TRAF; previously TRAF2 |
| Gene groups (HGNC) | Zinc fingers UBZ1 CCHH-type |
| Hallmark sets | ADIPOGENESIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: Regulation of TBK1, IKKε-mediated activation of IRF3, IRF7 upon TLR3 ligation; Regulation of TBK1, IKKε (IKBKE)-mediated activation of IRF3, IRF7; TICAM1-dependent activation of IRF3/IRF7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92844](https://www.uniprot.org/uniprotkb/Q92844) (TRAF family member-associated NF-kappa-B activator):

> Adapter protein involved in I-kappa-B-kinase (IKK) regulation which constitutively binds TBK1 and IKBKE playing a role in antiviral innate immunity. Acts as a regulator of TRAF function by maintaining them in a latent state. Blocks TRAF2 binding to LMP1 and inhibits LMP1-mediated NF-kappa-B activation. Negatively regulates NF-kappaB signaling and cell survival upon DNA damage. Plays a role as an adapter to assemble ZC3H12A, USP10 in a deubiquitination complex which plays a negative feedback …

**Summary**, from NCBI Gene [10010](https://www.ncbi.nlm.nih.gov/gene/10010):

> The TRAF (tumor necrosis factor receptor-associated factor) family of proteins associate with and transduce signals from members of the tumor necrosis factor receptor superfamily. The protein encoded by this gene is found in the cytoplasm and can bind to TRAF1, TRAF2, or TRAF3, thereby inhibiting TRAF function by sequestering the TRAFs in a latent state in the cytoplasm. For example, the protein encoded by this gene can block TRAF2 binding to LMP1, the Epstein-Barr virus transforming protein, …

**Accessions** — [HGNC:11562](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11562) · Entrez [10010](https://www.ncbi.nlm.nih.gov/gene/10010) · UniProt [Q92844](https://www.uniprot.org/uniprotkb/Q92844) · Ensembl [ENSG00000136560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136560)

## Data

Gene col 5880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5880); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5880]; `tensor/DDL_lfc|DDL_z.npy` [5880]; `embed/gene_vectors.npy` [5880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5880 or target_col == 5880). Every well: [[TANK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TANK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
