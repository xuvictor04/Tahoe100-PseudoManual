---
symbol: "OGG1"
type: "gene"
col: 3518
ensembl_id: "ENSG00000114026"
name: "8-oxoguanine DNA glycosylase"
location: "3p25.3"
module: 218
arm: "+"
pooled_cpm: 20.48
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# OGG1

*8-oxoguanine DNA glycosylase* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.20× (z +15.5, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.482× (z -13.8, q 3e-40, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A42]] (+0.71, fdr 7e-06), [[GFOD2]] (+0.71, fdr 1e-05), [[TFAP2E]] (+0.67, fdr 9e-06); moves opposite to [[PHACTR2]] (-0.68, fdr 1e-05), [[DECR1]] (-0.66, fdr 1e-05), [[ARMT1]] (-0.64, fdr 1e-05).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +15.5 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +15.2 | 0e+00 | 45/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +10.2 | 3e-22 | 31/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.5 | 7e-06 | 18/44 (HT-29, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.002 | 8/48 (KATO III, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.003 | 7/48 (PANC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.008 | 8/47 (HepG2/C3A, A549, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.053 | 7/47 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.070 | 10/48 (SNU-423, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.073 | 10/48 (SW1417, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.11 | 5/48 (LS 180, NCI-H2347, …) | two highest doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.11 | 2/48 (NCI-H2030, KATO III) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.11× | +3.0 | 0.11 | 2/48 (Hs 766T, SK-MEL-2) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.482×** | -13.8 | 3e-40 | 36/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.645×** | -8.6 | 2e-15 | 30/48 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -7.5 | 1e-11 | 25/47 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -7.2 | 7e-11 | 23/47 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.779×** | -6.9 | 6e-10 | 25/47 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -6.8 | 8e-10 | 25/48 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -6.6 | 3e-09 | 26/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -6.2 | 3e-08 | 20/46 (COLO 205, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.723×** | -5.9 | 3e-07 | 20/39 (SW480, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -5.5 | 2e-06 | 20/48 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.764×** | -5.3 | 7e-06 | 19/47 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.784×** | -4.8 | 9e-05 | 20/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.807×** | -4.2 | 0.001 | 18/47 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.803×** | -4.0 | 0.002 | 16/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.0 | 0.002 | 20/46 (HCT15, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.008 | 14/47 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.6 | 0.010 | 18/47 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.035 | 11/47 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.853× | -3.1 | 0.052 | 13/48 (A-172, A549, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 35.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -11.5) |
| [[A-172 (line)]] | wt | 29.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.236× (z -13.7) |
| [[A498 (line)]] | wt | 23.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.289× (z -10.8) |
| [[A549 (line)]] | wt | 26.2 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.337× (z -8.5) |
| [[SW480 (line)]] | alt | 21.8 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.384× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -20.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H460 (line)]] | wt | 14.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 25.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +9.1) | — |
| [[A-427 (line)]] | wt | 19.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -12.4) |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -9.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -8.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 15.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +8.9) | — |
| [[LoVo (line)]] | wt | 13.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.274× (z -8.5) |
| [[PANC-1 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.1) ⚠ cell-cycle shift, explains ~61% of this change |
| [[RPMI-7951 (line)]] | alt | 37.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.277× (z -8.7) |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -8.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A42]] | +0.71 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[GFOD2]] | +0.71 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TFAP2E]] | +0.67 | +0.57 / +0.77 | both halves | 9e-06 |  |
| [[SPATA33]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ATAT1]] | +0.66 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SH3GL1]] | +0.66 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[SDF2]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | +0.63 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[AP1M1]] | +0.63 | +0.62 / +0.49 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SH2B2]] | +0.62 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[RTN4R]] | +0.62 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHACTR2]] | -0.68 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[DECR1]] | -0.66 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ARMT1]] | -0.64 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[LACTB2]] | -0.63 | -0.56 / -0.24 | both halves | 5e-04 |  |
| [[PARD3B]] | -0.60 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CFL2]] | -0.60 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[RWDD2B]] | -0.60 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[TIA1]] | -0.59 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.59 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.59 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.58 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[THOC7]] | -0.57 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises OGG1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without STARD9 | 0.025 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[ZIM2-AS1]] | B | ZIM2-AS1 activity raises OGG1's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without ZIM2-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[ITGB8]] | B | ITGB8 activity lowers OGG1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.19× higher at baseline in the lines without ITGB8 | 0.050 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[HDAC6]] | B | HDAC6 activity lowers OGG1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises OGG1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MYADM]] | C | MYADM's natural level strengthens OGG1's drug response | MYADM's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.34; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[CFL2]] | C | CFL2 activity raises OGG1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.64× lower at baseline in the lines without CFL2 | 0.093 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.0, -0.1); signed map (-43.8, -2.4). **Vector** length 88.1, 18.1% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +15.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +10.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -13.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | 8-oxoguanine DNA glycosylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,749,944-9,788,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMMH, HOGG1, OGH1, MUTM |
| Gene groups (HGNC) | DNA glycosylases; DNA-(apurinic or apyrimidinic site) lyases |
| Reactome | 14 pathways, smallest: Diseases of Base Excision Repair; APEX1-Independent Resolution of AP Sites via the Single Nucleotide Replacement Pathway; Displacement of DNA glycosylase by APEX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15527](https://www.uniprot.org/uniprotkb/O15527) (N-glycosylase/DNA lyase):

> DNA repair enzyme that incises DNA at 8-oxoG residues. Excises 7,8-dihydro-8-oxoguanine and 2,6-diamino-4-hydroxy-5-N-methylformamidopyrimidine (FAPY) from damaged DNA. Has a beta-lyase activity that nicks DNA 3' to the lesion.

**Summary**, from NCBI Gene [4968](https://www.ncbi.nlm.nih.gov/gene/4968):

> This gene encodes the enzyme responsible for the excision of 8-oxoguanine, a mutagenic base byproduct which occurs as a result of exposure to reactive oxygen. The action of this enzyme includes lyase activity for chain cleavage. Alternative splicing of the C-terminal region of this gene classifies splice variants into two major groups, type 1 and type 2, depending on the last exon of the sequence. Type 1 alternative splice variants end with exon 7 and type 2 end with exon 8. All variants share …

**Accessions** — [HGNC:8125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8125) · Entrez [4968](https://www.ncbi.nlm.nih.gov/gene/4968) · UniProt [O15527](https://www.uniprot.org/uniprotkb/O15527) · Ensembl [ENSG00000114026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114026)

## Data

Gene col 3518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3518); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3518]; `tensor/DDL_lfc|DDL_z.npy` [3518]; `embed/gene_vectors.npy` [3518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3518 or target_col == 3518). Every well: [[OGG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
