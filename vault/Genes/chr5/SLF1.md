---
symbol: "SLF1"
type: "gene"
col: 5437
ensembl_id: "ENSG00000133302"
name: "SMC5/6 complex localization factor 1"
location: "5q15"
module: 71
arm: "+"
pooled_cpm: 74.65
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# SLF1

*SMC5/6 complex localization factor 1* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.23× (z +17.1, q 0e+00, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.26× (z +5.0, q 3e-05, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.566× (z -12.2, q 3e-31, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP152]] (+0.78, fdr 7e-06), [[BLM]] (+0.78, fdr 7e-06), [[RAD54B]] (+0.78, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.23×** | +17.1 | 0e+00 | 43/47 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.16×** | +16.5 | 0e+00 | 44/47 (A498, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.99×** | +14.8 | 0e+00 | 42/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.63×** | +10.0 | 2e-21 | 35/47 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.58×** | +9.4 | 6e-19 | 33/49 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.31×** | +8.1 | 4e-14 | 29/48 (SNU-423, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +7.9 | 3e-13 | 30/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~90% of this change | **1.31×** | +5.5 | 2e-06 | 23/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.29×** | +5.4 | 5e-06 | 25/47 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.28×** | +5.3 | 8e-06 | 18/47 (NCI-H2347, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.27×** | +5.1 | 2e-05 | 21/47 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 3e-05 | 20/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.9 | 4e-05 | 24/48 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.16× | +4.4 | 4e-04 | 13/47 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.002 | 15/47 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.005 | 16/46 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.026 | 8/47 (RKO, NCI-H23, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.033 | 15/47 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.17× | +3.2 | 0.039 | 9/48 (Panc 03.27, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.1 | 0.047 | 17/47 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.078 | 9/47 (SW48, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.566×** | -12.2 | 3e-31 | 42/47 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.9 | 3e-04 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.797×** | -4.7 | 5e-04 | 16/46 (SW480, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.804×** | -4.7 | 5e-04 | 19/48 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.805×** | -4.5 | 6e-04 | 19/46 (HOP62, SW480, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.813×** | -4.4 | 9e-04 | 22/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.865× | -4.4 | 0.001 | 15/47 (KATO III, Hs 766T, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.810×** | -4.3 | 0.001 | 17/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.815×** | -4.0 | 0.003 | 21/44 (C-33 A, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.832×** | -3.9 | 0.005 | 16/47 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -3.9 | 0.005 | 20/47 (NCI-H460, HOP62, …) | two highest doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.775×** | -3.9 | 0.005 | 14/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.6 | 0.012 | 15/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.846× | -3.6 | 0.014 | 16/47 (NCI-H460, C-33 A, …) | two highest doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.798×** | -3.4 | 0.022 | 13/47 (PANC-1, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.894× | -3.4 | 0.024 | 14/47 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.740×** | -3.4 | 0.026 | 16/46 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.895× | -3.3 | 0.026 | 13/47 (LS 180, RPMI-7951, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.897× | -3.3 | 0.033 | 10/48 (NCI-H460, A-427, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.759×** | -3.1 | 0.057 | 12/47 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.771×** | -2.9 | 0.093 | 10/46 (KATO III, A-427, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.76 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 328 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -21.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.224× (z -15.0) |
| [[A498 (line)]] | wt | 61.1 | 3 (3 ⚠) | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +12.2) ⚠ cell-cycle shift, explains ~62% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.542× (z -10.7) |
| [[C-33 A (line)]] | alt | 376 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0300× (z -41.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -13.7) |
| [[PANC-1 (line)]] | alt | 57.8 | 4 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +12.6) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.456× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 48.3 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 109 | 2 (2 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.1) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -16.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 50.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +10.6) ⚠ cell-cycle shift, explains ~62% of this change | [[Selinexor (drug)]] 5 µM 0.444× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 84.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +9.6) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 5 µM 0.141× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 75.2 | 3 (3 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.5) ⚠ cell-cycle shift, explains ~62% of this change | [[Auranofin (drug)]] 5 µM 0.387× (z -13.7) |
| [[J82 (line)]] | alt | 79.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.14× (z +9.2) ⚠ cell-cycle shift, explains ~95% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 62.0 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.4) ⚠ cell-cycle shift, explains ~62% of this change | [[Auranofin (drug)]] 5 µM 0.459× (z -8.7) |
| [[SHP-77 (line)]] | alt | 319 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.433× (z -10.9) |
| [[LoVo (line)]] | wt | 48.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +12.1) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[SW48 (line)]] | wt | 56.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 45.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +8.6) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0969× (z -15.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[AsPC-1 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +8.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.267× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 60.2 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 45.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.355× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +10.0) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[A-172 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP152]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[BLM]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[RAD54B]] | +0.78 | +0.71 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[WDHD1]] | +0.77 | +0.71 / +0.77 | both halves | 7e-06 | STRING 503 |
| [[FANCM]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 | STRING 495 |
| [[RBL1]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.75 | +0.74 / +0.78 | both halves | 7e-06 | STRING 433 |
| [[NCAPD3]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[DTL]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[MTBP]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLF1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises SLF1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without DSCC1 | 0.094 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.0, -49.3); signed map (-40.7, -41.2). **Vector** length 134, 42.5% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.0 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.9 | +7.9 |
|  | [[NG25 (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.7 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.0 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -7.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.8 | -4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.2 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SMC5/6 complex localization factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:94,618,669-94,739,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761C121, DKFZp564C0469, BRCTx, hNSE5; previously BRCTD1, ANKRD32 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQI6](https://www.uniprot.org/uniprotkb/Q9BQI6) (SMC5-SMC6 complex localization factor protein 1):

> Plays a role in the DNA damage response (DDR) pathway by regulating postreplication repair of UV-damaged DNA and genomic stability maintenance. The SLF1-SLF2 complex acts to link RAD18 with the SMC5-SMC6 complex at replication-coupled interstrand cross-links (ICL) and DNA double-strand breaks (DSBs) sites on chromatin during DNA repair in response to stalled replication forks. Promotes the recruitment of SLF2 and the SMC5-SMC6 complex to DNA lesions.

**Summary**, from NCBI Gene [84250](https://www.ncbi.nlm.nih.gov/gene/84250):

> Enables ubiquitin protein ligase binding activity. Involved in several processes, including positive regulation of cellular component organization; positive regulation of double-strand break repair; and protein localization to site of double-strand break. Located in site of double-strand break. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25408) · Entrez [84250](https://www.ncbi.nlm.nih.gov/gene/84250) · UniProt [Q9BQI6](https://www.uniprot.org/uniprotkb/Q9BQI6) · Ensembl [ENSG00000133302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133302)

## Data

Gene col 5437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5437); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5437]; `tensor/DDL_lfc|DDL_z.npy` [5437]; `embed/gene_vectors.npy` [5437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5437 or target_col == 5437). Every well: [[SLF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
