---
symbol: "ZBED5"
type: "gene"
col: 14074
ensembl_id: "ENSG00000236287"
name: "zinc finger BED-type containing 5"
location: "11p15.4"
module: 95
arm: "+"
pooled_cpm: 31.82
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# ZBED5

*zinc finger BED-type containing 5* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.24× (z +25.1, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.564× (z -8.7, q 3e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED13]] (+0.77, fdr 7e-06), [[THAP2]] (+0.75, fdr 9e-05), [[LINC01004]] (+0.74, fdr 2e-04); moves opposite to [[ANKRD27]] (-0.72, fdr 7e-05), [[TMEM120B]] (-0.70, fdr 8e-05), [[MAST3]] (-0.70, fdr 1e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +25.1 | 0e+00 | 47/47 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +17.7 | 0e+00 | 45/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +13.6 | 1e-39 | 42/47 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +10.9 | 1e-25 | 40/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +10.8 | 2e-25 | 39/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.7 | 4e-20 | 39/48 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +9.6 | 9e-20 | 40/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.1 | 7e-08 | 34/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.8 | 1e-04 | 24/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 22/48 (BT-474, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.3 | 0.001 | 24/46 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.017 | 19/47 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.10 | 9/47 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14074.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -8.7 | 3e-15 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.568×** | -8.5 | 4e-15 | 38/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -8.0 | 3e-13 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -6.1 | 2e-07 | 34/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.674×** | -6.0 | 3e-07 | 28/46 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.756×** | -4.1 | 0.004 | 17/34 (HCT15, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.619×** | -3.8 | 0.012 | 19/46 (HepG2/C3A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.785×** | -3.7 | 0.017 | 18/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.637×** | -3.6 | 0.023 | 20/46 (HepG2/C3A, A-172, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.813× | -3.1 | 0.10 | 18/47 (PANC-1, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.815× | -3.1 | 0.10 | 15/47 (C-33 A, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | 0.803× | -3.1 | 0.10 | 17/41 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HEC-1-A (line)]] | alt | 28.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 28.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +17.5) | — |
| [[HT-29 (line)]] | alt | 41.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +13.4) | — |
| [[LoVo (line)]] | wt | 23.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +24.8) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 48.7 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +15.2) | — |
| [[SW480 (line)]] | alt | 43.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +17.1) | — |
| [[C32 (line)]] | wt | 19.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +14.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -8.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 26.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +15.8) | — |
| [[NCI-H460 (line)]] | wt | 22.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.355× (z -8.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 39.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +14.7) | — |
| [[A498 (line)]] | wt | 25.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +15.1) | — |
| [[BT-474 (line)]] | alt | 44.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[HCT15 (line)]] | alt | 38.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[J82 (line)]] | alt | 38.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +15.3) | — |
| [[KATO III (line)]] | alt | 19.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 26.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +15.5) | — |
| [[NCI-H1792 (line)]] | alt | 28.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H2347 (line)]] | alt | 14.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 67.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +15.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 35.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 38.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 43.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.1) | — |
| [[H4 (line)]] | wt | 39.2 | 1 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.220× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 26.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 30.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.338× (z -8.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 32.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 23.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 16.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SW48 (line)]] | wt | 28.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +12.8) | — |
| [[A-427 (line)]] | wt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +17.4) | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 0.05 µM 0.0653× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H2030 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +10.3) | — |
| [[A549 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13]] | +0.77 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[THAP2]] | +0.75 | +0.76 / +0.36 | both halves | 9e-05 |  |
| [[LINC01004]] | +0.74 | +0.75 / +0.32 | both halves | 2e-04 |  |
| [[PBLD]] | +0.74 | +0.78 / +0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[UBE3B]] | +0.73 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[ERCC6L2-AS1]] | +0.73 | +0.76 / +0.22 | both halves | 6e-04 |  |
| [[ZNF689]] | +0.73 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ERCC6L2]] | +0.72 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[GGPS1]] | +0.72 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | +0.72 | +0.75 / +0.24 | both halves | 5e-04 |  |
| [[CCDC90B-AS1]] | +0.72 | +0.78 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[NEK8]] | +0.72 | +0.73 / +0.38 | both halves | 6e-05 |  |
| [[ANKRD17-DT]] | +0.72 | +0.72 / +0.37 | both halves | 9e-05 |  |
| [[MMADHC-DT]] | +0.72 | +0.73 / +0.21 | both halves | 6e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | -0.72 | -0.70 / -0.37 | both halves | 7e-05 |  |
| [[TMEM120B]] | -0.70 | -0.69 / -0.37 | both halves | 8e-05 |  |
| [[MAST3]] | -0.70 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[ELP1]] | -0.69 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[WASF3]] | -0.69 | -0.64 / -0.39 | both halves | 6e-05 |  |
| [[HACE1]] | -0.69 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[STX7]] | -0.68 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[ST6GALNAC4]] | -0.68 | -0.61 / -0.29 | both halves | 3e-04 |  |
| [[NDRG3]] | -0.68 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[PLA2G12A]] | -0.67 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[AIF1L]] | -0.67 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MYPOP]] | -0.67 | -0.61 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZBED5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FLRT2]] | B | FLRT2 activity raises ZBED5's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.09× lower at baseline in the lines without FLRT2 | 0.070 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[SOCS2]] | B | SOCS2 activity raises ZBED5's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without SOCS2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[HDAC6]] | B | HDAC6 activity raises ZBED5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.812). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (5.3, 10.8); signed map (22.7, -9.5). **Vector** length 125, 34.6% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.55 to 7); *Activation of HOX genes during differentiation* (reactome, mean cos +0.60 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +25.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.5 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +17.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.9 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +4.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.9 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -9.7 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -9.5 | -8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -9.3 | -8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.0 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -3.8 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:10,812,074-10,858,796 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Buster1 |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

UniProt [Q49AG3](https://www.uniprot.org/uniprotkb/Q49AG3) carries no function annotation.

**Summary**, from NCBI Gene [58486](https://www.ncbi.nlm.nih.gov/gene/58486):

> This gene is unusual in that its coding sequence is mostly derived from Charlie-like DNA transposon; however, it does not appear to be an active DNA transposon as it is not flanked by terminal inverted repeats. The encoded protein is conserved among the mammalian Laurasiatheria branch. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:30803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30803) · Entrez [58486](https://www.ncbi.nlm.nih.gov/gene/58486) · UniProt [Q49AG3](https://www.uniprot.org/uniprotkb/Q49AG3) · Ensembl [ENSG00000236287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236287)

## Data

Gene col 14074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14074); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14074]; `tensor/DDL_lfc|DDL_z.npy` [14074]; `embed/gene_vectors.npy` [14074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14074 or target_col == 14074). Every well: [[ZBED5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
