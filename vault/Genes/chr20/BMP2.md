---
symbol: "BMP2"
type: "gene"
col: 4676
ensembl_id: "ENSG00000125845"
name: "bone morphogenetic protein 2"
location: "20p12.3"
module: 228
arm: "+"
pooled_cpm: 15.05
n_lines_expressing: 30
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 15
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 18
direction_downstream: 42
tags: ["gene", "module/228"]
generated_by: "tahoemap"
---

# BMP2

*bone morphogenetic protein 2* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.52× (z +23.0, q 0e+00, up in 24 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.527× (z -8.2, q 1e-13, down in 19 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH17]] (+0.63, fdr 1e-05), [[PTHLH]] (+0.61, fdr 7e-06), [[DUSP10]] (+0.61, fdr 7e-06); moves opposite to [[ABCB10]] (-0.60, fdr 1e-05), [[WDR5]] (-0.57, fdr 1e-05), [[WHAMMP1]] (-0.53, fdr 4e-05).
> It is in [[Module 228]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[ARHGAP42]] → it (grade B ⚠); 42 go from it, the strongest it → [[DUSP10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.52×** | +23.0 | 0e+00 | 24/27 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.72×** | +12.4 | 4e-33 | 22/27 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +11.0 | 5e-26 | 12/26 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +10.9 | 1e-25 | 14/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +7.5 | 7e-12 | 10/26 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +6.1 | 1e-07 | 14/27 (Hs 766T, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 7e-06 | 6/26 (Panc 03.27, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.45×** | +4.6 | 3e-04 | 15/25 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.001 | 9/26 (A549, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.010 | 6/25 (KATO III, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.010 | 6/27 (NCI-H1573, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.011 | 8/25 (KATO III, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.31×** | +3.5 | 0.023 | 12/27 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.032 | 16/26 (SW 900, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.049 | 2/26 (AsPC-1, NCI-H460) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.088 | 12/27 (A498, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.527×** | -8.2 | 1e-13 | 19/27 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.552×** | -7.6 | 6e-12 | 15/25 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.572×** | -7.2 | 1e-10 | 19/28 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.597×** | -6.6 | 5e-09 | 15/26 (NCI-H2347, HS-578T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.602×** | -6.5 | 8e-09 | 18/27 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.611×** | -6.3 | 2e-08 | 15/28 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.648×** | -5.6 | 2e-06 | 10/26 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.675×** | -5.0 | 3e-05 | 11/26 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.677×** | -5.0 | 4e-05 | 16/29 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.691×** | -4.8 | 1e-04 | 13/28 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.701×** | -4.6 | 3e-04 | 15/26 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.694×** | -4.4 | 5e-04 | 8/26 (SW 900, A549, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.798×** | -4.1 | 0.002 | 12/27 (HS-578T, NCI-H2347, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.739×** | -3.9 | 0.004 | 14/23 (LoVo, HT-29, …) | two highest doses | composition shift |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.748×** | -3.7 | 0.007 | 10/26 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.033 | 13/28 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.835× | -3.3 | 0.033 | 11/27 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.619×** | -3.2 | 0.035 | 5/26 (NCI-H1792, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.0 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +18.2) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.213× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 66.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 76.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -11.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.5) |
| [[HS-578T (line)]] | alt | 27.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 13.7× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 42.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 5.77 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +13.7) | [[Clobetasol propionate (drug)]] 0.5 µM 0.0442× (z -10.5) |
| [[SNU-423 (line)]] | alt | 20.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +10.8) | [[Sunitinib (drug)]] 5 µM 0.137× (z -9.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 27.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.7× (z +15.6) | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0998× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 2 (1 ⚠) | — | [[Budesonide (drug)]] 0.05 µM 0.265× (z -8.7) |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.9) |
| [[SW 900 (line)]] | alt | 42.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0204× (z -13.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 5.81 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 44.2× (z +10.4) | — |
| [[SW 1088 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +8.6) | — |
| [[A-172 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH17]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PTHLH]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 | STRING 697 |
| [[DUSP10]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[C15orf48]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[INHBA]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[LINC01828]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[IL1A]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS; STRING 465 |
| [[DLX2]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 | STRING 597 |
| [[PGBD5]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RAP2B]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[SOX4]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[KIAA1217]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[WDR5]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[WHAMMP1]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[DFFB]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[IPO11]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ALG6]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PRMT7]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ENOPH1]] | -0.51 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ZDHHC7]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PPIH]] | -0.50 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[SMPD4]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SRPX]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 11, C 7. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP42]] | B | ARHGAP42 activity raises BMP2's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without ARHGAP42 | 0.036 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[FAM107B]] | B | FAM107B activity raises BMP2's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without FAM107B | 0.036 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[DUSP10]] | B | DUSP10 activity raises BMP2's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without DUSP10 | 0.037 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises BMP2's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 3.21× lower at baseline in the lines without IKZF2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers BMP2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[RDH10]] | B | RDH10 activity raises BMP2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 2.67× lower at baseline in the lines without RDH10 | 0.046 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[KCNK1]] | B | KCNK1 activity raises BMP2's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.22× lower at baseline in the lines without KCNK1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[GATA6]] | B | GATA6 activity raises BMP2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.44× lower at baseline in the lines without GATA6 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[BDKRB2]] | B | BDKRB2 activity raises BMP2's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.37× lower at baseline in the lines without BDKRB2 | 0.058 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[ITGA1]] | B | ITGA1 activity raises BMP2's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without ITGA1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[FRMD4B]] | B | FRMD4B activity raises BMP2's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.37× lower at baseline in the lines without FRMD4B | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[ADGRF4]] | C | ADGRF4 activity raises BMP2's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 3.76× lower at baseline in the lines without ADGRF4 | 0.004 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 33, C 9. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP10]] | B | BMP2 activity raises DUSP10's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without BMP2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[RND3]] | B | BMP2 activity raises RND3's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.64× lower at baseline in the lines without BMP2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[GATA6]] | B | BMP2 activity raises GATA6's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without BMP2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[BCL7C]] | B | BMP2 activity lowers BCL7C's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.31× higher at baseline in the lines without BMP2 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[HMGN2P46]] | B | BMP2 activity raises HMGN2P46's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.63× lower at baseline in the lines without BMP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[PRMT7]] | B | BMP2 activity lowers PRMT7's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.34× higher at baseline in the lines without BMP2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[KCNK1]] | B | BMP2 activity raises KCNK1's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 3.04× lower at baseline in the lines without BMP2 | 0.019 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[IKZF2]] | B | BMP2 activity raises IKZF2's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without BMP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[FAM107B]] | B | BMP2 activity raises FAM107B's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without BMP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[MAST4]] | B | BMP2 activity raises MAST4's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without BMP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[WDR5]] | B | BMP2 activity lowers WDR5's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.33× higher at baseline in the lines without BMP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[ATP1B1]] | B | BMP2 activity raises ATP1B1's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.37× lower at baseline in the lines without BMP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |

