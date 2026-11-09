---
symbol: "PDCD4"
type: "gene"
col: 7445
ensembl_id: "ENSG00000150593"
name: "programmed cell death 4"
location: "10q25.2"
module: 69
arm: "+"
pooled_cpm: 95.92
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 38
n_dd_up_clean: 4
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PDCD4

*programmed cell death 4* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.44× (z +8.0, q 7e-13, up in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 0.5 µM: 1.21× (z +5.0, q 1e-04, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.244× (z -30.9, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.198× (z -18.5, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP44]] (+0.67, fdr 1e-05), [[TBC1D15]] (+0.66, fdr 7e-05), [[HBP1]] (+0.66, fdr 1e-05); moves opposite to [[HMGXB3]] (-0.53, fdr 2e-04), [[UBE2N]] (-0.53, fdr 1e-05), [[PAK1IP1]] (-0.51, fdr 3e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +8.0 | 7e-13 | 34/49 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.2 | 5e-05 | 26/44 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +5.0 | 1e-04 | 23/48 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.0 | 0.007 | 18/49 (MIA PaCa-2, Hs 766T, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.007 | 16/48 (LS 180, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.020 | 24/47 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.029 | 20/47 (LS 180, NCI-H1573, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.029 | 17/48 (Hs 766T, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.5 | 0.029 | 5/48 (NCI-H1573, SNU-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.052 | 18/49 (LoVo, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.14× | +3.3 | 0.052 | 16/50 (LS 180, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.094 | 11/48 (A-427, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.094 | 17/48 (SW1417, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.244×** | -30.9 | 0e+00 | 48/48 (SNU-423, HT-29, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.198×** | -18.5 | 0e+00 | 46/48 (RKO, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -18.1 | 0e+00 | 36/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -17.7 | 0e+00 | 42/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.227×** | -17.0 | 0e+00 | 46/48 (SNU-423, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.253×** | -15.7 | 0e+00 | 46/48 (SW1417, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.275×** | -14.8 | 0e+00 | 46/49 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.281×** | -14.5 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.289×** | -14.2 | 5e-44 | 46/48 (SW1417, C32, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.425×** | -13.4 | 7e-39 | 46/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -13.0 | 5e-37 | 38/48 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.550×** | -12.3 | 3e-33 | 44/48 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -11.8 | 2e-30 | 42/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.584×** | -11.7 | 4e-30 | 36/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -10.7 | 2e-25 | 44/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -8.9 | 2e-17 | 36/48 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.572×** | -8.7 | 1e-16 | 45/49 (SW480, SW 900, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 103 | 2 (2 ⚠) | 14 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.02× (z +10.5) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -21.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.437× (z -18.0) |
| [[A498 (line)]] | wt | 115 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -21.4) |
| [[RKO (line)]] | wt | 115 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -27.8) |
| [[LoVo (line)]] | wt | 91.0 | 3 | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.185× (z -21.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.250× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 90.3 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -22.4) |
| [[SW48 (line)]] | wt | 94.8 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.4) |
| [[PANC-1 (line)]] | alt | 125 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -28.2) |
| [[HOP62 (line)]] | alt | 69.8 | 0 | 10 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.176× (z -19.0) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.344× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 2 (2 ⚠) | 8 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -19.4) |
| [[SW1417 (line)]] | alt | 110 | 0 | 10 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.224× (z -18.7) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.107× (z -14.6) |
| [[C32 (line)]] | wt | 94.3 | 0 | 9 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.205× (z -17.4) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0950× (z -13.5) |
| [[HT-29 (line)]] | alt | 120 | 0 | 9 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.158× (z -21.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.128× (z -12.8) |
| [[SNU-423 (line)]] | alt | 142 | 0 | 9 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.148× (z -23.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0941× (z -15.4) |
| [[A-172 (line)]] | wt | 83.0 | 0 | 8 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -17.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.404× (z -14.1) |
| [[A-427 (line)]] | wt | 96.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -28.7) |
| [[HEC-1-A (line)]] | alt | 66.9 | 0 | 8 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.188× (z -17.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.336× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 97.7 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +12.8) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.231× (z -17.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.135× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 8 (2 ⚠) | — | [[TAK-733 (drug)]] 5 µM 0.123× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 121 | 0 | 7 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -15.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.237× (z -12.3) |
| [[Hs 766T (line)]] | wt | 76.7 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.174× (z -16.5) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.107× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 77.9 | 0 | 7 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.234× (z -14.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.8) |
| [[H4 (line)]] | wt | 139 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -13.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.115× (z -10.5) |
| [[HS-578T (line)]] | alt | 82.5 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -15.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.171× (z -16.9) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.285× (z -11.5) |
| [[LS 180 (line)]] | wt | 78.8 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.138× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 90.0 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.9) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -16.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.194× (z -10.3) |
| [[A549 (line)]] | wt | 71.1 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -16.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.423× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 86.2 | 0 | 5 (1 ⚠) | — | [[EX229 (drug)]] 5 µM 0.148× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.280× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.6) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -14.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.249× (z -9.7) |
| [[SW 900 (line)]] | alt | 89.5 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.225× (z -15.5) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.219× (z -15.2) |
| [[C-33 A (line)]] | alt | 69.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.5) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.271× (z -11.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -9.4) |
| [[COLO 205 (line)]] | alt | 129 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -13.6) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.335× (z -10.0) |
| [[HCT15 (line)]] | alt | 150 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -14.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0878× (z -13.2) |
| [[KATO III (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -17.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.158× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 52.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +14.2) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.367× (z -10.0) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 93.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +10.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.479× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 94.0 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -12.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.151× (z -9.5) |
| [[AN3 CA (line)]] | alt | 92.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -10.0) |
| [[SHP-77 (line)]] | alt | 73.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -12.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.4) |
| [[CHP-212 (line)]] | wt | 72.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.157× (z -10.2) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -12.2) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -14.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP44]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[TBC1D15]] | +0.66 | +0.38 / +0.77 | both halves | 7e-05 | **novel candidate** |
| [[HBP1]] | +0.66 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[KLHL24]] | +0.65 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.63 | +0.49 / +0.78 | both halves | 1e-05 |  |
| [[TCP11L2]] | +0.63 | +0.43 / +0.72 | both halves | 3e-05 |  |
| [[YPEL5]] | +0.63 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[JMY]] | +0.63 | +0.38 / +0.74 | both halves | 6e-05 |  |
| [[RB1CC1]] | +0.62 | +0.34 / +0.75 | both halves | 1e-04 |  |
| [[HECA]] | +0.59 | +0.37 / +0.69 | both halves | 9e-05 |  |
| [[SARAF]] | +0.59 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[FBXO25]] | +0.58 | +0.43 / +0.74 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGXB3]] | -0.53 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[UBE2N]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[EIF4E]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 | STRING 802 |
| [[NACC1]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZNF81]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PDSS1]] | -0.45 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[CIAPIN1]] | -0.45 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[SLC35B4]] | -0.45 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[MPHOSPH6]] | -0.45 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NME1]] | -0.44 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[RRS1]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.1, -44.9); signed map (-14.6, 10.0). **Vector** length 134, 45.7% of its response variance represented; |z| ≥ 3 in 1,790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 5 µM |  | +4.8 | +1.0 |
|  | [[NG25 (drug)]] 5 µM |  | +3.9 | +3.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.7 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +4.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +5.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -17.7 | -30.9 |
|  | [[EX229 (drug)]] 5 µM |  | -13.2 | -18.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -12.8 | -17.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -12.0 | -14.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -11.5 | -14.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.6 | -15.7 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,871,795-110,900,006 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H731 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | APOPTOSIS, ESTROGEN_RESPONSE_LATE, ADIPOGENESIS |
| Reactome | 5 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53EL6](https://www.uniprot.org/uniprotkb/Q53EL6) (Programmed cell death protein 4):

> Inhibits translation initiation and cap-dependent translation. May excert its function by hindering the interaction between EIF4A1 and EIF4G. Inhibits the helicase activity of EIF4A. Modulates the activation of JUN kinase. Down-regulates the expression of MAP4K1, thus inhibiting events important in driving invasion, namely, MAPK85 activation and consequent JUN-dependent transcription. May play a role in apoptosis. Tumor suppressor. Inhibits tumor promoter-induced neoplastic transformation. …

**Summary**, from NCBI Gene [27250](https://www.ncbi.nlm.nih.gov/gene/27250):

> This gene is a tumor suppressor and encodes a protein that binds to the eukaryotic translation initiation factor 4A1 and inhibits its function by preventing RNA binding. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:8763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8763) · Entrez [27250](https://www.ncbi.nlm.nih.gov/gene/27250) · UniProt [Q53EL6](https://www.uniprot.org/uniprotkb/Q53EL6) · Ensembl [ENSG00000150593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150593)

## Data

Gene col 7445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7445); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7445]; `tensor/DDL_lfc|DDL_z.npy` [7445]; `embed/gene_vectors.npy` [7445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7445 or target_col == 7445). Every well: [[PDCD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
