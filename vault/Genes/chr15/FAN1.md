---
symbol: "FAN1"
type: "gene"
col: 12643
ensembl_id: "ENSG00000198690"
name: "FANCD2 and FANCI associated nuclease 1"
location: "15q13.3"
module: 1
arm: "+"
pooled_cpm: 33.36
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FAN1

*FANCD2 and FANCI associated nuclease 1* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.26× (z +5.1, q 1e-04, up in 19 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.26× (z +5.1, q 1e-04, up in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 2.56×, SHP-77 2.06×, A-427 2.16×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.460× (z -17.0, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCERG1]] (+0.66, fdr 7e-06), [[IMPACT]] (+0.61, fdr 1e-05), [[CCDC113]] (+0.60, fdr 1e-05); moves opposite to [[TSC22D4]] (-0.58, fdr 1e-05), [[PTMS]] (-0.53, fdr 1e-05), [[CXCR4]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12643.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LOX-IMVI 2.56×, SHP-77 2.06×, A-427 2.16×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.1 | 1e-04 | 19/46 (NCI-H1573, LoVo, …) | two highest doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 1e-04 | 20/47 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | 1.20× | +3.9 | 0.022 | 17/36 (HT-29, SNU-423, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.22 | 11/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.25 | 7/47 (A-172, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.14× | +3.0 | 0.25 | 12/48 (LS 180, COLO 205, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.460×** | -17.0 | 0e+00 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -13.7 | 3e-40 | 36/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -13.7 | 3e-40 | 33/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -11.0 | 9e-26 | 34/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -10.4 | 5e-23 | 32/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.465×** | -8.7 | 2e-16 | 31/48 (C32, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -6.7 | 2e-09 | 25/47 (HCT15, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.567×** | -6.5 | 7e-09 | 29/46 (C32, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.793×** | -4.8 | 9e-05 | 18/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.816×** | -4.2 | 0.001 | 16/46 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.886× | -3.7 | 0.012 | 11/48 (Hs 766T, H4, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.743×** | -3.4 | 0.036 | 9/32 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.858× | -3.3 | 0.041 | 7/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | 0.856× | -3.2 | 0.048 | 6/47 (Panc 03.27, HS-578T, …) | rises with dose | position effect removed |
| [[crizotinib (drug)]] 5 µM |  | 0.860× | -3.1 | 0.063 | 7/48 (Hs 766T, HOP62, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.902× | -3.1 | 0.064 | 3/48 (LOX-IMVI, NCI-H23, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 27.9 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.9) |
| [[SW480 (line)]] | alt | 32.6 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -15.5) |
| [[HOP62 (line)]] | alt | 29.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 84.2 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -13.8) |
| [[PANC-1 (line)]] | alt | 36.1 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -14.6) |
| [[LoVo (line)]] | wt | 51.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.420× (z -9.8) |
| [[SW 1271 (line)]] | alt | 82.2 | 0 | 3 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0741× (z -11.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -10.6) |
| [[C32 (line)]] | wt | 88.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -15.5) |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.263× (z -9.6) |
| [[A-172 (line)]] | wt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.8) |
| [[A-427 (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 35.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -10.4) |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0892× (z -9.3) |
| [[COLO 205 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -11.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 37.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -8.8) |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.249× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0959× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -8.6) |
| [[KATO III (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0600× (z -10.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 45.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.277× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 59.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -9.5) |
| [[SHP-77 (line)]] | alt | 68.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -8.9) |
| [[A549 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCERG1]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CCDC113]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CEP290]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ICE2]] | +0.60 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DPH5]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MKS1]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[BMS1]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[DNAJA3]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PTCD2]] | +0.56 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PTMS]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CXCR4]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GATA2]] | -0.49 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[GNAS]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GRN]] | -0.48 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[SPINT1]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PERP]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[TOR1B]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TIMP2]] | -0.47 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NPTN]] | -0.47 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[UBL5]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.9, 2.2); signed map (-0.2, -38.4). **Vector** length 79.8, 15.1% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | +3.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -11.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -13.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -13.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -17.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -6.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | FANCD2 and FANCI associated nuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:30,890,559-30,943,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1018, MTMR15 |
| Gene groups (HGNC) | Zinc fingers UBZ4 CCHC-type |
| Reactome | 2 pathways, smallest: Fanconi Anemia Pathway; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2M0](https://www.uniprot.org/uniprotkb/Q9Y2M0) (Fanconi-associated nuclease 1):

> Nuclease required for the repair of DNA interstrand cross-links (ICL) recruited at sites of DNA damage by monoubiquitinated FANCD2. Specifically involved in repair of ICL-induced DNA breaks by being required for efficient homologous recombination, probably in the resolution of homologous recombination intermediates. Not involved in DNA double-strand breaks resection. Acts as a 5'-3' exonuclease that anchors at a cut end of DNA and cleaves DNA successively at every third nucleotide, allowing to …

**Summary**, from NCBI Gene [22909](https://www.ncbi.nlm.nih.gov/gene/22909):

> This gene plays a role in DNA interstrand cross-link repair and encodes a protein with 5' flap endonuclease and 5'-3' exonuclease activity. Mutations in this gene cause karyomegalic interstitial nephritis. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:29170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29170) · Entrez [22909](https://www.ncbi.nlm.nih.gov/gene/22909) · UniProt [Q9Y2M0](https://www.uniprot.org/uniprotkb/Q9Y2M0) · Ensembl [ENSG00000198690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198690)

## Data

Gene col 12643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12643); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12643]; `tensor/DDL_lfc|DDL_z.npy` [12643]; `embed/gene_vectors.npy` [12643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12643 or target_col == 12643). Every well: [[FAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
