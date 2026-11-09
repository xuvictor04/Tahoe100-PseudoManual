---
symbol: "XPO6"
type: "gene"
col: 9765
ensembl_id: "ENSG00000169180"
name: "exportin 6"
location: "16p12.1"
module: 33
arm: "+"
pooled_cpm: 141.58
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# XPO6

*exportin 6* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.66× (z +16.1, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.460× (z -13.9, q 7e-41, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.749× (z -5.2, q 3e-05, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (RKO 0.0455×, A-427 0.135×, SNU-1 0.211×, SK-MEL-2 0.212×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.0474×, C32 0.128×, NCI-H1573 0.233×, MIA PaCa-2 0.237×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.210×, HOP62 0.275×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (C32 0.312×, RKO 0.387×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.476×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDHD5]] (+0.59, fdr 1e-05), [[PARVB]] (+0.59, fdr 1e-05), [[USP31]] (+0.57, fdr 1e-05); moves opposite to [[DAZAP2]] (-0.48, fdr 6e-05), [[SMIM14]] (-0.46, fdr 3e-05), [[UBL3]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.66×** | +16.1 | 0e+00 | 49/49 (J82, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.57×** | +11.8 | 1e-29 | 45/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +10.8 | 6e-25 | 43/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.7 | 4e-16 | 38/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +8.5 | 3e-15 | 30/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +8.2 | 3e-14 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +8.2 | 3e-14 | 45/48 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +7.1 | 1e-10 | 41/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.0 | 2e-10 | 40/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +5.8 | 5e-07 | 33/48 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.7 | 6e-07 | 29/48 (PANC-1, HT-29, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.38×** | +5.7 | 7e-07 | 34/49 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +5.1 | 1e-05 | 29/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 2e-04 | 28/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 7e-04 | 33/48 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 26/48 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 28/48 (HT-29, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9765.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (RKO 0.0455×, A-427 0.135×, SNU-1 0.211×, SK-MEL-2 0.212×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.0474×, C32 0.128×, NCI-H1573 0.233×, MIA PaCa-2 0.237×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.210×, HOP62 0.275×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (C32 0.312×, RKO 0.387×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.476×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.460×** | -13.9 | 7e-41 | 43/49 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -12.9 | 8e-36 | 37/44 (Panc 03.27, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.640×** | -7.4 | 3e-11 | 32/45 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.749×** | -5.2 | 3e-05 | 30/48 (C32, RKO, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.022 | 26/48 (Panc 03.27, SW480, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.11 | 20/49 (RKO, PANC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.731× | -3.2 | 0.11 | 21/48 (HEC-1-A, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.829× | -3.1 | 0.12 | 20/48 (AsPC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.841× | -3.1 | 0.12 | 22/47 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.0 | 0.13 | 11/48 (NCI-H23, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 134 | 9 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 80.5 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +16.2) | — |
| [[C32 (line)]] | wt | 247 | 1 | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 5.13× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.312× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 96.5 | 7 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.08× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -16.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 93.6 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +16.8) | — |
| [[SW480 (line)]] | alt | 118 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.20× (z +12.4) | — |
| [[J82 (line)]] | alt | 265 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.14× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 223 | 3 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.15× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0455× (z -38.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -12.0) |
| [[A-427 (line)]] | wt | 121 | 4 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.87× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -28.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 166 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.57× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 126 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.07× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -13.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 80.1 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 282 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.66× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -16.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 99.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0474× (z -32.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 189 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.14× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -15.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 150 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.18× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -10.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 177 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.40× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -11.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 193 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -10.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 158 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -14.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 62.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +9.8) | — |
| [[LoVo (line)]] | wt | 107 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 156 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.99× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 96.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -12.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 129 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.84× (z +11.0) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 129 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.27× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 113 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.42× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 193 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.95× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 62.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +18.2) | — |
| [[NCI-H460 (line)]] | wt | 134 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.34× (z +9.2) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 4.78× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 198 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.87× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -16.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.60× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 143 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.4) | — |
| [[SW48 (line)]] | wt | 169 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.27× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -11.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 100 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.03× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 144 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.34× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 121 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.73× (z +10.1) | — |
| [[SW 1271 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD5]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PARVB]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[USP31]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PDSS1]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SLC15A4]] | +0.55 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[USP10]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DHODH]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[NME1]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[TFB1M]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[FMNL2]] | +0.53 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[NUDCD3]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TRIM65]] | +0.53 | +0.50 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAZAP2]] | -0.48 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[SMIM14]] | -0.46 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[UBL3]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ATF3]] | -0.46 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ATP9A]] | -0.45 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[C11orf54]] | -0.45 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[TMEM167B]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[MUC20]] | -0.44 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[YIPF6]] | -0.44 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[YPEL5]] | -0.44 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ATOSA]] | -0.44 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[RMND5A]] | -0.44 | -0.46 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises XPO6's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without FAM78B | 0.019 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[ADCY3]] | B | ADCY3 activity raises XPO6's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without ADCY3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[FSD1L]] | C | FSD1L activity raises XPO6's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without FSD1L | 0.026 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.3, -54.0); signed map (-3.5, -55.2). **Vector** length 103, 37.5% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.9 | +5.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.4 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +8.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.2 | +5.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +11.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | +8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | +10.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | +0.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | exportin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:28,097,976-28,211,965 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0370, FLJ22519; previously RANBP20 |
| Gene groups (HGNC) | Exportins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QU8](https://www.uniprot.org/uniprotkb/Q96QU8) (Exportin-6):

> Mediates the nuclear export of actin and profilin-actin complexes in somatic cells.

**Summary**, from NCBI Gene [23214](https://www.ncbi.nlm.nih.gov/gene/23214):

> The protein encoded by this gene is a member of the importin-beta family. Members of this family are regulated by the GTPase Ran to mediate transport of cargo across the nuclear envelope. This protein has been shown to mediate nuclear export of profilin-actin complexes. A pseudogene of this gene is located on the long arm of chromosome 14. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:19733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19733) · Entrez [23214](https://www.ncbi.nlm.nih.gov/gene/23214) · UniProt [Q96QU8](https://www.uniprot.org/uniprotkb/Q96QU8) · Ensembl [ENSG00000169180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169180)

## Data

Gene col 9765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9765); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9765]; `tensor/DDL_lfc|DDL_z.npy` [9765]; `embed/gene_vectors.npy` [9765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9765 or target_col == 9765). Every well: [[XPO6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPO6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
