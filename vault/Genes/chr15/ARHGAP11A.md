---
symbol: "ARHGAP11A"
type: "gene"
col: 12694
ensembl_id: "ENSG00000198826"
name: "Rho GTPase activating protein 11A"
location: "15q13.3"
module: 22
arm: "+"
pooled_cpm: 64.42
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 37
n_dd_up_clean: 8
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ARHGAP11A

*Rho GTPase activating protein 11A* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (18 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.81× (z +9.6, q 1e-19, up in 40 of 45 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.37× (z +4.7, q 8e-05, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (16 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.588× (z -11.0, q 2e-25, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~75% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.603× (z -10.6, q 7e-24, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1B]] (+0.96, fdr 7e-06), [[KIF4A]] (+0.94, fdr 7e-06), [[KIF23]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **1.81×** | +9.6 | 1e-19 | 40/45 (HOP62, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.85×** | +9.6 | 1e-19 | 31/43 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.80×** | +9.6 | 1e-19 | 36/46 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +6.3 | 3e-08 | 27/47 (NCI-H2347, Panc 03.27, …) | top dose only | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.33×** | +6.2 | 8e-08 | 37/47 (NCI-H2030, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.43×** | +5.8 | 8e-07 | 24/46 (A549, PANC-1, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.42×** | +5.5 | 3e-06 | 30/46 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.38×** | +5.2 | 1e-05 | 24/47 (KATO III, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.38×** | +5.2 | 1e-05 | 29/47 (KATO III, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +5.0 | 3e-05 | 27/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.36×** | +5.0 | 3e-05 | 27/46 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.79×** | +5.0 | 3e-05 | 25/46 (PANC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.8 | 6e-05 | 25/47 (RKO, PANC-1, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +4.8 | 6e-05 | 24/46 (KATO III, HOP62, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 8e-05 | 26/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.34×** | +4.7 | 9e-05 | 24/46 (HOP62, H4, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.26×** | +4.6 | 1e-04 | 22/47 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +4.4 | 3e-04 | 22/46 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.001 | 18/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 22/47 (C32, KATO III, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 20/47 (A-172, LoVo, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.026 | 19/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.588×** | -11.0 | 2e-25 | 39/47 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -10.6 | 7e-24 | 34/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -7.8 | 1e-12 | 31/47 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.598×** | -6.8 | 2e-09 | 29/47 (HOP62, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.665×** | -6.4 | 1e-08 | 33/47 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.679×** | -6.3 | 2e-08 | 38/47 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.689×** | -6.1 | 1e-07 | 30/47 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.577×** | -5.7 | 1e-06 | 32/47 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -5.4 | 5e-06 | 29/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **0.565×** | -4.9 | 6e-05 | 28/43 (KATO III, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.746×** | -4.8 | 9e-05 | 23/47 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.752×** | -4.7 | 2e-04 | 24/47 (SNU-1, NCI-H1573, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.763×** | -4.4 | 4e-04 | 24/47 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.4 | 4e-04 | 25/46 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.686×** | -4.4 | 4e-04 | 22/47 (A549, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.779×** | -4.1 | 0.001 | 17/47 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.625×** | -4.0 | 0.002 | 22/47 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.834× | -4.0 | 0.002 | 22/47 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.830×** | -4.0 | 0.002 | 19/47 (HCT15, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.818×** | -3.8 | 0.003 | 17/47 (A-427, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.785×** | -3.7 | 0.006 | 15/47 (NCI-H2347, C-33 A, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.785×** | -3.7 | 0.006 | 18/46 (NCI-H661, LOX-IMVI, …) | all doses, flat |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.014 | 14/46 (SHP-77, LoVo, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.849× | -3.4 | 0.015 | 18/47 (MIA PaCa-2, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.90 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 84.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 57.2 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.204× (z -14.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.392× (z -9.9) |
| [[LS 180 (line)]] | wt | 56.4 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.211× (z -13.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.322× (z -10.4) |
| [[A-172 (line)]] | wt | 41.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.39× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.309× (z -10.4) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A-427 (line)]] | wt | 88.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.341× (z -12.2) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.456× (z -10.0) |
| [[LoVo (line)]] | wt | 53.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.320× (z -11.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.445× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 50.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 50.8 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -12.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 83.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.431× (z -9.3) |
| [[HOP62 (line)]] | alt | 86.0 | 1 (1 ⚠) | 1 | [[Docetaxel (drug)]] 0.05 µM 2.33× (z +8.7) ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 32.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[NCI-H23 (line)]] | alt | 77.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 50.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.369× (z -10.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -10.2) |
| [[PANC-1 (line)]] | alt | 91.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.6) |
| [[SHP-77 (line)]] | alt | 117 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -8.9) |
| [[H4 (line)]] | wt | 79.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -10.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HS-578T (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 66.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[NCI-H1573 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2030 (line)]] | alt | 72.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H661 (line)]] | alt | 92.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0774× (z -10.1) |
| [[RKO (line)]] | wt | 83.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SNU-1 (line)]] | wt | 95.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.234× (z -10.0) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW1417 (line)]] | alt | 81.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[SW48 (line)]] | wt | 91.4 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.420× (z -9.0) |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 84.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1B]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | STRING 796 |
| [[KIF4A]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | STRING 682 |
| [[KIF23]] | +0.93 | +0.94 / +0.92 | both halves | 7e-06 | STRING 625 |
| [[TPX2]] | +0.93 | +0.93 / +0.91 | both halves | 7e-06 | STRING 553 |
| [[CCNA2]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | STRING 715 |
| [[DLGAP5]] | +0.93 | +0.92 / +0.91 | both halves | 7e-06 | STRING 801 |
| [[BUB1]] | +0.92 | +0.93 / +0.92 | both halves | 7e-06 | STRING 766 |
| [[MKI67]] | +0.92 | +0.93 / +0.90 | both halves | 7e-06 | STRING 812 |
| [[BIRC5]] | +0.92 | +0.92 / +0.89 | both halves | 7e-06 | STRING 581 |
| [[INCENP]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[PRC1]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | STRING 535 |
| [[KIF11]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | STRING 821 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises ARHGAP11A's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without PIMREG | 0.016 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[HYLS1]] | B | HYLS1 activity raises ARHGAP11A's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[MYEF2]] | B | MYEF2 activity raises ARHGAP11A's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.27× lower at baseline in the lines without MYEF2 | 0.082 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |
| [[MYBL1]] | B | MYBL1 activity raises ARHGAP11A's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without MYBL1 | 0.087 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises ARHGAP11A's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without NEURL1B | 0.089 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises ARHGAP11A's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without NDC80 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises ARHGAP11A's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.43× lower at baseline in the lines without PBK | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ARHGAP11A's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without AURKB | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises ARHGAP11A's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.69× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[SKA3]] | C | SKA3 activity raises ARHGAP11A's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises ARHGAP11A's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[TP53]] | C | TP53 activity strengthens ARHGAP11A's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 16 not recorded | the TP53-altered lines respond 0.93× as strongly (z diff +0.11); strongest at Selinexor 5 µM: 0.68x vs 0.36x (z diff +4.3) | 0.801 over the table, 0.058 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.938). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -55.3); signed map (-49.1, -43.3). **Vector** length 160, 59.3% of its response variance represented; |z| ≥ 3 in 1,278 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.75 to 60); *DREAM G2/M down* (control, mean cos +0.84 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.73 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | +6.3 | +9.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.4 | +5.8 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +5.2 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.8 | +9.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.8 | +4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.7 | +4.7 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.6 | +4.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | -7.0 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -6.1 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -6.1 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -5.8 | -11.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.8 | -4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 11A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:32,615,144-32,639,941 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0013 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4F7](https://www.uniprot.org/uniprotkb/Q6P4F7) (Rho GTPase-activating protein 11A):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [9824](https://www.ncbi.nlm.nih.gov/gene/9824):

> This gene encodes a member of the Rho GTPase activating protein family. In response to DNA damage, the encoded protein interacts with the p53 tumor suppressor protein and stimulates its tetramerization, which results in cell-cycle arrest and apoptosis. A chromosomal deletion that includes this gene is one cause of Prader-Willi syndrome, and an intronic variant of this gene may be associated with sleep duration in children. This gene is highly expressed in colon cancers and in a human basal-like …

**Accessions** — [HGNC:15783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15783) · Entrez [9824](https://www.ncbi.nlm.nih.gov/gene/9824) · UniProt [Q6P4F7](https://www.uniprot.org/uniprotkb/Q6P4F7) · Ensembl [ENSG00000198826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198826)

## Data

Gene col 12694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12694); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12694]; `tensor/DDL_lfc|DDL_z.npy` [12694]; `embed/gene_vectors.npy` [12694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12694 or target_col == 12694). Every well: [[ARHGAP11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
