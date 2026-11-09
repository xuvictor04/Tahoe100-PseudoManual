---
symbol: "CTNNBIP1"
type: "gene"
col: 10940
ensembl_id: "ENSG00000178585"
name: "catenin beta interacting protein 1"
location: "1p36.22"
module: 2
arm: "+"
pooled_cpm: 23.18
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CTNNBIP1

*catenin beta interacting protein 1* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.94× (z +12.8, q 9e-35, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.335× (z -20.4, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRK6]] (+0.61, fdr 1e-05), [[CROCCP3]] (+0.60, fdr 1e-05), [[PPM1F]] (+0.60, fdr 1e-05); moves opposite to [[SYNE1]] (-0.62, fdr 1e-05), [[RBM7]] (-0.60, fdr 2e-05), [[RIPK2-DT]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ETS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +12.8 | 9e-35 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +11.8 | 1e-29 | 37/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +10.5 | 2e-23 | 36/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.8 | 2e-16 | 28/46 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.0 | 4e-10 | 21/35 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.2 | 4e-08 | 22/43 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.32×** | +5.1 | 2e-05 | 19/46 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +4.6 | 3e-04 | 19/48 (HT-29, C32, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +4.3 | 0.001 | 11/44 (HOP62, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.1 | 0.003 | 14/46 (HT-29, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.003 | 5/47 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.017 | 13/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.025 | 9/47 (SW1417, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.20× | +3.4 | 0.027 | 14/48 (LS 180, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.3 | 0.037 | 10/48 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.048 | 7/48 (LoVo, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.335×** | -20.4 | 0e+00 | 43/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.577×** | -15.1 | 0e+00 | 38/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -14.5 | 1e-45 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -14.1 | 7e-43 | 37/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.485×** | -14.0 | 9e-43 | 36/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.336×** | -11.1 | 2e-26 | 35/47 (LS 180, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.603×** | -9.8 | 8e-21 | 33/48 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.380×** | -9.8 | 8e-21 | 35/45 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -9.2 | 2e-18 | 31/45 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -8.7 | 3e-16 | 27/45 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.674×** | -7.6 | 1e-12 | 30/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -6.5 | 5e-09 | 24/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.760×** | -5.3 | 4e-06 | 21/47 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -5.3 | 5e-06 | 20/47 (A-427, C-33 A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -4.4 | 3e-04 | 19/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.678×** | -3.9 | 0.003 | 12/47 (HS-578T, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.824×** | -3.8 | 0.006 | 17/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.867× | -3.4 | 0.018 | 13/48 (C32, COLO 205, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.6 | 2 | 8 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -19.7) |
| [[A-427 (line)]] | wt | 38.5 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0709× (z -21.8) |
| [[SW480 (line)]] | alt | 36.6 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -15.4) |
| [[A549 (line)]] | wt | 13.0 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0537× (z -17.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.170× (z -10.8) |
| [[A498 (line)]] | wt | 10.1 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.1) |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.238× (z -11.3) |
| [[LS 180 (line)]] | wt | 25.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.241× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 44.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.312× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 12.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.7) | [[Harringtonine (drug)]] 0.5 µM 0.274× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.258× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.3) |
| [[COLO 205 (line)]] | alt | 33.4 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0259× (z -11.9) |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -17.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.300× (z -10.1) |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.5) |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -8.9) |
| [[J82 (line)]] | alt | 17.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.6) |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0831× (z -9.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.5) |
| [[SW48 (line)]] | wt | 24.4 | 0 | 2 (1 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.0687× (z -11.7) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.7) |
| [[AN3 CA (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.126× (z -8.7) ⚠ transcription drop |
| [[C32 (line)]] | wt | 43.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.299× (z -8.7) |
| [[H4 (line)]] | wt | 17.1 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0689× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -11.1) |
| [[LoVo (line)]] | wt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.280× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -8.9) |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK6]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CROCCP3]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[INPP5A]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MAP2K1]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CAPN10]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CORO7]] | +0.58 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[FBH1]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[BCL7C]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.58 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[MYO9B]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNE1]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[RBM7]] | -0.60 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[UBQLN2]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[REPIN1]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPH2]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ZNF155]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ARID5B]] | -0.58 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TLR3]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ARHGAP24]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ZNF711]] | -0.57 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZNF317]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS2]] | B | ETS2 activity lowers CTNNBIP1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.51× higher at baseline in the lines without ETS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[ZEB2]] | B | ZEB2 activity lowers CTNNBIP1's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 1.41× higher at baseline in the lines without ZEB2 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16 |
| [[PBX4]] | C | PBX4 activity raises CTNNBIP1's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without PBX4 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-15.9, 7.5); signed map (-44.7, -4.7). **Vector** length 82.9, 17.8% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +12.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +8.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -0.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.2 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -14.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -20.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | catenin beta interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,848,276-9,910,336 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ICAT, MGC15093 |
| Reactome | 3 pathways, smallest: Deactivation of the beta-catenin transactivating complex; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSA3](https://www.uniprot.org/uniprotkb/Q9NSA3) (Beta-catenin-interacting protein 1):

> Prevents the interaction between CTNNB1 and TCF family members, and acts as a negative regulator of the Wnt signaling pathway.

**Summary**, from NCBI Gene [56998](https://www.ncbi.nlm.nih.gov/gene/56998):

> The protein encoded by this gene binds CTNNB1 and prevents interaction between CTNNB1 and TCF family members. The encoded protein is a negative regulator of the Wnt signaling pathway. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16913) · Entrez [56998](https://www.ncbi.nlm.nih.gov/gene/56998) · UniProt [Q9NSA3](https://www.uniprot.org/uniprotkb/Q9NSA3) · Ensembl [ENSG00000178585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178585)

## Data

Gene col 10940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10940); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10940]; `tensor/DDL_lfc|DDL_z.npy` [10940]; `embed/gene_vectors.npy` [10940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10940 or target_col == 10940). Every well: [[CTNNBIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNNBIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
