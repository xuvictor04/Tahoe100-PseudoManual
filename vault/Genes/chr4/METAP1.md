---
symbol: "METAP1"
type: "gene"
col: 8836
ensembl_id: "ENSG00000164024"
name: "methionyl aminopeptidase 1"
location: "4q23"
module: 188
arm: "+"
pooled_cpm: 67.33
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# METAP1

*methionyl aminopeptidase 1* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.76× (z +10.6, q 1e-23, up in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +6.9, q 9e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.504× (z -19.2, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALS2]] (+0.78, fdr 7e-06), [[FAR1]] (+0.75, fdr 7e-06), [[C20orf27]] (+0.73, fdr 2e-05); moves opposite to [[RBM23]] (-0.79, fdr 7e-06), [[ZNF764]] (-0.77, fdr 1e-05), [[LINC00571]] (-0.72, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +10.6 | 1e-23 | 41/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +7.7 | 5e-12 | 29/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.42×** | +7.0 | 4e-10 | 35/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +6.9 | 9e-10 | 32/48 (A-172, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.38×** | +6.4 | 1e-08 | 31/47 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +5.8 | 6e-07 | 29/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +5.5 | 3e-06 | 28/48 (HT-29, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.2 | 2e-05 | 29/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +5.0 | 3e-05 | 26/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.26×** | +4.5 | 3e-04 | 22/48 (HT-29, A-172, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.011 | 20/48 (A498, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.20×** | +3.7 | 0.011 | 18/48 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.011 | 14/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.19× | +3.5 | 0.021 | 20/48 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | 1.19× | +3.5 | 0.021 | 19/47 (HepG2/C3A, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Tadalafil (drug)]] 5 µM |  | 1.19× | +3.3 | 0.030 | 19/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.053 | 14/48 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.076 | 12/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +3.0 | 0.076 | 13/48 (PANC-1, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +2.9 | 0.088 | 8/49 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.088 | 16/47 (LS 180, NCI-H23, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.098 | 10/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.504×** | -19.2 | 0e+00 | 44/48 (AN3 CA, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -8.0 | 4e-13 | 34/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -6.7 | 3e-09 | 30/48 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -6.4 | 2e-08 | 31/48 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.829×** | -3.7 | 0.020 | 21/48 (RKO, SW48, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.873× | -3.7 | 0.020 | 15/48 (CHP-212, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.822×** | -3.4 | 0.064 | 15/50 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.854× | -3.1 | 0.12 | 11/47 (J82, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 145 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -21.1) |
| [[A-172 (line)]] | wt | 45.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.8) |
| [[PANC-1 (line)]] | alt | 57.8 | 2 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.18× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -10.1) |
| [[A-427 (line)]] | wt | 95.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -11.9) |
| [[AN3 CA (line)]] | alt | 86.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.2) |
| [[H4 (line)]] | wt | 68.9 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.24× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.0) |
| [[LoVo (line)]] | wt | 65.8 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.44× (z +10.0) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -12.2) |
| [[LS 180 (line)]] | wt | 106 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.1) ⚠ cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.625× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 70.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 63.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.2) |
| [[NCI-H460 (line)]] | wt | 60.9 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.52× (z +9.7) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -10.4) |
| [[SNU-1 (line)]] | wt | 93.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.8) |
| [[SW480 (line)]] | alt | 52.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 59.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.2) |
| [[C-33 A (line)]] | alt | 98.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 44.5 | 1 | 0 | [[Ponatinib (drug)]] 5 µM 3.06× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 68.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -9.6) |
| [[HCT15 (line)]] | alt | 76.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.5) |
| [[HOP62 (line)]] | alt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -15.6) |
| [[HS-578T (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.1) |
| [[J82 (line)]] | alt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 80.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 65.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.37× (z +9.6) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 73.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 64.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 86.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -17.1) |
| [[SW 1271 (line)]] | alt | 41.4 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0674× (z -8.6) |
| [[SW48 (line)]] | wt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.8) |
| [[A498 (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALS2]] | +0.78 | +0.85 / +0.68 | both halves | 7e-06 |  |
| [[FAR1]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[C20orf27]] | +0.73 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[PPAT]] | +0.72 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[WASF3]] | +0.72 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SDHAF3]] | +0.72 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.71 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.71 | +0.84 / +0.57 | both halves | 1e-05 |  |
| [[CCNY]] | +0.71 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.71 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SKP2]] | +0.70 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[GPD1L]] | +0.69 | +0.69 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | -0.79 | -0.80 / -0.63 | both halves | 7e-06 |  |
| [[ZNF764]] | -0.77 | -0.81 / -0.54 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.72 | -0.72 / -0.54 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.72 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.71 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[SP2]] | -0.70 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[CHMP4A]] | -0.69 | -0.78 / -0.58 | both halves | 7e-06 |  |
| [[FAM200A]] | -0.69 | -0.76 / -0.35 | both halves | 1e-04 |  |
| [[HELQ]] | -0.68 | -0.80 / -0.37 | both halves | 8e-05 |  |
| [[RAB30-DT]] | -0.68 | -0.73 / -0.37 | both halves | 7e-05 |  |
| [[LZIC]] | -0.67 | -0.73 / -0.47 | both halves | 2e-05 |  |
| [[GTF2IRD2]] | -0.67 | -0.69 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.0, -5.5); signed map (-40.8, -14.0). **Vector** length 128, 38.2% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +7.1 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | +7.1 | +5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.1 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.4 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -13.3 | -19.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.8 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.5 | -8.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +3.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | methionyl aminopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:98,995,659-99,062,809 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0094, MetAP1A, MAP1A |
| Gene groups (HGNC) | Aminopeptidases; M24 metallopeptidase family; MicroRNA protein coding host genes |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P53582](https://www.uniprot.org/uniprotkb/P53582) (Methionine aminopeptidase 1):

> Cotranslationally removes the N-terminal methionine from nascent proteins. The N-terminal methionine is often cleaved when the second residue in the primary sequence is small and uncharged (Met-Ala-, Cys, Gly, Pro, Ser, Thr, or Val). Required for normal progression through the cell cycle.

**Summary**, from NCBI Gene [23173](https://www.ncbi.nlm.nih.gov/gene/23173):

> Enables aminopeptidase activity. Involved in protein maturation. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15789) · Entrez [23173](https://www.ncbi.nlm.nih.gov/gene/23173) · UniProt [P53582](https://www.uniprot.org/uniprotkb/P53582) · Ensembl [ENSG00000164024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164024)

## Data

Gene col 8836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8836); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8836]; `tensor/DDL_lfc|DDL_z.npy` [8836]; `embed/gene_vectors.npy` [8836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8836 or target_col == 8836). Every well: [[METAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
