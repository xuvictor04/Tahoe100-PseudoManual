---
symbol: "SBDS"
type: "gene"
col: 4743
ensembl_id: "ENSG00000126524"
name: "SBDS ribosome maturation factor"
location: "7q11.21"
module: 54
arm: "-"
pooled_cpm: 55.59
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SBDS

*SBDS ribosome maturation factor* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.66× (z +17.7, q 0e+00, up in 37 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.94× (z +9.4, q 7e-19, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.663× (z -4.1, q 0.018, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 5 µM in 1 line (SW 1271 0.0770×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBDSP1]] (+0.71, fdr 7e-06), [[FLII]] (+0.67, fdr 1e-05), [[DSG2]] (+0.61, fdr 3e-05); moves opposite to [[MNX1]] (-0.57, fdr 4e-05), [[PTMAP2]] (-0.52, fdr 6e-05, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[MTF2]] (-0.51, fdr 4e-05), [[NR2F6]] (-0.50, fdr 5e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +17.7 | 0e+00 | 37/39 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.45×** | +17.5 | 0e+00 | 47/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.02×** | +14.1 | 4e-43 | 42/47 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +13.3 | 3e-38 | 41/42 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.19×** | +11.1 | 2e-26 | 45/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +9.4 | 7e-19 | 42/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +8.1 | 4e-14 | 42/48 (SW480, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.81×** | +8.1 | 4e-14 | 41/48 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.73×** | +7.8 | 6e-13 | 39/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +7.7 | 8e-13 | 39/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.75×** | +7.6 | 1e-12 | 42/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +7.5 | 4e-12 | 41/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.4 | 5e-09 | 38/47 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +6.4 | 5e-09 | 38/48 (PANC-1, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.56×** | +6.3 | 1e-08 | 36/48 (PANC-1, SW48, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.7 | 3e-07 | 37/48 (PANC-1, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.8 | 5e-05 | 26/49 (HT-29, CFPAC-1, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 2e-04 | 34/48 (HT-29, KATO III, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.001 | 29/47 (HT-29, NCI-H460, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.003 | 25/48 (NCI-H460, NCI-H2030, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.004 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.005 | 24/48 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.007 | 25/47 (NCI-H460, HT-29, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.011 | 20/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.048 | 15/49 (KATO III, SW 900, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.050 | 13/48 (SW480, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4743.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 5 µM in 1 line (SW 1271 0.0770×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.663×** | -4.1 | 0.018 | 29/48 (NCI-H661, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.758×** | -3.9 | 0.018 | 24/48 (LoVo, SW480, …) | two highest doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | **0.822×** | -3.9 | 0.018 | 25/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | 0.791× | -3.3 | 0.14 | 24/48 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.741× | -3.0 | 0.29 | 18/48 (hTERT-HPNE, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.1 | 13 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.19× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 38.2 | 10 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.73× (z +8.8) | — |
| [[SW480 (line)]] | alt | 65.8 | 10 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.06× (z +11.5) | — |
| [[LoVo (line)]] | wt | 60.3 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +14.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 29.6 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +19.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 53.0 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.22× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 54.7 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.3) | — |
| [[A549 (line)]] | wt | 38.5 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.23× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 38.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 108 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 127 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 32.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +13.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 60.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +12.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 84.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.82× (z +9.6) | — |
| [[A-172 (line)]] | wt | 70.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 40.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +14.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 34.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 43.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +10.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 53.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 49.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 56.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +11.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 60.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 77.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 50.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +11.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 50.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 58.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[H4 (line)]] | wt | 37.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 80.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 73.5 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0770× (z -10.2) |
| [[SW1417 (line)]] | alt | 76.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBDSP1]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[FLII]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[DSG2]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[PAK2]] | +0.60 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[NCOA4]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[LIN7C]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[UBE2A]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SLC25A24]] | +0.56 | +0.43 / +0.63 | both halves | 4e-05 |  |
| [[LEPROT]] | +0.56 | +0.37 / +0.63 | both halves | 7e-05 |  |
| [[LPGAT1]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[DSP]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[DYNC1LI2]] | +0.54 | +0.36 / +0.60 | both halves | 9e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MNX1]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PTMAP2]] ⚠ | -0.52 | -0.39 / -0.53 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTF2]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[NR2F6]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[NSUN5P1-1]] | -0.50 | -0.22 / -0.56 | both halves | 6e-04 |  |
| [[IGFBP2]] | -0.49 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[PDXP]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[F12]] | -0.48 | -0.15 / -0.58 | ⚠ one half (not replicated) | 0.001 |  |
| [[RAB20]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[NUDT22]] | -0.48 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[CNOT8]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PPP3R1]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ST3GAL2]] | -0.47 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[LIPE]] | -0.47 | -0.27 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.2, -18.5); signed map (8.9, -9.3). **Vector** length 84.9, 24.5% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +9.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.1 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.5 | +4.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.5 | +1.1 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -4.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.2 | -0.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -0.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +2.5 |

## What is on record

|  |  |
|---|---|
| Name | SBDS ribosome maturation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:66,987,680-66,995,693 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-97, FLJ10917, SDS, SWDS, SDO1 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3A5](https://www.uniprot.org/uniprotkb/Q9Y3A5) (Ribosome maturation protein SBDS):

> Required for the assembly of mature ribosomes and ribosome biogenesis. Together with EFL1, triggers the GTP-dependent release of EIF6 from 60S pre-ribosomes in the cytoplasm, thereby activating ribosomes for translation competence by allowing 80S ribosome assembly and facilitating EIF6 recycling to the nucleus, where it is required for 60S rRNA processing and nuclear export. Required for normal levels of protein synthesis. May play a role in cellular stress resistance. May play a role in …

**Summary**, from NCBI Gene [51119](https://www.ncbi.nlm.nih.gov/gene/51119):

> This gene encodes a highly conserved protein that plays an essential role in ribosome biogenesis. The encoded protein interacts with elongation factor-like GTPase 1 to disassociate eukaryotic initiation factor 6 from the late cytoplasmic pre-60S ribosomal subunit allowing assembly of the 80S subunit. Mutations within this gene are associated with the autosomal recessive disorder Shwachman-Bodian-Diamond syndrome. This gene has a closely linked pseudogene that is distally located. [provided by …

**Accessions** — [HGNC:19440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19440) · Entrez [51119](https://www.ncbi.nlm.nih.gov/gene/51119) · UniProt [Q9Y3A5](https://www.uniprot.org/uniprotkb/Q9Y3A5) · Ensembl [ENSG00000126524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126524)

## Data

Gene col 4743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4743); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4743]; `tensor/DDL_lfc|DDL_z.npy` [4743]; `embed/gene_vectors.npy` [4743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4743 or target_col == 4743). Every well: [[SBDS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBDS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
