---
symbol: "ZMYM3"
type: "gene"
col: 7152
ensembl_id: "ENSG00000147130"
name: "zinc finger MYM-type containing 3"
location: "Xq13.1"
module: 29
arm: "+"
pooled_cpm: 15.57
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 35
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ZMYM3

*zinc finger MYM-type containing 3* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.1, q 0.020, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.55×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.346× (z -16.2, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF8]] (+0.66, fdr 7e-06), [[MDH1]] (+0.64, fdr 9e-06), [[RBBP9]] (+0.64, fdr 1e-05); moves opposite to [[CDR2]] (-0.61, fdr 1e-05), [[LINC02804]] (-0.61, fdr 1e-05), [[C19orf25]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.55×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.020 | 18/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.6 | 0.064 | 7/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.064 | 18/48 (PANC-1, C32, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 1.77× | +3.2 | 0.16 | 8/44 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.34× | +3.2 | 0.16 | 16/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.22× | +3.1 | 0.19 | 17/48 (KATO III, AsPC-1, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.346×** | -16.2 | 0e+00 | 42/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.283×** | -13.6 | 2e-39 | 45/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.292×** | -13.2 | 9e-38 | 38/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.343×** | -11.5 | 2e-28 | 43/47 (SNU-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -11.0 | 3e-26 | 39/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.398×** | -9.9 | 4e-21 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.402×** | -9.8 | 9e-21 | 46/47 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.417×** | -9.0 | 1e-17 | 35/48 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.436×** | -8.9 | 3e-17 | 44/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -8.8 | 7e-17 | 39/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.476×** | -8.0 | 7e-14 | 37/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.482×** | -7.8 | 2e-13 | 39/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.504×** | -6.9 | 2e-10 | 36/48 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.554×** | -6.4 | 9e-09 | 37/47 (HT-29, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.558×** | -6.3 | 1e-08 | 33/47 (SW480, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -5.2 | 8e-06 | 28/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.676×** | -4.2 | 8e-04 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.781×** | -3.7 | 0.004 | 22/48 (MIA PaCa-2, A-427, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0454× (z -19.6) |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -16.4) |
| [[SW480 (line)]] | alt | 28.8 | 0 | 9 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 1 (1 ⚠) | 6 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.55× (z +9.2) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0615× (z -16.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.168× (z -15.5) |
| [[C32 (line)]] | wt | 16.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0405× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.197× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.154× (z -9.8) |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.9) |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0594× (z -11.4) |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.6) |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0977× (z -12.5) |
| [[J82 (line)]] | alt | 14.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -11.2) |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.7) |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0423× (z -13.1) |
| [[A-172 (line)]] | wt | 17.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.2) |
| [[LoVo (line)]] | wt | 8.10 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0392× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 8.97 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -10.0) |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -13.0) |
| [[A-427 (line)]] | wt | 18.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -10.8) |
| [[A498 (line)]] | wt | 9.33 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.7) |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0490× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 5.82 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0350× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.0) |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.157× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.5) |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.1) |
| [[HS-578T (line)]] | alt | 7.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0728× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -9.8) |
| [[KATO III (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 7.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0418× (z -16.1) |
| [[RKO (line)]] | wt | 10.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.8) |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF8]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MDH1]] | +0.64 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[RBBP9]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[COPS6]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CNOT1]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TAF6]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PFKM]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ATP5F1A]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[EHMT2]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ATP5F1B]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[TSPAN6]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDR2]] | -0.61 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[LINC02804]] | -0.61 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[UBE2CP5]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[MAFG]] | -0.56 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.55 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[XIAP]] | -0.54 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[ZNF83]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[C11orf91]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FBXO10]] | -0.53 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[ZBTB7A]] | -0.53 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity lowers ZMYM3's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.51× higher at baseline in the lines without C11orf91 | 0.094 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[SLC44A2]] | C | SLC44A2 activity raises ZMYM3's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without SLC44A2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.5, -17.8); signed map (-19.4, -41.3). **Vector** length 76.4, 17.4% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +3.0 |
|  | [[NG25 (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.6 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | -3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.7 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -13.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.8 | -6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYM-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,239,624-71,255,146 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF198L2, DXS6673E, KIAA0385, MYM; previously ZNF261 |
| Gene groups (HGNC) | Zinc fingers MYM-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14202](https://www.uniprot.org/uniprotkb/Q14202) (Zinc finger MYM-type protein 3):

> Required for regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [9203](https://www.ncbi.nlm.nih.gov/gene/9203):

> This gene is located on the X chromosome and is subject to X inactivation. It is highly conserved in vertebrates and most abundantly expressed in the brain. The encoded protein is a component of histone deacetylase-containing multiprotein complexes that function through modifying chromatin structure to keep genes silent. A chromosomal translocation (X;13) involving this gene is associated with X-linked cognitive disability. Several alternatively spliced transcript variants have been found for …

**Accessions** — [HGNC:13054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13054) · Entrez [9203](https://www.ncbi.nlm.nih.gov/gene/9203) · UniProt [Q14202](https://www.uniprot.org/uniprotkb/Q14202) · Ensembl [ENSG00000147130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147130)

## Data

Gene col 7152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7152); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7152]; `tensor/DDL_lfc|DDL_z.npy` [7152]; `embed/gene_vectors.npy` [7152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7152 or target_col == 7152). Every well: [[ZMYM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
