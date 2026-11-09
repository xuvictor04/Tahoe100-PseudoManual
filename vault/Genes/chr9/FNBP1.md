---
symbol: "FNBP1"
type: "gene"
col: 11903
ensembl_id: "ENSG00000187239"
name: "formin binding protein 1"
location: "9q34.11"
module: 4
arm: "-"
pooled_cpm: 181.58
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FNBP1

*formin binding protein 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +13.2, q 7e-37, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.571× (z -16.7, q 0e+00, down in 41 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.718× (z -10.2, q 2e-22, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM5B]] (+0.61, fdr 1e-05), [[AAMDC]] (+0.60, fdr 1e-05), [[VASN]] (+0.57, fdr 1e-05); moves opposite to [[LTBR]] (-0.58, fdr 1e-05), [[ABCE1]] (-0.57, fdr 1e-05), [[MRPL3]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZFYVE1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +13.2 | 7e-37 | 27/44 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +6.3 | 7e-08 | 20/45 (LoVo, LS 180, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.35×** | +4.8 | 3e-04 | 27/44 (A498, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.10× | +4.3 | 0.002 | 5/44 (LS 180, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.13× | +3.9 | 0.011 | 10/46 (H4, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.12× | +3.7 | 0.022 | 16/44 (PANC-1, BT-474, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.032 | 17/44 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.11× | +3.1 | 0.14 | 10/45 (J82, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -16.7 | 0e+00 | 41/43 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.571×** | -16.0 | 0e+00 | 35/42 (CHP-212, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -15.1 | 0e+00 | 34/42 (C-33 A, SW 900, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.711×** | -10.4 | 5e-23 | 33/45 (NCI-H1792, NCI-H460, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -10.2 | 2e-22 | 36/44 (SW 900, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.728×** | -9.7 | 4e-20 | 31/44 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.809×** | -6.2 | 5e-08 | 23/44 (SW 900, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.819×** | -6.2 | 5e-08 | 22/44 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.821×** | -6.0 | 1e-07 | 23/44 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.718×** | -5.3 | 5e-06 | 22/45 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.842× | -5.3 | 6e-06 | 21/44 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.843× | -5.2 | 7e-06 | 19/44 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.733×** | -5.0 | 2e-05 | 20/44 (NCI-H1792, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.850× | -5.0 | 3e-05 | 17/44 (SW 900, HOP62, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.847× | -4.9 | 3e-05 | 19/44 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.744×** | -4.8 | 6e-05 | 24/44 (NCI-H1792, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.872× | -4.2 | 7e-04 | 17/44 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.876× | -4.1 | 0.001 | 15/44 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.870× | -4.0 | 0.002 | 16/43 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.881× | -3.9 | 0.003 | 17/44 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.914× | -3.9 | 0.003 | 9/44 (NCI-H1792, SW 900, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 393 | 0 | 23 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.427× (z -12.2) |
| [[SW 900 (line)]] | alt | 478 | 0 | 15 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -20.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 224 | 1 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.329× (z -14.6) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.513× (z -9.0) |
| [[HOP62 (line)]] | alt | 308 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.490× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 92.9 | 2 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.8) | [[Dexamethasone (drug)]] 5 µM 0.396× (z -11.3) |
| [[A-172 (line)]] | wt | 255 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.532× (z -9.8) |
| [[CHP-212 (line)]] | wt | 788 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 214 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.523× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 173 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -11.1) |
| [[BT-474 (line)]] | alt | 323 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +19.9) | — |
| [[A498 (line)]] | wt | 174 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +27.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.574× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 225 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -14.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.533× (z -9.6) |
| [[PANC-1 (line)]] | alt | 200 | 4 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.77× (z +18.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.510× (z -13.3) ⚠ toxic |
| [[C32 (line)]] | wt | 157 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.517× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 207 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.501× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.606× (z -9.2) |
| [[LoVo (line)]] | wt | 147 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.64× (z +13.3) | [[Auranofin (drug)]] 5 µM 0.550× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 130 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.421× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 146 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.476× (z -11.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 148 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.434× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 217 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.607× (z -11.8) ⚠ cell-cycle shift, explains ~1% of this change |
| [[SW480 (line)]] | alt | 150 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.517× (z -9.9) ⚠ toxic |
| [[A549 (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.439× (z -11.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.411× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -21.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 209 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 105 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 209 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.476× (z -10.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 139 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.7) | — |
| [[hTERT-HPNE (line)]] | wt | 212 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 132 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.530× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 293 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.486× (z -11.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.499× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 157 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -12.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 79.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 66.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.449× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.459× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 97.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 81.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +16.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.457× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 235 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5B]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[AAMDC]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[VASN]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CERT1]] | +0.57 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[MORC3]] | +0.57 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[MINDY2]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[DAAM1]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 | pathway: CDC42 GTPase cycle; STRING 656 |
| [[ZMIZ1]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[WBP1]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CDKN2D]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FGFR1]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MEF2A]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBR]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.57 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[MRPL3]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[COX10]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ATIC]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[BYSL]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[METAP1D]] | -0.54 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[GNL3L]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[EEF1E1]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.53 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[HNRNPF]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFYVE1]] | C | FNBP1 activity lowers ZFYVE1's level | lines that do not express FNBP1 (4) vs lines expressing it (46) | 1.02× higher at baseline in the lines without FNBP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CITED2, WHAMMP3, RDX; its own permutation p |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.9, -42.4); signed map (-10.8, 13.8). **Vector** length 127, 37.2% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.2 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.7 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Darolutamide (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.2 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -10.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.2 | -9.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.8 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -16.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.4 | -16.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.4 | -3.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.3 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.9 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | formin binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,887,187-130,043,189 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBP17, KIAA0554 |
| Gene groups (HGNC) | F-BAR domain containing; SH3 domain containing |
| Reactome | 10 pathways, smallest: RND2 GTPase cycle; RHOJ GTPase cycle; RHOQ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RU3](https://www.uniprot.org/uniprotkb/Q96RU3) (Formin-binding protein 1):

> May act as a link between RND2 signaling and regulation of the actin cytoskeleton (By similarity). Required to coordinate membrane tubulation with reorganization of the actin cytoskeleton during the late stage of clathrin-mediated endocytosis. Binds to lipids such as phosphatidylinositol 4,5-bisphosphate and phosphatidylserine and promotes membrane invagination and the formation of tubules. Also enhances actin polymerization via the recruitment of WASL/N-WASP, which in turn activates the Arp2/3 …

**Summary**, from NCBI Gene [23048](https://www.ncbi.nlm.nih.gov/gene/23048):

> The protein encoded by this gene is a member of the formin-binding-protein family. The protein contains an N-terminal Fer/Cdc42-interacting protein 4 (CIP4) homology (FCH) domain followed by a coiled-coil domain, a proline-rich motif, a second coiled-coil domain, a Rho family protein-binding domain (RBD), and a C-terminal SH3 domain. This protein binds sorting nexin 2 (SNX2), tankyrase (TNKS), and dynamin; an interaction between this protein and formin has not been demonstrated yet in human. …

**Accessions** — [HGNC:17069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17069) · Entrez [23048](https://www.ncbi.nlm.nih.gov/gene/23048) · UniProt [Q96RU3](https://www.uniprot.org/uniprotkb/Q96RU3) · Ensembl [ENSG00000187239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187239)

## Data

Gene col 11903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11903); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11903]; `tensor/DDL_lfc|DDL_z.npy` [11903]; `embed/gene_vectors.npy` [11903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11903 or target_col == 11903). Every well: [[FNBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
