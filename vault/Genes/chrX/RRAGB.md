---
symbol: "RRAGB"
type: "gene"
col: 1378
ensembl_id: "ENSG00000083750"
name: "Ras related GTP binding B"
location: "Xp11.21"
module: 122
arm: "+"
pooled_cpm: 21.28
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# RRAGB

*Ras related GTP binding B* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.61× (z +9.8, q 5e-20, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +7.3, q 7e-11, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.633× (z -6.7, q 9e-09, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 0.765× (z -3.8, q 0.011, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1573 0.132×, SW480 0.293×, A-427 0.215×, LoVo 0.250×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.128×, MIA PaCa-2 0.220×, NCI-H2030 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (COLO 205 0.0549×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.138×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SW48 0.0994×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC2C]] (+0.74, fdr 7e-06), [[HPS1]] (+0.71, fdr 1e-05), [[ARMCX5-GPRASP2]] (+0.70, fdr 7e-06); moves opposite to [[EHD4]] (-0.64, fdr 1e-05), [[LSM4]] (-0.63, fdr 1e-05), [[SRGAP2C]] (-0.61, fdr 4e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.61×** | +9.8 | 5e-20 | 41/48 (A-172, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.66×** | +7.4 | 5e-11 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +7.3 | 7e-11 | 27/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.9 | 1e-04 | 22/46 (SW480, SW48, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.003 | 21/48 (HOP62, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.87×** | +4.0 | 0.005 | 10/47 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.29×** | +3.7 | 0.016 | 13/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.020 | 9/47 (SW1417, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.020 | 9/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.32×** | +3.5 | 0.025 | 16/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.030 | 14/47 (KATO III, LS 180, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.4 | 0.030 | 12/48 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.18× | +3.3 | 0.042 | 8/48 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.074 | 5/46 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.077 | 9/47 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1378.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1573 0.132×, SW480 0.293×, A-427 0.215×, LoVo 0.250×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.128×, MIA PaCa-2 0.220×, NCI-H2030 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (COLO 205 0.0549×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.138×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SW48 0.0994×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.633×** | -6.7 | 9e-09 | 31/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.647×** | -6.4 | 4e-08 | 32/47 (SW480, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.669×** | -5.9 | 6e-07 | 25/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.730×** | -4.6 | 5e-04 | 22/41 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.731×** | -4.5 | 1e-03 | 16/30 (KATO III, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.815×** | -4.3 | 0.002 | 22/48 (CHP-212, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.011 | 16/47 (H4, NCI-H2030, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.786×** | -3.6 | 0.024 | 18/47 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.794×** | -3.4 | 0.040 | 16/47 (H4, HT-29, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **0.805×** | -3.2 | 0.071 | 18/45 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 5 µM |  | 0.860× | -3.2 | 0.078 | 10/48 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.814× | -3.1 | 0.10 | 11/48 (A549, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 38.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 26.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 31.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +18.8) | — |
| [[A-172 (line)]] | wt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[A549 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.279× (z -8.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[C32 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0549× (z -14.8) |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.138× (z -9.9) |
| [[Hs 766T (line)]] | wt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.2) | — |
| [[J82 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +9.5) | — |
| [[KATO III (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 9.84 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +8.7) | — |
| [[SW48 (line)]] | wt | 22.4 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0994× (z -9.9) |
| [[A498 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC2C]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[HPS1]] | +0.71 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ARMCX5-GPRASP2]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[WASHC2A]] | +0.70 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ATP6V1C1]] | +0.67 | +0.68 / +0.68 | both halves | 7e-06 | pathway: Amino acids regulate mTORC1; STRING 554 |
| [[GPRASP3]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[TMEM192]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[LINC01278]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[HEXA]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[C1orf43]] | +0.65 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CLN3]] | +0.65 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[CC2D2A]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[LSM4]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[SRGAP2C]] | -0.61 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[MAPKAPK2]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PGP]] | -0.58 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[ADARB1]] | -0.57 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[MYCBP]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.56 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[TMEM184B]] | -0.56 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[RCOR1]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[ECE1]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RRM2]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RRAGB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GPRASP3]] | C | GPRASP3 activity raises RRAGB's level | lines that do not express GPRASP3 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without GPRASP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DCP1B, ST8SIA5, DISC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.9, 14.1); signed map (16.3, -14.3). **Vector** length 88.8, 18.6% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +8.8 | +9.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.4 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Afatinib (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -5.6 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.3 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -5.3 | -6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Ras related GTP binding B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:55,717,749-55,758,774 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ras related GTP binding proteins |
| Reactome | 15 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VZM2](https://www.uniprot.org/uniprotkb/Q5VZM2) (Ras-related GTP-binding protein B):

> Guanine nucleotide-binding protein that plays a crucial role in the cellular response to amino acid availability through regulation of the mTORC1 signaling cascade. Forms heterodimeric Rag complexes with RagC/RRAGC or RagD/RRAGD and cycles between an inactive GDP-bound and an active GTP-bound form: RagB/RRAGB is in its active form when GTP-bound RagB/RRAGB forms a complex with GDP-bound RagC/RRAGC (or RagD/RRAGD) and in an inactive form when GDP-bound RagB/RRAGB heterodimerizes with GTP-bound …

**Summary**, from NCBI Gene [10325](https://www.ncbi.nlm.nih.gov/gene/10325):

> Ras-homologous GTPases constitute a large family of signal transducers that alternate between an activated, GTP-binding state and an inactivated, GDP-binding state. These proteins represent cellular switches that are operated by GTP-exchange factors and factors that stimulate their intrinsic GTPase activity. All GTPases of the Ras superfamily have in common the presence of six conserved motifs involved in GTP/GDP binding, three of which are phosphate-/magnesium-binding sites (PM1-PM3) and three …

**Accessions** — [HGNC:19901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19901) · Entrez [10325](https://www.ncbi.nlm.nih.gov/gene/10325) · UniProt [Q5VZM2](https://www.uniprot.org/uniprotkb/Q5VZM2) · Ensembl [ENSG00000083750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083750)

## Data

Gene col 1378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1378); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1378]; `tensor/DDL_lfc|DDL_z.npy` [1378]; `embed/gene_vectors.npy` [1378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1378 or target_col == 1378). Every well: [[RRAGB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAGB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
