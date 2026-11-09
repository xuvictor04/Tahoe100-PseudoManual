---
symbol: "NRG1"
type: "gene"
col: 8046
ensembl_id: "ENSG00000157168"
name: "neuregulin 1"
location: "8p12"
module: 19
arm: "+"
pooled_cpm: 156.04
n_lines_expressing: 31
n_dd_up: 19
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NRG1

*neuregulin 1* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.85× (z +9.3, q 8e-18, up in 19 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.453× (z -12.6, q 2e-33, down in 26 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH11]] (+0.62, fdr 1e-05), [[NCKAP5]] (+0.60, fdr 1e-05), [[NALCN]] (+0.60, fdr 3e-05); moves opposite to [[SDHAP1]] (-0.56, fdr 2e-05), [[SDHAP2]] (-0.53, fdr 3e-05), [[MAX]] (-0.50, fdr 4e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SIPA1L2]] → it (grade B ⚠); 7 go from it, the strongest it → [[SPATA33]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +9.3 | 8e-18 | 19/29 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +8.0 | 3e-13 | 16/29 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.5 | 2e-08 | 15/29 (A498, A-172, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +6.0 | 2e-07 | 11/27 (hTERT-HPNE, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 1e-06 | 15/30 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.28×** | +5.5 | 4e-06 | 16/29 (A-172, A498, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.1 | 2e-05 | 13/30 (LOX-IMVI, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.8 | 1e-04 | 10/30 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +4.8 | 1e-04 | 15/29 (A549, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.7 | 1e-04 | 13/29 (SNU-423, HS-578T, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 15/29 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.016 | 13/29 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.024 | 12/29 (HS-578T, PANC-1, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.032 | 6/29 (SNU-423, NCI-H661, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.032 | 8/30 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.2 | 0.042 | 9/29 (SHP-77, SW 900, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.057 | 8/29 (A549, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.453×** | -12.6 | 2e-33 | 26/29 (Hs 766T, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.474×** | -11.8 | 9e-30 | 25/29 (Hs 766T, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.493×** | -11.2 | 9e-27 | 26/29 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -7.3 | 5e-11 | 18/29 (SHP-77, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -7.1 | 1e-10 | 19/29 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.765×** | -6.0 | 2e-07 | 12/29 (SHP-77, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.726×** | -5.1 | 3e-05 | 17/29 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.730×** | -5.0 | 4e-05 | 14/29 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.576×** | -4.6 | 3e-04 | 16/29 (SW 900, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.770×** | -4.1 | 0.002 | 15/30 (SW 900, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.788×** | -3.6 | 0.019 | 12/29 (SW 900, SHP-77, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.019 | 11/29 (Hs 766T, A498, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.029 | 11/29 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.030 | 11/29 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.817×** | -3.2 | 0.050 | 6/28 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.822×** | -3.0 | 0.077 | 12/30 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.878× | -2.9 | 0.087 | 10/29 (Hs 766T, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.832×** | -2.9 | 0.090 | 12/29 (J82, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 373 | 0 | 25 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0776× (z -17.1) |
| [[SW 900 (line)]] | alt | 1,605 | 0 | 14 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0753× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 233 | 2 (1 ⚠) | 11 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.55× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.77× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.204× (z -11.9) |
| [[A498 (line)]] | wt | 124 | 7 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +24.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.98× (z +19.1) | [[Clobetasol propionate (drug)]] 0.05 µM 0.381× (z -8.9) |
| [[SHP-77 (line)]] | alt | 1,079 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -20.3) |
| [[A-172 (line)]] | wt | 55.0 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +24.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 14.1× (z +20.0) | — |
| [[A549 (line)]] | wt | 357 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 4.56× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 74.2 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +19.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.299× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 667 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -14.9) |
| [[C-33 A (line)]] | alt | 295 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 497 | 2 (1 ⚠) | 3 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.43× (z +10.3) | [[Adagrasib (drug)]] 0.05 µM 0.588× (z -14.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.2) |
| [[CHP-212 (line)]] | wt | 1,713 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -13.6) |
| [[HOP62 (line)]] | alt | 72.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.77× (z +14.6) | — |
| [[J82 (line)]] | alt | 115 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +14.2) ⚠ cell-cycle shift, explains ~40% of this change | [[Selinexor (drug)]] 5 µM 0.334× (z -12.2) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.294× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 59.6 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 72.3 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.67× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.4) |
| [[SNU-423 (line)]] | alt | 71.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +15.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.63× (z +10.1) | — |
| [[A-427 (line)]] | wt | 124 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.3) ⚠ cell-cycle shift, explains ~40% of this change | [[Panobinostat (drug)]] 5 µM 0.365× (z -8.7) |
| [[C32 (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.211× (z -8.8) |
| [[HS-578T (line)]] | alt | 92.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +13.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.08× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 56.1 | 2 (2 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 7.65× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 58.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +11.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 64.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +15.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 50.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.47× (z +8.8) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.547× (z -13.7) ⚠ position not correctable |
| [[AN3 CA (line)]] | alt | 28.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH11]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[NCKAP5]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NALCN]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[STEAP1B-AS1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[IL7R]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[EBF1]] | +0.59 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[OFCC1]] | +0.59 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[LMNTD1]] | +0.58 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[TLR6]] | +0.58 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ABCC9]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 | pathway: Neuronal System |
| [[ADGRL4]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZNF804A]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[MAX]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[HSPB11]] | -0.50 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[PDPR2P]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[LSP1P5-1]] | -0.49 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[GTF2H2B]] | -0.49 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[C12orf76]] | -0.49 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[SDHAP4]] | -0.48 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[FHIP1B]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[ATPAF2]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SPATA33]] | -0.48 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIPA1L2]] | B | SIPA1L2 activity raises NRG1's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without SIPA1L2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[DOCK4]] | B | DOCK4 activity raises NRG1's level | lines that do not express DOCK4 (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without DOCK4 | 0.088 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[ZNF385D]] | C | ZNF385D activity raises NRG1's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 3.65× lower at baseline in the lines without ZNF385D | 0.063 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[TEX41]] | C | TEX41 activity raises NRG1's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 3.60× lower at baseline in the lines without TEX41 | 0.077 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATA33]] | B | NRG1 activity raises SPATA33's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 1.29× lower at baseline in the lines without NRG1 | 0.056 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23 |
| [[ATPAF2]] | B | NRG1 activity raises ATPAF2's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 1.22× lower at baseline in the lines without NRG1 | 0.082 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23 |
| [[ZNF385D]] | C | NRG1 activity raises ZNF385D's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without NRG1 | 0.056 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |
| [[GLIPR1]] | C | NRG1 activity raises GLIPR1's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 3.18× lower at baseline in the lines without NRG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |
| [[HECW2]] | C | NRG1 activity raises HECW2's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 5.00× lower at baseline in the lines without NRG1 | 0.080 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |
| [[DOCK10]] | C | NRG1 activity raises DOCK10's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 6.60× lower at baseline in the lines without NRG1 | 0.088 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |
| [[NCKAP5]] | C | NRG1 activity raises NCKAP5's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without NRG1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, 27.1); signed map (41.7, 28.7). **Vector** length 112, 29.2% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +10.7 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -12.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -11.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.9 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -2.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | neuregulin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:31,639,222-32,855,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRG, NDF, GGF; previously HGL, NRG1-IT2 |
| Gene groups (HGNC) | I-set domain containing; Neuregulins |
| Reactome | 35 pathways, smallest: GRB7 events in ERBB2 signaling; PI3K events in ERBB4 signaling; Downregulation of ERBB2:ERBB3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02297](https://www.uniprot.org/uniprotkb/Q02297) (Pro-neuregulin-1, membrane-bound isoform):

> Direct ligand for ERBB3 and ERBB4 tyrosine kinase receptors. Concomitantly recruits ERBB1 and ERBB2 coreceptors, resulting in ligand-stimulated tyrosine phosphorylation and activation of the ERBB receptors. The multiple isoforms perform diverse functions such as inducing growth and differentiation of epithelial, glial, neuronal, and skeletal muscle cells; inducing expression of acetylcholine receptor in synaptic vesicles during the formation of the neuromuscular junction; stimulating …

**Summary**, from NCBI Gene [3084](https://www.ncbi.nlm.nih.gov/gene/3084):

> The protein encoded by this gene is a membrane glycoprotein that mediates cell-cell signaling and plays a critical role in the growth and development of multiple organ systems. An extraordinary variety of different isoforms are produced from this gene through alternative promoter usage and splicing. These isoforms are expressed in a tissue-specific manner and differ significantly in their structure, and are classified as types I, II, III, IV, V and VI. Dysregulation of this gene has been linked …

**Accessions** — [HGNC:7997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7997) · Entrez [3084](https://www.ncbi.nlm.nih.gov/gene/3084) · UniProt [Q02297](https://www.uniprot.org/uniprotkb/Q02297) · Ensembl [ENSG00000157168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157168)

## Data

Gene col 8046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8046); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8046]; `tensor/DDL_lfc|DDL_z.npy` [8046]; `embed/gene_vectors.npy` [8046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8046 or target_col == 8046). Every well: [[NRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
