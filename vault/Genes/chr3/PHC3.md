---
symbol: "PHC3"
type: "gene"
col: 10437
ensembl_id: "ENSG00000173889"
name: "polyhomeotic homolog 3"
location: "3q26.2"
module: 28
arm: "+"
pooled_cpm: 192.01
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# PHC3

*polyhomeotic homolog 3* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +8.5, q 1e-14, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.471× (z -12.8, q 2e-34, down in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.794× (z -5.5, q 2e-06, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.131×, SK-MEL-2 0.182×, A-427 0.277×, A-172 0.280×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (Panc 03.27 0.296×, A-427 0.348×, RPMI-7951 0.266×, SNU-423 0.344×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.266×, CFPAC-1 0.338×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.578×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS5]] (+0.75, fdr 7e-06), [[CEPT1]] (+0.70, fdr 7e-06), [[CLK4]] (+0.67, fdr 7e-06); moves opposite to [[MAPKAPK2]] (-0.66, fdr 1e-05), [[SMG1P2]] (-0.63, fdr 2e-05), [[ITGB1]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +8.5 | 1e-14 | 38/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +6.1 | 3e-07 | 36/48 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.6 | 9e-04 | 30/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.013 | 28/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.013 | 28/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.088 | 24/48 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.14× | +3.1 | 0.14 | 2/48 (NCI-H1792, LS 180) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.42× | +3.1 | 0.16 | 25/50 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.22× | +3.0 | 0.16 | 27/50 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10437.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H23 0.131×, SK-MEL-2 0.182×, A-427 0.277×, A-172 0.280×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (Panc 03.27 0.296×, A-427 0.348×, RPMI-7951 0.266×, SNU-423 0.344×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (J82 0.266×, CFPAC-1 0.338×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.578×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.471×** | -12.8 | 2e-34 | 46/49 (Panc 03.27, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.487×** | -11.7 | 2e-29 | 43/44 (NCI-H23, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.496×** | -11.0 | 8e-26 | 41/45 (J82, CFPAC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.605×** | -8.5 | 2e-15 | 43/48 (SNU-423, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.714×** | -8.1 | 6e-14 | 38/49 (A549, SNU-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.651×** | -7.3 | 3e-11 | 39/48 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.655×** | -7.2 | 6e-11 | 37/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.654×** | -6.9 | 3e-10 | 39/47 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.712×** | -5.5 | 2e-06 | 32/47 (SNU-1, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -5.5 | 2e-06 | 31/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.746×** | -5.0 | 3e-05 | 32/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.758×** | -4.7 | 1e-04 | 35/48 (AsPC-1, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.790×** | -3.8 | 0.005 | 29/50 (A-172, SNU-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.814×** | -3.5 | 0.020 | 27/48 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.825×** | -3.3 | 0.041 | 23/49 (HS-578T, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.088 | 20/48 (A498, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 282 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 196 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 200 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 298 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.388× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 187 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.529× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 291 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 200 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A549 (line)]] | wt | 197 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 197 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HS-578T (line)]] | alt | 232 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 182 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 274 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[J82 (line)]] | alt | 212 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 164 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 310 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 182 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 239 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 191 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 213 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[C-33 A (line)]] | alt | 144 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[C32 (line)]] | wt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 263 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.285× (z -8.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 124 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 91.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H460 (line)]] | wt | 142 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RKO (line)]] | wt | 202 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.9) | — |
| [[RPMI-7951 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW 900 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[AsPC-1 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 225 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HepG2_C3A (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LS 180 (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.440× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 226 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 168 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 263 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS5]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[CEPT1]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[CLK4]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.65 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[COG4]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[AIMP1]] | +0.64 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[NFYB]] | +0.64 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[RAD52]] | +0.64 | +0.54 / +0.47 | both halves | 2e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[RUFY1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[HPS4]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ARFGEF2]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK2]] | -0.66 | -0.62 / -0.53 | both halves | 1e-05 | pathway: Cellular Senescence; STRING 507 |
| [[SMG1P2]] | -0.63 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ITGB1]] | -0.62 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ACOT7]] | -0.60 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.59 | -0.65 / -0.47 | both halves | 2e-05 | pathway: Differentiation of T cells; STRING 499 |
| [[ACTN1]] | -0.58 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[DUSP5]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CYTH1]] | -0.56 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[EHD4]] | -0.56 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[GFOD1]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SLC20A1]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[RSU1]] | -0.55 | -0.56 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.5, 4.7); signed map (-4.2, -7.9). **Vector** length 100, 37.3% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.3 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.3 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | -3.1 | -5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | polyhomeotic homolog 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:170,086,732-170,181,749 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EDR3, FLJ12967, FLJ12729, HPH3 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Reactome | 20 pathways, smallest: SUMOylation of DNA methylation proteins; Transcriptional Regulation by E2F6; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDX5](https://www.uniprot.org/uniprotkb/Q8NDX5) (Polyhomeotic-like protein 3):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility.

**Summary**, from NCBI Gene [80012](https://www.ncbi.nlm.nih.gov/gene/80012):

> Predicted to enable chromatin binding activity and histone binding activity. Predicted to be involved in negative regulation of DNA-templated transcription. Located in nucleoplasm. Part of PRC1 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15682) · Entrez [80012](https://www.ncbi.nlm.nih.gov/gene/80012) · UniProt [Q8NDX5](https://www.uniprot.org/uniprotkb/Q8NDX5) · Ensembl [ENSG00000173889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173889)

## Data

Gene col 10437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10437); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10437]; `tensor/DDL_lfc|DDL_z.npy` [10437]; `embed/gene_vectors.npy` [10437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10437 or target_col == 10437). Every well: [[PHC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
