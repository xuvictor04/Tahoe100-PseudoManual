---
symbol: "NFYA"
type: "gene"
col: 7
ensembl_id: "ENSG00000001167"
name: "nuclear transcription factor Y subunit alpha"
location: "6p21.1"
module: 40
arm: "+"
pooled_cpm: 52.7
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# NFYA

*nuclear transcription factor Y subunit alpha* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.42× (z +14.6, q 1e-45, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.383× (z -11.4, q 2e-27, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.668× (z -4.8, q 2e-04, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH2]] (+0.62, fdr 1e-05), [[ANKRD37]] (+0.59, fdr 3e-05), [[PPP1R2]] (+0.59, fdr 1e-05); moves opposite to [[UBXN4]] (-0.58, fdr 1e-05), [[DPP8]] (-0.58, fdr 3e-05), [[DNAJC11]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTGS1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[SBI-0640756 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.42×** | +14.6 | 1e-45 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +12.9 | 2e-35 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.45×** | +10.6 | 5e-24 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.41×** | +10.5 | 1e-23 | 46/49 (COLO 205, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.22×** | +9.5 | 4e-19 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.63×** | +8.0 | 1e-13 | 45/48 (BT-474, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +7.8 | 7e-13 | 30/48 (COLO 205, A498, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +6.9 | 4e-10 | 30/48 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.70×** | +6.3 | 2e-08 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.54×** | +5.1 | 2e-05 | 31/48 (SW480, COLO 205, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.50×** | +4.8 | 8e-05 | 33/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 5e-04 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.36×** | +3.6 | 0.012 | 26/48 (COLO 205, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.034 | 23/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.053 | 20/49 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.079 | 23/48 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.096 | 19/48 (LS 180, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.383×** | -11.4 | 2e-27 | 40/49 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.382×** | -11.0 | 1e-25 | 33/40 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.542×** | -6.7 | 3e-09 | 31/45 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -4.8 | 2e-04 | 33/48 (A-172, SW 1088, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.6 | 5e-04 | 32/48 (SW 900, H4, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.036 | 26/48 (HT-29, HCT15, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.750×** | -3.4 | 0.044 | 26/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.750×** | -3.4 | 0.044 | 23/48 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.771× | -3.1 | 0.12 | 21/48 (LS 180, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 40.2 | 11 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.30× (z +19.2) | — |
| [[NCI-H460 (line)]] | wt | 27.3 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.0× (z +20.0) | — |
| [[BT-474 (line)]] | alt | 74.2 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.73× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 105 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +17.7) | — |
| [[PANC-1 (line)]] | alt | 45.8 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.27× (z +20.4) | — |
| [[SW1417 (line)]] | alt | 89.7 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -17.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 92.1 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 29.7 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 14.5× (z +19.1) | — |
| [[LS 180 (line)]] | wt | 28.5 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 13.7× (z +17.6) | — |
| [[NCI-H2347 (line)]] | alt | 113 | 3 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.66× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -22.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 59.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.50× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 28.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.00× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -15.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 53.4 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 74.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 55.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 71.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -14.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 63.6 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.5× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -13.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 60.3 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 10.4× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -16.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 45.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 32.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.08× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 44.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 70.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -22.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 41.8 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.64× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 42.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0579× (z -15.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 34.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 52.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -12.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 61.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.42× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 90.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -11.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 57.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 16.0× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 84.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 55.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.84× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 83.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0917× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0595× (z -10.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH2]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 | STRING 406 |
| [[ANKRD37]] | +0.59 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R2]] | +0.59 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ORC4]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZNF710-AS1]] | +0.55 | +0.58 / +0.36 | both halves | 9e-05 |  |
| [[SVBP]] | +0.55 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[POGLUT2]] | +0.55 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[NPTN]] | +0.54 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[RAB8B]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MED26]] | +0.54 | +0.63 / +0.35 | both halves | 1e-04 | pathway: PPARA activates gene expression |
| [[SEMA4B]] | +0.53 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[FBXO33]] | +0.53 | +0.55 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN4]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[DPP8]] | -0.58 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.55 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.54 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[C11orf58]] | -0.52 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[ANKLE2]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[FCF1]] | -0.52 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[DNAJC7]] | -0.52 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[CCAR1]] | -0.52 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[RAB30-DT]] | -0.51 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[NDUFS1]] | -0.51 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[PIGL]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGS1]] | B | PTGS1 activity lowers NFYA's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.15× higher at baseline in the lines without PTGS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[SBI-0640756 (drug)]] 5 µM | C | NFYA's natural level raises the cells' numbers under SBI-0640756 5 µM (protects the cells) | NFYA's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.339 over the table, 0.082 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.358). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.6, -12.6); signed map (-34.1, 17.4). **Vector** length 78.1, 22.2% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.7 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.4 | +1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.3 | -0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.4 | +1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transcription factor Y subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,072,974-41,102,403 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HAP2, CBF-B, NF-YA |
| Gene groups (HGNC) | Nuclear transcription factor Y |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 15 pathways, smallest: ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones; FOXO-mediated transcription of cell death genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P23511](https://www.uniprot.org/uniprotkb/P23511) (Nuclear transcription factor Y subunit alpha):

> Component of the sequence-specific heterotrimeric transcription factor (NF-Y) which specifically recognizes a 5'-CCAAT-3' box motif found in the promoters of its target genes. NF-Y can function as both an activator and a repressor, depending on its interacting cofactors. NF-YA positively regulates the transcription of the core clock component BMAL1.

**Summary**, from NCBI Gene [4800](https://www.ncbi.nlm.nih.gov/gene/4800):

> The protein encoded by this gene is one subunit of a trimeric complex, forming a highly conserved transcription factor that binds to CCAAT motifs in the promoter regions in a variety of genes. Subunit A associates with a tight dimer composed of the B and C subunits, resulting in a trimer that binds to DNA with high specificity and affinity. The sequence specific interactions of the complex are made by the A subunit, suggesting a role as the regulatory subunit. In addition, there is evidence of …

**Accessions** — [HGNC:7804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7804) · Entrez [4800](https://www.ncbi.nlm.nih.gov/gene/4800) · UniProt [P23511](https://www.uniprot.org/uniprotkb/P23511) · Ensembl [ENSG00000001167](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001167)

## Data

Gene col 7: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7]; `tensor/DDL_lfc|DDL_z.npy` [7]; `embed/gene_vectors.npy` [7]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7 or target_col == 7). Every well: [[NFYA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFYA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
