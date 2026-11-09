---
symbol: "TPCN1"
type: "gene"
col: 11858
ensembl_id: "ENSG00000186815"
name: "two pore segment channel 1"
location: "12q24.13"
module: 106
arm: "+"
pooled_cpm: 73.25
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 40
n_dd_up_clean: 14
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# TPCN1

*two pore segment channel 1* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +12.8, q 1e-34, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.415× (z -20.0, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCD]] (+0.66, fdr 1e-05, ⚠ same locus), [[ESYT2]] (+0.60, fdr 1e-05), [[TBC1D8]] (+0.57, fdr 2e-05), [[STK17B]] (+0.54, fdr 1e-05); moves opposite to [[ZNF518B]] (-0.57, fdr 1e-05), [[TTC7B]] (-0.54, fdr 1e-05), [[FSD1L]] (-0.53, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MLPH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 1 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +12.8 | 1e-34 | 32/49 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.3 | 4e-14 | 27/48 (A-172, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.2 | 1e-10 | 27/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +6.8 | 1e-09 | 27/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.7 | 1e-06 | 22/49 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.7 | 1e-06 | 29/50 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +5.6 | 1e-06 | 24/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.24×** | +5.0 | 5e-05 | 21/48 (A549, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 8e-05 | 21/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +4.8 | 8e-05 | 18/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 2e-04 | 17/48 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 8e-04 | 17/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 8e-04 | 19/50 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 8e-04 | 19/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.20×** | +4.2 | 1e-03 | 20/48 (HOP62, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.415×** | -20.0 | 0e+00 | 44/48 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.471×** | -17.1 | 0e+00 | 45/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.477×** | -16.8 | 0e+00 | 45/48 (SW 900, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.606×** | -16.1 | 0e+00 | 35/47 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -13.3 | 3e-38 | 39/47 (A549, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.563×** | -12.3 | 5e-33 | 35/48 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -12.0 | 2e-31 | 38/47 (A549, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.586×** | -11.7 | 1e-29 | 36/47 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -11.0 | 3e-26 | 37/49 (COLO 205, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -11.0 | 3e-26 | 31/48 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -10.6 | 1e-24 | 34/48 (COLO 205, H4, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -10.0 | 1e-21 | 34/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -9.4 | 2e-19 | 30/48 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.662×** | -9.4 | 3e-19 | 35/48 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -9.1 | 4e-18 | 34/47 (NCI-H1573, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.661×** | -8.4 | 1e-15 | 32/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.782×** | -7.9 | 9e-14 | 29/49 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -7.5 | 2e-12 | 27/48 (RPMI-7951, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 212 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -20.2) |
| [[SW 900 (line)]] | alt | 143 | 0 | 14 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.224× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -22.8) |
| [[PANC-1 (line)]] | alt | 90.2 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -15.6) |
| [[A549 (line)]] | wt | 94.9 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -28.7) |
| [[LoVo (line)]] | wt | 86.0 | 1 | 9 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.260× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 86.1 | 0 | 9 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -13.7) |
| [[H4 (line)]] | wt | 104 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 40.6 | 3 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +20.7) | [[Harringtonine (drug)]] 0.5 µM 0.216× (z -19.3) |
| [[SW480 (line)]] | alt | 48.7 | 4 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +15.5) | [[Harringtonine (drug)]] 5 µM 0.422× (z -11.2) |
| [[SNU-423 (line)]] | alt | 91.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -20.9) |
| [[hTERT-HPNE (line)]] | wt | 82.5 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.176× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 90.6 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.255× (z -11.2) |
| [[HT-29 (line)]] | alt | 95.1 | 0 | 5 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.172× (z -15.6) |
| [[A498 (line)]] | wt | 115 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.244× (z -13.5) |
| [[BT-474 (line)]] | alt | 177 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.312× (z -11.5) |
| [[HOP62 (line)]] | alt | 70.5 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +10.7) | [[Harringtonine (drug)]] 0.5 µM 0.263× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 54.9 | 1 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -18.4) |
| [[KATO III (line)]] | alt | 56.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.348× (z -9.7) |
| [[SHP-77 (line)]] | alt | 84.4 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.411× (z -9.3) |
| [[C32 (line)]] | wt | 43.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.320× (z -9.0) |
| [[HS-578T (line)]] | alt | 53.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 26.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.1) | [[Harringtonine (drug)]] 0.5 µM 0.157× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 54.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.1) | [[Harringtonine (drug)]] 0.5 µM 0.309× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 63.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 67.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.271× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 41.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.5) |
| [[SW1417 (line)]] | alt | 84.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.5) | [[Ixazomib citrate (drug)]] 5 µM 0.418× (z -9.9) |
| [[A-172 (line)]] | wt | 39.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 69.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.245× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 45.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 45.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.4) |
| [[J82 (line)]] | alt | 47.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 94.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.374× (z -10.1) |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0746× (z -8.5) |
| [[RKO (line)]] | wt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.6) | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0848× (z -8.5) |
| [[SW 1271 (line)]] | alt | 93.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -9.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCD]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 | STRING 497; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ESYT2]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[STK17B]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[TOP1]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[REPS2]] | +0.52 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[FUCA1]] | +0.52 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[NCK1-DT]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[RILPL2]] | +0.51 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[NARF]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.50 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[HPS5]] | +0.49 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[SLC19A2]] | +0.49 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518B]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TTC7B]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[FSD1L]] | -0.53 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZNF624]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ATP9B]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 | pathway: Ion channel transport |
| [[ZNF613]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ZNF260]] | -0.50 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[RNF180]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NCF2]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[BBOX1-AS1]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PSMD7]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SHTN1]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLPH]] | B | MLPH activity raises TPCN1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without MLPH | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[EPAS1]] | B | EPAS1 activity raises TPCN1's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without EPAS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[TBC1D8]] | B | TBC1D8 activity raises TPCN1's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.94× lower at baseline in the lines without TBC1D8 | 0.022 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[DHRS3]] | B | DHRS3 activity raises TPCN1's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without DHRS3 | 0.050 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[TOP2A]] | B | TOP2A activity lowers TPCN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EPAS1]] | B | EPAS1 activity strengthens TPCN1's drug response | lines that do not express EPAS1 (9) vs lines expressing it (40) | the lines without EPAS1 respond 0.63× as strongly (z diff +1.64); strongest at Topotecan (hydrochloride) 5 µM: 0.81x vs 0.54x (z diff +3.6) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS; target measured in part of the lines; artifact flags |
| [[REPS2]] | B | REPS2 activity raises TPCN1's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without REPS2 | 0.089 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.448). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.4, 11.1); signed map (12.7, 32.2). **Vector** length 119, 38.5% of its response variance represented; |z| ≥ 3 in 1,854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +12.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.8 | +2.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.8 | +5.0 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +3.8 | +4.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.7 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.2 | -20.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -16.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -17.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.8 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -10.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | two pore segment channel 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,221,050-113,298,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1169, FLJ20612, TPC1 |
| Gene groups (HGNC) | Two pore segment channels; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULQ1](https://www.uniprot.org/uniprotkb/Q9ULQ1) (Two pore channel protein 1):

> Intracellular channel initially characterized as a non-selective Ca(2+)-permeable channel activated by NAADP (nicotinic acid adenine dinucleotide phosphate), it is also a voltage-gated highly-selective Na(+) channel activated directly by PI(3,5)P2 (phosphatidylinositol 3,5-bisphosphate) that senses pH changes and confers electrical excitability to organelles. Localizes to the early and recycling endosomes membranes where it plays a role in the uptake and processing of proteins and regulates …

**Summary**, from NCBI Gene [53373](https://www.ncbi.nlm.nih.gov/gene/53373):

> Voltage-gated Ca(2+) and Na+ channels have 4 homologous domains, each containing 6 transmembrane segments, S1 to S6. TPCN1 is similar to these channels, but it has only 2 domains containing S1 to S6 (Ishibashi et al., 2000 [PubMed 10753632]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18182) · Entrez [53373](https://www.ncbi.nlm.nih.gov/gene/53373) · UniProt [Q9ULQ1](https://www.uniprot.org/uniprotkb/Q9ULQ1) · Ensembl [ENSG00000186815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186815)

## Data

Gene col 11858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11858); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11858]; `tensor/DDL_lfc|DDL_z.npy` [11858]; `embed/gene_vectors.npy` [11858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11858 or target_col == 11858). Every well: [[TPCN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPCN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
