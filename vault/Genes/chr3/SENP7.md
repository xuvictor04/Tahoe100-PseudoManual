---
symbol: "SENP7"
type: "gene"
col: 6183
ensembl_id: "ENSG00000138468"
name: "SUMO specific peptidase 7"
location: "3q12.3"
module: 64
arm: "+"
pooled_cpm: 77.55
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# SENP7

*SUMO specific peptidase 7* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.79× (z +6.8, q 6e-09, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 2.32×, A549 1.84×, BT-474 1.83×; ⚠ cell-cycle shift, explains ~13% of this change); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 4.71×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.12×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.524× (z -14.4, q 5e-44, down in 38 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.527× (z -14.2, q 1e-43, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN3]] (+0.53, fdr 1e-05), [[SGCE]] (+0.53, fdr 2e-05), [[INTU]] (+0.53, fdr 6e-05); moves opposite to [[PUS1]] (-0.48, fdr 3e-05), [[MRPS25]] (-0.47, fdr 2e-05), [[LETM1]] (-0.44, fdr 9e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6183.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 2.32×, A549 1.84×, BT-474 1.83×; ⚠ cell-cycle shift, explains ~13% of this change); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 4.71×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.12×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +6.8 | 6e-09 | 28/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.093 | 19/47 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.26 | 11/46 (Hs 766T, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.524×** | -14.4 | 5e-44 | 38/47 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.527×** | -14.2 | 1e-43 | 40/47 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.534×** | -13.4 | 8e-39 | 43/46 (HepG2/C3A, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -11.3 | 3e-27 | 39/44 (NCI-H2347, LS 180, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.592×** | -11.2 | 5e-27 | 32/43 (NCI-H1792, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.606×** | -11.1 | 1e-26 | 34/48 (A-427, RKO, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -9.4 | 5e-19 | 42/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -9.2 | 2e-18 | 39/47 (SW480, HCT15, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.676×** | -8.7 | 2e-16 | 31/47 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -8.4 | 2e-15 | 34/46 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -8.3 | 6e-15 | 37/47 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.695×** | -8.1 | 4e-14 | 39/47 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -6.1 | 5e-08 | 22/47 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.777×** | -5.4 | 3e-06 | 28/49 (NCI-H460, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.630×** | -5.4 | 3e-06 | 28/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.796×** | -5.1 | 1e-05 | 24/47 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.818×** | -4.4 | 3e-04 | 20/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -4.4 | 3e-04 | 26/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.683×** | -4.4 | 3e-04 | 21/47 (NCI-H460, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.692×** | -4.3 | 5e-04 | 23/47 (NCI-H2347, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.704×** | -4.1 | 0.001 | 21/47 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.834× | -4.0 | 0.001 | 21/47 (HCT15, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.836× | -4.0 | 0.002 | 20/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.002 | 19/47 (LOX-IMVI, NCI-H23, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.720×** | -3.8 | 0.003 | 20/47 (SW 900, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.7 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.410× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 94.0 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -11.9) |
| [[A549 (line)]] | wt | 80.8 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.8) ⚠ cell-cycle shift, explains ~13% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -12.4) |
| [[HOP62 (line)]] | alt | 63.1 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 57.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -10.4) |
| [[PANC-1 (line)]] | alt | 107 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.485× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.509× (z -9.8) |
| [[A-172 (line)]] | wt | 90.9 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.385× (z -11.4) |
| [[Hs 766T (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -10.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 55.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 63.7 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.368× (z -12.7) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.5) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.241× (z -9.6) |
| [[BT-474 (line)]] | alt | 68.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.1) ⚠ cell-cycle shift, explains ~13% of this change | [[Auranofin (drug)]] 5 µM 0.350× (z -11.2) |
| [[HS-578T (line)]] | alt | 118 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -14.0) ⚠ cell-cycle shift, explains ~13% of this change |
| [[LOX-IMVI (line)]] | wt | 76.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.352× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 81.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.9) ⚠ cell-cycle shift, explains ~13% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -11.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 74.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 64.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.195× (z -14.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 60.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 82.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 59.3 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.259× (z -12.0) |
| [[A498 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 90.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.1) ⚠ cell-cycle shift, explains ~13% of this change |
| [[H4 (line)]] | wt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 124 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.286× (z -12.1) |
| [[J82 (line)]] | alt | 62.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -11.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.9) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H2030 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.476× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H596 (line)]] | alt | 78.4 | 1 | 0 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 4.71× (z +11.7) | — |
| [[RKO (line)]] | wt | 71.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1088 (line)]] | alt | 93.1 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.05 µM 0.0659× (z -10.3) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -9.1) ⚠ toxic |
| [[SW48 (line)]] | wt | 59.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.281× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN3]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SGCE]] | +0.53 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[INTU]] | +0.53 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[MORN2]] | +0.53 | +0.29 / +0.44 | both halves | 2e-04 |  |
| [[POLK]] | +0.49 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[TMEM67]] | +0.48 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[CEP57]] | +0.48 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[IFT22]] | +0.48 | +0.36 / +0.35 | both halves | 1e-04 |  |
| [[EFHC1]] | +0.48 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[EXOC1]] | +0.47 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[HADHB]] | +0.47 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[ARL6IP5]] | +0.47 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS1]] | -0.48 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[MRPS25]] | -0.47 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[LETM1]] | -0.44 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[NOP16]] | -0.44 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[SLFNL1-AS1]] | -0.43 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SLC7A1]] | -0.42 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[RRP7BP]] | -0.42 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[RRP1]] | -0.41 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[SLC19A1]] | -0.41 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[KCNG1]] | -0.41 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[RAB4A-AS1]] | -0.41 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[DDX21]] | -0.41 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.165). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-26.3, -8.3); signed map (-9.9, -2.0). **Vector** length 99.1, 27.5% of its response variance represented; |z| ≥ 3 in 1,278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.5 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.1 | -13.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SUMO specific peptidase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,324,205-101,513,241 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SUMO specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQF6](https://www.uniprot.org/uniprotkb/Q9BQF6) (Sentrin-specific protease 7):

> Protease that acts as a positive regulator of the cGAS-STING pathway by catalyzing desumoylation of CGAS. Desumoylation of CGAS promotes DNA-binding activity of CGAS, subsequent oligomerization and activation (By similarity). Deconjugates SUMO2 and SUMO3 from targeted proteins, but not SUMO1. Catalyzes the deconjugation of poly-SUMO2 and poly-SUMO3 chains. Has very low efficiency in processing full-length SUMO proteins to their mature forms.

**Summary**, from NCBI Gene [57337](https://www.ncbi.nlm.nih.gov/gene/57337):

> The reversible posttranslational modification of proteins by the addition of small ubiquitin-like SUMO proteins (see SUMO1; MIM 601912) is required for many cellular processes. SUMO-specific proteases, such as SENP7, process SUMO precursors to generate a C-terminal diglycine motif required for the conjugation reaction. They also display isopeptidase activity for deconjugation of SUMO-conjugated substrates (Lima and Reverter, 2008 [PubMed 18799455]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:30402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30402) · Entrez [57337](https://www.ncbi.nlm.nih.gov/gene/57337) · UniProt [Q9BQF6](https://www.uniprot.org/uniprotkb/Q9BQF6) · Ensembl [ENSG00000138468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138468)

## Data

Gene col 6183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6183); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6183]; `tensor/DDL_lfc|DDL_z.npy` [6183]; `embed/gene_vectors.npy` [6183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6183 or target_col == 6183). Every well: [[SENP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SENP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
