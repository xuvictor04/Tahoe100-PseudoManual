---
symbol: "KATNA1"
type: "gene"
col: 11837
ensembl_id: "ENSG00000186625"
name: "katanin catalytic subunit A1"
location: "6q25.1"
module: 4
arm: "-"
pooled_cpm: 34.74
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KATNA1

*katanin catalytic subunit A1* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.35× (z +18.8, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.607× (z -7.5, q 3e-11, down in 27 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.786× (z -3.6, q 0.053, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MINDY2]] (+0.66, fdr 1e-05), [[FSCN1]] (+0.64, fdr 7e-06), [[ANKRD37]] (+0.64, fdr 2e-05); moves opposite to [[CHCHD3]] (-0.65, fdr 7e-06), [[TMEM33]] (-0.61, fdr 1e-05), [[MRRF]] (-0.59, fdr 4e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +18.8 | 0e+00 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +13.0 | 4e-36 | 42/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.87×** | +9.8 | 3e-20 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +9.5 | 3e-19 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.79×** | +9.1 | 1e-17 | 38/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.78×** | +9.0 | 2e-17 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.65×** | +7.9 | 3e-13 | 39/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +7.2 | 3e-11 | 28/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.9 | 3e-10 | 38/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.56×** | +6.9 | 3e-10 | 32/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.1 | 5e-08 | 30/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 5e-08 | 33/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +5.9 | 2e-07 | 30/48 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.41×** | +5.4 | 3e-06 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +5.0 | 2e-05 | 25/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +4.8 | 6e-05 | 23/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.607×** | -7.5 | 3e-11 | 27/37 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -6.9 | 1e-09 | 30/44 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.786×** | -3.6 | 0.053 | 19/48 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.802×** | -3.5 | 0.069 | 18/47 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.797×** | -3.4 | 0.069 | 18/47 (C32, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.2 | 0.13 | 0/48 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.821× | -3.1 | 0.14 | 10/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.846× | -3.1 | 0.14 | 11/48 (AsPC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.812× | -3.0 | 0.15 | 20/41 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.9 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +18.5) | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 7 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +15.7) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 29.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +15.8) | — |
| [[AsPC-1 (line)]] | alt | 30.5 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 44.0 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 70.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 33.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 50.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -17.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 31.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -12.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +14.6) | — |
| [[AN3 CA (line)]] | alt | 73.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.180× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +15.0) | — |
| [[A549 (line)]] | wt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.192× (z -8.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +8.8) | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.100× (z -10.3) |
| [[J82 (line)]] | alt | 28.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[KATO III (line)]] | alt | 8.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.0) | — |
| [[A-172 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY2]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[FSCN1]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ANKRD37]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[FGFR1OP2]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CDKN2D]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[NARF]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[AAMDC]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[WDR47]] | +0.60 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ATP11B]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TMEM134]] | +0.59 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD3]] | -0.65 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[MRRF]] | -0.59 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[SLC35F6]] | -0.56 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[SARS2]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NUDC]] | -0.55 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[LARP4]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ALG14]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LARP1]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.54 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[SNX19]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[TRRAP]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KATNA1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.4, -35.8); signed map (-23.5, 17.6). **Vector** length 83.2, 20.3% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +13.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +6.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.4 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | katanin catalytic subunit A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,594,873-149,648,972 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | AAA ATPases; Katanin catalytic subunit family |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [O75449](https://www.uniprot.org/uniprotkb/O75449) (Katanin p60 ATPase-containing subunit A1):

> Catalytic subunit of a complex which severs microtubules in an ATP-dependent manner. Microtubule severing may promote rapid reorganization of cellular microtubule arrays and the release of microtubules from the centrosome following nucleation. Microtubule release from the mitotic spindle poles may allow depolymerization of the microtubule end proximal to the spindle pole, leading to poleward microtubule flux and poleward motion of chromosome. Microtubule release within the cell body of neurons …

**Summary**, from NCBI Gene [11104](https://www.ncbi.nlm.nih.gov/gene/11104):

> Microtubules, polymers of alpha and beta tubulin subunits, form the mitotic spindle of a dividing cell and help to organize membranous organelles during interphase. Katanin is a heterodimer that consists of a 60 kDa ATPase (p60 subunit A 1) and an 80 kDa accessory protein (p80 subunit B 1). The p60 subunit acts to sever and disassemble microtubules, while the p80 subunit targets the enzyme to the centrosome. This gene encodes the p80 subunit. This protein is a member of the AAA family of …

**Accessions** — [HGNC:6216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6216) · Entrez [11104](https://www.ncbi.nlm.nih.gov/gene/11104) · UniProt [O75449](https://www.uniprot.org/uniprotkb/O75449) · Ensembl [ENSG00000186625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186625)

## Data

Gene col 11837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11837); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11837]; `tensor/DDL_lfc|DDL_z.npy` [11837]; `embed/gene_vectors.npy` [11837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11837 or target_col == 11837). Every well: [[KATNA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KATNA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
