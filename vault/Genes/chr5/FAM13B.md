---
symbol: "FAM13B"
type: "gene"
col: 399
ensembl_id: "ENSG00000031003"
name: "family with sequence similarity 13 member B"
location: "5q31.2"
module: 85
arm: "+"
pooled_cpm: 194.7
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# FAM13B

*family with sequence similarity 13 member B* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.82× (z +7.4, q 1e-10, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.378× (z -22.0, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.588× (z -17.7, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.79, fdr 1e-05), [[SUFU]] (+0.76, fdr 1e-05), [[CARHSP1]] (+0.69, fdr 8e-05); moves opposite to [[DPH5-DT]] (-0.65, fdr 4e-05), [[ZNF564]] (-0.65, fdr 5e-05), [[CPSF2]] (-0.63, fdr 8e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +7.4 | 1e-10 | 39/49 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.7 | 6e-04 | 24/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +4.7 | 6e-04 | 32/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.6 | 6e-04 | 24/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.8 | 0.015 | 17/48 (SW480, RKO, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.058 | 15/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.058 | 22/49 (MIA PaCa-2, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.058 | 18/48 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.065 | 26/48 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.071 | 21/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.14 | 9/48 (PANC-1, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.378×** | -22.0 | 0e+00 | 43/44 (HCT15, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.435×** | -19.6 | 0e+00 | 47/49 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -17.7 | 0e+00 | 45/49 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.454×** | -17.2 | 0e+00 | 44/45 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -9.0 | 2e-17 | 39/50 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.682×** | -9.0 | 2e-17 | 44/48 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -8.7 | 2e-16 | 41/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -8.7 | 2e-16 | 43/48 (A-172, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.700×** | -8.4 | 3e-15 | 38/48 (A-172, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -7.5 | 4e-12 | 38/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -6.2 | 4e-08 | 24/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -5.3 | 7e-06 | 34/48 (A498, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.814×** | -4.8 | 6e-05 | 27/48 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.870× | -4.6 | 2e-04 | 11/48 (SK-MEL-2, AsPC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.834× | -4.1 | 0.002 | 23/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.042 | 18/47 (SW480, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.876× | -3.1 | 0.060 | 15/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.869× | -3.0 | 0.066 | 14/47 (A-172, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.803×** | -2.9 | 0.098 | 22/47 (SNU-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 203 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -18.3) |
| [[HOP62 (line)]] | alt | 224 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 208 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -15.3) |
| [[PANC-1 (line)]] | alt | 180 | 2 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 270 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.59× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -11.2) |
| [[SNU-423 (line)]] | alt | 206 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 306 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 251 | 2 (2 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.95× (z +9.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.187× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.4) |
| [[SW1417 (line)]] | alt | 255 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -14.6) |
| [[SW480 (line)]] | alt | 176 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.06× (z +12.0) | [[Docetaxel (drug)]] 0.05 µM 0.585× (z -11.0) ⚠ transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.636× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 240 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.1) |
| [[H4 (line)]] | wt | 234 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 176 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 290 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.9) |
| [[A-427 (line)]] | wt | 215 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -32.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.1) |
| [[A549 (line)]] | wt | 208 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -24.6) |
| [[AsPC-1 (line)]] | alt | 214 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -15.0) |
| [[LoVo (line)]] | wt | 186 | 2 (2 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.88× (z +11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -18.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 184 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -33.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 206 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.93× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -9.3) |
| [[Hs 766T (line)]] | wt | 185 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 213 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.9) |
| [[J82 (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -9.1) |
| [[LS 180 (line)]] | wt | 143 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 174 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 191 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -10.2) |
| [[RKO (line)]] | wt | 167 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.454× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 170 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.437× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.3) |
| [[SHP-77 (line)]] | alt | 179 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -9.8) |
| [[SNU-1 (line)]] | wt | 225 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.1) |
| [[A498 (line)]] | wt | 151 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -17.8) |
| [[AN3 CA (line)]] | alt | 268 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.9) |
| [[BT-474 (line)]] | alt | 175 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 172 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -13.1) |
| [[SW48 (line)]] | wt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 208 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.234× (z -11.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0335× (z -42.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.450× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.525× (z -8.7) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 277 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 151 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.7) |
| [[COLO 205 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 258 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.79 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[SUFU]] | +0.76 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.69 | +0.67 / +0.37 | both halves | 8e-05 |  |
| [[PAFAH1B3]] | +0.66 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[CFD]] | +0.65 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[HACE1]] | +0.65 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[GNAI2]] | +0.65 | +0.63 / +0.26 | both halves | 3e-04 |  |
| [[CRTC1]] | +0.64 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.64 | +0.58 / +0.25 | both halves | 4e-04 |  |
| [[IGSF8]] | +0.64 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[CBFA2T2]] | +0.64 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.63 | +0.51 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH5-DT]] | -0.65 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[ZNF564]] | -0.65 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[CPSF2]] | -0.63 | -0.67 / -0.37 | both halves | 8e-05 |  |
| [[KICS2]] | -0.63 | -0.65 / -0.37 | both halves | 8e-05 |  |
| [[RNF6]] | -0.63 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[CSTF3]] | -0.63 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[MTHFSD]] | -0.61 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[PSME3IP1]] | -0.60 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[ARRDC3-AS1]] | -0.59 | -0.61 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[MCPH1]] | -0.59 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[CFLAR]] | -0.59 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MCTS1]] | -0.59 | -0.59 / -0.23 | both halves | 5e-04 |  |
| [[CHD1-DT]] | -0.59 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FAM13B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLTCL1]] | C | CLTCL1 activity raises FAM13B's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.62× lower at baseline in the lines without CLTCL1 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[CLTCL1]] | C | CLTCL1 activity strengthens FAM13B's drug response | lines that do not express CLTCL1 (3) vs lines expressing it (47) | the lines without CLTCL1 respond 0.68× as strongly (z diff +2.34); strongest at Dinaciclib 0.5 µM: 0.74x vs 0.44x (z diff +4.7) | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.5, -6.8); signed map (-32.9, -0.5). **Vector** length 113, 40.3% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.8 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.6 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.4 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -17.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 13 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:137,937,960-138,051,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | N61, KHCHP, ARHGAP49; previously C5orf5, FAM13B1 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 5 pathways, smallest: CDC42 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

UniProt [Q9NYF5](https://www.uniprot.org/uniprotkb/Q9NYF5) carries no function annotation.

**Summary**, from NCBI Gene [51306](https://www.ncbi.nlm.nih.gov/gene/51306):

> Predicted to enable GTPase activator activity. Predicted to be involved in regulation of small GTPase mediated signal transduction. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1335) · Entrez [51306](https://www.ncbi.nlm.nih.gov/gene/51306) · UniProt [Q9NYF5](https://www.uniprot.org/uniprotkb/Q9NYF5) · Ensembl [ENSG00000031003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000031003)

## Data

Gene col 399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 399); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 399]; `tensor/DDL_lfc|DDL_z.npy` [399]; `embed/gene_vectors.npy` [399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 399 or target_col == 399). Every well: [[FAM13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
