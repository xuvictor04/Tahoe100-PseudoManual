---
symbol: "SLCO3A1"
type: "gene"
col: 10722
ensembl_id: "ENSG00000176463"
name: "solute carrier organic anion transporter family member 3A1"
location: "15q26.1"
module: 14
arm: "+"
pooled_cpm: 62.08
n_lines_expressing: 37
n_dd_up: 26
n_dd_down: 18
n_dd_up_clean: 21
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLCO3A1

*solute carrier organic anion transporter family member 3A1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +10.4, q 1e-22, up in 26 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.619× (z -8.5, q 1e-14, down in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.715× (z -5.9, q 5e-07, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP1B]] (+0.61, fdr 1e-05), [[PLCE1]] (+0.59, fdr 1e-05), [[SLCO2B1]] (+0.58, fdr 1e-05); moves opposite to [[WDR37]] (-0.54, fdr 1e-05), [[BCL7C]] (-0.50, fdr 3e-05), [[CRLS1]] (-0.49, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PGBD5]] → it (grade B ⚠); 2 go from it, the strongest it → [[DMD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10722.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +10.4 | 1e-22 | 26/35 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +9.8 | 5e-20 | 17/35 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +8.8 | 2e-16 | 25/35 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +8.5 | 2e-15 | 23/36 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +7.6 | 4e-12 | 18/36 (Panc 03.27, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +7.4 | 2e-11 | 20/35 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +6.2 | 4e-08 | 18/33 (NCI-H460, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.7 | 9e-07 | 20/34 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.9 | 5e-05 | 16/36 (NCI-H2030, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 7e-05 | 17/35 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +4.8 | 8e-05 | 17/35 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +4.7 | 1e-04 | 17/36 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 13/35 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 2e-04 | 17/35 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.20× | +4.5 | 3e-04 | 15/36 (RKO, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 3e-04 | 18/34 (NCI-H460, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +4.2 | 8e-04 | 14/35 (NCI-H460, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10722.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -8.5 | 1e-14 | 25/35 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -8.4 | 2e-14 | 19/28 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.715×** | -5.9 | 5e-07 | 23/36 (Panc 03.27, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -5.9 | 5e-07 | 22/35 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.831×** | -4.6 | 3e-04 | 15/36 (SHP-77, Panc 03.27, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.606×** | -4.6 | 3e-04 | 19/33 (Panc 03.27, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.853× | -4.0 | 0.005 | 10/36 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.802×** | -3.9 | 0.007 | 14/35 (SHP-77, AsPC-1, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.663×** | -3.8 | 0.009 | 16/34 (LoVo, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.808×** | -3.8 | 0.009 | 16/34 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.811×** | -3.7 | 0.010 | 16/35 (SHP-77, AsPC-1, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.863× | -3.7 | 0.010 | 13/35 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.673×** | -3.7 | 0.011 | 8/34 (Panc 03.27, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.817×** | -3.6 | 0.014 | 16/35 (SHP-77, AsPC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.820×** | -3.5 | 0.016 | 13/35 (Panc 03.27, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.695×** | -3.4 | 0.026 | 7/34 (Panc 03.27, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.829×** | -3.3 | 0.029 | 15/35 (SHP-77, AsPC-1, …) | all doses, flat |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.877× | -3.3 | 0.031 | 5/35 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.833× | -3.2 | 0.034 | 11/35 (SHP-77, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10722. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 240 | 0 | 32 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -20.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 332 | 1 | 11 (9 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.193× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 31.3 | 8 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +11.4) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 3.42× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 107 | 0 | 8 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -13.2) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 220 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.424× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 107 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +12.7) | [[Selinexor (drug)]] 5 µM 0.416× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 34.5 | 5 (2 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.76× (z +12.7) | — |
| [[J82 (line)]] | alt | 79.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +17.3) | — |
| [[LoVo (line)]] | wt | 66.9 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.224× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[LS 180 (line)]] | wt | 154 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 52.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +17.0) | [[Docetaxel (drug)]] 0.05 µM 0.501× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 45.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 159 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -11.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 35.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -15.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 18.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +16.4) | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.50× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 51.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.08× (z +11.0) | — |
| [[A549 (line)]] | wt | 62.8 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 3.22× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 54.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 81.3 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +8.6) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[NCI-H2030 (line)]] | alt | 39.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.34× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 41.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +11.8) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[SNU-1 (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.259× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +14.5) | — |
| [[AN3 CA (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10722), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP1B]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[PLCE1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SLCO2B1]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 | same gene group; pathway: Organic anion transport by SLCO transporters; STRING 499 |
| [[DENND2B]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[EGFEM1P]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CCL2]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ARHGAP42]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SLC37A1]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[RASGRP3]] | +0.55 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[KCND3]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[DOC2B]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.54 | +0.61 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR37]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[BCL7C]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CRLS1]] | -0.49 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[OGG1]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ACOX3]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[RINT1]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SWI5]] | -0.46 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[DPY19L3]] | -0.46 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ING5]] | -0.46 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[OSTC]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGBD5]] | B | PGBD5 activity raises SLCO3A1's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without PGBD5 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[NR3C1]] | B | NR3C1 activity lowers SLCO3A1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[ARHGAP42]] | B | ARHGAP42 activity raises SLCO3A1's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.67× lower at baseline in the lines without ARHGAP42 | 0.056 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[COL22A1]] | B | COL22A1 activity raises SLCO3A1's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without COL22A1 | 0.083 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[TRIML2]] | B | TRIML2 activity lowers SLCO3A1's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 1.64× higher at baseline in the lines without TRIML2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SLCO3A1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMD]] | B | SLCO3A1 activity lowers DMD's level | lines that do not express SLCO3A1 (13) vs lines expressing it (37) | 1.16× higher at baseline in the lines without SLCO3A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: BEX2, PRKAA2, NHS |
| [[PGBD5]] | B | SLCO3A1 activity raises PGBD5's level | lines that do not express SLCO3A1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without SLCO3A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEX2, PRKAA2, NHS |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 39.1); signed map (47.5, 16.6). **Vector** length 118, 31.4% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.9 | +8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +5.8 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +3.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.6 | -5.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.0 | -3.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 3A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:91,853,708-92,172,435 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OATP-D, OATP3A1; previously SLC21A11 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Reactome | 4 pathways, smallest: Organic anion transport by SLCO transporters; SLC-mediated transport of organic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIG8](https://www.uniprot.org/uniprotkb/Q9UIG8) (Solute carrier organic anion transporter family member 3A1):

> Putative organic anion antiporter with apparent broad substrate specificity. Recognizes various substrates including thyroid hormone L-thyroxine, prostanoids such as prostaglandin E1 and E2, bile acids such as taurocholate, glycolate and glycochenodeoxycholate and peptide hormones such as L-arginine vasopressin, likely operating in a tissue-specific manner. The transport mechanism, its electrogenicity and potential tissue-specific counterions remain to be elucidated (Probable). Mediates …

**Summary**, from NCBI Gene [28232](https://www.ncbi.nlm.nih.gov/gene/28232):

> Enables prostaglandin transmembrane transporter activity. Involved in carboxylic acid transport and positive regulation of intracellular signal transduction. Located in apical plasma membrane and basolateral plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10952) · Entrez [28232](https://www.ncbi.nlm.nih.gov/gene/28232) · UniProt [Q9UIG8](https://www.uniprot.org/uniprotkb/Q9UIG8) · Ensembl [ENSG00000176463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176463)

## Data

Gene col 10722: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10722); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10722, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10722]; `tensor/DDL_lfc|DDL_z.npy` [10722]; `embed/gene_vectors.npy` [10722]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10722 or target_col == 10722). Every well: [[SLCO3A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO3A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
