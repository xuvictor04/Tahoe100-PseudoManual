---
symbol: "DCUN1D2"
type: "gene"
col: 7431
ensembl_id: "ENSG00000150401"
name: "defective in cullin neddylation 1 domain containing 2"
location: "13q34"
module: 16
arm: "-"
pooled_cpm: 38.17
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DCUN1D2

*defective in cullin neddylation 1 domain containing 2* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.23× (z +11.1, q 8e-26, up in 31 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.85× (z +9.9, q 2e-20, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.697× (z -8.3, q 6e-14, down in 29 of 47 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.727× (z -5.2, q 3e-05, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTFR1]] (+0.70, fdr 7e-06), [[FOXK2]] (+0.65, fdr 7e-06), [[ZNF250]] (+0.65, fdr 7e-06); moves opposite to [[FNBP1P1]] (-0.67, fdr 2e-05), [[ZNF620]] (-0.67, fdr 3e-05), [[METTL18]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DMRTA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +11.1 | 8e-26 | 31/49 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +9.9 | 2e-20 | 45/48 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +9.2 | 4e-18 | 43/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +8.7 | 3e-16 | 42/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +6.6 | 4e-09 | 37/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.0 | 2e-07 | 29/48 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.8 | 1e-04 | 31/48 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 3e-04 | 24/47 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.002 | 22/48 (SNU-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.007 | 20/47 (H4, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.28×** | +3.7 | 0.011 | 15/48 (J82, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.025 | 18/48 (BT-474, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.25×** | +3.4 | 0.027 | 19/46 (SW480, SHP-77, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.034 | 7/48 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.23×** | +3.3 | 0.035 | 16/47 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.052 | 13/47 (HOP62, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.077 | 12/47 (SNU-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.080 | 18/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.0 | 0.080 | 14/48 (HOP62, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.697×** | -8.3 | 6e-14 | 29/47 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -7.2 | 2e-10 | 29/45 (J82, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -5.7 | 2e-06 | 23/42 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.727×** | -5.2 | 3e-05 | 27/48 (A549, A-172, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.767×** | -4.2 | 0.004 | 23/48 (A498, A-427, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.1 | 0.004 | 24/48 (HS-578T, SW 900, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.784×** | -3.8 | 0.010 | 18/39 (NCI-H1573, J82, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.8 | 0.012 | 19/47 (A549, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -3.7 | 0.015 | 23/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.819×** | -3.3 | 0.058 | 18/47 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.068 | 13/48 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.878× | -3.1 | 0.11 | 13/48 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.880× | -3.0 | 0.12 | 7/48 (C-33 A, A-427, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 76.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 51.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H1573 (line)]] | alt | 90.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0652× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A498 (line)]] | wt | 24.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -11.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 27.1 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.306× (z -9.1) |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0198× (z -31.0) ⚠ cell-cycle shift, explains ~60% of this change |
| [[hTERT-HPNE (line)]] | wt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[J82 (line)]] | alt | 49.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[SNU-1 (line)]] | wt | 83.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A-427 (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -10.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.116× (z -8.6) ⚠ toxic |
| [[C32 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HCT15 (line)]] | alt | 43.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.196× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.159× (z -9.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -10.0) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HT-29 (line)]] | alt | 72.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[LOX-IMVI (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 49.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0657× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTFR1]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[FOXK2]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ZNF250]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GPR89A]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TAF4]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SOCS7]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[MFN1]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ATP7B]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNBP1P1]] | -0.67 | -0.72 / -0.47 | both halves | 2e-05 |  |
| [[ZNF620]] | -0.67 | -0.75 / -0.43 | both halves | 3e-05 |  |
| [[METTL18]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[DZIP3]] | -0.66 | -0.75 / -0.46 | both halves | 3e-05 |  |
| [[PDCL3P4]] | -0.65 | -0.74 / -0.45 | both halves | 3e-05 |  |
| [[LYRM2]] | -0.64 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[SDSL]] | -0.63 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[DARS1]] | -0.62 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[LPXN]] | -0.62 | -0.72 / -0.57 | both halves | 8e-06 |  |
| [[FUNDC1]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[ZFHX2]] | -0.62 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[TEX9]] | -0.62 | -0.67 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMRTA1]] | B | DMRTA1 activity strengthens DCUN1D2's drug response | lines that do not express DMRTA1 (19) vs lines expressing it (30) | the lines without DMRTA1 respond 0.71× as strongly (z diff +0.75); strongest at Panobinostat 0.5 µM: 1.53x vs 1.86x (z diff +1.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC01239, CFAP20DC, NALCN; target measured in part of the lines; artifact flags |
| [[TMCO3]] | C | TMCO3's natural level strengthens DCUN1D2's drug response | TMCO3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.39; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.2, 12.6); signed map (-42.8, 0.4). **Vector** length 90.3, 20.4% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +2.7 | +3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -10.8 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -8.5 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -7.4 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | defective in cullin neddylation 1 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,455,819-113,490,951 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10704, FLJ20092; previously C13orf17 |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PH85](https://www.uniprot.org/uniprotkb/Q6PH85) (DCN1-like protein 2):

> Contributes to the neddylation of all cullins by transferring NEDD8 from N-terminally acetylated NEDD8-conjugating E2s enzyme to different cullin C-terminal domain-RBX complexes and plays an essential role in the regulation of SCF (SKP1-CUL1-F-box protein)-type complexes activity.

**Summary**, from NCBI Gene [55208](https://www.ncbi.nlm.nih.gov/gene/55208):

> Enables cullin family protein binding activity. Involved in positive regulation of protein neddylation. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20328) · Entrez [55208](https://www.ncbi.nlm.nih.gov/gene/55208) · UniProt [Q6PH85](https://www.uniprot.org/uniprotkb/Q6PH85) · Ensembl [ENSG00000150401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150401)

## Data

Gene col 7431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7431); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7431]; `tensor/DDL_lfc|DDL_z.npy` [7431]; `embed/gene_vectors.npy` [7431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7431 or target_col == 7431). Every well: [[DCUN1D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCUN1D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
