---
symbol: "MAGI2"
type: "gene"
col: 11911
ensembl_id: "ENSG00000187391"
name: "membrane associated guanylate kinase, WW and PDZ domain containing 2"
location: "7q21.11"
module: 121
arm: "+"
pooled_cpm: 178.67
n_lines_expressing: 20
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 19
direction_downstream: 16
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# MAGI2

*membrane associated guanylate kinase, WW and PDZ domain containing 2* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +12.6, q 1e-33, up in 2 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.370× (z -14.5, q 1e-44, down in 17 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGI2-AS3]] (+0.77, fdr 1e-05, ⚠ same locus), [[MIR548XHG]] (+0.67, fdr 7e-06), [[RBMS3]] (+0.66, fdr 7e-06), [[LINC01435]] (+0.66, fdr 7e-06); moves opposite to [[ALG6]] (-0.52, fdr 1e-05), [[RALGPS1]] (-0.51, fdr 6e-05), [[TTC13]] (-0.50, fdr 2e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[HAS2-AS1]] → it (grade B ⚠); 16 go from it, the strongest it → [[NR2F2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +12.6 | 1e-33 | 2/19 (A-172, H4) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +11.7 | 5e-29 | 13/18 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +7.5 | 1e-11 | 0/19 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.0 | 3e-07 | 5/18 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +5.8 | 7e-07 | 13/18 (A-172, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.5 | 7e-04 | 0/17 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.4 | 0.001 | 9/18 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.003 | 13/18 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.004 | 8/18 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.006 | 10/18 (A-172, PANC-1, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.006 | 5/18 (A-172, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +3.7 | 0.011 | 1/17 (A-172) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.018 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.020 | 0/19 | two highest doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.027 | 0/20 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.039 | 0/18 | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.042 | 7/18 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.370×** | -14.5 | 1e-44 | 17/18 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.428×** | -12.3 | 2e-32 | 17/18 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.465×** | -11.1 | 1e-26 | 18/18 (NCI-H1792, C32, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.541×** | -8.9 | 6e-17 | 16/18 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.628×** | -6.5 | 9e-09 | 16/17 (C32, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.663×** | -6.0 | 2e-07 | 15/18 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.667×** | -5.9 | 3e-07 | 15/18 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.477×** | -5.6 | 1e-06 | 16/19 (HepG2/C3A, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -4.4 | 7e-04 | 17/18 (CFPAC-1, RPMI-7951, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -4.1 | 0.003 | 13/18 (CFPAC-1, CHP-212, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **0.769×** | -3.8 | 0.007 | 1/18 (SW 1088) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.774×** | -3.7 | 0.009 | 0/18 | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.777×** | -3.5 | 0.019 | 10/18 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.027 | 1/17 (NCI-H23) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -3.4 | 0.029 | 6/18 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.801×** | -3.1 | 0.066 | 11/18 (C32, SNU-423, …) | top dose only | plate-row cell shift |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.800×** | -3.1 | 0.071 | 0/18 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 3,067 | 0 | 19 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0459× (z -27.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.135× (z -25.5) |
| [[SNU-423 (line)]] | alt | 805 | 2 | 15 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +18.1) | [[Panobinostat (drug)]] 0.5 µM 0.0628× (z -26.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0654× (z -25.6) |
| [[RPMI-7951 (line)]] | alt | 500 | 2 | 13 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.0517× (z -25.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0736× (z -22.5) |
| [[NCI-H1792 (line)]] | alt | 840 | 0 | 14 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0403× (z -29.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0852× (z -22.5) |
| [[HS-578T (line)]] | alt | 460 | 5 (2 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.109× (z -17.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.126× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 171 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0947× (z -21.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.144× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 484 | 3 (1 ⚠) | 8 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 4.59× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.0818× (z -19.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.119× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 282 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0786× (z -22.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.125× (z -18.2) |
| [[HepG2_C3A (line)]] | wt | 840 | 1 | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.0526× (z -27.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.114× (z -20.6) |
| [[HOP62 (line)]] | alt | 348 | 2 | 8 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 5.96× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.0759× (z -22.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0938× (z -20.5) |
| [[NCI-H460 (line)]] | wt | 75.0 | 5 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.208× (z -13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.288× (z -10.8) |
| [[PANC-1 (line)]] | alt | 205 | 3 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +23.1) | [[Panobinostat (drug)]] 5 µM 0.209× (z -15.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.285× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 346 | 2 | 7 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 5.40× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -19.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.133× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 135 | 4 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +19.5) | [[Panobinostat (drug)]] 5 µM 0.223× (z -12.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.231× (z -11.7) |
| [[A-172 (line)]] | wt | 45.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +22.0) | [[Panobinostat (drug)]] 5 µM 0.285× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 188 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.149× (z -13.7) |
| [[CHP-212 (line)]] | wt | 201 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.130× (z -12.8) |
| [[A-427 (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 27.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 37.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 42.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 43.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 28.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGI2-AS3]] | +0.77 | +0.85 / +0.52 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MIR548XHG]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RBMS3]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LINC01435]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[FLRT2]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[LINC02335]] | +0.63 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[JAM2]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FAP]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[LINC02941]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[LINC02438]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PRRX1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MSR1]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MIR137HG]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG6]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[RALGPS1]] | -0.51 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[TTC13]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[PIK3CB]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 | pathway: Cell-Cell communication |
| [[GK5]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[FAR1]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[POGLUT2]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAS2-AS1]] | B | HAS2-AS1 activity raises MAGI2's level | lines that do not express HAS2-AS1 (10) vs lines expressing it (40) | 4.13× lower at baseline in the lines without HAS2-AS1 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises MAGI2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 12.91× lower at baseline in the lines without MAGI2-AS3 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises MAGI2's level | lines that do not express GYPC (35) vs lines expressing it (15) | 7.06× lower at baseline in the lines without GYPC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises MAGI2's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 7.65× lower at baseline in the lines without CTHRC1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises MAGI2's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 4.57× lower at baseline in the lines without SLC43A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |
| [[JAM2]] | C | JAM2 activity raises MAGI2's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 5.23× lower at baseline in the lines without JAM2 | 0.027 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R; co-absent with the target |
| [[ARMCX1]] | C | ARMCX1 activity raises MAGI2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 5.70× lower at baseline in the lines without ARMCX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |
| [[SOX5]] | C | SOX5 activity raises MAGI2's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 4.81× lower at baseline in the lines without SOX5 | 0.049 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |
| [[DPY19L2]] | C | DPY19L2 activity raises MAGI2's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 5.50× lower at baseline in the lines without DPY19L2 | 0.050 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises MAGI2's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 5.02× lower at baseline in the lines without MSC-AS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises MAGI2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.43× lower at baseline in the lines without FRMD4A | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises MAGI2's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.92× lower at baseline in the lines without PAPPA | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F2-AS1]] | B | MAGI2 activity raises NR2F2-AS1's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without MAGI2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1 |
| [[HAS2-AS1]] | B | MAGI2 activity raises HAS2-AS1's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without MAGI2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1 |
| [[TMEM45A]] | B | MAGI2 activity raises TMEM45A's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 4.05× lower at baseline in the lines without MAGI2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1 |
| [[MAGI2-AS3]] | C | MAGI2 activity raises MAGI2-AS3's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 9.02× lower at baseline in the lines without MAGI2 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[DPY19L2]] | C | MAGI2 activity raises DPY19L2's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 3.76× lower at baseline in the lines without MAGI2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[FLRT2]] | C | MAGI2 activity raises FLRT2's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 5.80× lower at baseline in the lines without MAGI2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[OR9Q1]] | C | MAGI2 activity raises OR9Q1's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 4.31× lower at baseline in the lines without MAGI2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[DNAH11]] | C | MAGI2 activity raises DNAH11's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without MAGI2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[MIR3171HG]] | C | MAGI2 activity raises MIR3171HG's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 4.57× lower at baseline in the lines without MAGI2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[PAPPA]] | C | MAGI2 activity raises PAPPA's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 4.50× lower at baseline in the lines without MAGI2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[APCDD1L-DT]] | C | MAGI2 activity raises APCDD1L-DT's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 4.13× lower at baseline in the lines without MAGI2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[FRMD4A]] | C | MAGI2 activity raises FRMD4A's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 4.56× lower at baseline in the lines without MAGI2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.4, 25.9); signed map (33.8, 40.6). **Vector** length 107, 40.0% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -8.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated guanylate kinase, WW and PDZ domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:78,017,055-79,453,667 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AIP1, ARIP1, KIAA0705, ACVRIP1, MAGI-2 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 2 pathways, smallest: Nephrin family interactions; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UL8](https://www.uniprot.org/uniprotkb/Q86UL8) (Membrane-associated guanylate kinase, WW and PDZ domain-containing protein 2):

> Seems to act as a scaffold molecule at synaptic junctions by assembling neurotransmitter receptors and cell adhesion proteins (By similarity). Plays a role in nerve growth factor (NGF)-induced recruitment of RAPGEF2 to late endosomes and neurite outgrowth (By similarity). May play a role in regulating activin-mediated signaling in neuronal cells (By similarity). Enhances the ability of PTEN to suppress AKT1 activation. Plays a role in receptor-mediated clathrin-dependent endocytosis which is …

**Summary**, from NCBI Gene [9863](https://www.ncbi.nlm.nih.gov/gene/9863):

> The protein encoded by this gene interacts with atrophin-1. Atrophin-1 contains a polyglutamine repeat, expansion of which is responsible for dentatorubral and pallidoluysian atrophy. This encoded protein is characterized by two WW domains, a guanylate kinase-like domain, and multiple PDZ domains. It has structural similarity to the membrane-associated guanylate kinase homologue (MAGUK) family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18957) · Entrez [9863](https://www.ncbi.nlm.nih.gov/gene/9863) · UniProt [Q86UL8](https://www.uniprot.org/uniprotkb/Q86UL8) · Ensembl [ENSG00000187391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187391)

## Data

Gene col 11911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11911); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11911]; `tensor/DDL_lfc|DDL_z.npy` [11911]; `embed/gene_vectors.npy` [11911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11911 or target_col == 11911). Every well: [[MAGI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
