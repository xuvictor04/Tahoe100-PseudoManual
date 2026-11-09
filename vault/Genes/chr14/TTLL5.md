---
symbol: "TTLL5"
type: "gene"
col: 4098
ensembl_id: "ENSG00000119685"
name: "tubulin tyrosine ligase like 5"
location: "14q24.3"
module: 68
arm: "-"
pooled_cpm: 145.75
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TTLL5

*tubulin tyrosine ligase like 5* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.27× (z +19.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.548× (z -13.9, q 2e-41, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.570× (z -13.0, q 3e-36, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R12B]] (+0.66, fdr 2e-05), [[RTTN]] (+0.64, fdr 1e-05), [[CDKAL1]] (+0.63, fdr 7e-06); moves opposite to [[LTO1]] (-0.65, fdr 2e-05), [[ZBTB21]] (-0.64, fdr 1e-05), [[FRMD6-AS2]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +19.0 | 0e+00 | 48/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +16.2 | 0e+00 | 48/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +16.1 | 0e+00 | 48/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.8 | 1e-06 | 31/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +5.7 | 1e-06 | 40/49 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +5.0 | 6e-05 | 26/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.24×** | +4.8 | 1e-04 | 26/48 (SW 900, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.17× | +3.3 | 0.081 | 16/48 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.084 | 20/49 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.15× | +3.2 | 0.084 | 17/48 (HS-578T, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4098.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -13.9 | 2e-41 | 45/49 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.570×** | -13.0 | 3e-36 | 38/48 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -12.8 | 3e-35 | 39/44 (HCT15, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.587×** | -11.4 | 4e-28 | 39/45 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -10.4 | 3e-23 | 38/48 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -9.3 | 2e-18 | 38/48 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.669×** | -8.9 | 3e-17 | 36/47 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -8.7 | 3e-16 | 31/49 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.778×** | -8.2 | 1e-14 | 26/48 (KATO III, HOP62, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -7.6 | 2e-12 | 35/48 (C32, LOX-IMVI, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.756×** | -6.5 | 5e-09 | 32/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -6.1 | 4e-08 | 26/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -4.8 | 9e-05 | 13/49 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.817×** | -4.7 | 1e-04 | 27/49 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -4.3 | 6e-04 | 16/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.841× | -4.0 | 0.002 | 20/47 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.844× | -3.6 | 0.009 | 19/47 (NCI-H460, C32, …) | all doses, flat | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.861× | -3.5 | 0.014 | 20/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.903× | -3.3 | 0.020 | 6/49 (MIA PaCa-2, CHP-212, …) | rises with dose |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.873× | -3.2 | 0.038 | 9/48 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.819×** | -3.0 | 0.059 | 18/48 (RKO, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.883× | -2.9 | 0.084 | 15/48 (LOX-IMVI, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 242 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 204 | 3 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.533× (z -9.5) |
| [[HS-578T (line)]] | alt | 68.8 | 9 | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.70× (z +10.2) | — |
| [[KATO III (line)]] | alt | 144 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -14.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 177 | 4 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -10.4) |
| [[A498 (line)]] | wt | 92.8 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +10.7) | [[Harringtonine (drug)]] 0.5 µM 0.396× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 122 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +13.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 150 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +13.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.446× (z -10.9) |
| [[PANC-1 (line)]] | alt | 126 | 4 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.54× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.504× (z -11.2) |
| [[SW480 (line)]] | alt | 198 | 1 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.66× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.428× (z -16.9) |
| [[HOP62 (line)]] | alt | 131 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -14.1) |
| [[SW1417 (line)]] | alt | 135 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -15.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.531× (z -9.0) |
| [[A549 (line)]] | wt | 139 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 2.57× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 71.6 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 3.43× (z +11.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 140 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.528× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 127 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.512× (z -9.9) |
| [[A-427 (line)]] | wt | 147 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -11.7) |
| [[C32 (line)]] | wt | 137 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.346× (z -12.5) |
| [[HCT15 (line)]] | alt | 163 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -10.6) |
| [[LoVo (line)]] | wt | 117 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -12.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.457× (z -11.9) |
| [[LS 180 (line)]] | wt | 131 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 2.54× (z +12.3) | [[Harringtonine (drug)]] 0.5 µM 0.493× (z -9.5) |
| [[RKO (line)]] | wt | 147 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -11.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.433× (z -10.2) |
| [[C-33 A (line)]] | alt | 186 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -11.7) |
| [[J82 (line)]] | alt | 173 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 140 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 2.67× (z +13.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 201 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.547× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 135 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.13× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -8.6) |
| [[A-172 (line)]] | wt | 59.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.83× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 133 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.27× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 106 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -8.5) |
| [[HT-29 (line)]] | alt | 121 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.445× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 231 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 176 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.412× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 127 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 192 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.416× (z -10.1) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 201 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -11.7) |
| [[H4 (line)]] | wt | 111 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -11.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.4) |
| [[SNU-423 (line)]] | alt | 139 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -11.1) |
| [[SW48 (line)]] | wt | 180 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +11.1) | — |
| [[SNU-1 (line)]] | wt | 126 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 160 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12B]] | +0.66 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[RTTN]] | +0.64 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CDKAL1]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SPIDR]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SNRNP25]] | +0.62 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[CEP152]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SHMT1]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NUP85]] | +0.60 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[ZDHHC12]] | +0.60 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[SLF1]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ULK4]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[AP2S1]] | +0.59 | +0.51 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTO1]] | -0.65 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ZBTB21]] | -0.64 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[FRMD6-AS2]] | -0.63 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SOCS2-AS1]] | -0.63 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[MMRN2]] | -0.63 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[RGS20]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[BCDIN3D]] | -0.62 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[FKRP]] | -0.61 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[ZNF425]] | -0.60 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[FEZ1]] | -0.59 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ZNF621]] | -0.59 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[LINC02542]] | -0.58 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TTLL5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ERG28]] | C | ERG28's natural level strengthens TTLL5's drug response | ERG28's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.15; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **-** arm (projection on the module's main direction -0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (10.2, 7.7); signed map (-37.9, -38.8). **Vector** length 128, 43.8% of its response variance represented; |z| ≥ 3 in 1,456 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +19.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.7 | +16.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +16.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.7 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +2.7 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +3.6 | +2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +3.4 | +1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -14.3 | -13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -11.6 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -11.5 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -10.7 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.1 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.7 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.4 | -7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,633,625-75,955,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STAMP; previously KIAA0998 |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6EMB2](https://www.uniprot.org/uniprotkb/Q6EMB2) (Tubulin polyglutamylase TTLL5):

> Polyglutamylase which modifies tubulin, generating polyglutamate side chains on the gamma-carboxyl group of specific glutamate residues within the C-terminal tail of tubulin. Preferentially mediates ATP-dependent initiation step of the polyglutamylation reaction over the elongation step. Preferentially modifies the alpha-tubulin tail over a beta-tail (By similarity). Required for CCSAP localization to both polyglutamylated spindle and cilia microtubules. Increases the effects of transcriptional …

**Summary**, from NCBI Gene [23093](https://www.ncbi.nlm.nih.gov/gene/23093):

> This gene encodes a member of the tubulin tyrosine ligase like protein family. This protein interacts with two glucocorticoid receptor coactivators, transcriptional intermediary factor 2 and steroid receptor coactivator 1. This protein may function as a coregulator of glucocorticoid receptor mediated gene induction and repression. This protein may also function as an alpha tubulin polyglutamylase.[provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:19963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19963) · Entrez [23093](https://www.ncbi.nlm.nih.gov/gene/23093) · UniProt [Q6EMB2](https://www.uniprot.org/uniprotkb/Q6EMB2) · Ensembl [ENSG00000119685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119685)

## Data

Gene col 4098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4098); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4098]; `tensor/DDL_lfc|DDL_z.npy` [4098]; `embed/gene_vectors.npy` [4098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4098 or target_col == 4098). Every well: [[TTLL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
