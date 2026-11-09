---
symbol: "MSH6"
type: "gene"
col: 3756
ensembl_id: "ENSG00000116062"
name: "mutS homolog 6"
location: "2p16.3"
module: 6
arm: "+"
pooled_cpm: 78.28
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MSH6

*mutS homolog 6* — 2p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.61× (z +11.1, q 8e-26, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.44× (z +8.4, q 5e-15, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.670× (z -9.3, q 6e-18, down in 33 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.896× (z -3.6, q 0.022, down in 6 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.199×, C-33 A 0.296×, NCI-H2030 0.337×, A498 0.467×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.268×, SK-MEL-2 0.358×, A-427 0.383×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.285×, NCI-H23 0.399×; ⚠ cell-cycle shift, explains ~26% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.550×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.134×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.644×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP1]] (+0.71, fdr 7e-06), [[CDT1]] (+0.68, fdr 1e-05), [[FAM111B]] (+0.61, fdr 7e-06); moves opposite to [[ZC3H3]] (-0.54, fdr 3e-04), [[MSTO1]] (-0.53, fdr 0.004, ⚠ one half only (not replicated)), [[CTTN]] (-0.49, fdr 2e-04), [[RNF11]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.61×** | +11.1 | 8e-26 | 40/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.60×** | +10.9 | 5e-25 | 32/48 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +10.7 | 2e-24 | 27/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +9.5 | 3e-19 | 31/48 (SHP-77, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +8.4 | 5e-15 | 37/48 (A549, J82, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.43×** | +8.3 | 1e-14 | 33/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.4 | 1e-08 | 31/47 (A549, MIA PaCa-2, …) | all doses, flat | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.3 | 2e-08 | 0/49 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.31×** | +6.3 | 2e-08 | 30/48 (Panc 03.27, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +5.9 | 2e-07 | 29/48 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.4 | 3e-06 | 22/48 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.27×** | +5.3 | 7e-06 | 24/50 (SW480, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.23×** | +4.8 | 7e-05 | 19/48 (MIA PaCa-2, NCI-H2030, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.24×** | +4.8 | 7e-05 | 25/48 (A549, SHP-77, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.7 | 8e-05 | 22/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 1e-04 | 25/48 (SHP-77, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.004 | 15/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Allantoin (drug)]] 5 µM |  | 1.10× | +3.1 | 0.051 | 5/48 (NCI-H23, Hs 766T, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.087 | 8/48 (RKO, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3756.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-172 0.199×, C-33 A 0.296×, NCI-H2030 0.337×, A498 0.467×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.268×, SK-MEL-2 0.358×, A-427 0.383×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.285×, NCI-H23 0.399×; ⚠ cell-cycle shift, explains ~26% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.550×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.134×); [[Amsacrine (drug)]] 5 µM in 1 line (A498 0.644×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.670×** | -9.3 | 6e-18 | 33/49 (SK-MEL-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.706×** | -7.5 | 2e-11 | 29/45 (A-172, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -7.5 | 2e-11 | 26/44 (C-33 A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.838× | -5.8 | 8e-07 | 24/48 (A498, LoVo, …) | rises with dose | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.832×** | -4.3 | 0.002 | 18/48 (J82, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.852× | -3.7 | 0.018 | 20/48 (A498, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.896× | -3.6 | 0.022 | 6/48 (Hs 766T, HT-29, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.901× | -3.4 | 0.041 | 7/49 (Panc 03.27, A-427, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.083 | 14/48 (HOP62, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.10 | 8/47 (HS-578T, SW48, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.913× | -3.0 | 0.13 | 8/48 (KATO III, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 194 | 0 | 8 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.521× (z -13.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.550× (z -12.5) |
| [[A549 (line)]] | wt | 80.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.46× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 40.9 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 168 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -20.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 55.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +8.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Digitoxin (drug)]] 5 µM 0.344× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 85.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -11.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -14.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 56.2 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.134× (z -9.9) |
| [[HOP62 (line)]] | alt | 75.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 70.1 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0755× (z -16.1) ⚠ toxic |
| [[J82 (line)]] | alt | 87.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.00× (z +8.8) | — |
| [[LoVo (line)]] | wt | 55.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Selinexor (drug)]] 5 µM 0.528× (z -10.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LOX-IMVI (line)]] | wt | 52.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1792 (line)]] | alt | 40.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 217 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -15.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 45.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 67.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +9.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -10.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 99.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 94.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -17.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 72.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -9.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 60.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 60.2 | 1 | 0 | [[Methylthiouracil (drug)]] 0.05 µM 4.45× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 53.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.37× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 75.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 88.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 80.9 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.115× (z -9.1) |
| [[SW 900 (line)]] | alt | 65.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 85.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.18× (z +9.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SW480 (line)]] | alt | 86.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.465× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP1]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CDT1]] | +0.68 | +0.51 / +0.74 | both halves | 1e-05 | STRING 578 |
| [[FAM111B]] | +0.61 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ERCC6L]] | +0.58 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[ORC6]] | +0.57 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[DCLRE1B]] | +0.56 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[MCM10]] | +0.56 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[FEN1]] | +0.55 | +0.35 / +0.66 | both halves | 1e-04 | STRING 950 |
| [[THSD8]] ⚠ | +0.55 | +0.42 / +0.64 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MCM6]] | +0.55 | +0.58 / +0.56 | both halves | 1e-05 | STRING 802 |
| [[NXT1]] | +0.55 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[CDC25A]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 | STRING 566 |
| [[CASP8AP2]] | +0.54 | +0.35 / +0.68 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H3]] | -0.54 | -0.29 / -0.60 | both halves | 3e-04 |  |
| [[MSTO1]] | -0.53 | -0.06 / -0.60 | ⚠ one half (not replicated) | 0.004 |  |
| [[CTTN]] | -0.49 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[RNF11]] | -0.48 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[GCC2-AS1]] | -0.47 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[ZNF561-AS1]] | -0.46 | -0.15 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[C8orf44-SGK3]] | -0.46 | -0.18 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[RAD51-AS1]] | -0.45 | -0.25 / -0.50 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MSH6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DLX1]] | B | DLX1 activity raises MSH6's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without DLX1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.3, -48.9); signed map (-42.3, -43.3). **Vector** length 116, 31.5% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.5 | +4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | +2.8 | +4.3 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.3 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +6.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.0 | +1.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.4 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.0 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.9 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -7.1 | -5.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.7 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -1.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | mutS homolog 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.3 — chr2:47,695,530-47,810,063 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSH-6; previously GTBP |
| Gene groups (HGNC) | MutS homologs; PWWP domain containing; BRCA1-associated genome surveillance complex |
| Reactome | 11 pathways, smallest: Defective Mismatch Repair Associated With MSH2; Diseases of Mismatch Repair (MMR); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha) |
| Matched by | ensembl_id |

