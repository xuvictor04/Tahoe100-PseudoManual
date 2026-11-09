---
symbol: "ATP8A1"
type: "gene"
col: 4527
ensembl_id: "ENSG00000124406"
name: "ATPase phospholipid transporting 8A1"
location: "4p13"
module: 45
arm: "+"
pooled_cpm: 28.27
n_lines_expressing: 37
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 21
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ATP8A1

*ATPase phospholipid transporting 8A1* — 4p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.24× (z +36.3, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.530× (z -11.7, q 1e-28, down in 26 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM102B]] (+0.69, fdr 1e-05), [[NR3C2]] (+0.68, fdr 1e-05), [[HMGN3]] (+0.66, fdr 1e-05); moves opposite to [[RAB30-DT]] (-0.65, fdr 2e-05), [[ZNF621]] (-0.65, fdr 1e-05), [[CSTF3]] (-0.62, fdr 6e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); 6 go from it, the strongest it → [[MGAT4A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.24×** | +36.3 | 0e+00 | 33/35 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.18×** | +33.4 | 0e+00 | 32/35 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.15×** | +33.3 | 0e+00 | 34/35 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.67×** | +25.4 | 0e+00 | 31/35 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.83×** | +24.6 | 0e+00 | 34/35 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.76×** | +15.0 | 0e+00 | 32/35 (NCI-H460, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.09×** | +13.5 | 2e-39 | 25/34 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +13.4 | 6e-39 | 24/35 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.92×** | +11.9 | 6e-31 | 24/35 (NCI-H1573, SW 900, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.60×** | +8.6 | 4e-16 | 20/35 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.13×** | +7.2 | 2e-11 | 16/34 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +5.7 | 5e-07 | 14/35 (SK-MEL-2, SNU-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.81×** | +5.7 | 5e-07 | 13/32 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.6 | 9e-07 | 14/32 (SHP-77, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +4.9 | 4e-05 | 6/35 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +4.1 | 0.001 | 8/35 (LS 180, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.530×** | -11.7 | 1e-28 | 26/35 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.634×** | -8.4 | 1e-14 | 22/35 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -6.1 | 2e-07 | 18/35 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.736×** | -5.6 | 2e-06 | 17/35 (AN3 CA, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.731×** | -5.6 | 3e-06 | 19/35 (LoVo, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.751×** | -5.3 | 1e-05 | 12/35 (Hs 766T, RKO, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.823×** | -5.1 | 3e-05 | 21/35 (AN3 CA, Hs 766T, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.610×** | -4.8 | 1e-04 | 13/35 (LS 180, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.781×** | -4.6 | 3e-04 | 15/33 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.652×** | -4.1 | 0.002 | 10/34 (LoVo, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -3.8 | 0.008 | 10/34 (SW 900, SW48, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.872× | -3.6 | 0.015 | 13/35 (LoVo, SW48, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.825×** | -3.6 | 0.016 | 4/35 (KATO III, NCI-H2347, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -3.5 | 0.017 | 18/32 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.023 | 10/34 (HT-29, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.829×** | -3.2 | 0.046 | 8/35 (SW 900, KATO III, …) | all doses, flat |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.845× | -3.1 | 0.060 | 11/34 (CHP-212, Panc 03.27, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.736×** | -3.0 | 0.084 | 9/33 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.855× | -2.9 | 0.095 | 6/35 (SNU-423, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.5 | 5 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.42× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.8) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.308× (z -9.2) |
| [[LoVo (line)]] | wt | 139 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 22.9 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.66× (z +15.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -8.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H2030 (line)]] | alt | 8.07 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 13.4× (z +13.1) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0444× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 8.52 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 15.1× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.9) ⚠ cell-cycle shift, explains ~76% of this change |
| [[SW480 (line)]] | alt | 7.81 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 9.16× (z +13.1) | — |
| [[AN3 CA (line)]] | alt | 289 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -19.1) ⚠ cell-cycle shift, explains ~76% of this change |
| [[RKO (line)]] | wt | 8.36 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 9.87× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 11.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.99× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.36× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.31× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 9.76 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 10.7× (z +10.4) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.107× (z -9.9) |
| [[SW 900 (line)]] | alt | 62.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.28× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[CFPAC-1 (line)]] | alt | 7.25 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 15.7× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 12.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.31× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 36.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.10× (z +11.3) | — |
| [[A-427 (line)]] | wt | 24.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.224× (z -9.7) |
| [[J82 (line)]] | alt | 9.09 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.18× (z +9.4) | — |
| [[KATO III (line)]] | alt | 46.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -10.3) ⚠ toxic |
| [[LS 180 (line)]] | wt | 271 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.186× (z -9.1) |
| [[H4 (line)]] | wt | 10.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 14.1× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 48.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -8.6) |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[Panc 03.27 (line)]] | alt | 9.64 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.73× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[SW48 (line)]] | wt | 87.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM102B]] | +0.69 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NR3C2]] | +0.68 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ATP6V0E2]] | +0.64 | +0.39 / +0.54 | both halves | 6e-05 | pathway: Ion channel transport |
| [[NOS1AP]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[CDON]] | +0.62 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[MPP7]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CAT]] | +0.62 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[TSPAN33]] | +0.62 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.61 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MGAT4A]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[METAP1]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30-DT]] | -0.65 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF621]] | -0.65 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.62 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SCAF1]] | -0.61 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[METTL6]] | -0.61 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ANKLE2]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[LINC01134]] | -0.60 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[NEPRO-AS1]] | -0.59 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[SMIM15-AS1]] | -0.59 | -0.57 / -0.26 | both halves | 3e-04 |  |
| [[SLC9A8]] | -0.59 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ACTR3-AS1]] | -0.59 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[MIRLET7IHG]] | -0.59 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises ATP8A1's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.75× lower at baseline in the lines without NR3C2 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[ERG]] | B | ERG activity weakens ATP8A1's drug response | lines that do not express ERG (23) vs lines expressing it (12) | the lines without ERG respond 1.31× as strongly (z diff -1.45); strongest at Tucidinostat 5 µM: 2.57x vs 1.95x (z diff -2.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PTPN13]] | B | PTPN13 activity raises ATP8A1's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without PTPN13 | 0.077 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[TSPAN12]] | C | TSPAN12 activity raises ATP8A1's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without TSPAN12 | 0.068 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT4A]] | B | ATP8A1 activity raises MGAT4A's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 3.27× lower at baseline in the lines without ATP8A1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[UGT8]] | B | ATP8A1 activity raises UGT8's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without ATP8A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[SLAIN1]] | B | ATP8A1 activity raises SLAIN1's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without ATP8A1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[SYTL4]] | B | ATP8A1 activity raises SYTL4's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without ATP8A1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[MPP7]] | B | ATP8A1 activity raises MPP7's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without ATP8A1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[SLC25A27]] | C | ATP8A1 activity raises SLC25A27's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 3.40× lower at baseline in the lines without ATP8A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.7, 5.5); signed map (-28.7, -5.7). **Vector** length 96.9, 22.8% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +25.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +13.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +24.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +15.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +11.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.9 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.9 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -4.3 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.9 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 8A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p13 — chr4:42,408,373-42,657,121 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIA |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 5 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Q0](https://www.uniprot.org/uniprotkb/Q9Y2Q0) (Phospholipid-transporting ATPase IA):

> Catalytic component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids from the outer to the inner leaflet of various membranes and ensures the maintenance of asymmetric distribution of phospholipids. Phospholipid translocation also seems to be implicated in vesicle formation and in uptake of lipid signaling molecules. In vitro, its ATPase activity is selectively and stereospecifically stimulated by phosphatidylserine (PS). The …

**Summary**, from NCBI Gene [10396](https://www.ncbi.nlm.nih.gov/gene/10396):

> The P-type adenosinetriphosphatases (P-type ATPases) are a family of proteins which use the free energy of ATP hydrolysis to drive uphill transport of ions across membranes. Several subfamilies of P-type ATPases have been identified. One subfamily catalyzes transport of heavy metal ions. Another subfamily transports non-heavy metal ions (NMHI). The protein encoded by this gene is a member of the third subfamily of P-type ATPases and acts to transport amphipaths, such as phosphatidylserine. Two …

**Accessions** — [HGNC:13531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13531) · Entrez [10396](https://www.ncbi.nlm.nih.gov/gene/10396) · UniProt [Q9Y2Q0](https://www.uniprot.org/uniprotkb/Q9Y2Q0) · Ensembl [ENSG00000124406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124406)

## Data

Gene col 4527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4527); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4527]; `tensor/DDL_lfc|DDL_z.npy` [4527]; `embed/gene_vectors.npy` [4527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4527 or target_col == 4527). Every well: [[ATP8A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP8A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
