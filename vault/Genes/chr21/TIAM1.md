---
symbol: "TIAM1"
type: "gene"
col: 7969
ensembl_id: "ENSG00000156299"
name: "TIAM Rac1 associated GEF 1"
location: "21q22.11"
module: 34
arm: "+"
pooled_cpm: 57.4
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TIAM1

*TIAM Rac1 associated GEF 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.20× (z +18.1, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.610× (z -7.7, q 8e-12, down in 18 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.772× (z -4.2, q 0.002, down in 14 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCOR1]] (+0.61, fdr 1e-05), [[OSBPL3]] (+0.60, fdr 8e-06), [[PSD3]] (+0.60, fdr 1e-05); moves opposite to [[LRRC27]] (-0.60, fdr 1e-05), [[LINC00663]] (-0.57, fdr 8e-05), [[POLR1HASP]] (-0.57, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PARM1]] → it (grade B ⚠); 3 go from it, the strongest it → [[LUZP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +18.1 | 0e+00 | 35/37 (SW1417, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.01×** | +17.9 | 0e+00 | 35/37 (J82, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.85×** | +17.0 | 0e+00 | 35/37 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.31×** | +13.6 | 7e-40 | 35/37 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.25×** | +13.2 | 2e-37 | 36/37 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +11.0 | 2e-26 | 31/37 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.40×** | +7.4 | 9e-12 | 28/37 (NCI-H2030, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +6.3 | 2e-08 | 23/37 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +6.1 | 7e-08 | 18/36 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.7 | 1e-04 | 18/37 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 16/36 (A-172, H4, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.27×** | +3.8 | 0.008 | 16/37 (H4, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.5 | 0.018 | 15/33 (C-33 A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.018 | 16/36 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.24×** | +3.4 | 0.023 | 13/37 (SW480, HOP62, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.025 | 15/37 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.041 | 10/37 (J82, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.050 | 14/36 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.067 | 5/37 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -7.7 | 8e-12 | 18/30 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.639×** | -7.2 | 1e-10 | 22/37 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.682×** | -5.7 | 2e-06 | 18/31 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.540×** | -5.2 | 3e-05 | 16/27 (NCI-H1792, H4, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.760×** | -4.4 | 0.001 | 19/36 (SW 1271, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.764×** | -4.3 | 0.001 | 19/37 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.772×** | -4.2 | 0.002 | 14/37 (SNU-423, SW 1088, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.611×** | -4.2 | 0.002 | 16/38 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.622×** | -4.0 | 0.004 | 17/36 (CFPAC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -3.8 | 0.010 | 16/37 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.789×** | -3.7 | 0.013 | 15/37 (A-427, H4, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.801×** | -3.6 | 0.017 | 18/37 (BT-474, J82, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.3 | 0.043 | 4/38 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.061 | 12/37 (SW480, SW48, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 76.6 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 133 | 6 (2 ⚠) | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.09× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -17.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 28.0 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +18.7) | — |
| [[J82 (line)]] | alt | 37.1 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.58× (z +17.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.39× (z +15.8) | — |
| [[A-427 (line)]] | wt | 92.4 | 5 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.64× (z +15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.76× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -19.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.7 | 7 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.02× (z +14.6) | — |
| [[H4 (line)]] | wt | 78.4 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.58× (z +11.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.64× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 48.2 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.19× (z +17.4) | — |
| [[KATO III (line)]] | alt | 76.3 | 4 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.00× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 37.7 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.30× (z +17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 9.09× (z +17.3) | — |
| [[NCI-H460 (line)]] | wt | 41.0 | 4 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.15× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 118 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.39× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.48× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 104 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.11× (z +11.4) | — |
| [[SW48 (line)]] | wt | 58.0 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.17× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.213× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.76× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 50.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -11.8) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.231× (z -9.6) |
| [[C-33 A (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 165 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 42.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.28× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.61× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 59.0 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.55× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 55.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 279 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -16.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.15× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 87.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -9.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 188 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.21× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 84.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 81.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 45.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.44× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0922× (z -9.2) |
| [[SW 1271 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0909× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~23% of this change |
| [[A498 (line)]] | wt | 9.54 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.94 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 57.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR1]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[OSBPL3]] | +0.60 | +0.58 / +0.59 | both halves | 8e-06 | same gene group |
| [[PSD3]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 | same gene group |
| [[LAMA3]] | +0.59 | +0.61 / +0.45 | both halves | 3e-05 | pathway: Cell junction organization |
| [[EML4]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.58 | +0.51 / +0.45 | both halves | 3e-05 | pathway: RAC1 GTPase cycle |
| [[CD58]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[STRIP2]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LIPG]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SERPINB1]] | +0.56 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[AREG]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[LYPD3]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.60 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[LINC00663]] | -0.57 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[POLR1HASP]] | -0.57 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[MAIP1]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ENTPD3-AS1]] | -0.54 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[DICER1-AS1]] | -0.54 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ARFGEF2]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ERMARD]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[NUDT13]] | -0.52 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SUPV3L1]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SAFB]] | -0.51 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[GPALPP1]] | -0.51 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARM1]] | B | PARM1 activity strengthens TIAM1's drug response | lines that do not express PARM1 (22) vs lines expressing it (16) | the lines without PARM1 respond 0.97× as strongly (z diff +0.55); strongest at Panobinostat 0.05 µM: 1.96x vs 2.77x (z diff +2.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A; target measured in part of the lines; artifact flags |
| [[ACP7]] | B | ACP7 activity raises TIAM1's level | lines that do not express ACP7 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without ACP7 | 0.086 | ⚠ within organs, on part of the lines; also absent: FGF20, ONECUT3, GPR87 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUZP1]] | B | TIAM1 activity lowers LUZP1's level | lines that do not express TIAM1 (11) vs lines expressing it (39) | 1.56× higher at baseline in the lines without TIAM1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RASSF2, SPATC1L, DNAH2 |
| [[KRT15]] | B | TIAM1 activity raises KRT15's level | lines that do not express TIAM1 (11) vs lines expressing it (39) | 1.19× lower at baseline in the lines without TIAM1 | 0.082 | ⚠ within organs, on part of the lines; also absent: RASSF2, SPATC1L, DNAH2 |
| [[MCCC1]] | B | TIAM1 activity raises MCCC1's level | lines that do not express TIAM1 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without TIAM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: RASSF2, SPATC1L, DNAH2 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.9, 19.4); signed map (1.9, 41.6). **Vector** length 101, 23.7% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.8 | +18.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.3 | +11.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.4 | +13.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +7.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | TIAM Rac1 associated GEF 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:31,118,416-31,559,977 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; PDZ domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MITOTIC_SPINDLE |
| Reactome | 30 pathways, smallest: Activated NTRK2 signals through CDK5; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST); Signaling by NTRK2 (TRKB) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13009](https://www.uniprot.org/uniprotkb/Q13009) (Rho guanine nucleotide exchange factor TIAM1):

> Guanyl-nucleotide exchange factor that activates RHO-like proteins and connects extracellular signals to cytoskeletal activities. Activates RAC1, CDC42, and to a lesser extent RHOA and their downstream signaling to regulate processes like cell adhesion and cell migration.

**Summary**, from NCBI Gene [7074](https://www.ncbi.nlm.nih.gov/gene/7074):

> This gene encodes a RAC1-specific guanine nucleotide exchange factor (GEF). GEFs mediate the exchange of guanosine diphosphate (GDP) for guanosine triphosphate (GTP). The binding of GTP induces a conformational change in RAC1 that allows downstream effectors to bind and transduce a signal. This gene thus regulates RAC1 signaling pathways that affect cell shape, migration, adhesion, growth, survival, and polarity, as well as influencing actin cytoskeletal formation, endocytosis, and membrane …

**Accessions** — [HGNC:11805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11805) · Entrez [7074](https://www.ncbi.nlm.nih.gov/gene/7074) · UniProt [Q13009](https://www.uniprot.org/uniprotkb/Q13009) · Ensembl [ENSG00000156299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156299)

## Data

Gene col 7969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7969); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7969]; `tensor/DDL_lfc|DDL_z.npy` [7969]; `embed/gene_vectors.npy` [7969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7969 or target_col == 7969). Every well: [[TIAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
