---
symbol: "MSL1"
type: "gene"
col: 12061
ensembl_id: "ENSG00000188895"
name: "MSL complex subunit 1"
location: "17q21.1"
module: 15
arm: "+"
pooled_cpm: 81.91
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MSL1

*MSL complex subunit 1* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +13.8, q 9e-41, up in 40 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 13 lines (A549 2.41×, NCI-H2030 2.17×, SW480 1.94×, KATO III 2.20×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 1.88×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.233× (z -34.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM10]] (+0.63, fdr 1e-05), [[BCL2L2-PABPN1]] (+0.60, fdr 3e-05), [[STBD1]] (+0.59, fdr 6e-05); moves opposite to [[WDR7]] (-0.60, fdr 1e-05), [[RPAP3]] (-0.58, fdr 3e-05), [[TBC1D19]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DGKE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12061.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 13 lines (A549 2.41×, NCI-H2030 2.17×, SW480 1.94×, KATO III 2.20×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 1.88×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +13.8 | 9e-41 | 40/49 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.0 | 4e-07 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +5.8 | 2e-06 | 29/48 (A549, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.042 | 20/47 (SW480, SW1417, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.042 | 16/47 (HEC-1-A, HOP62, …) | rises with dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.042 | 17/47 (LoVo, J82, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.16× | +3.5 | 0.042 | 17/47 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.052 | 15/48 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.052 | 10/48 (HOP62, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.052 | 19/48 (LoVo, SW480, …) | two highest doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.063 | 10/47 (Panc 03.27, HEC-1-A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.233×** | -34.8 | 0e+00 | 48/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.260×** | -32.2 | 0e+00 | 48/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.305×** | -28.4 | 0e+00 | 48/48 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.444×** | -27.4 | 0e+00 | 44/48 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.539×** | -14.8 | 0e+00 | 46/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.656×** | -14.2 | 5e-44 | 45/48 (NCI-H2347, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -12.7 | 8e-35 | 38/48 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.477×** | -12.5 | 5e-34 | 38/48 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.504×** | -8.6 | 8e-16 | 42/49 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.738×** | -7.0 | 2e-10 | 41/48 (LoVo, HS-578T, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -6.3 | 2e-08 | 33/48 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.771×** | -6.2 | 3e-08 | 30/48 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.762×** | -6.1 | 4e-08 | 28/48 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.784×** | -5.8 | 3e-07 | 25/49 (HS-578T, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.782×** | -5.4 | 2e-06 | 25/45 (MIA PaCa-2, A498, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.754×** | -4.8 | 7e-05 | 25/49 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.830×** | -4.4 | 3e-04 | 24/48 (A-172, HOP62, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 95.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -26.0) |
| [[NCI-H1573 (line)]] | alt | 86.2 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -17.4) |
| [[A-427 (line)]] | wt | 86.6 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.234× (z -19.2) |
| [[A549 (line)]] | wt | 71.9 | 1 | 7 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.198× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 85.9 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -27.0) |
| [[PANC-1 (line)]] | alt | 81.5 | 1 | 7 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -23.4) |
| [[SW480 (line)]] | alt | 73.1 | 2 (1 ⚠) | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.219× (z -21.6) |
| [[A498 (line)]] | wt | 108 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -22.5) |
| [[HEC-1-A (line)]] | alt | 97.5 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -21.2) |
| [[HS-578T (line)]] | alt | 79.0 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -17.3) |
| [[Panc 03.27 (line)]] | alt | 81.0 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -22.0) |
| [[A-172 (line)]] | wt | 123 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -25.3) |
| [[AsPC-1 (line)]] | alt | 52.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -16.4) |
| [[HT-29 (line)]] | alt | 79.1 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -17.8) |
| [[LS 180 (line)]] | wt | 83.5 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 104 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 79.6 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.226× (z -20.4) |
| [[RKO (line)]] | wt | 66.0 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -29.0) |
| [[SK-MEL-2 (line)]] | alt | 88.8 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.179× (z -18.5) |
| [[AN3 CA (line)]] | alt | 91.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -11.1) |
| [[HOP62 (line)]] | alt | 81.7 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -20.2) |
| [[hTERT-HPNE (line)]] | wt | 84.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -15.1) |
| [[J82 (line)]] | alt | 76.6 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -18.0) |
| [[KATO III (line)]] | alt | 76.3 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.259× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 93.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -24.0) |
| [[NCI-H23 (line)]] | alt | 80.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -22.9) |
| [[SW 900 (line)]] | alt | 60.1 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -15.7) |
| [[BT-474 (line)]] | alt | 59.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -19.1) |
| [[C-33 A (line)]] | alt | 116 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 109 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -18.7) |
| [[CHP-212 (line)]] | wt | 127 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.220× (z -11.8) |
| [[Hs 766T (line)]] | wt | 63.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.200× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 73.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -17.4) |
| [[RPMI-7951 (line)]] | alt | 65.7 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.214× (z -13.6) |
| [[SW1417 (line)]] | alt | 62.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -16.6) |
| [[COLO 205 (line)]] | alt | 83.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 76.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -12.9) |
| [[LoVo (line)]] | wt | 69.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -17.1) |
| [[SNU-423 (line)]] | alt | 74.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -14.5) |
| [[SW48 (line)]] | wt | 72.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -14.7) |
| [[C32 (line)]] | wt | 62.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -12.6) |
| [[H4 (line)]] | wt | 72.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -10.7) |
| [[HCT15 (line)]] | alt | 89.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -11.5) |
| [[SHP-77 (line)]] | alt | 52.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -10.2) |
| [[SW 1271 (line)]] | alt | 88.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.5) |
| [[SNU-1 (line)]] | wt | 72.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -10.5) |
| [[SW 1088 (line)]] | alt | 67.1 | 0 | 1 | — | [[Daidzin (drug)]] 5 µM 0.0620× (z -9.0) |
| [[NCI-H2122 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM10]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[BCL2L2-PABPN1]] | +0.60 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[STBD1]] | +0.59 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[SETD1B]] | +0.59 | +0.27 / +0.58 | both halves | 3e-04 | pathway: Chromatin modifying enzymes |
| [[EEF1AKMT3]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[S100PBP]] | +0.57 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[ZNF460-AS1]] | +0.56 | +0.22 / +0.48 | both halves | 6e-04 |  |
| [[SOS1]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SLC12A9]] | +0.55 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[SEC24B-AS1]] | +0.55 | +0.24 / +0.43 | both halves | 4e-04 |  |
| [[WDR20]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[TOB2]] | +0.54 | +0.29 / +0.58 | both halves | 3e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[RPAP3]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[TBC1D19]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[MOCS2]] | -0.55 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PCNX2]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TTC3P1]] | -0.53 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[DHRS2]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TRNP1]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[VEZT]] | -0.50 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ALKBH8]] | -0.49 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[BRD7]] | -0.49 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[IFTAP]] | -0.49 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKE]] | B | DGKE activity raises MSL1's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.03× lower at baseline in the lines without DGKE | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |
| [[CCDC152]] | B | CCDC152 activity lowers MSL1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 1.07× higher at baseline in the lines without CCDC152 | 0.0997 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.3, 17.4); signed map (3.1, 1.7). **Vector** length 119, 35.8% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +15.6 | +13.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.2 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.5 | +3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -14.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.6 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -4.9 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -27.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -4.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | MSL complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:40,121,971-40,136,917 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hMSL1, MSL-1, DKFZp686P24239 |
| Gene groups (HGNC) | MSL histone acetyltransferase complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DK7](https://www.uniprot.org/uniprotkb/Q68DK7) (Male-specific lethal 1 homolog):

> Non-catalytic component of the MSL histone acetyltransferase complex, a multiprotein complex that mediates the majority of histone H4 acetylation at 'Lys-16' (H4K16ac), an epigenetic mark that prevents chromatin compaction. The MSL complex is required for chromosome stability and genome integrity by maintaining homeostatic levels of H4K16ac. The MSL complex is also involved in gene dosage by promoting up-regulation of genes expressed by the X chromosome (By similarity). X up-regulation is …

**Summary**, from NCBI Gene [339287](https://www.ncbi.nlm.nih.gov/gene/339287):

> Enables protein-macromolecule adaptor activity. Involved in positive regulation of DNA-templated transcription. Located in nuclear speck. Part of MSL complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27905) · Entrez [339287](https://www.ncbi.nlm.nih.gov/gene/339287) · UniProt [Q68DK7](https://www.uniprot.org/uniprotkb/Q68DK7) · Ensembl [ENSG00000188895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188895)

## Data

Gene col 12061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12061); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12061]; `tensor/DDL_lfc|DDL_z.npy` [12061]; `embed/gene_vectors.npy` [12061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12061 or target_col == 12061). Every well: [[MSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
