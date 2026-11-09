---
symbol: "MTCH2"
type: "gene"
col: 3093
ensembl_id: "ENSG00000109919"
name: "mitochondrial carrier 2"
location: "11p11.2"
module: 28
arm: "+"
pooled_cpm: 55.62
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MTCH2

*mitochondrial carrier 2* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +14.7, q 0e+00, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.84× (z +12.9, q 7e-36, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0654×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.347×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.477×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1B]] (+0.60, fdr 7e-06), [[ZBTB25]] (+0.59, fdr 1e-05), [[NIPSNAP2]] (+0.58, fdr 1e-05); moves opposite to [[DNAJB6]] (-0.54, fdr 1e-05), [[DEDD2]] (-0.51, fdr 3e-05), [[PDCL]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.64×** | +14.7 | 0e+00 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +12.9 | 7e-36 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +12.1 | 1e-31 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +10.6 | 3e-24 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.60×** | +9.6 | 1e-19 | 31/41 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +9.3 | 2e-18 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.51×** | +7.9 | 3e-13 | 31/47 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.38×** | +6.8 | 6e-10 | 30/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.9 | 2e-07 | 30/48 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.68×** | +5.7 | 7e-07 | 35/48 (C32, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.67×** | +5.7 | 8e-07 | 29/48 (HT-29, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.31×** | +5.6 | 1e-06 | 29/48 (COLO 205, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +5.4 | 3e-06 | 32/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.7 | 9e-05 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.53×** | +4.7 | 1e-04 | 25/49 (NCI-H23, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +4.6 | 1e-04 | 24/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 7e-04 | 22/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.46×** | +4.2 | 9e-04 | 18/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.001 | 19/47 (C32, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.011 | 15/48 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.024 | 12/48 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3093.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0654×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.347×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.477×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.715× | -3.7 | 0.11 | 12/48 (C-33 A, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | 0.735× | -3.4 | 0.17 | 19/43 (SK-MEL-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.828× | -3.0 | 0.32 | 13/48 (J82, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.868× | -3.0 | 0.32 | 13/47 (NCI-H2030, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 79.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +10.4) | — |
| [[SW480 (line)]] | alt | 65.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 33.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +13.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 61.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 51.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 45.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +20.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 30.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +14.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 54.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 60.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +9.1) | — |
| [[A-172 (line)]] | wt | 85.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 69.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CHP-212 (line)]] | wt | 43.2 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0654× (z -11.3) |
| [[H4 (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 81.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 57.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 48.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H23 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H2347 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 65.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1B]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ZBTB25]] | +0.59 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[NIPSNAP2]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LSM14A]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[AGPAT5]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[C1GALT1]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[VPS26C]] | +0.49 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[ZNG1A]] | +0.49 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[VPS8]] | +0.49 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[UBE2V2]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PCID2]] | +0.48 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[TAF15]] | +0.48 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB6]] | -0.54 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[DEDD2]] | -0.51 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[PDCL]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MYO7A]] | -0.46 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[NR1H2]] | -0.45 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[TCP1]] | -0.45 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[NAPG]] | -0.44 | -0.63 / -0.22 | both halves | 6e-04 |  |
| [[SERPINH1]] | -0.43 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[MSANTD1]] | -0.42 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[SAR1A]] | -0.42 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[ZNF75D]] | -0.42 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[MOCS2-DT]] | -0.42 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.346). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.4, 17.9); signed map (8.4, -15.0). **Vector** length 110, 29.9% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.6 | +10.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.2 | +12.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +14.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +12.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.2 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -4.9 | -3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.4 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial carrier 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,617,315-47,642,607 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC25A50, MIMP |
| Gene groups (HGNC) | Solute carrier family 25 |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6C9](https://www.uniprot.org/uniprotkb/Q9Y6C9) (Mitochondrial carrier homolog 2):

> Protein insertase that mediates insertion of transmembrane proteins into the mitochondrial outer membrane. Catalyzes insertion of proteins with alpha-helical transmembrane regions, such as signal-anchored, tail-anchored and multi-pass membrane proteins. Does not mediate insertion of beta-barrel transmembrane proteins. Also acts as a receptor for the truncated form of pro-apoptotic BH3-interacting domain death agonist (p15 BID) and has therefore a critical function in apoptosis (By similarity). …

**Summary**, from NCBI Gene [23788](https://www.ncbi.nlm.nih.gov/gene/23788):

> This gene encodes a member of the SLC25 family of nuclear-encoded transporters that are localized in the inner mitochondrial membrane. Members of this superfamily are involved in many metabolic pathways and cell functions. Genome-wide association studies in human have identified single-nucleotide polymorphisms in several loci associated with obesity. This gene is one such locus, which is highly expressed in white adipose tissue and adipocytes, and thought to play a regulatory role in adipocyte …

**Accessions** — [HGNC:17587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17587) · Entrez [23788](https://www.ncbi.nlm.nih.gov/gene/23788) · UniProt [Q9Y6C9](https://www.uniprot.org/uniprotkb/Q9Y6C9) · Ensembl [ENSG00000109919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109919)

## Data

Gene col 3093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3093); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3093]; `tensor/DDL_lfc|DDL_z.npy` [3093]; `embed/gene_vectors.npy` [3093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3093 or target_col == 3093). Every well: [[MTCH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTCH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
