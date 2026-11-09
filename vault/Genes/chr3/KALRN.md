---
symbol: "KALRN"
type: "gene"
col: 8304
ensembl_id: "ENSG00000160145"
name: "kalirin RhoGEF kinase"
location: "3q21.1-q21.2"
module: 102
arm: "+"
pooled_cpm: 45.68
n_lines_expressing: 40
n_dd_up: 21
n_dd_down: 17
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# KALRN

*kalirin RhoGEF kinase* — 3q21.1-q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.67× (z +30.7, q 0e+00, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.702× (z -6.3, q 2e-07, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFBP6]] (+0.52, fdr 5e-05), [[ADAM23]] (+0.52, fdr 5e-05), [[GPR161]] (+0.51, fdr 8e-05); moves opposite to [[TAF8]] (-0.47, fdr 7e-05), [[BTBD2]] (-0.43, fdr 1e-04), [[COPS8]] (-0.42, fdr 6e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[CYP26B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.67×** | +30.7 | 0e+00 | 33/38 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +15.6 | 0e+00 | 28/38 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +13.5 | 2e-39 | 26/38 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +11.7 | 1e-29 | 24/38 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +10.0 | 1e-21 | 25/37 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +9.7 | 2e-20 | 26/38 (BT-474, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.0 | 1e-13 | 23/38 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +7.2 | 6e-11 | 22/38 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.3 | 3e-08 | 22/34 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 15/38 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.0 | 3e-05 | 10/30 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 3e-05 | 16/38 (NCI-H2347, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +4.9 | 5e-05 | 15/38 (NCI-H23, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 3e-04 | 14/39 (C32, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.29×** | +4.4 | 4e-04 | 21/38 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.001 | 16/38 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.001 | 14/38 (C32, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.702×** | -6.3 | 2e-07 | 23/38 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -5.5 | 8e-06 | 22/38 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -5.5 | 8e-06 | 21/39 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.743×** | -5.3 | 2e-05 | 21/37 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.771×** | -4.6 | 5e-04 | 19/38 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.777×** | -4.5 | 7e-04 | 16/37 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.789×** | -4.2 | 0.002 | 18/38 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.638×** | -4.2 | 0.002 | 11/38 (C32, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.791×** | -4.2 | 0.002 | 21/38 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **0.803×** | -3.9 | 0.005 | 18/37 (A-172, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.805×** | -3.9 | 0.006 | 16/38 (J82, A498, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.863× | -3.7 | 0.010 | 13/38 (H4, A498, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.820×** | -3.5 | 0.018 | 14/38 (HOP62, A498, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.688×** | -3.5 | 0.022 | 10/27 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.022 | 16/38 (HS-578T, A-172, …) | top dose only |  |
| [[Econazole (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.034 | 10/38 (SW 1088, A498, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.703×** | -3.3 | 0.037 | 13/37 (HEC-1-A, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.077 | 11/38 (H4, Panc 03.27, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.879× | -3.0 | 0.079 | 4/39 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.848× | -2.9 | 0.082 | 14/38 (NCI-H2347, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 146 | 0 | 13 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.394× (z -10.7) |
| [[A-172 (line)]] | wt | 144 | 1 | 10 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.375× (z -9.5) |
| [[H4 (line)]] | wt | 116 | 4 (1 ⚠) | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.270× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 34.7 | 2 | 9 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +17.9) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.219× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 21.4 | 2 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.75× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -11.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.282× (z -8.6) |
| [[HS-578T (line)]] | alt | 90.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -11.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.249× (z -9.7) |
| [[J82 (line)]] | alt | 148 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 14.3 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 5.26× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 23.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +12.8) | [[Digitoxin (drug)]] 0.5 µM 0.216× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 16.6 | 5 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.49× (z +11.2) | — |
| [[A549 (line)]] | wt | 26.3 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +17.2) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 30.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +15.8) | [[Digitoxin (drug)]] 0.05 µM 0.250× (z -10.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 49.6 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.17× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 26.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +12.5) | — |
| [[A498 (line)]] | wt | 89.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +15.1) | — |
| [[BT-474 (line)]] | alt | 43.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +14.0) | — |
| [[C32 (line)]] | wt | 70.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 58.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.17× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 72.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.195× (z -10.8) |
| [[HCT15 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 30.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.46× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 42.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 51.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.7) | — |
| [[SW480 (line)]] | alt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +15.8) | — |
| [[AN3 CA (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.68 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 110 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP6]] | +0.52 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[ADAM23]] | +0.52 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[GPR161]] | +0.51 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[LINC01605]] | +0.50 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[MTCL1]] | +0.49 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[RASSF2]] | +0.49 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CCDC3]] | +0.49 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[NMNAT2]] | +0.48 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CSMD2]] | +0.48 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[RHBDL3]] | +0.48 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[NECTIN3]] | +0.48 | +0.47 / +0.40 | both halves | 5e-05 | same gene group |
| [[LINC01411]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF8]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[BTBD2]] | -0.43 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[COPS8]] | -0.42 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[CCND3]] | -0.42 | -0.41 / -0.40 | both halves | 5e-05 | pathway: MAPK family signaling cascades |
| [[VPS33A]] | -0.42 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[RNF214]] | -0.41 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[DBT]] | -0.40 | -0.30 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KALRN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers KALRN's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP26B1]] | B | KALRN activity lowers CYP26B1's level | lines that do not express KALRN (10) vs lines expressing it (40) | 1.39× higher at baseline in the lines without KALRN | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EPCAM]] | B | KALRN activity raises EPCAM's level | lines that do not express KALRN (10) vs lines expressing it (40) | 1.91× lower at baseline in the lines without KALRN | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SERINC5]] | B | KALRN activity raises SERINC5's level | lines that do not express KALRN (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without KALRN | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.385). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.7, 11.7); signed map (23.4, 50.6). **Vector** length 101, 24.1% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.2 | +30.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +10.7 | +15.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.5 | +13.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -3.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.1 | -2.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | kalirin RhoGEF kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1-q21.2 — chr3:124,033,369-124,726,325 (+) |
| Ensembl biotype | protein_coding |
| Also known as | duo, Hs.8004, TRAD, DUET, Kalirin, ARHGEF24, KALNC2; previously HAPIP |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Dbl family Rho GEFs; MicroRNA protein coding host genes; TRIO family; Spectrin repeat containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 20 pathways, smallest: EPHB-mediated forward signaling; NRAGE signals death through JNK; G alpha (12/13) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [O60229](https://www.uniprot.org/uniprotkb/O60229) (Kalirin):

> Promotes the exchange of GDP by GTP. Activates specific Rho GTPase family members, thereby inducing various signaling mechanisms that regulate neuronal shape, growth, and plasticity, through their effects on the actin cytoskeleton. Induces lamellipodia independent of its GEF activity.

**Summary**, from NCBI Gene [8997](https://www.ncbi.nlm.nih.gov/gene/8997):

> Huntington's disease (HD), a neurodegenerative disorder characterized by loss of striatal neurons, is caused by an expansion of a polyglutamine tract in the HD protein huntingtin. This gene encodes a protein that interacts with the huntingtin-associated protein 1, which is a huntingtin binding protein that may function in vesicle trafficking. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:4814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4814) · Entrez [8997](https://www.ncbi.nlm.nih.gov/gene/8997) · UniProt [O60229](https://www.uniprot.org/uniprotkb/O60229) · Ensembl [ENSG00000160145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160145)

## Data

Gene col 8304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8304); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8304]; `tensor/DDL_lfc|DDL_z.npy` [8304]; `embed/gene_vectors.npy` [8304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8304 or target_col == 8304). Every well: [[KALRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KALRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