## Where it sits

- **Module**: [[Module 228]]; 8 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, 3.0); signed map (44.5, 13.0). **Vector** length 86.8, 22.2% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +23.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +11.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -8.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:6,767,686-6,780,246 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BMP2A |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Hallmark sets | TGF_BETA_SIGNALING, APOPTOSIS, UV_RESPONSE_UP, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 7 pathways, smallest: Signaling by BMP; Molecules associated with elastic fibres; Elastic fibre formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P12643](https://www.uniprot.org/uniprotkb/P12643) (Bone morphogenetic protein 2):

> Growth factor of the TGF-beta superfamily that plays essential roles in many developmental processes, including cardiogenesis, neurogenesis, and osteogenesis. Induces cartilage and bone formation. Initiates the canonical BMP signaling cascade by associating with type I receptor BMPR1A and type II receptor BMPR2. Once all three components are bound together in a complex at the cell surface, BMPR2 phosphorylates and activates BMPR1A. In turn, BMPR1A propagates signal by phosphorylating SMAD1/5/8 …

**Summary**, from NCBI Gene [650](https://www.ncbi.nlm.nih.gov/gene/650):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer, which plays a role in bone and cartilage development. Duplication of a regulatory region downstream of this gene …

**Accessions** — [HGNC:1069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1069) · Entrez [650](https://www.ncbi.nlm.nih.gov/gene/650) · UniProt [P12643](https://www.uniprot.org/uniprotkb/P12643) · Ensembl [ENSG00000125845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125845)

## Data

Gene col 4676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4676); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4676]; `tensor/DDL_lfc|DDL_z.npy` [4676]; `embed/gene_vectors.npy` [4676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4676 or target_col == 4676). Every well: [[BMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
