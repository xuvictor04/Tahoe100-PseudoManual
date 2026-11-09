---
symbol: "CNIH1"
type: "gene"
col: 1981
ensembl_id: "ENSG00000100528"
name: "cornichon family member 1"
location: "14q22.2"
module: 57
arm: "+"
pooled_cpm: 51.53
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# CNIH1

*cornichon family member 1* — 14q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +14.2, q 5e-43, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.51× (z +6.8, q 1e-09, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.786× (z -5.6, q 1e-05, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.169×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.189×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.479×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLA2G12A]] (+0.71, fdr 7e-06), [[NDRG3]] (+0.66, fdr 7e-06), [[JAM3]] (+0.65, fdr 1e-05); moves opposite to [[PDCD7]] (-0.61, fdr 8e-06), [[UNK]] (-0.59, fdr 1e-05), [[OFD1]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF891]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +14.2 | 5e-43 | 45/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +12.7 | 2e-34 | 36/42 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +10.2 | 2e-22 | 38/45 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +6.8 | 1e-09 | 41/48 (HT-29, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.51×** | +6.7 | 2e-09 | 35/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +6.0 | 2e-07 | 40/48 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 2e-07 | 35/48 (J82, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.7 | 9e-07 | 35/48 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.41×** | +5.7 | 9e-07 | 27/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.42×** | +5.6 | 1e-06 | 34/47 (COLO 205, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.4 | 3e-06 | 32/43 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.0 | 3e-05 | 30/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.8 | 6e-05 | 27/47 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.28×** | +4.0 | 0.002 | 24/47 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +4.0 | 0.003 | 22/49 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.004 | 23/48 (CFPAC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.009 | 20/48 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.034 | 16/48 (NCI-H460, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.036 | 17/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.078 | 7/49 (LS 180, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1981.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.169×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.189×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.479×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.786×** | -5.6 | 1e-05 | 29/48 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.820× | -3.2 | 0.20 | 16/49 (CFPAC-1, AsPC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.820× | -3.1 | 0.20 | 18/47 (C-33 A, RKO, …) | rises with dose | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | 0.698× | -3.1 | 0.20 | 12/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.807× | -3.1 | 0.20 | 19/49 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.701× | -3.1 | 0.20 | 15/49 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 54.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.7) |
| [[PANC-1 (line)]] | alt | 34.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 32.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 47.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 45.0 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.56× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 25.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 51.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 50.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +10.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 42.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 64.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -16.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 67.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.26× (z +10.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +11.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +8.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +8.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 49.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 60.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLA2G12A]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[JAM3]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ATP2C1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[OPA1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MRPS35]] | +0.62 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RAB4A]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.60 | +0.68 / +0.54 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[TOM1L1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD7]] | -0.61 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[UNK]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[OFD1]] | -0.59 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[RSF1]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[RBX1]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SIX5]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[RELB]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[PSME2]] | -0.57 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[RBBP6]] | -0.57 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[BOLA1]] | -0.56 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[ZNF687]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF891]] | B | ZNF891 activity lowers CNIH1's level | lines that do not express ZNF891 (7) vs lines expressing it (43) | 1.49× higher at baseline in the lines without ZNF891 | 0.049 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KMT2D; also absent: ENSG00000256825, ZNF140, CEP126 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.2, -10.6); signed map (-34.8, -14.4). **Vector** length 73.1, 16.8% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | -1.4 | +0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.3 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | cornichon family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.2 — chr14:54,423,561-54,441,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TGAM77, CNIL; previously CNIH |
| Gene groups (HGNC) | Cornichon family |
| Reactome | 7 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; ER to Golgi Anterograde Transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95406](https://www.uniprot.org/uniprotkb/O95406) (Protein cornichon homolog 1):

> Involved in the selective transport and maturation of TGF-alpha family proteins.

**Summary**, from NCBI Gene [10175](https://www.ncbi.nlm.nih.gov/gene/10175):

> Predicted to enable signaling receptor binding activity. Predicted to be involved in immune response and signal transduction. Predicted to be located in ER to Golgi transport vesicle membrane; endoplasmic reticulum membrane; and endoplasmic reticulum-Golgi intermediate compartment membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19431) · Entrez [10175](https://www.ncbi.nlm.nih.gov/gene/10175) · UniProt [O95406](https://www.uniprot.org/uniprotkb/O95406) · Ensembl [ENSG00000100528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100528)

## Data

Gene col 1981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1981); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1981]; `tensor/DDL_lfc|DDL_z.npy` [1981]; `embed/gene_vectors.npy` [1981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1981 or target_col == 1981). Every well: [[CNIH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNIH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
