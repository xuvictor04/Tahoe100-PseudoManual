---
symbol: "MIPEP"
type: "gene"
col: 376
ensembl_id: "ENSG00000027001"
name: "mitochondrial intermediate peptidase"
location: "13q12.12"
module: 18
arm: "+"
pooled_cpm: 37.04
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MIPEP

*mitochondrial intermediate peptidase* — 13q12.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.71× (z +15.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.595× (z -7.6, q 2e-11, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.624× (z -6.7, q 5e-09, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDN1]] (+0.59, fdr 4e-05), [[ULK4]] (+0.58, fdr 2e-05), [[TASP1]] (+0.58, fdr 3e-05); moves opposite to [[ARL4D]] (-0.48, fdr 3e-05), [[GLIPR2]] (-0.47, fdr 2e-04), [[COL26A1]] (-0.46, fdr 0.007, ⚠ one half only (not replicated)), [[KIAA0513]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +15.1 | 0e+00 | 46/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +12.1 | 3e-31 | 44/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +11.0 | 4e-26 | 44/48 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +8.0 | 2e-13 | 39/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.30×** | +5.6 | 3e-06 | 29/48 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.3 | 1e-05 | 29/48 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.38×** | +4.8 | 2e-04 | 26/47 (NCI-H460, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.4 | 9e-04 | 25/48 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 1e-03 | 22/47 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.80×** | +3.9 | 0.004 | 20/48 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.007 | 21/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +3.6 | 0.014 | 15/48 (C32, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.094 | 10/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.098 | 10/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.595×** | -7.6 | 2e-11 | 31/48 (SNU-423, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.624×** | -6.7 | 5e-09 | 29/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -6.4 | 3e-08 | 30/48 (SW48, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.393×** | -6.3 | 5e-08 | 37/48 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.680×** | -5.8 | 6e-07 | 28/48 (KATO III, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.700×** | -5.4 | 6e-06 | 28/47 (LOX-IMVI, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -5.2 | 1e-05 | 27/47 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -4.8 | 1e-04 | 27/48 (SW48, A498, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -3.8 | 0.007 | 23/48 (C32, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~87% of this change | **0.777×** | -3.8 | 0.008 | 22/46 (NCI-H1573, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -3.6 | 0.018 | 21/48 (SW48, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.041 | 16/48 (SW48, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.804×** | -3.3 | 0.041 | 19/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.805×** | -3.3 | 0.041 | 18/48 (SW48, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.618×** | -3.2 | 0.046 | 13/42 (HepG2/C3A, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.635×** | -3.1 | 0.080 | 15/47 (CHP-212, SW1417, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 122 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.155× (z -11.9) |
| [[A498 (line)]] | wt | 37.2 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.312× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 33.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.53× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.179× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 66.1 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.74× (z +12.5) | [[Auranofin (drug)]] 5 µM 0.467× (z -9.4) |
| [[C32 (line)]] | wt | 39.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0898× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 35.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 35.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.59× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 61.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 55.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.122× (z -9.5) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0927× (z -10.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0805× (z -12.1) |
| [[Hs 766T (line)]] | wt | 46.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.41× (z +8.7) | — |
| [[J82 (line)]] | alt | 49.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[KATO III (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -9.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[LoVo (line)]] | wt | 38.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.381× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 49.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 35.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.118× (z -8.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -12.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDN1]] | +0.59 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ULK4]] | +0.58 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[TASP1]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[IPO11]] | +0.57 | +0.27 / +0.62 | both halves | 3e-04 |  |
| [[PUM3]] | +0.56 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TCTN3]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[CAD]] | +0.55 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[ANAPC1]] | +0.54 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[TMEM231]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MRPS25]] | +0.52 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CHCHD3]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[NOL10]] | +0.51 | +0.19 / +0.62 | ⚠ one half (not replicated) | 8e-04 |  |
| [[URB1]] | +0.51 | +0.35 / +0.58 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL4D]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[GLIPR2]] | -0.47 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[COL26A1]] | -0.46 | -0.02 / -0.52 | ⚠ one half (not replicated) | 0.007 |  |
| [[KIAA0513]] | -0.45 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[NRG4]] | -0.45 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[VWA5A]] | -0.44 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[DNAJB2]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[ALOXE3]] | -0.44 | -0.18 / -0.46 | ⚠ not reproduced | 1e-03 |  |
| [[KDM5B]] | -0.43 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[SPTBN4]] | -0.43 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[KSR1]] | -0.43 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[DNAJB4]] | -0.43 | -0.13 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[STYK1]] | -0.42 | -0.24 / -0.46 | both halves | 5e-04 |  |
| [[ZNF222]] | -0.42 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[HES7]] | -0.42 | -0.26 / -0.36 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.8, -34.9); signed map (-14.4, -49.3). **Vector** length 86.0, 20.4% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +8.0 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.0 | +1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.9 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.2 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -9.2 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.0 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.7 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial intermediate peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.12 — chr13:23,730,189-23,889,400 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIP |
| Gene groups (HGNC) | M3 metallopeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99797](https://www.uniprot.org/uniprotkb/Q99797) (Mitochondrial intermediate peptidase):

> Cleaves proteins, imported into the mitochondrion, to their mature size.

**Summary**, from NCBI Gene [4285](https://www.ncbi.nlm.nih.gov/gene/4285):

> The product of this gene performs the final step in processing a specific class of nuclear-encoded proteins targeted to the mitochondrial matrix or inner membrane. This protein is primarily involved in the maturation of oxidative phosphorylation (OXPHOS)-related proteins. This gene may contribute to the functional effects of frataxin deficiency and the clinical manifestations of Friedreich ataxia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7104) · Entrez [4285](https://www.ncbi.nlm.nih.gov/gene/4285) · UniProt [Q99797](https://www.uniprot.org/uniprotkb/Q99797) · Ensembl [ENSG00000027001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000027001)

## Data

Gene col 376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 376); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 376]; `tensor/DDL_lfc|DDL_z.npy` [376]; `embed/gene_vectors.npy` [376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 376 or target_col == 376). Every well: [[MIPEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIPEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
