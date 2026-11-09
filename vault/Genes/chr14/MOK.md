---
symbol: "MOK"
type: "gene"
col: 1293
ensembl_id: "ENSG00000080823"
name: "MOK protein kinase"
location: "14q32.31"
module: 205
arm: "+"
pooled_cpm: 39.5
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# MOK

*MOK protein kinase* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.12× (z +23.5, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.605× (z -10.5, q 8e-23, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP69]] (+0.70, fdr 7e-06), [[CCDC157]] (+0.60, fdr 1e-05), [[DRC3]] (+0.60, fdr 2e-05); moves opposite to [[B3GNT2]] (-0.51, fdr 7e-05), [[ITPKA]] (-0.47, fdr 3e-05), [[IL17RA]] (-0.46, fdr 1e-04).
> It is in [[Module 205]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.12×** | +23.5 | 0e+00 | 45/47 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.59×** | +18.7 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +13.9 | 1e-41 | 46/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.61×** | +13.5 | 2e-39 | 40/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.29×** | +12.2 | 6e-32 | 42/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.55×** | +11.6 | 3e-29 | 42/48 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.11×** | +10.9 | 6e-26 | 37/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +10.6 | 3e-24 | 37/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +9.7 | 2e-20 | 32/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.80×** | +7.9 | 2e-13 | 31/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +7.9 | 2e-13 | 30/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +7.6 | 2e-12 | 35/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.60×** | +6.9 | 2e-10 | 25/48 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +6.5 | 3e-09 | 29/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.58×** | +6.2 | 2e-08 | 25/38 (A-427, SNU-423, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.52×** | +6.1 | 3e-08 | 29/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.013 | 18/48 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.024 | 12/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.605×** | -10.5 | 8e-23 | 42/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.625×** | -6.9 | 1e-09 | 33/48 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.027 | 18/48 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.7 | 0.027 | 19/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.771×** | -3.6 | 0.032 | 18/48 (NCI-H23, HT-29, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.791×** | -3.5 | 0.048 | 18/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.048 | 17/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.643×** | -3.4 | 0.048 | 16/46 (SW480, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.798× | -3.2 | 0.10 | 12/48 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.862× | -3.1 | 0.10 | 19/48 (A498, HS-578T, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.802× | -3.1 | 0.11 | 16/48 (PANC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.6 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +18.4) | — |
| [[A-427 (line)]] | wt | 50.7 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW480 (line)]] | alt | 23.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +17.4) | — |
| [[NCI-H1573 (line)]] | alt | 36.0 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.81× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 36.7 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.11× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 31.0 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.38× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 135 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +13.3) | — |
| [[A498 (line)]] | wt | 56.1 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.8) | [[Tucidinostat (drug)]] 0.5 µM 0.230× (z -12.1) |
| [[A549 (line)]] | wt | 34.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +16.4) | — |
| [[LoVo (line)]] | wt | 12.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 182 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -19.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SHP-77 (line)]] | alt | 36.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.77× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 79.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.8) | [[Tucidinostat (drug)]] 5 µM 0.544× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.03× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 41.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 52.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.11× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[RKO (line)]] | wt | 16.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +18.7) | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 40.6 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +9.3) | [[Tucidinostat (drug)]] 5 µM 0.446× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 22.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +17.2) | — |
| [[Panc 03.27 (line)]] | alt | 36.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 29.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +10.8) | — |
| [[A-172 (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.113× (z -9.4) |
| [[HCT15 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +11.4) | — |
| [[KATO III (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -8.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[LS 180 (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 39.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +8.9) | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0736× (z -9.9) |
| [[AN3 CA (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP69]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[CCDC157]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[DRC3]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[RNF213-AS1]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TMEM67]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[IQCK]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD42]] | +0.55 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[DNAL1]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SPATA17]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[IFT81]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[KIF9]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CCDC191]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT2]] | -0.51 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[ITPKA]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[IL17RA]] | -0.46 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[SIAH2]] | -0.44 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[FKBP1B]] | -0.44 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[HMOX2]] | -0.43 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[GRPEL2]] | -0.43 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[TBC1D20]] | -0.43 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[SFN]] | -0.42 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[C8orf76]] | -0.42 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[SLIRP]] | -0.42 | -0.15 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[TPTEP2-CSNK1E]] | -0.42 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[B3GNT5]] | -0.41 | -0.40 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.0, 20.5); signed map (-1.6, 7.4). **Vector** length 111, 30.6% of its response variance represented; |z| ≥ 3 in 1,416 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.1 | +18.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +5.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +5.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.3 | +6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +13.9 |
|  | [[Tofacitinib (drug)]] 0.05 µM |  | +2.2 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.0 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.3 | -10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.2 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | MOK protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.31 — chr14:102,224,500-102,305,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAGE1, STK30; previously RAGE |
| Gene groups (HGNC) | CILK1, MAK, MOK protein kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ07](https://www.uniprot.org/uniprotkb/Q9UQ07) (MAPK/MAK/MRK overlapping kinase):

> Able to phosphorylate several exogenous substrates and to undergo autophosphorylation. Negatively regulates cilium length in a cAMP and mTORC1 signaling-dependent manner.

**Summary**, from NCBI Gene [5891](https://www.ncbi.nlm.nih.gov/gene/5891):

> This gene belongs to the MAP kinase superfamily. The gene was found to be regulated by caudal type transcription factor 2 (Cdx2) protein. The encoded protein, which is localized to epithelial cells in the intestinal crypt, may play a role in growth arrest and differentiation of cells of upper crypt and lower villus regions. Multiple alternatively spliced transcript variants encoding different isoforms have been observed for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:9833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9833) · Entrez [5891](https://www.ncbi.nlm.nih.gov/gene/5891) · UniProt [Q9UQ07](https://www.uniprot.org/uniprotkb/Q9UQ07) · Ensembl [ENSG00000080823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080823)

## Data

Gene col 1293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1293); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1293]; `tensor/DDL_lfc|DDL_z.npy` [1293]; `embed/gene_vectors.npy` [1293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1293 or target_col == 1293). Every well: [[MOK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
