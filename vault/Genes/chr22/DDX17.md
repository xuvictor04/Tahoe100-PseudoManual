---
symbol: "DDX17"
type: "gene"
col: 1887
ensembl_id: "ENSG00000100201"
name: "DEAD-box helicase 17"
location: "22q13.1"
module: 95
arm: "+"
pooled_cpm: 280.1
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# DDX17

*DEAD-box helicase 17* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.64× (z +13.0, q 5e-36, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.251× (z -36.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPH2]] (+0.63, fdr 3e-05), [[DDX6]] (+0.62, fdr 1e-05), [[MED12]] (+0.61, fdr 1e-05); moves opposite to [[GRB2]] (-0.55, fdr 5e-05), [[NAPG]] (-0.54, fdr 4e-04), [[SGTB]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +13.0 | 5e-36 | 42/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +9.3 | 5e-18 | 38/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +7.0 | 5e-10 | 34/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +6.5 | 1e-08 | 30/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +5.0 | 6e-05 | 23/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.14× | +4.9 | 7e-05 | 19/48 (HEC-1-A, SNU-1, …) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.8 | 1e-04 | 26/47 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 1.18× | +4.2 | 0.002 | 13/48 (HEC-1-A, NCI-H460, …) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.021 | 24/50 (A-427, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.078 | 13/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.13× | +3.1 | 0.11 | 4/48 (SHP-77, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.0 | 0.11 | 1/48 (NCI-H661) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.251×** | -36.2 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.258×** | -35.5 | 0e+00 | 48/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.302×** | -31.4 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -24.9 | 0e+00 | 47/49 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.490×** | -18.7 | 0e+00 | 48/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.586×** | -14.0 | 9e-43 | 46/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.691×** | -9.3 | 9e-19 | 38/48 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.508×** | -9.3 | 1e-18 | 48/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.565×** | -7.8 | 3e-13 | 42/45 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.726×** | -7.8 | 5e-13 | 30/45 (SNU-1, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -7.7 | 7e-13 | 40/48 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.738×** | -7.7 | 9e-13 | 38/50 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **0.754×** | -7.4 | 6e-12 | 31/49 (NCI-H1573, RPMI-7951, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.758×** | -7.3 | 1e-11 | 33/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -7.2 | 2e-11 | 24/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -4.9 | 3e-05 | 18/48 (HOP62, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.831×** | -4.9 | 3e-05 | 24/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.834× | -4.8 | 5e-05 | 23/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.839× | -4.6 | 1e-04 | 22/48 (SNU-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.851× | -4.2 | 6e-04 | 22/48 (NCI-H23, HepG2/C3A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.805×** | -4.1 | 0.001 | 27/48 (MIA PaCa-2, SW 1088, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 396 | 3 (1 ⚠) | 10 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.180× (z -31.5) |
| [[LoVo (line)]] | wt | 346 | 3 (1 ⚠) | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.249× (z -26.0) |
| [[NCI-H460 (line)]] | wt | 156 | 6 (2 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.226× (z -27.3) |
| [[HEC-1-A (line)]] | alt | 294 | 3 (1 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +16.5) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.33× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.283× (z -24.5) |
| [[NCI-H23 (line)]] | alt | 368 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -30.3) |
| [[SNU-1 (line)]] | wt | 346 | 5 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.263× (z -19.8) |
| [[HOP62 (line)]] | alt | 249 | 1 | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.175× (z -27.4) |
| [[hTERT-HPNE (line)]] | wt | 267 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -23.3) |
| [[KATO III (line)]] | alt | 241 | 4 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -22.8) |
| [[LS 180 (line)]] | wt | 254 | 3 (1 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.290× (z -22.9) |
| [[SK-MEL-2 (line)]] | alt | 403 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -25.0) |
| [[C-33 A (line)]] | alt | 462 | 1 | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.267× (z -23.0) |
| [[HT-29 (line)]] | alt | 201 | 1 | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.222× (z -25.5) |
| [[MIA PaCa-2 (line)]] | alt | 305 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -27.3) |
| [[RPMI-7951 (line)]] | alt | 283 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -22.7) |
| [[SW1417 (line)]] | alt | 203 | 3 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +14.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -19.2) |
| [[A-172 (line)]] | wt | 198 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -21.1) |
| [[A549 (line)]] | wt | 221 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -22.7) |
| [[AsPC-1 (line)]] | alt | 194 | 2 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.7) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -21.8) |
| [[BT-474 (line)]] | alt | 318 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -27.1) |
| [[C32 (line)]] | wt | 344 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -22.5) |
| [[COLO 205 (line)]] | alt | 387 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -26.4) |
| [[HCT15 (line)]] | alt | 486 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -22.5) |
| [[LOX-IMVI (line)]] | wt | 251 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -25.9) |
| [[Panc 03.27 (line)]] | alt | 214 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -22.7) |
| [[PANC-1 (line)]] | alt | 254 | 1 | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.230× (z -25.1) |
| [[RKO (line)]] | wt | 326 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -16.8) |
| [[SNU-423 (line)]] | alt | 302 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -24.9) |
| [[SW 900 (line)]] | alt | 215 | 2 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -20.7) |
| [[SW48 (line)]] | wt | 281 | 2 (1 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +12.9) | [[Belinostat (drug)]] 5 µM 0.241× (z -19.6) |
| [[A498 (line)]] | wt | 263 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -23.1) |
| [[CFPAC-1 (line)]] | alt | 275 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -22.0) |
| [[HS-578T (line)]] | alt | 252 | 1 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.260× (z -19.2) |
| [[J82 (line)]] | alt | 229 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -20.0) |
| [[NCI-H1573 (line)]] | alt | 653 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -21.1) |
| [[NCI-H1792 (line)]] | alt | 210 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -22.1) |
| [[A-427 (line)]] | wt | 206 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -18.9) |
| [[CHP-212 (line)]] | wt | 391 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.248× (z -14.6) |
| [[H4 (line)]] | wt | 283 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -18.2) |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -19.2) |
| [[Hs 766T (line)]] | wt | 432 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.2) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 5 µM 0.283× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 205 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.8) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -16.7) |
| [[AN3 CA (line)]] | alt | 262 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -21.7) |
| [[SHP-77 (line)]] | alt | 252 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -16.4) |
| [[SW 1271 (line)]] | alt | 361 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -10.3) |
| [[SW 1088 (line)]] | alt | 346 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -11.0) |
| [[NCI-H2122 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH2]] | +0.63 | +0.43 / +0.63 | both halves | 3e-05 | STRING 580 |
| [[DDX6]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 | same gene group; STRING 584 |
| [[MED12]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SCYL3]] | +0.60 | +0.58 / +0.26 | both halves | 4e-04 |  |
| [[SRRM2]] | +0.59 | +0.44 / +0.52 | both halves | 3e-05 | STRING 533 |
| [[TMEM80]] | +0.58 | +0.45 / +0.30 | both halves | 2e-04 |  |
| [[ZNF776]] | +0.58 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[BAZ2B]] | +0.58 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[SCAF8]] | +0.57 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[EP300]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 870 |
| [[ACIN1]] | +0.56 | +0.37 / +0.58 | both halves | 8e-05 | STRING 611 |
| [[PNRC2]] | +0.56 | +0.53 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB2]] | -0.55 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[NAPG]] | -0.54 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[SGTB]] | -0.52 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[RGS10]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[CCNB1IP1]] | -0.51 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[GDAP2]] | -0.50 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[GNAI3]] | -0.50 | -0.43 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[SPTLC2]] | -0.50 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[WASF3]] | -0.50 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[EIF4EBP1]] | -0.50 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[EXOSC1]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CARD19]] | -0.49 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[ST6GALNAC6]] | -0.48 | -0.37 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-9.2, 3.7); signed map (17.6, -22.5). **Vector** length 112, 37.9% of its response variance represented; |z| ≥ 3 in 1,523 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +10.7 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | +10.1 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +9.7 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +9.3 | +13.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +7.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +4.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.3 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.6 | -0.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.4 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.0 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.3 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -14.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -18.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -3.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.7 | -0.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.6 | +0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,483,438-38,507,660 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P72 |
| Gene groups (HGNC) | DEAD-box helicases |
| Reactome | 3 pathways, smallest: SUMOylation of transcription cofactors; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92841](https://www.uniprot.org/uniprotkb/Q92841) (Probable ATP-dependent RNA helicase DDX17):

> As an RNA helicase, unwinds RNA and alters RNA structures through ATP binding and hydrolysis. Involved in multiple cellular processes, including pre-mRNA splicing, alternative splicing, ribosomal RNA processing and miRNA processing, as well as transcription regulation. Regulates the alternative splicing of exons exhibiting specific features. For instance, promotes the inclusion of AC-rich alternative exons in CD44 transcripts. This function requires the RNA helicase activity. Affects NFAT5 and …

**Summary**, from NCBI Gene [10521](https://www.ncbi.nlm.nih.gov/gene/10521):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and splicesosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes …

**Accessions** — [HGNC:2740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2740) · Entrez [10521](https://www.ncbi.nlm.nih.gov/gene/10521) · UniProt [Q92841](https://www.uniprot.org/uniprotkb/Q92841) · Ensembl [ENSG00000100201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100201)

## Data

Gene col 1887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1887); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1887]; `tensor/DDL_lfc|DDL_z.npy` [1887]; `embed/gene_vectors.npy` [1887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1887 or target_col == 1887). Every well: [[DDX17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
