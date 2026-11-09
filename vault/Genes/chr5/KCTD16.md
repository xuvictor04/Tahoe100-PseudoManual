---
symbol: "KCTD16"
type: "gene"
col: 11453
ensembl_id: "ENSG00000183775"
name: "potassium channel tetramerization domain containing 16"
location: "5q31.3"
module: 152
arm: "+"
pooled_cpm: 23.16
n_lines_expressing: 32
n_dd_up: 35
n_dd_down: 19
n_dd_up_clean: 27
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 15
direction_downstream: 17
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# KCTD16

*potassium channel tetramerization domain containing 16* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.99× (z +12.6, q 1e-33, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.387× (z -12.3, q 9e-32, down in 28 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP28]] (+0.67, fdr 7e-06), [[RARB]] (+0.65, fdr 7e-06), [[EPHA6]] (+0.63, fdr 1e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[GXYLT2]] → it (grade B ⚠); 17 go from it, the strongest it → [[GXYLT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +12.6 | 1e-33 | 25/30 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +9.8 | 2e-20 | 18/30 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +9.5 | 5e-19 | 22/30 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +8.7 | 5e-16 | 4/20 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +8.4 | 6e-15 | 15/30 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +7.9 | 3e-13 | 15/30 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +6.9 | 3e-10 | 18/30 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +6.6 | 2e-09 | 14/27 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +5.8 | 4e-07 | 14/29 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.7 | 6e-07 | 10/30 (A-172, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +5.7 | 7e-07 | 8/30 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.6 | 1e-06 | 3/23 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.45×** | +4.8 | 6e-05 | 8/30 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.41×** | +4.8 | 7e-05 | 12/30 (A-172, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 2e-04 | 5/30 (SK-MEL-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 2e-04 | 15/29 (SK-MEL-2, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 4e-04 | 8/30 (J82, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +4.3 | 6e-04 | 14/29 (A498, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.001 | 6/29 (SK-MEL-2, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.387×** | -12.3 | 9e-32 | 28/30 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.397×** | -11.9 | 3e-30 | 20/28 (H4, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.430×** | -10.9 | 3e-25 | 27/30 (SHP-77, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.573×** | -10.1 | 5e-22 | 24/29 (NCI-H1792, H4, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.499×** | -9.0 | 3e-17 | 22/29 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.500×** | -8.9 | 4e-17 | 23/27 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.514×** | -8.2 | 1e-14 | 24/25 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.530×** | -7.9 | 2e-13 | 18/29 (NCI-H1792, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.589×** | -6.8 | 5e-10 | 19/30 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.597×** | -6.7 | 2e-09 | 17/28 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.621×** | -6.2 | 4e-08 | 17/29 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.662×** | -5.3 | 5e-06 | 18/29 (PANC-1, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -5.3 | 6e-06 | 20/26 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -5.1 | 1e-05 | 18/28 (NCI-H1792, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.813×** | -3.8 | 0.006 | 4/30 (SW 1271, SHP-77, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -3.6 | 0.011 | 11/28 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.750×** | -3.6 | 0.011 | 8/30 (SW 1088, PANC-1, …) | top dose only |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -3.1 | 0.052 | 3/30 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.850× | -3.0 | 0.084 | 9/30 (NCI-H1573, HS-578T, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 179 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -19.5) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.134× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 344 | 0 | 17 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0406× (z -43.6) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.365× (z -9.7) |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -16.3) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -11.9) |
| [[HS-578T (line)]] | alt | 89.2 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -17.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[CHP-212 (line)]] | wt | 130 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.6) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.1000× (z -9.1) |
| [[HOP62 (line)]] | alt | 48.2 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 3.11× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.1) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.310× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 33.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -11.7) |
| [[PANC-1 (line)]] | alt | 8.84 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -11.0) |
| [[A498 (line)]] | wt | 7.28 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.3× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[NCI-H23 (line)]] | alt | 9.39 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -9.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 23.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.192× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0446× (z -13.1) |
| [[SHP-77 (line)]] | alt | 36.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.183× (z -10.1) |
| [[A-172 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0815× (z -12.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 7.15 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0516× (z -8.8) |
| [[J82 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -12.2) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0922× (z -10.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A-427 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP28]] | +0.67 | +0.59 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[RARB]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[EPHA6]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[PTPRD]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NDNF]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[MIR3171HG]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[EPHA3]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[KCNJ6]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CCNYL2]] | +0.60 | +0.55 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[ADGRB3]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TMEM45A]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[MARCHF1]] | +0.58 | +0.39 / +0.63 | both halves | 5e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | GXYLT2 activity raises KCTD16's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.55× lower at baseline in the lines without GXYLT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[HTRA3]] | B | HTRA3 activity raises KCTD16's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.93× lower at baseline in the lines without HTRA3 | 0.047 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[P2RX7]] | B | P2RX7 activity raises KCTD16's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.14× lower at baseline in the lines without P2RX7 | 0.048 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[LINC02575]] | B | LINC02575 activity strengthens KCTD16's drug response | lines that do not express LINC02575 (20) vs lines expressing it (10) | the lines without LINC02575 respond 0.76× as strongly (z diff +1.37); strongest at Homoharringtonine 5 µM: 0.50x vs 0.22x (z diff +5.1) | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1; target measured in part of the lines; artifact flags |
| [[ZNF883]] | B | ZNF883 activity raises KCTD16's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without ZNF883 | 0.060 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43 |
| [[EPHA3]] | C | EPHA3 activity raises KCTD16's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.49× lower at baseline in the lines without EPHA3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[CCNYL2]], [[CCNYL2-1]] | C | CCNYL2, CCNYL2-1 activity raises KCTD16's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 4.27× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[NREP]] | C | NREP activity raises KCTD16's level | lines that do not express NREP (13) vs lines expressing it (37) | 3.99× lower at baseline in the lines without NREP | 0.028 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises KCTD16's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.95× lower at baseline in the lines without SLC8A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[ZSCAN23]] | C | ZSCAN23 activity raises KCTD16's level | lines that do not express ZSCAN23 (23) vs lines expressing it (27) | 3.68× lower at baseline in the lines without ZSCAN23 | 0.043 | ⚠ within organs, on part of the lines; also absent: TRHDE, SUSD5, EDIL3; co-absent with the target |
| [[LRP2]] | C | LRP2 activity raises KCTD16's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 3.01× lower at baseline in the lines without LRP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[ADGRB3]] | C | ADGRB3 activity raises KCTD16's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.76× lower at baseline in the lines without ADGRB3 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | KCTD16 activity raises GXYLT2's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 3.32× lower at baseline in the lines without KCTD16 | 0.055 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[NIM1K]] | B | KCTD16 activity raises NIM1K's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without KCTD16 | 0.066 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[P2RX7]] | B | KCTD16 activity raises P2RX7's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 2.37× lower at baseline in the lines without KCTD16 | 0.087 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[RORA]] | B | KCTD16 activity raises RORA's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without KCTD16 | 0.090 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[TMEM45A]] | C | KCTD16 activity raises TMEM45A's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 4.99× lower at baseline in the lines without KCTD16 | 0.008 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[NREP]] | C | KCTD16 activity raises NREP's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 4.56× lower at baseline in the lines without KCTD16 | 0.011 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[SLC8A1]] | C | KCTD16 activity raises SLC8A1's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 5.13× lower at baseline in the lines without KCTD16 | 0.011 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[EPHA3]] | C | KCTD16 activity raises EPHA3's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 3.72× lower at baseline in the lines without KCTD16 | 0.022 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[GLIS1]] | C | KCTD16 activity raises GLIS1's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 3.94× lower at baseline in the lines without KCTD16 | 0.022 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[ZSCAN23]] | C | KCTD16 activity raises ZSCAN23's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without KCTD16 | 0.031 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[SMAD9]] | C | KCTD16 activity raises SMAD9's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 3.52× lower at baseline in the lines without KCTD16 | 0.041 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |
| [[SLFN11]] | C | KCTD16 activity raises SLFN11's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 4.80× lower at baseline in the lines without KCTD16 | 0.043 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 27.5); signed map (31.8, 42.6). **Vector** length 81.7, 20.5% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +9.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.3 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -10.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -0.3 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:144,170,873-144,485,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1317 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DU8](https://www.uniprot.org/uniprotkb/Q68DU8) (BTB/POZ domain-containing protein KCTD16):

> Auxiliary subunit of GABA-B receptors that determine the pharmacology and kinetics of the receptor response. Increases agonist potency and markedly alter the G protein signaling of the receptors by accelerating onset and promoting desensitization (By similarity).

**Summary**, from NCBI Gene [57528](https://www.ncbi.nlm.nih.gov/gene/57528):

> Predicted to enable obsolete G protein-coupled neurotransmitter receptor activity involved in regulation of postsynaptic membrane potential and obsolete G protein-coupled neurotransmitter receptor activity involved in regulation of presynaptic membrane potential. Predicted to be involved in regulation of G protein-coupled receptor signaling pathway. Predicted to act upstream of or within behavioral fear response and memory. Predicted to be part of signaling receptor complex. Predicted to be …

**Accessions** — [HGNC:29244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29244) · Entrez [57528](https://www.ncbi.nlm.nih.gov/gene/57528) · UniProt [Q68DU8](https://www.uniprot.org/uniprotkb/Q68DU8) · Ensembl [ENSG00000183775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183775)

## Data

Gene col 11453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11453); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11453]; `tensor/DDL_lfc|DDL_z.npy` [11453]; `embed/gene_vectors.npy` [11453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11453 or target_col == 11453). Every well: [[KCTD16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
