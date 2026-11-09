---
symbol: "WNK1"
type: "gene"
col: 685
ensembl_id: "ENSG00000060237"
name: "WNK lysine deficient protein kinase 1"
location: "12p13.33"
module: 3
arm: "-"
pooled_cpm: 330.59
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# WNK1

*WNK lysine deficient protein kinase 1* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +21.2, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.697× (z -12.3, q 7e-32, down in 42 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (PANC-1 0.499×, MIA PaCa-2 0.531×, NCI-H460 0.586×, A498 0.623×, …; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.548×, A549 0.609×, NCI-H2030 0.669×; ⚠ cell-cycle shift, explains <1% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.497×, RKO 0.507×, NCI-H23 0.584×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP11C]] (+0.64, fdr 1e-05), [[CPSF2]] (+0.61, fdr 1e-05), [[ZMYND11]] (+0.58, fdr 2e-05); moves opposite to [[ZNF461]] (-0.59, fdr 3e-05), [[ZNF112]] (-0.58, fdr 2e-05), [[PIGH]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SMARCA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +21.2 | 0e+00 | 37/48 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +11.4 | 1e-27 | 33/48 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +9.3 | 3e-18 | 34/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +8.3 | 2e-14 | 29/50 (LS 180, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +7.6 | 4e-12 | 27/48 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.16× | +7.4 | 1e-11 | 19/49 (AsPC-1, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +6.4 | 1e-08 | 24/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.16× | +5.3 | 7e-06 | 15/48 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.2 | 1e-05 | 17/48 (C32, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | 1.16× | +5.2 | 1e-05 | 22/47 (HOP62, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.15× | +4.8 | 7e-05 | 18/48 (COLO 205, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.12× | +3.9 | 0.006 | 14/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.008 | 19/48 (NCI-H23, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.7 | 0.010 | 15/48 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 1.11× | +3.6 | 0.012 | 3/48 (J82, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.12× | +3.4 | 0.026 | 6/47 (RPMI-7951, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.10× | +3.2 | 0.039 | 0/48 | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.09× | +3.1 | 0.071 | 6/48 (HEC-1-A, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 685.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (PANC-1 0.499×, MIA PaCa-2 0.531×, NCI-H460 0.586×, A498 0.623×, …; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.548×, A549 0.609×, NCI-H2030 0.669×; ⚠ cell-cycle shift, explains <1% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.497×, RKO 0.507×, NCI-H23 0.584×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -12.3 | 7e-32 | 42/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -5.5 | 1e-05 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -5.4 | 2e-05 | 17/48 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.872× | -4.8 | 2e-04 | 8/48 (RKO, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.891× | -4.1 | 0.004 | 8/49 (A498, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.878× | -4.1 | 0.004 | 15/45 (A-427, SNU-1, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.927× | -3.8 | 0.011 | 8/48 (A498, HT-29, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.929× | -3.7 | 0.016 | 7/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.903× | -3.6 | 0.017 | 15/48 (BT-474, SW1417, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.869× | -3.6 | 0.021 | 17/48 (HCT15, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.906× | -3.5 | 0.024 | 3/49 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.908× | -3.4 | 0.029 | 6/48 (HepG2/C3A, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.875× | -3.4 | 0.030 | 11/48 (Hs 766T, BT-474, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.911× | -3.3 | 0.036 | 18/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.914× | -3.2 | 0.055 | 7/48 (HS-578T, A-427, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.916× | -3.1 | 0.067 | 1/48 (NCI-H2347) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.886× | -3.1 | 0.068 | 8/48 (H4, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.942× | -3.0 | 0.073 | 1/48 (RKO) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 257 | 11 | 0 | [[Dexamethasone (drug)]] 0.5 µM 1.83× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 233 | 10 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +22.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.586× (z -12.0) ⚠ toxic |
| [[C32 (line)]] | wt | 298 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +24.9) | — |
| [[COLO 205 (line)]] | alt | 237 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +25.7) | — |
| [[LoVo (line)]] | wt | 365 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +21.1) | — |
| [[LOX-IMVI (line)]] | wt | 427 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +13.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.616× (z -10.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 551 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.531× (z -12.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 326 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.477× (z -10.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 628 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[A498 (line)]] | wt | 345 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +26.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.623× (z -11.3) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 176 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +19.3) | — |
| [[BT-474 (line)]] | alt | 221 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.494× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 214 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +19.4) | — |
| [[HepG2_C3A (line)]] | wt | 449 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.457× (z -10.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 226 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +20.4) | — |
| [[LS 180 (line)]] | wt | 323 | 3 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 212 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +24.9) | — |
| [[NCI-H23 (line)]] | alt | 646 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.584× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[PANC-1 (line)]] | alt | 427 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -18.3) ⚠ cell-cycle shift, explains <1% of this change |
| [[RKO (line)]] | wt | 370 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[SW1417 (line)]] | alt | 245 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.581× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 121 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +18.8) | — |
| [[H4 (line)]] | wt | 265 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 534 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 354 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +15.5) | — |
| [[KATO III (line)]] | alt | 289 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.594× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 242 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 215 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.567× (z -10.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 404 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.662× (z -8.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 195 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +15.2) | — |
| [[SW480 (line)]] | alt | 557 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.641× (z -9.5) ⚠ toxic |
| [[A549 (line)]] | wt | 270 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -12.2) ⚠ cell-cycle shift, explains <1% of this change |
| [[J82 (line)]] | alt | 295 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 206 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.3) | — |
| [[SK-MEL-2 (line)]] | alt | 320 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +13.1) | — |
| [[A-172 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 311 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 370 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 230 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 362 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 483 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 317 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 | pathway: Ion channel transport |
| [[CPSF2]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HECTD1]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[USP7]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[HNRNPK]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PAK2]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TRIP12]] | +0.54 | +0.37 / +0.54 | both halves | 7e-05 | STRING 576 |
| [[KIF5B]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[DGKH]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TAOK1]] | +0.53 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[DSP]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF461]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[ZNF112]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[PIGH]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[VPS37C]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PHLDB3]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[C1orf52]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SNU13]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[FAM24B]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[SDHAP2]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZNF512]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ZNF790-AS1]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[SDHAP1]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA2]] | B | SMARCA2 activity lowers WNK1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.68× higher at baseline in the lines without SMARCA2 | 0.084 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |
| [[UTRN]] | C | UTRN activity raises WNK1's level | lines that do not express UTRN (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without UTRN | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.418). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-5.5, 2.9); signed map (15.0, -7.8). **Vector** length 124, 35.6% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +8.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.0 | +1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +3.0 | +1.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.0 | -12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -3.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -6.4 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.9 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -4.1 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.4 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | WNK lysine deficient protein kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:752,579-911,452 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSAN2, PPP1R167; previously PRKWNK1, HSN2 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Minor histocompatibility antigens; WNK lysine deficient protein kinases |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4A3](https://www.uniprot.org/uniprotkb/Q9H4A3) (Serine/threonine-protein kinase WNK1):

> Serine/threonine-protein kinase component of the WNK1-SPAK/OSR1 kinase cascade, which acts as a key regulator of blood pressure and regulatory volume increase by promoting ion influx. WNK1 mediates regulatory volume increase in response to hyperosmotic stress by acting as a molecular crowding sensor, which senses cell shrinkage and mediates formation of a membraneless compartment by undergoing liquid-liquid phase separation. The membraneless compartment concentrates WNK1 with its substrates, …

**Summary**, from NCBI Gene [65125](https://www.ncbi.nlm.nih.gov/gene/65125):

> This gene encodes a member of the WNK subfamily of serine/threonine protein kinases. The encoded protein may be a key regulator of blood pressure by controlling the transport of sodium and chloride ions. Mutations in this gene have been associated with pseudohypoaldosteronism type II and hereditary sensory neuropathy type II. Alternatively spliced transcript variants encoding different isoforms have been described but the full-length nature of all of them has yet to be determined.[provided by …

**Accessions** — [HGNC:14540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14540) · Entrez [65125](https://www.ncbi.nlm.nih.gov/gene/65125) · UniProt [Q9H4A3](https://www.uniprot.org/uniprotkb/Q9H4A3) · Ensembl [ENSG00000060237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060237)

## Data

Gene col 685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 685); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 685]; `tensor/DDL_lfc|DDL_z.npy` [685]; `embed/gene_vectors.npy` [685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 685 or target_col == 685). Every well: [[WNK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
