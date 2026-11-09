---
symbol: "PSORS1C1"
type: "gene"
col: 12887
ensembl_id: "ENSG00000204540"
name: "psoriasis susceptibility 1 candidate 1"
location: "6p21.33"
module: 31
arm: "+"
pooled_cpm: 20.34
n_lines_expressing: 35
n_dd_up: 3
n_dd_down: 43
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 19
direction_downstream: 22
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PSORS1C1

*psoriasis susceptibility 1 candidate 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Bimiralisib (drug)]] 5 µM: 1.71× (z +3.9, q 0.064, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (21 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.170× (z -24.1, q 0e+00, down in 32 of 33 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.439× (z -15.8, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC13D]] (+0.61, fdr 1e-05), [[ACOT9]] (+0.56, fdr 3e-05), [[ALS2CL]] (+0.56, fdr 1e-05); moves opposite to [[PDE7A]] (-0.56, fdr 3e-05), [[CHD1L]] (-0.56, fdr 4e-05), [[NBAS]] (-0.54, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[C1orf116]] → it (grade B ⚠); 22 go from it, the strongest it → [[BCL2L1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | **1.71×** | +3.9 | 0.064 | 14/33 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.076 | 11/33 (J82, Hs 766T, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.098 | 6/32 (CFPAC-1, PANC-1, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.39× | +3.2 | 0.16 | 8/32 (HEC-1-A, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 1.26× | +3.2 | 0.16 | 6/32 (HOP62, SW1417, …) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.25× | +3.1 | 0.16 | 6/33 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.26× | +3.1 | 0.16 | 11/33 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.26× | +3.1 | 0.16 | 3/33 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.170×** | -24.1 | 0e+00 | 32/33 (LoVo, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.199×** | -22.0 | 0e+00 | 31/32 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.205×** | -21.4 | 0e+00 | 31/33 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.439×** | -15.8 | 0e+00 | 30/33 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.320×** | -15.5 | 0e+00 | 32/33 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.428×** | -11.5 | 2e-28 | 29/32 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.445×** | -11.0 | 4e-26 | 29/32 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.471×** | -9.8 | 8e-21 | 25/32 (LoVo, Panc 03.27, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.498×** | -9.1 | 7e-18 | 25/33 (HEC-1-A, SW48, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.520×** | -8.5 | 8e-16 | 24/31 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.306×** | -8.4 | 2e-15 | 24/33 (LoVo, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.543×** | -8.3 | 7e-15 | 25/32 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.654×** | -8.1 | 2e-14 | 20/33 (HEC-1-A, A549, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.535×** | -8.0 | 5e-14 | 25/33 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.601×** | -6.9 | 2e-10 | 23/31 (LoVo, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -6.4 | 7e-09 | 19/31 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.633×** | -6.1 | 2e-08 | 20/32 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.433×** | -5.9 | 8e-08 | 24/33 (KATO III, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.513×** | -4.7 | 5e-05 | 16/32 (A498, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -4.7 | 5e-05 | 15/32 (SW48, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.560×** | -4.1 | 8e-04 | 14/32 (HEC-1-A, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.561×** | -4.1 | 8e-04 | 17/31 (HEC-1-A, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.568×** | -4.0 | 0.001 | 14/31 (HEC-1-A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.582×** | -3.8 | 0.002 | 14/31 (LS 180, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.75 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 61.9 | 0 | 15 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0516× (z -26.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -14.3) |
| [[LoVo (line)]] | wt | 59.0 | 0 | 15 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0573× (z -24.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.130× (z -17.7) |
| [[LS 180 (line)]] | wt | 48.0 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -16.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 41.4 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -18.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -13.6) |
| [[A549 (line)]] | wt | 27.8 | 0 | 8 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0812× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.4) |
| [[J82 (line)]] | alt | 28.4 | 0 | 8 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.137× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.216× (z -10.7) |
| [[KATO III (line)]] | alt | 54.1 | 0 | 8 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0448× (z -28.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -15.4) |
| [[SW480 (line)]] | alt | 22.1 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -15.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 58.2 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -17.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.255× (z -10.5) |
| [[PANC-1 (line)]] | alt | 13.7 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -14.3) |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0666× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -10.2) |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0455× (z -14.3) |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.0) |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0953× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -14.2) |
| [[A-172 (line)]] | wt | 22.6 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.140× (z -13.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 30.9 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.320× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 33.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -11.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.6) |
| [[A498 (line)]] | wt | 12.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 31.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 17.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.104× (z -8.9) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 7.85 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -10.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.3) |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.4) |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 9.59 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.0866× (z -8.8) |
| [[SW 900 (line)]] | alt | 9.57 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0901× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0840× (z -10.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13D]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ACOT9]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ALS2CL]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZNF674]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLC9A8]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[PDCD6IP-DT]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[C1orf116]] | +0.54 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[CLCF1]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SH2D3A]] | +0.53 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[ZNF431]] | +0.50 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[MST1R]] | +0.50 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ARHGEF5]] | +0.50 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE7A]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[CHD1L]] | -0.56 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[NBAS]] | -0.54 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[MYH10]] | -0.54 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[ALDH18A1]] | -0.52 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[ATRN]] | -0.51 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[CABIN1]] | -0.50 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[TENT4A]] | -0.50 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[PLEKHA8]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[HACE1]] | -0.50 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[CEP170]] | -0.49 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[DCUN1D4]] | -0.49 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf116]] | B | C1orf116 activity raises PSORS1C1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.52× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[FAM83B]] | B | FAM83B activity raises PSORS1C1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.99× lower at baseline in the lines without FAM83B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[ABCC3]] | B | ABCC3 activity raises PSORS1C1's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.16× lower at baseline in the lines without ABCC3 | 0.008 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[B3GNT3]] | B | B3GNT3 activity raises PSORS1C1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without B3GNT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[ANXA3]] | B | ANXA3 activity raises PSORS1C1's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.23× lower at baseline in the lines without ANXA3 | 0.014 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[SDR16C5]] | B | SDR16C5 activity raises PSORS1C1's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without SDR16C5 | 0.015 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[HTR1D]] | B | HTR1D activity raises PSORS1C1's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without HTR1D | 0.020 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[MTOR]] | B | MTOR activity lowers PSORS1C1's level | compounds that target MTOR: 3 of 8 raise it (Bimiralisib, Rapamycin, Temsirolimus) | 38% of the class's compounds vs 0.8% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[KLF5]] | B | KLF5 activity raises PSORS1C1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without KLF5 | 0.024 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[SH2D3A]] | B | SH2D3A activity raises PSORS1C1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.49× lower at baseline in the lines without SH2D3A | 0.032 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[RNF39]] | B | RNF39 activity raises PSORS1C1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.70× lower at baseline in the lines without RNF39 | 0.039 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[ALS2CL]] | B | ALS2CL activity raises PSORS1C1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.96× lower at baseline in the lines without ALS2CL | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2L1-AS1]] | B | PSORS1C1 activity raises BCL2L1-AS1's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without PSORS1C1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[ABCC3]] | B | PSORS1C1 activity raises ABCC3's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.45× lower at baseline in the lines without PSORS1C1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[SDR16C5]] | B | PSORS1C1 activity raises SDR16C5's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 2.53× lower at baseline in the lines without PSORS1C1 | 0.028 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[RNF103-CHMP3]] | B | PSORS1C1 activity raises RNF103-CHMP3's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without PSORS1C1 | 0.031 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[HTR1D]] | B | PSORS1C1 activity raises HTR1D's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.61× lower at baseline in the lines without PSORS1C1 | 0.033 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[ANXA3]] | B | PSORS1C1 activity raises ANXA3's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.25× lower at baseline in the lines without PSORS1C1 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[C1orf116]] | B | PSORS1C1 activity raises C1orf116's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.29× lower at baseline in the lines without PSORS1C1 | 0.042 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[ALS2CL]] | B | PSORS1C1 activity raises ALS2CL's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 2.62× lower at baseline in the lines without PSORS1C1 | 0.051 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[IER5]] | B | PSORS1C1 activity raises IER5's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without PSORS1C1 | 0.053 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[KLF5]] | B | PSORS1C1 activity raises KLF5's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without PSORS1C1 | 0.059 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[FAM83B]] | B | PSORS1C1 activity raises FAM83B's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.01× lower at baseline in the lines without PSORS1C1 | 0.062 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[PLA2R1]] | B | PSORS1C1 activity raises PLA2R1's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 2.22× lower at baseline in the lines without PSORS1C1 | 0.064 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.1, 53.3); signed map (1.7, 35.1). **Vector** length 87.2, 22.1% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.5 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -11.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | -3.6 | -9.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -15.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -8.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | psoriasis susceptibility 1 candidate 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,114,750-31,140,092 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEEK1; previously C6orf16 |
| Matched by | ensembl_id |

UniProt [Q9UIG5](https://www.uniprot.org/uniprotkb/Q9UIG5) carries no function annotation.

**Summary**, from NCBI Gene [170679](https://www.ncbi.nlm.nih.gov/gene/170679):

> This gene is one of several genes thought to confer susceptibility to psoriasis and systemic sclerosis, located on chromosome 6 near the major histocompatibility complex (MHC) class I region. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:17202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17202) · Entrez [170679](https://www.ncbi.nlm.nih.gov/gene/170679) · UniProt [Q9UIG5](https://www.uniprot.org/uniprotkb/Q9UIG5) · Ensembl [ENSG00000204540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204540)

## Data

Gene col 12887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12887); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12887]; `tensor/DDL_lfc|DDL_z.npy` [12887]; `embed/gene_vectors.npy` [12887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12887 or target_col == 12887). Every well: [[PSORS1C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSORS1C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
