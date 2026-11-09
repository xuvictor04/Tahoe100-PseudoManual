---
symbol: "MLLT3"
type: "gene"
col: 10172
ensembl_id: "ENSG00000171843"
name: "MLLT3 super elongation complex subunit"
location: "9p21.3"
module: 99
arm: "+"
pooled_cpm: 145.4
n_lines_expressing: 44
n_dd_up: 12
n_dd_down: 44
n_dd_up_clean: 11
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 16
direction_downstream: 17
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# MLLT3

*MLLT3 super elongation complex subunit* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.40× (z +6.2, q 3e-07, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.379× (z -25.3, q 0e+00, down in 37 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLOD2]] (+0.66, fdr 7e-06), [[WDR54]] (+0.65, fdr 8e-06), [[SAP30-DT]] (+0.64, fdr 7e-06); moves opposite to [[DPH5-DT]] (-0.59, fdr 1e-05), [[GNL3L]] (-0.57, fdr 1e-05), [[PCBD2]] (-0.56, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); 17 go from it, the strongest it → [[OPLAH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 3e-07 | 31/43 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.0 | 4e-07 | 24/42 (SW1417, KATO III, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +6.0 | 4e-07 | 32/41 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +5.4 | 8e-06 | 29/43 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +5.2 | 2e-05 | 26/42 (RKO, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +4.6 | 4e-04 | 21/43 (HOP62, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 8e-04 | 26/41 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.001 | 21/42 (HOP62, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +4.3 | 0.001 | 24/44 (HOP62, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.009 | 22/42 (C32, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.015 | 16/42 (HOP62, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.016 | 13/42 (HOP62, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.016 | 19/43 (HOP62, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.036 | 16/42 (KATO III, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.077 | 14/42 (HOP62, KATO III, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.079 | 10/42 (LoVo, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.379×** | -25.3 | 0e+00 | 37/42 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.285×** | -22.2 | 0e+00 | 37/37 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.315×** | -21.3 | 0e+00 | 37/42 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.301×** | -21.3 | 0e+00 | 40/42 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.320×** | -19.4 | 0e+00 | 36/39 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.365×** | -18.6 | 0e+00 | 38/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.365×** | -18.6 | 0e+00 | 35/42 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.377×** | -18.0 | 0e+00 | 41/42 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.402×** | -16.8 | 0e+00 | 37/42 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.424×** | -15.8 | 0e+00 | 40/42 (C32, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.503×** | -12.2 | 2e-32 | 34/41 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.524×** | -11.9 | 4e-31 | 37/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.561×** | -10.7 | 6e-25 | 34/42 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.600×** | -9.4 | 2e-19 | 34/42 (C32, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.626×** | -8.7 | 2e-16 | 34/41 (RPMI-7951, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.731×** | -8.2 | 1e-14 | 28/43 (RKO, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.644×** | -8.1 | 2e-14 | 27/42 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.662×** | -7.6 | 8e-13 | 34/42 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.676×** | -7.2 | 1e-11 | 27/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.662×** | -6.8 | 3e-10 | 30/42 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.740×** | -5.4 | 2e-06 | 21/41 (HOP62, RKO, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 344 | 1 | 22 (12 ⚠) | [[Ponatinib (drug)]] 5 µM 2.00× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -34.8) |
| [[SNU-423 (line)]] | alt | 178 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -25.0) |
| [[NCI-H460 (line)]] | wt | 203 | 0 | 18 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -23.4) |
| [[SNU-1 (line)]] | wt | 214 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -24.8) |
| [[SW480 (line)]] | alt | 86.4 | 1 (1 ⚠) | 16 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.1) ⚠ cell-cycle shift, explains ~47% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -23.1) |
| [[SW 900 (line)]] | alt | 134 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -23.6) |
| [[HOP62 (line)]] | alt | 162 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -29.0) |
| [[LOX-IMVI (line)]] | wt | 331 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.219× (z -17.8) |
| [[RKO (line)]] | wt | 64.6 | 3 (1 ⚠) | 11 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 3.26× (z +9.2) | [[Harringtonine (drug)]] 0.5 µM 0.171× (z -13.9) |
| [[H4 (line)]] | wt | 189 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -14.0) |
| [[HCT15 (line)]] | alt | 278 | 0 | 13 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.169× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 264 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -23.4) |
| [[RPMI-7951 (line)]] | alt | 212 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0760× (z -28.6) |
| [[A-172 (line)]] | wt | 200 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -25.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.288× (z -15.4) |
| [[C-33 A (line)]] | alt | 194 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.263× (z -13.4) |
| [[HT-29 (line)]] | alt | 438 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.282× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 55.1 | 4 (3 ⚠) | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.46× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.70× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.6) |
| [[HepG2_C3A (line)]] | wt | 84.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -22.1) |
| [[J82 (line)]] | alt | 129 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -19.3) |
| [[SK-MEL-2 (line)]] | alt | 163 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0738× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.228× (z -21.8) |
| [[LS 180 (line)]] | wt | 254 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -13.1) |
| [[HS-578T (line)]] | alt | 107 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.300× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 242 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.360× (z -10.7) |
| [[KATO III (line)]] | alt | 125 | 1 | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.83× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -18.7) |
| [[LoVo (line)]] | wt | 299 | 1 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -32.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 71.8 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -19.1) |
| [[Panc 03.27 (line)]] | alt | 145 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 74.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.1) |
| [[SHP-77 (line)]] | alt | 109 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.399× (z -9.6) |
| [[A549 (line)]] | wt | 221 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 225 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.0) |
| [[COLO 205 (line)]] | alt | 84.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.7) |
| [[A498 (line)]] | wt | 213 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.482× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.190× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 40.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 4.11× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -9.8) |
| [[SW48 (line)]] | wt | 78.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.8) |
| [[CHP-212 (line)]] | wt | 255 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -13.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -14.8) |
| [[SW1417 (line)]] | alt | 45.9 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.37× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.8) |
| [[SW 1088 (line)]] | alt | 161 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.147× (z -9.1) |
| [[A-427 (line)]] | wt | 28.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 34.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 50.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLOD2]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[WDR54]] | +0.65 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[SAP30-DT]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[IPMK]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CDON]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MXI1]] | +0.63 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 | same gene group |
| [[FAM162A]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RAB20]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ARL6]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[RBPJ]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.60 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH5-DT]] | -0.59 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PCBD2]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 | same gene group |
| [[PIGL]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 | same gene group |
| [[ITPA]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[AVEN]] | -0.51 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[TXNRD3]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ERMAP]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ZNF783]] ⚠ | -0.50 | -0.43 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[OPLAH]] ⚠ | -0.49 | -0.45 / -0.48 | both halves | 3e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises MLLT3's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.95× lower at baseline in the lines without PLOD2 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[CA12]] | B | CA12 activity raises MLLT3's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.28× lower at baseline in the lines without CA12 | 0.002 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[LIMCH1]] | B | LIMCH1 activity raises MLLT3's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 2.24× lower at baseline in the lines without LIMCH1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[RORA]] | B | RORA activity raises MLLT3's level | lines that do not express RORA (8) vs lines expressing it (42) | 3.31× lower at baseline in the lines without RORA | 0.016 | ⚠ within organs, on part of the lines; also absent: DPF3, TMC3-AS1 |
| [[RNF144B]] | B | RNF144B activity raises MLLT3's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without RNF144B | 0.022 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MLLT3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM13A]] | B | FAM13A activity raises MLLT3's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without FAM13A | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[RARB]] | B | RARB activity raises MLLT3's level | lines that do not express RARB (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without RARB | 0.038 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[SNAP25]] | B | SNAP25 activity raises MLLT3's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without SNAP25 | 0.051 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[CA12]] | B | CA12 activity weakens MLLT3's drug response | lines that do not express CA12 (23) vs lines expressing it (20) | the lines without CA12 respond 1.08× as strongly (z diff -0.62); strongest at Homoharringtonine 0.5 µM: 0.32x vs 0.40x (z diff -2.5) | 0.060 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; target measured in part of the lines; both ways; artifact flags |
| [[NDNF]] | B | NDNF activity raises MLLT3's level | lines that do not express NDNF (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without NDNF | 0.069 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[PPP1R3C]] | B | PPP1R3C activity raises MLLT3's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.20× lower at baseline in the lines without PPP1R3C | 0.077 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OPLAH]] | B | MLLT3 activity lowers OPLAH's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.01× higher at baseline in the lines without MLLT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[NFIL3]] | B | MLLT3 activity raises NFIL3's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without MLLT3 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[FAM13A]] | B | MLLT3 activity raises FAM13A's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.61× lower at baseline in the lines without MLLT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[TCAF2]] | B | MLLT3 activity raises TCAF2's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.16× lower at baseline in the lines without MLLT3 | 0.016 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[PLOD2]] | B | MLLT3 activity raises PLOD2's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 4.00× lower at baseline in the lines without MLLT3 | 0.030 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[RNF24]] | B | MLLT3 activity raises RNF24's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without MLLT3 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[LIMCH1]] | B | MLLT3 activity raises LIMCH1's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 4.97× lower at baseline in the lines without MLLT3 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[RORA]] | B | MLLT3 activity raises RORA's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 3.40× lower at baseline in the lines without MLLT3 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[DIPK2A]] | B | MLLT3 activity raises DIPK2A's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without MLLT3 | 0.043 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[HELZ]] | B | MLLT3 activity raises HELZ's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without MLLT3 | 0.045 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[HILPDA]] | B | MLLT3 activity raises HILPDA's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without MLLT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[NDRG1]] | B | MLLT3 activity raises NDRG1's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.35× lower at baseline in the lines without MLLT3 | 0.071 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, -15.4); signed map (-34.7, 24.3). **Vector** length 112, 38.6% of its response variance represented; |z| ≥ 3 in 1,734 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Gluconeogenesis* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +6.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.2 | -22.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.9 | -19.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.4 | -3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -4.1 | -3.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.9 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.8 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | MLLT3 super elongation complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:20,341,669-20,622,499 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AF-9, AF9, YEATS3 |
| Gene groups (HGNC) | Super elongation complex; YEATS domain containing; MicroRNA protein coding host genes |
| Reactome | 7 pathways, smallest: Formation of RNA Pol II elongation complex; RNA Polymerase II Transcription Elongation; RNA Polymerase II Pre-transcription Events |
| Matched by | ensembl_id |

