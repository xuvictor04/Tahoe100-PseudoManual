---
symbol: "HACD3"
type: "gene"
col: 1089
ensembl_id: "ENSG00000074696"
name: "3-hydroxyacyl-CoA dehydratase 3"
location: "15q22.31"
module: 170
arm: "-"
pooled_cpm: 97.4
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# HACD3

*3-hydroxyacyl-CoA dehydratase 3* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.50× (z +19.8, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +8.8, q 1e-16, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.508× (z -15.2, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK9]] (+0.71, fdr 7e-06), [[TMTC4]] (+0.68, fdr 7e-06), [[GMPS]] (+0.66, fdr 1e-05); moves opposite to [[METTL25B]] (-0.72, fdr 1e-05), [[HELQ]] (-0.70, fdr 7e-06), [[TJAP1]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.50×** | +19.8 | 0e+00 | 48/49 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.73×** | +15.3 | 0e+00 | 41/44 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.30×** | +12.2 | 7e-32 | 41/45 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +8.8 | 1e-16 | 37/49 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +7.9 | 4e-13 | 45/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.63×** | +7.7 | 1e-12 | 40/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.60×** | +7.1 | 8e-11 | 39/47 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +7.0 | 1e-10 | 37/48 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +6.9 | 4e-10 | 40/48 (C32, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +6.3 | 1e-08 | 41/48 (SW480, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.47×** | +6.1 | 6e-08 | 36/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.42×** | +5.6 | 1e-06 | 30/48 (NCI-H1573, COLO 205, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.42×** | +5.3 | 5e-06 | 33/48 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.39×** | +5.2 | 6e-06 | 28/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.2 | 6e-06 | 36/48 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.032 | 12/48 (NCI-H460, A-427, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.038 | 16/48 (CHP-212, AsPC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.038 | 20/49 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.043 | 14/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.053 | 15/48 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.37×** | +2.8 | 0.076 | 15/48 (J82, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.20× | +2.7 | 0.098 | 18/48 (CFPAC-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.508×** | -15.2 | 0e+00 | 44/48 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -7.9 | 7e-13 | 34/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.751×** | -4.4 | 0.002 | 28/48 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.661×** | -3.4 | 0.083 | 20/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.820× | -3.0 | 0.24 | 17/48 (J82, HCT15, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.875× | -3.0 | 0.24 | 15/48 (LS 180, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 111 | 6 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.07× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -12.7) |
| [[A-172 (line)]] | wt | 95.5 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -19.2) |
| [[HT-29 (line)]] | alt | 63.8 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 73.8 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 66.4 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 76.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 128 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -23.6) |
| [[NCI-H1573 (line)]] | alt | 40.1 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.7× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 99.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -19.0) |
| [[PANC-1 (line)]] | alt | 114 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -16.9) |
| [[A549 (line)]] | wt | 124 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 61.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.2) |
| [[J82 (line)]] | alt | 115 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -24.8) |
| [[NCI-H2347 (line)]] | alt | 104 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.8) | — |
| [[RKO (line)]] | wt | 188 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -23.8) |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -21.1) |
| [[SNU-423 (line)]] | alt | 46.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.5) | — |
| [[A498 (line)]] | wt | 120 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 97.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.7) |
| [[Hs 766T (line)]] | wt | 70.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -14.6) |
| [[LS 180 (line)]] | wt | 94.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RPMI-7951 (line)]] | alt | 61.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.3) |
| [[AN3 CA (line)]] | alt | 177 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.7) |
| [[C-33 A (line)]] | alt | 219 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.6) |
| [[COLO 205 (line)]] | alt | 39.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.62× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 117 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -16.6) |
| [[HS-578T (line)]] | alt | 46.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 73.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 117 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 82.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 79.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.9) |
| [[SNU-1 (line)]] | wt | 130 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -29.1) |
| [[SW48 (line)]] | wt | 151 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -10.7) |
| [[A-427 (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -15.1) |
| [[C32 (line)]] | wt | 76.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -29.2) |
| [[SW1417 (line)]] | alt | 99.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | +0.71 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[GMPS]] | +0.66 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[ELAVL1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[NUTF2]] | +0.64 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[INPP4A]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[RAP1GDS1]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[AHSA1]] | +0.63 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[TMEM97]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PALS2]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[METAP1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL25B]] | -0.72 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[HELQ]] | -0.70 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[TJAP1]] | -0.69 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[CHMP4A]] | -0.68 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[OFD1]] | -0.67 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[MED18]] | -0.65 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[STK16]] | -0.64 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[ZNF674]] | -0.64 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.63 | -0.73 / -0.46 | both halves | 2e-05 |  |
| [[CYP20A1]] | -0.62 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[TMEM265]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises HACD3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without WNK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[FGD1]] | B | FGD1 activity raises HACD3's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without FGD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-23.8, -27.7); signed map (-20.9, -49.0). **Vector** length 110, 38.9% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.3 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +3.8 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.2 | -0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -13.3 | -15.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.7 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.4 | -7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxyacyl-CoA dehydratase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,530,418-65,578,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B-ind1, HSPC121; previously PTPLAD1 |
| Gene groups (HGNC) | 3-hydroxyacyl-CoA dehydratase family |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P035](https://www.uniprot.org/uniprotkb/Q9P035) (Very-long-chain):

> Catalyzes the third of the four reactions of the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process, allows the addition of two carbons to the chain of long- and very long-chain fatty acids/VLCFAs per cycle. This enzyme catalyzes the dehydration of the 3-hydroxyacyl-CoA intermediate into trans-2,3-enoyl-CoA, within each cycle of fatty acid elongation. Thereby, it participates in the production of VLCFAs of different chain lengths that are involved in …

**Summary**, from NCBI Gene [51495](https://www.ncbi.nlm.nih.gov/gene/51495):

> Enables enzyme binding activity and very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase activity. Involved in fatty acid biosynthetic process; positive regulation by virus of viral protein levels in host cell; and positive regulation of viral genome replication. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24175) · Entrez [51495](https://www.ncbi.nlm.nih.gov/gene/51495) · UniProt [Q9P035](https://www.uniprot.org/uniprotkb/Q9P035) · Ensembl [ENSG00000074696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074696)

## Data

Gene col 1089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1089); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1089]; `tensor/DDL_lfc|DDL_z.npy` [1089]; `embed/gene_vectors.npy` [1089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1089 or target_col == 1089). Every well: [[HACD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HACD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
