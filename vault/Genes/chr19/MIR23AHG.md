---
symbol: "MIR23AHG"
type: "gene"
col: 15556
ensembl_id: "ENSG00000267519"
name: "miR-23a/27a/24-2 cluster host gene"
location: "19p13.12"
module: 109
arm: "+"
pooled_cpm: 37.47
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# MIR23AHG

*miR-23a/27a/24-2 cluster host gene* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.44× (z +5.4, q 4e-05, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.340× (z -15.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HES1]] (+0.67, fdr 7e-06), [[NR4A1]] (+0.64, fdr 7e-06), [[NRARP]] (+0.64, fdr 2e-05); moves opposite to [[MRPL13]] (-0.54, fdr 5e-05), [[CUL2]] (-0.52, fdr 4e-05), [[ACTL6A]] (-0.50, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +5.4 | 4e-05 | 24/47 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.65×** | +5.2 | 5e-05 | 34/48 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 0.001 | 29/48 (SNU-423, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.016 | 25/48 (SNU-423, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +3.4 | 0.084 | 22/48 (SHP-77, SNU-423, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.55× | +3.2 | 0.11 | 19/48 (HOP62, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 1.34× | +3.0 | 0.17 | 17/48 (NCI-H460, SW 900, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.17 | 14/48 (A549, SW1417, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.340×** | -15.9 | 0e+00 | 46/48 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.289×** | -13.0 | 6e-36 | 42/48 (SW1417, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.298×** | -12.6 | 2e-34 | 42/48 (SW1417, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.384×** | -9.6 | 1e-19 | 42/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.404×** | -9.5 | 4e-19 | 41/48 (NCI-H23, SW1417, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.430×** | -8.5 | 2e-15 | 39/48 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.516×** | -6.6 | 3e-09 | 26/35 (Hs 766T, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.560×** | -6.1 | 1e-07 | 33/45 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.418×** | -4.8 | 1e-04 | 33/48 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.653×** | -4.4 | 5e-04 | 26/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.634×** | -4.4 | 5e-04 | 24/40 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.458×** | -4.3 | 1e-03 | 31/47 (SNU-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.681×** | -4.0 | 0.003 | 30/48 (SNU-423, SW48, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.694×** | -3.8 | 0.005 | 27/48 (MIA PaCa-2, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.702×** | -3.7 | 0.008 | 22/48 (A-427, AsPC-1, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.783×** | -3.6 | 0.011 | 28/48 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.014 | 24/47 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.717×** | -3.5 | 0.016 | 20/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.714×** | -3.4 | 0.021 | 19/47 (SNU-423, SW 900, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.5 µM |  | **0.735×** | -3.2 | 0.037 | 20/48 (SNU-423, PANC-1, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[vincristine (drug)]] 0.05 µM |  | **0.728×** | -3.1 | 0.047 | 21/48 (MIA PaCa-2, SNU-423, …) | all doses, flat | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.047 | 21/48 (HOP62, SW480, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -2.9 | 0.081 | 19/48 (HOP62, hTERT-HPNE, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.700×** | -2.9 | 0.092 | 18/48 (SNU-423, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.753×** | -2.9 | 0.092 | 19/48 (SW480, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.63 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 60.4 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0462× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.4) |
| [[HT-29 (line)]] | alt | 56.5 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 32.9 | 0 | 6 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0622× (z -18.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 83.0 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -13.2) |
| [[SW1417 (line)]] | alt | 36.1 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 51.2 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.162× (z -12.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -9.8) |
| [[SW480 (line)]] | alt | 48.4 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -11.6) |
| [[HOP62 (line)]] | alt | 56.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.4) |
| [[HS-578T (line)]] | alt | 49.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 67.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 46.4 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.302× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -8.7) |
| [[SNU-423 (line)]] | alt | 57.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -14.5) |
| [[A-172 (line)]] | wt | 41.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -10.2) |
| [[A498 (line)]] | wt | 44.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -8.5) |
| [[KATO III (line)]] | alt | 27.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0592× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 27.9 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.24× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 29.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 53.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.1) |
| [[A549 (line)]] | wt | 35.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 33.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.7) |
| [[J82 (line)]] | alt | 25.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.0) |
| [[LoVo (line)]] | wt | 24.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -12.0) |
| [[LS 180 (line)]] | wt | 36.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.1) |
| [[SW 900 (line)]] | alt | 43.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -9.3) |
| [[SW48 (line)]] | wt | 50.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -10.3) |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -8.6) |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -10.7) |
| [[HCT15 (line)]] | alt | 37.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0916× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NR4A1]] | +0.64 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[NRARP]] | +0.64 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[FOSB]] | +0.62 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[FOS]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ADGRE5]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LMNA]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NR4A2]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[IER3]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SEMA4A]] | +0.57 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[NR4A3]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TENT5C]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL13]] | -0.54 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[CUL2]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ACTL6A]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SNRNP40]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[RPE]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ALG5]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[ZW10]] | -0.48 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[VPS37A]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[MIGA1]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NEDD1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[RNF4]] | -0.47 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TXNDC9]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIR23AHG's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IER3]] | B | IER3 activity raises MIR23AHG's level | lines that do not express IER3 (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without IER3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[NR4A2]] | B | NR4A2 activity raises MIR23AHG's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without NR4A2 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SEMA4A]] | B | SEMA4A activity raises MIR23AHG's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without SEMA4A | 0.060 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[GATA6]] | B | GATA6 activity raises MIR23AHG's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without GATA6 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | MIR23AHG's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | MIR23AHG's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.090 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, -0.8); signed map (6.1, 27.4). **Vector** length 116, 34.8% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.52 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | +3.4 | +5.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.4 | -9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.0 | -8.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.9 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -15.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.9 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -3.9 | -2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.8 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | miR-23a/27a/24-2 cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19p13.12 — chr19:13,823,880-13,842,928 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC284454, Smyca |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [284454](https://www.ncbi.nlm.nih.gov/gene/284454):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27620) · Entrez [284454](https://www.ncbi.nlm.nih.gov/gene/284454) · Ensembl [ENSG00000267519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267519)

## Data

Gene col 15556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15556); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15556]; `tensor/DDL_lfc|DDL_z.npy` [15556]; `embed/gene_vectors.npy` [15556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15556 or target_col == 15556). Every well: [[MIR23AHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR23AHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
