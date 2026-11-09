---
symbol: "MKNK1"
type: "gene"
col: 1248
ensembl_id: "ENSG00000079277"
name: "MAPK interacting serine/threonine kinase 1"
location: "1p33"
module: 2
arm: "+"
pooled_cpm: 33.32
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MKNK1

*MAPK interacting serine/threonine kinase 1* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.14× (z +16.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.659× (z -8.8, q 8e-16, down in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.466× (z -8.4, q 1e-14, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABAT]] (+0.60, fdr 2e-05), [[SLC8B1]] (+0.57, fdr 2e-05), [[KCTD21]] (+0.57, fdr 6e-05); moves opposite to [[SLC12A2-DT]] (-0.62, fdr 4e-05), [[SINHCAF]] (-0.61, fdr 1e-05), [[DICER1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARHGAP27]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +16.0 | 0e+00 | 45/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +15.7 | 0e+00 | 45/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +10.4 | 6e-23 | 40/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +5.1 | 6e-05 | 21/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +4.6 | 4e-04 | 14/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.21×** | +3.8 | 0.016 | 14/48 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +3.7 | 0.018 | 13/47 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.029 | 8/48 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.035 | 8/47 (A498, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.043 | 8/47 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.059 | 14/47 (CFPAC-1, SW1417, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.659×** | -8.8 | 8e-16 | 32/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.466×** | -8.4 | 1e-14 | 36/49 (NCI-H460, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.476×** | -8.2 | 5e-14 | 29/47 (HOP62, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.687×** | -7.9 | 3e-13 | 28/47 (A549, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.666×** | -7.3 | 3e-11 | 27/48 (AsPC-1, H4, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.713×** | -7.1 | 9e-11 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.708×** | -6.2 | 4e-08 | 27/47 (SNU-1, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.755×** | -5.9 | 2e-07 | 22/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.775×** | -5.4 | 5e-06 | 22/47 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.800×** | -4.7 | 1e-04 | 22/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -4.3 | 8e-04 | 17/48 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.806×** | -4.2 | 0.001 | 19/39 (KATO III, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.710×** | -3.8 | 0.007 | 15/47 (LoVo, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | 0.839× | -3.7 | 0.008 | 19/45 (NCI-H23, LoVo, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -3.3 | 0.031 | 18/47 (Hs 766T, Panc 03.27, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.897× | -3.3 | 0.037 | 11/48 (LoVo, BT-474, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.043 | 14/47 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.902× | -3.1 | 0.059 | 9/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.3 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.339× (z -12.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 36.7 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.446× (z -9.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 30.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +10.5) | — |
| [[A549 (line)]] | wt | 25.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 41.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 33.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 29.1 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0482× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -8.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[H4 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[LS 180 (line)]] | wt | 34.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -9.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[Panc 03.27 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.401× (z -8.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 52.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABAT]] | +0.60 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[SLC8B1]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[KCTD21]] | +0.57 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[TPCN2]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SAMD4B]] | +0.56 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[CYTH1]] | +0.55 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[DNAJB1]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[DOK4]] | +0.54 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[F11R]] | +0.53 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[VRK3]] | +0.53 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[UBE2H]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[LMTK3]] | +0.53 | +0.44 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A2-DT]] | -0.62 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SINHCAF]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[DICER1]] | -0.57 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[BIVM]] | -0.55 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[ARID2]] | -0.54 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[ZNRF2P2]] | -0.54 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[MBNL3]] | -0.54 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[FBXL17]] | -0.54 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[KLHL42]] | -0.53 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[DICER1-AS1]] | -0.53 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[PCMTD1-DT]] | -0.53 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[DNAAF2]] | -0.52 | -0.45 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP27]] | B | ARHGAP27 activity raises MKNK1's level | lines that do not express ARHGAP27 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without ARHGAP27 | 0.086 | ⚠ within organs, on part of the lines; also absent: TRIB3, LMNTD2, PLEKHN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.379). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.3, 10.9); signed map (-21.5, 23.3). **Vector** length 71.7, 13.3% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +15.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +16.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.3 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +0.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.6 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -4.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | MAPK interacting serine/threonine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:46,557,407-46,616,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MNK1 |
| Gene groups (HGNC) | MAPK activated protein kinases; MAPK interacting serine/threonine kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 11 pathways, smallest: Spry regulation of FGF signaling; Negative regulation of FGFR1 signaling; Negative regulation of FGFR2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUB5](https://www.uniprot.org/uniprotkb/Q9BUB5) (MAP kinase-interacting serine/threonine-protein kinase 1):

> May play a role in the response to environmental stress and cytokines. Appears to regulate translation by phosphorylating EIF4E, thus increasing the affinity of this protein for the 7-methylguanosine-containing mRNA cap.

**Summary**, from NCBI Gene [8569](https://www.ncbi.nlm.nih.gov/gene/8569):

> This gene encodes a Ser/Thr protein kinase that interacts with, and is activated by ERK1 and p38 mitogen-activated protein kinases, and thus may play a role in the response to environmental stress and cytokines. This kinase may also regulate transcription by phosphorylating eIF4E via interaction with the C-terminal region of eIF4G. Alternatively spliced transcript variants have been noted for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:7110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7110) · Entrez [8569](https://www.ncbi.nlm.nih.gov/gene/8569) · UniProt [Q9BUB5](https://www.uniprot.org/uniprotkb/Q9BUB5) · Ensembl [ENSG00000079277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079277)

## Data

Gene col 1248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1248); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1248]; `tensor/DDL_lfc|DDL_z.npy` [1248]; `embed/gene_vectors.npy` [1248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1248 or target_col == 1248). Every well: [[MKNK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKNK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
