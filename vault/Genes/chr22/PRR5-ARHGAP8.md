---
symbol: "PRR5-ARHGAP8"
type: "gene"
col: 14537
ensembl_id: "ENSG00000248405"
name: "PRR5-ARHGAP8 readthrough"
location: "22q13.31"
module: 77
arm: "+"
pooled_cpm: 3.63
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 13
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# PRR5-ARHGAP8

*PRR5-ARHGAP8 readthrough* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.35× (z +13.4, q 4e-38, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.50× (z +10.5, q 2e-23, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.413× (z -14.4, q 2e-44, down in 24 of 31 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.412× (z -10.3, q 3e-22, down in 23 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR5]] (+0.81, fdr 7e-06, ⚠ same locus), [[ARHGAP8]] (+0.68, fdr 1e-05, ⚠ same locus), [[TPST2]] (+0.66, fdr 1e-05), [[IGSF9]] (+0.63, fdr 1e-05), [[LRP8]] (+0.59, fdr 1e-05); moves opposite to [[ZNF518A]] (-0.63, fdr 1e-05), [[TRMT1L]] (-0.61, fdr 1e-05), [[TAF9]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PIK3AP1]] → it (grade B ⚠); 13 go from it, the strongest it → cells under [[Doxycycline (monohydrate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +13.4 | 4e-38 | 1/2 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.50×** | +10.5 | 2e-23 | 26/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.9 | 5e-13 | 19/32 (A498, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.5 | 7e-12 | 9/17 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +6.7 | 2e-09 | 3/8 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +6.0 | 2e-07 | 13/41 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.48×** | +5.5 | 3e-06 | 7/11 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.3 | 1e-05 | 12/40 (SW480, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 1e-05 | 16/41 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 1e-05 | 10/38 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.8 | 8e-05 | 9/41 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.8 | 8e-05 | 12/36 (NCI-H1792, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.44×** | +4.2 | 0.001 | 11/39 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.001 | 3/34 (LoVo, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.007 | 7/39 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.011 | 4/31 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.015 | 3/40 (NCI-H460, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.016 | 5/28 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.086 | 5/37 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.413×** | -14.4 | 2e-44 | 24/31 (SW48, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.412×** | -10.3 | 3e-22 | 23/42 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.426×** | -9.8 | 1e-20 | 21/30 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.527×** | -7.4 | 2e-11 | 21/40 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.523×** | -7.2 | 7e-11 | 17/36 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -5.7 | 1e-06 | 12/35 (A498, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.626×** | -5.0 | 4e-05 | 14/34 (HOP62, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.695×** | -4.2 | 0.002 | 13/39 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.713×** | -3.9 | 0.006 | 11/40 (LoVo, SHP-77, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -3.6 | 0.021 | 13/40 (NCI-H460, LoVo, …) | top dose only |  |
| [[Aliskiren (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.024 | 6/40 (HS-578T, NCI-H1792, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.748×** | -3.4 | 0.037 | 10/34 (KATO III, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -3.2 | 0.064 | 6/39 (C32, CFPAC-1, …) | top dose only |  |
| [[LJI308 (drug)]] 0.05 µM |  | **0.755×** | -3.1 | 0.087 | 5/37 (PANC-1, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.30 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0673× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0894× (z -12.0) |
| [[LS 180 (line)]] | wt | 7.68 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0671× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0776× (z -10.6) |
| [[SW48 (line)]] | wt | 16.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0931× (z -9.4) |
| [[A498 (line)]] | wt | 9.15 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.20 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0744× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 3.13 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 6.93 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0797× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 2.03 | 0 | 1 | — | [[Vemurafenib (drug)]] 0.5 µM 0.138× (z -22.8) |
| [[SW1417 (line)]] | alt | 6.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 5.12 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR5]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ARHGAP8]] | +0.68 | +0.69 / +0.52 | both halves | 1e-05 | STRING 759; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TPST2]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[IGSF9]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[LRP8]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[GAK]] | +0.59 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[NEURL1]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[FGFR4]] | +0.58 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[B4GALNT3]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[FAM222A-AS1]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RGS10]] | +0.57 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ST6GALNAC6-1]] | +0.56 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ATP7B]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | -0.63 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[TAF9]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[NFYC]] | -0.59 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ZNF429]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LATS1]] | -0.58 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CGGBP1]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[THAP1]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CLK4]] | -0.58 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[WASHC3]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TIA1]] | -0.57 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ZNF764]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3AP1]] | B | PIK3AP1 activity raises PRR5-ARHGAP8's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without PIK3AP1 | 0.025 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[AIF1L]] | B | AIF1L activity raises PRR5-ARHGAP8's level | lines that do not express AIF1L (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without AIF1L | 0.082 | ⚠ within organs, on part of the lines; also absent: FAM169A, NUP210, PRR36; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.68× the cells of the other lines | 0.040 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| [[LARP7]] | C | PRR5-ARHGAP8 activity raises LARP7's level | lines that do not express PRR5-ARHGAP8 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without PRR5-ARHGAP8 | 0.040 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |
| cells under [[EX229 (drug)]] 0.05 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.77× the cells of the other lines | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Glycyrrhizic acid (drug)]] 0.5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.73× the cells of the other lines | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.71× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.75× the cells of the other lines | 0.063 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Apalutamide (drug)]] 0.5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 1.26× the cells of the other lines | 0.065 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| [[CGREF1]] | C | [[PRR5]], PRR5-ARHGAP8 activity raises CGREF1's level | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (46) | 2.92× lower at baseline in the lines without PRR5, PRR5-ARHGAP8 | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under Procainamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.77× the cells of the other lines | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Afatinib (drug)]] 0.05 µM | C | [[PRR5]], PRR5-ARHGAP8 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 1.17× the cells of the other lines | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under Hydroxyurea 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.72× the cells of the other lines | 0.093 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| cells under [[Mozavaptan (drug)]] 0.5 µM | C | [[PRR5]], PRR5-ARHGAP8 activity raises the cells' numbers under Mozavaptan 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.75× the cells of the other lines | 0.094 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (0.3, 14.8); signed map (-20.0, 36.6). **Vector** length 59.9, 8.85% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.8 | -7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | PRR5-ARHGAP8 readthrough |
| Locus type | readthrough (other) |
| Location | 22q13.31 — chr22:44,702,233-44,862,706 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [553158](https://www.ncbi.nlm.nih.gov/gene/553158):

> The PRR5-ARHGAP8 mRNA is an infrequent but naturally occurring read-through transcript of the neighboring proline rich 5, renal (PRR5) and Rho GTPase activating protein 8 (ARHGAP8) genes. The resulting fusion protein contains sequence identity with each individual gene product, and it includes domains characteristic of a RhoGAP protein. The significance of this read-through transcript and the function of its protein product have not yet been determined. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:34512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34512) · Entrez [553158](https://www.ncbi.nlm.nih.gov/gene/553158) · Ensembl [ENSG00000248405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248405)

## Data

Gene col 14537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14537); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14537]; `tensor/DDL_lfc|DDL_z.npy` [14537]; `embed/gene_vectors.npy` [14537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14537 or target_col == 14537). Every well: [[PRR5-ARHGAP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR5-ARHGAP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
