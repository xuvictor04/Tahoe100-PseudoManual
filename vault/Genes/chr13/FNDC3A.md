---
symbol: "FNDC3A"
type: "gene"
col: 2253
ensembl_id: "ENSG00000102531"
name: "fibronectin type III domain containing 3A"
location: "13q14.2"
module: 2
arm: "-"
pooled_cpm: 307.18
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FNDC3A

*fibronectin type III domain containing 3A* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 1.28× (z +5.8, q 4e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.518× (z -22.6, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC1A3]] (+0.58, fdr 2e-05), [[ANKRD17]] (+0.56, fdr 5e-05), [[ZC3H12C]] (+0.55, fdr 4e-05); moves opposite to [[DNAJC5]] (-0.54, fdr 3e-05), [[CAMSAP1]] (-0.54, fdr 7e-05), [[DPP9]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SEMA7A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +5.8 | 4e-06 | 31/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +5.5 | 1e-05 | 25/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.19× | +4.4 | 0.002 | 20/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.13× | +4.3 | 0.002 | 10/48 (SW 900, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.2 | 0.003 | 22/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.7 | 0.017 | 20/48 (AsPC-1, RKO, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.029 | 17/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.056 | 20/48 (C32, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.14× | +3.3 | 0.060 | 18/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.1 | 0.10 | 3/48 (NCI-H23, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -22.6 | 0e+00 | 46/49 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.428×** | -20.6 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.454×** | -19.2 | 0e+00 | 48/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.479×** | -17.9 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.605×** | -12.2 | 4e-32 | 41/49 (COLO 205, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.622×** | -11.1 | 2e-26 | 38/44 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -9.0 | 2e-17 | 43/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.705×** | -8.5 | 2e-15 | 34/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -8.0 | 8e-14 | 33/48 (H4, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.733×** | -6.6 | 3e-09 | 30/45 (CHP-212, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.755×** | -6.5 | 3e-09 | 35/48 (hTERT-HPNE, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.775×** | -5.9 | 1e-07 | 31/47 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.792×** | -5.7 | 7e-07 | 30/48 (H4, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.786×** | -5.6 | 9e-07 | 29/50 (hTERT-HPNE, BT-474, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.810×** | -5.1 | 1e-05 | 29/47 (BT-474, Panc 03.27, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -5.0 | 2e-05 | 16/48 (CHP-212, BT-474, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.770×** | -4.5 | 2e-04 | 28/48 (SW 900, HCT15, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.879× | -4.4 | 3e-04 | 13/49 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.722×** | -4.0 | 0.002 | 26/46 (SW 900, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.803×** | -3.8 | 0.004 | 22/48 (SNU-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.741×** | -3.7 | 0.005 | 22/49 (HepG2/C3A, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.862× | -3.6 | 0.007 | 20/48 (H4, COLO 205, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.873× | -3.1 | 0.029 | 17/48 (AsPC-1, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.887× | -2.9 | 0.069 | 18/48 (NCI-H1573, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 863 | 9 (6 ⚠) | 7 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.75× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.86× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -23.8) |
| [[BT-474 (line)]] | alt | 539 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -18.4) |
| [[HOP62 (line)]] | alt | 219 | 3 (2 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.05× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.394× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 662 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.0) |
| [[RKO (line)]] | wt | 339 | 3 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.76× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.327× (z -17.9) |
| [[J82 (line)]] | alt | 307 | 3 (1 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 2.44× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -11.0) |
| [[H4 (line)]] | wt | 249 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.342× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 231 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 366 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -14.5) |
| [[SW 900 (line)]] | alt | 447 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -11.4) |
| [[CHP-212 (line)]] | wt | 515 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -13.4) |
| [[COLO 205 (line)]] | alt | 771 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.280× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 358 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -18.2) |
| [[Hs 766T (line)]] | wt | 411 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -16.2) |
| [[HT-29 (line)]] | alt | 334 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 253 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 191 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.354× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 141 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.477× (z -12.0) |
| [[SHP-77 (line)]] | alt | 486 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -15.5) |
| [[SW480 (line)]] | alt | 433 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -19.2) |
| [[A-172 (line)]] | wt | 287 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -16.2) |
| [[C32 (line)]] | wt | 350 | 2 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.46× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -15.3) |
| [[HS-578T (line)]] | alt | 195 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -14.0) |
| [[KATO III (line)]] | alt | 295 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -13.9) |
| [[LS 180 (line)]] | wt | 365 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 218 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.7) |
| [[PANC-1 (line)]] | alt | 209 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -16.0) |
| [[SNU-423 (line)]] | alt | 224 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -15.6) |
| [[HCT15 (line)]] | alt | 251 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.375× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 211 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.519× (z -11.5) |
| [[LoVo (line)]] | wt | 225 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.533× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 189 | 0 | 3 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.144× (z -13.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.488× (z -9.5) |
| [[SW1417 (line)]] | alt | 255 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -16.1) |
| [[A-427 (line)]] | wt | 160 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 195 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +23.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.37× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 272 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 137 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -8.8) |
| [[SW48 (line)]] | wt | 364 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.8) |
| [[A498 (line)]] | wt | 255 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -18.8) |
| [[A549 (line)]] | wt | 257 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -16.7) |
| [[C-33 A (line)]] | alt | 174 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 223 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -11.4) |
| [[SNU-1 (line)]] | wt | 221 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.525× (z -8.5) |
| [[AN3 CA (line)]] | alt | 222 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 414 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 447 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 326 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC1A3]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ANKRD17]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ZC3H12C]] | +0.55 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[CRADD]] | +0.51 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[ELF1]] | +0.51 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[IL1R1]] | +0.51 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[ARID5B]] | +0.50 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[CEBPD]] | +0.50 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[SAMSN1]] | +0.50 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[GOPC]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[NFE2L2]] | +0.49 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[BRAF]] | +0.49 | +0.39 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC5]] | -0.54 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CAMSAP1]] | -0.54 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[DPP9]] | -0.53 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[LTBP4]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CAPN10]] | -0.52 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[PLCB3]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[WIPI2]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[MACO1]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MIEF2]] | -0.49 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[CROCCP3]] | -0.49 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[MYO9B]] | -0.49 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[CDS2]] | -0.48 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA7A]] | B | SEMA7A activity lowers FNDC3A's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.47× higher at baseline in the lines without SEMA7A | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (25.0, 10.4); signed map (16.6, -9.8). **Vector** length 119, 40.0% of its response variance represented; |z| ≥ 3 in 1,616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +6.7 | -12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.0 | -11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +0.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.9 | +1.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.8 | +2.6 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.4 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.2 | -2.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.9 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM | ⚠ position correction uncertain | -3.2 | -5.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin type III domain containing 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:48,975,912-49,209,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA203I16.5, KIAA0970; previously FNDC3 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2H6](https://www.uniprot.org/uniprotkb/Q9Y2H6) (Fibronectin type-III domain-containing protein 3A):

> Mediates spermatid-Sertoli adhesion during spermatogenesis.

**Summary**, from NCBI Gene [22862](https://www.ncbi.nlm.nih.gov/gene/22862):

> Enables RNA binding activity. Predicted to be involved in spermatid development. Predicted to act upstream of or within Sertoli cell development; cell-cell adhesion; and fertilization. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20296) · Entrez [22862](https://www.ncbi.nlm.nih.gov/gene/22862) · UniProt [Q9Y2H6](https://www.uniprot.org/uniprotkb/Q9Y2H6) · Ensembl [ENSG00000102531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102531)

## Data

Gene col 2253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2253); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2253]; `tensor/DDL_lfc|DDL_z.npy` [2253]; `embed/gene_vectors.npy` [2253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2253 or target_col == 2253). Every well: [[FNDC3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNDC3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
