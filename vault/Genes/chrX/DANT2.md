---
symbol: "DANT2"
type: "gene"
col: 14007
ensembl_id: "ENSG00000235244"
name: "DXZ4 associated non-coding transcript 2, distal"
location: "Xq23"
module: 200
arm: "+"
pooled_cpm: 141.17
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# DANT2

*DXZ4 associated non-coding transcript 2, distal* — Xq23

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.345× (z -31.8, q 0e+00, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLYBL]] (+0.55, fdr 3e-05), [[KLHL13]] (+0.55, fdr 3e-05), [[CENPV]] (+0.54, fdr 4e-05); moves opposite to [[ADD1]] (-0.49, fdr 2e-04), [[GANC]] (-0.46, fdr 2e-04), [[NADSYN1]] (-0.44, fdr 1e-04).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZC3H12B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +3.8 | 0.057 | 15/37 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.19× | +3.6 | 0.057 | 18/38 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.6 | 0.057 | 11/37 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.2 | 0.17 | 5/37 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.20 | 11/37 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.0 | 0.21 | 11/36 (RKO, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.345×** | -31.8 | 0e+00 | 36/37 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.373×** | -29.5 | 0e+00 | 35/38 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.407×** | -19.0 | 0e+00 | 36/37 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.436×** | -17.5 | 0e+00 | 35/37 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.440×** | -16.7 | 0e+00 | 36/39 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.456×** | -16.6 | 0e+00 | 32/37 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.457×** | -16.5 | 0e+00 | 36/37 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.448×** | -16.3 | 0e+00 | 33/37 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.449×** | -16.3 | 0e+00 | 30/33 (C-33 A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -15.3 | 0e+00 | 34/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.487×** | -14.6 | 0e+00 | 36/36 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.503×** | -14.5 | 0e+00 | 37/37 (KATO III, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.520×** | -13.1 | 2e-37 | 31/38 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.521×** | -12.7 | 1e-35 | 27/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.553×** | -12.5 | 2e-34 | 33/37 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -12.1 | 3e-32 | 36/38 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -11.9 | 3e-31 | 32/37 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -11.0 | 1e-26 | 35/37 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.443×** | -9.0 | 6e-18 | 33/37 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.689×** | -7.9 | 9e-14 | 32/37 (PANC-1, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.700×** | -7.1 | 3e-11 | 29/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.810×** | -6.3 | 8e-09 | 23/38 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.769×** | -5.6 | 6e-07 | 26/37 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 290 | 0 | 27 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -43.3) |
| [[LoVo (line)]] | wt | 168 | 0 | 21 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -47.3) |
| [[NCI-H460 (line)]] | wt | 218 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -35.1) |
| [[KATO III (line)]] | alt | 180 | 0 | 19 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -26.6) |
| [[LS 180 (line)]] | wt | 290 | 0 | 19 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -33.5) |
| [[SW48 (line)]] | wt | 282 | 0 | 18 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -26.6) |
| [[RKO (line)]] | wt | 146 | 0 | 16 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0721× (z -27.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.214× (z -17.1) |
| [[SNU-1 (line)]] | wt | 279 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -28.3) |
| [[A498 (line)]] | wt | 176 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -29.0) |
| [[SHP-77 (line)]] | alt | 262 | 0 | 14 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -18.5) |
| [[HCT15 (line)]] | alt | 196 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -17.9) |
| [[HT-29 (line)]] | alt | 198 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -25.3) |
| [[NCI-H1573 (line)]] | alt | 277 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -35.9) |
| [[NCI-H1792 (line)]] | alt | 159 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -45.3) |
| [[A-172 (line)]] | wt | 82.7 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -18.0) |
| [[C-33 A (line)]] | alt | 239 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0543× (z -37.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -13.1) |
| [[HOP62 (line)]] | alt | 91.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -18.8) |
| [[A-427 (line)]] | wt | 192 | 0 | 10 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -16.0) |
| [[A549 (line)]] | wt | 143 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -24.3) |
| [[NCI-H23 (line)]] | alt | 236 | 0 | 10 (6 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -18.7) |
| [[CFPAC-1 (line)]] | alt | 171 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -23.5) |
| [[HEC-1-A (line)]] | alt | 263 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 90.5 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -22.3) |
| [[SK-MEL-2 (line)]] | alt | 168 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -34.2) |
| [[H4 (line)]] | wt | 176 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -19.0) |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -20.8) |
| [[CHP-212 (line)]] | wt | 222 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.215× (z -12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.2) |
| [[SW480 (line)]] | alt | 45.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -11.9) |
| [[COLO 205 (line)]] | alt | 65.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.8) |
| [[SW1417 (line)]] | alt | 61.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.3) |
| [[SNU-423 (line)]] | alt | 53.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -17.3) |
| [[SW 900 (line)]] | alt | 105 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -20.8) |
| [[NCI-H2347 (line)]] | alt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -15.0) |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0781× (z -9.2) |
| [[SW 1271 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.181× (z -9.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 28.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLYBL]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[KLHL13]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[CENPV]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[CCSER1]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZC3H12B]] | +0.52 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[RAPGEF5]] | +0.49 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[WWOX]] | +0.49 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[SERBP1]] | +0.48 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[SFXN4]] | +0.48 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[BCL2]] | +0.48 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[B3GALT1]] | +0.48 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[UTP14A]] | +0.48 | +0.27 / +0.51 | both halves | 3e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADD1]] | -0.49 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[GANC]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[NADSYN1]] | -0.44 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[CENPT]] | -0.43 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[RAB5B]] | -0.43 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[PPP1R7]] | -0.42 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[HECTD3]] | -0.42 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[CEP104]] | -0.42 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[AIDA]] | -0.41 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[TMOD3]] | -0.41 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[CERCAM]] | -0.41 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[TMCO3]] | -0.41 | -0.35 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12B]] | B | DANT2 activity raises ZC3H12B's level | lines that do not express DANT2 (11) vs lines expressing it (39) | 3.41× lower at baseline in the lines without DANT2 | 0.060 | ⚠ within organs, on part of the lines; also absent: DANT1, LRRC36, SGSM1; its own permutation p |

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-26.5, 33.5); signed map (11.4, -12.2). **Vector** length 83.2, 24.2% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.5 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.2 |
| fall | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -16.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -12.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.7 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -6.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | DXZ4 associated non-coding transcript 2, distal |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq23 — chrX:115,694,880-115,969,148 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50862) · Entrez [642776](https://www.ncbi.nlm.nih.gov/gene/642776) · Ensembl [ENSG00000235244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235244)

## Data

Gene col 14007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14007); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14007]; `tensor/DDL_lfc|DDL_z.npy` [14007]; `embed/gene_vectors.npy` [14007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14007 or target_col == 14007). Every well: [[DANT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DANT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
