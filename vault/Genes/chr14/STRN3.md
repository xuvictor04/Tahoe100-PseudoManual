---
symbol: "STRN3"
type: "gene"
col: 12284
ensembl_id: "ENSG00000196792"
name: "striatin 3"
location: "14q12"
module: 46
arm: "+"
pooled_cpm: 273.84
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# STRN3

*striatin 3* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.93× (z +11.1, q 5e-26, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.338× (z -18.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMBRA1]] (+0.65, fdr 7e-06), [[PPP2R5E]] (+0.62, fdr 8e-06), [[WDFY3]] (+0.60, fdr 1e-05); moves opposite to [[IER2]] (-0.55, fdr 6e-05), [[N4BP3]] (-0.52, fdr 3e-05), [[EGR1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RASA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.93×** | +11.1 | 5e-26 | 47/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +9.4 | 2e-18 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.9 | 4e-13 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 2e-12 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +7.6 | 3e-12 | 44/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +7.5 | 5e-12 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.3 | 2e-08 | 41/48 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-08 | 38/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 7e-05 | 33/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.5 | 4e-04 | 30/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.007 | 26/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.029 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.338×** | -18.4 | 0e+00 | 48/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.347×** | -18.0 | 0e+00 | 48/48 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.355×** | -16.2 | 0e+00 | 45/45 (CFPAC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.404×** | -15.4 | 0e+00 | 48/49 (COLO 205, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -15.1 | 0e+00 | 42/44 (NCI-H1792, SW48, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.453×** | -13.4 | 4e-39 | 48/48 (HT-29, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.599×** | -8.7 | 3e-16 | 44/48 (SW 900, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -7.4 | 8e-12 | 45/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -7.0 | 2e-10 | 32/49 (A549, BT-474, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.692×** | -6.2 | 2e-08 | 44/48 (SW 900, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.750×** | -4.9 | 5e-05 | 38/48 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.788×** | -4.0 | 0.002 | 35/48 (HepG2/C3A, NCI-H661, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -3.3 | 0.037 | 17/48 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.872× | -3.3 | 0.038 | 4/48 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.838× | -3.0 | 0.096 | 21/49 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.826×** | -3.0 | 0.096 | 20/48 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.834× | -3.0 | 0.098 | 23/48 (NCI-H2347, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 251 | 7 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 365 | 6 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.276× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 240 | 6 (3 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.54× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 422 | 3 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -15.8) |
| [[SW480 (line)]] | alt | 240 | 5 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -14.5) |
| [[HT-29 (line)]] | alt | 164 | 5 | 5 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.18× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -16.1) |
| [[KATO III (line)]] | alt | 177 | 5 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -13.6) |
| [[SW 900 (line)]] | alt | 260 | 1 | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.274× (z -16.3) |
| [[HOP62 (line)]] | alt | 237 | 2 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 321 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.44× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.348× (z -13.2) |
| [[PANC-1 (line)]] | alt | 190 | 4 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 614 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.316× (z -14.0) |
| [[H4 (line)]] | wt | 223 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 285 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.303× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 354 | 1 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.255× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 513 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -17.2) |
| [[SW1417 (line)]] | alt | 281 | 2 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.293× (z -16.1) |
| [[A549 (line)]] | wt | 349 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -21.3) |
| [[AsPC-1 (line)]] | alt | 219 | 2 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.250× (z -16.0) |
| [[BT-474 (line)]] | alt | 490 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -20.0) |
| [[C-33 A (line)]] | alt | 322 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.344× (z -12.8) |
| [[C32 (line)]] | wt | 250 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.96× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -14.0) |
| [[LoVo (line)]] | wt | 222 | 5 (2 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.48× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.499× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 406 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 188 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -12.8) |
| [[SHP-77 (line)]] | alt | 280 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -15.9) |
| [[COLO 205 (line)]] | alt | 192 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.26× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -23.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 331 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.221× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 317 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -17.6) |
| [[SW48 (line)]] | wt | 397 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.80× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.376× (z -9.1) |
| [[A-427 (line)]] | wt | 240 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.94× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.435× (z -11.6) |
| [[HCT15 (line)]] | alt | 364 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 211 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.296× (z -13.9) |
| [[J82 (line)]] | alt | 158 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -13.2) |
| [[LS 180 (line)]] | wt | 287 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.354× (z -10.8) |
| [[RKO (line)]] | wt | 267 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.15× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.374× (z -11.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.444× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 239 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -14.3) |
| [[SNU-1 (line)]] | wt | 307 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.51× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -9.6) |
| [[SNU-423 (line)]] | alt | 223 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -11.5) |
| [[A-172 (line)]] | wt | 111 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -12.1) |
| [[CHP-212 (line)]] | wt | 258 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -10.0) |
| [[HS-578T (line)]] | alt | 152 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -14.6) |
| [[A498 (line)]] | wt | 151 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -12.5) |
| [[Hs 766T (line)]] | wt | 172 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -12.1) |
| [[SW 1271 (line)]] | alt | 308 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -8.9) |
| [[AN3 CA (line)]] | alt | 254 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 658 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMBRA1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 | same gene group |
| [[PPP2R5E]] | +0.62 | +0.76 / +0.58 | both halves | 8e-06 | same gene group; STRING 522 |
| [[WDFY3]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[PIP5K1A]] | +0.60 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[RAF1]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CLASP1]] | +0.59 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[TLK2]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[MAP2K4]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 | same gene group |
| [[ATAD2B]] | +0.57 | +0.29 / +0.56 | both halves | 3e-04 |  |
| [[MKLN1]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[C2orf42]] | +0.56 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[ZNF148]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | -0.55 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[N4BP3]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[EGR1]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[FOSL1]] | -0.50 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[PHLDA1]] | -0.49 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[BCL10]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SLC9A3R1]] | -0.49 | -0.50 / -0.40 | both halves | 5e-05 | same gene group |
| [[DUSP7]] | -0.48 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[TENT5C]] | -0.48 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[FOS]] | -0.48 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ETV3]] | -0.48 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.47 | -0.54 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[RSC1A1]] | -0.47 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASA3]] | B | RASA3 activity lowers STRN3's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.61× higher at baseline in the lines without RASA3 | 0.044 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers STRN3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.7, 15.0); signed map (-2.3, 1.8). **Vector** length 85.6, 36.9% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.6 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | -15.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | -0.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.8 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -18.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -18.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | striatin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:30,893,799-31,026,401 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SG2NA, PPP2R6B, S/G2NA |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 2 regulatory subunits; STRIPAK complex; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13033](https://www.uniprot.org/uniprotkb/Q13033) (Striatin-3):

> Calmodulin-binding scaffolding protein which is the center of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes such as cell growth, differentiation, apoptosis, metabolism and immune regulation (Probable).

**Summary**, from NCBI Gene [29966](https://www.ncbi.nlm.nih.gov/gene/29966):

> Enables armadillo repeat domain binding activity; enzyme binding activity; and protein-macromolecule adaptor activity. Involved in negative regulation of hippo signaling; negative regulation of transcription by RNA polymerase II; and positive regulation of transcription by RNA polymerase II. Located in Golgi apparatus; nucleoplasm; and plasma membrane. Part of FAR/SIN/STRIPAK complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15720) · Entrez [29966](https://www.ncbi.nlm.nih.gov/gene/29966) · UniProt [Q13033](https://www.uniprot.org/uniprotkb/Q13033) · Ensembl [ENSG00000196792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196792)

## Data

Gene col 12284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12284); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12284]; `tensor/DDL_lfc|DDL_z.npy` [12284]; `embed/gene_vectors.npy` [12284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12284 or target_col == 12284). Every well: [[STRN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
