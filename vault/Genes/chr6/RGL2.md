---
symbol: "RGL2"
type: "gene"
col: 14132
ensembl_id: "ENSG00000237441"
name: "ral guanine nucleotide dissociation stimulator like 2"
location: "6p21.32"
module: 173
arm: "+"
pooled_cpm: 11.12
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# RGL2

*ral guanine nucleotide dissociation stimulator like 2* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +12.6, q 8e-34, up in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +4.4, q 0.001, up in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (MIA PaCa-2 4.83×, SNU-423 4.82×, NCI-H460 4.15×, LoVo 3.91×, …; ⚠ cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.447× (z -10.1, q 4e-21, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBRS]] (+0.72, fdr 7e-06), [[SIX5]] (+0.70, fdr 7e-06), [[GPR137]] (+0.68, fdr 9e-06); moves opposite to [[PACC1]] (-0.57, fdr 2e-05), [[MTERF3]] (-0.56, fdr 4e-05), [[ATG5]] (-0.56, fdr 3e-05).
> It is in [[Module 173]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (MIA PaCa-2 4.83×, SNU-423 4.82×, NCI-H460 4.15×, LoVo 3.91×, …; ⚠ cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.05×** | +12.6 | 8e-34 | 33/47 (MIA PaCa-2, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +6.6 | 1e-08 | 12/21 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.4 | 2e-08 | 25/35 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.4 | 0.001 | 16/31 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.43×** | +4.4 | 0.001 | 17/44 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.4 | 0.001 | 19/45 (NCI-H2347, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +4.3 | 0.001 | 17/44 (MIA PaCa-2, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.29× | +3.1 | 0.14 | 8/47 (NCI-H2030, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -10.1 | 4e-21 | 40/47 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.466×** | -9.6 | 4e-19 | 41/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.504×** | -8.6 | 2e-15 | 35/47 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.668×** | -7.2 | 1e-10 | 29/48 (LS 180, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -5.5 | 3e-06 | 26/47 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.662×** | -5.2 | 2e-05 | 26/47 (Hs 766T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.727×** | -4.0 | 0.004 | 13/47 (NCI-H1573, HCT15, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.458×** | -4.0 | 0.004 | 13/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.721×** | -4.0 | 0.005 | 16/45 (HepG2/C3A, A-427, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.759×** | -3.5 | 0.029 | 15/42 (SW1417, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.739×** | -3.3 | 0.058 | 10/47 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.774× | -3.1 | 0.11 | 10/44 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.757× | -3.0 | 0.11 | 10/48 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -10.5) |
| [[LoVo (line)]] | wt | 7.99 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +12.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 6.34 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +10.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0859× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[SNU-423 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +12.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBRS]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[SIX5]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[GPR137]] | +0.68 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[AKT1S1]] | +0.67 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[STX10]] | +0.66 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[IRF3]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[KDM6B]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ENO3]] | +0.65 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[USP11]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CYB5D1]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.64 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[MMRN2]] | +0.63 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MTERF3]] | -0.56 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ATG5]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[FAR1]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RFXAP]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[GTF2E2]] | -0.54 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[TPD52]] | -0.53 | -0.49 / -0.43 | both halves | 4e-05 |  |
| [[CROT]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PIP4K2A]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[CBX1]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PLA2G12A]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[BLVRA]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.3, 9.9); signed map (14.7, -8.8). **Vector** length 78.4, 16.4% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +10.2 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.3 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ral guanine nucleotide dissociation stimulator like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,291,654-33,298,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KE1.5, HKE1.5; previously RAB2L |
| Gene groups (HGNC) | Ral guanine nucleotide dissociation stimulator family |
| Reactome | 3 pathways, smallest: RAF/MAP kinase cascade; MAPK1/MAPK3 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [O15211](https://www.uniprot.org/uniprotkb/O15211) (Ral guanine nucleotide dissociation stimulator-like 2):

> Probable guanine nucleotide exchange factor. Putative effector of Ras and/or Rap. Associates with the GTP-bound form of Rap 1A and H-Ras in vitro (By similarity).

**Summary**, from NCBI Gene [5863](https://www.ncbi.nlm.nih.gov/gene/5863):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in Ras protein signal transduction. Predicted to act upstream of or within negative regulation of cardiac muscle cell apoptotic process; positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and regulation of Ral protein signal transduction. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9769) · Entrez [5863](https://www.ncbi.nlm.nih.gov/gene/5863) · UniProt [O15211](https://www.uniprot.org/uniprotkb/O15211) · Ensembl [ENSG00000237441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237441)

## Data

Gene col 14132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14132); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14132]; `tensor/DDL_lfc|DDL_z.npy` [14132]; `embed/gene_vectors.npy` [14132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14132 or target_col == 14132). Every well: [[RGL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
