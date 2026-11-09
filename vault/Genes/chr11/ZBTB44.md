---
symbol: "ZBTB44"
type: "gene"
col: 12178
ensembl_id: "ENSG00000196323"
name: "zinc finger and BTB domain containing 44"
location: "11q24.3"
module: 225
arm: "+"
pooled_cpm: 108.18
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# ZBTB44

*zinc finger and BTB domain containing 44* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.19× (z +6.2, q 2e-07, up in 24 of 49 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +6.1, q 2e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.556× (z -20.9, q 0e+00, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.545× (z -14.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAN3]] (+0.64, fdr 1e-05), [[PCMTD1]] (+0.63, fdr 2e-05), [[NDUFAF6]] (+0.62, fdr 2e-05); moves opposite to [[ALAS1]] (-0.51, fdr 4e-05), [[TRIM16]] (-0.48, fdr 5e-05), [[TUBB2A]] (-0.45, fdr 9e-05).
> It is in [[Module 225]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +6.2 | 2e-07 | 24/49 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.1 | 2e-07 | 29/48 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.15× | +5.0 | 9e-05 | 16/48 (COLO 205, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.46×** | +4.6 | 6e-04 | 24/50 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.9 | 0.011 | 6/48 (HEC-1-A, CFPAC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.011 | 16/49 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.022 | 9/49 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.042 | 15/47 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.09× | +3.2 | 0.071 | 7/48 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.071 | 15/48 (H4, hTERT-HPNE, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.071 | 12/50 (LS 180, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.18× | +3.1 | 0.082 | 12/50 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.09× | +3.1 | 0.088 | 1/49 (NCI-H2030) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.10 | 13/48 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.556×** | -20.9 | 0e+00 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.545×** | -14.7 | 0e+00 | 46/48 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.596×** | -13.0 | 1e-36 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -11.7 | 2e-29 | 40/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -10.4 | 2e-23 | 39/48 (HEC-1-A, LOX-IMVI, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -9.6 | 1e-19 | 45/48 (LoVo, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.471×** | -9.2 | 3e-18 | 44/48 (LoVo, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -9.1 | 5e-18 | 40/48 (LOX-IMVI, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.482×** | -8.9 | 3e-17 | 43/48 (KATO III, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.486×** | -8.8 | 7e-17 | 41/48 (HEC-1-A, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.730×** | -7.9 | 1e-13 | 27/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.722×** | -7.9 | 2e-13 | 37/47 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.537×** | -7.6 | 2e-12 | 38/48 (CHP-212, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.736×** | -7.3 | 1e-11 | 34/48 (LoVo, Hs 766T, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.552×** | -7.2 | 2e-11 | 35/48 (KATO III, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.696×** | -6.5 | 2e-09 | 38/48 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.708×** | -6.2 | 2e-08 | 34/49 (LoVo, HCT15, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.659×** | -5.1 | 1e-05 | 27/47 (RPMI-7951, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.757×** | -5.0 | 2e-05 | 28/48 (LoVo, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 94.0 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.519× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.436× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 121 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -19.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -15.8) |
| [[RKO (line)]] | wt | 105 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -9.8) |
| [[SW480 (line)]] | alt | 156 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -22.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -16.6) |
| [[LoVo (line)]] | wt | 97.1 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.480× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 165 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.242× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.394× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 77.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -19.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.285× (z -18.7) |
| [[PANC-1 (line)]] | alt | 222 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -19.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -19.4) |
| [[A-427 (line)]] | wt | 104 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.464× (z -9.0) |
| [[COLO 205 (line)]] | alt | 84.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.339× (z -9.3) |
| [[HOP62 (line)]] | alt | 67.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -9.0) |
| [[KATO III (line)]] | alt | 221 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 87.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.297× (z -13.7) |
| [[SW 900 (line)]] | alt | 81.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -9.0) |
| [[SW48 (line)]] | wt | 95.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -10.3) |
| [[AN3 CA (line)]] | alt | 130 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0573× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 71.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -8.6) |
| [[HT-29 (line)]] | alt | 151 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.421× (z -11.0) |
| [[J82 (line)]] | alt | 50.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -11.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.361× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -11.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.448× (z -9.8) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -18.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -12.1) |
| [[A-172 (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 109 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0487× (z -9.5) |
| [[H4 (line)]] | wt | 87.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.142× (z -8.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 93.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 72.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 64.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 79.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 160 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAN3]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PCMTD1]] | +0.63 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[NDUFAF6]] | +0.62 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[GPBP1L1]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DPY19L2P3]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SLC49A4]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[H3-3A-DT]] | +0.59 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[NEK7]] | +0.59 | +0.40 / +0.66 | both halves | 4e-05 |  |
| [[ZNRF2P2]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PCMTD2]] | +0.56 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[KLHL24]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 | same gene group |
| [[FBXL20]] | +0.55 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAS1]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TRIM16]] | -0.48 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[TUBB2A]] | -0.45 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[KRT16]] | -0.45 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[DPF1]] | -0.45 | -0.38 / -0.40 | both halves | 6e-05 | same gene group |
| [[DNAJB1]] | -0.45 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[PCYT1A]] | -0.44 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ULBP3]] | -0.44 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[CREB3]] | -0.44 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[ZNF365]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 | same gene group |
| [[BRF2]] | -0.43 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[OSGIN1]] | -0.43 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.1, -42.4); signed map (-14.1, 12.0). **Vector** length 112, 33.3% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.8 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.2 | -0.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.0 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.1 | -20.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.6 | -8.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.4 | -9.2 |
|  | [[EX229 (drug)]] 5 µM |  | -6.2 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -8.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:130,226,677-130,314,917 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC063, ZNF851; previously BTBD15 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCP5](https://www.uniprot.org/uniprotkb/Q8NCP5) (Zinc finger and BTB domain-containing protein 44):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [29068](https://www.ncbi.nlm.nih.gov/gene/29068):

> Predicted to enable DNA binding activity and zinc ion binding activity. Predicted to be involved in DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25001) · Entrez [29068](https://www.ncbi.nlm.nih.gov/gene/29068) · UniProt [Q8NCP5](https://www.uniprot.org/uniprotkb/Q8NCP5) · Ensembl [ENSG00000196323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196323)

## Data

Gene col 12178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12178); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12178]; `tensor/DDL_lfc|DDL_z.npy` [12178]; `embed/gene_vectors.npy` [12178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12178 or target_col == 12178). Every well: [[ZBTB44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
