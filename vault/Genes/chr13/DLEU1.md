---
symbol: "DLEU1"
type: "gene"
col: 10685
ensembl_id: "ENSG00000176124"
name: "deleted in lymphocytic leukemia 1"
location: "13q14.2-q14.3"
module: 27
arm: "+"
pooled_cpm: 239.65
n_lines_expressing: 34
n_dd_up: 13
n_dd_down: 37
n_dd_up_clean: 11
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 2
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# DLEU1

*deleted in lymphocytic leukemia 1* — 13q14.2-q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.48× (z +6.7, q 1e-08, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (18 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.555× (z -10.5, q 6e-23, down in 28 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4713HG]] (+0.71, fdr 7e-06), [[LINC01748]] (+0.68, fdr 7e-06), [[SORL1]] (+0.67, fdr 1e-05); moves opposite to [[CDR2L]] (-0.61, fdr 1e-05), [[WIPF1]] (-0.59, fdr 9e-06), [[CCM2]] (-0.58, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MIR4713HG]] → it (grade B ⚠); 2 go from it, the strongest it → [[TM4SF18]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +6.7 | 1e-08 | 26/31 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +6.5 | 3e-08 | 23/32 (LoVo, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 3e-05 | 24/31 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.0 | 7e-05 | 12/32 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 7e-05 | 20/32 (KATO III, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.5 | 6e-04 | 8/33 (RKO, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.27×** | +4.1 | 0.004 | 22/34 (C32, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.004 | 8/33 (RKO, SNU-423, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +4.0 | 0.005 | 15/33 (C32, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.008 | 17/32 (C32, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.7 | 0.012 | 20/32 (C32, SW480, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.017 | 4/33 (C32, KATO III, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.017 | 12/31 (C32, SNU-423, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.017 | 12/32 (C32, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 6/32 (KATO III, NCI-H1792, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.023 | 18/32 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.032 | 6/33 (C-33 A, SW 1271, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.033 | 11/32 (Hs 766T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.555×** | -10.5 | 6e-23 | 28/32 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -8.9 | 2e-16 | 28/32 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.613×** | -8.7 | 6e-16 | 27/32 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.619×** | -8.5 | 2e-15 | 28/32 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.673×** | -7.0 | 2e-10 | 27/32 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -6.7 | 2e-09 | 26/33 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.695×** | -6.5 | 8e-09 | 25/32 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -6.1 | 1e-07 | 25/32 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -5.6 | 1e-06 | 19/32 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.734×** | -5.5 | 2e-06 | 25/32 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -5.5 | 2e-06 | 25/33 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.563×** | -5.3 | 4e-06 | 24/30 (MIA PaCa-2, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.741×** | -5.3 | 5e-06 | 24/32 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.743×** | -5.3 | 5e-06 | 25/31 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.737×** | -5.2 | 7e-06 | 24/32 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.743×** | -5.1 | 1e-05 | 21/32 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.762×** | -4.5 | 1e-04 | 24/32 (HepG2/C3A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.775×** | -4.5 | 2e-04 | 24/31 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.772×** | -4.4 | 2e-04 | 17/31 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.785×** | -4.3 | 4e-04 | 20/32 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.789×** | -4.2 | 6e-04 | 20/32 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.745×** | -3.7 | 0.003 | 19/32 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.675×** | -3.7 | 0.005 | 16/32 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 312 | 0 | 24 (12 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.152× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 568 | 0 | 20 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -19.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.344× (z -11.2) |
| [[COLO 205 (line)]] | alt | 2,623 | 0 | 17 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -31.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 764 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -13.9) |
| [[SW480 (line)]] | alt | 490 | 0 | 15 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -11.3) |
| [[C32 (line)]] | wt | 141 | 12 (2 ⚠) | 2 (1 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 5.14× (z +14.2) | [[Digitoxin (drug)]] 0.5 µM 0.299× (z -10.4) |
| [[HCT15 (line)]] | alt | 764 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -14.3) |
| [[HT-29 (line)]] | alt | 611 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 288 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -12.9) |
| [[SNU-1 (line)]] | wt | 326 | 0 | 12 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.245× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 851 | 0 | 10 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -17.6) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.465× (z -9.9) |
| [[LS 180 (line)]] | wt | 699 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -19.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.446× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.364× (z -8.9) |
| [[LoVo (line)]] | wt | 163 | 2 (1 ⚠) | 6 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 2.05× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.452× (z -10.6) |
| [[SW48 (line)]] | wt | 607 | 0 | 8 (8 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.232× (z -13.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[KATO III (line)]] | alt | 285 | 1 | 6 (4 ⚠) | [[Ponatinib (drug)]] 5 µM 2.33× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.366× (z -11.1) |
| [[Hs 766T (line)]] | wt | 175 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.283× (z -11.6) |
| [[SHP-77 (line)]] | alt | 332 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 138 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.353× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.286× (z -12.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H23 (line)]] | alt | 214 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.347× (z -9.0) |
| [[PANC-1 (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.399× (z -10.8) |
| [[RKO (line)]] | wt | 74.6 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 0.5 µM 0.327× (z -9.0) |
| [[AN3 CA (line)]] | alt | 65.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -9.4) |
| [[A-172 (line)]] | wt | 30.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 40.8 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 38.8 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 36.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 35.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 31.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 41.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 34.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 36.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 473 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 53.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4713HG]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[LINC01748]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SORL1]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[BANK1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NIHCOLE]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 | same gene group |
| [[GLDN]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[DNAH7]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[LINC00649]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[RNF43]] | +0.62 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[LINC02253]] | +0.61 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[AXIN2]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CHN2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDR2L]] | -0.61 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[WIPF1]] | -0.59 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[CCM2]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[CHFR]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[AP1M1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[FBH1]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MPP3]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TSHZ3]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MEIS3]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TSHZ3-AS1]] | -0.54 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[PARVB]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR4713HG]] | B | MIR4713HG activity raises DLEU1's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 4.40× lower at baseline in the lines without MIR4713HG | 0.002 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[GLDN]] | B | GLDN activity raises DLEU1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without GLDN | 0.007 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[CHN2]] | B | CHN2 activity raises DLEU1's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without CHN2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[DEPTOR]] | B | DEPTOR activity raises DLEU1's level | lines that do not express DEPTOR (6) vs lines expressing it (44) | 3.22× lower at baseline in the lines without DEPTOR | 0.057 | ⚠ within organs, on part of the lines; also absent: WWOX; maybe low, not absent |
| [[MAP2K6]] | B | MAP2K6 activity raises DLEU1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.23× lower at baseline in the lines without MAP2K6 | 0.057 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[PLCB1]] | B | PLCB1 activity raises DLEU1's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without PLCB1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[BAMBI]] | B | BAMBI activity raises DLEU1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without BAMBI | 0.061 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises DLEU1's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without LINC01876 | 0.075 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[SLC44A3]] | B | SLC44A3 activity raises DLEU1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without SLC44A3 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[LINC01814]] | B | LINC01814 activity raises DLEU1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without LINC01814 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF18]] | B | DLEU1 activity raises TM4SF18's level | lines that do not express DLEU1 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without DLEU1 | 0.046 | ⚠ within organs, on part of the lines; also absent: MLXIPL, TESC, PDE3B; maybe low, not absent |
| [[TSHZ3]] | B | DLEU1 activity weakens TSHZ3's drug response | lines that do not express DLEU1 (12) vs lines expressing it (11) | the lines without DLEU1 respond 1.39× as strongly (z diff -0.98); strongest at Dinaciclib 5 µM: 0.20x vs 0.54x (z diff -5.1) | 0.069 | ⚠ within organs, on part of the lines; also absent: MLXIPL, TESC, PDE3B; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 45.3); signed map (58.8, 16.7). **Vector** length 110, 35.9% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.4 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +5.6 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.5 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | -4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -6.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.6 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | -4.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.1 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -6.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | deleted in lymphocytic leukemia 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q14.2-q14.3 — chr13:50,082,169-50,906,856 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LEU1, XTP6, NCRNA00021, LINC00021, BCMS1; previously DLB1, BCMS |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Function**, from UniProt [O43261](https://www.uniprot.org/uniprotkb/O43261) (Leukemia-associated protein 1):

> May act as a tumor suppressor.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13747) · Entrez [10301](https://www.ncbi.nlm.nih.gov/gene/10301) · UniProt [O43261](https://www.uniprot.org/uniprotkb/O43261) · Ensembl [ENSG00000176124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176124)

## Data

Gene col 10685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10685); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10685]; `tensor/DDL_lfc|DDL_z.npy` [10685]; `embed/gene_vectors.npy` [10685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10685 or target_col == 10685). Every well: [[DLEU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLEU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
