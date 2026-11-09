---
symbol: "PPP6R1"
type: "gene"
col: 2544
ensembl_id: "ENSG00000105063"
name: "protein phosphatase 6 regulatory subunit 1"
location: "19q13.42"
module: 2
arm: "+"
pooled_cpm: 70.16
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PPP6R1

*protein phosphatase 6 regulatory subunit 1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.38× (z +6.0, q 8e-07, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.33× (z +5.3, q 3e-05, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.783× (z -4.6, q 0.001, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHRF1]] (+0.69, fdr 7e-06), [[SAP130]] (+0.69, fdr 1e-05), [[GAK]] (+0.63, fdr 1e-05); moves opposite to [[TRMT13]] (-0.57, fdr 1e-05), [[GCFC2]] (-0.55, fdr 2e-05), [[AASDHPPT]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +6.0 | 8e-07 | 29/48 (LS 180, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.3 | 3e-05 | 33/48 (LoVo, COLO 205, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.30×** | +4.8 | 3e-04 | 25/47 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 5e-04 | 27/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.4 | 0.001 | 27/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.4 | 0.001 | 25/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.17× | +4.2 | 0.002 | 19/49 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.23×** | +3.9 | 0.005 | 24/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +3.9 | 0.005 | 21/48 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 24/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.005 | 24/48 (HT-29, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.21×** | +3.6 | 0.015 | 21/48 (SW480, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | 1.17× | +3.0 | 0.11 | 17/47 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.783×** | -4.6 | 0.001 | 26/48 (NCI-H2347, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.784×** | -4.6 | 0.001 | 28/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.788×** | -4.5 | 0.001 | 25/48 (NCI-H2347, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.815×** | -3.9 | 0.016 | 21/47 (NCI-H460, C32, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.811×** | -3.8 | 0.017 | 22/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -3.5 | 0.035 | 15/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.824×** | -3.5 | 0.035 | 21/47 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.877× | -3.5 | 0.035 | 18/48 (SK-MEL-2, NCI-H2347, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.045 | 23/48 (NCI-H2347, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.3 | 0.046 | 20/48 (J82, NCI-H2347, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.2 | 0.063 | 18/48 (LS 180, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 58.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.485× (z -8.8) |
| [[SW480 (line)]] | alt | 56.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | — |
| [[NCI-H460 (line)]] | wt | 53.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.15× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[BT-474 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.272× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 39.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 95.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +11.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 82.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 71.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -11.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 71.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | — |
| [[SNU-1 (line)]] | wt | 82.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SW 1088 (line)]] | alt | 83.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.101× (z -8.5) |
| [[SW 1271 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0706× (z -9.4) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 68.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHRF1]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SAP130]] | +0.69 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[GAK]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SBF1]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 | STRING 401 |
| [[TUSC2]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[C2CD2L]] | +0.62 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NELFB]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[CAPN10]] | +0.60 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TRIM11]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 | same gene group |
| [[TESK1]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 | same gene group |
| [[TBC1D10B]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[GCFC2]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[AASDHPPT]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SLC16A9]] | -0.53 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[SETDB2]] | -0.53 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TAF9]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TMEM35B]] | -0.53 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[CHIC1]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[ZNF280D]] | -0.52 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[UBQLN2]] | -0.51 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[CC2D2A]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ZXDA]] | -0.51 | -0.49 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-12.2, -6.5); signed map (-42.0, 4.0). **Vector** length 100, 24.9% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.0 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.2 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 6 regulatory subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,229,779-55,259,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAP190; previously KIAA1115, SAPS1 |
| Gene groups (HGNC) | Protein phosphatase 6 regulatory subunits; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPN7](https://www.uniprot.org/uniprotkb/Q9UPN7) (Serine/threonine-protein phosphatase 6 regulatory subunit 1):

> Regulatory subunit of protein phosphatase 6 (PP6). May function as a scaffolding PP6 subunit. Involved in the PP6-mediated dephosphorylation of NFKBIE opposing its degradation in response to TNF.

**Summary**, from NCBI Gene [22870](https://www.ncbi.nlm.nih.gov/gene/22870):

> Protein phosphatase regulatory subunits, such as SAPS1, modulate the activity of protein phosphatase catalytic subunits by restricting substrate specificity, recruiting substrates, and determining the intracellular localization of the holoenzyme. SAPS1 is a regulatory subunit for the protein phosphatase-6 catalytic subunit (PPP6C; MIM 612725) (Stefansson and Brautigan, 2006 [PubMed 16769727]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:29195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29195) · Entrez [22870](https://www.ncbi.nlm.nih.gov/gene/22870) · UniProt [Q9UPN7](https://www.uniprot.org/uniprotkb/Q9UPN7) · Ensembl [ENSG00000105063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105063)

## Data

Gene col 2544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2544); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2544]; `tensor/DDL_lfc|DDL_z.npy` [2544]; `embed/gene_vectors.npy` [2544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2544 or target_col == 2544). Every well: [[PPP6R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP6R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
