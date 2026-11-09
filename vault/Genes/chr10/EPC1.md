---
symbol: "EPC1"
type: "gene"
col: 4194
ensembl_id: "ENSG00000120616"
name: "enhancer of polycomb 1"
location: "10p11.22"
module: 51
arm: "+"
pooled_cpm: 135.24
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# EPC1

*enhancer of polycomb 1* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +46.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.296× (z -36.2, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.635× (z -19.1, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ING3]] (+0.78, fdr 7e-06), [[COIL]] (+0.76, fdr 7e-06), [[KMT5B]] (+0.76, fdr 7e-06); moves opposite to [[BCAP31]] (-0.67, fdr 7e-06), [[ENTPD4]] (-0.66, fdr 7e-06), [[SETD3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PNPLA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.01×** | +46.4 | 0e+00 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.76×** | +24.9 | 0e+00 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +17.5 | 0e+00 | 43/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +13.8 | 5e-41 | 46/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +12.9 | 4e-36 | 41/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +11.1 | 9e-27 | 41/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +8.5 | 2e-15 | 27/48 (A498, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +7.5 | 5e-12 | 31/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +7.4 | 8e-12 | 28/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +7.2 | 3e-11 | 28/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +6.9 | 2e-10 | 32/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +6.8 | 4e-10 | 27/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +5.1 | 2e-05 | 22/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +4.8 | 6e-05 | 20/48 (J82, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +4.6 | 2e-04 | 21/47 (SNU-1, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 21/49 (A-427, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.296×** | -36.2 | 0e+00 | 48/49 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.361×** | -25.1 | 0e+00 | 42/44 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.492×** | -19.5 | 0e+00 | 39/45 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -19.1 | 0e+00 | 44/49 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.545×** | -18.0 | 0e+00 | 46/48 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.558×** | -17.4 | 0e+00 | 44/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.577×** | -16.3 | 0e+00 | 46/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -15.0 | 0e+00 | 44/50 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -14.2 | 4e-44 | 45/48 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.637×** | -13.4 | 3e-39 | 43/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.716×** | -9.9 | 2e-21 | 32/48 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -9.1 | 4e-18 | 31/48 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -8.7 | 1e-16 | 27/48 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.591×** | -8.2 | 1e-14 | 38/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.792×** | -6.9 | 2e-10 | 27/48 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.816×** | -6.0 | 7e-08 | 27/48 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.833×** | -3.9 | 0.004 | 19/48 (NCI-H23, SK-MEL-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.792×** | -3.6 | 0.009 | 17/46 (H4, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.918× | -3.5 | 0.010 | 10/48 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.893× | -3.3 | 0.020 | 10/47 (RPMI-7951, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 126 | 11 (2 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +34.8) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.6) |
| [[LS 180 (line)]] | wt | 218 | 7 (1 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 149 | 9 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +28.0) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.530× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 131 | 4 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +21.5) | [[Belinostat (drug)]] 5 µM 0.346× (z -14.1) |
| [[PANC-1 (line)]] | alt | 118 | 3 | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +25.5) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -17.8) |
| [[SW480 (line)]] | alt | 145 | 6 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +30.2) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.534× (z -11.8) |
| [[A498 (line)]] | wt | 102 | 5 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +41.8) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -12.8) |
| [[HOP62 (line)]] | alt | 119 | 3 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 203 | 3 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.0988× (z -30.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -13.1) |
| [[A-172 (line)]] | wt | 133 | 5 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +27.2) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -15.8) |
| [[HS-578T (line)]] | alt | 102 | 3 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +19.2) | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 267 | 3 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +22.8) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -13.2) |
| [[KATO III (line)]] | alt | 94.4 | 5 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +25.7) | [[Belinostat (drug)]] 0.5 µM 0.305× (z -15.6) |
| [[LoVo (line)]] | wt | 114 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +24.6) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 133 | 1 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -12.8) |
| [[SNU-1 (line)]] | wt | 166 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.0950× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -18.2) |
| [[C32 (line)]] | wt | 91.3 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 126 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +21.5) | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 173 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +24.5) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 136 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -19.6) |
| [[SNU-423 (line)]] | alt | 127 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +21.3) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.8) |
| [[SW1417 (line)]] | alt | 131 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +25.1) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.455× (z -11.6) |
| [[HT-29 (line)]] | alt | 123 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.466× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 193 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +20.4) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 138 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +27.3) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -13.3) |
| [[J82 (line)]] | alt | 94.6 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +26.4) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 95.3 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +27.7) | [[Belinostat (drug)]] 0.5 µM 0.499× (z -9.5) |
| [[A549 (line)]] | wt | 138 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +27.1) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -11.2) |
| [[H4 (line)]] | wt | 107 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[vincristine (drug)]] 5 µM 0.160× (z -9.3) |
| [[SW 900 (line)]] | alt | 131 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -10.8) |
| [[A-427 (line)]] | wt | 126 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +20.7) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 111 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -13.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 93.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +27.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0784× (z -27.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 176 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +26.7) | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -22.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 241 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0477× (z -30.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.4) |
| [[CHP-212 (line)]] | wt | 159 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[AZD-7648 (drug)]] 5 µM 0.0943× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 195 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -19.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 64.1 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.450× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 107 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +20.2) | [[Lonafarnib (drug)]] 5 µM 0.135× (z -13.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 148 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.5) |
| [[BT-474 (line)]] | alt | 104 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +21.1) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.1) |
| [[AN3 CA (line)]] | alt | 275 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 197 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -14.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 129 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +23.4) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.103× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING3]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes; STRING 996 |
| [[COIL]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[KMT5B]] | +0.76 | +0.79 / +0.62 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[LARP7]] | +0.74 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[CLK4]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[CWC22]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ZNF518A]] | +0.74 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[YJU2]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[NFYC]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ADNP]] | +0.72 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[RBM5]] | +0.72 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[WARS2]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.67 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[ENTPD4]] | -0.66 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[SETD3]] | -0.63 | -0.55 / -0.56 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[LIMK1]] | -0.62 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[MXRA7]] | -0.61 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[MAPK9]] | -0.61 | -0.56 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNPLA4]] | B | PNPLA4 activity lowers EPC1's level | lines that do not express PNPLA4 (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without PNPLA4 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000285679, PRKCZ, GPR160 |
| [[ID3]] | B | ID3 activity raises EPC1's level | lines that do not express ID3 (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without ID3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |
| [[TOP2A]] | B | TOP2A activity raises EPC1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.877). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.8, 11.3); signed map (6.9, -19.2). **Vector** length 121, 42.2% of its response variance represented; |z| ≥ 3 in 1,424 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.0 | +24.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.7 | +46.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +10.5 | +8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.8 | +17.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.4 | +11.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +3.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.5 | +1.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.2 | -13.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.8 | -9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -14.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.0 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -8.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.7 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | enhancer of polycomb 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22 — chr10:32,267,751-32,378,798 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Epl1 |
| Gene groups (HGNC) | Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 4 pathways, smallest: Transcriptional Regulation by E2F6; HATs acetylate histones; Chromatin modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2F5](https://www.uniprot.org/uniprotkb/Q9H2F5) (Enhancer of polycomb homolog 1):

> Component of the NuA4 histone acetyltransferase (HAT) complex, a multiprotein complex involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. The NuA4 complex plays a direct role in repair of DNA double-strand breaks (DSBs) by promoting homologous recombination (HR). The NuA4 complex is also required for spermatid development by promoting acetylation of histones: histone acetylation is required for histone replacement during the …

**Summary**, from NCBI Gene [80314](https://www.ncbi.nlm.nih.gov/gene/80314):

> This gene encodes a member of the polycomb group (PcG) family. The encoded protein is a component of the NuA4 histone acetyltransferase complex and can act as both a transcriptional activator and repressor. The encoded protein has been linked to apoptosis, DNA repair, skeletal muscle differentiation, gene silencing, and adult T-cell leukemia/lymphoma. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:19876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19876) · Entrez [80314](https://www.ncbi.nlm.nih.gov/gene/80314) · UniProt [Q9H2F5](https://www.uniprot.org/uniprotkb/Q9H2F5) · Ensembl [ENSG00000120616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120616)

## Data

Gene col 4194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4194); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4194]; `tensor/DDL_lfc|DDL_z.npy` [4194]; `embed/gene_vectors.npy` [4194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4194 or target_col == 4194). Every well: [[EPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
