---
symbol: "GDE1"
type: "gene"
col: 96
ensembl_id: "ENSG00000006007"
name: "glycerophosphodiester phosphodiesterase 1"
location: "16p12.3"
module: 124
arm: "-"
pooled_cpm: 34.22
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# GDE1

*glycerophosphodiester phosphodiesterase 1* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.87× (z +17.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.813× (z -4.9, q 7e-04, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (BT-474 0.231×, KATO III 0.372×, LoVo 0.433×, NCI-H460 0.543×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.291×, RKO 0.431×; ⚠ cell-cycle shift, would explain all of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HCT15 0.259×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH3A2]] (+0.65, fdr 6e-05), [[MAPRE2]] (+0.59, fdr 4e-05), [[GOLM2]] (+0.59, fdr 3e-05); moves opposite to [[STARD7-AS1]] (-0.63, fdr 3e-05), [[GABPB1]] (-0.60, fdr 2e-04), [[RCC1L]] (-0.60, fdr 5e-05).
> It sits in the **-** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 96.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +17.6 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +16.5 | 0e+00 | 46/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.63×** | +16.1 | 0e+00 | 38/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +14.7 | 0e+00 | 46/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.14×** | +12.2 | 4e-32 | 33/35 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.01×** | +10.7 | 6e-25 | 30/40 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +10.6 | 4e-24 | 42/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +8.6 | 7e-16 | 35/48 (A498, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +8.3 | 5e-15 | 41/47 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +6.8 | 5e-10 | 40/48 (A498, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +6.1 | 6e-08 | 27/48 (LS 180, HT-29, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +5.4 | 3e-06 | 26/48 (HOP62, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.32×** | +4.7 | 1e-04 | 25/46 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.19× | +4.2 | 0.001 | 18/48 (PANC-1, C-33 A, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.002 | 21/45 (Panc 03.27, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 14/48 (A498, A549, …) | top dose only |  |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.009 | 17/47 (PANC-1, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.021 | 20/48 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.036 | 13/48 (A-172, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.048 | 11/48 (Hs 766T, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 96.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (BT-474 0.231×, KATO III 0.372×, LoVo 0.433×, NCI-H460 0.543×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.291×, RKO 0.431×; ⚠ cell-cycle shift, would explain all of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HCT15 0.259×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -4.9 | 7e-04 | 27/48 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 96. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.9 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.86× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.03× (z +12.5) | — |
| [[A498 (line)]] | wt | 30.7 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.70× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 41.1 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 25.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.99× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.93× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -8.7) |
| [[PANC-1 (line)]] | alt | 63.9 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.77× (z +11.0) | — |
| [[A549 (line)]] | wt | 36.8 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.57× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 12.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.56× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 59.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +10.8) | — |
| [[KATO III (line)]] | alt | 55.8 | 3 | 1 | [[Belinostat (drug)]] 5 µM 2.96× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -13.6) |
| [[SNU-423 (line)]] | alt | 20.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.88× (z +9.2) | — |
| [[SW480 (line)]] | alt | 22.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.02× (z +13.1) | — |
| [[J82 (line)]] | alt | 35.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.55× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 38.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.58× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 48.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 14.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.22× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.17× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 5.04× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 50.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -14.9) |
| [[C32 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 35.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 32.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.52× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 45.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.259× (z -8.9) |
| [[HT-29 (line)]] | alt | 45.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +9.3) | — |
| [[LoVo (line)]] | wt | 44.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 41.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 33.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +9.1) | — |
| [[A-427 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 96), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3A2]] | +0.65 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[MAPRE2]] | +0.59 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[GOLM2]] | +0.59 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ALAD]] | +0.58 | +0.34 / +0.48 | both halves | 1e-04 | pathway: HALLMARK_HEME_METABOLISM |
| [[SLC25A23]] | +0.58 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[PPP1CC]] | +0.57 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[ENPP4]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TMEM170B]] | +0.57 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[PLS1]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[HPS3]] | +0.56 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[PRKAR2B]] | +0.56 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[ENDOD1]] | +0.55 | +0.45 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_HEME_METABOLISM |

## Genes that move opposite

*57 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD7-AS1]] | -0.63 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[GABPB1]] | -0.60 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[RCC1L]] | -0.60 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[POU6F1]] | -0.59 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[MIRLET7A1HG]] | -0.59 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PTPN9]] | -0.58 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[PCBP1-AS1]] | -0.57 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[DUS2]] | -0.57 | -0.15 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[LRRC41]] | -0.57 | -0.23 / -0.56 | both halves | 5e-04 |  |
| [[ZNF785]] | -0.56 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[GTF3C2-AS2]] | -0.56 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[MSANTD2]] | -0.56 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[SPRY3]] | -0.56 | -0.23 / -0.41 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLS1]] | B | PLS1 activity raises GDE1's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 1.60× lower at baseline in the lines without PLS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **-** arm (projection on the module's main direction -0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-8.8, 18.3); signed map (-2.9, 18.2). **Vector** length 92.9, 23.3% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +14.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +5.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | glycerophosphodiester phosphodiesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,501,693-19,522,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIR16 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: Glycerophospholipid catabolism; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZC3](https://www.uniprot.org/uniprotkb/Q9NZC3) (Glycerophosphodiester phosphodiesterase 1):

> Hydrolyzes the phosphodiester bond of glycerophosphodiesters such as glycerophosphoinositol (GroPIns) and glycerophosphoethanolamine (GroPEth), to yield a glycerol phosphate and an alcohol (By similarity). Hydrolyzes glycerophospho-N-acylethanolamines to N-acylethanolamines in the brain and participates in bioactive N-acylethanolamine biosynthesis such as anandamide (an endocannabinoid), N-palmitoylethanolamine (an anti-inflammatory), and N-oleoylethanolamine (an anorexic). In addition, has a …

**Summary**, from NCBI Gene [51573](https://www.ncbi.nlm.nih.gov/gene/51573):

> Predicted to enable glycerophosphodiester phosphodiesterase activity; glycerophosphoinositol glycerophosphodiesterase activity; and phosphatidylcholine lysophospholipase A1 activity. Predicted to be involved in N-acylethanolamine metabolic process; ethanolamine metabolic process; and phospholipid metabolic process. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29644) · Entrez [51573](https://www.ncbi.nlm.nih.gov/gene/51573) · UniProt [Q9NZC3](https://www.uniprot.org/uniprotkb/Q9NZC3) · Ensembl [ENSG00000006007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006007)

## Data

Gene col 96: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 96); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 96, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 96]; `tensor/DDL_lfc|DDL_z.npy` [96]; `embed/gene_vectors.npy` [96]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 96 or target_col == 96). Every well: [[GDE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
