---
symbol: "IL20RB"
type: "gene"
col: 10503
ensembl_id: "ENSG00000174564"
name: "interleukin 20 receptor subunit beta"
location: "3q22.3"
module: 47
arm: "+"
pooled_cpm: 26.73
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# IL20RB

*interleukin 20 receptor subunit beta* — 3q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.316× (z -13.1, q 1e-36, down in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -8.6, q 6e-16, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL4]] (+0.70, fdr 7e-06), [[LINC02803]] (+0.70, fdr 7e-06), [[CHRNA10]] (+0.70, fdr 1e-05); moves opposite to [[BPHL]] (-0.51, fdr 2e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPRC5D-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MINAR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.4 | 3e-05 | 4/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.316×** | -13.1 | 1e-36 | 41/47 (SW 900, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.370×** | -13.0 | 3e-36 | 40/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.518×** | -12.2 | 8e-32 | 33/47 (A-427, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.458×** | -10.2 | 2e-22 | 38/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.477×** | -9.0 | 4e-17 | 30/38 (KATO III, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.457×** | -8.9 | 4e-17 | 23/33 (KATO III, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.509×** | -8.9 | 7e-17 | 31/42 (LoVo, NCI-H1792, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -8.6 | 6e-16 | 32/47 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.514×** | -7.6 | 2e-12 | 33/43 (KATO III, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.562×** | -7.6 | 2e-12 | 35/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -7.1 | 5e-11 | 34/47 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.544×** | -6.9 | 2e-10 | 31/46 (LoVo, LS 180, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -6.7 | 7e-10 | 30/48 (Panc 03.27, BT-474, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.617×** | -6.3 | 1e-08 | 34/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.417×** | -6.0 | 8e-08 | 32/48 (NCI-H1573, SW 900, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -5.2 | 7e-06 | 26/47 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -4.4 | 3e-04 | 23/46 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.809×** | -3.9 | 0.002 | 20/48 (CHP-212, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.737×** | -3.7 | 0.006 | 22/46 (SW480, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.011 | 14/47 (CFPAC-1, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.013 | 20/47 (NCI-H661, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.731×** | -2.9 | 0.071 | 12/47 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.805×** | -2.8 | 0.094 | 9/48 (NCI-H661, A549, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.783×** | -2.8 | 0.096 | 15/47 (SW 1088, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.782×** | -2.8 | 0.096 | 14/46 (Panc 03.27, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 97.6 | 0 | 13 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0450× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 30.7 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.9) |
| [[H4 (line)]] | wt | 64.9 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0919× (z -16.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -9.8) |
| [[LoVo (line)]] | wt | 36.0 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0497× (z -25.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.5) |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.132× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 40.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW 900 (line)]] | alt | 23.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -11.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 18.8 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.193× (z -13.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.136× (z -11.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -16.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 18.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 50.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -13.0) |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.153× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 35.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -16.6) |
| [[AsPC-1 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.240× (z -8.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.113× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.8) |
| [[A549 (line)]] | wt | 18.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.8) |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.155× (z -8.9) |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.149× (z -8.6) |
| [[HT-29 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[J82 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0688× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -9.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RPMI-7951 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0673× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0921× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL4]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.70 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[EPHX3]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[RAPSN]] | +0.69 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[FLACC1]] | +0.68 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[SLC22A13]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TVP23C-CDRT4]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[SLC22A14]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[CDRT4]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPHL]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5D-AS1]] | B | GPRC5D-AS1 activity raises IL20RB's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without GPRC5D-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MINAR1]] | C | IL20RB's natural level strengthens MINAR1's drug response | IL20RB's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.36; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.5, -15.2); signed map (16.1, 8.6). **Vector** length 86.1, 20.4% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.4 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.7 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -4.1 | -8.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.9 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.8 | -13.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 20 receptor subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:136,946,230-137,011,085 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIRS1, IL-20R2, MGC34923; previously FNDC6 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Interleukin receptors |
| Reactome | 3 pathways, smallest: Interleukin-20 family signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXL0](https://www.uniprot.org/uniprotkb/Q6UXL0) (Interleukin-20 receptor subunit beta):

> The IL20RA/IL20RB dimer is a receptor for IL19, IL20 and IL24. The IL22RA1/IL20RB dimer is a receptor for IL20 and IL24.

**Summary**, from NCBI Gene [53833](https://www.ncbi.nlm.nih.gov/gene/53833):

> IL20RB and IL20RA (MIM 605620) form a heterodimeric receptor for interleukin-20 (IL20; MIM 605619) (Blumberg et al., 2001 [PubMed 11163236]).[supplied by OMIM, Feb 2009]

**Accessions** — [HGNC:6004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6004) · Entrez [53833](https://www.ncbi.nlm.nih.gov/gene/53833) · UniProt [Q6UXL0](https://www.uniprot.org/uniprotkb/Q6UXL0) · Ensembl [ENSG00000174564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174564)

## Data

Gene col 10503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10503); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10503]; `tensor/DDL_lfc|DDL_z.npy` [10503]; `embed/gene_vectors.npy` [10503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10503 or target_col == 10503). Every well: [[IL20RB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL20RB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
