---
symbol: "NUDCD1"
type: "gene"
col: 4189
ensembl_id: "ENSG00000120526"
name: "NudC domain containing 1"
location: "8q23.1"
module: 4
arm: "+"
pooled_cpm: 62.14
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NUDCD1

*NudC domain containing 1* — 8q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.73× (z +12.8, q 5e-35, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.41× (z +8.1, q 5e-14, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.697× (z -12.0, q 3e-30, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1A]] (+0.64, fdr 7e-06), [[LYAR]] (+0.61, fdr 1e-05), [[EBNA1BP2]] (+0.61, fdr 1e-05); moves opposite to [[KMT2E]] (-0.57, fdr 2e-05), [[CA11]] (-0.56, fdr 2e-05), [[CLIP3]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 26 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.73×** | +12.8 | 5e-35 | 41/48 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.73×** | +12.8 | 5e-35 | 37/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.49×** | +9.4 | 1e-18 | 32/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.47×** | +9.1 | 2e-17 | 32/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.45×** | +8.3 | 9e-15 | 27/42 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +8.1 | 5e-14 | 35/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +8.1 | 6e-14 | 31/49 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +7.3 | 3e-11 | 26/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +6.6 | 3e-09 | 27/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.32×** | +6.5 | 5e-09 | 26/48 (HT-29, RKO, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +6.5 | 5e-09 | 29/48 (RPMI-7951, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.31×** | +6.2 | 2e-08 | 24/48 (A-172, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +5.9 | 2e-07 | 30/48 (NCI-H2347, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +5.5 | 1e-06 | 23/47 (HOP62, NCI-H460, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +5.4 | 3e-06 | 26/47 (HEC-1-A, HOP62, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 5e-06 | 22/48 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.8 | 5e-05 | 14/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.20× | +4.2 | 7e-04 | 11/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.002 | 18/47 (NCI-H460, HOP62, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.002 | 16/48 (HOP62, SW480, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.7 | 0.005 | 13/48 (HOP62, H4, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.007 | 14/46 (HOP62, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.012 | 11/48 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.014 | 13/48 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4189.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.697×** | -12.0 | 3e-30 | 32/48 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.788×** | -5.6 | 6e-06 | 28/48 (J82, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -4.6 | 7e-04 | 21/48 (RKO, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.826×** | -4.5 | 0.001 | 23/47 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.3 | 0.002 | 3/49 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.852× | -4.3 | 0.002 | 17/48 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.831×** | -4.2 | 0.002 | 19/47 (H4, RKO, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.844× | -4.0 | 0.005 | 16/48 (RKO, RPMI-7951, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.848× | -3.9 | 0.006 | 12/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.853× | -3.7 | 0.011 | 22/48 (RKO, A498, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.851× | -3.7 | 0.013 | 16/48 (HepG2/C3A, RKO, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.899× | -3.6 | 0.017 | 10/48 (CHP-212, A549, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.858× | -3.5 | 0.024 | 10/48 (SW 1088, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.905× | -3.3 | 0.034 | 9/49 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.2 | 0.049 | 10/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.874× | -3.2 | 0.053 | 9/47 (SK-MEL-2, LOX-IMVI, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.872× | -3.1 | 0.063 | 14/48 (A498, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.872× | -3.1 | 0.063 | 11/48 (RKO, J82, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.064 | 13/48 (CFPAC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.890× | -3.0 | 0.068 | 9/48 (HEC-1-A, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | 0.876× | -3.0 | 0.071 | 9/48 (NCI-H2347, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 301 | 1 (1 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +8.5) ⚠ cell-cycle shift, explains ~55% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.237× (z -20.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.551× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.20× (z +10.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H460 (line)]] | wt | 30.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[HEC-1-A (line)]] | alt | 53.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0705× (z -27.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.539× (z -9.6) |
| [[HT-29 (line)]] | alt | 32.4 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +10.9) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[A498 (line)]] | wt | 140 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -14.4) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.503× (z -13.9) |
| [[C32 (line)]] | wt | 41.2 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.84× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H23 (line)]] | alt | 61.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2347 (line)]] | alt | 51.2 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.39× (z +9.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.34× (z +9.3) | — |
| [[A-172 (line)]] | wt | 57.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -12.5) |
| [[A549 (line)]] | wt | 59.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | — |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 65.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.5) |
| [[C-33 A (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -10.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -9.0) ⚠ cell-cycle shift, explains ~94% of this change |
| [[HOP62 (line)]] | alt | 58.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -9.0) |
| [[J82 (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -18.6) |
| [[LOX-IMVI (line)]] | wt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -11.0) |
| [[SW48 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.646× (z -9.0) |
| [[A-427 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1A]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LYAR]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SPATA5]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NDUFAF2]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[URB2]] | +0.60 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SNRPD1]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[EIPR1]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[EIF2S1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TOMM40]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[TWNK]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MTAP]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[CA11]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CLIP3]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[HOOK2]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CCDC159]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CCDC115]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TRA2A]] | -0.51 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[CBX4]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RAP1GAP]] | -0.51 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[IST1]] | -0.51 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity lowers NUDCD1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.30× higher at baseline in the lines without MPZL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[NFATC4]] | B | NFATC4 activity lowers NUDCD1's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 1.42× higher at baseline in the lines without NFATC4 | 0.071 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.2, -34.7); signed map (-4.7, -48.2). **Vector** length 121, 34.3% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.7 | +12.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.1 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.7 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -12.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.5 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Ixazomib (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | NudC domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.1 — chr8:109,240,919-109,334,121 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CML66, FLJ14991 |
| Gene groups (HGNC) | NudC family |
| Matched by | ensembl_id |

UniProt [Q96RS6](https://www.uniprot.org/uniprotkb/Q96RS6) carries no function annotation.

**Summary**, from NCBI Gene [84955](https://www.ncbi.nlm.nih.gov/gene/84955):

> Predicted to be involved in immune system process. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24306) · Entrez [84955](https://www.ncbi.nlm.nih.gov/gene/84955) · UniProt [Q96RS6](https://www.uniprot.org/uniprotkb/Q96RS6) · Ensembl [ENSG00000120526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120526)

## Data

Gene col 4189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4189); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4189]; `tensor/DDL_lfc|DDL_z.npy` [4189]; `embed/gene_vectors.npy` [4189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4189 or target_col == 4189). Every well: [[NUDCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
