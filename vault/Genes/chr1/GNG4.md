---
symbol: "GNG4"
type: "gene"
col: 9615
ensembl_id: "ENSG00000168243"
name: "G protein subunit gamma 4"
location: "1q42.3"
module: 101
arm: "+"
pooled_cpm: 25.63
n_lines_expressing: 30
n_dd_up: 25
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# GNG4

*G protein subunit gamma 4* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.23× (z +37.8, q 0e+00, up in 20 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.693× (z -5.4, q 3e-05, down in 13 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP3B2]] (+0.63, fdr 1e-05), [[NFATC1]] (+0.60, fdr 1e-05), [[NANOS3]] (+0.59, fdr 1e-05); moves opposite to [[LRIG2]] (-0.57, fdr 1e-05), [[JKAMP]] (-0.55, fdr 3e-05), [[VLDLR]] (-0.53, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[LMNB1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.23×** | +37.8 | 0e+00 | 20/27 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +18.5 | 0e+00 | 14/27 (BT-474, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +16.1 | 0e+00 | 19/25 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.83×** | +14.6 | 0e+00 | 20/27 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.67×** | +14.4 | 1e-44 | 15/27 (SW480, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +13.7 | 2e-40 | 12/21 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +13.6 | 2e-40 | 17/27 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +7.9 | 1e-13 | 13/24 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.7 | 7e-13 | 13/28 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.5 | 2e-12 | 13/28 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.64×** | +7.2 | 3e-11 | 12/27 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.6 | 2e-09 | 7/25 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 1e-06 | 9/27 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.4 | 2e-06 | 7/26 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +4.9 | 4e-05 | 10/27 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +4.7 | 9e-05 | 11/27 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 4e-04 | 9/27 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.2 | 8e-04 | 9/28 (SW 900, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.001 | 7/27 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.068 | 3/28 (AsPC-1, SW 900, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.068 | 8/27 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.072 | 5/26 (SHP-77, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.693×** | -5.4 | 3e-05 | 13/27 (A549, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.677×** | -5.3 | 3e-05 | 11/27 (SW48, SK-MEL-2, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.728×** | -4.7 | 6e-04 | 16/27 (A549, NCI-H23, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.736×** | -4.5 | 9e-04 | 8/27 (A549, NCI-H460, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.582×** | -4.2 | 0.004 | 17/26 (A-427, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.830×** | -3.9 | 0.009 | 7/28 (A-172, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.809×** | -3.9 | 0.009 | 10/28 (SW48, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.013 | 11/27 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.019 | 8/27 (A549, AsPC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.019 | 12/27 (SW48, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.800×** | -3.1 | 0.097 | 15/27 (SW48, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.866× | -3.0 | 0.11 | 4/27 (SW48, SW480, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.676× | -3.0 | 0.11 | 11/26 (A549, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.9 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +28.3) | — |
| [[SW48 (line)]] | wt | 121 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.197× (z -9.9) |
| [[SW480 (line)]] | alt | 78.5 | 8 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +24.6) | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -10.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 22.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +21.1) | — |
| [[NCI-H1573 (line)]] | alt | 32.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +19.9) | — |
| [[NCI-H23 (line)]] | alt | 35.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.5) |
| [[SHP-77 (line)]] | alt | 284 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.59× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -15.1) |
| [[A549 (line)]] | wt | 74.3 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.244× (z -9.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 0.233× (z -8.7) |
| [[HOP62 (line)]] | alt | 7.78 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.4× (z +22.5) | — |
| [[RPMI-7951 (line)]] | alt | 9.04 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 40.8× (z +19.0) | [[Macitentan (drug)]] 5 µM 0.0677× (z -9.4) |
| [[SW 900 (line)]] | alt | 27.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +21.4) | — |
| [[BT-474 (line)]] | alt | 10.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +12.1) | [[Simotinib (drug)]] 5 µM 0.116× (z -9.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 31.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +18.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.328× (z -8.9) ⚠ toxic |
| [[A498 (line)]] | wt | 22.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 33.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +15.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 53.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +14.9) | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 9.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0575× (z -9.2) |
| [[AN3 CA (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3B2]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[NFATC1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 | pathway: Beta-catenin independent WNT signaling |
| [[NANOS3]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[HCG20]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ASIC2]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SERPINB9]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[DPH1-AS1]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SSUH2]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[OLFM2]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DNAH17]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[AGO2]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 | pathway: Beta-catenin independent WNT signaling |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2]] | -0.57 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[JKAMP]] | -0.55 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[VLDLR]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[INPP5B]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[CDK5RAP1]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[VDAC3]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PRUNE1]] | -0.51 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[ZNF449]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[GAPVD1]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[ZNF174]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZDHHC7]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 | pathway: ESR-mediated signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GNG4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLRC3]] | B | KLRC3 activity raises GNG4's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without KLRC3 | 0.037 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[PHLDA2]] | B | PHLDA2 activity lowers GNG4's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.16× higher at baseline in the lines without PHLDA2 | 0.075 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[MAGEA4]] | B | MAGEA4 activity raises GNG4's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 3.41× lower at baseline in the lines without MAGEA4 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[ELFN1]] | C | ELFN1 activity raises GNG4's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.75× lower at baseline in the lines without ELFN1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; co-absent with the target |
| [[OLFM1]] | C | OLFM1 activity raises GNG4's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 3.62× lower at baseline in the lines without OLFM1 | 0.049 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMNB1-DT]] | B | GNG4 activity raises LMNB1-DT's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 1.35× lower at baseline in the lines without GNG4 | 0.048 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[LNC-LBCS]] | B | GNG4 activity raises LNC-LBCS's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without GNG4 | 0.055 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[NKAIN1]] | B | GNG4 activity raises NKAIN1's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 1.40× lower at baseline in the lines without GNG4 | 0.058 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[ZNF174]] | B | GNG4 activity raises ZNF174's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 1.14× lower at baseline in the lines without GNG4 | 0.071 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[OSBP2]] | B | GNG4 activity raises OSBP2's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 1.40× lower at baseline in the lines without GNG4 | 0.072 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B |
| [[OLFM1]] | C | GNG4 activity raises OLFM1's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 4.02× lower at baseline in the lines without GNG4 | 0.001 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B; co-absent with the target |
| [[AP3B2]] | C | GNG4 activity raises AP3B2's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without GNG4 | 0.067 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B; co-absent with the target |
| [[CHST8]] | C | GNG4 activity raises CHST8's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 2.49× lower at baseline in the lines without GNG4 | 0.098 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B; co-absent with the target |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.5, -3.0); signed map (8.5, 26.8). **Vector** length 92.5, 23.6% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +37.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.3 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +14.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.8 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -5.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,547,685-235,650,754 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits gamma |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [P50150](https://www.uniprot.org/uniprotkb/P50150) (Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-4):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems. The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction.

**Summary**, from NCBI Gene [2786](https://www.ncbi.nlm.nih.gov/gene/2786):

> Predicted to enable G-protein beta-subunit binding activity. Involved in negative regulation of cell growth. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4407) · Entrez [2786](https://www.ncbi.nlm.nih.gov/gene/2786) · UniProt [P50150](https://www.uniprot.org/uniprotkb/P50150) · Ensembl [ENSG00000168243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168243)

## Data

Gene col 9615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9615); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9615]; `tensor/DDL_lfc|DDL_z.npy` [9615]; `embed/gene_vectors.npy` [9615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9615 or target_col == 9615). Every well: [[GNG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
