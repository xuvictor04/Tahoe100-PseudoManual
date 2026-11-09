---
symbol: "TPRG1"
type: "gene"
col: 11965
ensembl_id: "ENSG00000188001"
name: "tumor protein p63 regulated 1"
location: "3q28"
module: 10
arm: "+"
pooled_cpm: 26.17
n_lines_expressing: 40
n_dd_up: 18
n_dd_down: 22
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TPRG1

*tumor protein p63 regulated 1* — 3q28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.49× (z +6.1, q 6e-07, up in 21 of 38 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.40× (z +5.2, q 7e-05, up in 16 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.406× (z -9.7, q 2e-19, down in 28 of 38 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.348× (z -6.0, q 2e-07, down in 23 of 39 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXPH1]] (+0.68, fdr 2e-05), [[GUCY1B2]] (+0.65, fdr 1e-05), [[DPH6-DT]] (+0.63, fdr 1e-05); moves opposite to [[SOCS7]] (-0.51, fdr 6e-05), [[PI4KAP2]] (-0.50, fdr 8e-05), [[MPG]] (-0.50, fdr 0.002, ⚠ one half only (not replicated)), [[SRD5A1]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02211]] → it (grade B ⚠); 3 go from it, the strongest it → [[LRGUK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.49×** | +6.1 | 6e-07 | 21/38 (J82, A-427, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +5.2 | 7e-05 | 16/36 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.4 | 0.002 | 10/38 (KATO III, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.47×** | +4.2 | 0.004 | 16/38 (LoVo, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +4.2 | 0.004 | 20/37 (KATO III, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.007 | 15/38 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.42×** | +3.8 | 0.011 | 9/38 (KATO III, HT-29, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.011 | 13/38 (KATO III, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.7 | 0.016 | 7/25 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.016 | 10/38 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.029 | 10/38 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.031 | 9/37 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.032 | 13/37 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.77×** | +3.2 | 0.048 | 8/38 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.060 | 16/36 (SW480, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.065 | 13/37 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.69×** | +3.0 | 0.098 | 7/36 (A-172, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.098 | 11/37 (SW480, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.406×** | -9.7 | 2e-19 | 28/38 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.421×** | -9.3 | 3e-18 | 28/38 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.462×** | -8.3 | 2e-14 | 29/37 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.474×** | -8.0 | 1e-13 | 25/36 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.477×** | -8.0 | 2e-13 | 26/38 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.491×** | -7.7 | 2e-12 | 30/38 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.556×** | -6.3 | 2e-08 | 24/36 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -6.0 | 2e-07 | 21/32 (hTERT-HPNE, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.348×** | -6.0 | 2e-07 | 23/39 (MIA PaCa-2, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -5.7 | 6e-07 | 20/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.571×** | -5.7 | 8e-07 | 20/37 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.590×** | -5.5 | 2e-06 | 21/32 (NCI-H460, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -5.4 | 4e-06 | 19/34 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.637×** | -4.7 | 1e-04 | 17/37 (NCI-H460, NCI-H1792, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.650×** | -4.6 | 1e-04 | 22/35 (J82, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -4.5 | 3e-04 | 18/38 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.698×** | -3.6 | 0.009 | 15/38 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.639×** | -3.4 | 0.017 | 10/38 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.753×** | -2.9 | 0.088 | 9/38 (MIA PaCa-2, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.0 | 0 | 22 (17 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0659× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 225 | 0 | 18 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -21.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.6) |
| [[A549 (line)]] | wt | 40.1 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 81.1 | 0 | 9 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -15.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 36.0 | 1 (1 ⚠) | 7 (7 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +9.0) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.116× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.0) |
| [[SW480 (line)]] | alt | 32.1 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0861× (z -15.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -8.5) |
| [[A498 (line)]] | wt | 37.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -18.8) |
| [[SHP-77 (line)]] | alt | 56.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -11.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW 900 (line)]] | alt | 39.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0595× (z -11.2) ⚠ toxic · without an alert: [[Canagliflozin (drug)]] 5 µM 0.0610× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.148× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 6.65 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM 0.0477× (z -8.8) |
| [[HS-578T (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +11.0) | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.209× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXPH1]] | +0.68 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[GUCY1B2]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[DPH6-DT]] | +0.63 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.63 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[DLG2]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | +0.59 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[KIAA0825]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[LINC00240]] | +0.59 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[CASC9]] | +0.59 | +0.65 / +0.37 | both halves | 9e-05 |  |
| [[LINC00486]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | +0.58 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[LINC02398]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS7]] | -0.51 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[PI4KAP2]] | -0.50 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[MPG]] | -0.50 | -0.65 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[TMEM120B]] | -0.50 | -0.54 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[SRD5A1]] | -0.50 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[IDH2]] | -0.49 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[PIGF]] | -0.49 | -0.46 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02211]] | B | LINC02211 activity raises TPRG1's level | lines that do not express LINC02211 (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without LINC02211 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02945, LINC01035, PSG5 |
| [[LINC02428]] | B | LINC02428 activity raises TPRG1's level | lines that do not express LINC02428 (32) vs lines expressing it (18) | 1.66× lower at baseline in the lines without LINC02428 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ENSG00000287598, ENSG00000287474 |
| [[CD226]] | B | CD226 activity raises TPRG1's level | lines that do not express CD226 (7) vs lines expressing it (43) | 2.84× lower at baseline in the lines without CD226 | 0.069 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |
| [[CASC9]] | B | CASC9 activity raises TPRG1's level | lines that do not express CASC9 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without CASC9 | 0.075 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5 |
| [[CASC9]] | B | CASC9 activity strengthens TPRG1's drug response | lines that do not express CASC9 (16) vs lines expressing it (23) | the lines without CASC9 respond 0.50× as strongly (z diff +2.08); strongest at Digitoxin 5 µM: 0.56x vs 0.29x (z diff +3.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRGUK]] | B | TPRG1 activity raises LRGUK's level | lines that do not express TPRG1 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without TPRG1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SYCP2L; maybe low, not absent |
| [[DLG2]] | B | TPRG1 activity raises DLG2's level | lines that do not express TPRG1 (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without TPRG1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SYCP2L; maybe low, not absent |
| [[PMFBP1]] | C | TPRG1 activity raises PMFBP1's level | lines that do not express TPRG1 (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without TPRG1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SYCP2L; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (18.0, 20.7); signed map (33.1, -11.7). **Vector** length 79.9, 17.5% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.5 | -8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.2 | -8.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.3 | -7.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.6 | -0.3 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein p63 regulated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q28 — chr3:188,947,214-189,325,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41238, FLJ43694; previously FAM79B |
| Matched by | ensembl_id |

UniProt [Q6ZUI0](https://www.uniprot.org/uniprotkb/Q6ZUI0) carries no function annotation.

**Summary**, from NCBI Gene [285386](https://www.ncbi.nlm.nih.gov/gene/285386):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24759) · Entrez [285386](https://www.ncbi.nlm.nih.gov/gene/285386) · UniProt [Q6ZUI0](https://www.uniprot.org/uniprotkb/Q6ZUI0) · Ensembl [ENSG00000188001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188001)

## Data

Gene col 11965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11965); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11965]; `tensor/DDL_lfc|DDL_z.npy` [11965]; `embed/gene_vectors.npy` [11965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11965 or target_col == 11965). Every well: [[TPRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