**Function**, from UniProt [P42568](https://www.uniprot.org/uniprotkb/P42568) (Protein AF-9):

> Chromatin reader component of the super elongation complex (SEC), a complex required to increase the catalytic rate of RNA polymerase II transcription by suppressing transient pausing by the polymerase at multiple sites along the DNA. Specifically recognizes and binds acylated histone H3, with a preference for histone H3 that is crotonylated. Crotonylation marks active promoters and enhancers and confers resistance to transcriptional repressors. Recognizes and binds histone H3 crotonylated at …

**Summary**, from NCBI Gene [4300](https://www.ncbi.nlm.nih.gov/gene/4300):

> Enables several functions, including chromatin binding activity; histone H3 reader activity; and histone binding activity. Involved in several processes, including hematopoietic stem cell differentiation; positive regulation of DNA-templated transcription; and regulation of stem cell division. Acts upstream of or within negative regulation of canonical Wnt signaling pathway and positive regulation of Wnt signaling pathway, planar cell polarity pathway. Located in nucleoplasm. Part of …

**Accessions** — [HGNC:7136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7136) · Entrez [4300](https://www.ncbi.nlm.nih.gov/gene/4300) · UniProt [P42568](https://www.uniprot.org/uniprotkb/P42568) · Ensembl [ENSG00000171843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171843)

## Data

Gene col 10172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10172); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10172]; `tensor/DDL_lfc|DDL_z.npy` [10172]; `embed/gene_vectors.npy` [10172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10172 or target_col == 10172). Every well: [[MLLT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLLT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
