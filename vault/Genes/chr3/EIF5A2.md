---
symbol: "EIF5A2"
type: "gene"
col: 8720
ensembl_id: "ENSG00000163577"
name: "eukaryotic translation initiation factor 5A2"
location: "3q26.2"
module: 34
arm: "+"
pooled_cpm: 22.15
n_lines_expressing: 47
n_dd_up: 36
n_dd_down: 11
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# EIF5A2

*eukaryotic translation initiation factor 5A2* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.56× (z +20.6, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.592× (z -8.2, q 1e-13, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2]] (+0.66, fdr 1e-05), [[PLEK2]] (+0.60, fdr 2e-05), [[GOLT1A]] (+0.60, fdr 1e-05); moves opposite to [[WBP11]] (-0.56, fdr 2e-05), [[SUPV3L1]] (-0.55, fdr 1e-05), [[ALDH2]] (-0.48, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CCDC88A]] → it (grade B ⚠); 2 go from it, the strongest it → [[LAMC2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +20.6 | 0e+00 | 37/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.61×** | +14.8 | 0e+00 | 40/44 (SW1417, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.59×** | +14.7 | 0e+00 | 41/44 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.44×** | +13.8 | 3e-41 | 40/44 (HT-29, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.17×** | +12.0 | 4e-31 | 29/34 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.21×** | +11.8 | 4e-30 | 22/28 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.99×** | +10.6 | 1e-24 | 36/43 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +10.3 | 7e-23 | 37/45 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +9.9 | 2e-21 | 33/43 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +9.9 | 4e-21 | 34/43 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +8.8 | 9e-17 | 34/39 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.74×** | +8.5 | 7e-16 | 29/44 (COLO 205, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.72×** | +8.4 | 2e-15 | 27/43 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +8.4 | 3e-15 | 34/44 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.66×** | +7.8 | 2e-13 | 27/44 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +7.1 | 4e-11 | 29/44 (SNU-423, LS 180, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.4 | 5e-09 | 25/43 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.0 | 6e-08 | 26/42 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 1e-07 | 23/44 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.1 | 7e-06 | 16/45 (A498, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +4.7 | 7e-05 | 17/43 (A498, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.001 | 17/45 (HOP62, HS-578T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.002 | 10/45 (SW1417, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.010 | 11/43 (NCI-H1792, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.010 | 11/40 (AsPC-1, A549, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.592×** | -8.2 | 1e-13 | 26/45 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.726×** | -4.9 | 2e-04 | 21/44 (A-172, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.723×** | -4.8 | 3e-04 | 17/43 (A549, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.772×** | -4.8 | 3e-04 | 21/45 (CFPAC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.775×** | -4.3 | 0.001 | 18/45 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Megestrol (drug)]] 5 µM |  | **0.820×** | -4.3 | 0.001 | 23/45 (A-172, A498, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.614×** | -3.9 | 0.007 | 16/44 (AsPC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.836× | -3.9 | 0.008 | 19/45 (NCI-H1792, BT-474, …) | all doses, stronger at high dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.848× | -3.6 | 0.020 | 13/45 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.790×** | -3.4 | 0.039 | 13/44 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.857× | -3.4 | 0.039 | 11/45 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.661×** | -3.3 | 0.039 | 11/43 (AsPC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.086 | 8/44 (A498, SNU-423, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.088 | 8/44 (Panc 03.27, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 52.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +15.4) | — |
| [[SW1417 (line)]] | alt | 27.2 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +14.5) | — |
| [[COLO 205 (line)]] | alt | 12.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 8.88 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +10.8) | — |
| [[SW480 (line)]] | alt | 39.6 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.0) | [[Trametinib (drug)]] 5 µM 0.387× (z -9.3) |
| [[KATO III (line)]] | alt | 10.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.54× (z +9.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.56× (z +9.0) | — |
| [[A498 (line)]] | wt | 24.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +12.0) | — |
| [[J82 (line)]] | alt | 81.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.38× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 29.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0889× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +10.9) | — |
| [[H4 (line)]] | wt | 21.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.27× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +15.3) | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 57.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.9) | — |
| [[A-172 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2]] | +0.66 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.60 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[GOLT1A]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[S100A16]] | +0.58 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[MYL12A]] | +0.57 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[SEPTIN10]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[CDCP1]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TNFRSF12A]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[DCBLD2]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[ITGB5]] | +0.55 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP11]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SUPV3L1]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ALDH2]] | -0.48 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[CNOT1]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ZNF451]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HMBOX1]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[MIA2]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[SAFB]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MAP2K5]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC88A]] | B | CCDC88A activity raises EIF5A2's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without CCDC88A | 0.037 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[MAP2K1]] | B | MAP2K1 activity raises EIF5A2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CALB2]] | B | CALB2 activity raises EIF5A2's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without CALB2 | 0.046 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[CCDC68]] | B | CCDC68 activity lowers EIF5A2's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 1.67× higher at baseline in the lines without CCDC68 | 0.050 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[RAB3B]] | B | RAB3B activity raises EIF5A2's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without RAB3B | 0.054 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[KIRREL1]] | B | KIRREL1 activity raises EIF5A2's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without KIRREL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[SAMD5]] | B | SAMD5 activity lowers EIF5A2's level | lines that do not express SAMD5 (15) vs lines expressing it (35) | 1.46× higher at baseline in the lines without SAMD5 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000287976, ENSG00000227681, TSPAN7 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC2]] | C | EIF5A2 activity lowers LAMC2's level | lines that do not express EIF5A2 (3) vs lines expressing it (47) | 13.68× higher at baseline in the lines without EIF5A2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with MET; also absent: ZDHHC14, GRK5, GASAL1; maybe low, not absent; its own permutation p |
| [[SH2D3A]] | C | EIF5A2 activity lowers SH2D3A's level | lines that do not express EIF5A2 (3) vs lines expressing it (47) | 6.74× higher at baseline in the lines without EIF5A2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with MET; also absent: ZDHHC14, GRK5, GASAL1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.4, 3.1); signed map (8.7, 41.5). **Vector** length 89.7, 21.2% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.4 | +8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.9 | +8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.7 | +7.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +3.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.1 | -8.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -4.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 5A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:170,888,418-170,908,644 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Hypusine synthesis from eIF5A-lysine; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZV4](https://www.uniprot.org/uniprotkb/Q9GZV4) (Eukaryotic translation initiation factor 5A-2):

> Translation factor that promotes translation elongation and termination, particularly upon ribosome stalling at specific amino acid sequence contexts. Binds between the exit (E) and peptidyl (P) site of the ribosome and promotes rescue of stalled ribosome: specifically required for efficient translation of polyproline-containing peptides as well as other motifs that stall the ribosome. Acts as a ribosome quality control (RQC) cofactor by joining the RQC complex to facilitate peptidyl transfer …

**Summary**, from NCBI Gene [56648](https://www.ncbi.nlm.nih.gov/gene/56648):

> Predicted to enable translation elongation factor activity. Predicted to be involved in translational elongation. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3301) · Entrez [56648](https://www.ncbi.nlm.nih.gov/gene/56648) · UniProt [Q9GZV4](https://www.uniprot.org/uniprotkb/Q9GZV4) · Ensembl [ENSG00000163577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163577)

## Data

Gene col 8720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8720); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8720]; `tensor/DDL_lfc|DDL_z.npy` [8720]; `embed/gene_vectors.npy` [8720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8720 or target_col == 8720). Every well: [[EIF5A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF5A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
