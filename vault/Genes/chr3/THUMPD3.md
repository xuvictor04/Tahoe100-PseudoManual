---
symbol: "THUMPD3"
type: "gene"
col: 5508
ensembl_id: "ENSG00000134077"
name: "THUMP domain 3 tRNA guanosine methyltransferase"
location: "3p25.3"
module: 11
arm: "+"
pooled_cpm: 31.15
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# THUMPD3

*THUMP domain 3 tRNA guanosine methyltransferase* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.47× (z +19.2, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.782× (z -5.6, q 1e-05, down in 22 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.794× (z -3.7, q 0.034, down in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.186×, A-172 0.240×, C-33 A 0.189×, hTERT-HPNE 0.126×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.185×, NCI-H23 0.220×, KATO III 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.212×, RKO 0.389×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB6]] (+0.82, fdr 7e-06), [[RBAK]] (+0.78, fdr 7e-06), [[UTP3]] (+0.75, fdr 7e-06); moves opposite to [[SEC11A]] (-0.64, fdr 7e-06), [[RNF38]] (-0.64, fdr 1e-05), [[CD81]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.47×** | +19.2 | 0e+00 | 42/48 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +18.7 | 0e+00 | 45/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.70×** | +18.5 | 0e+00 | 39/47 (NCI-H2030, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.11×** | +18.3 | 0e+00 | 46/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +17.1 | 0e+00 | 43/47 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +11.3 | 2e-27 | 31/46 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +11.1 | 1e-26 | 37/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +7.9 | 1e-13 | 28/47 (A-172, PANC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +6.1 | 5e-08 | 25/47 (A-172, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.9 | 2e-07 | 23/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.23×** | +5.1 | 2e-05 | 23/48 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +5.1 | 2e-05 | 20/47 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +5.0 | 2e-05 | 20/47 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +5.0 | 2e-05 | 17/48 (AsPC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +5.0 | 3e-05 | 18/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +4.9 | 3e-05 | 16/48 (PANC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +4.6 | 1e-04 | 16/45 (NCI-H1573, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.2 | 0.001 | 12/48 (Hs 766T, PANC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.005 | 8/47 (NCI-H2347, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5508.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.186×, A-172 0.240×, C-33 A 0.189×, hTERT-HPNE 0.126×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.185×, NCI-H23 0.220×, KATO III 0.327×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.212×, RKO 0.389×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.782×** | -5.6 | 1e-05 | 22/43 (RKO, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.832×** | -4.7 | 9e-04 | 15/48 (A-427, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.794×** | -3.7 | 0.034 | 10/47 (RPMI-7951, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.856× | -3.6 | 0.036 | 12/47 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.885× | -3.6 | 0.036 | 14/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.903× | -3.5 | 0.036 | 5/48 (CHP-212, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.862× | -3.5 | 0.037 | 17/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.862× | -3.4 | 0.041 | 10/48 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.868× | -3.4 | 0.043 | 10/48 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.863× | -3.4 | 0.045 | 11/47 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.790× | -3.0 | 0.12 | 3/48 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.881× | -3.0 | 0.12 | 10/47 (SNU-423, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 44.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.35× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.98× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 29.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.83× (z +12.4) | — |
| [[SW480 (line)]] | alt | 27.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.03× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 37.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 37.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 28.5 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.83× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 32.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +10.5) | — |
| [[RKO (line)]] | wt | 61.8 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.46× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 33.7 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.77× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 32.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 48.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 44.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.86× (z +9.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 44.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.04× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 26.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.38× (z +8.5) | — |
| [[LoVo (line)]] | wt | 28.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.98× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -12.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 29.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.49× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.461× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 34.4 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.15× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 25.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB6]] | +0.82 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[RBAK]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[UTP3]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.75 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[CWC22]] | +0.74 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[MRM2]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 | same gene group |
| [[ABRAXAS2]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.71 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.70 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[MED1]] | +0.70 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[NOL11]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC11A]] | -0.64 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[RNF38]] | -0.64 | -0.71 / -0.57 | both halves | 1e-05 |  |
| [[CD81]] | -0.62 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[TMEM50B]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[SEC61A2]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[MFSD14B]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.7, 6.8); signed map (-0.5, -21.5). **Vector** length 98.5, 22.6% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.0 | +18.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +18.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +11.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +19.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +17.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.9 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.8 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.2 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | THUMP domain 3 tRNA guanosine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,362,971-9,386,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434F091 |
| Gene groups (HGNC) | 7BS N2-guanosine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV44](https://www.uniprot.org/uniprotkb/Q9BV44) (tRNA):

> Catalytic subunit of the THUMPD3-TRM112 methyltransferase complex, that specifically mediates the S-adenosyl-L-methionine-dependent N(2)-methylation of guanosine nucleotide at position 6 (m2G6) in tRNAs. This is one of the major tRNA (guanine-N(2))-methyltransferases. Also catalyzes the S-adenosyl-L-methionine-dependent N(2)-methylation of guanosine nucleotide at position 7 of tRNA(Trp).

**Summary**, from NCBI Gene [25917](https://www.ncbi.nlm.nih.gov/gene/25917):

> Enables tRNA (guanine(6)-N2)-methyltransferase activity and tRNA (guanine(7)-N2)-methyltransferase activity. Involved in tRNA methylation. Located in cytosol and nucleolus. Part of tRNA methyltransferase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24493) · Entrez [25917](https://www.ncbi.nlm.nih.gov/gene/25917) · UniProt [Q9BV44](https://www.uniprot.org/uniprotkb/Q9BV44) · Ensembl [ENSG00000134077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134077)

## Data

Gene col 5508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5508); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5508]; `tensor/DDL_lfc|DDL_z.npy` [5508]; `embed/gene_vectors.npy` [5508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5508 or target_col == 5508). Every well: [[THUMPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THUMPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
