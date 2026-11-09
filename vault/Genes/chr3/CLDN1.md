---
symbol: "CLDN1"
type: "gene"
col: 8672
ensembl_id: "ENSG00000163347"
name: "claudin 1"
location: "3q28"
module: 14
arm: "+"
pooled_cpm: 69.66
n_lines_expressing: 27
n_dd_up: 41
n_dd_down: 14
n_dd_up_clean: 27
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CLDN1

*claudin 1* — 3q28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.64× (z +17.7, q 0e+00, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.610× (z -9.0, q 9e-17, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL1]] (+0.64, fdr 1e-05), [[CLDN16]] (+0.61, fdr 7e-06, ⚠ same locus), [[LINC02605]] (+0.59, fdr 1e-05), [[KRT80]] (+0.58, fdr 1e-05); moves opposite to [[SAP130]] (-0.52, fdr 3e-05), [[TNPO3]] (-0.51, fdr 3e-05), [[ZCCHC17]] (-0.51, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 9 go from it, the strongest it → [[NCEH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.64×** | +17.7 | 0e+00 | 19/25 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.87×** | +16.1 | 0e+00 | 17/25 (A498, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.45×** | +15.7 | 0e+00 | 18/25 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +15.0 | 0e+00 | 12/26 (A549, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +12.8 | 3e-35 | 15/24 (LS 180, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +12.5 | 1e-33 | 14/25 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +11.3 | 2e-27 | 19/25 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.51×** | +10.6 | 3e-24 | 16/26 (HT-29, A-427, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +10.3 | 4e-23 | 21/25 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.72×** | +9.8 | 5e-21 | 19/25 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +9.8 | 7e-21 | 20/26 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.4 | 2e-19 | 7/24 (NCI-H23, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +9.3 | 4e-19 | 15/25 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.68×** | +9.1 | 5e-18 | 20/25 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.9 | 2e-17 | 7/26 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +8.7 | 1e-16 | 6/26 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.54×** | +7.9 | 1e-13 | 19/25 (A-427, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.48×** | +7.2 | 2e-11 | 16/25 (HT-29, A-427, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.8 | 2e-07 | 11/25 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.6 | 4e-07 | 15/26 (NCI-H2347, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.3 | 2e-06 | 8/25 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.610×** | -9.0 | 9e-17 | 20/25 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.767×** | -4.9 | 3e-04 | 10/25 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.614×** | -4.7 | 6e-04 | 17/24 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.780×** | -4.3 | 0.002 | 20/25 (A549, KATO III, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.791×** | -4.3 | 0.002 | 9/25 (NCI-H460, A549, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.5 µM |  | **0.798×** | -4.1 | 0.003 | 1/25 (AsPC-1) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.801×** | -4.1 | 0.004 | 7/25 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.803×** | -4.0 | 0.004 | 11/25 (NCI-H460, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.818×** | -3.7 | 0.014 | 6/25 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.808×** | -3.6 | 0.015 | 8/25 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.015 | 15/25 (NCI-H23, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.015 | 15/26 (Hs 766T, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.877× | -3.4 | 0.026 | 7/25 (NCI-H460, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.029 | 10/25 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.056 | 11/25 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.725×** | -3.1 | 0.072 | 1/25 (Panc 03.27) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.074 | 7/25 (NCI-H460, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 87.3 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +21.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.99× (z +18.7) | [[Ixazomib citrate (drug)]] 5 µM 0.302× (z -10.2) |
| [[A549 (line)]] | wt | 121 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +10.6) | [[Ixazomib citrate (drug)]] 5 µM 0.191× (z -14.5) |
| [[KATO III (line)]] | alt | 163 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.469× (z -8.7) |
| [[A-427 (line)]] | wt | 419 | 2 | 3 (3 ⚠) | [[Peretinoin (drug)]] 5 µM 2.56× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -12.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +19.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.00× (z +14.9) | — |
| [[HEC-1-A (line)]] | alt | 162 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.441× (z -9.4) |
| [[Hs 766T (line)]] | wt | 159 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.163× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 140 | 1 | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.25× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.398× (z -9.2) |
| [[PANC-1 (line)]] | alt | 20.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.40× (z +17.4) | — |
| [[SW480 (line)]] | alt | 74.9 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.442× (z -8.9) |
| [[J82 (line)]] | alt | 47.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +17.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.99× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 122 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -14.6) |
| [[SW1417 (line)]] | alt | 185 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Auranofin (drug)]] 5 µM 0.244× (z -15.4) |
| [[HT-29 (line)]] | alt | 49.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 85.9 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.41× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 86.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.97× (z +12.1) | — |
| [[HepG2_C3A (line)]] | wt | 63.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 71.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Daptomycin (drug)]] 0.5 µM 3.95× (z +8.5) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 234 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 3.31× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.304× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +13.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.84× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.65× (z +8.9) | — |
| [[A-172 (line)]] | wt | 6.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CLDN16]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 | same gene group; pathway: Cell junction organization; STRING 831; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[LINC02605]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[KRT80]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CXCL2]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LYPD1]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CXCL3]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HIVEP2]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[FILIP1L]] | +0.55 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[SERPINB7]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CD274]] | +0.54 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CDH2]] | +0.54 | +0.48 / +0.41 | both halves | 4e-05 | pathway: Cell junction organization; STRING 675 |
| [[ZNF702P]] | +0.53 | +0.39 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP130]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TNPO3]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ZCCHC17]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[UFD1]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[RAB43]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[NFATC3]] | -0.48 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[PSMD13]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 | pathway: Cell junction organization |
| [[MED31]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SS18L1]] | -0.47 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[SLC30A6]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[DRD4]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers CLDN1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[RASEF]] | B | RASEF activity strengthens CLDN1's drug response | lines that do not express RASEF (7) vs lines expressing it (19) | the lines without RASEF respond 0.27× as strongly (z diff +3.28); strongest at Homoharringtonine 5 µM: 0.62x vs 2.34x (z diff +11.7) | 0.053 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers CLDN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TSPAN2]] | B | TSPAN2 activity raises CLDN1's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without TSPAN2 | 0.069 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[ATXN1-AS1]] | B | ATXN1-AS1 activity raises CLDN1's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 3.72× lower at baseline in the lines without ATXN1-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[CLDN16]] | C | CLDN16 activity raises CLDN1's level | lines that do not express CLDN16 (27) vs lines expressing it (23) | 6.37× lower at baseline in the lines without CLDN16 | 2e-04 | ⚠ within organs, on part of the lines; also absent: DAW1, ENSG00000257869, ENSG00000255029; co-absent with the target |
| [[EDN1]] | C | EDN1 activity raises CLDN1's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 4.25× lower at baseline in the lines without EDN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC; co-absent with the target |
| [[LINC02577]] | C | LINC02577 activity raises CLDN1's level | lines that do not express LINC02577 (22) vs lines expressing it (28) | 2.95× lower at baseline in the lines without LINC02577 | 0.038 | ⚠ within organs, on part of the lines; also absent: CALB2, LHX1-DT, PTX3; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCEH1]] | B | CLDN1 activity raises NCEH1's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without CLDN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[RAD9A]] | B | CLDN1 activity raises RAD9A's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 1.40× lower at baseline in the lines without CLDN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[NEDD4L]] | B | CLDN1 activity raises NEDD4L's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 1.27× lower at baseline in the lines without CLDN1 | 0.064 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[LINC01186]] | B | CLDN1 activity raises LINC01186's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without CLDN1 | 0.085 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[LEPROT]] | B | CLDN1 activity raises LEPROT's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 1.23× lower at baseline in the lines without CLDN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[INHBA]] | B | CLDN1 activity lowers INHBA's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 2.01× higher at baseline in the lines without CLDN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[KRT80]] | C | CLDN1 activity raises KRT80's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 2.64× lower at baseline in the lines without CLDN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH; co-absent with the target |
| [[EDN1]] | C | CLDN1 activity raises EDN1's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 4.35× lower at baseline in the lines without CLDN1 | 0.027 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH; co-absent with the target |
| [[CLDN16]] | C | CLDN1 activity raises CLDN16's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 2.40× lower at baseline in the lines without CLDN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, 26.5); signed map (43.2, 16.0). **Vector** length 100, 27.1% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +10.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +9.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.6 | +7.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.1 | -9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.9 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | claudin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q28 — chr3:190,305,707-190,322,446 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEMP1, ILVASC |
| Gene groups (HGNC) | Claudins |
| Reactome | 7 pathways, smallest: Tight junction interactions; Dengue Virus Attachment and Entry; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O95832](https://www.uniprot.org/uniprotkb/O95832) (Claudin-1):

> Claudins function as major constituents of the tight junction complexes that regulate the permeability of epithelia. While some claudin family members play essential roles in the formation of impermeable barriers, others mediate the permeability to ions and small molecules. Often, several claudin family members are coexpressed and interact with each other, and this determines the overall permeability. CLDN1 is required to prevent the paracellular diffusion of small molecules through tight …

**Summary**, from NCBI Gene [9076](https://www.ncbi.nlm.nih.gov/gene/9076):

> Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. These junctions are comprised of sets of continuous networking strands in the outwardly facing cytoplasmic leaflet, with complementary grooves in the inwardly facing extracytoplasmic leaflet. The protein encoded by this gene, a member of the …

**Accessions** — [HGNC:2032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2032) · Entrez [9076](https://www.ncbi.nlm.nih.gov/gene/9076) · UniProt [O95832](https://www.uniprot.org/uniprotkb/O95832) · Ensembl [ENSG00000163347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163347)

## Data

Gene col 8672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8672); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8672]; `tensor/DDL_lfc|DDL_z.npy` [8672]; `embed/gene_vectors.npy` [8672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8672 or target_col == 8672). Every well: [[CLDN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLDN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
