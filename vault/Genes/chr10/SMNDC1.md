---
symbol: "SMNDC1"
type: "gene"
col: 4143
ensembl_id: "ENSG00000119953"
name: "survival motor neuron domain containing 1"
location: "10q25.2"
module: 11
arm: "+"
pooled_cpm: 82.88
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SMNDC1

*survival motor neuron domain containing 1* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +13.1, q 1e-36, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.08× (z +10.5, q 3e-23, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Demeclocycline (drug)]] 5 µM: 0.825× (z -3.9, q 0.058, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SNU-1 0.235×, AsPC-1 0.269×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (AsPC-1 0.273×, SNU-1 0.381×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.412×, SNU-1 0.431×; ⚠ cell-cycle shift, would explain all of this change); [[Ponatinib (drug)]] 5 µM in 1 line (SNU-1 0.338×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.495×); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 0.148×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS18B]] (+0.55, fdr 3e-05), [[TIMM17B]] (+0.54, fdr 1e-05, ⚠ TIMM17B in the vector space only through flagged drug-doses), [[ZNF570]] (+0.54, fdr 6e-05), [[RNF7]] (+0.53, fdr 4e-05); moves opposite to [[CCDC61]] (-0.50, fdr 3e-05), [[GLB1L2]] (-0.44, fdr 1e-04), [[ANO7]] (-0.44, fdr 7e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.91×** | +13.1 | 1e-36 | 43/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +10.5 | 3e-23 | 44/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.91×** | +9.3 | 2e-18 | 43/47 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.90×** | +9.2 | 4e-18 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.86×** | +8.4 | 5e-15 | 42/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +8.1 | 4e-14 | 44/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +6.8 | 7e-10 | 40/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +6.3 | 2e-08 | 36/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.3 | 2e-08 | 39/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +6.0 | 1e-07 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.54×** | +5.8 | 3e-07 | 37/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.9 | 4e-05 | 37/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 3e-04 | 33/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.37×** | +4.5 | 3e-04 | 28/49 (A-427, A549, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.008 | 35/48 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.008 | 26/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.010 | 29/48 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.029 | 22/48 (AsPC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.032 | 22/48 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.096 | 19/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.22×** | +2.8 | 0.099 | 21/48 (HEC-1-A, SHP-77, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4143.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SNU-1 0.235×, AsPC-1 0.269×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (AsPC-1 0.273×, SNU-1 0.381×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.412×, SNU-1 0.431×; ⚠ cell-cycle shift, would explain all of this change); [[Ponatinib (drug)]] 5 µM in 1 line (SNU-1 0.338×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.495×); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | **0.825×** | -3.9 | 0.058 | 24/48 (RPMI-7951, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.0 | 10 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.06× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 82.7 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +18.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 389 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.338× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 65.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +18.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +12.6) | — |
| [[A549 (line)]] | wt | 86.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 258 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.495× (z -9.8) |
| [[LoVo (line)]] | wt | 89.6 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.30× (z +9.0) | — |
| [[SW480 (line)]] | alt | 75.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.31× (z +9.9) | — |
| [[A-427 (line)]] | wt | 68.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.13× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[COLO 205 (line)]] | alt | 53.3 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 63.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +9.9) | [[Lonafarnib (drug)]] 5 µM 0.198× (z -9.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 81.0 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 102 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 49.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 83.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.3) | — |
| [[H4 (line)]] | wt | 60.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 42.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 77.0 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 56.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 72.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SNU-423 (line)]] | alt | 81.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +16.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +8.5) | — |
| [[A-172 (line)]] | wt | 81.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 88.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.2) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 52.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 83.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 58.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 53.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H596 (line)]] | alt | 80.8 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.148× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 64.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 64.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 91.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 132 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18B]] | +0.55 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[TIMM17B]] ⚠ | +0.54 | +0.51 / +0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF570]] | +0.54 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[RNF7]] | +0.53 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[THAP5]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[THUMPD1]] | +0.53 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[DBNDD2]] | +0.52 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[ZNF639]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[NME6]] | +0.52 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[PSMG3]] | +0.51 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[HEIH]] | +0.50 | +0.50 / +0.40 | both halves | 4e-05 |  |
| [[PPP1R3D]] | +0.49 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[ZNF286B]] | +0.48 | +0.48 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC61]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GLB1L2]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ANO7]] | -0.44 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[SH3D21]] | -0.43 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[VAMP1]] | -0.42 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[LENG8]] | -0.42 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[RPS18]] | -0.40 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[BCAP31]] | -0.40 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[MAN2B2]] | -0.39 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[POMGNT1]] | -0.39 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[ABHD17A]] | -0.39 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CHID1]] | -0.39 | -0.37 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-47.4, -5.8); signed map (0.8, -22.2). **Vector** length 69.9, 17.5% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.5 | +13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +2.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | -0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.3 | +6.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.9 | +9.2 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -0.5 |
|  | [[Elagolix sodium (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | survival motor neuron domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,290,730-110,304,938 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPF30, SMNR, TDRD16C |
| Gene groups (HGNC) | Tudor domain containing; Spliceosomal A complex |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75940](https://www.uniprot.org/uniprotkb/O75940) (Survival of motor neuron-related-splicing factor 30):

> Involved in spliceosome assembly.

**Summary**, from NCBI Gene [10285](https://www.ncbi.nlm.nih.gov/gene/10285):

> This gene is a paralog of SMN1 gene, which encodes the survival motor neuron protein, mutations in which are cause of autosomal recessive proximal spinal muscular atrophy. The protein encoded by this gene is a nuclear protein that has been identified as a constituent of the spliceosome complex. This gene is differentially expressed, with abundant levels in skeletal muscle, and may share similar cellular function as the SMN1 gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16900) · Entrez [10285](https://www.ncbi.nlm.nih.gov/gene/10285) · UniProt [O75940](https://www.uniprot.org/uniprotkb/O75940) · Ensembl [ENSG00000119953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119953)

## Data

Gene col 4143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4143); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4143]; `tensor/DDL_lfc|DDL_z.npy` [4143]; `embed/gene_vectors.npy` [4143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4143 or target_col == 4143). Every well: [[SMNDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMNDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
