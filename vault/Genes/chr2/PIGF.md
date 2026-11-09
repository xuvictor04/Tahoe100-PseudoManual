---
symbol: "PIGF"
type: "gene"
col: 7548
ensembl_id: "ENSG00000151665"
name: "phosphatidylinositol glycan anchor biosynthesis class F"
location: "2p21"
module: 51
arm: "-"
pooled_cpm: 32.08
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# PIGF

*phosphatidylinositol glycan anchor biosynthesis class F* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.46× (z +18.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -29.9, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC5]] (+0.66, fdr 7e-06), [[POM121]] (+0.66, fdr 7e-06), [[SRD5A1]] (+0.65, fdr 1e-05); moves opposite to [[ZNF644]] (-0.72, fdr 7e-06), [[RBM23]] (-0.70, fdr 1e-05), [[REPIN1]] (-0.68, fdr 1e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TRIP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +18.3 | 0e+00 | 46/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +17.8 | 0e+00 | 46/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +16.4 | 0e+00 | 46/48 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +14.3 | 5e-44 | 42/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.4 | 4e-23 | 34/47 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +9.9 | 3e-21 | 40/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 3e-10 | 31/48 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.6 | 3e-09 | 24/48 (A498, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +5.6 | 1e-06 | 28/48 (A498, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +5.5 | 3e-06 | 20/48 (A498, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.21×** | +5.4 | 3e-06 | 20/48 (SNU-423, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.005 | 7/48 (A498, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.014 | 12/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.029 | 9/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.038 | 7/47 (SW480, C32, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.078 | 12/48 (NCI-H1573, A549, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -29.9 | 0e+00 | 46/47 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.394×** | -18.2 | 0e+00 | 44/47 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -16.5 | 0e+00 | 43/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.428×** | -16.4 | 0e+00 | 41/47 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -13.2 | 5e-38 | 33/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.362×** | -10.8 | 3e-25 | 36/48 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -9.9 | 4e-21 | 37/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -9.8 | 8e-21 | 32/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -8.6 | 4e-16 | 31/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.460×** | -8.3 | 8e-15 | 30/47 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -8.1 | 4e-14 | 33/47 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -8.0 | 4e-14 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -4.9 | 5e-05 | 25/48 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.674×** | -4.2 | 0.001 | 20/42 (SW 900, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.829×** | -3.6 | 0.012 | 18/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.896× | -3.2 | 0.057 | 7/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 0.5 µM |  | 0.854× | -3.1 | 0.070 | 6/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.901× | -3.0 | 0.079 | 6/48 (PANC-1, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 51.5 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -23.4) |
| [[SW480 (line)]] | alt | 34.8 | 5 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.75× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -16.0) |
| [[A498 (line)]] | wt | 20.8 | 5 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +17.0) | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.1) |
| [[HOP62 (line)]] | alt | 24.5 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.89× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.3) |
| [[LS 180 (line)]] | wt | 35.2 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.32× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 30.8 | 2 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +15.0) | [[Harringtonine (drug)]] 0.5 µM 0.212× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 28.8 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 3.07× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 64.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -21.2) |
| [[A-172 (line)]] | wt | 29.3 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.6) |
| [[KATO III (line)]] | alt | 43.0 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 99.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.7) |
| [[A-427 (line)]] | wt | 65.3 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.08× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -32.6) |
| [[A549 (line)]] | wt | 49.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -24.4) |
| [[Panc 03.27 (line)]] | alt | 36.2 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -16.6) |
| [[SW1417 (line)]] | alt | 25.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.8) |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0745× (z -17.5) |
| [[HT-29 (line)]] | alt | 20.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.2) |
| [[LoVo (line)]] | wt | 22.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.342× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 3.00× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.9) |
| [[AsPC-1 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.4) |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.6) |
| [[H4 (line)]] | wt | 30.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 34.5 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -14.4) |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.0) |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0709× (z -9.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 21.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.41× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.8) |
| [[RKO (line)]] | wt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.5) |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.2) |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.8) |
| [[SW48 (line)]] | wt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.5) |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC5]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[POM121]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SRD5A1]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MFN1]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[AP1S1]] | +0.64 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[UQCRH]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[HEBP1]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SMARCD2]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[SNHG30]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SHQ1]] | +0.62 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[RNF4]] | +0.62 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | -0.72 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[RBM23]] | -0.70 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[REPIN1]] | -0.68 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[CCDC102A]] | -0.67 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[COQ7]] | -0.66 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.66 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.65 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ZNF776]] | -0.65 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[EPC2]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[USP16]] | -0.65 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.64 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[LARP7]] | -0.64 | -0.57 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity lowers PIGF's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.48× higher at baseline in the lines without TRIP6 | 0.050 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[RBPMS]] | B | RBPMS activity lowers PIGF's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.54× higher at baseline in the lines without RBPMS | 0.052 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[TOP2A]] | B | TOP2A activity lowers PIGF's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.9, 11.0); signed map (-47.3, -4.5). **Vector** length 79.8, 18.5% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.5 | +16.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +10.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +18.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | -0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +5.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.8 | -29.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -16.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | +1.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.5 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,580,937-46,617,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIG-F |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07326](https://www.uniprot.org/uniprotkb/Q07326) (GPI ethanolamine phosphate transferase, stabilizing subunit):

> Stabilizing subunit of the ethanolamine phosphate transferase 3 and ethanolamine phosphate transferase 2 complexes that sequentially transfer an ethanolamine phosphate (EtNP) from a phosphatidylethanolamine (PE) to the 6-OH position of the third alpha-1,2-linked mannose and the second alpha-1,6-linked mannose of a 2-acyl-6-[alpha-D-mannosyl-(1->2)-alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol …

**Summary**, from NCBI Gene [5281](https://www.ncbi.nlm.nih.gov/gene/5281):

> This gene encodes a protein involved in glycosylphosphatidylinositol (GPI)-anchor biosynthesis. The GPI-anchor, a glycolipid containing three mannose molecules in its core backbone, is found on many blood cells where it serves to anchor proteins to the cell surface. The encoded protein and another GPI synthesis protein, PIGO, function in the transfer of ethanolaminephosphate to the third mannose in GPI. Alternatively spliced transcript variants encoding different isoforms have been described. …

**Accessions** — [HGNC:8962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8962) · Entrez [5281](https://www.ncbi.nlm.nih.gov/gene/5281) · UniProt [Q07326](https://www.uniprot.org/uniprotkb/Q07326) · Ensembl [ENSG00000151665](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151665)

## Data

Gene col 7548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7548); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7548]; `tensor/DDL_lfc|DDL_z.npy` [7548]; `embed/gene_vectors.npy` [7548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7548 or target_col == 7548). Every well: [[PIGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