**Function**, from UniProt [P52701](https://www.uniprot.org/uniprotkb/P52701) (DNA mismatch repair protein Msh6):

> Component of the post-replicative DNA mismatch repair system (MMR). Heterodimerizes with MSH2 to form MutS alpha, which binds to DNA mismatches thereby initiating DNA repair. When bound, MutS alpha bends the DNA helix and shields approximately 20 base pairs, and recognizes single base mismatches and dinucleotide insertion-deletion loops (IDL) in the DNA. After mismatch binding, forms a ternary complex with the MutL alpha heterodimer, which is thought to be responsible for directing the …

**Summary**, from NCBI Gene [2956](https://www.ncbi.nlm.nih.gov/gene/2956):

> This gene encodes a member of the DNA mismatch repair MutS family. In E. coli, the MutS protein helps in the recognition of mismatched nucleotides prior to their repair. A highly conserved region of approximately 150 aa, called the Walker-A adenine nucleotide binding motif, exists in MutS homologs. The encoded protein heterodimerizes with MSH2 to form a mismatch recognition complex that functions as a bidirectional molecular switch that exchanges ADP and ATP as DNA mismatches are bound and …

**Accessions** — [HGNC:7329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7329) · Entrez [2956](https://www.ncbi.nlm.nih.gov/gene/2956) · UniProt [P52701](https://www.uniprot.org/uniprotkb/P52701) · Ensembl [ENSG00000116062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116062)

## Data

Gene col 3756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3756); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3756]; `tensor/DDL_lfc|DDL_z.npy` [3756]; `embed/gene_vectors.npy` [3756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3756 or target_col == 3756). Every well: [[MSH6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSH6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
