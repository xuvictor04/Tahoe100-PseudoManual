---
symbol: "DCAKD"
type: "gene"
col: 10328
ensembl_id: "ENSG00000172992"
name: "dephospho-CoA kinase domain containing"
location: "17q21.31"
module: 52
arm: "+"
pooled_cpm: 31.61
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# DCAKD

*dephospho-CoA kinase domain containing* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.73× (z +11.0, q 2e-25, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.781× (z -7.1, q 7e-10, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~82% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.652× (z -4.5, q 7e-04, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A498 0.304×, HS-578T 0.337×, PANC-1 0.483×, A549 0.442×, …; ⚠ cell-cycle shift, explains ~82% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (A-427 0.279×, LoVo 0.293×, SHP-77 0.252×, J82 0.338×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.261×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A16]] (+0.68, fdr 1e-05), [[BCL7C]] (+0.61, fdr 1e-05), [[TMEM230]] (+0.60, fdr 7e-06); moves opposite to [[BDH2]] (-0.52, fdr 5e-05), [[DUSP19]] (-0.52, fdr 4e-05), [[ZNF608]] (-0.51, fdr 8e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +11.0 | 2e-25 | 37/48 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +10.3 | 2e-22 | 24/38 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +9.5 | 3e-19 | 35/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.47×** | +7.5 | 8e-12 | 30/45 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +7.5 | 1e-11 | 29/48 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.4 | 1e-11 | 25/47 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.9 | 3e-10 | 25/44 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.21×** | +3.6 | 0.022 | 12/48 (NCI-H460, HT-29, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.022 | 6/46 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | **1.21×** | +3.5 | 0.022 | 15/42 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.027 | 10/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.19× | +3.4 | 0.031 | 15/47 (NCI-H460, C32, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.032 | 7/47 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.17× | +3.1 | 0.078 | 11/48 (A549, A-427, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.16× | +3.0 | 0.099 | 14/48 (A549, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10328.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A498 0.304×, HS-578T 0.337×, PANC-1 0.483×, A549 0.442×, …; ⚠ cell-cycle shift, explains ~82% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (A-427 0.279×, LoVo 0.293×, SHP-77 0.252×, J82 0.338×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.261×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.781×** | -7.1 | 7e-10 | 22/47 (A498, HS-578T, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -6.4 | 5e-08 | 26/47 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.773×** | -5.2 | 3e-05 | 21/48 (SW480, LoVo, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.777×** | -5.1 | 5e-05 | 23/45 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.652×** | -4.5 | 7e-04 | 19/48 (AN3 CA, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.811×** | -4.1 | 0.004 | 22/48 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.701×** | -3.8 | 0.012 | 19/47 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.831×** | -3.8 | 0.012 | 15/47 (HS-578T, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.834× | -3.7 | 0.013 | 19/48 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **0.784×** | -3.5 | 0.024 | 15/45 (NCI-H1573, A-427, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.895× | -3.2 | 0.070 | 13/48 (HS-578T, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 51.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.44× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -19.4) ⚠ cell-cycle shift, explains ~82% of this change |
| [[HEC-1-A (line)]] | alt | 41.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.30× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 36.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 37.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -9.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SHP-77 (line)]] | alt | 43.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.5) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.252× (z -10.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 33.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.95× (z +11.8) | — |
| [[A-427 (line)]] | wt | 39.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 37.9 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.8) ⚠ cell-cycle shift, explains ~82% of this change |
| [[CFPAC-1 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.98× (z +11.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.338× (z -9.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.293× (z -11.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 26.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.6) ⚠ cell-cycle shift, explains ~82% of this change |
| [[NCI-H2030 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.9) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SK-MEL-2 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.365× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A16]] | +0.68 | +0.51 / +0.74 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[BCL7C]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TMEM230]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MTG1]] | +0.60 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[SZT2]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SPG7]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TIMM23B]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | +0.56 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CBY1]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TAF12]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MCRIP1]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDH2]] | -0.52 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DUSP19]] | -0.52 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[ZNF608]] | -0.51 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[ZNF711]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[PIK3R1]] | -0.48 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[PARP8]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 | pathway: Metabolism of vitamins and cofactors |
| [[ASF1A]] | -0.48 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[TBL1XR1]] | -0.47 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[ATF7IP]] | -0.47 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[CEP19]] | -0.46 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[MAP3K1]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[RARG]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-7.4, -0.9); signed map (-47.7, -1.1). **Vector** length 86.0, 17.0% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +4.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.4 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -4.2 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -3.1 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -2.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.8 | +0.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | dephospho-CoA kinase domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,023,338-45,061,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22955 |
| Reactome | 4 pathways, smallest: Coenzyme A biosynthesis; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

UniProt [Q8WVC6](https://www.uniprot.org/uniprotkb/Q8WVC6) carries no function annotation.

**Summary**, from NCBI Gene [79877](https://www.ncbi.nlm.nih.gov/gene/79877):

> Enables dephospho-CoA kinase activity. Predicted to be involved in coenzyme A biosynthetic process. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26238) · Entrez [79877](https://www.ncbi.nlm.nih.gov/gene/79877) · UniProt [Q8WVC6](https://www.uniprot.org/uniprotkb/Q8WVC6) · Ensembl [ENSG00000172992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172992)

## Data

Gene col 10328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10328); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10328]; `tensor/DDL_lfc|DDL_z.npy` [10328]; `embed/gene_vectors.npy` [10328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10328 or target_col == 10328). Every well: [[DCAKD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAKD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
