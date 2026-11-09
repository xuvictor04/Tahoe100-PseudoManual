---
symbol: "KCTD10"
type: "gene"
col: 3177
ensembl_id: "ENSG00000110906"
name: "potassium channel tetramerization domain containing 10"
location: "12q24.11"
module: 7
arm: "+"
pooled_cpm: 30.58
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# KCTD10

*potassium channel tetramerization domain containing 10* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.53× (z +11.1, q 5e-26, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.588× (z -9.5, q 8e-19, down in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.831× (z -4.9, q 2e-04, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF25]] (+0.63, fdr 1e-05), [[ATOSB]] (+0.60, fdr 7e-06), [[RIC8A]] (+0.58, fdr 3e-05); moves opposite to [[PSPC1]] (-0.52, fdr 2e-05), [[CRNDE]] (-0.51, fdr 3e-05), [[PAXBP1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +11.1 | 5e-26 | 35/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +10.1 | 1e-21 | 42/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +7.9 | 6e-13 | 36/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +7.0 | 3e-10 | 1/48 (SW 1088) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.4 | 1e-08 | 32/48 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.0 | 2e-07 | 25/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.7 | 8e-07 | 29/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.7 | 9e-07 | 27/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +5.0 | 3e-05 | 25/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +4.8 | 8e-05 | 22/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 8e-05 | 25/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 3e-04 | 19/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 21/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 20/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.8 | 0.006 | 12/41 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.008 | 13/48 (C-33 A, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -9.5 | 8e-19 | 23/35 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.607×** | -9.3 | 4e-18 | 27/45 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -4.9 | 2e-04 | 20/48 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.070 | 14/48 (SW 1088, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.821×** | -3.4 | 0.070 | 17/39 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.071 | 14/47 (SW480, Panc 03.27, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.839× | -3.3 | 0.085 | 17/48 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.842× | -3.2 | 0.091 | 12/48 (NCI-H2030, A-172, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.890× | -3.1 | 0.12 | 13/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.849× | -3.1 | 0.12 | 12/48 (HOP62, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.6) | — |
| [[SW480 (line)]] | alt | 26.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.57× (z +9.7) | — |
| [[A-427 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -9.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0968× (z -8.5) |
| [[HOP62 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0701× (z -17.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 38.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.5) | — |
| [[A-172 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF25]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ATOSB]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RIC8A]] | +0.58 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[EIF2B2]] | +0.57 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[RAMAC]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ZNF408]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ZNF17]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ZSCAN20]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[HECTD3]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[ZSCAN22]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[TIMM22]] | +0.53 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[SDE2]] | +0.53 | +0.49 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSPC1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CRNDE]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PAXBP1]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SMCHD1]] | -0.50 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PKD2]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NAP1L1]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[DPY19L1P1]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LCORL]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SLC25A5]] | -0.45 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ADGRA3]] | -0.45 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[NFIA]] | -0.45 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[PUM2]] | -0.44 | -0.31 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-48.9, 4.5); signed map (-24.5, 3.6). **Vector** length 89.6, 19.1% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.7 | +11.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.5 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +10.1 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.6 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | -9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,448,655-109,477,359 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MSTP028, BTBD28 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3F6](https://www.uniprot.org/uniprotkb/Q9H3F6) (BTB/POZ domain-containing adapter for CUL3-mediated RhoA degradation protein 3):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that mediates the ubiquitination of multiple substrates, leading to either their proteasomal or lysosomal degradation, or modulating their activity through non-degradative ubiquitination. Controls endothelial barrier function by mediating 'Lys-63'-linked polyubiquitination of RHOB, promoting its lysosomal degradation. Mediates polyubiquitination of CEP97, targeting it for proteasomal degradation. CEP97 degradation …

**Summary**, from NCBI Gene [83892](https://www.ncbi.nlm.nih.gov/gene/83892):

> The protein encoded by this gene binds proliferating cell nuclear antigen (PCNA) and may be involved in DNA synthesis and cell proliferation. In addition, the encoded protein may be a tumor suppressor. Several protein-coding and non-protein coding transcript variants have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:23236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23236) · Entrez [83892](https://www.ncbi.nlm.nih.gov/gene/83892) · UniProt [Q9H3F6](https://www.uniprot.org/uniprotkb/Q9H3F6) · Ensembl [ENSG00000110906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110906)

## Data

Gene col 3177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3177); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3177]; `tensor/DDL_lfc|DDL_z.npy` [3177]; `embed/gene_vectors.npy` [3177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3177 or target_col == 3177). Every well: [[KCTD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
