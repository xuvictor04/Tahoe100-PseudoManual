---
symbol: "SLC7A1"
type: "gene"
col: 6312
ensembl_id: "ENSG00000139514"
name: "solute carrier family 7 member 1"
location: "13q12.3"
module: 63
arm: "+"
pooled_cpm: 140.29
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 22
n_dd_up_clean: 19
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SLC7A1

*solute carrier family 7 member 1* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.49× (z +13.9, q 2e-41, up in 42 of 47 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.58× (z +11.2, q 5e-27, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.490× (z -24.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARS1]] (+0.75, fdr 7e-06), [[YARS1]] (+0.74, fdr 7e-06), [[IARS1]] (+0.72, fdr 7e-06); moves opposite to [[ZNF654]] (-0.52, fdr 1e-05), [[FGFR1OP2]] (-0.47, fdr 3e-05), [[ARRDC3]] (-0.47, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ position correction uncertain | **1.49×** | +13.9 | 2e-41 | 42/47 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +13.6 | 7e-40 | 45/47 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +12.6 | 4e-34 | 40/46 (Hs 766T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.58×** | +11.2 | 5e-27 | 40/47 (Hs 766T, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.56×** | +10.9 | 2e-25 | 42/47 (SW48, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM | ⚠ position correction uncertain | **1.43×** | +8.7 | 3e-16 | 38/46 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +8.6 | 9e-16 | 30/47 (NCI-H460, NCI-H2030, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +8.0 | 6e-14 | 32/46 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +7.8 | 4e-13 | 30/47 (Panc 03.27, Hs 766T, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.37×** | +7.7 | 7e-13 | 30/47 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.34×** | +7.2 | 3e-11 | 34/47 (RKO, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +7.0 | 1e-10 | 27/46 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +6.7 | 1e-09 | 20/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +6.5 | 4e-09 | 28/47 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +6.2 | 2e-08 | 23/46 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +6.1 | 4e-08 | 30/47 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +5.8 | 3e-07 | 23/47 (HCT15, NCI-H1573, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.18× | +5.6 | 6e-07 | 18/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +5.2 | 6e-06 | 21/47 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +4.9 | 2e-05 | 21/47 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.46×** | +4.9 | 3e-05 | 25/47 (SW 900, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +4.7 | 5e-05 | 23/47 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | **1.44×** | +4.7 | 6e-05 | 21/47 (Hs 766T, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.490×** | -24.8 | 0e+00 | 44/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.433×** | -20.5 | 0e+00 | 42/47 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.461×** | -19.0 | 0e+00 | 44/47 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -17.7 | 0e+00 | 44/47 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -12.6 | 3e-34 | 37/47 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -11.2 | 3e-27 | 33/49 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.738×** | -10.5 | 4e-24 | 35/47 (RKO, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.674×** | -9.7 | 2e-20 | 32/47 (SW48, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -9.7 | 3e-20 | 35/48 (RKO, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.683×** | -9.3 | 5e-19 | 35/47 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.766×** | -9.3 | 1e-18 | 27/47 (RKO, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -8.6 | 3e-16 | 26/46 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -7.9 | 2e-13 | 27/47 (SNU-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.742×** | -7.1 | 7e-11 | 28/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -6.9 | 2e-10 | 26/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.774×** | -6.3 | 1e-08 | 24/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 268 | 0 | 17 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -17.6) |
| [[LoVo (line)]] | wt | 210 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -26.6) |
| [[RKO (line)]] | wt | 226 | 0 | 17 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -32.0) |
| [[HT-29 (line)]] | alt | 557 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -23.2) |
| [[HEC-1-A (line)]] | alt | 210 | 1 (1 ⚠) | 12 | [[Artesunate (drug)]] 5 µM 1.50× (z +8.7) ⚠ position correction uncertain | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -30.9) |
| [[SW48 (line)]] | wt | 376 | 0 | 13 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -21.8) |
| [[SW480 (line)]] | alt | 214 | 1 (1 ⚠) | 12 (2 ⚠) | [[Artesunate (drug)]] 5 µM 1.57× (z +9.8) ⚠ position correction uncertain | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -25.9) |
| [[A498 (line)]] | wt | 138 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -24.0) |
| [[LS 180 (line)]] | wt | 203 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -27.0) |
| [[PANC-1 (line)]] | alt | 130 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -21.3) |
| [[SW1417 (line)]] | alt | 128 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -23.1) |
| [[A-172 (line)]] | wt | 143 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -17.3) |
| [[SNU-1 (line)]] | wt | 314 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.191× (z -19.0) |
| [[Hs 766T (line)]] | wt | 96.0 | 8 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.32× (z +11.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.9) | — |
| [[J82 (line)]] | alt | 214 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 160 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -22.5) |
| [[NCI-H460 (line)]] | wt | 74.4 | 7 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.22× (z +12.1) ⚠ unreliable plate only · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.97× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -17.0) |
| [[HS-578T (line)]] | alt | 87.7 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 84.8 | 6 (4 ⚠) | 0 | [[5-Azacytidine (drug)]] 5 µM 3.00× (z +10.6) | — |
| [[A-427 (line)]] | wt | 112 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -22.6) |
| [[COLO 205 (line)]] | alt | 268 | 2 (2 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.57× (z +9.9) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.0) |
| [[HOP62 (line)]] | alt | 91.2 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -20.4) |
| [[NCI-H2030 (line)]] | alt | 78.0 | 1 (1 ⚠) | 4 | [[Artesunate (drug)]] 5 µM 1.87× (z +8.6) ⚠ position correction uncertain | [[Panobinostat (drug)]] 5 µM 0.280× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 90.4 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.08× (z +9.9) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -13.9) |
| [[H4 (line)]] | wt | 127 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -18.7) |
| [[HepG2_C3A (line)]] | wt | 180 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 150 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 84.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -11.3) |
| [[A549 (line)]] | wt | 68.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 48.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 91.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.49× (z +10.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 3.67× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.9) |
| [[SHP-77 (line)]] | alt | 110 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.20× (z +8.6) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.461× (z -8.8) |
| [[SW 900 (line)]] | alt | 76.6 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.76× (z +9.7) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -14.0) |
| [[C-33 A (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.5) |
| [[CHP-212 (line)]] | wt | 96.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 72.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.6) |
| [[SNU-423 (line)]] | alt | 61.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARS1]] | +0.75 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[YARS1]] | +0.74 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[IARS1]] | +0.72 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[JDP2]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CEBPG]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ASNS]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | STRING 507 |
| [[PSAT1]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 | STRING 424 |
| [[SLC1A5]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 | pathway: Amino acid transport across the plasma membrane; STRING 747 |
| [[AARS1]] | +0.69 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[XPOT]] | +0.68 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[TARS1]] | +0.68 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SLC1A4]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 | pathway: Amino acid transport across the plasma membrane; STRING 752 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF654]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[FGFR1OP2]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ARRDC3]] | -0.47 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[OGA]] | -0.47 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CLEC2B]] | -0.45 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[ZNF224]] | -0.44 | -0.48 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC7A1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ASNSP1]] | B | ASNSP1 activity raises SLC7A1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.25× lower at baseline in the lines without ASNSP1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.0, 47.4); signed map (-13.6, 23.8). **Vector** length 149, 54.6% of its response variance represented; |z| ≥ 3 in 1,791 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.59 to 16); *mTORC1 signaling* (hallmark, mean cos +0.53 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.64 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +12.1 | +13.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +11.1 | +12.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +9.7 | +7.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +8.0 | +11.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.9 | +8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.5 | +6.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.2 | +8.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.1 | +6.1 |
| fall | [[Harringtonine (drug)]] 0.05 µM |  | -6.2 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -10.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -9.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.2 | -6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:29,509,414-29,595,688 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAT-1, HCAT1, REC1L; previously ERR, ATRC1 |
| Gene groups (HGNC) | Solute carrier family 7 |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, G2M_CHECKPOINT |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P30825](https://www.uniprot.org/uniprotkb/P30825) (High affinity cationic amino acid transporter 1):

> High-affinity, low capacity permease involved in the transport of the cationic amino acids (arginine, lysine and ornithine) in non-hepatic tissues.

**Summary**, from NCBI Gene [6541](https://www.ncbi.nlm.nih.gov/gene/6541):

> Enables L-arginine transmembrane transporter activity; L-histidine transmembrane transporter activity; and L-lysine transmembrane transporter activity. Involved in carboxylic acid transport. Located in apical plasma membrane and basolateral plasma membrane. Part of protein-containing complex. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11057) · Entrez [6541](https://www.ncbi.nlm.nih.gov/gene/6541) · UniProt [P30825](https://www.uniprot.org/uniprotkb/P30825) · Ensembl [ENSG00000139514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139514)

## Data

Gene col 6312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6312); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6312]; `tensor/DDL_lfc|DDL_z.npy` [6312]; `embed/gene_vectors.npy` [6312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6312 or target_col == 6312). Every well: [[SLC7A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
