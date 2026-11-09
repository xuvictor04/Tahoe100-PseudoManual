---
symbol: "CDC42EP3"
type: "gene"
col: 8651
ensembl_id: "ENSG00000163171"
name: "CDC42 effector protein 3"
location: "2p22.2"
module: 151
arm: "+"
pooled_cpm: 48.86
n_lines_expressing: 42
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# CDC42EP3

*CDC42 effector protein 3* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +25.3, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.784× (z -3.7, q 0.090, down in 13 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.340×, SW 1088 0.0753×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.478×, A-172 0.507×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.629×; ⚠ position not correctable); [[Decitabine (drug)]] 0.05 µM in 1 line (HCT15 0.0759×); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.0988×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALM2AKAP2]] (+0.59, fdr 1e-05), [[CAMK4]] (+0.55, fdr 1e-05), [[TBX3]] (+0.53, fdr 2e-05); moves opposite to [[GPR107]] (-0.46, fdr 3e-05), [[ATF6B]] (-0.46, fdr 3e-05), [[UMAD1]] (-0.45, fdr 5e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC00973]] → it (grade B ⚠); 3 go from it, the strongest it → [[ARF6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +25.3 | 0e+00 | 38/40 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.68×** | +20.8 | 0e+00 | 33/40 (SW480, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +16.5 | 0e+00 | 32/40 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +15.0 | 0e+00 | 38/40 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +13.3 | 2e-38 | 34/40 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.84×** | +12.9 | 6e-36 | 32/40 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +12.8 | 9e-36 | 32/40 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +11.5 | 7e-29 | 26/40 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.69×** | +11.1 | 1e-26 | 27/40 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +10.6 | 3e-24 | 33/40 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +10.4 | 1e-23 | 28/41 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +10.3 | 5e-23 | 28/40 (HS-578T, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +9.8 | 5e-21 | 31/40 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.54×** | +9.1 | 5e-18 | 28/40 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.52×** | +8.8 | 6e-17 | 23/40 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +5.7 | 4e-07 | 18/40 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 6e-07 | 18/40 (A498, SK-MEL-2, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 2e-04 | 16/40 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.45×** | +4.1 | 9e-04 | 18/40 (HS-578T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8651.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.340×, SW 1088 0.0753×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HS-578T 0.478×, A-172 0.507×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.629×; ⚠ position not correctable); [[Decitabine (drug)]] 0.05 µM in 1 line (HCT15 0.0759×); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.0988×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.784×** | -3.7 | 0.090 | 13/40 (SW 1271, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.829×** | -3.6 | 0.090 | 13/40 (SW48, HCT15, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.848× | -3.5 | 0.091 | 11/39 (C32, Hs 766T, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.860× | -3.2 | 0.19 | 12/40 (J82, HT-29, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.22 | 8/40 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 104 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +23.2) | [[Binimetinib (drug)]] 5 µM 0.374× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 19.2 | 8 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +18.4) | — |
| [[HS-578T (line)]] | alt | 102 | 6 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.80× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.4) |
| [[A498 (line)]] | wt | 26.8 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 58.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.6) | — |
| [[SW480 (line)]] | alt | 47.4 | 5 | 0 | [[Auranofin (drug)]] 5 µM 6.76× (z +22.1) | — |
| [[A-172 (line)]] | wt | 284 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -8.9) |
| [[A-427 (line)]] | wt | 18.2 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.89× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +15.0) | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.39× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 51.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +14.9) | — |
| [[SW 900 (line)]] | alt | 142 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.25× (z +12.1) | — |
| [[A549 (line)]] | wt | 32.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +16.9) | — |
| [[CFPAC-1 (line)]] | alt | 71.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +19.9) | — |
| [[HOP62 (line)]] | alt | 52.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +17.1) | — |
| [[HT-29 (line)]] | alt | 27.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 10.0× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 23.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.4 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 25.5× (z +14.1) | [[Adagrasib (drug)]] 0.05 µM 0.629× (z -13.4) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 65.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.1) | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0753× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Bestatin (drug)]] 0.05 µM 0.0803× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 43.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.56× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 79.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +11.3) | — |
| [[LoVo (line)]] | wt | 15.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +14.0) | — |
| [[SHP-77 (line)]] | alt | 76.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.87× (z +8.7) | — |
| [[SW48 (line)]] | wt | 16.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 7.64× (z +8.8) | [[Bendamustine (drug)]] 5 µM 0.0988× (z -9.7) |
| [[COLO 205 (line)]] | alt | 21.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0759× (z -11.0) |
| [[J82 (line)]] | alt | 111 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.48× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 54.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 47.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALM2AKAP2]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CAMK4]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TBX3]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PLPP4]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[FRMD6]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[KCTD12]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ARSJ]] | +0.52 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[KITLG]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[PMAIP1]] | +0.50 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[HHEX]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[LINC02930]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[PPP1R14C]] | +0.49 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR107]] | -0.46 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ATF6B]] | -0.46 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[UMAD1]] | -0.45 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PDSS2]] | -0.45 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PIGN]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[SARNP]] | -0.41 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[PARN]] | -0.41 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[UBAC2]] | -0.41 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[NUP133]] | -0.41 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[EMC2]] | -0.41 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[ALDH6A1]] | -0.41 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[LIN52]] | -0.41 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00973]] | B | LINC00973 activity raises CDC42EP3's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 3.00× lower at baseline in the lines without LINC00973 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[PRICKLE2]] | B | PRICKLE2 activity raises CDC42EP3's level | lines that do not express PRICKLE2 (20) vs lines expressing it (30) | 3.08× lower at baseline in the lines without PRICKLE2 | 0.033 | ⚠ within organs, on part of the lines; also absent: SNAI2, STK32A, LINC00973 |
| [[PLPP4]] | B | PLPP4 activity raises CDC42EP3's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without PLPP4 | 0.041 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[CCDC85A]] | B | CCDC85A activity raises CDC42EP3's level | lines that do not express CCDC85A (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without CCDC85A | 0.045 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, SERPINB7, KRT86; maybe low, not absent |
| [[FJX1]] | B | FJX1 activity raises CDC42EP3's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 2.80× lower at baseline in the lines without FJX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[FERMT2]] | B | FERMT2 activity raises CDC42EP3's level | lines that do not express FERMT2 (8) vs lines expressing it (42) | 3.00× lower at baseline in the lines without FERMT2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF512B, HLTF, SIX1 |
| [[GJC1]] | B | GJC1 activity raises CDC42EP3's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 3.00× lower at baseline in the lines without GJC1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARF6]] | B | CDC42EP3 activity raises ARF6's level | lines that do not express CDC42EP3 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CDC42EP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCDC110, C3orf52, KLF12 |
| [[PMAIP1]] | B | CDC42EP3 activity raises PMAIP1's level | lines that do not express CDC42EP3 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without CDC42EP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: CCDC110, C3orf52, KLF12 |
| [[PCNX2]] | B | CDC42EP3 activity raises PCNX2's level | lines that do not express CDC42EP3 (8) vs lines expressing it (42) | 3.14× lower at baseline in the lines without CDC42EP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: CCDC110, C3orf52, KLF12 |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.2, 13.2); signed map (18.1, 39.4). **Vector** length 95.6, 22.7% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +20.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +16.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +3.8 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +5.6 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 effector protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,641,882-37,738,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEP3, UB1, BORG2 |
| Gene groups (HGNC) | CDC42 effector proteins |
| Reactome | 7 pathways, smallest: RHOQ GTPase cycle; MAPK6/MAPK4 signaling; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKI2](https://www.uniprot.org/uniprotkb/Q9UKI2) (Cdc42 effector protein 3):

> Probably involved in the organization of the actin cytoskeleton. May act downstream of CDC42 to induce actin filament assembly leading to cell shape changes. Induces pseudopodia formation in fibroblasts.

**Summary**, from NCBI Gene [10602](https://www.ncbi.nlm.nih.gov/gene/10602):

> This gene encodes a member of a small family of guanosine triphosphate (GTP) metabolizing proteins that contain a CRIB (Cdc42, Rac interactive binding) domain. Members of this family of proteins act as effectors of CDC42 function. The encoded protein is involved in actin cytoskeleton re-organization during cell shape changes, including pseudopodia formation. A pseudogene of this gene is found on chromosome 19. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:16943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16943) · Entrez [10602](https://www.ncbi.nlm.nih.gov/gene/10602) · UniProt [Q9UKI2](https://www.uniprot.org/uniprotkb/Q9UKI2) · Ensembl [ENSG00000163171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163171)

## Data

Gene col 8651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8651); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8651]; `tensor/DDL_lfc|DDL_z.npy` [8651]; `embed/gene_vectors.npy` [8651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8651 or target_col == 8651). Every well: [[CDC42EP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42EP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
