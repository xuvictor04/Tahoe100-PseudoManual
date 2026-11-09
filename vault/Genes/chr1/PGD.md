---
symbol: "PGD"
type: "gene"
col: 6642
ensembl_id: "ENSG00000142657"
name: "phosphogluconate dehydrogenase"
location: "1p36.22"
module: 86
arm: "+"
pooled_cpm: 47.01
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# PGD

*phosphogluconate dehydrogenase* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.42× (z +19.8, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.769× (z -5.9, q 2e-06, down in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.445×, LS 180 0.415×, COLO 205 0.326×; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.491×; ⚠ cell-cycle shift, explains ~28% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[G6PD]] (+0.60, fdr 1e-05), [[TKT]] (+0.59, fdr 1e-05), [[FASN]] (+0.55, fdr 2e-05); moves opposite to [[DTWD1]] (-0.48, fdr 1e-04), [[THOC1]] (-0.45, fdr 5e-05), [[NOP10]] (-0.44, fdr 5e-05, ⚠ NOP10 in the vector space only through flagged drug-doses), [[ZCCHC9]] (-0.44, fdr 3e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AKR1C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +19.8 | 0e+00 | 43/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.66×** | +15.5 | 0e+00 | 43/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.20×** | +12.5 | 1e-33 | 42/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.20×** | +12.5 | 1e-33 | 43/46 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.50×** | +12.2 | 3e-32 | 42/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +11.8 | 5e-30 | 29/48 (HOP62, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.05×** | +10.9 | 6e-26 | 34/37 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +10.5 | 4e-24 | 41/47 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +9.6 | 4e-20 | 38/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +8.4 | 3e-15 | 35/48 (LS 180, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.77×** | +8.3 | 4e-15 | 34/43 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.7 | 6e-13 | 36/48 (HOP62, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +6.7 | 1e-09 | 36/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.53×** | +6.5 | 4e-09 | 30/48 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +6.2 | 3e-08 | 32/43 (CFPAC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.0 | 6e-08 | 28/47 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +5.7 | 5e-07 | 25/48 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.4 | 2e-06 | 27/48 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 5e-06 | 26/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.21×** | +4.2 | 7e-04 | 21/49 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.006 | 17/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.022 | 13/49 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.030 | 13/48 (BT-474, HT-29, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.030 | 17/47 (NCI-H1792, J82, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.058 | 6/46 (MIA PaCa-2, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6642.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.445×, LS 180 0.415×, COLO 205 0.326×; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.491×; ⚠ cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.769×** | -5.9 | 2e-06 | 26/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.729×** | -5.0 | 1e-04 | 27/48 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.798× | -3.4 | 0.13 | 15/48 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.807× | -3.3 | 0.14 | 18/47 (CHP-212, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 11 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 30.9 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.9) | — |
| [[SW480 (line)]] | alt | 40.2 | 9 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 41.7 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +13.6) | — |
| [[A498 (line)]] | wt | 88.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change | [[Selinexor (drug)]] 5 µM 0.445× (z -12.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HEC-1-A (line)]] | alt | 31.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 49.8 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.75× (z +8.9) | [[Selinexor (drug)]] 5 µM 0.415× (z -11.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1792 (line)]] | alt | 41.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[RKO (line)]] | wt | 57.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 43.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 24.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.6) | — |
| [[LoVo (line)]] | wt | 32.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 23.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.5) | — |
| [[A-172 (line)]] | wt | 21.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.1) | — |
| [[A-427 (line)]] | wt | 34.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.9) | — |
| [[J82 (line)]] | alt | 38.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 30.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 27.4 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.68× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 19.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 30.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 37.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[C32 (line)]] | wt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.326× (z -9.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HepG2_C3A (line)]] | wt | 79.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 41.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 42.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.56× (z +8.9) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 58.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 2.67× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 58.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW48 (line)]] | wt | 46.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[G6PD]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 | same gene group; pathway: Cellular response to chemical stress; STRING 999 |
| [[TKT]] | +0.59 | +0.53 / +0.65 | both halves | 1e-05 | pathway: Cellular response to chemical stress; STRING 975 |
| [[FASN]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 | STRING 552 |
| [[HMGCS1]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ACLY]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 | STRING 717 |
| [[SCD]] | +0.53 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[UGDH]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 | same gene group; pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 597 |
| [[DHCR7]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.52 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[AKR1B10]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[NQO1]] | +0.51 | +0.48 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 430 |
| [[PCYT2]] | +0.50 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTWD1]] | -0.48 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[THOC1]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[NOP10]] ⚠ | -0.44 | -0.41 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCCHC9]] | -0.44 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[GEMIN8]] | -0.43 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[THUMPD2]] | -0.43 | -0.21 / -0.51 | both halves | 6e-04 |  |
| [[DCAF10]] | -0.43 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[FBXO28]] | -0.43 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SEC22A]] | -0.42 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[MECR]] | -0.41 | -0.40 / -0.31 | both halves | 2e-04 | same gene group |
| [[MINCR]] | -0.41 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[MYNN]] | -0.41 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[PRPF38B]] | -0.41 | -0.23 / -0.37 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C2]] | B | AKR1C2 activity raises PGD's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 1.96× lower at baseline in the lines without AKR1C2 | 0.005 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[AKR1C1]] | B | AKR1C1 activity raises PGD's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without AKR1C1 | 0.006 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[JAKMIP3]] | B | JAKMIP3 activity raises PGD's level | lines that do not express JAKMIP3 (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without JAKMIP3 | 0.021 | ⚠ within organs, on part of the lines; also absent: RHOU, ABCG1, CASZ1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PGD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AKR1B10]] | B | AKR1B10 activity raises PGD's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 1.83× lower at baseline in the lines without AKR1B10 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.0, -51.4); signed map (-51.3, 30.4). **Vector** length 87.6, 22.6% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.8 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.7 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +9.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | -0.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -6.4 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.9 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | +0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphogluconate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:10,398,592-10,420,511 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 8 pathways, smallest: NFE2L2 regulates pentose phosphate pathway genes; Pentose phosphate pathway; Nuclear events mediated by NFE2L2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P52209](https://www.uniprot.org/uniprotkb/P52209) (6-phosphogluconate dehydrogenase, decarboxylating):

> Catalyzes the oxidative decarboxylation of 6-phosphogluconate to ribulose 5-phosphate and CO(2), with concomitant reduction of NADP to NADPH.

**Summary**, from NCBI Gene [5226](https://www.ncbi.nlm.nih.gov/gene/5226):

> 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:8891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8891) · Entrez [5226](https://www.ncbi.nlm.nih.gov/gene/5226) · UniProt [P52209](https://www.uniprot.org/uniprotkb/P52209) · Ensembl [ENSG00000142657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142657)

## Data

Gene col 6642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6642); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6642]; `tensor/DDL_lfc|DDL_z.npy` [6642]; `embed/gene_vectors.npy` [6642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6642 or target_col == 6642). Every well: [[PGD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
