---
symbol: "LMBRD2"
type: "gene"
col: 8898
ensembl_id: "ENSG00000164187"
name: "LMBR1 domain containing 2"
location: "5p13.2"
module: 215
arm: "+"
pooled_cpm: 33.24
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# LMBRD2

*LMBR1 domain containing 2* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.96× (z +10.2, q 8e-22, up in 27 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +8.5, q 3e-15, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.364× (z -15.9, q 0e+00, down in 42 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.414× (z -13.8, q 5e-41, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG4]] (+0.63, fdr 7e-06), [[SLC30A9]] (+0.61, fdr 1e-05), [[UCHL5]] (+0.60, fdr 1e-05); moves opposite to [[CBLC]] (-0.56, fdr 1e-05), [[RABIF]] (-0.53, fdr 3e-05), [[SNN]] (-0.51, fdr 2e-05).
> It is in [[Module 215]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[POGLUT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +10.2 | 8e-22 | 27/39 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +10.2 | 8e-22 | 31/43 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.5 | 3e-15 | 36/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +5.7 | 2e-06 | 29/48 (HS-578T, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.5 | 4e-06 | 24/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +5.1 | 4e-05 | 23/48 (NCI-H23, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.7 | 2e-04 | 19/40 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +4.4 | 6e-04 | 20/48 (J82, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 7e-04 | 25/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.003 | 16/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +4.0 | 0.004 | 22/48 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.017 | 16/48 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.24×** | +3.4 | 0.031 | 11/48 (SHP-77, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.031 | 11/48 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.23×** | +3.3 | 0.039 | 17/48 (NCI-H23, A498, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.076 | 14/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.081 | 15/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.090 | 10/47 (SNU-423, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.098 | 5/48 (SW480, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.364×** | -15.9 | 0e+00 | 42/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.414×** | -13.8 | 5e-41 | 40/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.451×** | -12.5 | 1e-33 | 40/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.462×** | -12.1 | 1e-31 | 40/48 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -7.6 | 2e-12 | 28/48 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -6.3 | 3e-08 | 33/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.471×** | -6.2 | 5e-08 | 29/41 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.709×** | -5.4 | 5e-06 | 24/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.790×** | -5.2 | 1e-05 | 30/48 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -5.1 | 2e-05 | 27/48 (PANC-1, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -4.7 | 2e-04 | 23/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[EX229 (drug)]] 5 µM |  | **0.572×** | -4.6 | 2e-04 | 23/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.740×** | -4.5 | 3e-04 | 22/47 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.760×** | -4.3 | 7e-04 | 25/47 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.769×** | -4.1 | 0.002 | 24/48 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.648×** | -3.6 | 0.013 | 21/44 (CFPAC-1, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.024 | 14/48 (NCI-H2030, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.2 | 0.033 | 14/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 59.8 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -15.9) |
| [[PANC-1 (line)]] | alt | 33.5 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.204× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -14.1) |
| [[SW480 (line)]] | alt | 51.3 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.224× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 49.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -10.8) |
| [[HCT15 (line)]] | alt | 64.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -9.5) |
| [[Hs 766T (line)]] | wt | 69.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -9.6) |
| [[HT-29 (line)]] | alt | 33.7 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -10.7) |
| [[J82 (line)]] | alt | 40.1 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.326× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.290× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 31.2 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.342× (z -8.9) |
| [[SW 900 (line)]] | alt | 78.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.262× (z -12.2) |
| [[A-172 (line)]] | wt | 46.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -8.5) |
| [[C32 (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -8.7) |
| [[KATO III (line)]] | alt | 37.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.263× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 40.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.360× (z -9.0) |
| [[C-33 A (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -9.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -10.5) ⚠ toxic |
| [[H4 (line)]] | wt | 44.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0714× (z -11.1) |
| [[HS-578T (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -8.5) |
| [[SHP-77 (line)]] | alt | 49.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -10.7) |
| [[SW1417 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.7) | — |
| [[A498 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG4]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SLC30A9]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[UCHL5]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PUS7L]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[BRCC3]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[PRIMPOL]] | +0.55 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[SLC25A46]] | +0.54 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[IRAK4]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[NDUFS1]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[COPS3]] | +0.53 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[ERLIN2]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLC]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[RABIF]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SNN]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[RBM38]] | -0.50 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[CDC34]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SBK1]] | -0.49 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[RPL36AL]] ⚠ | -0.48 | -0.33 / -0.43 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ABHD6]] | -0.48 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[CELF1]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[NOP10]] ⚠ | -0.48 | -0.27 / -0.47 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TNFAIP8L1]] | -0.47 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CARMIL2]] | -0.47 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[VPS37C]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CMTM8]] | -0.46 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POGLUT3]] | B | POGLUT3 activity raises LMBRD2's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without POGLUT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[TOP2A]] | B | TOP2A activity lowers LMBRD2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.7, -25.1); signed map (-5.3, -38.1). **Vector** length 85.6, 20.8% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.0 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.2 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +2.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +1.8 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -6.3 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.8 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -1.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.2 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | LMBR1 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:36,098,407-36,151,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434H2226 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; LMBR family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DH5](https://www.uniprot.org/uniprotkb/Q68DH5) (G protein-coupled receptor-associated protein LMBRD2):

> Recruited to ligand-activated beta-2 adrenergic receptor/ADRB2, it negatively regulates the adrenergic receptor signaling pathway. May also regulate other G protein coupled receptors including type-1 angiotensin II receptor/AGTR1 (Probable).

**Summary**, from NCBI Gene [92255](https://www.ncbi.nlm.nih.gov/gene/92255):

> Involved in adrenergic receptor signaling pathway. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25287) · Entrez [92255](https://www.ncbi.nlm.nih.gov/gene/92255) · UniProt [Q68DH5](https://www.uniprot.org/uniprotkb/Q68DH5) · Ensembl [ENSG00000164187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164187)

## Data

Gene col 8898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8898); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8898]; `tensor/DDL_lfc|DDL_z.npy` [8898]; `embed/gene_vectors.npy` [8898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8898 or target_col == 8898). Every well: [[LMBRD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMBRD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
