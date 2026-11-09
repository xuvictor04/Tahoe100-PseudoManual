---
symbol: "ATAD2"
type: "gene"
col: 8014
ensembl_id: "ENSG00000156802"
name: "ATPase family AAA domain containing 2"
location: "8q24.13"
module: 6
arm: "+"
pooled_cpm: 142.59
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ATAD2

*ATPase family AAA domain containing 2* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (28 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.62× (z +18.3, q 0e+00, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Cytarabine (hydrochloride) (drug)]] 0.05 µM: 1.30× (z +4.6, q 9e-05, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.701× (z -9.6, q 7e-19, down in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~68% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.788× (z -6.4, q 2e-08, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.91, fdr 7e-06), [[WDHD1]] (+0.88, fdr 7e-06), [[BRIP1]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 30 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 28 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.62×** | +18.3 | 0e+00 | 43/47 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.48×** | +17.3 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.01×** | +13.3 | 8e-38 | 40/47 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **2.00×** | +13.1 | 4e-37 | 40/47 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.95×** | +12.7 | 1e-34 | 40/47 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.95×** | +12.6 | 2e-34 | 42/47 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.51×** | +11.1 | 8e-27 | 27/47 (NCI-H1792, LOX-IMVI, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.78×** | +10.9 | 6e-26 | 40/47 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.51×** | +7.8 | 5e-13 | 33/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.46×** | +6.9 | 2e-10 | 28/43 (HS-578T, C32, …) | all doses, stronger at high dose | composition shift |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.29×** | +6.7 | 9e-10 | 29/47 (HT-29, SW480, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.26×** | +6.1 | 5e-08 | 24/48 (HT-29, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.37×** | +6.0 | 1e-07 | 28/47 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.34×** | +5.5 | 1e-06 | 27/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +5.5 | 1e-06 | 26/47 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +4.6 | 9e-05 | 21/47 (HT-29, SW480, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.003 | 23/47 (LS 180, LoVo, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.003 | 21/47 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.003 | 20/47 (SW480, HOP62, …) | top dose only | plate-row cell shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.014 | 16/46 (SW480, J82, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.043 | 17/47 (NCI-H1792, Hs 766T, …) | two highest doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.046 | 11/47 (HT-29, SW480, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.053 | 14/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.071 | 11/47 (SW480, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.18× | +2.8 | 0.072 | 11/47 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Methotrexate (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.072 | 7/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Irinotecan (drug)]] 5 µM |  | **1.35×** | +2.7 | 0.084 | 10/49 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.701×** | -9.6 | 7e-19 | 32/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.621×** | -8.0 | 4e-13 | 34/47 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.788×** | -6.4 | 2e-08 | 30/47 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.716×** | -6.4 | 3e-08 | 31/48 (COLO 205, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -6.3 | 5e-08 | 30/47 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.732×** | -5.3 | 1e-05 | 32/47 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.836× | -4.8 | 1e-04 | 21/47 (COLO 205, RKO, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.607×** | -4.5 | 4e-04 | 26/46 (SW480, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.729×** | -4.3 | 0.001 | 24/47 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.854× | -4.3 | 0.001 | 15/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.808×** | -3.9 | 0.005 | 24/46 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.785×** | -3.9 | 0.005 | 20/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.795×** | -3.7 | 0.010 | 24/47 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.671×** | -3.6 | 0.011 | 18/46 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.026 | 19/46 (SW1417, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.821×** | -3.3 | 0.031 | 15/47 (SW 1271, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.037 | 18/47 (HepG2/C3A, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.888× | -3.2 | 0.037 | 15/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.789×** | -3.2 | 0.037 | 15/47 (NCI-H460, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.888× | -3.2 | 0.038 | 11/48 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.891× | -3.1 | 0.051 | 10/48 (AN3 CA, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.053 | 15/46 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.853× | -3.0 | 0.053 | 14/47 (A-172, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.853× | -3.0 | 0.053 | 19/47 (A-427, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.02 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 110 | 9 (9 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +15.5) ⚠ cell-cycle shift, explains ~57% of this change | [[Selinexor (drug)]] 5 µM 0.443× (z -10.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[LS 180 (line)]] | wt | 95.1 | 4 (4 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +12.7) ⚠ cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.337× (z -13.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.474× (z -9.0) |
| [[PANC-1 (line)]] | alt | 112 | 8 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +16.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LoVo (line)]] | wt | 69.3 | 6 (6 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +12.6) ⚠ cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.485× (z -10.2) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H460 (line)]] | wt | 66.2 | 5 (5 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +10.0) ⚠ cell-cycle shift, explains ~87% of this change | [[Selinexor (drug)]] 5 µM 0.359× (z -12.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 72.6 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +14.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 86.1 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +14.4) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[HT-29 (line)]] | alt | 345 | 5 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.7) ⚠ cell-cycle shift, explains ~44% of this change | [[Selinexor (drug)]] 5 µM 0.454× (z -10.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-427 (line)]] | wt | 200 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.252× (z -19.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.346× (z -10.6) |
| [[A498 (line)]] | wt | 159 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -17.0) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.497× (z -9.5) |
| [[J82 (line)]] | alt | 355 | 4 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +14.2) ⚠ cell-cycle shift, explains ~44% of this change | [[Belumosudil (drug)]] 5 µM 0.559× (z -8.5) |
| [[RKO (line)]] | wt | 356 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.5) ⚠ cell-cycle shift, explains ~57% of this change | [[Selinexor (drug)]] 0.5 µM 0.398× (z -8.7) ⚠ cell-cycle shift, explains ~74% of this change |
| [[AsPC-1 (line)]] | alt | 86.8 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +11.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[H4 (line)]] | wt | 63.2 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.86× (z +10.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW480 (line)]] | alt | 187 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +14.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[BT-474 (line)]] | alt | 214 | 3 | 0 | [[Budesonide (drug)]] 0.5 µM 3.26× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 217 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C32 (line)]] | wt | 75.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +14.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[Panc 03.27 (line)]] | alt | 165 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Lonafarnib (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 140 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Selinexor (drug)]] 5 µM 0.445× (z -8.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HCT15 (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 346 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -9.9) |
| [[KATO III (line)]] | alt | 163 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +10.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1792 (line)]] | alt | 44.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +18.7) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H23 (line)]] | alt | 187 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.7) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SHP-77 (line)]] | alt | 247 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SNU-423 (line)]] | alt | 74.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[SW1417 (line)]] | alt | 206 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[A-172 (line)]] | wt | 90.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.265× (z -14.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[CFPAC-1 (line)]] | alt | 62.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.8) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.289× (z -10.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[NCI-H1573 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.5) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW48 (line)]] | wt | 142 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.342× (z -12.5) |
| [[AN3 CA (line)]] | alt | 160 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 98.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 96.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | STRING 510 |
| [[WDHD1]] | +0.88 | +0.82 / +0.91 | both halves | 7e-06 | STRING 445 |
| [[BRIP1]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[NCAPG2]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | STRING 502 |
| [[POLQ]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[DTL]] | +0.87 | +0.87 / +0.89 | both halves | 7e-06 | same gene group; STRING 509 |
| [[CENPK]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 |  |
| [[SPC24]] | +0.87 | +0.85 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDC45]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | STRING 579 |
| [[FANCI]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | STRING 512 |
| [[BLM]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | STRING 444 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises ATAD2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without CDC25A | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises ATAD2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without CDCA7 | 0.024 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises ATAD2's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib) | 50% of the class's compounds vs 3.9% of all compounds | 0.060 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers ATAD2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises ATAD2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without FAM111B | 0.085 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises ATAD2's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.72× lower at baseline in the lines without ZNF367 | 0.017 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.897). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.1, -46.3); signed map (-39.5, -44.5). **Vector** length 163, 64.2% of its response variance represented; |z| ≥ 3 in 1,947 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.71 to 40); *E2F G1/S* (control, mean cos +0.71 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +6.8 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +6.2 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.9 | +18.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +5.6 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.4 | +12.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +5.1 | +4.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +4.6 | +3.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +4.6 | +3.8 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +3.9 | +2.1 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +3.8 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -9.5 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -9.2 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.5 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | -7.5 | -3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -7.4 | -8.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -6.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.0 | -2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | ATPase family AAA domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:123,319,850-123,416,350 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO2000, DKFZp667N1320, MGC5254, MGC29843, CT137, ANCCA |
| Gene groups (HGNC) | AAA ATPases; Bromodomain containing; MicroRNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 2 pathways, smallest: TFAP2 (AP-2) family regulates transcription of growth factors and their receptors; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PL18](https://www.uniprot.org/uniprotkb/Q6PL18) (ATPase family AAA domain-containing protein 2):

> May be a transcriptional coactivator of the nuclear receptor ESR1 required to induce the expression of a subset of estradiol target genes, such as CCND1, MYC and E2F1. May play a role in the recruitment or occupancy of CREBBP at some ESR1 target gene promoters. May be required for histone hyperacetylation. Involved in the estrogen-induced cell proliferation and cell cycle progression of breast cancer cells.

**Summary**, from NCBI Gene [29028](https://www.ncbi.nlm.nih.gov/gene/29028):

> A large family of ATPases has been described, whose key feature is that they share a conserved region of about 220 amino acids that contains an ATP-binding site. The proteins that belong to this family either contain one or two AAA (ATPases Associated with diverse cellular Activities) domains. AAA family proteins often perform chaperone-like functions that assist in the assembly, operation, or disassembly of protein complexes. The protein encoded by this gene contains two AAA domains, as well …

**Accessions** — [HGNC:30123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30123) · Entrez [29028](https://www.ncbi.nlm.nih.gov/gene/29028) · UniProt [Q6PL18](https://www.uniprot.org/uniprotkb/Q6PL18) · Ensembl [ENSG00000156802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156802)

## Data

Gene col 8014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8014); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8014]; `tensor/DDL_lfc|DDL_z.npy` [8014]; `embed/gene_vectors.npy` [8014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8014 or target_col == 8014). Every well: [[ATAD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATAD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
