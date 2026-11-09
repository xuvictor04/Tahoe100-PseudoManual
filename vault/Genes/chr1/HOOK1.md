---
symbol: "HOOK1"
type: "gene"
col: 5592
ensembl_id: "ENSG00000134709"
name: "hook microtubule tethering protein 1"
location: "1p32.1"
module: 118
arm: "-"
pooled_cpm: 34.51
n_lines_expressing: 28
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 12
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# HOOK1

*hook microtubule tethering protein 1* — 1p32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +17.3, q 0e+00, up in 20 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.47× (z +8.0, q 1e-13, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.752× (z -5.7, q 9e-06, down in 17 of 24 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.677× (z -4.2, q 0.005, down in 14 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW48 0.300×, SHP-77 0.521×, SW480 0.586×, NCI-H1573 0.614×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.420×, KATO III 0.449×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.135×; ⚠ cell-cycle shift, explains ~32% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSX2IP]] (+0.62, fdr 1e-05), [[LRRCC1]] (+0.55, fdr 9e-05), [[POTEF]] (+0.55, fdr 4e-05); moves opposite to [[HMGA1P4]] (-0.53, fdr 7e-05), [[BANP]] (-0.52, fdr 5e-05), [[WBP1L]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXADR]] → it (grade B ⚠); 12 go from it, the strongest it → [[ATXN7L3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +17.3 | 0e+00 | 20/24 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +13.5 | 7e-39 | 15/21 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +11.0 | 8e-26 | 14/26 (SW1417, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +9.2 | 4e-18 | 13/22 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +8.4 | 5e-15 | 15/26 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +8.0 | 1e-13 | 15/26 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.9 | 3e-13 | 12/26 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +7.8 | 3e-13 | 17/26 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +7.0 | 2e-10 | 16/26 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.9 | 4e-10 | 17/25 (SHP-77, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.7 | 1e-09 | 18/25 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +6.4 | 7e-09 | 15/26 (SW480, SHP-77, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +5.4 | 2e-06 | 14/26 (SW480, COLO 205, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +5.2 | 9e-06 | 18/26 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 1e-04 | 12/26 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.040 | 12/26 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5592.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW48 0.300×, SHP-77 0.521×, SW480 0.586×, NCI-H1573 0.614×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.420×, KATO III 0.449×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.135×; ⚠ cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -5.7 | 9e-06 | 17/24 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -4.6 | 1e-03 | 18/25 (SW48, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.677×** | -4.2 | 0.005 | 14/27 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.020 | 2/26 (NCI-H2030, LoVo) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.834× | -3.8 | 0.020 | 5/25 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.836× | -3.7 | 0.021 | 6/26 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.886× | -3.5 | 0.032 | 12/26 (SW1417, COLO 205, …) | top dose only | low cells (technical?) |
| [[Drospirenone (drug)]] 0.5 µM |  | 0.861× | -3.1 | 0.12 | 2/25 (J82, Panc 03.27) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.862× | -3.1 | 0.12 | 8/25 (J82, RKO, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.864× | -3.0 | 0.12 | 4/26 (HCT15, LoVo, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.756× | -3.0 | 0.12 | 5/26 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.758× | -3.0 | 0.12 | 7/25 (SW480, A-427, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 63.2 | 6 (6 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.52× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 95.0 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 82.3 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.22× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 13.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.98× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 98.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 82.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.449× (z -8.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 13.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.41× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 81.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -8.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.89× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 80.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[LRRCC1]] | +0.55 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[POTEF]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[HLTF]] | +0.54 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[MIA3]] | +0.51 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[AMOT]] | +0.48 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[HMGN3]] | +0.48 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[DNAJC10]] | +0.48 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[CDC73]] | +0.48 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[MNS1]] | +0.47 | +0.29 / +0.40 | both halves | 3e-04 |  |
| [[MPP7]] | +0.47 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[ISOC1]] | +0.47 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA1P4]] | -0.53 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[BANP]] | -0.52 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[WBP1L]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[NGDN]] | -0.52 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[GSK3B-DT]] | -0.52 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[CLP1]] | -0.50 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[MEF2B]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PRR14L]] | -0.50 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PPP2CB]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PRCC]] | -0.49 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[FRS2]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[IREB2]] | -0.49 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | B | CXADR activity raises HOOK1's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.44× lower at baseline in the lines without CXADR | 0.033 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[MPP7]] | C | MPP7 activity raises HOOK1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 5.82× lower at baseline in the lines without MPP7 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN7L3-AS1]] | B | HOOK1 activity raises ATXN7L3-AS1's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without HOOK1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[PLS1]] | B | HOOK1 activity raises PLS1's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 3.25× lower at baseline in the lines without HOOK1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[CXADR]] | B | HOOK1 activity raises CXADR's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 3.75× lower at baseline in the lines without HOOK1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[GXYLT2]] | B | HOOK1 activity lowers GXYLT2's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 2.18× higher at baseline in the lines without HOOK1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[SLC20A2]] | B | HOOK1 activity raises SLC20A2's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without HOOK1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[SEC63]] | B | HOOK1 activity lowers SEC63's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.27× higher at baseline in the lines without HOOK1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| cells under [[9-ING-41 (drug)]] 5 µM | B | HOOK1 activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express HOOK1 (22) vs lines expressing it (26) | the lines without HOOK1: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[NGDN]] | B | HOOK1 activity raises NGDN's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.20× lower at baseline in the lines without HOOK1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | HOOK1 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express HOOK1 (22) vs lines expressing it (26) | the lines without HOOK1: 0.88× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[NOXRED1]] | B | HOOK1 activity raises NOXRED1's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.10× lower at baseline in the lines without HOOK1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[CDCA7L]] | B | HOOK1 activity weakens CDCA7L's drug response | lines that do not express HOOK1 (16) vs lines expressing it (24) | the lines without HOOK1 respond 1.17× as strongly (z diff -0.89); strongest at Panobinostat 5 µM: 3.50x vs 1.97x (z diff -3.0) | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1; target measured in part of the lines; artifact flags |
| [[MPP7]] | C | HOOK1 activity raises MPP7's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 3.55× lower at baseline in the lines without HOOK1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **-** arm (projection on the module's main direction -0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.0, 28.0); signed map (-34.0, -35.3). **Vector** length 72.3, 19.7% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | hook microtubule tethering protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.1 — chr1:59,814,786-59,876,322 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HK1 |
| Gene groups (HGNC) | FHF complex; HOOK family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJC3](https://www.uniprot.org/uniprotkb/Q9UJC3) (Protein Hook homolog 1):

> Component of the FTS/Hook/FHIP complex (FHF complex). The FHF complex may function to promote vesicle trafficking and/or fusion via the homotypic vesicular protein sorting complex (the HOPS complex). FHF complex promotes the distribution of AP-4 complex to the perinuclear area of the cell. Required for spermatid differentiation. Probably involved in the positioning of the microtubules of the manchette and the flagellum in relation to the membrane skeleton (By similarity).

**Summary**, from NCBI Gene [51361](https://www.ncbi.nlm.nih.gov/gene/51361):

> This gene encodes a member of the hook family of coiled-coil proteins, which bind to microtubules and organelles through their N- and C-terminal domains, respectively. The encoded protein localizes to discrete punctuate subcellular structures, and interacts with several members of the Rab GTPase family involved in endocytosis. It is thought to link endocytic membrane trafficking to the microtubule cytoskeleton. Several alternatively spliced transcript variants have been identified, but the …

**Accessions** — [HGNC:19884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19884) · Entrez [51361](https://www.ncbi.nlm.nih.gov/gene/51361) · UniProt [Q9UJC3](https://www.uniprot.org/uniprotkb/Q9UJC3) · Ensembl [ENSG00000134709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134709)

## Data

Gene col 5592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5592); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5592]; `tensor/DDL_lfc|DDL_z.npy` [5592]; `embed/gene_vectors.npy` [5592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5592 or target_col == 5592). Every well: [[HOOK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOOK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
