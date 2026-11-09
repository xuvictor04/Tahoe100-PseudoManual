---
symbol: "NCOA3"
type: "gene"
col: 4486
ensembl_id: "ENSG00000124151"
name: "nuclear receptor coactivator 3"
location: "20q13.12"
module: 97
arm: "+"
pooled_cpm: 317.41
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# NCOA3

*nuclear receptor coactivator 3* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.20× (z +15.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.466× (z -14.8, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (AsPC-1 0.265×, Hs 766T 0.229×, NCI-H1792 0.311×, CFPAC-1 0.322×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (AsPC-1 0.224×, Panc 03.27 0.285×, Hs 766T 0.233×, BT-474 0.255×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 0.336×, NCI-H1792 0.568×, A-427 0.633×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 0.494×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.401×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP13]] (+0.65, fdr 7e-06), [[KIF13B]] (+0.63, fdr 8e-06), [[TBC1D8]] (+0.61, fdr 1e-05); moves opposite to [[LYPLAL1-AS1]] (-0.50, fdr 6e-05), [[MTMR1]] (-0.49, fdr 6e-05), [[IQCK]] (-0.46, fdr 3e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[AQP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +15.9 | 0e+00 | 44/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +12.4 | 5e-33 | 43/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +12.4 | 6e-33 | 42/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +12.4 | 6e-33 | 47/48 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +9.1 | 7e-18 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +7.8 | 6e-13 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +7.3 | 2e-11 | 44/49 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.8 | 7e-10 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.6 | 2e-09 | 38/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +6.4 | 9e-09 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +5.9 | 2e-07 | 23/48 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 6e-04 | 25/48 (LOX-IMVI, HS-578T, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +3.9 | 0.004 | 26/48 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.21×** | +3.8 | 0.007 | 24/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.008 | 22/48 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.008 | 23/48 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.011 | 25/49 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Econazole (drug)]] 5 µM |  | 1.18× | +3.4 | 0.023 | 20/48 (HS-578T, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4486.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (AsPC-1 0.265×, Hs 766T 0.229×, NCI-H1792 0.311×, CFPAC-1 0.322×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (AsPC-1 0.224×, Panc 03.27 0.285×, Hs 766T 0.233×, BT-474 0.255×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 0.336×, NCI-H1792 0.568×, A-427 0.633×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H1573 0.494×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.401×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -14.8 | 0e+00 | 36/44 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.515×** | -13.4 | 3e-38 | 38/49 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.652×** | -7.5 | 1e-11 | 31/45 (SW1417, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.803×** | -4.4 | 0.001 | 27/48 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -4.3 | 0.002 | 22/49 (A549, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.822×** | -3.9 | 0.008 | 21/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.883× | -3.5 | 0.033 | 14/48 (H4, NCI-H1573, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.890× | -3.3 | 0.061 | 4/48 (NCI-H2347, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 304 | 14 (5 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.58× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 176 | 10 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +12.1) | — |
| [[SW480 (line)]] | alt | 198 | 10 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +19.7) | — |
| [[A498 (line)]] | wt | 215 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +23.4) | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 727 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -17.5) |
| [[SNU-423 (line)]] | alt | 268 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 264 | 5 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.98× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -13.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 270 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 266 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 318 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -15.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 156 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +11.7) | — |
| [[LoVo (line)]] | wt | 132 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 3,023 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 136 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.05× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 166 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 319 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.568× (z -11.3) |
| [[SW 900 (line)]] | alt | 284 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.60× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 481 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -13.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 173 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.48× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.633× (z -8.6) |
| [[A549 (line)]] | wt | 604 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -22.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 646 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -19.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 186 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 124 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 914 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 214 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 255 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -12.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 173 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 447 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 198 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 168 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 353 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.61× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 252 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 427 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -13.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 347 | 1 | 1 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 2.92× (z +13.9) | [[Everolimus (drug)]] 5 µM 0.179× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 358 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -17.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 157 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.89× (z +9.8) | — |
| [[C32 (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.1) | — |
| [[H4 (line)]] | wt | 155 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 173 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 209 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 128 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 269 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.136× (z -9.2) |
| [[AN3 CA (line)]] | alt | 208 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP13]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[KIF13B]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[TBC1D8]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[PACSIN2]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CPM]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[TANC2]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MT1X]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[USP53]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SAA1]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CYTH1]] | +0.56 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[FRY]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CCND3]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLAL1-AS1]] | -0.50 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[MTMR1]] | -0.49 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[IQCK]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MAGOHB]] | -0.46 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MAPKAPK5]] | -0.46 | -0.38 / -0.40 | both halves | 6e-05 | pathway: MAPK family signaling cascades |
| [[RNF169]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[GDNF-AS1]] | -0.44 | -0.31 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | AQP3 activity raises NCOA3's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without AQP3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[S100P]] | B | S100P activity raises NCOA3's level | lines that do not express S100P (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without S100P | 0.027 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |
| [[SLPI]] | B | SLPI activity raises NCOA3's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without SLPI | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[EPAS1]] | B | EPAS1 activity raises NCOA3's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 1.74× lower at baseline in the lines without EPAS1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises NCOA3's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.65× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.065 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity strengthens NCOA3's drug response | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (27) | the lines without SAA2-SAA4, SAA4 respond 0.88× as strongly (z diff +0.61); strongest at Dinaciclib 0.05 µM: 0.80x vs 0.50x (z diff +4.1) | 0.081 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; target measured in part of the lines; artifact flags; co-absent genes |
| [[S100A9]] | B | S100A9 activity raises NCOA3's level | lines that do not express S100A9 (42) vs lines expressing it (8) | 2.51× lower at baseline in the lines without S100A9 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, GSDMC, KRT20 |
| [[SAA1]] | B | SAA1 activity raises NCOA3's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.27× lower at baseline in the lines without SAA1 | 0.0995 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 12.3); signed map (12.1, 33.4). **Vector** length 121, 42.8% of its response variance represented; |z| ≥ 3 in 1,476 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.2 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.1 | +7.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.5 | +1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.5 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +6.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.4 | +3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.3 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.6 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.9 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor coactivator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:47,501,887-47,656,877 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAC3, AIB1, ACTR, p/CIP, TRAM-1, CAGH16, TNRC16, KAT13B |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Lysine acetyltransferases; PAS domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 17 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis; Transcriptional regulation of white adipocyte differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Q9](https://www.uniprot.org/uniprotkb/Q9Y6Q9) (Nuclear receptor coactivator 3):

> Nuclear receptor coactivator that directly binds nuclear receptors and stimulates the transcriptional activities in a hormone-dependent fashion. Plays a central role in creating a multisubunit coactivator complex, which probably acts via remodeling of chromatin. Involved in the coactivation of different nuclear receptors, such as for steroids (GR and ER), retinoids (RARs and RXRs), thyroid hormone (TRs), vitamin D3 (VDR) and prostanoids (PPARs). Displays histone acetyltransferase activity. Also …

**Summary**, from NCBI Gene [8202](https://www.ncbi.nlm.nih.gov/gene/8202):

> The protein encoded by this gene is a nuclear receptor coactivator that interacts with nuclear hormone receptors to enhance their transcriptional activator functions. The encoded protein has histone acetyltransferase activity and recruits p300/CBP-associated factor and CREB binding protein as part of a multisubunit coactivation complex. This protein is initially found in the cytoplasm but is translocated into the nucleus upon phosphorylation. Several transcript variants encoding different …

**Accessions** — [HGNC:7670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7670) · Entrez [8202](https://www.ncbi.nlm.nih.gov/gene/8202) · UniProt [Q9Y6Q9](https://www.uniprot.org/uniprotkb/Q9Y6Q9) · Ensembl [ENSG00000124151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124151)

## Data

Gene col 4486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4486); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4486]; `tensor/DDL_lfc|DDL_z.npy` [4486]; `embed/gene_vectors.npy` [4486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4486 or target_col == 4486). Every well: [[NCOA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
