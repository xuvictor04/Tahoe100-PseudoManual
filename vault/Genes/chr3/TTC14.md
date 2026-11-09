---
symbol: "TTC14"
type: "gene"
col: 8765
ensembl_id: "ENSG00000163728"
name: "tetratricopeptide repeat domain 14"
location: "3q26.33"
module: 57
arm: "+"
pooled_cpm: 64.03
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# TTC14

*tetratricopeptide repeat domain 14* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.30× (z +9.4, q 2e-18, up in 28 of 46 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.38× (z +8.1, q 2e-13, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.592× (z -18.7, q 0e+00, down in 39 of 45 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.677× (z -13.9, q 1e-41, down in 34 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (SHP-77 0.418×, CHP-212 0.183×, LoVo 0.434×, A-172 0.422×, …); [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H1792 0.116×, LoVo 0.225×, AsPC-1 0.220×, PANC-1 0.481×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.456×, NCI-H1792 0.261×; ⚠ cell-cycle shift, explains ~28% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.439×, NCI-H1792 0.378×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.202×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF512]] (+0.70, fdr 1e-05), [[OPA1]] (+0.66, fdr 1e-05), [[DNAJC24]] (+0.63, fdr 3e-05); moves opposite to [[ATRIP]] (-0.54, fdr 2e-04), [[LRRC37A2]] (-0.52, fdr 7e-05), [[ESPL1]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPIN3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.30×** | +9.4 | 2e-18 | 28/46 (LoVo, A498, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +8.1 | 2e-13 | 35/46 (HEC-1-A, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.5 | 1e-11 | 28/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +7.1 | 2e-10 | 22/42 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +7.0 | 3e-10 | 25/46 (HT-29, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +5.9 | 3e-07 | 27/46 (HEC-1-A, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.23×** | +5.3 | 1e-05 | 21/46 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.7 | 2e-04 | 20/45 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.20×** | +4.5 | 5e-04 | 22/45 (LS 180, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +4.2 | 0.001 | 8/47 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.09× | +3.2 | 0.079 | 7/46 (LoVo, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.100 | 5/45 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[IQ 1 (drug)]] 5 µM |  | 1.32× | +3.0 | 0.10 | 4/46 (KATO III, RKO, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8765.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 12 lines (SHP-77 0.418×, CHP-212 0.183×, LoVo 0.434×, A-172 0.422×, …); [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H1792 0.116×, LoVo 0.225×, AsPC-1 0.220×, PANC-1 0.481×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.456×, NCI-H1792 0.261×; ⚠ cell-cycle shift, explains ~28% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.439×, NCI-H1792 0.378×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.592×** | -18.7 | 0e+00 | 39/45 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -13.9 | 1e-41 | 34/46 (SHP-77, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.601×** | -12.4 | 7e-33 | 34/46 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -10.0 | 3e-21 | 34/46 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.705×** | -8.8 | 1e-16 | 30/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.740×** | -7.6 | 3e-12 | 31/46 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.829×** | -4.5 | 5e-04 | 21/45 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.838× | -4.5 | 6e-04 | 21/46 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.846× | -4.2 | 0.002 | 17/46 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.855× | -3.9 | 0.005 | 21/45 (A-427, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~78% of this change | 0.864× | -3.7 | 0.012 | 19/45 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.05 µM |  | 0.859× | -3.5 | 0.019 | 13/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 54.6 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -24.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 54.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -17.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.439× (z -11.3) |
| [[SW480 (line)]] | alt | 77.7 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.443× (z -12.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.9) |
| [[A498 (line)]] | wt | 56.2 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.64× (z +8.5) ⚠ cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.7) |
| [[PANC-1 (line)]] | alt | 102 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.63× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -19.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.605× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 97.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 63.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -31.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.378× (z -10.0) |
| [[A-172 (line)]] | wt | 66.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.48× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.5) |
| [[CHP-212 (line)]] | wt | 76.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.4) |
| [[COLO 205 (line)]] | alt | 59.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 91.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.81× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 57.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.7) |
| [[J82 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -17.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 67.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 73.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.475× (z -8.6) |
| [[RKO (line)]] | wt | 41.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.202× (z -12.8) |
| [[A-427 (line)]] | wt | 98.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -12.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.118× (z -9.5) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -20.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 42.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.603× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 65.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.298× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~78% of this change |
| [[HCT15 (line)]] | alt | 76.7 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.265× (z -8.9) |
| [[HOP62 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 62.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.4) |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 98.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.391× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 69.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.8) |
| [[SHP-77 (line)]] | alt | 90.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -14.7) |
| [[SNU-423 (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF512]] | +0.70 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[OPA1]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[DNAJC24]] | +0.63 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[GTF3C3]] | +0.62 | +0.53 / +0.66 | both halves | 1e-05 | same gene group |
| [[RPRD1A]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TMEM161B]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[LINC03006-1]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ATG5]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[COPS7A]] | +0.59 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[AP3M1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZNF891]] | +0.56 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[SUDS3]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRIP]] | -0.54 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[LRRC37A2]] | -0.52 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[ESPL1]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ERF]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ZC3H6]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[FZD7]] | -0.52 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[FOXA2]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[IRX5]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ENO3]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ZIC2]] | -0.51 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[FAM110A]] | -0.50 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[EMC9]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPIN3]] | C | SPIN3 activity raises TTC14's level | lines that do not express SPIN3 (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without SPIN3 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IRAK2, EXO5, ZNF567; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.1, -14.6); signed map (-31.3, -26.5). **Vector** length 94.6, 21.0% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +6.6 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.1 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.6 | -18.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.7 | -12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.3 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -10.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:180,602,163-180,617,828 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00166, KIAA1980 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q96N46](https://www.uniprot.org/uniprotkb/Q96N46) carries no function annotation.

**Summary**, from NCBI Gene [151613](https://www.ncbi.nlm.nih.gov/gene/151613):

> Predicted to enable nucleic acid binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24697) · Entrez [151613](https://www.ncbi.nlm.nih.gov/gene/151613) · UniProt [Q96N46](https://www.uniprot.org/uniprotkb/Q96N46) · Ensembl [ENSG00000163728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163728)

## Data

Gene col 8765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8765); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8765]; `tensor/DDL_lfc|DDL_z.npy` [8765]; `embed/gene_vectors.npy` [8765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8765 or target_col == 8765). Every well: [[TTC14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
