---
symbol: "RRP12"
type: "gene"
col: 586
ensembl_id: "ENSG00000052749"
name: "ribosomal RNA processing 12 homolog"
location: "10q24.1"
module: 38
arm: "+"
pooled_cpm: 61.69
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# RRP12

*ribosomal RNA processing 12 homolog* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.61× (z +9.8, q 5e-20, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.674× (z -5.8, q 5e-06, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.642× (z -4.6, q 0.001, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL2]] (+0.63, fdr 7e-06), [[USP36]] (+0.62, fdr 1e-05), [[KCNJ14]] (+0.61, fdr 1e-05); moves opposite to [[RPP30]] (-0.56, fdr 5e-05), [[FAM199X]] (-0.54, fdr 3e-05), [[ABHD13]] (-0.53, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.61×** | +9.8 | 5e-20 | 44/48 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.92×** | +9.4 | 1e-18 | 39/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.33×** | +8.7 | 7e-16 | 46/48 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.6 | 8e-16 | 39/48 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.22×** | +8.1 | 4e-14 | 42/48 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.20×** | +7.7 | 9e-13 | 38/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +7.1 | 8e-11 | 40/48 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +6.2 | 3e-08 | 41/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +5.8 | 5e-07 | 37/48 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.74×** | +5.7 | 8e-07 | 41/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +5.6 | 8e-07 | 39/49 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.82×** | +5.5 | 1e-06 | 35/48 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +5.4 | 3e-06 | 38/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +5.0 | 3e-05 | 35/48 (HepG2/C3A, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 2e-04 | 30/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 34/49 (J82, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.71×** | +3.9 | 0.003 | 38/49 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.674×** | -5.8 | 5e-06 | 31/48 (A498, LoVo, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.642×** | -4.6 | 0.001 | 31/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.675×** | -3.9 | 0.018 | 31/48 (SW480, C-33 A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.688×** | -3.7 | 0.024 | 27/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.671×** | -3.7 | 0.024 | 29/48 (NCI-H1573, LS 180, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.711× | -3.3 | 0.11 | 25/48 (SW480, A-427, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.805× | -3.2 | 0.13 | 23/48 (SW480, A549, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.717× | -3.1 | 0.14 | 24/48 (AN3 CA, SK-MEL-2, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.721× | -3.0 | 0.15 | 21/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 66.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.68× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 62.4 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.15× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 28.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +11.0) | — |
| [[LoVo (line)]] | wt | 46.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 78.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 36.9 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.93× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 47.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 35.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 30.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 52.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.83× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.30× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 40.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.0) | — |
| [[A498 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.447× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 60.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 32.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 76.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 60.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.5) | — |
| [[KATO III (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.596× (z -9.1) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 47.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL2]] | +0.63 | +0.66 / +0.66 | both halves | 7e-06 | STRING 917 |
| [[USP36]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[KCNJ14]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[KIF9]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[FOSB]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KLHL18]] | +0.58 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ZNF335]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TXLNG]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[VWCE]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[USE1]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PPIEL]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CCDC40]] | +0.53 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP30]] | -0.56 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[FAM199X]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ABHD13]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TBC1D13]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SUMO2]] | -0.47 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[DLD]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[FBXO7]] | -0.47 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[PEX2]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[HDAC1]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[TRAF6]] | -0.46 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[VPS33B]] | -0.45 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[HDAC2]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, -27.5); signed map (8.0, 11.9). **Vector** length 111, 39.0% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +8.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.9 | +6.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.7 | +1.8 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Demeclocycline (drug)]] 0.05 µM |  | +2.5 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.9 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.1 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 12 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:97,356,358-97,426,076 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0690 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Ribosome biogenesis factors |
| Hallmark sets | MYC_TARGETS_V2, ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTH9](https://www.uniprot.org/uniprotkb/Q5JTH9) (RRP12-like protein):

> Participates in the nucleoplasmic stage of pre-40S ribosomal subunit assembly, functioning as a scaffold for assembly factors and preparing pre-40S particles for export from the nucleus to the cytoplasm.

**Summary**, from NCBI Gene [23223](https://www.ncbi.nlm.nih.gov/gene/23223):

> Enables RNA binding activity. Located in nucleolus and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29100) · Entrez [23223](https://www.ncbi.nlm.nih.gov/gene/23223) · UniProt [Q5JTH9](https://www.uniprot.org/uniprotkb/Q5JTH9) · Ensembl [ENSG00000052749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000052749)

## Data

Gene col 586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 586); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 586]; `tensor/DDL_lfc|DDL_z.npy` [586]; `embed/gene_vectors.npy` [586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 586 or target_col == 586). Every well: [[RRP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
