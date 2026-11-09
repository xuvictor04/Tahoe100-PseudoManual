---
symbol: "DCUN1D4"
type: "gene"
col: 3036
ensembl_id: "ENSG00000109184"
name: "defective in cullin neddylation 1 domain containing 4"
location: "4q12"
module: 163
arm: "+"
pooled_cpm: 108.35
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# DCUN1D4

*defective in cullin neddylation 1 domain containing 4* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.33× (z +5.6, q 1e-05, up in 32 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.24× (z +4.3, q 0.003, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SHP-77 2.33×, NCI-H460 2.02×, PANC-1 1.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 3.17×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 2.95×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.532× (z -17.8, q 0e+00, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.625× (z -9.6, q 2e-19, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC61A2]] (+0.68, fdr 7e-06), [[STRN]] (+0.65, fdr 4e-05), [[GIT1]] (+0.64, fdr 1e-05); moves opposite to [[PPP1R10]] (-0.66, fdr 7e-06), [[ZNF268]] (-0.66, fdr 1e-05), [[FBXO38]] (-0.65, fdr 1e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C21orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3036.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (SHP-77 2.33×, NCI-H460 2.02×, PANC-1 1.83×; ⚠ cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 3.17×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 2.95×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.6 | 1e-05 | 32/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.3 | 3e-05 | 30/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.003 | 23/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.014 | 21/48 (PANC-1, BT-474, …) | two highest doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.4 | 0.051 | 20/49 (SHP-77, C-33 A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.19× | +3.4 | 0.051 | 20/48 (A-427, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.051 | 20/48 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.051 | 12/48 (SHP-77, hTERT-HPNE, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.051 | 8/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.12× | +3.3 | 0.062 | 10/48 (SNU-1, SHP-77, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.17× | +3.2 | 0.068 | 18/50 (NCI-H1573, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.12× | +3.2 | 0.074 | 19/49 (SW480, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.077 | 21/48 (SHP-77, NCI-H460, …) | rises with dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.077 | 21/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.16× | +3.1 | 0.084 | 18/48 (A-427, RPMI-7951, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.532×** | -17.8 | 0e+00 | 39/48 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -9.6 | 2e-19 | 37/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -9.4 | 1e-18 | 39/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -8.7 | 4e-16 | 37/47 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.648×** | -8.6 | 1e-15 | 38/48 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.668×** | -7.6 | 2e-12 | 34/45 (LOX-IMVI, SW48, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -6.7 | 2e-09 | 29/44 (SNU-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.751×** | -5.9 | 3e-07 | 34/49 (RKO, SNU-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.766×** | -5.4 | 3e-06 | 32/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.629×** | -5.0 | 4e-05 | 28/49 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.790×** | -4.8 | 8e-05 | 30/48 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -4.2 | 0.001 | 17/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.819×** | -4.1 | 0.002 | 24/48 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.873× | -3.8 | 0.006 | 7/48 (H4, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -3.4 | 0.027 | 21/48 (SW48, SNU-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.052 | 19/47 (HT-29, HCT15, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.846× | -3.2 | 0.052 | 18/47 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | 0.860× | -3.0 | 0.097 | 16/47 (HT-29, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 136 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -23.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 170 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.389× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 82.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -19.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -19.1) |
| [[NCI-H1573 (line)]] | alt | 92.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -17.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -14.6) |
| [[C32 (line)]] | wt | 141 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -10.4) |
| [[HOP62 (line)]] | alt | 108 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -21.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.475× (z -8.7) |
| [[HS-578T (line)]] | alt | 93.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -21.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 100 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 112 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.607× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 104 | 2 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -12.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.486× (z -10.6) |
| [[SNU-1 (line)]] | wt | 206 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -16.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -18.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 80.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -12.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 114 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 47.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -13.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 42.4 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.17× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.461× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 199 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -14.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -11.7) |
| [[SNU-423 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.469× (z -9.7) |
| [[SW48 (line)]] | wt | 79.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 77.2 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.7) ⚠ cell-cycle shift, explains ~19% of this change | [[Auranofin (drug)]] 5 µM 0.415× (z -12.7) |
| [[A-427 (line)]] | wt | 83.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -17.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -12.5) |
| [[COLO 205 (line)]] | alt | 60.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.24× (z +8.6) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 174 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -9.7) |
| [[SW 900 (line)]] | alt | 124 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.443× (z -9.8) |
| [[SW1417 (line)]] | alt | 68.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.436× (z -8.5) ⚠ toxic |
| [[A498 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 85.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[STRN]] | +0.65 | +0.77 / +0.41 | both halves | 4e-05 |  |
| [[GIT1]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[ABHD12]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CDS2]] | +0.61 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[SEC11A]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SETD3]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZMYM2]] | +0.59 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[LNPK]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[RNF38]] | +0.59 | +0.70 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R10]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[ZNF268]] | -0.66 | -0.70 / -0.53 | both halves | 1e-05 |  |
| [[FBXO38]] | -0.65 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[EPC2]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[PYM1]] | -0.63 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CFLAR-AS1]] | -0.62 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[UTP3]] | -0.61 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.61 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[CWC22]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[HELQ]] | -0.61 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[ZNF502]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.60 | -0.63 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91]] | B | C21orf91 activity lowers DCUN1D4's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 1.55× higher at baseline in the lines without C21orf91 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[EDN1]] | B | EDN1 activity lowers DCUN1D4's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.39× higher at baseline in the lines without EDN1 | 0.040 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[NCEH1]] | B | NCEH1 activity lowers DCUN1D4's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.55× higher at baseline in the lines without NCEH1 | 0.057 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.4, 14.1); signed map (-40.3, -1.5). **Vector** length 129, 40.1% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.0 | +3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.8 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +5.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -11.5 | -17.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.9 | -9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -8.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.2 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | defective in cullin neddylation 1 domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:51,843,000-51,916,837 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0276 |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92564](https://www.uniprot.org/uniprotkb/Q92564) (DCN1-like protein 4):

> Contributes to the neddylation of all cullins by transferring NEDD8 from N-terminally acetylated NEDD8-conjugating E2s enzyme to different cullin C-terminal domain-RBX complexes which are necessary for the activation of cullin-RING E3 ubiquitin ligases (CRLs).

**Summary**, from NCBI Gene [23142](https://www.ncbi.nlm.nih.gov/gene/23142):

> Enables cullin family protein binding activity. Involved in positive regulation of protein neddylation. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28998) · Entrez [23142](https://www.ncbi.nlm.nih.gov/gene/23142) · UniProt [Q92564](https://www.uniprot.org/uniprotkb/Q92564) · Ensembl [ENSG00000109184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109184)

## Data

Gene col 3036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3036); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3036]; `tensor/DDL_lfc|DDL_z.npy` [3036]; `embed/gene_vectors.npy` [3036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3036 or target_col == 3036). Every well: [[DCUN1D4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCUN1D4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
