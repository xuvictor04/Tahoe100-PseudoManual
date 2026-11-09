---
symbol: "GALNT10"
type: "gene"
col: 8963
ensembl_id: "ENSG00000164574"
name: "polypeptide N-acetylgalactosaminyltransferase 10"
location: "5q33.2"
module: 207
arm: "-"
pooled_cpm: 56.05
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# GALNT10

*polypeptide N-acetylgalactosaminyltransferase 10* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.77× (z +28.0, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.577× (z -5.2, q 1e-04, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2030 0.432×, SNU-1 0.264×, J82 0.515×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.261×, A-427 0.546×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.214×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.389×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0727×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX2]] (+0.60, fdr 7e-06), [[ASAP1]] (+0.56, fdr 1e-05), [[EIF2B3]] (+0.55, fdr 1e-05); moves opposite to [[TTC9C]] (-0.63, fdr 1e-05), [[SYNRG]] (-0.63, fdr 1e-04), [[CCDC115]] (-0.57, fdr 7e-05).
> It sits in the **-** arm of [[Module 207]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.77×** | +28.0 | 0e+00 | 45/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.51×** | +27.0 | 0e+00 | 45/46 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.76×** | +23.7 | 0e+00 | 45/46 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +18.5 | 0e+00 | 45/46 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.45×** | +16.1 | 0e+00 | 44/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +15.5 | 0e+00 | 35/46 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +11.1 | 7e-27 | 39/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.81×** | +10.6 | 2e-24 | 28/45 (NCI-H1792, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.72×** | +9.3 | 7e-19 | 25/39 (LoVo, NCI-H1573, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.57×** | +8.8 | 5e-17 | 35/46 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.66×** | +8.4 | 3e-15 | 27/41 (NCI-H2347, CFPAC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.6 | 2e-12 | 30/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +6.6 | 1e-09 | 27/46 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +5.9 | 2e-07 | 25/46 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.5 | 1e-06 | 24/46 (C32, BT-474, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 23/46 (SW1417, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +5.0 | 2e-05 | 21/46 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +4.7 | 7e-05 | 22/46 (NCI-H1792, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.009 | 18/46 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8963.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H2030 0.432×, SNU-1 0.264×, J82 0.515×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.261×, A-427 0.546×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.214×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.389×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0727×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.577×** | -5.2 | 1e-04 | 26/47 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.624×** | -4.4 | 0.003 | 21/45 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.832× | -3.3 | 0.17 | 16/46 (NCI-H2030, SNU-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.889× | -3.0 | 0.37 | 12/46 (SNU-1, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 44.5 | 8 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.54× (z +16.1) | — |
| [[HOP62 (line)]] | alt | 34.5 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +18.6) | — |
| [[NCI-H2347 (line)]] | alt | 34.7 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +15.8) | — |
| [[SW480 (line)]] | alt | 27.1 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +19.8) | — |
| [[HT-29 (line)]] | alt | 35.3 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +14.1) | — |
| [[LoVo (line)]] | wt | 92.2 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.17× (z +13.7) | [[TAK-901 (drug)]] 5 µM 0.233× (z -9.1) |
| [[SNU-423 (line)]] | alt | 45.3 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.92× (z +15.6) | — |
| [[A-172 (line)]] | wt | 51.3 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.57× (z +17.4) | — |
| [[hTERT-HPNE (line)]] | wt | 65.9 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.14× (z +15.2) | — |
| [[NCI-H1792 (line)]] | alt | 59.8 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.61× (z +18.5) | — |
| [[A-427 (line)]] | wt | 99.0 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 2.61× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 61.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 48.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.80× (z +15.5) | — |
| [[HS-578T (line)]] | alt | 85.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +16.6) | — |
| [[J82 (line)]] | alt | 49.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.23× (z +18.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +15.9) | — |
| [[NCI-H2030 (line)]] | alt | 99.8 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.389× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 45.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.83× (z +16.6) | — |
| [[PANC-1 (line)]] | alt | 75.9 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +19.2) | — |
| [[SK-MEL-2 (line)]] | alt | 71.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +14.7) | — |
| [[SW1417 (line)]] | alt | 105 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.44× (z +17.6) | — |
| [[LOX-IMVI (line)]] | wt | 60.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.46× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 65.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 36.5 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.72× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 75.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.86× (z +15.6) | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.62× (z +12.4) | — |
| [[A498 (line)]] | wt | 63.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +15.0) | — |
| [[A549 (line)]] | wt | 65.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.98× (z +15.6) | — |
| [[C32 (line)]] | wt | 43.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 59.3 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -18.5) |
| [[SHP-77 (line)]] | alt | 26.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.46× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 170 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.439× (z -8.5) |
| [[H4 (line)]] | wt | 51.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.18× (z +9.7) | — |
| [[KATO III (line)]] | alt | 39.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +10.2) | — |
| [[RKO (line)]] | wt | 40.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.84× (z +10.4) | — |
| [[SW48 (line)]] | wt | 42.2 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.90× (z +8.9) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.185× (z -9.2) |
| [[C-33 A (line)]] | alt | 60.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[COLO 205 (line)]] | alt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +13.7) | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0727× (z -10.9) |
| [[AN3 CA (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX2]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ASAP1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[EIF2B3]] | +0.55 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[REEP3]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[EIF4G3]] | +0.55 | +0.62 / +0.53 | both halves | 1e-05 | same gene group |
| [[TACC1]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[GALNT1]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 | same gene group; pathway: O-linked glycosylation |
| [[TAF1B]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[AGPS]] | +0.54 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[LDLRAD3]] | +0.53 | +0.46 / +0.51 | both halves | 2e-05 | same gene group |
| [[CMSS1]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9C]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SYNRG]] | -0.63 | -0.36 / -0.69 | both halves | 1e-04 |  |
| [[CCDC115]] | -0.57 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[LRRC27]] | -0.57 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[CERT1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MCCC1]] | -0.55 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[PMS2P4-1]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CDK7]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PEX13]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[APTR]] | -0.54 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[KLC4]] | -0.54 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[COG7]] | -0.53 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **-** arm (projection on the module's main direction -0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-26.7, -8.9); signed map (11.7, 22.5). **Vector** length 103, 28.3% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +18.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +11.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.4 | +16.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +5.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.8 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -12.7 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.4 | +3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.7 | -4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.4 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,190,730-154,420,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T10 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SR1](https://www.uniprot.org/uniprotkb/Q86SR1) (Polypeptide N-acetylgalactosaminyltransferase 10):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Has activity toward Muc5Ac and EA2 peptide substrates.

**Summary**, from NCBI Gene [55568](https://www.ncbi.nlm.nih.gov/gene/55568):

> This gene encodes a member of the GalNAc polypeptide N-acetylgalactosaminyltransferases. These enzymes catalyze the first step in the synthesis of mucin-type oligosaccharides. These proteins transfer GalNAc from UDP-GalNAc to either serine or threonine residues of polypeptide acceptors. The protein encoded by this locus may have increased catalytic activity toward glycosylated peptides compared to activity toward non-glycosylated peptides.[provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:19873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19873) · Entrez [55568](https://www.ncbi.nlm.nih.gov/gene/55568) · UniProt [Q86SR1](https://www.uniprot.org/uniprotkb/Q86SR1) · Ensembl [ENSG00000164574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164574)

## Data

Gene col 8963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8963); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8963]; `tensor/DDL_lfc|DDL_z.npy` [8963]; `embed/gene_vectors.npy` [8963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8963 or target_col == 8963). Every well: [[GALNT10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
