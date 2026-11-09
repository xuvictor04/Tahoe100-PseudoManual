---
symbol: "CDKN2AIP"
type: "gene"
col: 9669
ensembl_id: "ENSG00000168564"
name: "CDKN2A interacting protein"
location: "4q35.1"
module: 11
arm: "+"
pooled_cpm: 15.24
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CDKN2AIP

*CDKN2A interacting protein* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.05× (z +46.8, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.735× (z -5.2, q 1e-04, down in 21 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Decitabine (drug)]] 0.5 µM: 0.812× (z -3.5, q 0.076, down in 6 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.174×, HOP62 0.226×, NCI-H2030 0.198×, NCI-H460 0.269×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 0.148×, LoVo 0.348×, NCI-H460 0.288×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (BT-474 0.131×, HS-578T 0.123×, LS 180 0.270×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (SHP-77 0.136×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SW48 0.152×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL10]] (+0.67, fdr 7e-06), [[ASF1A]] (+0.64, fdr 7e-06), [[VCPIP1]] (+0.64, fdr 1e-05); moves opposite to [[PMS2P3]] (-0.61, fdr 1e-05), [[SNRPA1]] (-0.58, fdr 1e-05), [[RPS3A]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.05×** | +46.8 | 0e+00 | 46/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.20×** | +30.9 | 0e+00 | 44/44 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **6.28×** | +29.9 | 0e+00 | 46/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.90×** | +23.0 | 0e+00 | 46/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.97×** | +18.4 | 0e+00 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.89×** | +18.0 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +14.3 | 3e-44 | 40/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.17×** | +13.1 | 2e-37 | 36/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +11.1 | 1e-26 | 30/45 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.83×** | +10.3 | 6e-23 | 35/48 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +10.1 | 2e-22 | 34/47 (BT-474, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +9.3 | 1e-18 | 36/47 (HOP62, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +9.2 | 1e-18 | 34/47 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +8.4 | 1e-15 | 31/48 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +7.9 | 1e-13 | 32/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +6.6 | 9e-10 | 24/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9669.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 0.174×, HOP62 0.226×, NCI-H2030 0.198×, NCI-H460 0.269×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LS 180 0.148×, LoVo 0.348×, NCI-H460 0.288×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (BT-474 0.131×, HS-578T 0.123×, LS 180 0.270×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (SHP-77 0.136×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (SW48 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.735×** | -5.2 | 1e-04 | 21/38 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.5 | 0.002 | 3/48 (HOP62, HepG2/C3A, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.076 | 6/46 (SW480, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 0.708× | -3.1 | 0.32 | 8/44 (C32, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.7 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +23.4) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 19.3 | 8 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +19.5) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 18.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +25.7) | — |
| [[HEC-1-A (line)]] | alt | 26.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +24.6) | — |
| [[LoVo (line)]] | wt | 27.3 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +24.2) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 13.3 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +24.2) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 29.0 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.46× (z +18.7) | — |
| [[A549 (line)]] | wt | 11.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +19.9) | — |
| [[J82 (line)]] | alt | 26.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +19.7) | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +24.2) | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +18.5) | — |
| [[C32 (line)]] | wt | 12.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +18.8) | — |
| [[HS-578T (line)]] | alt | 9.86 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 9.32 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 11.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +21.9) | — |
| [[A498 (line)]] | wt | 18.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +22.0) | — |
| [[AsPC-1 (line)]] | alt | 21.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +18.9) | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +18.4) | — |
| [[COLO 205 (line)]] | alt | 16.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +18.4) | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +18.1) | — |
| [[KATO III (line)]] | alt | 24.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.84 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +16.0) | — |
| [[RKO (line)]] | wt | 16.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +15.5) | — |
| [[SW 900 (line)]] | alt | 11.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +14.2) | — |
| [[SW1417 (line)]] | alt | 19.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +16.6) | — |
| [[HCT15 (line)]] | alt | 21.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 7.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 6.69 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 12.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.3) | [[HI-TOPK-032 (drug)]] 0.05 µM 0.136× (z -9.4) |
| [[SNU-423 (line)]] | alt | 10.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.96× (z +16.3) | — |
| [[SW48 (line)]] | wt | 23.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +11.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.152× (z -8.5) |
| [[H4 (line)]] | wt | 9.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 5.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +14.2) | — |
| [[A-427 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL10]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ASF1A]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[VCPIP1]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[LENG1]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.61 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZNF669]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[THAP5]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CMTR2]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[REST]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SPEN]] | +0.58 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[THUMPD1]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SNRPA1]] | -0.58 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[RPS3A]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.58 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[DANCR]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[CPSF6]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[POLR2B]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NDC1]] | -0.56 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[BTAF1]] | -0.56 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[EEF1AKMT2]] | -0.54 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF4]] | B | KLF4 activity raises CDKN2AIP's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without KLF4 | 0.074 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.9, 8.3); signed map (1.3, -22.8). **Vector** length 79.2, 16.9% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.6 | +23.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +29.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +30.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +46.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +10.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.2 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | CDKN2A interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:183,444,635-183,449,064 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XTBD2, FLJ20036, CARF |
| Gene groups (HGNC) | XTBD family |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXV6](https://www.uniprot.org/uniprotkb/Q9NXV6) (CDKN2A-interacting protein):

> Regulates DNA damage response in a dose-dependent manner through a number of signaling pathways involved in cell proliferation, apoptosis and senescence.

**Summary**, from NCBI Gene [55602](https://www.ncbi.nlm.nih.gov/gene/55602):

> The protein encoded by this gene regulates the DNA damage response through several different signaling pathways. One such pathway is the p53-HDM2-p21(WAF1) pathway, which is critical to the DNA damage response. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:24325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24325) · Entrez [55602](https://www.ncbi.nlm.nih.gov/gene/55602) · UniProt [Q9NXV6](https://www.uniprot.org/uniprotkb/Q9NXV6) · Ensembl [ENSG00000168564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168564)

## Data

Gene col 9669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9669); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9669]; `tensor/DDL_lfc|DDL_z.npy` [9669]; `embed/gene_vectors.npy` [9669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9669 or target_col == 9669). Every well: [[CDKN2AIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN2AIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
