---
symbol: "DNM2"
type: "gene"
col: 1265
ensembl_id: "ENSG00000079805"
name: "dynamin 2"
location: "19p13.2"
module: 85
arm: "+"
pooled_cpm: 145.51
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# DNM2

*dynamin 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +25.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.719× (z -15.6, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB40B]] (+0.61, fdr 1e-05), [[DCAF11]] (+0.60, fdr 1e-05), [[ABHD12]] (+0.58, fdr 2e-05); moves opposite to [[ZNF391]] (-0.58, fdr 3e-05), [[SBF2-AS1]] (-0.58, fdr 3e-05), [[ZNF525]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SLC44A4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +25.2 | 0e+00 | 44/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +22.1 | 0e+00 | 42/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +19.7 | 0e+00 | 42/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +10.7 | 2e-24 | 29/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +10.3 | 1e-22 | 32/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +8.0 | 2e-13 | 20/49 (C32, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +7.2 | 4e-11 | 25/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +6.6 | 2e-09 | 24/48 (A549, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.17× | +5.3 | 7e-06 | 17/48 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +5.3 | 7e-06 | 19/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.30×** | +4.6 | 3e-04 | 16/49 (MIA PaCa-2, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.13× | +4.1 | 0.002 | 15/48 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.13× | +4.0 | 0.003 | 20/50 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.021 | 14/48 (MIA PaCa-2, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.20× | +3.2 | 0.056 | 9/48 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.083 | 10/48 (H4, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.719×** | -15.6 | 0e+00 | 43/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -12.6 | 1e-33 | 32/48 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.724×** | -10.4 | 7e-23 | 27/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.749×** | -9.7 | 7e-20 | 33/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -9.1 | 7e-18 | 25/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.776×** | -8.5 | 3e-15 | 31/48 (A498, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.762×** | -8.4 | 4e-15 | 28/45 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.783×** | -8.1 | 3e-14 | 28/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.791×** | -7.8 | 3e-13 | 30/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -7.4 | 6e-12 | 28/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.825×** | -6.4 | 8e-09 | 24/49 (HT-29, NCI-H2347, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -6.3 | 1e-08 | 24/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.845× | -5.2 | 9e-06 | 16/47 (AN3 CA, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.874× | -4.5 | 3e-04 | 17/48 (H4, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.002 | 15/48 (A498, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.927× | -3.5 | 0.014 | 7/48 (HT-29, LoVo, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.898× | -3.4 | 0.020 | 17/48 (HS-578T, LoVo, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | 0.839× | -3.1 | 0.065 | 11/49 (HCT15, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 0.845× | -2.9 | 0.098 | 17/47 (LoVo, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 388 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -21.0) |
| [[NCI-H460 (line)]] | wt | 75.7 | 13 (9 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +15.9) | — |
| [[A498 (line)]] | wt | 227 | 0 | 9 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.585× (z -13.6) |
| [[LoVo (line)]] | wt | 313 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -18.1) |
| [[RKO (line)]] | wt | 108 | 6 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -11.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 106 | 6 | 1 | [[Cobimetinib (drug)]] 5 µM 2.25× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.524× (z -8.5) |
| [[J82 (line)]] | alt | 111 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +11.7) | [[Selinexor (drug)]] 5 µM 0.630× (z -10.3) |
| [[KATO III (line)]] | alt | 184 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.427× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 65.6 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 119 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.86× (z +15.8) | [[Selinexor (drug)]] 5 µM 0.637× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 74.4 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 1.96× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -11.4) |
| [[A-172 (line)]] | wt | 141 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.17× (z +12.3) | — |
| [[A-427 (line)]] | wt | 88.0 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.99× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.438× (z -10.1) |
| [[C-33 A (line)]] | alt | 86.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 272 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -11.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.2) |
| [[H4 (line)]] | wt | 80.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.39× (z +10.3) | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -17.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 264 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.571× (z -14.0) |
| [[LS 180 (line)]] | wt | 332 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -11.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.424× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 90.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 110 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.15× (z +13.1) | [[Selinexor (drug)]] 5 µM 0.524× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 103 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 216 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.461× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.539× (z -10.2) |
| [[SW480 (line)]] | alt | 180 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +11.6) | [[Harringtonine (drug)]] 5 µM 0.549× (z -9.1) |
| [[A549 (line)]] | wt | 74.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +12.6) | — |
| [[C32 (line)]] | wt | 89.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +15.3) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[HOP62 (line)]] | alt | 89.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 117 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 189 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 1.87× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.644× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 126 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 115 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +12.7) | — |
| [[SW48 (line)]] | wt | 129 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +12.8) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.45× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 104 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 122 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 86.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.467× (z -13.5) |
| [[HS-578T (line)]] | alt | 167 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.583× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 72.6 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.18× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 87.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.575× (z -8.8) |
| [[SNU-1 (line)]] | wt | 102 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB40B]] | +0.61 | +0.51 / +0.50 | both halves | 1e-05 | same gene group |
| [[DCAF11]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ABHD12]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[CORO2A]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[AGFG2]] | +0.57 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[STK24]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LLGL2]] | +0.56 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[TJP3]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[NECTIN2]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 | pathway: Adherens junctions interactions |
| [[ANXA11]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.56 | +0.52 / +0.46 | both halves | 2e-05 | same gene group; pathway: Clathrin-mediated endocytosis; STRING 849 |
| [[RHPN2]] | +0.55 | +0.54 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF391]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SBF2-AS1]] | -0.58 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF525]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[DUS4L]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[TRMT5]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MSANTD4]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[FAM169A]] | -0.56 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[KICS2]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[GCFC2]] | -0.54 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[C12orf29]] | -0.54 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.54 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ZSCAN12]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A4]] | B | SLC44A4 activity raises DNM2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 1.62× lower at baseline in the lines without SLC44A4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[CREB3L1]] | B | CREB3L1 activity raises DNM2's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.27× lower at baseline in the lines without CREB3L1 | 0.028 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[ST14]] | B | ST14 activity raises DNM2's level | lines that do not express ST14 (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without ST14 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[SERPINA5]] | B | SERPINA5 activity raises DNM2's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.32× lower at baseline in the lines without SERPINA5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[TJP3]] | B | TJP3 activity raises DNM2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without TJP3 | 0.046 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[ESRP1]] | B | ESRP1 activity raises DNM2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without ESRP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TJP3]] | B | TJP3 activity weakens DNM2's drug response | lines that do not express TJP3 (29) vs lines expressing it (19) | the lines without TJP3 respond 1.04× as strongly (z diff -0.32); strongest at Panobinostat 0.5 µM: 2.19x vs 1.38x (z diff -4.6) | 0.068 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; target measured in part of the lines; both ways; artifact flags |
| [[PRR15L]] | B | PRR15L activity raises DNM2's level | lines that do not express PRR15L (38) vs lines expressing it (12) | 1.83× lower at baseline in the lines without PRR15L | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: TMEM30B, CDH17, ENSG00000267881 |
| [[HDAC6]] | B | HDAC6 activity lowers DNM2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[APC]] | C | APC activity strengthens DNM2's drug response | recorded loss-of-function mutation of APC in 7 lines vs 38 not recorded | the APC-altered lines respond 0.91× as strongly (z diff +0.83); strongest at Panobinostat 0.5 µM: 1.07x vs 2.04x (z diff +7.2) | 0.072 | ⚠ tissue-confounded; across organs; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (7.9, 4.3); signed map (-15.8, 38.1). **Vector** length 135, 40.3% of its response variance represented; |z| ≥ 3 in 1,411 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.7 | +25.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.0 | +19.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | +22.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.4 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +0.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -12.0 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.7 | -12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.5 | -9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.0 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.1 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | dynamin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,718,055-10,833,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DYNII, DYN2, CMTDIB, CMTDI1, DI-CMTB, CMT2M |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes; Dynamins |
| Reactome | 36 pathways, smallest: NOSTRIN mediated eNOS trafficking; Formation of annular gap junctions; Gap junction degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P50570](https://www.uniprot.org/uniprotkb/P50570) (Dynamin-2):

> Catalyzes the hydrolysis of GTP and utilizes this energy to mediate vesicle scission at plasma membrane during endocytosis and filament remodeling at many actin structures during organization of the actin cytoskeleton. Plays an important role in vesicular trafficking processes, namely clathrin-mediated endocytosis (CME), exocytic and clathrin-coated vesicle from the trans-Golgi network, and PDGF stimulated macropinocytosis. During vesicular trafficking process, associates to the membrane, …

**Summary**, from NCBI Gene [1785](https://www.ncbi.nlm.nih.gov/gene/1785):

> Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such as bone resorption by osteoclasts. Dynamins bind many proteins that bind actin and other …

**Accessions** — [HGNC:2974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2974) · Entrez [1785](https://www.ncbi.nlm.nih.gov/gene/1785) · UniProt [P50570](https://www.uniprot.org/uniprotkb/P50570) · Ensembl [ENSG00000079805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079805)

## Data

Gene col 1265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1265); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1265]; `tensor/DDL_lfc|DDL_z.npy` [1265]; `embed/gene_vectors.npy` [1265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1265 or target_col == 1265). Every well: [[DNM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
