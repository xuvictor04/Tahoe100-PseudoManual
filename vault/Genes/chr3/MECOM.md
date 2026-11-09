---
symbol: "MECOM"
type: "gene"
col: 1421
ensembl_id: "ENSG00000085276"
name: "MDS1 and EVI1 complex locus"
location: "3q26.2"
module: 44
arm: "+"
pooled_cpm: 79.39
n_lines_expressing: 32
n_dd_up: 26
n_dd_down: 24
n_dd_up_clean: 24
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 22
direction_downstream: 14
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MECOM

*MDS1 and EVI1 complex locus* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +13.7, q 3e-40, up in 26 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -10.8, q 2e-24, down in 24 of 30 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.450× (z -5.8, q 2e-06, down in 24 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A6]] (+0.68, fdr 7e-06), [[PLCH1]] (+0.65, fdr 7e-06), [[UGT1A9]] (+0.65, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.52, fdr 3e-05), [[FAM228B]] (-0.49, fdr 3e-05), [[ZIM2-AS1]] (-0.48, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[UGT1A6]] → it (grade B ⚠); 14 go from it, the strongest it → [[SAMD12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +13.7 | 3e-40 | 26/30 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.34×** | +11.7 | 3e-29 | 28/30 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +7.8 | 1e-12 | 21/30 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +5.6 | 2e-06 | 19/30 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 1e-05 | 15/30 (HOP62, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +5.1 | 3e-05 | 21/30 (A-172, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.39×** | +4.6 | 4e-04 | 21/30 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +4.3 | 0.001 | 19/30 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.003 | 15/30 (LS 180, A498, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +3.9 | 0.005 | 14/31 (HOP62, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.007 | 13/30 (A-172, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.007 | 15/31 (LS 180, LoVo, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.007 | 15/29 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.008 | 12/30 (HOP62, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.008 | 16/30 (LS 180, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.574×** | -10.8 | 2e-24 | 24/30 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.596×** | -7.1 | 3e-10 | 20/30 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.450×** | -5.8 | 2e-06 | 24/31 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.754×** | -5.5 | 5e-06 | 24/31 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.682×** | -5.3 | 2e-05 | 19/30 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -4.7 | 2e-04 | 21/30 (A-427, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.716×** | -4.6 | 4e-04 | 16/30 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.723×** | -4.5 | 6e-04 | 18/30 (HT-29, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -4.4 | 6e-04 | 18/30 (COLO 205, A-427, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.727×** | -4.4 | 6e-04 | 17/30 (HT-29, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.719×** | -4.4 | 6e-04 | 15/30 (HT-29, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -4.3 | 8e-04 | 15/30 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.726×** | -4.2 | 1e-03 | 20/30 (Hs 766T, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.763×** | -3.7 | 0.008 | 18/30 (COLO 205, LoVo, …) | all doses, flat | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.023 | 12/30 (KATO III, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.025 | 10/30 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.777×** | -3.3 | 0.028 | 7/30 (J82, BT-474, …) | top dose only | plate-row cell shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.631×** | -3.3 | 0.029 | 15/30 (KATO III, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.643×** | -3.2 | 0.044 | 12/30 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.745×** | -3.0 | 0.076 | 11/30 (HT-29, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.864× | -2.9 | 0.099 | 9/31 (KATO III, HEC-1-A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 322 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -23.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.200× (z -12.0) |
| [[Hs 766T (line)]] | wt | 412 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -18.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.274× (z -9.8) |
| [[KATO III (line)]] | alt | 344 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -12.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.471× (z -10.6) |
| [[LS 180 (line)]] | wt | 246 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.348× (z -9.9) |
| [[LoVo (line)]] | wt | 123 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -15.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.307× (z -11.0) |
| [[A-427 (line)]] | wt | 159 | 1 (1 ⚠) | 6 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.87× (z +9.5) ⚠ cell-cycle shift, explains ~79% of this change | [[Bortezomib (drug)]] 0.05 µM 0.300× (z -12.3) |
| [[HT-29 (line)]] | alt | 264 | 0 | 7 (3 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.368× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 298 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -27.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 112 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 0.270× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 91.1 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.27× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.190× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 64.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 23.8 | 2 | 0 | [[Ponatinib (drug)]] 5 µM 6.19× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 34.7 | 2 | 0 | [[Panobinostat (drug)]] 0.05 µM 3.90× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 45.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.52× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -12.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 45.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.90× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 75.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -8.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 1271 (line)]] | alt | 70.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW48 (line)]] | wt | 71.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.22 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A6]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[UGT1A9]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PTPRR]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[UGT8]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[UGT1A8]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PTPRB]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[IKZF2]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 | same gene group |
| [[LINC02331]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[EHF]] | +0.58 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[TSPAN8]] | +0.58 | +0.61 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[FAM228B]] | -0.49 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ZIM2-AS1]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[SLC28A2-AS1]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[FAM156A]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT1A6]] | B | UGT1A6 activity raises MECOM's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 4.74× lower at baseline in the lines without UGT1A6 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[UGT1A1]] | B | UGT1A1 activity raises MECOM's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 4.45× lower at baseline in the lines without UGT1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[B3GALT5]] | B | B3GALT5 activity raises MECOM's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without B3GALT5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[PTPRR]] | B | PTPRR activity raises MECOM's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without PTPRR | 0.034 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[UGT1A1]] | B | UGT1A1 activity weakens MECOM's drug response | lines that do not express UGT1A1 (19) vs lines expressing it (12) | the lines without UGT1A1 respond 0.89× as strongly (z diff +0.52); strongest at Panobinostat 0.05 µM: 2.10x vs 1.30x (z diff -3.1) | 0.036 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; target measured in part of the lines; both ways; artifact flags |
| [[PTPRB]] | B | PTPRB activity raises MECOM's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without PTPRB | 0.046 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[TCN1]] | B | TCN1 activity raises MECOM's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.86× lower at baseline in the lines without TCN1 | 0.059 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[PRSS12]] | B | PRSS12 activity raises MECOM's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without PRSS12 | 0.059 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[UGT1A6]] | B | UGT1A6 activity weakens MECOM's drug response | lines that do not express UGT1A6 (18) vs lines expressing it (13) | the lines without UGT1A6 respond 0.89× as strongly (z diff +0.42); strongest at Panobinostat 0.05 µM: 2.11x vs 1.35x (z diff -2.9) | 0.060 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; target measured in part of the lines; both ways; artifact flags |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises MECOM's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.54× lower at baseline in the lines without SH3BGRL2 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[SLC44A5]] | B | SLC44A5 activity raises MECOM's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.35× lower at baseline in the lines without SLC44A5 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |
| [[PARP8]] | B | PARP8 activity raises MECOM's level | lines that do not express PARP8 (6) vs lines expressing it (44) | 4.07× lower at baseline in the lines without PARP8 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITPKB, ZNF785 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD12]] | B | MECOM activity raises SAMD12's level | lines that do not express MECOM (18) vs lines expressing it (32) | 3.46× lower at baseline in the lines without MECOM | 0.021 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[CALML4]] | B | MECOM activity weakens CALML4's drug response | lines that do not express MECOM (18) vs lines expressing it (30) | the lines without MECOM respond 1.26× as strongly (z diff -0.50); strongest at Homoharringtonine 5 µM: 1.54x vs 1.03x (z diff -2.5) | 0.034 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PRSS12]] | B | MECOM activity raises PRSS12's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without MECOM | 0.035 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[PTPRB]] | B | MECOM activity raises PTPRB's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.86× lower at baseline in the lines without MECOM | 0.039 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[FAM156A]] | B | MECOM activity lowers FAM156A's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.50× higher at baseline in the lines without MECOM | 0.048 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[TBC1D1]] | B | MECOM activity raises TBC1D1's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.25× lower at baseline in the lines without MECOM | 0.070 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[P2RY1]] | B | MECOM activity raises P2RY1's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without MECOM | 0.092 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[PARP8]] | B | MECOM activity raises PARP8's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.91× lower at baseline in the lines without MECOM | 0.094 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[PTPRR]] | B | MECOM activity raises PTPRR's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.41× lower at baseline in the lines without MECOM | 0.095 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[PLAC8]] | B | MECOM activity raises PLAC8's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.13× lower at baseline in the lines without MECOM | 0.096 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[SAMD12-AS1]] | B | MECOM activity raises SAMD12-AS1's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without MECOM | 0.097 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[ARHGAP10]] | B | MECOM activity strengthens ARHGAP10's drug response | lines that do not express MECOM (16) vs lines expressing it (30) | the lines without MECOM respond 0.67× as strongly (z diff +1.42); strongest at Auranofin 5 µM: 0.86x vs 0.63x (z diff +2.9) | 0.098 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.1, 50.9); signed map (64.2, 2.7). **Vector** length 107, 33.2% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.65 to 4); *Aspirin ADME* (reactome, mean cos +0.65 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +13.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.0 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +4.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MDS1 and EVI1 complex locus |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:169,083,499-169,663,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MDS1-EVI1, PRDM3, KMT8E; previously MDS1, EVI1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Reactome | 9 pathways, smallest: Formation of the nephric duct; Kidney development; PKMTs methylate histone lysines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03112](https://www.uniprot.org/uniprotkb/Q03112) (Histone-lysine N-methyltransferase MECOM):

