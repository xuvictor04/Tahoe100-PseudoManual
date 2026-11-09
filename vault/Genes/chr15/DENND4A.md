---
symbol: "DENND4A"
type: "gene"
col: 10500
ensembl_id: "ENSG00000174485"
name: "DENN domain containing 4A"
location: "15q22.31"
module: 4
arm: "-"
pooled_cpm: 233.32
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 11
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DENND4A

*DENN domain containing 4A* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.07× (z +40.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.431× (z -16.8, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.526× (z -13.4, q 1e-38, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC50A1]] (+0.59, fdr 2e-05), [[SVIP]] (+0.56, fdr 1e-04), [[MAK]] (+0.54, fdr 4e-05); moves opposite to [[TOP3B]] (-0.57, fdr 1e-05), [[TRRAP]] (-0.55, fdr 7e-05), [[CSTF2]] (-0.54, fdr 2e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAJC12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.07×** | +40.2 | 0e+00 | 47/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.62×** | +25.7 | 0e+00 | 47/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +14.4 | 2e-44 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +11.4 | 9e-28 | 31/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +9.0 | 2e-17 | 38/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +9.0 | 2e-17 | 38/48 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +8.5 | 2e-15 | 35/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +8.4 | 2e-15 | 32/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +7.9 | 2e-13 | 35/49 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +7.9 | 2e-13 | 35/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.8 | 3e-13 | 37/48 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.5 | 3e-12 | 29/49 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +7.3 | 1e-11 | 30/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +7.3 | 1e-11 | 39/49 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +6.7 | 6e-10 | 34/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +5.8 | 2e-07 | 32/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -16.8 | 0e+00 | 41/44 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.467×** | -15.9 | 0e+00 | 45/49 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.526×** | -13.4 | 1e-38 | 46/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -8.4 | 8e-15 | 33/48 (RKO, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.702×** | -7.4 | 2e-11 | 34/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.804×** | -4.6 | 5e-04 | 27/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -4.3 | 0.001 | 24/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.2 | 0.002 | 13/48 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.683×** | -4.2 | 0.002 | 24/48 (SHP-77, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.844× | -3.6 | 0.021 | 21/48 (J82, HEC-1-A, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.5 | 0.023 | 19/48 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.847× | -3.5 | 0.023 | 16/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.844× | -3.4 | 0.026 | 19/47 (HepG2/C3A, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.026 | 22/48 (SHP-77, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.026 | 22/47 (NCI-H2030, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.858× | -3.2 | 0.044 | 13/48 (BT-474, HepG2/C3A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.859× | -3.2 | 0.044 | 18/48 (HepG2/C3A, BT-474, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.748×** | -3.2 | 0.047 | 17/49 (COLO 205, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.856× | -3.1 | 0.058 | 11/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.864× | -3.1 | 0.059 | 13/48 (A549, AsPC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.903× | -3.0 | 0.079 | 12/48 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.869× | -3.0 | 0.079 | 12/48 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 125 | 15 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +28.1) | [[Auranofin (drug)]] 5 µM 0.469× (z -11.0) |
| [[LoVo (line)]] | wt | 167 | 12 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +25.4) | [[Auranofin (drug)]] 5 µM 0.414× (z -13.8) |
| [[HOP62 (line)]] | alt | 117 | 13 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +32.4) | [[Auranofin (drug)]] 5 µM 0.350× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 243 | 13 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +33.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.461× (z -9.4) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 93.9 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +28.0) | — |
| [[NCI-H1573 (line)]] | alt | 317 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.27× (z +28.5) | — |
| [[PANC-1 (line)]] | alt | 264 | 9 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +43.8) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -12.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 188 | 7 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +29.6) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 155 | 7 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +29.0) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -10.6) |
| [[A-172 (line)]] | wt | 141 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +33.6) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 453 | 3 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +29.5) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 189 | 8 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +30.7) | [[Auranofin (drug)]] 5 µM 0.253× (z -18.4) |
| [[NCI-H1792 (line)]] | alt | 429 | 6 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +22.5) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -18.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 182 | 6 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +39.6) | [[Auranofin (drug)]] 5 µM 0.301× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 215 | 5 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +30.7) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.632× (z -9.3) |
| [[J82 (line)]] | alt | 197 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +32.7) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.520× (z -10.3) |
| [[BT-474 (line)]] | alt | 199 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +21.9) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 195 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -19.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 248 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +18.8) | — |
| [[SW48 (line)]] | wt | 154 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -18.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 251 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +22.0) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 284 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +32.6) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -11.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 499 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.457× (z -10.4) |
| [[Hs 766T (line)]] | wt | 200 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +23.2) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.454× (z -9.9) |
| [[HT-29 (line)]] | alt | 287 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -12.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 203 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +27.8) | — |
| [[LS 180 (line)]] | wt | 137 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +18.1) | — |
| [[RPMI-7951 (line)]] | alt | 308 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +24.5) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -10.7) |
| [[SNU-423 (line)]] | alt | 173 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +33.5) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -12.1) |
| [[SW 900 (line)]] | alt | 221 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +21.9) | [[Auranofin (drug)]] 5 µM 0.419× (z -9.5) |
| [[SW480 (line)]] | alt | 236 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +12.3) | [[Auranofin (drug)]] 5 µM 0.381× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 217 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +18.6) | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.502× (z -9.0) |
| [[AN3 CA (line)]] | alt | 196 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 202 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 223 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 459 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -14.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 358 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.341× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 209 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +25.4) | [[Auranofin (drug)]] 5 µM 0.415× (z -11.3) |
| [[SW1417 (line)]] | alt | 190 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.537× (z -9.3) |
| [[A-427 (line)]] | wt | 151 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.3) | — |
| [[RKO (line)]] | wt | 313 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.516× (z -11.5) |
| [[CHP-212 (line)]] | wt | 255 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.391× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 278 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 383 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 261 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 157 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +11.8) | — |
| [[NCI-H2122 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC50A1]] | +0.59 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[SVIP]] | +0.56 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[MAK]] | +0.54 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[HES4]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[GPX4]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ACAP1]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PEAK1]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MIEN1]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[SMDT1]] | +0.51 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[IFNAR2]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[COX7B]] | +0.50 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[ABCA5]] | +0.50 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP3B]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TRRAP]] | -0.55 | -0.38 / -0.59 | both halves | 7e-05 | same gene group |
| [[CSTF2]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NUP155]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PSMD12]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[MCM3AP]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GTF3C3]] | -0.51 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[GPN1]] | -0.50 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[HARS1]] | -0.50 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[NAXD]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[RAE1]] | -0.50 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[THAP4]] | -0.49 | -0.31 / -0.64 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC12]] | B | DNAJC12 activity raises DENND4A's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.34× lower at baseline in the lines without DNAJC12 | 0.088 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.382). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.8, -50.1); signed map (46.3, 2.3). **Vector** length 112, 40.3% of its response variance represented; |z| ≥ 3 in 1,652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.9 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +25.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +3.7 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -13.3 | -13.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.2 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.2 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +3.1 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,658,046-65,792,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IRLB; previously MYCPBP |
| Gene groups (HGNC) | DENN domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z401](https://www.uniprot.org/uniprotkb/Q7Z401) (C-myc promoter-binding protein):

> Probable guanine nucleotide exchange factor (GEF) which may activate RAB10. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form. According to PubMed:8056341, it may bind to ISRE-like element (interferon-stimulated response element) of MYC P2 promoter.

**Summary**, from NCBI Gene [10260](https://www.ncbi.nlm.nih.gov/gene/10260):

> This gene encodes a DENN domain-containing protein that may function as a guanine nucleotide exchange factor that specifically activates ras-related protein Rab-10. This protein also contains a interferon stimulated response element-binding domain and may be involved in regulating the v-myc avian myelocytomatosis viral (MYC) oncogene. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 8. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:24321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24321) · Entrez [10260](https://www.ncbi.nlm.nih.gov/gene/10260) · UniProt [Q7Z401](https://www.uniprot.org/uniprotkb/Q7Z401) · Ensembl [ENSG00000174485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174485)

## Data

Gene col 10500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10500); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10500]; `tensor/DDL_lfc|DDL_z.npy` [10500]; `embed/gene_vectors.npy` [10500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10500 or target_col == 10500). Every well: [[DENND4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
