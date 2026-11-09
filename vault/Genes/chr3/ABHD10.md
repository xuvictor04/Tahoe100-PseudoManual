---
symbol: "ABHD10"
type: "gene"
col: 6935
ensembl_id: "ENSG00000144827"
name: "abhydrolase domain containing 10, depalmitoylase"
location: "3q13.2"
module: 65
arm: "+"
pooled_cpm: 27.22
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ABHD10

*abhydrolase domain containing 10, depalmitoylase* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.75× (z +10.9, q 8e-25, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.464× (z -15.0, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG4C]] (+0.72, fdr 7e-06), [[HEATR6]] (+0.71, fdr 7e-06), [[PRMT9]] (+0.70, fdr 7e-06); moves opposite to [[AKT1S1]] (-0.66, fdr 1e-05), [[FBXL19-AS1]] (-0.64, fdr 2e-05), [[NPIPB4]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYB5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +10.9 | 8e-25 | 32/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +10.5 | 3e-23 | 38/48 (RPMI-7951, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +9.6 | 1e-19 | 32/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +9.2 | 4e-18 | 28/48 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.9 | 4e-13 | 28/43 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.6 | 2e-12 | 28/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +6.9 | 3e-10 | 29/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.6 | 3e-09 | 24/48 (NCI-H2347, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.59×** | +4.7 | 1e-04 | 15/47 (RPMI-7951, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 6e-04 | 22/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.4 | 6e-04 | 16/48 (A-172, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +4.2 | 0.001 | 17/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.018 | 12/48 (A-427, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | 1.17× | +3.1 | 0.092 | 13/44 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.464×** | -15.0 | 0e+00 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.593×** | -14.4 | 2e-44 | 36/47 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -13.1 | 1e-36 | 36/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.522×** | -12.7 | 2e-34 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -11.2 | 8e-27 | 39/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -11.0 | 3e-26 | 32/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.583×** | -10.5 | 8e-24 | 39/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -8.7 | 2e-16 | 32/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.681×** | -6.9 | 3e-10 | 20/37 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.706×** | -6.8 | 7e-10 | 25/41 (HEC-1-A, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -6.4 | 7e-09 | 27/48 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -6.1 | 6e-08 | 26/48 (NCI-H460, C32, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -5.2 | 7e-06 | 19/34 (Panc 03.27, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.772×** | -4.8 | 6e-05 | 21/47 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.812×** | -4.0 | 0.002 | 18/47 (hTERT-HPNE, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.829×** | -3.6 | 0.009 | 17/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.797×** | -3.2 | 0.051 | 7/48 (NCI-H661, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.894× | -3.0 | 0.065 | 10/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.896× | -3.0 | 0.073 | 12/48 (MIA PaCa-2, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.4 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.153× (z -17.1) |
| [[C32 (line)]] | wt | 23.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.2) |
| [[SW480 (line)]] | alt | 27.3 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.239× (z -16.4) |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -9.6) |
| [[KATO III (line)]] | alt | 36.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 3 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.205× (z -11.9) |
| [[RKO (line)]] | wt | 24.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.6) |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -9.6) |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 33.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 1 | 1 | [[Belinostat (drug)]] 5 µM 3.27× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -11.2) |
| [[A-427 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -12.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.9) |
| [[HCT15 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0620× (z -9.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.340× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -10.2) |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0780× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -14.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.4) |
| [[A-172 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | +0.72 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.71 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.69 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[POMGNT2]] | +0.69 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SDHAF3]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ARL6]] | +0.68 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[POT1]] | +0.67 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ORC4]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[POGLUT2]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[DUSP11]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1S1]] | -0.66 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | -0.64 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[NPIPB4]] | -0.60 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[PEPD]] | -0.60 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[WSB2]] | -0.59 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[DGKH]] | -0.59 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[GGPS1]] | -0.58 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[EFCAB2]] | -0.58 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MAFG]] | -0.58 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.57 | -0.46 / -0.43 | both halves | 4e-05 |  |
| [[ATXN1L]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PHF8]] | -0.56 | -0.37 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYB5A]] | B | CYB5A activity raises ABHD10's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without CYB5A | 0.096 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[HACE1]] | C | HACE1 activity raises ABHD10's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.39× lower at baseline in the lines without HACE1 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.3, -9.5); signed map (-30.0, -11.4). **Vector** length 112, 28.3% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.7 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +10.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.8 | -12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.6 | -15.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -14.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 10, depalmitoylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:111,979,010-111,993,368 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11342 |
| Gene groups (HGNC) | Abhydrolase domain containing; Thioester hydrolases |
| Reactome | 3 pathways, smallest: Glucuronidation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUJ1](https://www.uniprot.org/uniprotkb/Q9NUJ1) (Palmitoyl-protein thioesterase ABHD10, mitochondrial):

> Acts as an acyl-protein thioesterase that hydrolyzes fatty acids from acylated residues in proteins. Regulates the mitochondrial S-depalmitoylation of the nucleophilic active site residue of peroxiredoxin-5/PRDX5, a key antioxidant protein, therefore modulating mitochondrial antioxidant ability. Also catalyzes the deglucuronidation of mycophenolic acid acyl-glucuronide, an active metabolite of the immunosuppressant drug mycophenolate.

**Summary**, from NCBI Gene [55347](https://www.ncbi.nlm.nih.gov/gene/55347):

> This gene encodes a mitochondrially-localized enzyme that acts in liver cells as a hydrolase. The encoded protein removes glucuronide from mycophenolic acid acyl-glucuronide. There is a pseudogene for this gene on chromosome 6. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:25656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25656) · Entrez [55347](https://www.ncbi.nlm.nih.gov/gene/55347) · UniProt [Q9NUJ1](https://www.uniprot.org/uniprotkb/Q9NUJ1) · Ensembl [ENSG00000144827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144827)

## Data

Gene col 6935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6935); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6935]; `tensor/DDL_lfc|DDL_z.npy` [6935]; `embed/gene_vectors.npy` [6935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6935 or target_col == 6935). Every well: [[ABHD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
