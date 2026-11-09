---
symbol: "TMEM8B"
type: "gene"
col: 5969
ensembl_id: "ENSG00000137103"
name: "transmembrane protein 8B"
location: "9p13.3"
module: 2
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TMEM8B

*transmembrane protein 8B* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +7.6, q 1e-11, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.279× (z -14.5, q 1e-44, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLGL1]] (+0.56, fdr 3e-05), [[QARS1]] (+0.56, fdr 3e-05), [[CCNK]] (+0.54, fdr 3e-05); moves opposite to [[ZBED1]] (-0.54, fdr 2e-04), [[ATXN7L1]] (-0.52, fdr 3e-05), [[RPL7L1]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +7.6 | 1e-11 | 32/45 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +6.8 | 3e-09 | 28/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.7 | 3e-09 | 23/42 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +5.2 | 3e-05 | 21/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +5.0 | 8e-05 | 14/45 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.3 | 0.002 | 3/46 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.012 | 12/40 (A-172, A498, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +3.7 | 0.016 | 6/44 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.38×** | +3.6 | 0.017 | 14/46 (SW480, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.018 | 15/45 (KATO III, HT-29, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.030 | 5/44 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.039 | 15/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.052 | 11/42 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.32×** | +3.2 | 0.059 | 9/42 (MIA PaCa-2, Hs 766T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.062 | 6/42 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.279×** | -14.5 | 1e-44 | 42/45 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.285×** | -14.2 | 1e-43 | 42/44 (J82, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.349×** | -12.0 | 1e-30 | 37/41 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.353×** | -11.8 | 4e-30 | 30/41 (COLO 205, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.355×** | -11.8 | 7e-30 | 37/44 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.540×** | -9.9 | 5e-21 | 29/41 (A549, HT-29, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.556×** | -6.4 | 1e-08 | 19/36 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.559×** | -6.3 | 2e-08 | 23/43 (A549, J82, …) | rises with dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -5.8 | 5e-07 | 24/45 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.609×** | -5.6 | 1e-06 | 21/43 (J82, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.623×** | -5.4 | 4e-06 | 23/45 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.627×** | -5.3 | 6e-06 | 21/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.647×** | -4.9 | 4e-05 | 22/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -4.5 | 3e-04 | 18/33 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.532×** | -3.7 | 0.007 | 13/42 (Hs 766T, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.553×** | -3.5 | 0.016 | 11/38 (LS 180, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.563×** | -3.4 | 0.022 | 11/43 (H4, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.025 | 15/43 (HT-29, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.584×** | -3.2 | 0.041 | 11/39 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.763×** | -3.1 | 0.061 | 11/42 (HCT15, SHP-77, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 9.13 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0776× (z -12.9) |
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0188× (z -17.0) |
| [[PANC-1 (line)]] | alt | 7.60 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -13.0) |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0391× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0805× (z -13.2) |
| [[A549 (line)]] | wt | 9.06 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -10.2) |
| [[HOP62 (line)]] | alt | 7.44 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -10.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.6) |
| [[SW480 (line)]] | alt | 6.14 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0880× (z -12.2) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 6.46 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0748× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 5.78 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0643× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 5.09 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.179× (z -9.1) |
| [[A498 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.248× (z -8.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 5.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0640× (z -9.1) |
| [[C-33 A (line)]] | alt | 9.66 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0650× (z -10.1) |
| [[H4 (line)]] | wt | 11.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0868× (z -8.7) |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -8.9) |
| [[LoVo (line)]] | wt | 5.89 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -8.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 6.63 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -9.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 5.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0342× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 5.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0916× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 8.45 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0579× (z -12.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -8.5) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLGL1]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[QARS1]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CCNK]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[CACNB3]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ABCA2]] | +0.53 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[UNC119]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[MAN1B1]] | +0.52 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[ACBD4]] | +0.52 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[SBF1]] | +0.52 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TESK1]] | +0.51 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[CAPN5]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[WASF2]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED1]] | -0.54 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[ATXN7L1]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[RPL7L1]] | -0.51 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MRPL50]] | -0.50 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[NCOA5]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[CRCP]] | -0.49 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ERVK3-1]] | -0.49 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[JPX]] | -0.48 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ATXN10]] | -0.47 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[STAG1]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[CRADD]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SLC25A13]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.8, -20.3); signed map (-49.8, -11.9). **Vector** length 60.1, 9.40% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.2 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -11.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.1 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 8B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,814,451-35,865,518 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAG-5, NGX6, NGX6a, FP588; previously C9orf127, LINC00950 |
| Gene groups (HGNC) | TMEM8 family |
| Hallmark sets | APICAL_SURFACE, APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NDV4](https://www.uniprot.org/uniprotkb/A6NDV4) (Transmembrane protein 8B):

> May function as a regulator of the EGFR pathway. Probable tumor suppressor which may function in cell growth, proliferation and adhesion.

**Summary**, from NCBI Gene [51754](https://www.ncbi.nlm.nih.gov/gene/51754):

> Involved in cell-matrix adhesion. Located in cell surface and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21427) · Entrez [51754](https://www.ncbi.nlm.nih.gov/gene/51754) · UniProt [A6NDV4](https://www.uniprot.org/uniprotkb/A6NDV4) · Ensembl [ENSG00000137103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137103)

## Data

Gene col 5969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5969); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5969]; `tensor/DDL_lfc|DDL_z.npy` [5969]; `embed/gene_vectors.npy` [5969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5969 or target_col == 5969). Every well: [[TMEM8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
