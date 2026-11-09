---
symbol: "CNNM2"
type: "gene"
col: 7322
ensembl_id: "ENSG00000148842"
name: "cyclin and CBS domain divalent metal cation transport mediator 2"
location: "10q24.32"
module: 225
arm: "+"
pooled_cpm: 112.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 42
n_dd_up_clean: 13
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# CNNM2

*cyclin and CBS domain divalent metal cation transport mediator 2* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.25× (z +12.6, q 2e-33, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.310× (z -17.0, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.625× (z -7.3, q 4e-11, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPM3]] (+0.74, fdr 7e-06), [[VEGFB]] (+0.72, fdr 7e-06), [[FBXL20]] (+0.72, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.70, fdr 7e-06), [[TTPAL]] (-0.66, fdr 7e-06), [[MAK16]] (-0.66, fdr 7e-06).
> It is in [[Module 225]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TNC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +12.6 | 2e-33 | 47/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +11.3 | 3e-27 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +9.4 | 1e-18 | 38/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +8.4 | 6e-15 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +7.9 | 2e-13 | 42/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +7.7 | 1e-12 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +7.1 | 1e-10 | 37/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +6.3 | 2e-08 | 40/49 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.2 | 3e-08 | 35/49 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +5.9 | 3e-07 | 27/48 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +4.4 | 5e-04 | 29/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.005 | 28/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.049 | 21/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +3.2 | 0.049 | 24/50 (SW480, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.18× | +3.2 | 0.059 | 13/48 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.067 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.310×** | -17.0 | 0e+00 | 45/49 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.342×** | -16.0 | 0e+00 | 43/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.389×** | -13.5 | 3e-39 | 42/45 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.496×** | -10.8 | 3e-25 | 46/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -7.3 | 4e-11 | 37/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.462×** | -6.2 | 4e-08 | 43/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.497×** | -5.7 | 1e-06 | 42/48 (A498, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.704×** | -5.4 | 4e-06 | 38/48 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.512×** | -5.4 | 4e-06 | 37/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.517×** | -5.3 | 6e-06 | 39/48 (HT-29, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.709×** | -5.3 | 6e-06 | 40/48 (HT-29, A498, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.538×** | -5.0 | 3e-05 | 33/47 (SW 900, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.725×** | -5.0 | 3e-05 | 35/49 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.733×** | -4.8 | 7e-05 | 34/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.752×** | -4.4 | 4e-04 | 36/48 (J82, NCI-H1573, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.760×** | -4.2 | 8e-04 | 30/48 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **0.806×** | -4.2 | 0.001 | 29/48 (NCI-H460, KATO III, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.783×** | -3.8 | 0.005 | 26/49 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.773×** | -3.7 | 0.005 | 28/48 (A-172, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 99.5 | 7 (2 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 3.99× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -15.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 154 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 181 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -16.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 76.8 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.401× (z -11.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 103 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.20× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -10.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 92.1 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +10.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 136 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -16.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 96.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -14.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 102 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.319× (z -10.9) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 144 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 156 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -14.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 80.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.36× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -15.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 66.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -15.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 108 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 90.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 134 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 231 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -16.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 114 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 102 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 284 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 94.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 135 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0996× (z -20.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 56.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +9.1) | — |
| [[H4 (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.26× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -12.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -14.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 83.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.0) | — |
| [[J82 (line)]] | alt | 76.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 99.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 201 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -18.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 82.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -8.5) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -11.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 76.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 60.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0752× (z -12.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 136 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM3]] | +0.74 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[VEGFB]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CUTA]] | +0.70 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[TNRC6B]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HINFP]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ELF2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MZT2B]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.67 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[COX14]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.70 | -0.66 / -0.70 | both halves | 7e-06 |  |
| [[TTPAL]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[MAK16]] | -0.66 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.64 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.63 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.63 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[CCT5]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ZNF121]] | -0.60 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.60 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CCT2]] | -0.60 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.60 | -0.61 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNC]] | B | TNC activity lowers CNNM2's level | lines that do not express TNC (23) vs lines expressing it (27) | 1.31× higher at baseline in the lines without TNC | 0.061 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.2, -42.2); signed map (-16.2, 11.8). **Vector** length 133, 50.6% of its response variance represented; |z| ≥ 3 in 1,455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.6 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.2 | +12.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.5 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +1.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.3 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.4 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -7.2 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -6.2 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.2 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.7 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin and CBS domain divalent metal cation transport mediator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,918,294-103,090,222 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC70A2; previously ACDP2 |
| Gene groups (HGNC) | Solute carrier family 70, cyclin and CBS domain divalent metal cation transport mediators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8M5](https://www.uniprot.org/uniprotkb/Q9H8M5) (Metal transporter CNNM2):

> Divalent metal cation transporter. Mediates transport of divalent metal cations in an order of Mg(2+) > Co(2+) > Mn(2+) > Sr(2+) > Ba(2+) > Cu(2+) > Fe(2+) (By similarity).

**Summary**, from NCBI Gene [54805](https://www.ncbi.nlm.nih.gov/gene/54805):

> This gene encodes a member of the ancient conserved domain containing protein family. Members of this protein family contain a cyclin box motif and have structural similarity to the cyclins. The encoded protein may play an important role in magnesium homeostasis by mediating the epithelial transport and renal reabsorption of Mg2+. Mutations in this gene are associated with renal hypomagnesemia. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this …

**Accessions** — [HGNC:103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:103) · Entrez [54805](https://www.ncbi.nlm.nih.gov/gene/54805) · UniProt [Q9H8M5](https://www.uniprot.org/uniprotkb/Q9H8M5) · Ensembl [ENSG00000148842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148842)

## Data

Gene col 7322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7322); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7322]; `tensor/DDL_lfc|DDL_z.npy` [7322]; `embed/gene_vectors.npy` [7322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7322 or target_col == 7322). Every well: [[CNNM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNNM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