> [Isoform 1]: Functions as a transcriptional regulator binding to DNA sequences in the promoter region of target genes and regulating positively or negatively their expression. Oncogene which plays a role in development, cell proliferation and differentiation. May also play a role in apoptosis through regulation of the JNK and TGF-beta signaling. Involved in hematopoiesis.; [Isoform 7]: Displays histone methyltransferase activity and monomethylates 'Lys-9' of histone H3 (H3K9me1). Probably …

**Summary**, from NCBI Gene [2122](https://www.ncbi.nlm.nih.gov/gene/2122):

> The protein encoded by this gene is a transcriptional regulator and oncoprotein that may be involved in hematopoiesis, apoptosis, development, and cell differentiation and proliferation. The encoded protein can interact with CTBP1, SMAD3, CREBBP, KAT2B, MAPK8, and MAPK9. This gene can undergo translocation with the AML1 gene, resulting in overexpression of this gene and the onset of leukemia. Several transcript variants encoding a few different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:3498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3498) · Entrez [2122](https://www.ncbi.nlm.nih.gov/gene/2122) · UniProt [Q03112](https://www.uniprot.org/uniprotkb/Q03112) · Ensembl [ENSG00000085276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085276)

## Data

Gene col 1421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1421); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1421]; `tensor/DDL_lfc|DDL_z.npy` [1421]; `embed/gene_vectors.npy` [1421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1421 or target_col == 1421). Every well: [[MECOM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MECOM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
