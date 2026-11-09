---
symbol: "NR6A1"
type: "gene"
col: 7251
ensembl_id: "ENSG00000148200"
name: "nuclear receptor subfamily 6 group A member 1"
location: "9q33.3"
module: 216
arm: "+"
pooled_cpm: 193.97
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 15
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# NR6A1

*nuclear receptor subfamily 6 group A member 1* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.40× (z +18.7, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.432× (z -18.0, q 0e+00, down in 43 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Megestrol (drug)]] 5 µM: 0.700× (z -10.8, q 5e-25, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP32]] (+0.56, fdr 3e-05), [[VPS13A]] (+0.55, fdr 2e-05), [[ARHGEF3]] (+0.54, fdr 2e-05); moves opposite to [[TXNDC15]] (-0.55, fdr 4e-05), [[PGBD2]] (-0.55, fdr 5e-05), [[SNIP1]] (-0.54, fdr 3e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +18.7 | 0e+00 | 43/46 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +16.5 | 0e+00 | 43/46 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +15.1 | 0e+00 | 43/46 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +11.4 | 8e-28 | 28/46 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +11.1 | 2e-26 | 43/46 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +8.4 | 5e-15 | 34/46 (A-172, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +6.9 | 5e-10 | 40/46 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +6.8 | 8e-10 | 42/47 (HOP62, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 2e-09 | 34/47 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.8 | 5e-07 | 28/46 (HOP62, H4, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +5.5 | 2e-06 | 32/45 (AsPC-1, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +5.2 | 7e-06 | 28/45 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 8e-05 | 26/46 (HOP62, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.004 | 19/45 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.007 | 21/46 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.4 | 0.020 | 13/46 (AsPC-1, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.432×** | -18.0 | 0e+00 | 43/47 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -15.3 | 0e+00 | 36/42 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.489×** | -14.2 | 3e-43 | 39/43 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.602×** | -10.8 | 3e-25 | 45/47 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.700×** | -10.8 | 5e-25 | 42/47 (A498, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -8.0 | 8e-14 | 27/46 (KATO III, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.704×** | -7.5 | 4e-12 | 33/46 (HT-29, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -7.3 | 3e-11 | 34/45 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.512×** | -6.9 | 4e-10 | 32/47 (A498, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.726×** | -6.8 | 4e-10 | 33/46 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -6.6 | 2e-09 | 26/46 (RKO, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -6.5 | 3e-09 | 24/47 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.668×** | -4.1 | 0.002 | 21/35 (HEC-1-A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.1 | 0.002 | 22/46 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.716×** | -3.4 | 0.023 | 20/46 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.5 µM |  | 0.864× | -3.1 | 0.062 | 12/46 (NCI-H1792, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.861× | -3.0 | 0.095 | 12/45 (SW 1271, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.866× | -3.0 | 0.095 | 14/46 (SW480, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.862× | -2.9 | 0.096 | 15/45 (SW48, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.872× | -2.9 | 0.096 | 13/46 (NCI-H1573, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 269 | 3 | 10 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -15.6) |
| [[A-172 (line)]] | wt | 72.4 | 11 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +27.5) | [[Megestrol (drug)]] 5 µM 0.476× (z -9.1) |
| [[A498 (line)]] | wt | 166 | 6 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.5) | [[Megestrol (drug)]] 5 µM 0.468× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 261 | 4 | 8 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 144 | 2 (1 ⚠) | 8 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.93× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.97× (z +9.2) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.387× (z -12.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 121 | 7 (2 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 5.73× (z +19.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Megestrol (drug)]] 5 µM 0.572× (z -8.9) |
| [[SNU-423 (line)]] | alt | 227 | 5 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Megestrol (drug)]] 5 µM 0.527× (z -11.8) |
| [[SW1417 (line)]] | alt | 406 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -17.6) |
| [[HT-29 (line)]] | alt | 209 | 2 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.312× (z -15.7) |
| [[RKO (line)]] | wt | 342 | 3 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +11.2) | [[Harringtonine (drug)]] 0.5 µM 0.356× (z -13.5) |
| [[H4 (line)]] | wt | 154 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +23.1) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 115 | 7 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.21× (z +17.3) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.433× (z -10.1) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 168 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -14.9) |
| [[PANC-1 (line)]] | alt | 318 | 2 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +30.1) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -13.5) |
| [[SW480 (line)]] | alt | 313 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -14.6) |
| [[BT-474 (line)]] | alt | 53.4 | 7 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.26× (z +16.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 122 | 5 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 285 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0752× (z -32.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 136 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +19.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.391× (z -9.6) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 292 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.497× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 230 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Megestrol (drug)]] 5 µM 0.546× (z -10.6) |
| [[A-427 (line)]] | wt | 132 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -13.1) |
| [[HCT15 (line)]] | alt | 211 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -18.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 162 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Megestrol (drug)]] 5 µM 0.545× (z -10.0) |
| [[HS-578T (line)]] | alt | 98.6 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.62× (z +13.7) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.389× (z -10.1) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.567× (z -8.6) |
| [[LoVo (line)]] | wt | 273 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.632× (z -10.1) |
| [[LS 180 (line)]] | wt | 220 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.488× (z -9.2) |
| [[SW48 (line)]] | wt | 172 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.2) |
| [[C32 (line)]] | wt | 75.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.15× (z +16.8) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.9) | [[Megestrol (drug)]] 5 µM 0.521× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 127 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +12.4) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.383× (z -9.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 199 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +18.0) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -12.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 419 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -11.0) |
| [[J82 (line)]] | alt | 304 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 74.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 315 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -24.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 239 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -11.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 175 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -11.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 92.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +11.6) | — |
| [[CHP-212 (line)]] | wt | 167 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.39× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 346 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.3) |
| [[SNU-1 (line)]] | wt | 193 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -11.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 198 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 2.18× (z +8.8) | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0782× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 255 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 43.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP32]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[VPS13A]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ARHGEF3]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[C20orf27]] | +0.54 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[DLG1]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[STK3]] | +0.54 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[TBL1X]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[RABGAP1L]] | +0.53 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[MRPL14]] | +0.52 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[RALGPS1]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[GSK3B]] | +0.51 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | +0.51 | +0.38 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC15]] | -0.55 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[PGBD2]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[SNIP1]] | -0.54 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[KANSL2]] | -0.51 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[DPY19L3-DT]] | -0.51 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[ZNF561]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ZNF275]] | -0.51 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SPRY3]] | -0.50 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[DBR1]] | -0.50 | -0.61 / -0.26 | both halves | 4e-04 |  |
| [[ISY1]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[COQ6]] | -0.49 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[PPIE]] | -0.49 | -0.59 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 16.3); signed map (-16.7, 31.7). **Vector** length 122, 40.2% of its response variance represented; |z| ≥ 3 in 1,585 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.8 | +4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.7 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +7.5 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +8.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -14.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | +0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 6 group A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,517,275-124,771,311 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCNF1, RTR, CT150; previously GCNF |
| Gene groups (HGNC) | Nuclear receptor subfamily 6 group A |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG activate genes related to proliferation; Transcriptional regulation of pluripotent stem cells; Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15406](https://www.uniprot.org/uniprotkb/Q15406) (Nuclear receptor subfamily 6 group A member 1):

> Orphan nuclear receptor that binds to a response element containing the sequence 5'-TCAAGGTCA-3'. Acts as a regulator of embryonic stem cell pluripotency by mediating repression of POU5F1/OCT4: binds to the DR0 element within the POU5F1/OCT4 promoter and inhibits POU5F1/OCT4 expression during embryonic stem cell differentiation. Involved in the regulation of gene expression in germ cell development during gametogenesis (By similarity).

**Summary**, from NCBI Gene [2649](https://www.ncbi.nlm.nih.gov/gene/2649):

> This gene encodes an orphan nuclear receptor which is a member of the nuclear hormone receptor family. Its expression pattern suggests that it may be involved in neurogenesis and germ cell development. The protein can homodimerize and bind DNA, but in vivo targets have not been identified. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:7985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7985) · Entrez [2649](https://www.ncbi.nlm.nih.gov/gene/2649) · UniProt [Q15406](https://www.uniprot.org/uniprotkb/Q15406) · Ensembl [ENSG00000148200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148200)

## Data

Gene col 7251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7251); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7251]; `tensor/DDL_lfc|DDL_z.npy` [7251]; `embed/gene_vectors.npy` [7251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7251 or target_col == 7251). Every well: [[NR6A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR6A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
