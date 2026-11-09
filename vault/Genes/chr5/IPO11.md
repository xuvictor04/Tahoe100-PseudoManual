---
symbol: "IPO11"
type: "gene"
col: 1456
ensembl_id: "ENSG00000086200"
name: "importin 11"
location: "5q12.1"
module: 185
arm: "+"
pooled_cpm: 96.1
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# IPO11

*importin 11* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.67× (z +12.2, q 3e-31, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.597× (z -9.7, q 1e-19, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.736× (z -8.2, q 5e-14, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYW1]] (+0.71, fdr 7e-06), [[CDKAL1]] (+0.71, fdr 7e-06), [[ERI3]] (+0.70, fdr 7e-06); moves opposite to [[TFE3]] (-0.64, fdr 1e-05), [[TP53INP2]] (-0.61, fdr 1e-05), [[IER5]] (-0.56, fdr 1e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDKN2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.67×** | +12.2 | 3e-31 | 45/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.16×** | +10.8 | 1e-24 | 45/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +8.8 | 3e-16 | 43/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +8.6 | 8e-16 | 43/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +7.3 | 3e-11 | 39/47 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +7.1 | 9e-11 | 36/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.3 | 3e-08 | 31/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.1 | 1e-07 | 33/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +6.0 | 1e-07 | 40/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 4e-05 | 31/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 5e-05 | 33/48 (SW480, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.2 | 0.001 | 22/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 0.001 | 23/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.20× | +3.4 | 0.031 | 21/48 (COLO 205, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.034 | 19/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.034 | 19/49 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.597×** | -9.7 | 1e-19 | 41/49 (SW 1271, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -9.6 | 1e-19 | 34/45 (RKO, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.736×** | -8.2 | 5e-14 | 42/48 (SNU-423, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -8.1 | 8e-14 | 34/44 (NCI-H1573, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.710×** | -6.5 | 1e-08 | 35/48 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -5.9 | 5e-07 | 38/49 (SW 1088, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.790×** | -4.5 | 6e-04 | 33/48 (SW48, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.800×** | -4.1 | 0.003 | 24/47 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.024 | 21/47 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.831×** | -3.5 | 0.024 | 19/48 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | 0.846× | -3.2 | 0.078 | 17/48 (SW 1088, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.790× | -3.1 | 0.10 | 20/48 (J82, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.847× | -3.0 | 0.10 | 21/48 (PANC-1, AN3 CA, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 107 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.37× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -10.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 119 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.56× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 104 | 3 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.21× (z +9.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 4.27× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.476× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 63.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 14.2× (z +11.1) | — |
| [[J82 (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 115 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.82× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 102 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.42× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.64× (z +10.6) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.19× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 114 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.37× (z +8.8) | — |
| [[RKO (line)]] | wt | 112 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.77× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -21.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 88.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -17.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 72.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -12.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -13.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 76.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.09× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -13.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 73.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.74× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 60.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -19.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.175× (z -10.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -17.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 85.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.545× (z -9.3) |
| [[SW 1271 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0814× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 90.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 101 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW1]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[CDKAL1]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ERI3]] | +0.70 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[UTP18]] | +0.69 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[DROSHA]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[FARS2]] | +0.67 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[CDC123]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[NOL10]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[XPO4]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 | STRING 657 |
| [[CHCHD6]] | +0.65 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[FTO]] | +0.65 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFE3]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[TP53INP2]] | -0.61 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[IER5]] | -0.56 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CDKN2B]] | -0.56 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[DUSP8]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[C21orf91]] | -0.56 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[HLA-V-1]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | -0.55 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[DLX2]] | -0.55 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[ERF]] | -0.55 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ACHE]] | -0.55 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2B]] | B | CDKN2B activity lowers IPO11's level | lines that do not express CDKN2B (12) vs lines expressing it (38) | 1.26× higher at baseline in the lines without CDKN2B | 0.072 | ⚠ within organs, on part of the lines; deletion recorded too; co-occurs with CDKN2A; also absent: ENSG00000264545, CDKN2A, MTAP |
| [[KLF5]] | B | KLF5 activity lowers IPO11's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.20× higher at baseline in the lines without KLF5 | 0.098 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.6, -31.8); signed map (-15.3, -49.9). **Vector** length 99.7, 31.1% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.1 | +8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.4 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | importin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:62,403,972-62,628,582 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RanBP11 |
| Gene groups (HGNC) | Importins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI26](https://www.uniprot.org/uniprotkb/Q9UI26) (Importin-11):

> Functions in nuclear protein import as nuclear transport receptor. Serves as receptor for nuclear localization signals (NLS) in cargo substrates. Is thought to mediate docking of the importin/substrate complex to the nuclear pore complex (NPC) through binding to nucleoporin and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to the importin, the importin/substrate complex dissociates and …

**Summary**, from NCBI Gene [51194](https://www.ncbi.nlm.nih.gov/gene/51194):

> Importins, including IPO11, are a members of the karyopherin/importin-beta family of transport receptors (see KPNB1; 602738) that mediate nucleocytoplasmic transport of protein and RNA cargoes (Plafker and Macara, 2000 [PubMed 11032817]).[supplied by OMIM, Sep 2008]

**Accessions** — [HGNC:20628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20628) · Entrez [51194](https://www.ncbi.nlm.nih.gov/gene/51194) · UniProt [Q9UI26](https://www.uniprot.org/uniprotkb/Q9UI26) · Ensembl [ENSG00000086200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086200)

## Data

Gene col 1456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1456); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1456]; `tensor/DDL_lfc|DDL_z.npy` [1456]; `embed/gene_vectors.npy` [1456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1456 or target_col == 1456). Every well: [[IPO11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
