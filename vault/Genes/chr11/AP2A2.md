---
symbol: "AP2A2"
type: "gene"
col: 11358
ensembl_id: "ENSG00000183020"
name: "adaptor related protein complex 2 subunit alpha 2"
location: "11p15.5"
module: 2
arm: "+"
pooled_cpm: 72.13
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# AP2A2

*adaptor related protein complex 2 subunit alpha 2* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.38× (z +5.9, q 1e-06, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.542× (z -15.8, q 0e+00, down in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 13 lines (LoVo 0.353×, AsPC-1 0.381×, NCI-H2347 0.418×, SW1417 0.405×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.145×, SNU-1 0.127×, SK-MEL-2 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.503×, A-172 0.526×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRLF3]] (+0.75, fdr 7e-06), [[BRF1]] (+0.69, fdr 1e-05), [[TRABD]] (+0.69, fdr 1e-05); moves opposite to [[NFKB1]] (-0.64, fdr 1e-05), [[LPXN]] (-0.63, fdr 4e-05), [[ZNF341-AS1]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +5.9 | 1e-06 | 34/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.9 | 1e-06 | 39/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.5 | 6e-06 | 32/48 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 7e-04 | 25/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.007 | 24/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.007 | 24/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.6 | 0.022 | 21/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +3.3 | 0.061 | 18/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.20× | +3.2 | 0.10 | 19/48 (COLO 205, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.10 | 18/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.12 | 14/49 (NCI-H460, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11358.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 13 lines (LoVo 0.353×, AsPC-1 0.381×, NCI-H2347 0.418×, SW1417 0.405×, …); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.145×, SNU-1 0.127×, SK-MEL-2 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.503×, A-172 0.526×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -15.8 | 0e+00 | 45/49 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -5.0 | 2e-04 | 26/48 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.779×** | -4.6 | 1e-03 | 27/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | 0.849× | -4.2 | 0.003 | 24/48 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.779×** | -4.2 | 0.003 | 24/45 (LOX-IMVI, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.799×** | -4.1 | 0.004 | 23/49 (SNU-1, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.795×** | -4.0 | 0.005 | 25/50 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.797×** | -4.0 | 0.005 | 23/48 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.813×** | -3.8 | 0.010 | 26/48 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.870× | -3.6 | 0.018 | 9/48 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.821×** | -3.5 | 0.026 | 22/43 (LS 180, SNU-1, …) | all doses, flat | composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.848× | -3.0 | 0.12 | 13/48 (SW480, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 84.7 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -11.2) |
| [[LoVo (line)]] | wt | 99.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -19.5) |
| [[LOX-IMVI (line)]] | wt | 77.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.1) |
| [[SW480 (line)]] | alt | 69.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 71.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[AsPC-1 (line)]] | alt | 85.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.2) |
| [[C32 (line)]] | wt | 69.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.0) |
| [[HOP62 (line)]] | alt | 78.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 50.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +22.2) ⚠ cell-cycle shift, explains ~99% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.0) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 53.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.0) ⚠ cell-cycle shift, explains ~99% of this change | [[Dinaciclib (drug)]] 5 µM 0.219× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SNU-1 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SNU-423 (line)]] | alt | 78.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.1) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -10.7) |
| [[Hs 766T (line)]] | wt | 86.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -12.6) |
| [[HS-578T (line)]] | alt | 64.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.4) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 64.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.9) |
| [[J82 (line)]] | alt | 96.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -9.3) |
| [[LS 180 (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[MIA PaCa-2 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 81.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 47.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -10.7) |
| [[PANC-1 (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -9.4) |
| [[SW1417 (line)]] | alt | 68.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -13.6) |
| [[A498 (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 68.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRLF3]] | +0.75 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[BRF1]] | +0.69 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[TRABD]] | +0.69 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[USP35]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[SERAC1]] | +0.69 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[TCF3]] | +0.69 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[MAST3]] | +0.67 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 | pathway: Neuronal System |
| [[ANKRD27]] | +0.67 | +0.77 / +0.46 | both halves | 3e-05 |  |
| [[MYPOP]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[PACC1]] | +0.66 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ST6GALNAC6]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB1]] | -0.64 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[LPXN]] | -0.63 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[ZNF341-AS1]] | -0.61 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[HIVEP2-DT]] | -0.61 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ZBED5]] | -0.59 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.59 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[HIVEP2]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[HELQ]] | -0.59 | -0.69 / -0.36 | both halves | 9e-05 |  |
| [[MCTS1]] | -0.59 | -0.69 / -0.33 | both halves | 1e-04 |  |
| [[ACTR3-AS1]] | -0.59 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[SMIM19]] | -0.58 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ERCC6L2]] | -0.57 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AP2A2's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01239]] | B | LINC01239 activity lowers AP2A2's level | lines that do not express LINC01239 (19) vs lines expressing it (31) | 1.32× higher at baseline in the lines without LINC01239 | 0.099 | ⚠ within organs, on part of the lines; also absent: DMRTA1, ZFPM2-AS1, MIR4500HG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (0.8, 0.7); signed map (-41.7, -7.2). **Vector** length 91.5, 21.2% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.2 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.8 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -5.6 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.0 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 2 subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:924,881-1,012,245 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564D1864, HYPJ, KIAA0899, HIP9; previously CLAPA2, ADTAB |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 2 |
| Reactome | 45 pathways, smallest: Nef Mediated CD8 Down-regulation; Nef Mediated CD4 Down-regulation; WNT5A-dependent internalization of FZD2, FZD5 and ROR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O94973](https://www.uniprot.org/uniprotkb/O94973) (AP-2 complex subunit alpha-2):

> Component of the adaptor protein complex 2 (AP-2). Adaptor protein complexes function in protein transport via transport vesicles in different membrane traffic pathways. Adaptor protein complexes are vesicle coat components and appear to be involved in cargo selection and vesicle formation. AP-2 is involved in clathrin-dependent endocytosis in which cargo proteins are incorporated into vesicles surrounded by clathrin (clathrin-coated vesicles, CCVs) which are destined for fusion with the early …

**Summary**, from NCBI Gene [161](https://www.ncbi.nlm.nih.gov/gene/161):

> The protein encoded by this gene is a subunit of the AP-2 adaptor protein complex, which is involved in linking lipid and protein membrane components with the clathrin lattice. This interaction supports the formation of clathrin-coated vesicles, and the encoded subunit aids in the process by binding polyphosphoinositide-containing lipids in the cell membrane. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:562](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:562) · Entrez [161](https://www.ncbi.nlm.nih.gov/gene/161) · UniProt [O94973](https://www.uniprot.org/uniprotkb/O94973) · Ensembl [ENSG00000183020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183020)

## Data

Gene col 11358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11358); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11358]; `tensor/DDL_lfc|DDL_z.npy` [11358]; `embed/gene_vectors.npy` [11358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11358 or target_col == 11358). Every well: [[AP2A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP2A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
