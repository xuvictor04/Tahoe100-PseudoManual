---
symbol: "SP1"
type: "gene"
col: 11700
ensembl_id: "ENSG00000185591"
name: "Sp1 transcription factor"
location: "12q13.13"
module: 29
arm: "+"
pooled_cpm: 87.8
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SP1

*Sp1 transcription factor* — 12q13.13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.524× (z -10.7, q 8e-24, down in 40 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.737× (z -7.1, q 1e-10, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXJ2]] (+0.63, fdr 3e-05), [[TAPBP]] (+0.57, fdr 3e-05), [[ZNF436]] (+0.57, fdr 6e-04); moves opposite to [[FLNB-AS1]] (-0.56, fdr 2e-04), [[PFDN2]] (-0.56, fdr 6e-05), [[REP15]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 5 µM |  | 1.23× | +3.3 | 0.33 | 18/47 (SNU-423, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.22× | +3.2 | 0.33 | 22/48 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.43 | 20/48 (NCI-H23, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.524×** | -10.7 | 8e-24 | 40/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.535×** | -10.3 | 2e-22 | 46/48 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.553×** | -9.8 | 2e-20 | 46/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.737×** | -7.1 | 1e-10 | 31/48 (COLO 205, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.660×** | -6.9 | 7e-10 | 41/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -6.4 | 2e-08 | 36/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.672×** | -6.3 | 2e-08 | 26/44 (KATO III, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -5.6 | 1e-06 | 1/50 (CHP-212) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.711×** | -5.4 | 4e-06 | 31/47 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.727×** | -5.3 | 8e-06 | 35/48 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -5.0 | 3e-05 | 29/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.815×** | -4.8 | 9e-05 | 26/49 (NCI-H23, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.704×** | -4.5 | 4e-04 | 28/45 (NCI-H460, H4, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.787×** | -4.0 | 0.003 | 28/48 (KATO III, SW 1088, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.793×** | -3.8 | 0.005 | 28/48 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.783×** | -3.8 | 0.005 | 23/48 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.010 | 23/47 (C32, NCI-H460, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.816×** | -3.4 | 0.022 | 21/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.025 | 20/48 (BT-474, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.3 | 0.029 | 22/48 (HOP62, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.030 | 19/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.697×** | -3.2 | 0.030 | 21/48 (CFPAC-1, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.033 | 22/49 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.036 | 20/48 (MIA PaCa-2, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -3.1 | 0.041 | 14/49 (A-427, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 166 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -16.2) |
| [[HOP62 (line)]] | alt | 62.8 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 137 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.3) |
| [[HT-29 (line)]] | alt | 129 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.3) |
| [[SW480 (line)]] | alt | 124 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 102 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 161 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.6) |
| [[A-172 (line)]] | wt | 74.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 89.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[H4 (line)]] | wt | 69.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 66.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 66.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 79.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 91.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.468× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 71.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.377× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.8) |
| [[Hs 766T (line)]] | wt | 85.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 93.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -8.7) |
| [[LS 180 (line)]] | wt | 74.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 70.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H661 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0695× (z -11.0) ⚠ toxic; unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 67.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SNU-1 (line)]] | wt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXJ2]] | +0.63 | +0.46 / +0.64 | both halves | 3e-05 | pathway: Adherens junctions interactions |
| [[TAPBP]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ZNF436]] | +0.57 | +0.22 / +0.65 | both halves | 6e-04 | same gene group |
| [[KAT7]] | +0.57 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[APOBEC3B]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RAB8A]] | +0.52 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[RAB14]] | +0.52 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[LNPEP]] | +0.52 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[CNOT1]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CCP110]] | +0.50 | +0.42 / +0.46 | both halves | 4e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[JADE2]] | +0.50 | +0.23 / +0.55 | both halves | 5e-04 |  |
| [[CHRAC1]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB-AS1]] | -0.56 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[PFDN2]] | -0.56 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[REP15]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MPP3]] | -0.51 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[NDUFB9]] | -0.48 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[DAP3]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SHLD2]] | -0.48 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[RBM25]] | -0.47 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[NSUN5P1-1]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ST6GALNAC6-1]] | -0.46 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[SMS]] | -0.46 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[KBTBD11-OT1-1]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPP4]] | B | DPP4 activity raises SP1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.28× lower at baseline in the lines without DPP4 | 0.044 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[MMP7]] | B | MMP7 activity strengthens SP1's drug response | lines that do not express MMP7 (39) vs lines expressing it (11) | the lines without MMP7 respond 0.81× as strongly (z diff +1.47); strongest at Dinaciclib 5 µM: 0.67x vs 0.48x (z diff +3.6) | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.357). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (18.2, -23.6); signed map (24.1, -19.8). **Vector** length 94.0, 25.3% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.4 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.4 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.0 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.3 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -2.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.6 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | Sp1 transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,380,176-53,416,446 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Sp transcription factors |
| Hallmark sets | P53_PATHWAY |
| Reactome | 43 pathways, smallest: Regulation of CDH11 gene transcription; NFE2L2 regulating tumorigenic genes; Positive Regulation of CDH1 Gene Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P08047](https://www.uniprot.org/uniprotkb/P08047) (Transcription factor Sp1):

> Transcription factor that can activate or repress transcription in response to physiological and pathological stimuli. Binds with high affinity to GC-rich motifs and regulates the expression of a large number of genes involved in a variety of processes such as cell growth, apoptosis, differentiation and immune responses. Highly regulated by post-translational modifications (phosphorylations, sumoylation, proteolytic cleavage, glycosylation and acetylation). Also binds the PDGFR-alpha G-box …

**Summary**, from NCBI Gene [6667](https://www.ncbi.nlm.nih.gov/gene/6667):

> The protein encoded by this gene is a zinc finger transcription factor that binds to GC-rich motifs of many promoters. The encoded protein is involved in many cellular processes, including cell differentiation, cell growth, apoptosis, immune responses, response to DNA damage, and chromatin remodeling. Post-translational modifications such as phosphorylation, acetylation, glycosylation, and proteolytic processing significantly affect the activity of this protein, which can be an activator or a …

**Accessions** — [HGNC:11205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11205) · Entrez [6667](https://www.ncbi.nlm.nih.gov/gene/6667) · UniProt [P08047](https://www.uniprot.org/uniprotkb/P08047) · Ensembl [ENSG00000185591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185591)

## Data

Gene col 11700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11700); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11700]; `tensor/DDL_lfc|DDL_z.npy` [11700]; `embed/gene_vectors.npy` [11700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11700 or target_col == 11700). Every well: [[SP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
