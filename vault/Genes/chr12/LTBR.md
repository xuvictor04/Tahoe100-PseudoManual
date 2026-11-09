---
symbol: "LTBR"
type: "gene"
col: 3218
ensembl_id: "ENSG00000111321"
name: "lymphotoxin beta receptor"
location: "12p13.31"
module: 98
arm: "+"
pooled_cpm: 30.26
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 15
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# LTBR

*lymphotoxin beta receptor* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.23× (z +7.7, q 4e-12, up in 34 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.252× (z -25.4, q 0e+00, down in 39 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARP1]] (+0.61, fdr 1e-05), [[VSTM2L]] (+0.60, fdr 1e-05), [[LARP4]] (+0.59, fdr 2e-05); moves opposite to [[SLC41A2]] (-0.59, fdr 7e-06), [[FNBP1]] (-0.58, fdr 1e-05), [[C15orf48]] (-0.56, fdr 2e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 15 go from it, the strongest it → [[WDR12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +7.7 | 4e-12 | 34/40 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +7.7 | 4e-12 | 31/38 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.7 | 4e-09 | 23/36 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 2e-07 | 22/39 (A498, AsPC-1, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +6.0 | 3e-07 | 24/39 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.41×** | +5.9 | 4e-07 | 19/39 (Hs 766T, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.37×** | +5.8 | 5e-07 | 20/39 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +5.0 | 3e-05 | 18/39 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 3e-05 | 18/39 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.9 | 5e-05 | 15/32 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 3e-04 | 19/39 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +4.3 | 9e-04 | 18/38 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.25×** | +3.8 | 0.007 | 13/34 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.011 | 17/39 (A498, Hs 766T, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.6 | 0.013 | 18/38 (LS 180, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.013 | 17/39 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.014 | 14/39 (A498, Hs 766T, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.018 | 17/39 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.3 | 0.027 | 15/39 (Hs 766T, Panc 03.27, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | 1.19× | +3.3 | 0.027 | 17/39 (A498, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.252×** | -25.4 | 0e+00 | 39/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.273×** | -23.9 | 0e+00 | 39/39 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.304×** | -21.9 | 0e+00 | 38/39 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.495×** | -18.3 | 0e+00 | 36/39 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -8.8 | 2e-16 | 28/40 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.589×** | -8.7 | 4e-16 | 28/39 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -8.2 | 3e-14 | 24/38 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.529×** | -6.1 | 6e-08 | 25/40 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -6.0 | 1e-07 | 24/38 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.768×** | -4.7 | 2e-04 | 19/39 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.794×** | -4.2 | 0.001 | 14/39 (NCI-H2347, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.799×** | -4.1 | 0.002 | 14/39 (LoVo, SW480, …) | inconsistent across doses | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.847× | -3.9 | 0.004 | 15/40 (LoVo, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.805×** | -3.8 | 0.005 | 17/39 (SW48, A-427, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.863× | -3.8 | 0.005 | 9/39 (HS-578T, A549, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.675×** | -3.8 | 0.006 | 9/39 (A498, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.865× | -3.7 | 0.007 | 14/40 (LoVo, BT-474, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Gallic acid (drug)]] 5 µM |  | 0.872× | -3.5 | 0.014 | 7/40 (LoVo, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 64.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0937× (z -21.9) |
| [[MIA PaCa-2 (line)]] | alt | 62.2 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -18.4) |
| [[SNU-1 (line)]] | wt | 45.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0791× (z -15.8) |
| [[A498 (line)]] | wt | 56.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -21.2) |
| [[NCI-H460 (line)]] | wt | 23.7 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -16.6) |
| [[A-427 (line)]] | wt | 28.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -11.5) |
| [[C32 (line)]] | wt | 35.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -11.0) |
| [[HOP62 (line)]] | alt | 23.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -11.3) |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -10.8) |
| [[HT-29 (line)]] | alt | 53.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -12.4) |
| [[KATO III (line)]] | alt | 39.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -19.6) |
| [[RKO (line)]] | wt | 32.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.146× (z -13.3) |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.236× (z -11.7) |
| [[SW48 (line)]] | wt | 60.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0791× (z -16.8) |
| [[SW480 (line)]] | alt | 29.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -20.8) |
| [[A549 (line)]] | wt | 33.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 29.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.170× (z -13.9) |
| [[LS 180 (line)]] | wt | 37.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -16.7) |
| [[SW 900 (line)]] | alt | 34.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.3) |
| [[SW1417 (line)]] | alt | 42.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -12.3) |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 64.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -8.7) |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -8.7) |
| [[Hs 766T (line)]] | wt | 39.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -8.9) |
| [[A-172 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP1]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LARP4]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TNFRSF1A]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 841; ⚠ same locus (32.9 kb: neighbours can correlate without regulation) |
| [[ADGRG2]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[MAOA]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[CCND3]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[BYSL]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D14]] | +0.54 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[BATF]] | +0.53 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[PANX1]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FRMD3]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC41A2]] | -0.59 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[FNBP1]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[C15orf48]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[FAM107B]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MRPS6]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[IGFBP3]] | -0.54 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[DPF3]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ADAMTS16]] | -0.51 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[DUSP10]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[BTG1]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MPC2]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PTHLH]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises LTBR's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[BATF]] | B | BATF activity weakens LTBR's drug response | lines that do not express BATF (26) vs lines expressing it (14) | the lines without BATF respond 1.12× as strongly (z diff -0.64); strongest at Belinostat 5 µM: 0.28x vs 0.38x (z diff -2.1) | 0.063 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2; target measured in part of the lines; artifact flags |
| [[IGFBP3]] | B | IGFBP3 activity raises LTBR's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.19× lower at baseline in the lines without IGFBP3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[MLKL]] | B | MLKL activity raises LTBR's level | lines that do not express MLKL (7) vs lines expressing it (43) | 2.18× lower at baseline in the lines without MLKL | 0.073 | ⚠ within organs, on part of the lines; also absent: PSD4; maybe low, not absent |
| [[SH3TC1]] | B | SH3TC1 activity raises LTBR's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 1.97× lower at baseline in the lines without SH3TC1 | 0.094 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[TOP2A]] | B | TOP2A activity raises LTBR's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR12]] | B | LTBR activity lowers WDR12's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.54× higher at baseline in the lines without LTBR | 0.029 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[DHX33]] | B | LTBR activity lowers DHX33's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.62× higher at baseline in the lines without LTBR | 0.039 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[MLKL]] | B | LTBR activity raises MLKL's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.65× lower at baseline in the lines without LTBR | 0.054 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[BTG1]] | B | LTBR activity raises BTG1's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without LTBR | 0.057 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[BYSL]] | B | LTBR activity lowers BYSL's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.36× higher at baseline in the lines without LTBR | 0.060 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[DDX54]] | B | LTBR activity lowers DDX54's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.14× higher at baseline in the lines without LTBR | 0.063 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[ZBTB24]] | B | LTBR activity lowers ZBTB24's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.27× higher at baseline in the lines without LTBR | 0.071 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[TBRG4]] | B | LTBR activity lowers TBRG4's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.38× higher at baseline in the lines without LTBR | 0.072 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[FAM107B]] | B | LTBR activity raises FAM107B's level | lines that do not express LTBR (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without LTBR | 0.073 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[TFAP4]] | B | LTBR activity lowers TFAP4's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.33× higher at baseline in the lines without LTBR | 0.074 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[IGFBP3]] | B | LTBR activity raises IGFBP3's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without LTBR | 0.075 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| cells under [[MK-3903 (drug)]] 0.05 µM | B | LTBR activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express LTBR (8) vs lines expressing it (40) | the lines without LTBR: 0.90× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.7, 18.6); signed map (20.8, 32.2). **Vector** length 100, 25.6% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +4.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.3 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +7.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.7 | +6.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.3 | +6.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.1 | +5.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -18.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -1.6 | -4.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[9-ING-41 (drug)]] 0.05 µM |  | -1.5 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | lymphotoxin beta receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,375,045-6,391,571 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TNFCR, TNFR-RP, TNFR2-RP, TNF-R-III, TNFRSF3; previously D12S370 |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 3 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P36941](https://www.uniprot.org/uniprotkb/P36941) (Tumor necrosis factor receptor superfamily member 3):

