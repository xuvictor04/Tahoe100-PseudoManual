---
symbol: "EMC10"
type: "gene"
col: 8447
ensembl_id: "ENSG00000161671"
name: "ER membrane protein complex subunit 10"
location: "19q13.33"
module: 50
arm: "+"
pooled_cpm: 32.04
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# EMC10

*ER membrane protein complex subunit 10* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.48× (z +25.6, q 0e+00, up in 40 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.33× (z +4.9, q 1e-04, up in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HEC-1-A 5.64×, LoVo 10.4×, NCI-H2030 7.17×, SW480 6.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 10.8×, HEC-1-A 4.45×, NCI-H2030 6.98×, SHP-77 6.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 4.44×, NCI-H2030 6.01×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.693× (z -6.1, q 8e-07, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLE5]] (+0.69, fdr 1e-05), [[GAA]] (+0.61, fdr 1e-05), [[CLSTN1]] (+0.61, fdr 2e-05); moves opposite to [[CCDC137]] (-0.55, fdr 8e-05), [[C14orf119]] (-0.54, fdr 6e-05), [[NIFK]] (-0.53, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8447.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HEC-1-A 5.64×, LoVo 10.4×, NCI-H2030 7.17×, SW480 6.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 10.8×, HEC-1-A 4.45×, NCI-H2030 6.98×, SHP-77 6.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HEC-1-A 4.44×, NCI-H2030 6.01×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.48×** | +25.6 | 0e+00 | 40/42 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.74×** | +25.6 | 0e+00 | 37/38 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.93×** | +16.9 | 0e+00 | 38/39 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.39×** | +5.6 | 3e-06 | 24/44 (SW1417, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.3 | 1e-05 | 27/43 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.9 | 1e-04 | 22/46 (BT-474, LS 180, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.7 | 2e-04 | 19/31 (NCI-H2347, C32, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.1 | 0.003 | 0/46 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.28×** | +4.1 | 0.003 | 21/45 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.0 | 0.004 | 18/46 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.26×** | +3.9 | 0.006 | 17/45 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.25×** | +3.8 | 0.007 | 23/44 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +3.7 | 0.008 | 15/46 (PANC-1, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.21×** | +3.3 | 0.046 | 16/46 (A549, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.693×** | -6.1 | 8e-07 | 26/45 (SW 900, AN3 CA, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.765×** | -4.6 | 0.001 | 23/45 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.801×** | -3.8 | 0.024 | 18/46 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.064 | 17/46 (NCI-H2030, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.877× | -3.2 | 0.15 | 7/46 (Hs 766T, BT-474, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 0.833× | -3.2 | 0.15 | 5/46 (NCI-H23, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.829× | -3.0 | 0.16 | 15/46 (SW 900, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.16 | 15/46 (A-427, hTERT-HPNE, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.828× | -3.0 | 0.16 | 8/46 (SW 1088, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 40.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +14.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 16.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +13.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 76.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +21.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 23.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +13.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 50.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +15.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +19.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 34.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +18.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 23.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 24.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +14.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 51.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.44× (z +15.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 45.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.40× (z +17.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 68.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 31.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +17.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.94× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 34.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +11.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.4× (z +14.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 47.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.97× (z +13.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 59.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 60.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 49.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 30.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.41× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +14.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 32.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 63.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0984× (z -8.6) |
| [[COLO 205 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.40× (z +14.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 37.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.18× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.0) ⚠ cell-cycle shift, explains ~76% of this change |
| [[SNU-423 (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE5]] | +0.69 | +0.52 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[GAA]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[GUSB]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CTSZ]] | +0.55 | +0.40 / +0.46 | both halves | 4e-05 |  |
| [[GSTM2]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[BCAM]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ATP6AP1]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[USF2]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[OLFML2A]] | +0.54 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[SUMF2]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ERGIC3]] | +0.53 | +0.55 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC137]] | -0.55 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[C14orf119]] | -0.54 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[NIFK]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[VPS25]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MRPS31]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[METTL13]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MPLKIP]] | -0.52 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[RDH14]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CHCHD4]] | -0.51 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PALB2]] | -0.51 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[TP53RK]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[NME6]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.9, -21.9); signed map (-28.0, -36.8). **Vector** length 72.4, 14.2% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +25.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +25.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.8 | +5.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.4 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -2.9 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,476,400-50,490,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | INM02, HSS1, HSM1; previously C19orf63 |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5UCC4](https://www.uniprot.org/uniprotkb/Q5UCC4) (ER membrane protein complex subunit 10):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [284361](https://www.ncbi.nlm.nih.gov/gene/284361):

> Contributes to membrane insertase activity. Involved in positive regulation of angiogenesis; positive regulation of endothelial cell proliferation; and protein insertion into ER membrane. Located in endoplasmic reticulum membrane and extracellular region. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27609) · Entrez [284361](https://www.ncbi.nlm.nih.gov/gene/284361) · UniProt [Q5UCC4](https://www.uniprot.org/uniprotkb/Q5UCC4) · Ensembl [ENSG00000161671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161671)

## Data

Gene col 8447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8447); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8447]; `tensor/DDL_lfc|DDL_z.npy` [8447]; `embed/gene_vectors.npy` [8447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8447 or target_col == 8447). Every well: [[EMC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
