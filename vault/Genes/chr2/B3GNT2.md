---
symbol: "B3GNT2"
type: "gene"
col: 9937
ensembl_id: "ENSG00000170340"
name: "UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 2"
location: "2p15"
module: 31
arm: "+"
pooled_cpm: 25.02
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 7
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# B3GNT2

*UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 2* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.47× (z +16.1, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.45× (z +15.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.475× (z -12.8, q 1e-34, down in 23 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 0.779× (z -4.5, q 1e-03, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP15]] (+0.57, fdr 1e-05), [[TSPAN14]] (+0.55, fdr 4e-05), [[STK24]] (+0.55, fdr 4e-05); moves opposite to [[GTF2IRD2]] (-0.51, fdr 4e-05), [[MOK]] (-0.51, fdr 7e-05), [[COPZ1]] (-0.50, fdr 8e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.47×** | +16.1 | 0e+00 | 46/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +15.9 | 0e+00 | 44/48 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +15.8 | 0e+00 | 46/47 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +11.7 | 3e-29 | 34/47 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +11.6 | 4e-29 | 32/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.06×** | +10.4 | 2e-23 | 37/48 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +8.8 | 1e-16 | 33/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +8.3 | 1e-14 | 30/48 (A498, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +8.0 | 1e-13 | 33/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +7.6 | 2e-12 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +7.5 | 2e-12 | 29/47 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +7.2 | 4e-11 | 27/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +7.1 | 7e-11 | 26/47 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +6.9 | 2e-10 | 26/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 1e-09 | 24/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +6.4 | 7e-09 | 25/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.5 | 1e-06 | 21/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9937.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -12.8 | 1e-34 | 23/33 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.492×** | -12.7 | 2e-34 | 29/41 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -4.6 | 6e-04 | 19/37 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.779×** | -4.5 | 1e-03 | 17/45 (C-33 A, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.706×** | -4.4 | 1e-03 | 17/45 (SNU-1, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.032 | 12/44 (HS-578T, A549, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.045 | 12/47 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.831× | -3.1 | 0.15 | 15/46 (SW480, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 23.2 | 4 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.87× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 22.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.65× (z +9.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.62× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 22.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.28× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.229× (z -8.8) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 18.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.14× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 35.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -17.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.27 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.61× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -16.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 19.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +14.7) | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -12.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.125× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 44.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -11.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.6) | — |
| [[A-427 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -13.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 10.5 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0693× (z -8.6) |
| [[HCT15 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +10.5) | — |
| [[LoVo (line)]] | wt | 21.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.356× (z -8.7) |
| [[LS 180 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0747× (z -12.0) |
| [[SW480 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -18.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP15]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TSPAN14]] | +0.55 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[STK24]] | +0.55 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[MYORG]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[DAB2IP]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[RGS19]] | +0.52 | +0.49 / +0.38 | both halves | 6e-05 | same gene group |
| [[CORO2A]] | +0.51 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TMC6]] | +0.51 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ACSL3]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[AGPAT2]] | +0.50 | +0.31 / +0.39 | both halves | 2e-04 |  |
| [[CYTH1]] | +0.49 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[PHF13]] | +0.49 | +0.31 / +0.42 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[MOK]] | -0.51 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[COPZ1]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 | same gene group |
| [[ATM]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[BBOF1]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ODR4]] | -0.45 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[NDUFS1]] | -0.45 | -0.18 / -0.42 | ⚠ not reproduced | 9e-04 |  |
| [[DCAF8]] | -0.45 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[GPALPP1]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[TMEM260]] | -0.44 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[TXNRD2]] | -0.44 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[COG4]] | -0.44 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[DNAJC27-AS1]] | -0.44 | -0.24 / -0.42 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises B3GNT2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without PCDH1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[CRYBG2]] | B | CRYBG2 activity raises B3GNT2's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without CRYBG2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[B3GNT3]] | B | B3GNT3 activity raises B3GNT2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.61× lower at baseline in the lines without B3GNT3 | 0.044 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TMC6]] | B | TMC6 activity raises B3GNT2's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without TMC6 | 0.062 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[EPHA1]] | B | EPHA1 activity raises B3GNT2's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without EPHA1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.475). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.6, 30.5); signed map (-16.1, 39.2). **Vector** length 75.4, 15.1% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +8.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.5 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +11.6 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +2.0 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.0 | -12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.0 | +5.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -0.2 |
|  | [[Tolcapone (drug)]] 5 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:62,196,115-62,224,731 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B3GNT-2, BETA3GNT, B3GN-T2, B3GN-T1; previously B3GNT1 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Keratan sulfate biosynthesis; Keratan sulfate/keratin metabolism; O-linked glycosylation of mucins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY97](https://www.uniprot.org/uniprotkb/Q9NY97) (N-acetyllactosaminide beta-1,3-N-acetylglucosaminyltransferase 2):

> Beta-1,3-N-acetylglucosaminyltransferase involved in the synthesis of poly-N-acetyllactosamine. Catalyzes the initiation and elongation of poly-N-acetyllactosamine chains. Shows a marked preference for Gal(beta1-4)Glc(NAc)-based acceptors. Probably constitutes the main polylactosamine synthase.

**Summary**, from NCBI Gene [10678](https://www.ncbi.nlm.nih.gov/gene/10678):

> This gene encodes a member of the beta-1,3-N-acetylglucosaminyltransferase family. This enzyme is a type II transmembrane protein. It prefers the substrate of lacto-N-neotetraose, and is involved in the biosynthesis of poly-N-acetyllactosamine chains. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:15629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15629) · Entrez [10678](https://www.ncbi.nlm.nih.gov/gene/10678) · UniProt [Q9NY97](https://www.uniprot.org/uniprotkb/Q9NY97) · Ensembl [ENSG00000170340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170340)

## Data

Gene col 9937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9937); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9937]; `tensor/DDL_lfc|DDL_z.npy` [9937]; `embed/gene_vectors.npy` [9937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9937 or target_col == 9937). Every well: [[B3GNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
