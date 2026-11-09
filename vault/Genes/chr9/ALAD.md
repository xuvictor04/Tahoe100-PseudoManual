---
symbol: "ALAD"
type: "gene"
col: 7252
ensembl_id: "ENSG00000148218"
name: "aminolevulinate dehydratase"
location: "9q32"
module: 45
arm: "+"
pooled_cpm: 12.54
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 21
n_dd_up_clean: 23
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ALAD

*aminolevulinate dehydratase* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.01× (z +27.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.507× (z -11.4, q 1e-27, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHMT2]] (+0.78, fdr 7e-06), [[CAT]] (+0.74, fdr 7e-06), [[THYN1]] (+0.73, fdr 1e-05); moves opposite to [[AVEN]] (-0.70, fdr 1e-05), [[SIAH2-AS1]] (-0.70, fdr 1e-04), [[DPH5-DT]] (-0.69, fdr 1e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RASSF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.01×** | +27.2 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.27×** | +24.5 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.75×** | +22.3 | 0e+00 | 46/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +12.7 | 7e-35 | 39/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.76×** | +9.5 | 2e-19 | 21/36 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.74×** | +8.9 | 6e-17 | 35/48 (A498, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +7.8 | 6e-13 | 26/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.57×** | +7.4 | 1e-11 | 13/24 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +6.7 | 9e-10 | 21/41 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.7 | 9e-10 | 21/48 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.6 | 2e-09 | 20/48 (A-172, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 7e-08 | 20/46 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 2e-06 | 16/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.8 | 6e-05 | 16/48 (hTERT-HPNE, C32, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +4.7 | 8e-05 | 11/47 (KATO III, SW480, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.007 | 8/46 (NCI-H23, A498, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.007 | 3/44 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.009 | 12/47 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -11.4 | 1e-27 | 37/47 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.520×** | -11.0 | 1e-25 | 33/47 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.840× | -10.0 | 2e-21 | 23/48 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -9.4 | 6e-19 | 34/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -9.2 | 4e-18 | 29/46 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.646×** | -7.3 | 2e-11 | 26/47 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -7.3 | 3e-11 | 26/45 (SW1417, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -7.0 | 2e-10 | 26/47 (KATO III, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.725×** | -5.4 | 4e-06 | 18/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.802×** | -5.2 | 9e-06 | 17/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -5.1 | 2e-05 | 13/44 (Hs 766T, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.745×** | -4.9 | 5e-05 | 18/45 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.604×** | -4.4 | 4e-04 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.769×** | -4.4 | 4e-04 | 17/47 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.778×** | -4.2 | 9e-04 | 12/48 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.002 | 17/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.798×** | -3.8 | 0.005 | 14/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.811×** | -3.5 | 0.013 | 14/47 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.028 | 11/47 (HT-29, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 7.36× (z +10.8) | [[Homoharringtonine (drug)]] 0.05 µM 0.175× (z -9.4) |
| [[SW480 (line)]] | alt | 11.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.81× (z +17.4) | — |
| [[COLO 205 (line)]] | alt | 31.1 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.18× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -13.4) |
| [[LoVo (line)]] | wt | 11.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.88× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H460 (line)]] | wt | 10.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 18.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.01× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 8.11 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +12.7) | — |
| [[J82 (line)]] | alt | 12.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.26× (z +11.7) | — |
| [[KATO III (line)]] | alt | 17.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.91× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 5.12× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.185× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 10.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.30× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 6.35 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 21.2 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.81× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -15.9) |
| [[A-172 (line)]] | wt | 10.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.24× (z +9.0) | — |
| [[A549 (line)]] | wt | 8.47 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 6.96× (z +9.5) | [[Harringtonine (drug)]] 0.05 µM 0.0514× (z -13.4) |
| [[C32 (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -8.7) |
| [[HS-578T (line)]] | alt | 11.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 24.0 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.47× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 7.26 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.78× (z +8.8) | — |
| [[RKO (line)]] | wt | 10.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.75× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 13.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.71× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -11.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 14.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.84× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 20.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.46× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0817× (z -8.7) |
| [[A-427 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHMT2]] | +0.78 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[CAT]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[THYN1]] | +0.73 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MPP1]] | +0.71 | +0.50 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[ORC4]] | +0.71 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[RAB3A]] | +0.71 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TMEM14A]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[IFT172]] | +0.69 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[THRA]] | +0.68 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SUFU]] | +0.68 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[ARRB2]] | +0.68 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[METTL17]] | +0.67 | +0.42 / +0.68 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.70 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[SIAH2-AS1]] | -0.70 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[DPH5-DT]] | -0.69 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[EPM2A]] | -0.69 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.68 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LINC01829]] | -0.68 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[SPON1-AS1]] | -0.68 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[HCG18]] | -0.67 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[POU6F1]] | -0.67 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[MYH3]] | -0.67 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CDR2]] | -0.67 | -0.64 / -0.57 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[E2F3]] | -0.67 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF4]] | B | RASSF4 activity strengthens ALAD's drug response | lines that do not express RASSF4 (11) vs lines expressing it (37) | the lines without RASSF4 respond 0.85× as strongly (z diff +0.74); strongest at Panobinostat 0.5 µM: 3.20x vs 4.59x (z diff +1.8) | 0.054 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CYB5A]] | B | CYB5A activity raises ALAD's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CYB5A | 0.058 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[OSBPL7]] | B | OSBPL7 activity strengthens ALAD's drug response | lines that do not express OSBPL7 (7) vs lines expressing it (41) | the lines without OSBPL7 respond 0.79× as strongly (z diff +0.64); rises at some drug-doses, falls at others (67% from rises): Adagrasib 0.05 µM: 0.92x vs 0.81x (z diff +2.5); Panobinostat 0.5 µM: 3.21x vs 4.42x (z diff +1.8); Panobinostat 5 µM: 4.04x vs 5.22x (z diff +1.5) | 0.063 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ABL1]] | B | ABL1 activity lowers ALAD's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 6.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.7, -8.2); signed map (-28.6, -7.7). **Vector** length 85.2, 18.0% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +24.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +22.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +27.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[NG25 (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +8.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +7.8 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.1 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.3 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | aminolevulinate dehydratase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,386,312-113,401,290 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ALADH, PBGS |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Hallmark sets | FATTY_ACID_METABOLISM, HEME_METABOLISM |
| Reactome | 6 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P13716](https://www.uniprot.org/uniprotkb/P13716) (Delta-aminolevulinic acid dehydratase):

> Catalyzes an early step in the biosynthesis of tetrapyrroles. Binds two molecules of 5-aminolevulinate per subunit, each at a distinct site, and catalyzes their condensation to form porphobilinogen.

**Summary**, from NCBI Gene [210](https://www.ncbi.nlm.nih.gov/gene/210):

> The ALAD enzyme is composed of 8 identical subunits and catalyzes the condensation of 2 molecules of delta-aminolevulinate to form porphobilinogen (a precursor of heme, cytochromes and other hemoproteins). ALAD catalyzes the second step in the porphyrin and heme biosynthetic pathway; zinc is essential for enzymatic activity. ALAD enzymatic activity is inhibited by lead and a defect in the ALAD structural gene can cause increased sensitivity to lead poisoning and acute hepatic porphyria. …

**Accessions** — [HGNC:395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:395) · Entrez [210](https://www.ncbi.nlm.nih.gov/gene/210) · UniProt [P13716](https://www.uniprot.org/uniprotkb/P13716) · Ensembl [ENSG00000148218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148218)

## Data

Gene col 7252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7252); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7252]; `tensor/DDL_lfc|DDL_z.npy` [7252]; `embed/gene_vectors.npy` [7252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7252 or target_col == 7252). Every well: [[ALAD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALAD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
