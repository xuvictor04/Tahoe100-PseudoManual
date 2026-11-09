---
symbol: "UBE3A"
type: "gene"
col: 3521
ensembl_id: "ENSG00000114062"
name: "ubiquitin protein ligase E3A"
location: "15q11.2"
module: 51
arm: "+"
pooled_cpm: 221.6
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# UBE3A

*ubiquitin protein ligase E3A* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.32× (z +13.9, q 3e-41, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.572× (z -19.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THOC7]] (+0.68, fdr 1e-05), [[PRPF40A]] (+0.68, fdr 7e-06), [[SENP6]] (+0.67, fdr 9e-06); moves opposite to [[DNAAF3]] (-0.56, fdr 4e-05), [[P4HB]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +13.9 | 3e-41 | 32/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +13.1 | 2e-36 | 44/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +11.9 | 1e-30 | 39/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +11.0 | 7e-26 | 39/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +8.9 | 8e-17 | 38/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +8.3 | 1e-14 | 31/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +8.1 | 3e-14 | 26/48 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +7.9 | 2e-13 | 31/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +7.2 | 3e-11 | 29/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +6.2 | 3e-08 | 22/48 (LoVo, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.9 | 2e-07 | 24/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +5.2 | 8e-06 | 20/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.15× | +4.8 | 8e-05 | 8/48 (A-172, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +4.4 | 4e-04 | 14/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +4.3 | 6e-04 | 13/48 (HT-29, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.11× | +3.3 | 0.028 | 10/47 (LOX-IMVI, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.10× | +3.3 | 0.029 | 2/47 (LOX-IMVI, SW48) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | 1.18× | +3.1 | 0.062 | 14/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -19.6 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.584×** | -18.9 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.637×** | -15.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -10.4 | 5e-23 | 31/44 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.756×** | -9.5 | 3e-19 | 29/47 (LoVo, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.836× | -8.9 | 4e-17 | 24/49 (A549, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.782×** | -8.6 | 4e-16 | 30/49 (RKO, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.786×** | -7.4 | 7e-12 | 35/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.875× | -4.7 | 2e-04 | 10/48 (SW 900, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.832×** | -4.6 | 2e-04 | 24/48 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | 0.863× | -4.6 | 2e-04 | 20/45 (C-33 A, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -4.5 | 3e-04 | 0/50 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.889× | -4.0 | 0.003 | 18/50 (HOP62, BT-474, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.925× | -3.9 | 0.004 | 6/48 (A-172, HOP62, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | 0.890× | -3.7 | 0.009 | 7/47 (AN3 CA, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.932× | -3.5 | 0.014 | 5/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.020 | 16/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.893× | -3.4 | 0.021 | 8/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.05 µM |  | 0.912× | -2.9 | 0.099 | 6/47 (HS-578T, RKO, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.892× | -2.9 | 0.099 | 13/47 (NCI-H460, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 247 | 4 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.517× (z -11.5) |
| [[LoVo (line)]] | wt | 334 | 3 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.85× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.548× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 253 | 5 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.555× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.613× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 175 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.62× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.460× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 252 | 2 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.34× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.510× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.571× (z -11.1) |
| [[PANC-1 (line)]] | alt | 245 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +20.2) | [[Panobinostat (drug)]] 0.5 µM 0.578× (z -14.4) |
| [[SW48 (line)]] | wt | 265 | 3 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.86× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.500× (z -10.5) |
| [[SW480 (line)]] | alt | 221 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 3.00× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.462× (z -19.9) |
| [[A498 (line)]] | wt | 207 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.543× (z -12.8) |
| [[A549 (line)]] | wt | 162 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -14.6) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.467× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 258 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -12.5) |
| [[HOP62 (line)]] | alt | 287 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.485× (z -15.1) |
| [[LS 180 (line)]] | wt | 238 | 3 | 2 | [[TAK-901 (drug)]] 5 µM 2.87× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.615× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 199 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.394× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 217 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.441× (z -18.5) |
| [[H4 (line)]] | wt | 226 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 195 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.432× (z -11.2) |
| [[J82 (line)]] | alt | 205 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -16.7) |
| [[KATO III (line)]] | alt | 118 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 2.75× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.530× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 280 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -14.2) |
| [[NCI-H2030 (line)]] | alt | 245 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.507× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 208 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.12× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.427× (z -13.8) |
| [[RKO (line)]] | wt | 299 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.506× (z -13.0) |
| [[A-172 (line)]] | wt | 176 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.511× (z -13.6) |
| [[A-427 (line)]] | wt | 161 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -13.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[C-33 A (line)]] | alt | 266 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 224 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.576× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 240 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.471× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.384× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.531× (z -11.6) |
| [[SW1417 (line)]] | alt | 246 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.518× (z -12.5) |
| [[C32 (line)]] | wt | 176 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.51× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 223 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.98× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 143 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.556× (z -9.5) |
| [[HT-29 (line)]] | alt | 249 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.631× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 225 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.593× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 187 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 166 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.569× (z -9.5) |
| [[AN3 CA (line)]] | alt | 256 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 247 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HCT15 (line)]] | alt | 250 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.545× (z -9.8) |
| [[SHP-77 (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 275 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.573× (z -8.7) |
| [[SW 900 (line)]] | alt | 175 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 130 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 172 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC7]] | +0.68 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PRPF40A]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SENP6]] | +0.67 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[TACO1]] | +0.63 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[SNW1]] | +0.62 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[USP47]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[EIF3A]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MTIF2]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MTREX]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[USP7]] | +0.61 | +0.48 / +0.54 | both halves | 2e-05 | STRING 496 |
| [[GABPB2]] | +0.61 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[DDX28]] | +0.61 | +0.61 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.56 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[P4HB]] | -0.53 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UBE3A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-21.8, 9.0); signed map (11.3, -32.8). **Vector** length 89.9, 26.1% of its response variance represented; |z| ≥ 3 in 1,221 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +8.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.6 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.4 | -15.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -19.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -18.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | +6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | +8.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.0 | -0.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q11.2 — chr15:25,333,728-25,439,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AS, ANCR, E6-AP, FLJ26981; previously EPVE6AP, HPVE6A |
| Gene groups (HGNC) | HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05086](https://www.uniprot.org/uniprotkb/Q05086) (Ubiquitin-protein ligase E3A):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and transfers it to its substrates. Several substrates have been identified including the BMAL1, ARC, LAMTOR1, RAD23A and RAD23B, MCM7 (which is involved in DNA replication), annexin A1, the PML tumor suppressor, and the cell cycle regulator CDKN1B. Additionally, may function as a cellular quality control ubiquitin ligase by helping the degradation of the cytoplasmic misfolded …

**Summary**, from NCBI Gene [7337](https://www.ncbi.nlm.nih.gov/gene/7337):

> This gene encodes an E3 ubiquitin-protein ligase, part of the ubiquitin protein degradation system. This imprinted gene is maternally expressed in brain and biallelically expressed in other tissues. Maternally inherited deletion of this gene causes Angelman Syndrome, characterized by severe motor and intellectual retardation, ataxia, hypotonia, epilepsy, absence of speech, and characteristic facies. The protein also interacts with the E6 protein of human papillomavirus types 16 and 18, …

**Accessions** — [HGNC:12496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12496) · Entrez [7337](https://www.ncbi.nlm.nih.gov/gene/7337) · UniProt [Q05086](https://www.uniprot.org/uniprotkb/Q05086) · Ensembl [ENSG00000114062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114062)

## Data

Gene col 3521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3521); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3521]; `tensor/DDL_lfc|DDL_z.npy` [3521]; `embed/gene_vectors.npy` [3521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3521 or target_col == 3521). Every well: [[UBE3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
