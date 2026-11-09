---
symbol: "SETD2"
type: "gene"
col: 11196
ensembl_id: "ENSG00000181555"
name: "SET domain containing 2, histone lysine methyltransferase"
location: "3p21.31"
module: 51
arm: "+"
pooled_cpm: 219.78
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SETD2

*SET domain containing 2, histone lysine methyltransferase* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.17× (z +35.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.503× (z -21.3, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.574× (z -17.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLK1]] (+0.76, fdr 1e-05), [[LSM14A]] (+0.75, fdr 7e-06), [[NIPBL]] (+0.74, fdr 7e-06); moves opposite to [[PMPCA]] (-0.63, fdr 1e-05), [[QSOX1]] (-0.61, fdr 1e-05), [[LINC01128]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +35.3 | 0e+00 | 47/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +24.0 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +18.8 | 0e+00 | 47/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +18.5 | 0e+00 | 47/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +18.0 | 0e+00 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +15.9 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.10×** | +15.3 | 0e+00 | 48/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +14.5 | 1e-45 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +11.3 | 9e-28 | 45/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +9.4 | 3e-19 | 31/47 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +9.3 | 1e-18 | 33/48 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +8.3 | 4e-15 | 33/48 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +6.7 | 1e-09 | 28/48 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +6.5 | 3e-09 | 25/48 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +6.0 | 1e-07 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +5.5 | 2e-06 | 21/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +5.3 | 3e-06 | 19/48 (PANC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -21.3 | 0e+00 | 43/44 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -21.0 | 0e+00 | 47/49 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.574×** | -17.9 | 0e+00 | 46/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.572×** | -15.3 | 0e+00 | 38/45 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.745×** | -13.4 | 6e-39 | 34/49 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.687×** | -12.1 | 1e-31 | 40/48 (A498, SHP-77, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.694×** | -11.3 | 1e-27 | 43/47 (SW1417, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.735×** | -9.5 | 9e-20 | 35/50 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.750×** | -9.3 | 1e-18 | 31/48 (A498, SHP-77, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.783×** | -7.6 | 2e-12 | 28/48 (SNU-423, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -5.8 | 5e-07 | 12/48 (A-172, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -5.5 | 2e-06 | 11/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.801×** | -5.1 | 1e-05 | 26/49 (Hs 766T, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.815×** | -4.7 | 1e-04 | 28/48 (Hs 766T, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.817×** | -4.6 | 1e-04 | 27/48 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.825×** | -4.4 | 3e-04 | 26/47 (SW 1271, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.876× | -4.2 | 6e-04 | 13/48 (NCI-H661, HCT15, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.838× | -4.0 | 0.001 | 22/48 (HS-578T, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.884× | -4.0 | 0.002 | 12/48 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.891× | -3.7 | 0.005 | 8/48 (SW48, BT-474, …) | two highest doses |  |
| [[Simotinib (drug)]] 0.05 µM |  | 0.887× | -3.3 | 0.024 | 5/48 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.904× | -3.2 | 0.026 | 4/47 (hTERT-HPNE, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.891× | -3.1 | 0.037 | 11/47 (SW 1271, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Flutamide (drug)]] 5 µM |  | 0.910× | -3.0 | 0.052 | 2/48 (SW 1088, hTERT-HPNE) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 276 | 9 (1 ⚠) | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +23.5) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.502× (z -16.1) |
| [[KATO III (line)]] | alt | 221 | 8 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +22.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.489× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 229 | 6 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.571× (z -9.5) |
| [[LS 180 (line)]] | wt | 254 | 9 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -10.9) |
| [[SW1417 (line)]] | alt | 384 | 9 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +19.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -16.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 417 | 8 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +24.3) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -16.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 229 | 5 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.522× (z -11.7) |
| [[LoVo (line)]] | wt | 248 | 9 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.599× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 210 | 6 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.566× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 168 | 7 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +22.8) | [[Panobinostat (drug)]] 0.5 µM 0.496× (z -14.4) |
| [[RKO (line)]] | wt | 253 | 7 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +21.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.431× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.516× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 181 | 7 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +22.9) | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 162 | 8 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +25.8) | [[Dinaciclib (drug)]] 5 µM 0.524× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.578× (z -11.0) |
| [[SNU-423 (line)]] | alt | 249 | 3 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.515× (z -11.7) |
| [[A498 (line)]] | wt | 161 | 3 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +23.5) | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 131 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 254 | 5 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +21.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -19.3) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SK-MEL-2 (line)]] | alt | 273 | 2 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.521× (z -11.6) |
| [[A549 (line)]] | wt | 175 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +27.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -14.2) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -13.0) |
| [[BT-474 (line)]] | alt | 161 | 7 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.515× (z -10.2) |
| [[HS-578T (line)]] | alt | 210 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -13.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 272 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -16.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 251 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -17.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 232 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -22.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 195 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +22.5) | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 139 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.559× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 252 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +18.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 226 | 3 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -14.4) |
| [[A-172 (line)]] | wt | 205 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -21.3) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.601× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 138 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.516× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 219 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +19.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.302× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 194 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -16.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 226 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -8.6) |
| [[HT-29 (line)]] | alt | 165 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.594× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 156 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -13.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 123 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.1) | — |
| [[HCT15 (line)]] | alt | 305 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -16.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 212 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -12.0) |
| [[J82 (line)]] | alt | 259 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -12.3) ⚠ cell-cycle shift, explains ~20% of this change |
| [[AN3 CA (line)]] | alt | 354 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 281 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -16.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 260 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.45× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 258 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Capmatinib (drug)]] 5 µM 0.0617× (z -11.1) |
| [[COLO 205 (line)]] | alt | 137 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 160 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.9) | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLK1]] | +0.76 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[LSM14A]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[NIPBL]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 | STRING 771 |
| [[BAZ1B]] | +0.71 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SCAF11]] | +0.71 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CEP350]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SRSF4]] | +0.66 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[PAIP1]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[OBI1]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[CLUAP1]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[COIL]] | +0.64 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMPCA]] | -0.63 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.61 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[LINC01128]] | -0.60 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[RECQL]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[LTBP4]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ARPC2]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[EHBP1L1]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PLCB3]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[AMPD2]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PDCD6]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MLF2]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SETD2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.3, 5.8); signed map (5.3, -14.8). **Vector** length 97.9, 36.3% of its response variance represented; |z| ≥ 3 in 1,513 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +35.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +18.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +0.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.3 | +1.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.4 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.6 | -12.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.3 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -5.8 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 2, histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,016,428-47,164,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HYPB, HIF-1, KIAA1732, FLJ23184, KMT3A |
| Gene groups (HGNC) | Histone lysine methyltransferases; SET domain containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYW2](https://www.uniprot.org/uniprotkb/Q9BYW2) (Histone-lysine N-methyltransferase SETD2):

> Histone methyltransferase that specifically trimethylates 'Lys-36' of histone H3 (H3K36me3) using dimethylated 'Lys-36' (H3K36me2) as substrate. It is capable of trimethylating unmethylated H3K36 (H3K36me0) in vitro. Represents the main enzyme generating H3K36me3, a specific tag for epigenetic transcriptional activation (By similarity). Plays a role in chromatin structure modulation during elongation by coordinating recruitment of the FACT complex and by interacting with hyperphosphorylated …

**Summary**, from NCBI Gene [29072](https://www.ncbi.nlm.nih.gov/gene/29072):

> Huntington's disease (HD), a neurodegenerative disorder characterized by loss of striatal neurons, is caused by an expansion of a polyglutamine tract in the HD protein huntingtin. This gene encodes a protein belonging to a class of huntingtin interacting proteins characterized by WW motifs. This protein is a histone methyltransferase that is specific for lysine-36 of histone H3, and methylation of this residue is associated with active chromatin. This protein also contains a novel …

**Accessions** — [HGNC:18420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18420) · Entrez [29072](https://www.ncbi.nlm.nih.gov/gene/29072) · UniProt [Q9BYW2](https://www.uniprot.org/uniprotkb/Q9BYW2) · Ensembl [ENSG00000181555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181555)

## Data

Gene col 11196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11196); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11196]; `tensor/DDL_lfc|DDL_z.npy` [11196]; `embed/gene_vectors.npy` [11196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11196 or target_col == 11196). Every well: [[SETD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
