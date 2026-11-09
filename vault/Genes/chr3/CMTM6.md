---
symbol: "CMTM6"
type: "gene"
col: 1660
ensembl_id: "ENSG00000091317"
name: "CKLF like MARVEL transmembrane domain containing 6"
location: "3p22.3"
module: 156
arm: "+"
pooled_cpm: 60.03
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# CMTM6

*CKLF like MARVEL transmembrane domain containing 6* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +19.0, q 0e+00, up in 46 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +10.9, q 1e-25, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.791× (z -3.9, q 0.041, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNG12]] (+0.66, fdr 1e-05), [[CD164]] (+0.61, fdr 1e-05), [[EPB41L2]] (+0.59, fdr 7e-06); moves opposite to [[EPB41L4A-AS1]] (-0.59, fdr 2e-05), [[MPHOSPH10]] (-0.58, fdr 1e-05), [[ECSIT]] (-0.58, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 21 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.03×** | +19.0 | 0e+00 | 46/48 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.51×** | +15.1 | 0e+00 | 39/39 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.37×** | +13.7 | 3e-40 | 39/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.98×** | +11.7 | 2e-29 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +10.9 | 1e-25 | 41/47 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.89×** | +10.9 | 1e-25 | 44/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.53×** | +10.2 | 1e-22 | 33/47 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.82×** | +9.8 | 6e-21 | 38/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.67×** | +8.5 | 2e-15 | 39/46 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.49×** | +6.9 | 4e-10 | 32/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.43×** | +6.2 | 4e-08 | 34/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.42×** | +6.0 | 9e-08 | 33/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.42×** | +6.0 | 1e-07 | 35/47 (NCI-H1792, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +5.1 | 1e-05 | 30/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.32×** | +4.8 | 6e-05 | 27/47 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.3 | 6e-04 | 20/47 (HOP62, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.015 | 21/47 (SW480, HOP62, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.065 | 7/47 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.13× | +2.9 | 0.073 | 6/48 (Panc 03.27, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.080 | 12/46 (AN3 CA, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.26×** | +2.8 | 0.094 | 8/47 (SNU-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.041 | 23/48 (SW1417, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Bergenin (drug)]] 5 µM |  | 0.856× | -3.8 | 0.041 | 14/47 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -3.6 | 0.053 | 23/47 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.823×** | -3.4 | 0.077 | 19/47 (A498, SNU-423, …) | all doses, flat |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.817×** | -3.3 | 0.077 | 15/47 (SW1417, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.873× | -3.3 | 0.077 | 15/47 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.826×** | -3.3 | 0.077 | 19/47 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.829× | -3.1 | 0.13 | 13/47 (hTERT-HPNE, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.9 | 12 (11 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.74× (z +16.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 58.8 | 11 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +18.2) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[A549 (line)]] | wt | 55.0 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +18.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 62.6 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.2) | — |
| [[A-172 (line)]] | wt | 63.3 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 50.1 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 52.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 56.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 93.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +8.5) | — |
| [[C32 (line)]] | wt | 39.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 52.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 43.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 43.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 56.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 65.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 58.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[C-33 A (line)]] | alt | 48.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HCT15 (line)]] | alt | 45.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 57.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[J82 (line)]] | alt | 69.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 50.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 71.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 53.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.5) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[AsPC-1 (line)]] | alt | 65.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +8.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[COLO 205 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 26.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +10.0) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[NCI-H1792 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.144× (z -8.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.187× (z -24.4) |
| [[Panc 03.27 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RKO (line)]] | wt | 90.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.8) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[SHP-77 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.6) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[CD164]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[EPB41L2]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ACTR2]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[DR1]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LEPROT]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MOB1A]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MED14]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ACTR3]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PTBP3]] | +0.54 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[TMEM14C]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MYBL1]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | -0.59 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MPHOSPH10]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ECSIT]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PEX16]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[TMEM208]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TAF1D]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[SNHG7]] | -0.55 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[TM9SF4]] | -0.54 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[ZNF581]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[DDX55]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[BRF2]] | -0.53 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PCGF1]] ⚠ | -0.53 | -0.38 / -0.50 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF761]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction -0.572). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.9, -14.2); signed map (-5.8, 34.7). **Vector** length 86.6, 23.5% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +5.2 | +19.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.0 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.7 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.6 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.5 | +1.5 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | CKLF like MARVEL transmembrane domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:32,481,312-32,502,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20396; previously CKLFSF6 |
| Gene groups (HGNC) | CKLF like MARVEL transmembrane domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX76](https://www.uniprot.org/uniprotkb/Q9NX76) (CKLF-like MARVEL transmembrane domain-containing protein 6):

> Master regulator of recycling and plasma membrane expression of PD-L1/CD274, an immune inhibitory ligand critical for immune tolerance to self and antitumor immunity. Associates with both constitutive and IFNG-induced PD-L1/CD274 at recycling endosomes, where it protects PD-L1/CD274 from being targeted for lysosomal degradation, likely by preventing its STUB1-mediated ubiquitination. May stabilize PD-L1/CD274 expression on antigen presenting cells and potentiates inhibitory signaling by …

**Summary**, from NCBI Gene [54918](https://www.ncbi.nlm.nih.gov/gene/54918):

> This gene belongs to the chemokine-like factor gene superfamily, a novel family that is similar to the chemokine and transmembrane 4 superfamilies. This gene is one of several chemokine-like factor genes located in a cluster on chromosome 3. This gene is widely expressed in many tissues, but the exact function of the encoded protein is unknown. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19177) · Entrez [54918](https://www.ncbi.nlm.nih.gov/gene/54918) · UniProt [Q9NX76](https://www.uniprot.org/uniprotkb/Q9NX76) · Ensembl [ENSG00000091317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091317)

## Data

Gene col 1660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1660); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1660]; `tensor/DDL_lfc|DDL_z.npy` [1660]; `embed/gene_vectors.npy` [1660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1660 or target_col == 1660). Every well: [[CMTM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
