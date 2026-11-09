---
symbol: "XPOT"
type: "gene"
col: 11553
ensembl_id: "ENSG00000184575"
name: "exportin for tRNA"
location: "12q14.2"
module: 63
arm: "+"
pooled_cpm: 154.82
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 32
n_dd_up_clean: 33
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# XPOT

*exportin for tRNA* — 12q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.83× (z +12.5, q 3e-33, up in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.76× (z +11.7, q 2e-29, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.352× (z -30.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AARS1]] (+0.91, fdr 7e-06), [[IARS1]] (+0.89, fdr 7e-06), [[GARS1]] (+0.86, fdr 7e-06); moves opposite to [[POLR2L]] (-0.60, fdr 1e-05), [[NFAT5]] (-0.55, fdr 2e-05), [[SMAD3]] (-0.55, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); 2 go from it, the strongest it → [[IARS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +12.5 | 3e-33 | 46/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +12.2 | 5e-32 | 45/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.76×** | +11.7 | 2e-29 | 46/48 (NCI-H460, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.5 | 1e-28 | 39/49 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +10.7 | 8e-25 | 38/48 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.42×** | +10.3 | 5e-23 | 43/48 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.40×** | +9.8 | 1e-20 | 37/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +9.0 | 1e-17 | 40/48 (A549, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.54×** | +8.9 | 4e-17 | 41/48 (LOX-IMVI, C-33 A, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +8.6 | 3e-16 | 42/48 (BT-474, C-33 A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +8.5 | 1e-15 | 34/49 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.47×** | +7.9 | 1e-13 | 39/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.9 | 2e-13 | 34/44 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +7.3 | 1e-11 | 37/48 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.96×** | +7.3 | 1e-11 | 44/48 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +6.7 | 8e-10 | 32/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.25×** | +6.5 | 2e-09 | 25/49 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.33×** | +5.9 | 9e-08 | 36/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +5.9 | 1e-07 | 39/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.352×** | -30.6 | 0e+00 | 47/48 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -16.8 | 0e+00 | 43/48 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -16.0 | 0e+00 | 43/49 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.493×** | -14.6 | 0e+00 | 42/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.501×** | -14.3 | 3e-44 | 45/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -12.5 | 5e-34 | 43/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -12.4 | 3e-33 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -12.4 | 3e-33 | 34/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.596×** | -10.7 | 5e-25 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.599×** | -10.6 | 2e-24 | 42/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.614×** | -10.1 | 3e-22 | 36/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -9.6 | 3e-20 | 36/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.725×** | -9.4 | 2e-19 | 37/48 (SW480, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.696×** | -7.5 | 2e-12 | 32/48 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -7.2 | 2e-11 | 35/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -6.6 | 1e-09 | 30/48 (H4, A498, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 232 | 2 | 17 (4 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 1.83× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -21.0) |
| [[SW480 (line)]] | alt | 158 | 7 (3 ⚠) | 12 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +12.2) ⚠ toxic · without an alert: [[Artesunate (drug)]] 5 µM 1.70× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -20.5) |
| [[HT-29 (line)]] | alt | 277 | 1 | 17 (3 ⚠) | [[Artesunate (drug)]] 5 µM 1.54× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -37.9) |
| [[A-172 (line)]] | wt | 172 | 1 | 14 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.94× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -24.4) |
| [[NCI-H460 (line)]] | wt | 181 | 6 (1 ⚠) | 9 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.07× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -29.6) |
| [[PANC-1 (line)]] | alt | 254 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -30.7) |
| [[A-427 (line)]] | wt | 348 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -34.8) |
| [[HS-578T (line)]] | alt | 162 | 1 (1 ⚠) | 13 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -21.9) |
| [[RKO (line)]] | wt | 176 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -20.0) |
| [[SNU-1 (line)]] | wt | 197 | 1 | 12 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.81× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -16.7) |
| [[KATO III (line)]] | alt | 183 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -17.7) |
| [[A498 (line)]] | wt | 220 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -28.5) |
| [[SW1417 (line)]] | alt | 145 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -24.8) |
| [[H4 (line)]] | wt | 220 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -32.7) |
| [[J82 (line)]] | alt | 173 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -31.6) |
| [[LOX-IMVI (line)]] | wt | 124 | 8 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.43× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.7) |
| [[BT-474 (line)]] | alt | 116 | 2 | 6 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.95× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -17.2) |
| [[SW48 (line)]] | wt | 190 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 138 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.0) |
| [[LS 180 (line)]] | wt | 172 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 180 | 1 | 5 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.92× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -20.9) |
| [[HEC-1-A (line)]] | alt | 125 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 1.97× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -12.6) |
| [[SW 900 (line)]] | alt | 94.8 | 1 (1 ⚠) | 4 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.67× (z +9.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 81.3 | 3 (2 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.09× (z +10.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.60× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -21.0) |
| [[C-33 A (line)]] | alt | 189 | 1 | 3 | [[5-Azacytidine (drug)]] 5 µM 2.20× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -13.4) |
| [[HOP62 (line)]] | alt | 84.4 | 2 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 3.60× (z +13.3) ⚠ toxic · without an alert: [[Artesunate (drug)]] 5 µM 1.79× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 116 | 4 (2 ⚠) | 0 | [[Neratinib (maleate) (drug)]] 5 µM 2.01× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 92.9 | 3 (1 ⚠) | 1 | [[Neratinib (maleate) (drug)]] 0.5 µM 2.47× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -14.0) |
| [[A549 (line)]] | wt | 85.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.69× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 97.0 | 3 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.10× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 257 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -19.9) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 61.1 | 2 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.23× (z +9.8) ⚠ toxic · without an alert: [[5-Azacytidine (drug)]] 5 µM 2.95× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 89.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.6) |
| [[C32 (line)]] | wt | 60.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 66.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.9) |
| [[COLO 205 (line)]] | alt | 78.5 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.11× (z +10.4) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 176 | 1 | 0 | [[Artesunate (drug)]] 5 µM 2.34× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 76.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.6) |
| [[SHP-77 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.9) |
| [[SNU-423 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.9) |
| [[AN3 CA (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AARS1]] | +0.91 | +0.89 / +0.92 | both halves | 7e-06 | STRING 401 |
| [[IARS1]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 654 |
| [[GARS1]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[MTHFD2]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[PSAT1]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[TCEA1]] | +0.85 | +0.83 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CEBPG]] | +0.85 | +0.83 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[NARS1]] | +0.84 | +0.77 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MARS1]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | STRING 655 |
| [[SARS1]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PHGDH]] | +0.83 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[ASNS]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2L]] | -0.60 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[NFAT5]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SMAD3]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises XPOT's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without ANK2 | 0.026 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[ASNSP1]] | B | ASNSP1 activity raises XPOT's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.35× lower at baseline in the lines without ASNSP1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ULBP1]] | B | ULBP1 activity raises XPOT's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without ULBP1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PSAT1]] | B | PSAT1 activity raises XPOT's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without PSAT1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[PSAT1]] | B | PSAT1 activity strengthens XPOT's drug response | lines that do not express PSAT1 (8) vs lines expressing it (41) | the lines without PSAT1 respond 0.89× as strongly (z diff +1.56); strongest at Homoharringtonine 0.5 µM: 0.82x vs 0.56x (z diff +3.8) | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IARS1]] | C | XPOT's natural level weakens IARS1's drug response | XPOT's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.28; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HSPA9]] | C | XPOT's natural level weakens HSPA9's drug response | XPOT's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.27; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.930). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 47.6); signed map (-13.7, 24.2). **Vector** length 160, 63.8% of its response variance represented; |z| ≥ 3 in 2,179 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.70 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.85 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.85 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +14.5 | +12.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +11.0 | +12.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +10.7 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.6 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.3 | +10.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +10.0 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +9.4 | +8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +9.0 | +8.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.4 | -12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -8.1 | -10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.9 | -14.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -7.4 | -6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.2 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.1 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -9.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.4 | -4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | exportin for tRNA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.2 — chr12:64,404,392-64,451,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XPO3 |
| Gene groups (HGNC) | Exportins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MYC_TARGETS_V1 |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O43592](https://www.uniprot.org/uniprotkb/O43592) (Exportin-T):

> Mediates the nuclear export of aminoacylated tRNAs. In the nucleus binds to tRNA and to the GTPase Ran in its active GTP-bound form. Docking of this trimeric complex to the nuclear pore complex (NPC) is mediated through binding to nucleoporins. Upon transit of a nuclear export complex into the cytoplasm, disassembling of the complex and hydrolysis of Ran-GTP to Ran-GDP (induced by RANBP1 and RANGAP1, respectively) cause release of the tRNA from the export receptor. XPOT then return to the …

**Summary**, from NCBI Gene [11260](https://www.ncbi.nlm.nih.gov/gene/11260):

> This gene encodes a protein belonging to the RAN-GTPase exportin family that mediates export of tRNA from the nucleus to the cytoplasm. Translocation of tRNA to the cytoplasm occurs once exportin has bound both tRNA and GTP-bound RAN. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12826) · Entrez [11260](https://www.ncbi.nlm.nih.gov/gene/11260) · UniProt [O43592](https://www.uniprot.org/uniprotkb/O43592) · Ensembl [ENSG00000184575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184575)

## Data

Gene col 11553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11553); `tables/drug_effects.parquet` (91 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11553]; `tensor/DDL_lfc|DDL_z.npy` [11553]; `embed/gene_vectors.npy` [11553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11553 or target_col == 11553). Every well: [[XPOT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPOT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
