---
symbol: "GGH"
type: "gene"
col: 6035
ensembl_id: "ENSG00000137563"
name: "gamma-glutamyl hydrolase"
location: "8q12.3"
module: 67
arm: "+"
pooled_cpm: 31.82
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 16
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# GGH

*gamma-glutamyl hydrolase* — 8q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.80× (z +15.3, q 0e+00, up in 37 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +4.5, q 4e-04, up in 26 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.574× (z -6.3, q 1e-07, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM106C]] (+0.74, fdr 7e-06), [[GUSB]] (+0.70, fdr 7e-06), [[CALM3]] (+0.70, fdr 1e-05); moves opposite to [[EIF3J]] (-0.68, fdr 7e-06), [[TATDN1]] (-0.63, fdr 1e-05), [[ZNF286B]] (-0.62, fdr 4e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); 16 go from it, the strongest it → [[PBK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 13 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.80×** | +15.3 | 0e+00 | 37/38 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.27×** | +13.1 | 1e-36 | 32/32 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.68×** | +10.5 | 2e-23 | 34/36 (C-33 A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.04×** | +8.2 | 3e-14 | 35/43 (PANC-1, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.98×** | +7.9 | 4e-13 | 37/43 (PANC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +7.1 | 2e-10 | 33/42 (HS-578T, NCI-H2347, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.73×** | +6.3 | 2e-08 | 37/43 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.76×** | +6.2 | 3e-08 | 30/39 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.58×** | +5.2 | 1e-05 | 30/43 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.55×** | +4.9 | 6e-05 | 27/43 (A-172, LOX-IMVI, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.7 | 2e-04 | 16/28 (HS-578T, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.5 | 4e-04 | 26/43 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **1.46×** | +4.3 | 6e-04 | 23/40 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.26×** | +3.7 | 0.008 | 24/43 (Panc 03.27, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.058 | 16/43 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.063 | 15/43 (A-172, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6035.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -6.3 | 1e-07 | 29/43 (A-427, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.680×** | -3.7 | 0.047 | 21/43 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.541×** | -3.7 | 0.047 | 20/43 (HOP62, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.053 | 22/43 (H4, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -3.5 | 0.053 | 20/43 (LS 180, H4, …) | all doses, flat | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **0.563×** | -3.4 | 0.058 | 16/43 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.715×** | -3.3 | 0.092 | 16/43 (RPMI-7951, Hs 766T, …) | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | 0.755× | -3.2 | 0.10 | 19/42 (HEC-1-A, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 49.1 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.8) |
| [[LS 180 (line)]] | wt | 38.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.9) |
| [[A-427 (line)]] | wt | 66.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -13.0) |
| [[SW480 (line)]] | alt | 58.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.0) |
| [[A-172 (line)]] | wt | 36.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HOP62 (line)]] | alt | 46.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -9.5) |
| [[HS-578T (line)]] | alt | 56.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A498 (line)]] | wt | 34.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[C32 (line)]] | wt | 48.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2030 (line)]] | alt | 52.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 27.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SW1417 (line)]] | alt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[C-33 A (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.06× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[J82 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LoVo (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.92× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RKO (line)]] | wt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -8.8) |
| [[SW 900 (line)]] | alt | 44.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AN3 CA (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106C]] | +0.74 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[GUSB]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CALM3]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PCLAF]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ITM2C]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TWSG1]] | +0.65 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[TMEM14A]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PBK]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[NRM]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[TK1]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SPC25]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3J]] | -0.68 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[TATDN1]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ZNF286B]] | -0.62 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC2]] | -0.60 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[NIFK]] | -0.60 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[CLDN15]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[JMJD4]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[DNTTIP2]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SURF6]] | -0.56 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[DDX51]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ADRM1]] | -0.56 | -0.59 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises GGH's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without TCF19 | 0.016 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[DPYSL3]] | B | DPYSL3 activity raises GGH's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without DPYSL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[TOP2A]] | B | TOP2A activity lowers GGH's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KATNAL1]] | C | KATNAL1 activity raises GGH's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 3.02× lower at baseline in the lines without KATNAL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17; co-absent with the target |
| [[PBK]] | C | PBK activity raises GGH's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.02× lower at baseline in the lines without PBK | 0.019 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises GGH's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.07× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[POGLUT2]] | C | POGLUT2 activity raises GGH's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | B | GGH activity raises PBK's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without GGH | 0.018 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[TMEM245]] | B | GGH activity raises TMEM245's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without GGH | 0.036 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[ZNF621]] | B | GGH activity raises ZNF621's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.54× lower at baseline in the lines without GGH | 0.047 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[PSIP1]] | B | GGH activity raises PSIP1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without GGH | 0.048 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[MDH1]] | B | GGH activity raises MDH1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without GGH | 0.054 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[RPA1]] | B | GGH activity raises RPA1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without GGH | 0.055 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[SPC24]] | B | GGH activity raises SPC24's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without GGH | 0.067 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[ALDH7A1]] | B | GGH activity raises ALDH7A1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without GGH | 0.069 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[MELK]] | B | GGH activity raises MELK's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.61× lower at baseline in the lines without GGH | 0.077 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[SKP2]] | B | GGH activity raises SKP2's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without GGH | 0.079 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[ZC3H8]] | B | GGH activity raises ZC3H8's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without GGH | 0.091 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[PRDX3]] | B | GGH activity raises PRDX3's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.25× lower at baseline in the lines without GGH | 0.092 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.6, -38.9); signed map (-29.9, -38.2). **Vector** length 82.1, 21.6% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 12); *Mitotic Prometaphase* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.8 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | gamma-glutamyl hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.3 — chr8:63,014,881-63,039,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GATD10 |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92820](https://www.uniprot.org/uniprotkb/Q92820) (Gamma-glutamyl hydrolase):

> Hydrolyzes the polyglutamate sidechains of pteroylpolyglutamates. Progressively removes gamma-glutamyl residues from pteroylpoly-gamma-glutamate to yield pteroyl-alpha-glutamate (folic acid) and free glutamate. May play an important role in the bioavailability of dietary pteroylpolyglutamates and in the metabolism of pteroylpolyglutamates and antifolates.

**Summary**, from NCBI Gene [8836](https://www.ncbi.nlm.nih.gov/gene/8836):

> This gene catalyzes the hydrolysis of folylpoly-gamma-glutamates and antifolylpoly-gamma-glutamates by the removal of gamma-linked polyglutamates and glutamate. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4248) · Entrez [8836](https://www.ncbi.nlm.nih.gov/gene/8836) · UniProt [Q92820](https://www.uniprot.org/uniprotkb/Q92820) · Ensembl [ENSG00000137563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137563)

## Data

Gene col 6035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6035); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6035]; `tensor/DDL_lfc|DDL_z.npy` [6035]; `embed/gene_vectors.npy` [6035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6035 or target_col == 6035). Every well: [[GGH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
