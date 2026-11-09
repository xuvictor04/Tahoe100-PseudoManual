---
symbol: "FAM174A"
type: "gene"
col: 10464
ensembl_id: "ENSG00000174132"
name: "family with sequence similarity 174 member A"
location: "5q21.1"
module: 205
arm: "+"
pooled_cpm: 20.7
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# FAM174A

*family with sequence similarity 174 member A* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +11.7, q 7e-29, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.561× (z -13.9, q 2e-41, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC10]] (+0.72, fdr 7e-06), [[SLC25A14]] (+0.69, fdr 7e-06), [[ANKRD42]] (+0.69, fdr 1e-05); moves opposite to [[AKIRIN1]] (-0.56, fdr 2e-05), [[TMEM185B]] (-0.54, fdr 3e-05), [[ACSL4]] (-0.52, fdr 9e-05).
> It is in [[Module 205]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.7 | 7e-29 | 36/47 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.53×** | +11.2 | 7e-27 | 37/48 (SW480, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +10.1 | 9e-22 | 36/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +8.3 | 2e-14 | 35/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +5.9 | 3e-07 | 21/48 (NCI-H2347, PANC-1, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.5 | 3e-06 | 16/37 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.5 | 3e-06 | 24/48 (LOX-IMVI, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.37×** | +5.4 | 5e-06 | 25/48 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 1e-04 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 1e-04 | 19/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 1e-03 | 14/48 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.016 | 19/48 (SW480, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +3.6 | 0.016 | 14/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +3.4 | 0.023 | 19/47 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +3.4 | 0.024 | 10/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.046 | 4/46 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.059 | 10/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.059 | 3/48 (A-172, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.561×** | -13.9 | 2e-41 | 43/48 (HS-578T, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.625×** | -8.0 | 3e-13 | 30/48 (SW48, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -6.5 | 1e-08 | 26/48 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -5.9 | 5e-07 | 25/47 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.738×** | -5.2 | 3e-05 | 21/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -4.6 | 4e-04 | 17/33 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.764×** | -4.4 | 8e-04 | 11/47 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.008 | 17/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.811×** | -3.3 | 0.063 | 14/47 (KATO III, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 5 µM |  | 0.881× | -3.1 | 0.13 | 14/48 (NCI-H2347, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 31.1 | 0 | 3 (1 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.311× (z -11.9) |
| [[A498 (line)]] | wt | 33.8 | 0 | 2 | — | [[Tucidinostat (drug)]] 5 µM 0.436× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 12.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 22.6× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.374× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.432× (z -9.9) |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.181× (z -10.6) |
| [[HOP62 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.42× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 21.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.432× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.3) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H2030 (line)]] | alt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 40.0 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.560× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.408× (z -8.9) |
| [[PANC-1 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.4) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.1) | — |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC10]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[SLC25A14]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ANKRD42]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[FAM185BP]] | +0.68 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ASB7]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TMEM67]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[ALDH6A1]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.61 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[ZNF487]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[SEZ6L2]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[RELCH]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKIRIN1]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.54 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ACSL4]] | -0.52 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[TNFRSF12A]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[REEP3]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RASGRF1]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SKIL]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[LINC02516]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.4, 21.6); signed map (-19.7, 5.0). **Vector** length 98.2, 21.3% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.9 | +10.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +11.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.2 | +4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.7 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.5 | -13.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.8 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 174 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.1 — chr5:100,535,338-100,586,741 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ1912, NS5ATP6; previously TMEM157 |
| Matched by | ensembl_id |

UniProt [Q8TBP5](https://www.uniprot.org/uniprotkb/Q8TBP5) carries no function annotation.

**Summary**, from NCBI Gene [345757](https://www.ncbi.nlm.nih.gov/gene/345757):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24943) · Entrez [345757](https://www.ncbi.nlm.nih.gov/gene/345757) · UniProt [Q8TBP5](https://www.uniprot.org/uniprotkb/Q8TBP5) · Ensembl [ENSG00000174132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174132)

## Data

Gene col 10464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10464); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10464]; `tensor/DDL_lfc|DDL_z.npy` [10464]; `embed/gene_vectors.npy` [10464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10464 or target_col == 10464). Every well: [[FAM174A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM174A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
