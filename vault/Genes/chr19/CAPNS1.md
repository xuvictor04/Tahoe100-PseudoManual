---
symbol: "CAPNS1"
type: "gene"
col: 4725
ensembl_id: "ENSG00000126247"
name: "calpain small subunit 1"
location: "19q13.12"
module: 111
arm: "+"
pooled_cpm: 74.86
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# CAPNS1

*calpain small subunit 1* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +18.1, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.32× (z +3.4, q 0.081, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.06×, A549 4.26×, A498 3.55×, NCI-H460 3.95×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.13×, A498 3.69×, A549 3.57×, SK-MEL-2 4.76×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.591× (z -8.9, q 3e-16, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.66, fdr 1e-05), [[CDC42]] (+0.66, fdr 7e-06), [[ARPC4]] (+0.64, fdr 1e-05); moves opposite to [[RPL22L1]] (-0.55, fdr 2e-04, ⚠ RPL22L1 in the vector space only through flagged drug-doses), [[CAMLG]] (-0.54, fdr 4e-05), [[MNX1]] (-0.53, fdr 8e-05), [[LAMTOR5]] (-0.53, fdr 1e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAV1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 4.06×, A549 4.26×, A498 3.55×, NCI-H460 3.95×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.13×, A498 3.69×, A549 3.57×, SK-MEL-2 4.76×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +18.1 | 0e+00 | 48/49 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +17.7 | 0e+00 | 42/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +10.3 | 2e-22 | 38/43 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.24×** | +3.6 | 0.044 | 22/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.081 | 18/48 (HT-29, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4725.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.591×** | -8.9 | 3e-16 | 43/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.743×** | -7.1 | 3e-10 | 27/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.660×** | -7.0 | 4e-10 | 37/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.666×** | -6.9 | 9e-10 | 39/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.712×** | -5.8 | 1e-06 | 39/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -5.0 | 6e-05 | 28/48 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.618×** | -4.3 | 0.002 | 33/49 (LOX-IMVI, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.785×** | -3.9 | 0.007 | 22/47 (Panc 03.27, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.789×** | -3.8 | 0.009 | 23/48 (A-172, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.803×** | -3.7 | 0.012 | 25/48 (HOP62, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.805×** | -3.7 | 0.012 | 21/48 (RPMI-7951, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.028 | 24/48 (AsPC-1, SW 1088, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.029 | 19/47 (SW 900, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.693×** | -3.3 | 0.047 | 21/49 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.695×** | -3.2 | 0.047 | 21/45 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 104 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.460× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 94.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.380× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 54.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.330× (z -10.0) |
| [[A-427 (line)]] | wt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.69× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 70.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +15.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +18.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 61.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +11.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 57.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 103 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.465× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 93.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 58.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.8) |
| [[PANC-1 (line)]] | alt | 99.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +18.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 47.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.9) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 5 µM 0.152× (z -8.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 76.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +14.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 49.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 63.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 86.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +13.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 78.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 62.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +12.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 83.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +10.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 73.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 67.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 71.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 55.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +15.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 60.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 66.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +15.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 77.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 56.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.8) |
| [[SW 900 (line)]] | alt | 51.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.1) |
| [[HCT15 (line)]] | alt | 85.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +9.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 76.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0649× (z -9.4) ⚠ cell-cycle shift, explains ~2% of this change |
| [[AN3 CA (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CDC42]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ARPC4]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[YWHAZ]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 | STRING 418 |
| [[ACTR3]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CAV2]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RNF167]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TSPAN31]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[MYO1C]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[CLIC1]] | +0.56 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[DR1]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DBNL]] | +0.56 | +0.47 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 13 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL22L1]] ⚠ | -0.55 | -0.32 / -0.61 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.54 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[MNX1]] | -0.53 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[LAMTOR5]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[RPL18]] ⚠ | -0.53 | -0.45 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | -0.52 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NACA4P]] ⚠ | -0.52 | -0.48 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TOMM5]] | -0.52 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[RPL17]] | -0.51 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[MRPL34]] | -0.51 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[RBIS]] | -0.51 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[ATP5MC2]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[NR2F6]] | -0.51 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[LSM2]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[TOMM7]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV1]] | B | CAV1 activity raises CAPNS1's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without CAV1 | 0.070 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -18.7); signed map (-8.6, 34.3). **Vector** length 87.9, 22.9% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Platelet activation, signaling and aggregation* (reactome, mean cos +0.51 to 11); *RHO GTPase Effectors* (reactome, mean cos +0.53 to 10); *EPHB-mediated forward signaling* (reactome, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +17.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.3 | +0.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +1.5 |
| fall | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -3.4 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.9 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.7 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.9 | +0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | calpain small subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,139,953-36,150,353 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CANP, CANPS, 30K, CDPS; previously CAPN4 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 13 pathways, smallest: Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases; Defective Intrinsic Pathway for Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P04632](https://www.uniprot.org/uniprotkb/P04632) (Calpain small subunit 1):

> Regulatory subunit of the calcium-regulated non-lysosomal thiol-protease which catalyzes limited proteolysis of substrates involved in cytoskeletal remodeling and signal transduction. Essential for embryonic development (By similarity).

**Summary**, from NCBI Gene [826](https://www.ncbi.nlm.nih.gov/gene/826):

> This gene is a member of the calpain small subunit family. Calpains are calcium-dependent cysteine proteinases that are widely distributed in mammalian cells. Calpains operate as heterodimers, comprising a specific large catalytic subunit (calpain 1 subunit in Calpain I, and calpain 2 subunit in Calpain II), and a common small regulatory subunit encoded by this gene. This encoded protein is essential for the stability and function of both calpain heterodimers, whose proteolytic activities …

**Accessions** — [HGNC:1481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1481) · Entrez [826](https://www.ncbi.nlm.nih.gov/gene/826) · UniProt [P04632](https://www.uniprot.org/uniprotkb/P04632) · Ensembl [ENSG00000126247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126247)

## Data

Gene col 4725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4725); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4725]; `tensor/DDL_lfc|DDL_z.npy` [4725]; `embed/gene_vectors.npy` [4725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4725 or target_col == 4725). Every well: [[CAPNS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAPNS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
