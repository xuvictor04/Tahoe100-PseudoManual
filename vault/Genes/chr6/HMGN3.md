---
symbol: "HMGN3"
type: "gene"
col: 3988
ensembl_id: "ENSG00000118418"
name: "high mobility group nucleosomal binding domain 3"
location: "6q14.1"
module: 45
arm: "+"
pooled_cpm: 30.99
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# HMGN3

*high mobility group nucleosomal binding domain 3* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.28× (z +13.4, q 3e-38, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.432× (z -9.6, q 5e-19, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM14A]] (+0.79, fdr 7e-06), [[FAM102B]] (+0.72, fdr 7e-06), [[GUSBP18]] (+0.70, fdr 1e-05); moves opposite to [[SMIM15-AS1]] (-0.68, fdr 5e-05), [[EIF5]] (-0.68, fdr 1e-05), [[IDI2-AS1]] (-0.67, fdr 4e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CLCF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +13.4 | 3e-38 | 45/46 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.73×** | +11.5 | 3e-28 | 39/44 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +11.4 | 6e-28 | 42/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.61×** | +11.0 | 5e-26 | 44/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.47×** | +10.0 | 2e-21 | 33/37 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.34×** | +9.8 | 2e-20 | 44/46 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +9.2 | 2e-18 | 39/46 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.07×** | +8.4 | 4e-15 | 41/46 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.7 | 6e-13 | 32/42 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +5.7 | 9e-07 | 36/46 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +4.8 | 7e-05 | 32/45 (NCI-H23, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +4.7 | 1e-04 | 29/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +4.6 | 2e-04 | 27/46 (SHP-77, RPMI-7951, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 2e-04 | 32/46 (A-172, KATO III, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.09×** | +3.8 | 0.006 | 22/44 (KATO III, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +3.5 | 0.016 | 16/46 (HT-29, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.050 | 17/46 (HS-578T, PANC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.092 | 16/46 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +2.9 | 0.097 | 14/46 (NCI-H23, C32, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3988.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.432×** | -9.6 | 5e-19 | 38/45 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.654×** | -6.8 | 3e-09 | 29/46 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.586×** | -5.7 | 2e-06 | 30/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.626×** | -5.3 | 1e-05 | 30/46 (C32, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.4 | 0.001 | 22/46 (HCT15, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.690×** | -4.2 | 0.002 | 25/45 (KATO III, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -3.8 | 0.010 | 21/45 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.724×** | -3.7 | 0.017 | 23/46 (HepG2/C3A, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -3.6 | 0.020 | 23/46 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -3.3 | 0.053 | 21/46 (SHP-77, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.536×** | -3.2 | 0.076 | 15/46 (SHP-77, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.758×** | -3.1 | 0.081 | 19/46 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.748×** | -3.1 | 0.082 | 16/46 (SHP-77, LOX-IMVI, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.549×** | -3.1 | 0.087 | 16/46 (A-427, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.764×** | -3.0 | 0.087 | 19/45 (KATO III, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 37.2 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +10.7) | — |
| [[LoVo (line)]] | wt | 12.5 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.36× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 19.6 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.19× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 20.9 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.08× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 27.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 70.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 59.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.97× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.5) |
| [[LS 180 (line)]] | wt | 46.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.46× (z +10.8) | [[Bortezomib (drug)]] 0.05 µM 0.195× (z -9.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 20.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.48× (z +9.6) | — |
| [[A-427 (line)]] | wt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.0) |
| [[A498 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 39.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 27.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.69× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 26.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.71× (z +9.8) | — |
| [[RKO (line)]] | wt | 24.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.71× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.3) |
| [[SNU-1 (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -10.1) |
| [[SW480 (line)]] | alt | 54.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM14A]] | +0.79 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[FAM102B]] | +0.72 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[GUSBP18]] | +0.70 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CAT]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CXADR]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[CYB5A]] | +0.67 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[ATP8A1]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PLEKHH3]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[NDUFB6]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[HDAC1]] | +0.64 | +0.56 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | -0.68 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[EIF5]] | -0.68 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | -0.67 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[ZNF621]] | -0.66 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[PLAC8L1]] | -0.66 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.65 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[C6orf62]] | -0.64 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[C8orf33]] | -0.63 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[EMG1]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.63 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[GARIN1A]] | -0.62 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CSRNP2]] | -0.62 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCF1]] | B | CLCF1 activity lowers HMGN3's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.77× higher at baseline in the lines without CLCF1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[TRIM6]] | B | TRIM6 activity lowers HMGN3's level | lines that do not express TRIM6 (17) vs lines expressing it (33) | 1.63× higher at baseline in the lines without TRIM6 | 0.019 | ⚠ within organs, on part of the lines; also absent: TFPI2, KMO, ENSG00000289526 |
| [[SEMA6B]] | B | SEMA6B activity raises HMGN3's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without SEMA6B | 0.022 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[LINC00173]] | B | LINC00173 activity raises HMGN3's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without LINC00173 | 0.042 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[BCAM]] | B | BCAM activity raises HMGN3's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without BCAM | 0.070 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers HMGN3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[KCNK15-AS1]] | B | KCNK15-AS1 activity raises HMGN3's level | lines that do not express KCNK15-AS1 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without KCNK15-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DNAI1, FBXO15, ENSG00000132832; maybe low, not absent |
| [[SMARCD3]] | C | SMARCD3 activity raises HMGN3's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without SMARCD3 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |
| [[TMEM131L]] | C | TMEM131L activity raises HMGN3's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 3.58× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.5, 5.5); signed map (-28.7, -6.6). **Vector** length 120, 38.9% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.4 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.6 | +8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.2 | +9.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.7 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | +5.1 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -9.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.7 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group nucleosomal binding domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:79,201,245-79,234,689 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TRIP7 |
| Gene groups (HGNC) | Canonical high mobility group |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15651](https://www.uniprot.org/uniprotkb/Q15651) (High mobility group nucleosome-binding domain-containing protein 3):

> Binds to nucleosomes, regulating chromatin structure and consequently, chromatin-dependent processes such as transcription, DNA replication and DNA repair. Affects both insulin and glucagon levels and modulates the expression of pancreatic genes involved in insulin secretion. Regulates the expression of the glucose transporter SLC2A2 by binding specifically to its promoter region and recruiting PDX1 and additional transcription factors. Regulates the expression of SLC6A9, a glycine transporter …

**Summary**, from NCBI Gene [9324](https://www.ncbi.nlm.nih.gov/gene/9324):

> The protein encoded by this gene binds thyroid hormone receptor beta in the presence of thyroid hormone. The encoded protein, a member of the HMGN protein family, is thought to reduce the compactness of the chromatin fiber in nucleosomes, thereby enhancing transcription from chromatin templates. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. There is a related pseudogene on chromosome 1. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:12312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12312) · Entrez [9324](https://www.ncbi.nlm.nih.gov/gene/9324) · UniProt [Q15651](https://www.uniprot.org/uniprotkb/Q15651) · Ensembl [ENSG00000118418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118418)

## Data

Gene col 3988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3988); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3988]; `tensor/DDL_lfc|DDL_z.npy` [3988]; `embed/gene_vectors.npy` [3988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3988 or target_col == 3988). Every well: [[HMGN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