> Receptor for the heterotrimeric lymphotoxin containing LTA and LTB, and for TNFS14/LIGHT. Activates NF-kappa-B signaling pathway upon stimulation with lymphotoxin (LTA(1)-LTB(2)). Promotes apoptosis via TRAF3 and TRAF5. May play a role in the development of lymphoid organs.

**Summary**, from NCBI Gene [4055](https://www.ncbi.nlm.nih.gov/gene/4055):

> This gene encodes a member of the tumor necrosis factor receptor superfamily. The major ligands of this receptor include lymphotoxin alpha/beta and tumor necrosis factor ligand superfamily member 14. The encoded protein plays a role in signalling during the development of lymphoid and other organs, lipid metabolism, immune response, and programmed cell death. Activity of this receptor has also been linked to carcinogenesis. Alternatively spliced transcript variants encoding multiple isoforms …

**Accessions** — [HGNC:6718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6718) · Entrez [4055](https://www.ncbi.nlm.nih.gov/gene/4055) · UniProt [P36941](https://www.uniprot.org/uniprotkb/P36941) · Ensembl [ENSG00000111321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111321)

## Data

Gene col 3218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3218); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3218]; `tensor/DDL_lfc|DDL_z.npy` [3218]; `embed/gene_vectors.npy` [3218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3218 or target_col == 3218). Every well: [[LTBR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTBR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
