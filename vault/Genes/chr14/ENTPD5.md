---
symbol: "ENTPD5"
type: "gene"
col: 11885
ensembl_id: "ENSG00000187097"
name: "ectonucleoside triphosphate diphosphohydrolase 5"
location: "14q24.3"
module: 36
arm: "+"
pooled_cpm: 22.9
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ENTPD5

*ectonucleoside triphosphate diphosphohydrolase 5* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.51× (z +5.9, q 2e-06, up in 18 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.35× (z +4.5, q 0.002, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.361× (z -15.2, q 0e+00, down in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.379× (z -14.5, q 1e-45, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTG1]] (+0.64, fdr 1e-05), [[DNAJC16]] (+0.61, fdr 2e-05), [[POFUT1]] (+0.60, fdr 2e-05); moves opposite to [[STX17-DT]] (-0.58, fdr 9e-05), [[SORCS1]] (-0.55, fdr 7e-05), [[FER1L6]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SATB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.9 | 2e-06 | 18/35 (SW 900, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.0 | 1e-04 | 21/42 (HepG2/C3A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +4.5 | 0.002 | 18/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.008 | 18/47 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +3.4 | 0.065 | 15/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.068 | 18/48 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.24×** | +3.2 | 0.100 | 12/47 (NCI-H23, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.361×** | -15.2 | 0e+00 | 41/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.379×** | -14.5 | 1e-45 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.518×** | -13.9 | 8e-42 | 39/47 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.526×** | -9.6 | 9e-20 | 35/47 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.533×** | -9.4 | 6e-19 | 41/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.540×** | -9.2 | 3e-18 | 38/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -9.2 | 3e-18 | 39/47 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.579×** | -8.2 | 2e-14 | 27/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -8.1 | 2e-14 | 32/46 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -8.1 | 4e-14 | 32/46 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -8.0 | 7e-14 | 41/48 (A549, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.586×** | -7.7 | 7e-13 | 30/47 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -7.0 | 2e-10 | 32/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.683×** | -5.4 | 3e-06 | 28/48 (J82, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.721×** | -4.9 | 4e-05 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.779×** | -3.7 | 0.006 | 17/48 (SW48, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.728×** | -3.4 | 0.021 | 10/48 (MIA PaCa-2, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.028 | 13/48 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -3.2 | 0.032 | 14/48 (SNU-1, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.0 | 0.060 | 19/48 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -15.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -9.6) |
| [[SW480 (line)]] | alt | 23.4 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H1573 (line)]] | alt | 24.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -14.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.218× (z -12.3) |
| [[J82 (line)]] | alt | 17.0 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 40.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -9.4) |
| [[PANC-1 (line)]] | alt | 26.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -15.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -11.9) |
| [[A549 (line)]] | wt | 25.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HOP62 (line)]] | alt | 20.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -11.4) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -9.7) |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.237× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 43.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 15.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -9.0) |
| [[A-427 (line)]] | wt | 44.4 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.144× (z -10.2) |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.166× (z -11.2) |
| [[RKO (line)]] | wt | 17.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0527× (z -8.9) |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -10.1) |
| [[SW48 (line)]] | wt | 23.5 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0890× (z -10.5) |
| [[COLO 205 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HCT15 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.241× (z -8.7) |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 15.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -8.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0729× (z -12.2) |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.228× (z -9.2) |
| [[SW1417 (line)]] | alt | 15.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -8.9) |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTG1]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DNAJC16]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[POFUT1]] | +0.60 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[COPG2]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PARN]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MTOR]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[TADA2A]] | +0.55 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CAD]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 | pathway: Metabolism of nucleotides |
| [[WDR5]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NEK4]] | +0.55 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[PACS2]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[GK5]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX17-DT]] | -0.58 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[SORCS1]] | -0.55 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[FER1L6]] | -0.54 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[ESR1]] | -0.54 | -0.32 / -0.42 | both halves | 2e-04 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[NPHS1]] | -0.53 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[LINC00616]] | -0.53 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[GPRC5C]] | -0.53 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[LINC01033]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[LINC02955]] | -0.52 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[LINC01579]] | -0.52 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[DNM3]] | -0.52 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[MIR4300HG]] | -0.52 | -0.28 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SATB1]] | B | SATB1 activity lowers ENTPD5's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.38× higher at baseline in the lines without SATB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[VENTXP1]] | B | VENTXP1 activity lowers ENTPD5's level | lines that do not express VENTXP1 (12) vs lines expressing it (38) | 1.37× higher at baseline in the lines without VENTXP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.418). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.6, -29.7); signed map (-18.7, -53.8). **Vector** length 58.9, 10.1% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.3 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | -1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -7.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleoside triphosphate diphosphohydrolase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,958,010-74,019,399 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NTPDase-5; previously CD39L4, PCPH |
| Gene groups (HGNC) | Ectonucleoside triphosphate diphosphohydrolase family |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 7 pathways, smallest: Phosphate bond hydrolysis by NTPDase proteins; Cell recruitment (pro-inflammatory response); Purinergic signaling in leishmaniasis infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O75356](https://www.uniprot.org/uniprotkb/O75356) (Nucleoside diphosphate phosphatase ENTPD5):

> Hydrolyzes nucleoside diphosphates with a preference for GDP, IDP and UDP compared to ADP and CDP. In the lumen of the endoplasmic reticulum, hydrolyzes UDP that acts as an end-product feedback inhibitor of the UDP-Glc:glycoprotein glucosyltransferases. UMP can be transported back by an UDP-sugar antiporter to the cytosol where it is consumed to regenerate UDP-glucose. Therefore, it positively regulates protein reglucosylation by clearing UDP from the ER lumen and by promoting the regeneration …

**Summary**, from NCBI Gene [957](https://www.ncbi.nlm.nih.gov/gene/957):

> The protein encoded by this gene is similar to E-type nucleotidases (NTPases)/ecto-ATPase/apyrases. NTPases, such as CD39, mediate catabolism of extracellular nucleotides. ENTPD5 contains 4 apyrase-conserved regions which is characteristic of NTPases. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:3367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3367) · Entrez [957](https://www.ncbi.nlm.nih.gov/gene/957) · UniProt [O75356](https://www.uniprot.org/uniprotkb/O75356) · Ensembl [ENSG00000187097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187097)

## Data

Gene col 11885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11885); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11885]; `tensor/DDL_lfc|DDL_z.npy` [11885]; `embed/gene_vectors.npy` [11885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11885 or target_col == 11885). Every well: [[ENTPD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
