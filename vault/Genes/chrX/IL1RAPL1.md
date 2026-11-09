---
symbol: "IL1RAPL1"
type: "gene"
col: 9795
ensembl_id: "ENSG00000169306"
name: "interleukin 1 receptor accessory protein like 1"
location: "Xp21.3-p21.2"
module: 13
arm: "+"
pooled_cpm: 129.11
n_lines_expressing: 22
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# IL1RAPL1

*interleukin 1 receptor accessory protein like 1* — Xp21.3-p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +9.4, q 2e-18, up in 6 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.572× (z -8.9, q 2e-16, down in 17 of 20 measured lines) ⚠ toxic. The strongest without an alert is [[Clobetasol propionate (drug)]] 5 µM: 0.680× (z -6.4, q 2e-08, down in 10 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00973]] (+0.68, fdr 7e-06), [[SIGLEC15]] (+0.62, fdr 1e-05), [[CSMD2]] (+0.61, fdr 1e-05); moves opposite to [[TSC22D3]] (-0.51, fdr 1e-05), [[UGP2]] (-0.46, fdr 4e-05), [[CPD]] (-0.44, fdr 9e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC02220]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +9.4 | 2e-18 | 6/20 (hTERT-HPNE, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.8 | 3e-16 | 1/21 (hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.8 | 3e-16 | 1/21 (hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.7 | 2e-06 | 8/20 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 2e-06 | 4/20 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.4 | 5e-06 | 1/20 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 5e-06 | 5/21 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.6 | 3e-04 | 8/20 (C32, SK-MEL-2, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 1/21 (NCI-H2347) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.1 | 0.002 | 0/20 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.008 | 8/20 (C32, SNU-423, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.011 | 7/20 (C32, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +3.2 | 0.058 | 8/20 (C32, LOX-IMVI, …) | top dose only | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.080 | 2/20 (PANC-1, H4) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.096 | 5/20 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9795.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -8.9 | 2e-16 | 17/20 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.662×** | -6.9 | 2e-09 | 19/20 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.680×** | -6.4 | 2e-08 | 10/20 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.720×** | -5.5 | 6e-06 | 9/20 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.730×** | -5.2 | 2e-05 | 14/20 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.736×** | -5.1 | 3e-05 | 17/20 (Hs 766T, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.745×** | -4.8 | 1e-04 | 12/20 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.755×** | -4.7 | 2e-04 | 10/20 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.769×** | -4.4 | 8e-04 | 10/20 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.772×** | -4.3 | 9e-04 | 11/20 (H4, SNU-423, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.772×** | -4.3 | 9e-04 | 16/20 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.740×** | -4.1 | 0.002 | 6/20 (HOP62, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.746×** | -4.0 | 0.003 | 9/20 (HOP62, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.797×** | -3.8 | 0.007 | 9/20 (H4, AsPC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.854× | -3.7 | 0.007 | 9/20 (H4, Hs 766T, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.856× | -3.7 | 0.009 | 10/20 (A-172, CHP-212, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.804×** | -3.5 | 0.016 | 12/21 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.863× | -3.5 | 0.017 | 11/20 (LoVo, PANC-1, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.819×** | -3.3 | 0.025 | 7/20 (H4, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.045 | 14/20 (HOP62, SNU-423, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.833× | -3.0 | 0.075 | 12/20 (HOP62, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 380 | 0 | 20 (7 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.519× (z -16.0) ⚠ position not correctable · without an alert: [[Budesonide (drug)]] 0.05 µM 0.189× (z -12.0) |
| [[SNU-423 (line)]] | alt | 485 | 0 | 15 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -14.9) |
| [[C32 (line)]] | wt | 265 | 12 (7 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.01× (z +13.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 3.16× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.0) |
| [[Hs 766T (line)]] | wt | 1,402 | 0 | 12 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0728× (z -16.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -15.6) |
| [[LoVo (line)]] | wt | 396 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -21.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 563 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 210 | 2 (2 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.01× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.131× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.5) |
| [[A-172 (line)]] | wt | 199 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.190× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 73.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 578 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.9) |
| [[A-427 (line)]] | wt | 47.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0965× (z -11.1) ⚠ toxic |
| [[H4 (line)]] | wt | 89.1 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.159× (z -9.0) |
| [[PANC-1 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.280× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 74.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.249× (z -9.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 28.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 25.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00973]] | +0.68 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SIGLEC15]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[CSMD2]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[NHSL2]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[AFF3]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SLC14A1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[IL11]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NGF]] | +0.57 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ROR1-AS1]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[LINC01435]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[LINC01204]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LINC02930]] | +0.53 | +0.39 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[UGP2]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CPD]] | -0.44 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[SLC19A2]] | -0.43 | -0.40 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers IL1RAPL1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[RGS4]] | C | RGS4 activity raises IL1RAPL1's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 4.49× lower at baseline in the lines without RGS4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises IL1RAPL1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 4.59× lower at baseline in the lines without CCDC190 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[LINC01204]] | C | LINC01204 activity raises IL1RAPL1's level | lines that do not express LINC01204 (22) vs lines expressing it (28) | 3.34× lower at baseline in the lines without LINC01204 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC00460, WNT5A, LNCOG; maybe low, not absent; co-absent with the target |
| [[LAMA4]] | C | LAMA4 activity raises IL1RAPL1's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 3.59× lower at baseline in the lines without LAMA4 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[SIM1]] | C | SIM1 activity raises IL1RAPL1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 4.26× lower at baseline in the lines without SIM1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02220]] | B | IL1RAPL1 activity raises LINC02220's level | lines that do not express IL1RAPL1 (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without IL1RAPL1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ROBO2, EPB41L3, MMP2 |
| [[LINC01776]] | C | IL1RAPL1 activity raises LINC01776's level | lines that do not express IL1RAPL1 (28) vs lines expressing it (22) | 2.27× lower at baseline in the lines without IL1RAPL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ROBO2, EPB41L3, MMP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.385). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.7, 12.2); signed map (17.9, 48.6). **Vector** length 91.2, 26.5% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +3.9 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | -1.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -5.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor accessory protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.3-p21.2 — chrX:28,587,446-29,956,718 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OPHN4, TIGIRR-2, IL1R8, IL1RAPL-1; previously IL1RAPL, MRX34, MRX21, MRX10 |
| Gene groups (HGNC) | I-set domain containing; Interleukin receptors; TIR domain containing; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; Interleukin-1 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZN1](https://www.uniprot.org/uniprotkb/Q9NZN1) (Interleukin-1 receptor accessory protein-like 1):

> May regulate secretion and presynaptic differentiation through inhibition of the activity of N-type voltage-gated calcium channel. May activate the MAP kinase JNK. Plays a role in neurite outgrowth (By similarity). During dendritic spine formation can bidirectionally induce pre- and post-synaptic differentiation of neurons by trans-synaptically binding to PTPRD (By similarity).

**Summary**, from NCBI Gene [11141](https://www.ncbi.nlm.nih.gov/gene/11141):

> The protein encoded by this gene is a member of the interleukin 1 receptor family and is similar to the interleukin 1 accessory proteins. This protein has an N-terminal signal peptide, three extracellular immunoglobulin Ig-like domains, a transmembrane domain, an intracellular Toll/IL-1R domain, and a long C-terminal tail which interacts with multiple signalling molecules. This gene is located at a region on chromosome X that is associated with a non-syndromic form of X-linked intellectual …

**Accessions** — [HGNC:5996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5996) · Entrez [11141](https://www.ncbi.nlm.nih.gov/gene/11141) · UniProt [Q9NZN1](https://www.uniprot.org/uniprotkb/Q9NZN1) · Ensembl [ENSG00000169306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169306)

## Data

Gene col 9795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9795); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9795]; `tensor/DDL_lfc|DDL_z.npy` [9795]; `embed/gene_vectors.npy` [9795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9795 or target_col == 9795). Every well: [[IL1RAPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1RAPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
