---
symbol: "FN3KRP"
type: "gene"
col: 6545
ensembl_id: "ENSG00000141560"
name: "fructosamine 3 kinase related protein"
location: "17q25.3"
module: 85
arm: "+"
pooled_cpm: 19.5
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# FN3KRP

*fructosamine 3 kinase related protein* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.26× (z +31.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.522× (z -19.9, q 0e+00, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP131]] (+0.76, fdr 1e-05), [[CHTF18]] (+0.65, fdr 1e-04), [[BRAT1]] (+0.64, fdr 5e-05); moves opposite to [[C2orf49-DT]] (-0.64, fdr 2e-04), [[CCT6B]] (-0.62, fdr 4e-04), [[LINC00393]] (-0.62, fdr 6e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PXMP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.26×** | +31.4 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.37×** | +26.3 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.03×** | +24.1 | 0e+00 | 46/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +12.7 | 4e-35 | 18/29 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.39×** | +7.1 | 1e-10 | 25/42 (SW 900, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +6.7 | 2e-09 | 18/48 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +5.1 | 3e-05 | 11/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +5.0 | 3e-05 | 16/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.7 | 2e-04 | 9/48 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.25×** | +4.7 | 2e-04 | 19/43 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +4.6 | 3e-04 | 11/44 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +4.3 | 7e-04 | 14/47 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +4.0 | 0.003 | 3/48 (HS-578T, C-33 A, …) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.17× | +3.4 | 0.026 | 12/47 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.068 | 4/47 (SHP-77, NCI-H2030, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.099 | 8/48 (Hs 766T, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -19.9 | 0e+00 | 33/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -6.7 | 7e-09 | 22/47 (COLO 205, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.704×** | -5.9 | 6e-07 | 21/47 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.798×** | -4.7 | 4e-04 | 19/47 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -4.4 | 0.001 | 16/46 (SW480, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.827×** | -4.1 | 0.004 | 9/47 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -3.9 | 0.008 | 13/48 (Hs 766T, CFPAC-1, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.716×** | -3.8 | 0.011 | 11/46 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.028 | 4/48 (HCT15, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.900× | -3.2 | 0.075 | 5/48 (MIA PaCa-2, HepG2/C3A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.834× | -3.1 | 0.11 | 17/46 (A-172, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Delamanid (drug)]] 0.5 µM |  | 0.869× | -3.0 | 0.11 | 5/48 (A-427, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 17.0 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.24× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.9) |
| [[SW480 (line)]] | alt | 20.0 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.10× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -19.8) |
| [[KATO III (line)]] | alt | 42.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.82× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.32× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -19.9) |
| [[PANC-1 (line)]] | alt | 18.8 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.59× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.5) |
| [[A498 (line)]] | wt | 20.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +14.2) | — |
| [[A549 (line)]] | wt | 17.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.77× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 22.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 14.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.04× (z +11.1) | — |
| [[LoVo (line)]] | wt | 10.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.58× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.22× (z +12.5) | — |
| [[A-172 (line)]] | wt | 28.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 28.0 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 5.70× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.147× (z -10.7) |
| [[H4 (line)]] | wt | 14.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 8.04× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 43.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.51× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 10.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.47× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.65× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -10.1) |
| [[RKO (line)]] | wt | 14.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.08× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 35.2 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 14.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +10.1) | — |
| [[A-427 (line)]] | wt | 21.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -11.3) |
| [[CHP-212 (line)]] | wt | 30.3 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0724× (z -10.1) |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.108× (z -10.9) |
| [[HS-578T (line)]] | alt | 13.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0924× (z -8.6) |
| [[LS 180 (line)]] | wt | 32.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 9.42 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.41× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 13.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0898× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 20.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP131]] | +0.76 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CHTF18]] | +0.65 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[BRAT1]] | +0.64 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NPHP4]] | +0.63 | +0.53 / +0.27 | both halves | 3e-04 |  |
| [[KANK2]] | +0.63 | +0.43 / +0.31 | both halves | 2e-04 |  |
| [[RAB40B]] | +0.62 | +0.47 / +0.39 | both halves | 6e-05 | ⚠ same locus (18.0 kb: neighbours can correlate without regulation) |
| [[CABLES2]] | +0.62 | +0.50 / +0.27 | both halves | 3e-04 |  |
| [[DHTKD1]] | +0.61 | +0.45 / +0.27 | both halves | 3e-04 |  |
| [[CASP2]] | +0.60 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SLBP]] | +0.60 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[ARL6IP6]] | +0.60 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[IFT122]] | +0.60 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[MSH5]] | +0.59 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf49-DT]] | -0.64 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[CCT6B]] | -0.62 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[LINC00393]] | -0.62 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[LINC02542]] | -0.62 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[CIBAR1-DT]] | -0.61 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | -0.60 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ST7]] | -0.60 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[LINC02955]] | -0.59 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[ACTR3-AS1]] | -0.59 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LINC01829]] | -0.59 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[ERCC6L2-AS1]] | -0.59 | -0.43 / -0.18 | ⚠ not reproduced | 1e-03 |  |
| [[ZNF341-AS1]] | -0.59 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[ARRDC3-AS1]] | -0.58 | -0.42 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXMP4]] | B | PXMP4 activity raises FN3KRP's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.44× lower at baseline in the lines without PXMP4 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[PGAP4]] | B | PGAP4 activity raises FN3KRP's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.20× lower at baseline in the lines without PGAP4 | 0.092 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[HDAC6]] | B | HDAC6 activity lowers FN3KRP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-28.5, -45.2); signed map (-35.9, -38.9). **Vector** length 98.2, 21.6% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.9 | +31.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | +26.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.9 | +24.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +12.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.4 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -19.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.5 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | fructosamine 3 kinase related protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,716,706-82,730,328 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12171, FN3KL |
| Gene groups (HGNC) | Fructosamine 3 kinase family |
| Reactome | 1 pathways, smallest: Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HA64](https://www.uniprot.org/uniprotkb/Q9HA64) (Ketosamine-3-kinase):

> Ketosamine-3-kinase involved in protein deglycation by mediating phosphorylation of ribuloselysine and psicoselysine on glycated proteins, to generate ribuloselysine-3 phosphate and psicoselysine-3 phosphate, respectively. Ribuloselysine-3 phosphate and psicoselysine-3 phosphate adducts are unstable and decompose under physiological conditions. Not able to phosphorylate fructoselysine.

**Summary**, from NCBI Gene [79672](https://www.ncbi.nlm.nih.gov/gene/79672):

> A high concentration of glucose can result in non-enzymatic oxidation of proteins by reaction of glucose and lysine residues (glycation). Proteins modified in this way are less active or functional. This gene encodes an enzyme which catalyzes the phosphorylation of psicosamines and ribulosamines compared to the neighboring gene which encodes a highly similar enzyme, fructosamine-3-kinase, which has different substrate specificity. The activity of both enzymes may result in deglycation of …

**Accessions** — [HGNC:25700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25700) · Entrez [79672](https://www.ncbi.nlm.nih.gov/gene/79672) · UniProt [Q9HA64](https://www.uniprot.org/uniprotkb/Q9HA64) · Ensembl [ENSG00000141560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141560)

## Data

Gene col 6545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6545); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6545]; `tensor/DDL_lfc|DDL_z.npy` [6545]; `embed/gene_vectors.npy` [6545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6545 or target_col == 6545). Every well: [[FN3KRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FN3KRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
