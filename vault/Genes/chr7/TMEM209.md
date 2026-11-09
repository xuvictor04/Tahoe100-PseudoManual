---
symbol: "TMEM209"
type: "gene"
col: 7126
ensembl_id: "ENSG00000146842"
name: "transmembrane protein 209"
location: "7q32.2"
module: 1
arm: "+"
pooled_cpm: 34.86
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TMEM209

*transmembrane protein 209* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.89× (z +13.0, q 1e-35, up in 31 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.29× (z +5.4, q 6e-06, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 6.31×, A498 2.42×, A549 3.08×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HS-578T 7.17×, A498 3.21×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 3.14×, Panc 03.27 3.06×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.768× (z -7.9, q 1e-12, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (SW480 0.464×, SNU-1 0.201×, J82 0.465×, C-33 A 0.468×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (PANC-1 0.382×, BT-474 0.230×, SW1417 0.420×, NCI-H460 0.436×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.375×, MIA PaCa-2 0.363×; ⚠ cell-cycle shift, explains ~85% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.0931×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFT1]] (+0.74, fdr 7e-06), [[UMPS]] (+0.66, fdr 7e-06), [[RNASEH2B]] (+0.66, fdr 7e-06); moves opposite to [[ZSWIM6]] (-0.59, fdr 1e-05), [[ARIH1]] (-0.57, fdr 3e-05), [[IFRD1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SNAI1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7126.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 6.31×, A498 2.42×, A549 3.08×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HS-578T 7.17×, A498 3.21×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 3.14×, Panc 03.27 3.06×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +13.0 | 1e-35 | 31/41 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +11.6 | 9e-29 | 40/46 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +10.1 | 9e-22 | 35/46 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +6.1 | 1e-07 | 20/43 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +6.0 | 2e-07 | 20/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +5.8 | 6e-07 | 23/48 (SNU-423, A549, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.4 | 6e-06 | 20/48 (HT-29, AN3 CA, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 1e-05 | 21/47 (A-427, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.2 | 0.002 | 9/47 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +4.0 | 0.003 | 10/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +4.0 | 0.003 | 17/47 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.016 | 11/47 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.016 | 4/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.18× | +3.5 | 0.018 | 5/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.021 | 12/48 (Panc 03.27, NCI-H23, …) | top dose only |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.025 | 7/47 (A-172, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.082 | 11/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.094 | 7/47 (Hs 766T, SNU-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7126.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (SW480 0.464×, SNU-1 0.201×, J82 0.465×, C-33 A 0.468×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (PANC-1 0.382×, BT-474 0.230×, SW1417 0.420×, NCI-H460 0.436×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.375×, MIA PaCa-2 0.363×; ⚠ cell-cycle shift, explains ~85% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (HCT15 0.0931×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -7.9 | 1e-12 | 30/48 (SW480, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -6.6 | 9e-09 | 24/48 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.785×** | -5.2 | 5e-05 | 21/47 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -4.7 | 4e-04 | 20/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.892× | -3.5 | 0.061 | 19/47 (SK-MEL-2, MIA PaCa-2, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.3 | 0.098 | 18/48 (CHP-212, Hs 766T, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.816× | -3.1 | 0.14 | 8/48 (HCT15, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.903× | -3.1 | 0.14 | 5/48 (SNU-1, A549, …) | top dose only |  |
| [[Artemether (drug)]] 0.05 µM |  | 0.867× | -3.1 | 0.14 | 5/48 (SNU-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.905× | -3.0 | 0.15 | 7/48 (KATO III, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.8 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -11.9) |
| [[A498 (line)]] | wt | 69.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +14.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.1) |
| [[HS-578T (line)]] | alt | 35.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.17× (z +16.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.0) |
| [[C-33 A (line)]] | alt | 78.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.5) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 26.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.06× (z +8.5) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.190× (z -12.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 48.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.236× (z -8.5) |
| [[SW480 (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -14.4) |
| [[A549 (line)]] | wt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -9.1) |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0931× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 35.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.5) |
| [[KATO III (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.14× (z +10.1) ⚠ toxic | — |
| [[RKO (line)]] | wt | 50.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -12.1) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SNU-1 (line)]] | wt | 35.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -14.0) |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.258× (z -9.7) |
| [[SW1417 (line)]] | alt | 53.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.420× (z -9.1) |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFT1]] | +0.74 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[UMPS]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RNASEH2B]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[NAE1]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[DCAF17]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[MRPL3]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[AGK]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[C5orf22]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SNRNP40]] | +0.63 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[EEF1E1]] | +0.62 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[TADA2A]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ELMOD2]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ARIH1]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[IFRD1]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SPSB2]] | -0.56 | -0.40 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAI1]] | B | SNAI1 activity raises TMEM209's level | lines that do not express SNAI1 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without SNAI1 | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFSF9; maybe low, not absent |
| [[ZMIZ1]] | C | ZMIZ1 activity lowers TMEM209's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without ZMIZ1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.7, -38.3); signed map (-3.9, -39.6). **Vector** length 104, 23.6% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.9 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.2 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 209 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:130,164,713-130,207,770 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14803, NET31 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SK2](https://www.uniprot.org/uniprotkb/Q96SK2) (Transmembrane protein 209):

> Nuclear envelope protein which in association with NUP205, may be involved in nuclear transport of various nuclear proteins in addition to MYC.

**Summary**, from NCBI Gene [84928](https://www.ncbi.nlm.nih.gov/gene/84928):

> Predicted to be located in Golgi apparatus and nuclear envelope. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21898) · Entrez [84928](https://www.ncbi.nlm.nih.gov/gene/84928) · UniProt [Q96SK2](https://www.uniprot.org/uniprotkb/Q96SK2) · Ensembl [ENSG00000146842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146842)

## Data

Gene col 7126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7126); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7126]; `tensor/DDL_lfc|DDL_z.npy` [7126]; `embed/gene_vectors.npy` [7126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7126 or target_col == 7126). Every well: [[TMEM209 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM209.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
