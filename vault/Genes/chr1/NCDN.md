---
symbol: "NCDN"
type: "gene"
col: 318
ensembl_id: "ENSG00000020129"
name: "neurochondrin"
location: "1p34.3"
module: 96
arm: "+"
pooled_cpm: 5.65
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# NCDN

*neurochondrin* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.82× (z +7.1, q 6e-10, up in 16 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.79× (z +6.9, q 1e-09, up in 25 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.658× (z -4.8, q 1e-03, down in 12 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (C32 0.0708×); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SHP-77 0.0803×); [[Docetaxel (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.144×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAAP100]] (+0.71, fdr 7e-06), [[TAF1C]] (+0.68, fdr 7e-06), [[WIZ]] (+0.67, fdr 7e-06); moves opposite to [[ZNRF2]] (-0.53, fdr 3e-05), [[PIAS1]] (-0.52, fdr 3e-05), [[PPP2R5E]] (-0.51, fdr 5e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.1 | 6e-10 | 16/23 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +6.9 | 1e-09 | 25/39 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.5 | 2e-08 | 9/9 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +5.3 | 2e-05 | 14/46 (SK-MEL-2, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +5.1 | 3e-05 | 8/17 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 8e-04 | 11/42 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.4 | 1e-03 | 18/39 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.2 | 0.002 | 12/46 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.011 | 15/44 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.012 | 10/47 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.7 | 0.013 | 8/34 (A498, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.6 | 0.017 | 11/32 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Resveratrol (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.025 | 5/44 (A498, HT-29, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.028 | 9/43 (H4, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.041 | 6/42 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.050 | 4/47 (PANC-1, NCI-H1792, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.065 | 2/32 (HEC-1-A, NCI-H2347) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.069 | 3/43 (PANC-1, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.069 | 3/41 (SK-MEL-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 318.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (C32 0.0708×); [[Acetohexamide (drug)]] 0.5 µM in 1 line (SHP-77 0.0803×); [[Docetaxel (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.144×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.658×** | -4.8 | 1e-03 | 12/42 (A-172, J82, …) | top dose only | position effect removed |
| [[Silodosin (drug)]] 5 µM |  | **0.730×** | -3.6 | 0.094 | 9/43 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.4 | 0.12 | 8/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.755× | -3.3 | 0.12 | 11/45 (AN3 CA, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.590× | -3.3 | 0.12 | 3/11 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.762× | -3.2 | 0.12 | 10/47 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.771× | -3.1 | 0.17 | 11/39 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 4.70 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0708× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 7.10 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.144× (z -8.5) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 6.56 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0803× (z -8.8) |
| [[A-172 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAP100]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TAF1C]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[WIZ]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ARFRP1]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SRSF6]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHG4]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ATXN7L2]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[DRG2]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RHOT2]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CD2BP2]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.61 | +0.60 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WDR6]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF2]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PIAS1]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[PPP2R5E]] | -0.51 | -0.57 / -0.39 | both halves | 5e-05 | same gene group |
| [[ELF2]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CDC42SE2]] | -0.50 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[COX6A1]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MZT2B]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[PPP2R5A]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 | same gene group |
| [[TBC1D12]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A5]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RPS8]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.1, -25.0); signed map (-9.0, -32.1). **Vector** length 58.2, 7.85% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +0.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +0.6 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | -0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | neurochondrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,557,473-35,567,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCDN-1, NCDN-2 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBB6](https://www.uniprot.org/uniprotkb/Q9UBB6) (Neurochondrin):

> Probably involved in signal transduction in the nervous system, via increasing cell surface localization of GRM5/mGluR5 and positively regulating its signaling. Required for the spatial learning process. Acts as a negative regulator of Ca(2+)-calmodulin-dependent protein kinase 2 (CaMK2) phosphorylation. May play a role in modulating melanin-concentrating hormone-mediated functions via its interaction with MCHR1 that interferes with G protein-coupled signal transduction. May be involved in bone …

**Summary**, from NCBI Gene [23154](https://www.ncbi.nlm.nih.gov/gene/23154):

> This gene encodes a leucine-rich cytoplasmic protein, which is highly similar to a mouse protein that negatively regulates Ca/calmodulin-dependent protein kinase II phosphorylation and may be essential for spatial learning processes. Several alternatively spliced transcript variants of this gene have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17597) · Entrez [23154](https://www.ncbi.nlm.nih.gov/gene/23154) · UniProt [Q9UBB6](https://www.uniprot.org/uniprotkb/Q9UBB6) · Ensembl [ENSG00000020129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000020129)

## Data

Gene col 318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 318); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 318]; `tensor/DDL_lfc|DDL_z.npy` [318]; `embed/gene_vectors.npy` [318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 318 or target_col == 318). Every well: [[NCDN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCDN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
