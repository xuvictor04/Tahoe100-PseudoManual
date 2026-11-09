---
symbol: "CDC73"
type: "gene"
col: 5556
ensembl_id: "ENSG00000134371"
name: "cell division cycle 73"
location: "1q31.2"
module: 17
arm: "+"
pooled_cpm: 259.25
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CDC73

*cell division cycle 73* — 1q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +11.8, q 3e-29, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.467× (z -18.0, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD8]] (+0.64, fdr 1e-04), [[IFTAP]] (+0.62, fdr 1e-04), [[ZDHHC17]] (+0.61, fdr 7e-06); moves opposite to [[PITPNA]] (-0.64, fdr 1e-05), [[ARPC5L]] (-0.61, fdr 1e-05), [[TLNRD1]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +11.8 | 3e-29 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +9.4 | 2e-18 | 45/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +7.7 | 2e-12 | 35/48 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +7.3 | 3e-11 | 43/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.2 | 7e-11 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +6.5 | 9e-09 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 7e-08 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +4.7 | 2e-04 | 27/48 (PANC-1, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.7 | 2e-04 | 28/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 6e-04 | 29/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 32/48 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.036 | 29/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.3 | 0.036 | 25/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.036 | 25/48 (A498, HT-29, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.049 | 21/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.060 | 23/48 (NCI-H661, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.467×** | -18.0 | 0e+00 | 48/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -10.1 | 2e-21 | 45/48 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -9.6 | 1e-19 | 49/50 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.568×** | -9.5 | 3e-19 | 45/48 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -9.1 | 9e-18 | 47/47 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.575×** | -8.9 | 5e-17 | 36/44 (A-427, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.610×** | -8.3 | 1e-14 | 43/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.654×** | -7.1 | 8e-11 | 44/48 (A549, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.668×** | -6.8 | 9e-10 | 35/49 (NCI-H2347, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -6.6 | 2e-09 | 34/48 (SNU-1, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.754×** | -4.7 | 1e-04 | 37/48 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.779×** | -4.2 | 0.001 | 39/48 (NCI-H661, CHP-212, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.792×** | -3.9 | 0.004 | 29/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.796×** | -3.8 | 0.006 | 31/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.798×** | -3.8 | 0.006 | 27/48 (A549, SW 900, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.801×** | -3.7 | 0.007 | 27/48 (SW 900, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.823×** | -3.3 | 0.036 | 25/48 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.038 | 29/47 (CHP-212, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.829×** | -3.1 | 0.045 | 25/48 (NCI-H1573, RKO, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.829×** | -3.1 | 0.045 | 21/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.061 | 23/48 (SW48, C32, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.784×** | -2.9 | 0.087 | 21/48 (A498, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 223 | 8 (2 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.82× (z +21.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -16.4) |
| [[SW480 (line)]] | alt | 152 | 8 (2 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 357 | 6 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -20.3) |
| [[SW 900 (line)]] | alt | 473 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -16.3) |
| [[AsPC-1 (line)]] | alt | 321 | 3 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 289 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -20.3) |
| [[NCI-H2347 (line)]] | alt | 431 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -18.1) |
| [[LoVo (line)]] | wt | 177 | 5 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +16.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 324 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -17.3) |
| [[A498 (line)]] | wt | 231 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -18.8) |
| [[A549 (line)]] | wt | 226 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -22.1) |
| [[C32 (line)]] | wt | 842 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 382 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -13.4) |
| [[COLO 205 (line)]] | alt | 162 | 4 | 1 | [[TAK-901 (drug)]] 5 µM 7.28× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.8) |
| [[HOP62 (line)]] | alt | 269 | 2 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 287 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.73× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 193 | 3 | 2 | [[TAK-901 (drug)]] 5 µM 4.64× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -14.0) |
| [[H4 (line)]] | wt | 231 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.44× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.0) |
| [[HT-29 (line)]] | alt | 157 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -11.0) |
| [[LS 180 (line)]] | wt | 235 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 261 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.89× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.428× (z -10.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 181 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 308 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 248 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 177 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 220 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -15.2) |
| [[KATO III (line)]] | alt | 126 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 306 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 5.19× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 192 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -17.3) |
| [[RKO (line)]] | wt | 278 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.28× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -13.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -13.5) |
| [[SNU-1 (line)]] | wt | 396 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.381× (z -11.9) |
| [[SNU-423 (line)]] | alt | 163 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.8) |
| [[SW48 (line)]] | wt | 242 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.14× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -11.1) |
| [[A-172 (line)]] | wt | 249 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.8) |
| [[Hs 766T (line)]] | wt | 278 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.568× (z -9.2) |
| [[J82 (line)]] | alt | 218 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 306 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 214 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.7) |
| [[SW1417 (line)]] | alt | 171 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -11.1) |
| [[AN3 CA (line)]] | alt | 285 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -12.8) |
| [[C-33 A (line)]] | alt | 268 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 246 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -10.8) |
| [[HS-578T (line)]] | alt | 217 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -11.0) |
| [[NCI-H596 (line)]] | alt | 296 | 1 | 0 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 2.49× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 165 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -14.1) |
| [[BT-474 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 449 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD8]] | +0.64 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[IFTAP]] | +0.62 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[ZDHHC17]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ZNF292]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[VAPA]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[DLD]] | +0.60 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[MAP4K5]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DMXL1]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | same gene group |
| [[KPNA5]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[CNOT4]] | +0.58 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SPIN1]] | +0.58 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[MIER1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNA]] | -0.64 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CDR2]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[MROH1]] | -0.59 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[NFATC2IP]] | -0.58 | -0.31 / -0.57 | both halves | 2e-04 | same gene group |
| [[TMEM11-DT]] | -0.57 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[PDCD6]] | -0.56 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[NPIPB11]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PIGG]] | -0.55 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[TOP3A]] | -0.54 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[AXIN1]] | -0.54 | -0.18 / -0.64 | ⚠ one half (not replicated) | 1e-03 | pathway: Signaling by WNT |
| [[TPTEP2-CSNK1E]] | -0.53 | -0.31 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CDC73's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-16.5, 0.5); signed map (9.6, -26.2). **Vector** length 82.4, 34.3% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +7.9 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +7.7 | -6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +7.5 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | -0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +0.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -10.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -18.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -6.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 73 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.2 — chr1:193,121,983-193,254,815 (+) |
| Ensembl biotype | protein_coding |
| Also known as | parafibromin, FIHP; previously C1orf28, HRPT2, HRPT1 |
| Gene groups (HGNC) | Paf1/RNA polymerase II complex ; MicroRNA protein coding host genes |
| Reactome | 22 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; Formation of the beta-catenin:TCF transactivating complex; E3 ubiquitin ligases ubiquitinate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1J9](https://www.uniprot.org/uniprotkb/Q6P1J9) (Parafibromin):

> Tumor suppressor probably involved in transcriptional and post-transcriptional control pathways. May be involved in cell cycle progression through the regulation of cyclin D1/PRAD1 expression. Component of the PAF1 complex (PAF1C) which has multiple functions during transcription by RNA polymerase II and is implicated in regulation of development and maintenance of embryonic stem cell pluripotency. PAF1C associates with RNA polymerase II through interaction with POLR2A CTD non-phosphorylated …

**Summary**, from NCBI Gene [79577](https://www.ncbi.nlm.nih.gov/gene/79577):

> This gene encodes a tumor suppressor that is involved in transcriptional and post-transcriptional control pathways. The protein is a component of the the PAF protein complex, which associates with the RNA polymerase II subunit POLR2A and with a histone methyltransferase complex. This protein appears to facilitate the association of 3' mRNA processing factors with actively-transcribed chromatin. Mutations in this gene have been linked to hyperparathyroidism-jaw tumor syndrome, familial isolated …

**Accessions** — [HGNC:16783](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16783) · Entrez [79577](https://www.ncbi.nlm.nih.gov/gene/79577) · UniProt [Q6P1J9](https://www.uniprot.org/uniprotkb/Q6P1J9) · Ensembl [ENSG00000134371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134371)

## Data

Gene col 5556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5556); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5556]; `tensor/DDL_lfc|DDL_z.npy` [5556]; `embed/gene_vectors.npy` [5556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5556 or target_col == 5556). Every well: [[CDC73 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC73.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
