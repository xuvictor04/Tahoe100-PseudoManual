---
symbol: "DECR1"
type: "gene"
col: 2441
ensembl_id: "ENSG00000104325"
name: "2,4-dienoyl-CoA reductase 1"
location: "8q21.3"
module: 85
arm: "-"
pooled_cpm: 38.69
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 30
n_dd_up_clean: 20
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# DECR1

*2,4-dienoyl-CoA reductase 1* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +11.1, q 6e-26, up in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +8.8, q 3e-16, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.375× (z -15.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASD1]] (+0.72, fdr 1e-05), [[ANXA2R-AS1]] (+0.72, fdr 4e-05), [[IRAK4]] (+0.70, fdr 1e-05); moves opposite to [[SLC27A1]] (-0.76, fdr 1e-05), [[ANKRD27]] (-0.74, fdr 2e-05), [[MAST3]] (-0.71, fdr 3e-05).
> It sits in the **-** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +11.1 | 6e-26 | 40/47 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +9.1 | 2e-17 | 29/38 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.8 | 3e-16 | 35/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.2 | 1e-10 | 39/47 (HT-29, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.9 | 3e-07 | 29/40 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +5.9 | 3e-07 | 29/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.7 | 1e-06 | 32/48 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.5 | 2e-06 | 27/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 1e-04 | 22/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +4.5 | 5e-04 | 26/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 20/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.001 | 17/48 (CFPAC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 21/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.002 | 22/48 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.004 | 19/48 (LOX-IMVI, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.006 | 14/47 (KATO III, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.019 | 17/48 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.019 | 18/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.375×** | -15.1 | 0e+00 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.451×** | -12.3 | 5e-32 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.458×** | -12.0 | 6e-31 | 44/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.619×** | -10.0 | 1e-21 | 32/48 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.534×** | -9.6 | 6e-20 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.537×** | -9.6 | 1e-19 | 34/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -9.0 | 2e-17 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -7.4 | 9e-12 | 34/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -6.7 | 2e-09 | 33/49 (KATO III, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.632×** | -6.6 | 2e-09 | 37/48 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -6.5 | 5e-09 | 28/48 (SW480, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.656×** | -6.5 | 5e-09 | 28/48 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.660×** | -6.4 | 9e-09 | 34/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.657×** | -6.2 | 2e-08 | 30/46 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.474×** | -5.8 | 3e-07 | 32/48 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -5.0 | 2e-05 | 24/48 (COLO 205, SHP-77, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.568×** | -4.4 | 4e-04 | 20/48 (Hs 766T, RPMI-7951, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.757×** | -4.2 | 7e-04 | 23/48 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.3 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -15.1) |
| [[LoVo (line)]] | wt | 50.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -22.8) |
| [[NCI-H460 (line)]] | wt | 44.4 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 45.0 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.48× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.3) |
| [[KATO III (line)]] | alt | 46.0 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.219× (z -14.4) |
| [[LS 180 (line)]] | wt | 84.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -13.9) |
| [[PANC-1 (line)]] | alt | 44.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.381× (z -10.6) |
| [[RKO (line)]] | wt | 102 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -14.2) |
| [[A549 (line)]] | wt | 35.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.6) |
| [[COLO 205 (line)]] | alt | 48.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -14.7) |
| [[H4 (line)]] | wt | 23.6 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 32.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -8.7) |
| [[SHP-77 (line)]] | alt | 54.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.1) |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -10.0) |
| [[A-172 (line)]] | wt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +11.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 78.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 35.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0879× (z -10.9) |
| [[Hs 766T (line)]] | wt | 47.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -9.0) |
| [[SNU-423 (line)]] | alt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.9) |
| [[A498 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASD1]] | +0.72 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ANXA2R-AS1]] | +0.72 | +0.65 / +0.40 | both halves | 4e-05 |  |
| [[IRAK4]] | +0.70 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.69 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PBLD]] | +0.69 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[WAC-AS1]] | +0.69 | +0.64 / +0.31 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | +0.68 | +0.60 / +0.21 | both halves | 7e-04 |  |
| [[HFE]] | +0.67 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[AHI1-DT]] | +0.67 | +0.59 / +0.25 | both halves | 4e-04 |  |
| [[RNF146]] | +0.66 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[RWDD2B]] | +0.66 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[ACADM]] | +0.66 | +0.58 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 755 |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.76 | -0.64 / -0.54 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ANKRD27]] | -0.74 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[MAST3]] | -0.71 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SH2B2]] | -0.69 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[SH3PXD2B]] | -0.67 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SPATA2L]] | -0.67 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RBAK-RBAKDN]] | -0.66 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[PBX4]] | -0.66 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[OGG1]] | -0.66 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.66 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[TMEM120B]] | -0.65 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[CARMIL2]] | -0.65 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DECR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SH3BGRL]] | C | SH3BGRL activity raises DECR1's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without SH3BGRL | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D |
| [[RDX]] | C | RDX activity lowers DECR1's level | lines that do not express RDX (4) vs lines expressing it (46) | 1.99× higher at baseline in the lines without RDX | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SOGA1, CITED2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **-** arm (projection on the module's main direction -0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (3.6, 2.8); signed map (25.7, -20.7). **Vector** length 96.2, 26.7% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +1.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.0 | -12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.0 | -15.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.9 | -12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | 2,4-dienoyl-CoA reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:90,001,405-90,053,633 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR18C1; previously DECR |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: mitochondrial fatty acid beta-oxidation of unsaturated fatty acids; Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16698](https://www.uniprot.org/uniprotkb/Q16698) (2,4-dienoyl-CoA reductase):

> Auxiliary enzyme in the beta-oxidation of mono- and polyunsaturated fatty acids (Probable). Together with the Enoyl-CoA delta isomerase 1 (ECI1) and the Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (ECH1) they allow reentrance of the enoyl-CoA into the beta-oxidation cycle. It participates in the metabolism of unsaturated fatty enoyl-CoA esters having double bonds in both even- and odd-numbered positions in mitochondria. Acts primarily on polyunsaturated fatty acids (Probable). Catalyzes the …

**Summary**, from NCBI Gene [1666](https://www.ncbi.nlm.nih.gov/gene/1666):

> Enables 2,4-dienoyl-CoA reductase (NADPH) activity; NADPH binding activity; and identical protein binding activity. Involved in fatty acid beta-oxidation. Located in mitochondrion. Part of catalytic complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2753) · Entrez [1666](https://www.ncbi.nlm.nih.gov/gene/1666) · UniProt [Q16698](https://www.uniprot.org/uniprotkb/Q16698) · Ensembl [ENSG00000104325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104325)

## Data

Gene col 2441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2441); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2441]; `tensor/DDL_lfc|DDL_z.npy` [2441]; `embed/gene_vectors.npy` [2441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2441 or target_col == 2441). Every well: [[DECR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DECR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
