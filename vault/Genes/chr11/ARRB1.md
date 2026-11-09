---
symbol: "ARRB1"
type: "gene"
col: 6019
ensembl_id: "ENSG00000137486"
name: "arrestin beta 1"
location: "11q13.4"
module: 14
arm: "+"
pooled_cpm: 29.67
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 45
n_dd_up_clean: 10
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ARRB1

*arrestin beta 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +5.9, q 2e-06, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.446× (z -20.9, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISOC1]] (+0.58, fdr 1e-05), [[ANO9]] (+0.53, fdr 3e-05), [[SEMA6B]] (+0.52, fdr 2e-05); moves opposite to [[PIGG]] (-0.51, fdr 3e-05), [[RUBCN]] (-0.49, fdr 6e-05), [[PRR14L]] (-0.49, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[C1orf226]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.9 | 2e-06 | 25/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +5.7 | 3e-06 | 24/47 (NCI-H1573, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.5 | 9e-06 | 23/47 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.3 | 2e-05 | 18/47 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +4.9 | 1e-04 | 20/47 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 6e-04 | 20/47 (NCI-H1573, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Artesunate (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.011 | 10/47 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.8 | 0.011 | 11/47 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.013 | 9/46 (LS 180, C32, …) | inconsistent across doses | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.017 | 10/45 (A549, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.059 | 16/45 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.092 | 6/47 (PANC-1, AsPC-1, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.092 | 6/46 (KATO III, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -20.9 | 0e+00 | 42/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.442×** | -14.4 | 3e-44 | 35/46 (RKO, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.494×** | -12.9 | 9e-36 | 36/47 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.486×** | -12.7 | 8e-35 | 39/47 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.519×** | -12.0 | 5e-31 | 41/47 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -10.1 | 8e-22 | 37/47 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.594×** | -9.5 | 1e-19 | 34/46 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.624×** | -8.6 | 5e-16 | 29/47 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -8.4 | 2e-15 | 28/46 (NCI-H1573, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.639×** | -8.2 | 2e-14 | 29/46 (SW480, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.664×** | -7.5 | 4e-12 | 24/46 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.672×** | -7.3 | 2e-11 | 30/47 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.691×** | -6.7 | 7e-10 | 27/47 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -6.4 | 7e-09 | 29/47 (SW480, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.706×** | -6.3 | 9e-09 | 26/42 (C32, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.518×** | -6.3 | 1e-08 | 26/46 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.671×** | -6.3 | 1e-08 | 25/47 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.550×** | -5.7 | 3e-07 | 28/47 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -5.4 | 2e-06 | 22/45 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.745×** | -5.4 | 2e-06 | 23/46 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -5.3 | 3e-06 | 23/46 (PANC-1, C32, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.576×** | -5.3 | 3e-06 | 23/45 (PANC-1, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.586×** | -5.1 | 8e-06 | 23/45 (PANC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -13.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 36.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 25.3 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0819× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -14.1) |
| [[PANC-1 (line)]] | alt | 54.9 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -15.1) |
| [[C32 (line)]] | wt | 38.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 23.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0537× (z -16.2) |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 25.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -11.9) |
| [[HCT15 (line)]] | alt | 49.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.6) |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -13.5) |
| [[HT-29 (line)]] | alt | 43.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -13.0) |
| [[J82 (line)]] | alt | 23.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.6) |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[RKO (line)]] | wt | 27.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0701× (z -17.3) |
| [[SNU-1 (line)]] | wt | 60.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.192× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~57% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.357× (z -10.1) |
| [[SW1417 (line)]] | alt | 34.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 32.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.9) |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0700× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -11.0) |
| [[HOP62 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.125× (z -8.6) |
| [[LoVo (line)]] | wt | 24.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0527× (z -15.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 52.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.282× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.191× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 58.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.1) |
| [[SW 900 (line)]] | alt | 36.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.6) |
| [[SW48 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.233× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 25.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -8.5) |
| [[A-172 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISOC1]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 | same gene group |
| [[ANO9]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SEMA6B]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ZNF592]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MTARC2]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[NFIX]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[BCOR]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TSPAN15]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SSH2]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[AMOT]] | +0.51 | +0.47 / +0.47 | both halves | 2e-05 | same gene group |
| [[ECH1]] | +0.51 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[CGN]] | +0.50 | +0.42 / +0.52 | both halves | 4e-05 | pathway: Signaling by TGFB family members |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGG]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RUBCN]] | -0.49 | -0.38 / -0.45 | both halves | 6e-05 | same gene group |
| [[PRR14L]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[VTI1A]] | -0.48 | -0.37 / -0.47 | both halves | 8e-05 | same gene group |
| [[SENP5]] | -0.48 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[ZFC3H1]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[FBH1]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[FAM120B]] | -0.45 | -0.32 / -0.46 | both halves | 2e-04 | same gene group |
| [[SZT2]] | -0.43 | -0.43 / -0.34 | both halves | 1e-04 | same gene group |
| [[VPS53]] | -0.43 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[MEF2B]] | -0.43 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[CA5B]] | -0.43 | -0.36 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf226]] | B | C1orf226 activity raises ARRB1's level | lines that do not express C1orf226 (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without C1orf226 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, EPS8L2, EEPD1; maybe low, not absent |
| [[NOS1AP]] | B | NOS1AP activity raises ARRB1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without NOS1AP | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[SORL1]] | B | SORL1 activity raises ARRB1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without SORL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[KREMEN2]] | B | KREMEN2 activity raises ARRB1's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without KREMEN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.5, 2.1); signed map (46.4, 4.6). **Vector** length 93.4, 22.0% of its response variance represented; |z| ≥ 3 in 1,367 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.3 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.9 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +4.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -10.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -14.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -20.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -12.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | arrestin beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:75,260,122-75,351,705 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARR1 |
| Gene groups (HGNC) | Classical arrestins; MicroRNA protein coding host genes |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 37 pathways, smallest: TGFBR3 regulates TGF-beta signaling; Activation of SMO; Thrombin signalling through proteinase activated receptors (PARs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P49407](https://www.uniprot.org/uniprotkb/P49407) (Beta-arrestin-1):

> Functions in regulating agonist-mediated G protein-coupled receptor (GPCR) signaling by mediating both receptor desensitization and resensitization processes. During homologous desensitization, beta-arrestins bind to the GPCR-phosphorylated receptor and sterically preclude its coupling to the cognate G protein; the binding appears to require additional receptor determinants exposed only in the active receptor conformation. The beta-arrestins target many receptors for internalization by acting …

**Summary**, from NCBI Gene [408](https://www.ncbi.nlm.nih.gov/gene/408):

> Members of arrestin/beta-arrestin protein family are thought to participate in agonist-mediated desensitization of G-protein-coupled receptors and cause specific dampening of cellular responses to stimuli such as hormones, neurotransmitters, or sensory signals. Arrestin beta 1 is a cytosolic protein and acts as a cofactor in the beta-adrenergic receptor kinase (BARK) mediated desensitization of beta-adrenergic receptors. Besides the central nervous system, it is expressed at high levels in …

**Accessions** — [HGNC:711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:711) · Entrez [408](https://www.ncbi.nlm.nih.gov/gene/408) · UniProt [P49407](https://www.uniprot.org/uniprotkb/P49407) · Ensembl [ENSG00000137486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137486)

## Data

Gene col 6019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6019); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6019]; `tensor/DDL_lfc|DDL_z.npy` [6019]; `embed/gene_vectors.npy` [6019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6019 or target_col == 6019). Every well: [[ARRB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
