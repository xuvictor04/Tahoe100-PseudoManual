---
symbol: "FAF2"
type: "gene"
col: 3437
ensembl_id: "ENSG00000113194"
name: "Fas associated factor family member 2"
location: "5q35.2"
module: 156
arm: "+"
pooled_cpm: 140.68
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# FAF2

*Fas associated factor family member 2* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.39× (z +21.7, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.566× (z -14.8, q 0e+00, down in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.727× (z -12.7, q 2e-34, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP14]] (+0.73, fdr 7e-06), [[ALKBH1]] (+0.71, fdr 7e-06), [[UBE2J2]] (+0.69, fdr 7e-06); moves opposite to [[H3-3A]] (-0.62, fdr 7e-06), [[USP3]] (-0.61, fdr 9e-06), [[SEC61A2]] (-0.60, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.39×** | +21.7 | 0e+00 | 44/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.69×** | +14.5 | 4e-45 | 40/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +12.9 | 1e-35 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +9.8 | 1e-20 | 35/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +9.4 | 9e-19 | 40/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +8.1 | 4e-14 | 39/48 (COLO 205, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +5.5 | 4e-06 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 2e-05 | 31/48 (HEC-1-A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +5.1 | 2e-05 | 23/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.1 | 2e-05 | 24/48 (A-172, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.18× | +4.6 | 2e-04 | 17/47 (NCI-H1573, RPMI-7951, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +4.5 | 3e-04 | 18/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 6e-04 | 22/48 (A-172, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.16× | +4.0 | 0.002 | 21/48 (PANC-1, LOX-IMVI, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.13× | +3.5 | 0.018 | 19/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.566×** | -14.8 | 0e+00 | 35/45 (SW48, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -12.7 | 2e-34 | 35/49 (SNU-1, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -11.9 | 2e-30 | 40/47 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.683×** | -10.7 | 1e-24 | 35/49 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.733×** | -8.4 | 5e-15 | 28/44 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -7.9 | 4e-13 | 29/50 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -7.2 | 7e-11 | 30/48 (HEC-1-A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.821×** | -5.5 | 2e-06 | 25/48 (H4, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -5.2 | 1e-05 | 9/48 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.851× | -4.5 | 3e-04 | 22/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.872× | -3.8 | 0.006 | 17/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | 0.875× | -3.6 | 0.016 | 17/47 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.879× | -3.5 | 0.022 | 17/47 (NCI-H661, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.889× | -3.3 | 0.041 | 13/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.891× | -3.1 | 0.072 | 9/48 (CHP-212, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 156 | 5 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -15.1) |
| [[LoVo (line)]] | wt | 158 | 3 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.41× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 150 | 3 (1 ⚠) | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 8.33× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -20.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 203 | 3 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.515× (z -11.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 130 | 4 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -13.4) |
| [[H4 (line)]] | wt | 233 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.15× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 181 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -16.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 140 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.84× (z +12.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.9) |
| [[A-427 (line)]] | wt | 160 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.0) |
| [[COLO 205 (line)]] | alt | 167 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 168 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.7× (z +19.5) | — |
| [[A549 (line)]] | wt | 151 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.31× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.281× (z -14.3) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.449× (z -9.4) |
| [[HOP62 (line)]] | alt | 143 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.04× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.547× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 125 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.12× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -11.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 136 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 111 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.336× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 137 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.459× (z -11.0) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 133 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -15.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 111 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.370× (z -12.7) ⚠ toxic |
| [[BT-474 (line)]] | alt | 131 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 8.62× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -9.1) |
| [[C-33 A (line)]] | alt | 125 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.75× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -12.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 126 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 112 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.08× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -12.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.0) |
| [[SNU-1 (line)]] | wt | 104 | 2 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -18.4) |
| [[SW 900 (line)]] | alt | 259 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -12.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 128 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.55× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -11.8) |
| [[C32 (line)]] | wt | 92.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 123 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.68× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 91.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.45× (z +14.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.412× (z -10.9) ⚠ toxic |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 2 | — | [[Methylthiouracil (drug)]] 5 µM 0.366× (z -10.8) |
| [[SW480 (line)]] | alt | 140 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.07× (z +20.5) | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -10.2) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HCT15 (line)]] | alt | 136 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.67× (z +8.6) | — |
| [[J82 (line)]] | alt | 114 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.32× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 132 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.98× (z +11.1) | — |
| [[NCI-H661 (line)]] | alt | 90.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.167× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 117 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.38× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.1) |
| [[SNU-423 (line)]] | alt | 119 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.19× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.530× (z -8.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 223 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP14]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.71 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 | STRING 444 |
| [[TRIM4]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TAF2]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SDHAF2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NMT1]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[TSG101]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MAU2]] | +0.66 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TM9SF4]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3A]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[USP3]] | -0.61 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[SEC61A2]] | -0.60 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[SMG1P1]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[GLUD1]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[GPD1L]] | -0.55 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SNX30]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[WRNIP1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[METAP1]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[SLC25A30]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[DCUN1D4]] | -0.53 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FAF2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers FAF2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.3, 3.1); signed map (-4.7, -15.1). **Vector** length 132, 41.7% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.5 | +21.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +6.1 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.1 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +14.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +1.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.8 | -11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -7.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -3.1 | -2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | Fas associated factor family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,447,628-176,510,074 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ETEA, KIAA0887, UBXN3B; previously UBXD8 |
| Gene groups (HGNC) | UBX domain containing |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; Neutrophil degranulation; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CS3](https://www.uniprot.org/uniprotkb/Q96CS3) (FAS-associated factor 2):

> Plays an important role in endoplasmic reticulum-associated degradation (ERAD) that mediates ubiquitin-dependent degradation of misfolded endoplasmic reticulum proteins. By controlling the steady-state expression of the IGF1R receptor, indirectly regulates the insulin-like growth factor receptor signaling pathway. Recruits ATPase VCP to lipid droplets and also binds to phospholipase PNPLA2/ATGL, inhibiting PNPLA2 activity by promoting its dissociation from its ABHD5/CGI-58 activator. This …

**Summary**, from NCBI Gene [23197](https://www.ncbi.nlm.nih.gov/gene/23197):

> The protein encoded by this gene is highly expressed in peripheral blood of patients with atopic dermatitis (AD), compared to normal individuals. It may play a role in regulating the resistance to apoptosis that is observed in T cells and eosinophils of AD patients. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24666) · Entrez [23197](https://www.ncbi.nlm.nih.gov/gene/23197) · UniProt [Q96CS3](https://www.uniprot.org/uniprotkb/Q96CS3) · Ensembl [ENSG00000113194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113194)

## Data

Gene col 3437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3437); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3437]; `tensor/DDL_lfc|DDL_z.npy` [3437]; `embed/gene_vectors.npy` [3437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3437 or target_col == 3437). Every well: [[FAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
