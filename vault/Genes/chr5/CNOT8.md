---
symbol: "CNOT8"
type: "gene"
col: 7899
ensembl_id: "ENSG00000155508"
name: "CCR4-NOT transcription complex subunit 8"
location: "5q33.2"
module: 164
arm: "+"
pooled_cpm: 105.75
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# CNOT8

*CCR4-NOT transcription complex subunit 8* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.10× (z +5.0, q 3e-04, up in 2 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Dimethyl fumarate (drug)]] 5 µM: 1.36× (z +4.9, q 3e-04, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.330× (z -18.0, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -15.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR45B]] (+0.78, fdr 7e-06), [[MED26]] (+0.77, fdr 7e-06), [[SNAPC3]] (+0.76, fdr 7e-06); moves opposite to [[ZNF655]] (-0.69, fdr 1e-05), [[SFPQ]] (-0.68, fdr 1e-05), [[FKRP]] (-0.67, fdr 7e-06).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GLRX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.0 | 3e-04 | 2/50 (MIA PaCa-2, HOP62) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.36×** | +4.9 | 3e-04 | 36/49 (NCI-H1573, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +4.8 | 3e-04 | 30/49 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.28×** | +4.1 | 0.006 | 21/48 (NCI-H1792, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +3.8 | 0.016 | 25/48 (SW480, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.22×** | +3.3 | 0.099 | 24/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.22× | +3.2 | 0.11 | 24/49 (A549, HS-578T, …) | rises with dose | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.330×** | -18.0 | 0e+00 | 41/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.373×** | -16.3 | 0e+00 | 46/49 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -15.0 | 0e+00 | 47/48 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -11.8 | 7e-30 | 46/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.510×** | -10.5 | 9e-24 | 38/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -9.4 | 5e-19 | 42/48 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.648×** | -7.1 | 1e-10 | 40/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.753×** | -4.8 | 9e-05 | 30/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.753×** | -4.8 | 9e-05 | 27/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -4.1 | 0.002 | 24/48 (A-427, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.799×** | -3.7 | 0.012 | 22/47 (NCI-H1573, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.013 | 26/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.822×** | -3.3 | 0.038 | 20/48 (CFPAC-1, NCI-H2347, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 178 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -24.4) |
| [[CFPAC-1 (line)]] | alt | 159 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.3) |
| [[HepG2_C3A (line)]] | wt | 143 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 152 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.338× (z -16.8) |
| [[A-172 (line)]] | wt | 163 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 158 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.411× (z -15.4) |
| [[J82 (line)]] | alt | 135 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -19.7) |
| [[A-427 (line)]] | wt | 91.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0895× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -12.2) |
| [[A498 (line)]] | wt | 99.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.7) |
| [[HOP62 (line)]] | alt | 144 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0693× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 141 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.5) |
| [[HT-29 (line)]] | alt | 75.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 98.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.386× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 122 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 82.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 88.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -20.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 95.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.5) |
| [[A549 (line)]] | wt | 82.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -14.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 109 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 93.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -15.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 64.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -9.4) |
| [[RKO (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -20.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 83.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.0) |
| [[SW1417 (line)]] | alt | 99.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 79.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.626× (z -9.8) |
| [[AN3 CA (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0666× (z -18.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 93.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 96.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 85.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -12.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 74.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -9.5) |
| [[SNU-1 (line)]] | wt | 81.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -17.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 75.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -17.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR45B]] | +0.78 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[MED26]] | +0.77 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.76 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[KIAA2013]] | +0.74 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[PEX3]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PDXP]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.72 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.72 | +0.83 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.69 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.68 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[FKRP]] | -0.67 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.66 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[TRIM44]] | -0.66 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ST7L]] | -0.65 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[COA7]] | -0.65 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[PIEZO1]] | -0.65 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ARAP2]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ME3]] | -0.65 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SDCBP2-AS1]] | -0.64 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLRX]] | B | GLRX activity raises CNOT8's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without GLRX | 0.069 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[RGS20]] | B | RGS20 activity raises CNOT8's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without RGS20 | 0.085 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.7, -17.1); signed map (-36.4, 21.9). **Vector** length 131, 43.0% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +0.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.4 | +1.1 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.8 | -11.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.6 | -15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.4 | -18.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.1 | -16.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.0 | -7.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -3.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,857,553-154,876,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAF1, hCAF1, CALIF; previously POP2 |
| Gene groups (HGNC) | CCR4-NOT transcription complex |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UFF9](https://www.uniprot.org/uniprotkb/Q9UFF9) (CCR4-NOT transcription complex subunit 8):

> Has 3'-5' poly(A) exoribonuclease activity for synthetic poly(A) RNA substrate. Its function seems to be partially redundant with that of CNOT7. Catalytic component of the CCR4-NOT complex which is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. During miRNA-mediated repression the complex also seems to act as translational repressor during …

**Summary**, from NCBI Gene [9337](https://www.ncbi.nlm.nih.gov/gene/9337):

> Enables poly(A)-specific ribonuclease activity. Involved in miRNA-mediated gene silencing by mRNA destabilization and positive regulation of cell population proliferation. Located in nucleus. Part of CCR4-NOT complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9207) · Entrez [9337](https://www.ncbi.nlm.nih.gov/gene/9337) · UniProt [Q9UFF9](https://www.uniprot.org/uniprotkb/Q9UFF9) · Ensembl [ENSG00000155508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155508)

## Data

Gene col 7899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7899); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7899]; `tensor/DDL_lfc|DDL_z.npy` [7899]; `embed/gene_vectors.npy` [7899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7899 or target_col == 7899). Every well: [[CNOT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
