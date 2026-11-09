---
symbol: "CCDC126"
type: "gene"
col: 9770
ensembl_id: "ENSG00000169193"
name: "coiled-coil domain containing 126"
location: "7p15.3"
module: 43
arm: "+"
pooled_cpm: 22.65
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 7
n_dd_up_clean: 28
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# CCDC126

*coiled-coil domain containing 126* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.51× (z +24.4, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.908× (z -6.5, q 5e-08, down in 8 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Demeclocycline (drug)]] 5 µM: 0.824× (z -5.2, q 7e-05, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABARAPL2]] (+0.66, fdr 1e-05), [[DSTYK]] (+0.65, fdr 7e-06), [[ARL8A]] (+0.65, fdr 2e-05); moves opposite to [[TRIP13]] (-0.65, fdr 7e-06), [[CBX5]] (-0.60, fdr 2e-05), [[NUP155]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.51×** | +24.4 | 0e+00 | 39/48 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +24.0 | 0e+00 | 45/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.24×** | +22.1 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +19.5 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +19.0 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.54×** | +17.5 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.32×** | +15.8 | 0e+00 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +12.3 | 8e-33 | 37/48 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +11.5 | 6e-29 | 39/48 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +11.3 | 5e-28 | 42/47 (Panc 03.27, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +11.2 | 2e-27 | 40/48 (H4, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +11.2 | 3e-27 | 34/45 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.85×** | +10.9 | 5e-26 | 38/48 (SW480, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +10.8 | 2e-25 | 36/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +10.7 | 3e-25 | 36/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.4 | 2e-19 | 32/47 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.47×** | +8.8 | 3e-17 | 40/48 (PANC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -6.5 | 5e-08 | 8/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **0.824×** | -5.2 | 7e-05 | 23/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.762×** | -4.9 | 2e-04 | 17/35 (NCI-H2030, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.792×** | -4.4 | 0.002 | 20/41 (Panc 03.27, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.781×** | -4.3 | 0.002 | 15/38 (AN3 CA, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Megestrol (drug)]] 0.05 µM |  | **0.807×** | -3.7 | 0.018 | 11/48 (NCI-H2030, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.823×** | -3.7 | 0.020 | 6/48 (Panc 03.27, SNU-423, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.819×** | -3.5 | 0.033 | 9/48 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.878× | -3.5 | 0.033 | 5/48 (Hs 766T, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.7 | 13 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +18.3) | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 7.98 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0968× (z -10.3) |
| [[LoVo (line)]] | wt | 26.5 | 6 | 0 | [[Belinostat (drug)]] 5 µM 4.22× (z +12.2) | — |
| [[A-172 (line)]] | wt | 14.6 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 21.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +19.7) | — |
| [[PANC-1 (line)]] | alt | 25.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 43.6 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 15.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +18.4) | — |
| [[KATO III (line)]] | alt | 36.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 25.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +20.2) | — |
| [[SW1417 (line)]] | alt | 31.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +17.7) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -9.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 20.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +17.2) | — |
| [[BT-474 (line)]] | alt | 14.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 19.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 89.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 16.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 27.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +14.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +15.9) | — |
| [[NCI-H2030 (line)]] | alt | 41.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 25.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 25.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +14.6) | — |
| [[A549 (line)]] | wt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +11.0) | — |
| [[C32 (line)]] | wt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 6.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0707× (z -8.9) |
| [[H4 (line)]] | wt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.5) | — |
| [[J82 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +17.2) | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0562× (z -11.1) |
| [[RKO (line)]] | wt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.6) | — |
| [[A-427 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAPL2]] | +0.66 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[DSTYK]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ARL8A]] | +0.65 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[EIF1B]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[DHRS7]] | +0.63 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[HOTAIRM1]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.62 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[NENF]] | +0.61 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[SNHG6]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[RPS19]] | +0.61 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[RPL36]] | +0.60 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[UQCRB]] ⚠ | +0.60 | +0.45 / +0.63 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NCOA1]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP13]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[CBX5]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[NUP155]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ZNF460]] | -0.59 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[SMU1]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SSU72]] | -0.59 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[LAS1L]] | -0.58 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TARDBP]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.58 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[HNRNPUL1]] | -0.57 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[EMC1]] | -0.57 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[IPO4]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-41.6, -26.4); signed map (-23.0, 5.9). **Vector** length 81.0, 19.4% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +8.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +15.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +12.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +17.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 126 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,597,382-23,644,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23031 |
| Matched by | ensembl_id |

UniProt [Q96EE4](https://www.uniprot.org/uniprotkb/Q96EE4) carries no function annotation.

**Summary**, from NCBI Gene [90693](https://www.ncbi.nlm.nih.gov/gene/90693):

> Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22398) · Entrez [90693](https://www.ncbi.nlm.nih.gov/gene/90693) · UniProt [Q96EE4](https://www.uniprot.org/uniprotkb/Q96EE4) · Ensembl [ENSG00000169193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169193)

## Data

Gene col 9770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9770); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9770]; `tensor/DDL_lfc|DDL_z.npy` [9770]; `embed/gene_vectors.npy` [9770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9770 or target_col == 9770). Every well: [[CCDC126 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC126.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
