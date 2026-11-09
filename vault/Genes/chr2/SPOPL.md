---
symbol: "SPOPL"
type: "gene"
col: 6856
ensembl_id: "ENSG00000144228"
name: "speckle type BTB/POZ protein like"
location: "2q22.1"
module: 45
arm: "+"
pooled_cpm: 95.52
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SPOPL

*speckle type BTB/POZ protein like* — 2q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.18× (z +7.5, q 4e-11, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.638× (z -7.9, q 2e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP3]] (+0.67, fdr 8e-06), [[ORC4]] (+0.65, fdr 7e-06), [[LMBRD1]] (+0.63, fdr 1e-05); moves opposite to [[TAF2]] (-0.63, fdr 1e-05), [[OPA3]] (-0.61, fdr 1e-05), [[CDK12]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +7.5 | 4e-11 | 36/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.5 | 8e-06 | 31/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.3 | 0.002 | 25/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +4.3 | 0.002 | 25/49 (NCI-H1573, SW48, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.034 | 11/49 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.074 | 21/48 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.100 | 19/49 (SNU-423, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6856.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -7.9 | 2e-12 | 38/48 (HOP62, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.678×** | -7.2 | 2e-10 | 39/48 (HepG2/C3A, HOP62, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.776×** | -6.6 | 6e-09 | 32/49 (NCI-H460, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.700×** | -6.3 | 3e-08 | 28/44 (NCI-H1573, NCI-H2347, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -5.6 | 3e-06 | 30/48 (NCI-H661, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.771×** | -4.8 | 1e-04 | 25/48 (NCI-H460, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.778×** | -4.7 | 3e-04 | 23/49 (NCI-H2347, SW48, …) | rises with dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.793×** | -4.3 | 0.001 | 24/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.792×** | -4.1 | 0.002 | 24/47 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.870× | -3.7 | 0.015 | 11/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.829×** | -3.3 | 0.051 | 19/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.065 | 16/48 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.842× | -3.2 | 0.065 | 18/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.430× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -14.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -8.8) |
| [[PANC-1 (line)]] | alt | 78.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.4) | — |
| [[SW48 (line)]] | wt | 109 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.05× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AsPC-1 (line)]] | alt | 131 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 224 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -10.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 80.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -11.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 82.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 89.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -8.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CHP-212 (line)]] | wt | 80.9 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.219× (z -8.5) |
| [[COLO 205 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 103 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.69× (z +9.4) | — |
| [[LoVo (line)]] | wt | 51.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.74× (z +10.2) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 88.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H661 (line)]] | alt | 80.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.217× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 81.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -9.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SW 1088 (line)]] | alt | 62.8 | 0 | 1 | — | [[Hydroxyurea (drug)]] 5 µM 0.0755× (z -8.7) |
| [[SW 1271 (line)]] | alt | 94.9 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0539× (z -12.8) |
| [[SW1417 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 95.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 92.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 99.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 79.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP3]] | +0.67 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[ORC4]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[LMBRD1]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[NEK7]] | +0.63 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[KCTD6]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 | same gene group |
| [[LTA4H]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[FAM168A]] | +0.60 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[CNOT6L]] | +0.60 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[FRG1CP]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PRKAB2]] | +0.59 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[FHIP1A]] | +0.59 | +0.65 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.63 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[OPA3]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CDK12]] | -0.61 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[REXO1]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[AGAP6]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[GLYR1]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TM9SF4]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[RBM19]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[MED1]] | -0.54 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ZBTB40]] | -0.54 | -0.65 / -0.29 | both halves | 3e-04 | same gene group |
| [[CRK]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[METTL2B]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-4.7, -7.5); signed map (-29.6, -7.9). **Vector** length 104, 29.8% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +6.0 | +4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | -0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | speckle type BTB/POZ protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.1 — chr2:138,501,770-138,573,547 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTBD33 |
| Gene groups (HGNC) | BTB domain containing |
| Reactome | 2 pathways, smallest: Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ16](https://www.uniprot.org/uniprotkb/Q6IQ16) (Speckle-type POZ protein-like):

> Component of a cullin-RING-based BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex that mediates the ubiquitination and subsequent proteasomal degradation of target proteins, but with relatively low efficiency. Cullin-RING-based BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complexes containing homodimeric SPOPL or the heterodimer formed by SPOP and SPOPL are less efficient than ubiquitin ligase complexes containing only SPOP. May function to down-regulate the activity of …

**Summary**, from NCBI Gene [339745](https://www.ncbi.nlm.nih.gov/gene/339745):

> Enables identical protein binding activity. Involved in negative regulation of protein ubiquitination and proteasome-mediated ubiquitin-dependent protein catabolic process. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27934) · Entrez [339745](https://www.ncbi.nlm.nih.gov/gene/339745) · UniProt [Q6IQ16](https://www.uniprot.org/uniprotkb/Q6IQ16) · Ensembl [ENSG00000144228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144228)

## Data

Gene col 6856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6856); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6856]; `tensor/DDL_lfc|DDL_z.npy` [6856]; `embed/gene_vectors.npy` [6856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6856 or target_col == 6856). Every well: [[SPOPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
