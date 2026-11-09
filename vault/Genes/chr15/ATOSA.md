---
symbol: "ATOSA"
type: "gene"
col: 513
ensembl_id: "ENSG00000047346"
name: "atos homolog A"
location: "15q21.2-q21.3"
module: 69
arm: "+"
pooled_cpm: 105.6
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 30
n_dd_up_clean: 14
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# ATOSA

*atos homolog A* — 15q21.2-q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.79× (z +22.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.250× (z -21.5, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 0.251× (z -9.6, q 6e-20, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HBP1]] (+0.77, fdr 1e-05), [[CREBRF]] (+0.75, fdr 7e-06), [[TMEM59]] (+0.74, fdr 7e-06); moves opposite to [[TCOF1]] (-0.66, fdr 7e-06), [[EEFSEC]] (-0.65, fdr 1e-05), [[POLR3G]] (-0.65, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +22.6 | 0e+00 | 47/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.37×** | +13.5 | 8e-39 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +13.4 | 2e-38 | 40/49 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +10.1 | 5e-22 | 32/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.1 | 1e-17 | 35/48 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +8.8 | 2e-16 | 41/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +7.7 | 1e-12 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.8 | 6e-10 | 32/50 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 6e-08 | 32/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 9e-06 | 35/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.25×** | +5.0 | 3e-05 | 24/48 (J82, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.022 | 22/49 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.022 | 24/49 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.25×** | +3.5 | 0.022 | 22/48 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.022 | 24/50 (NCI-H1573, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.029 | 19/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.030 | 21/48 (A-172, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.043 | 20/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.250×** | -21.5 | 0e+00 | 48/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.422×** | -13.4 | 2e-38 | 45/49 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -13.3 | 8e-38 | 39/41 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.470×** | -10.8 | 3e-25 | 38/44 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.251×** | -9.6 | 6e-20 | 45/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.259×** | -9.4 | 5e-19 | 45/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.282×** | -8.8 | 1e-16 | 45/48 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.283×** | -8.8 | 1e-16 | 44/48 (NCI-H2347, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.384×** | -6.7 | 2e-09 | 43/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.773×** | -5.6 | 9e-07 | 29/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.695×** | -5.6 | 9e-07 | 30/48 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.736×** | -4.6 | 2e-04 | 28/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.777×** | -3.9 | 0.004 | 24/49 (SHP-77, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -3.7 | 0.009 | 23/48 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.781×** | -3.6 | 0.012 | 23/48 (SW 900, AsPC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.606×** | -3.5 | 0.016 | 21/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.645×** | -3.5 | 0.016 | 22/49 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.018 | 23/47 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.653×** | -3.4 | 0.021 | 18/48 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.805×** | -3.2 | 0.036 | 18/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.2 | 11 (3 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +26.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -22.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.147× (z -9.5) |
| [[SW480 (line)]] | alt | 95.7 | 5 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +17.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -16.0) ⚠ unreliable plate only · without an alert: [[Tucidinostat (drug)]] 5 µM 0.546× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 219 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0828× (z -11.4) |
| [[HT-29 (line)]] | alt | 169 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.218× (z -14.0) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 100 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +17.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.148× (z -18.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 76.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +20.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.356× (z -10.0) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 94.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -11.2) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 106 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +16.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -12.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0881× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.106× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 200 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.132× (z -19.6) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.115× (z -9.4) |
| [[PANC-1 (line)]] | alt | 86.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.37× (z +17.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -14.1) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 82.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +20.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -9.9) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 67.7 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -15.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +16.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.293× (z -8.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 94.2 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 88.1 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0517× (z -19.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 45.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +20.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -10.0) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 99.9 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -12.3) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +18.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -16.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 110 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -13.9) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 63.4 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0985× (z -18.8) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 75.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +18.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.258× (z -12.2) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 84.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -11.4) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 58.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +15.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.241× (z -12.1) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 95.0 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +13.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.297× (z -8.9) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 64.4 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +15.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -16.3) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 89.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 191 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.213× (z -13.8) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.349× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 40.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -8.9) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 157 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.0332× (z -29.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 175 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.132× (z -19.0) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 72.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -8.5) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 35.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 229 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -14.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -12.3) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 98.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -10.9) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.294× (z -10.4) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 133 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 95.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -14.9) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 151 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -10.5) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 158 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -10.4) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -15.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.124× (z -8.6) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0676× (z -16.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.2) | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 225 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -12.2) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 80.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0507× (z -10.9) |
| [[NCI-H2122 (line)]] | alt | 521 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBP1]] | +0.77 | +0.54 / +0.78 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.75 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.71 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[YPEL5]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[TXNDC16]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PIK3CA]] | +0.66 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[CERT1]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[WBP1]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[KDM6A]] | +0.65 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[SLU7]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCOF1]] | -0.66 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[EEFSEC]] | -0.65 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[POLR3G]] | -0.65 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[PGAM5]] | -0.64 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[PDCD11]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[ANKS6]] | -0.63 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[NAA15]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CHCHD6]] | -0.63 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[LYAR]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[TMEM177]] | -0.63 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[DKC1]] | -0.63 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[GNPNAT1]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.5, -43.6); signed map (-13.2, 9.9). **Vector** length 130, 50.2% of its response variance represented; |z| ≥ 3 in 1,545 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.8 | +1.1 |
|  | [[Ixazomib (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.9 | +0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.5 | -21.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.2 | -9.6 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -8.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.6 | -9.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.4 | -8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | atos homolog A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2-q21.3 — chr15:52,581,317-52,709,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10980; previously KIAA1370, FAM214A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32MH5](https://www.uniprot.org/uniprotkb/Q32MH5) (Atos homolog protein A):

> Transcription regulator that syncronizes transcriptional and translational programs to promote macrophage invasion of tissues.

**Summary**, from NCBI Gene [56204](https://www.ncbi.nlm.nih.gov/gene/56204):

> Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25609) · Entrez [56204](https://www.ncbi.nlm.nih.gov/gene/56204) · UniProt [Q32MH5](https://www.uniprot.org/uniprotkb/Q32MH5) · Ensembl [ENSG00000047346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047346)

## Data

Gene col 513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 513); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 513]; `tensor/DDL_lfc|DDL_z.npy` [513]; `embed/gene_vectors.npy` [513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 513 or target_col == 513). Every well: [[ATOSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATOSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
