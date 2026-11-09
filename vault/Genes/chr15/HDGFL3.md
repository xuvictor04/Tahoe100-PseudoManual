---
symbol: "HDGFL3"
type: "gene"
col: 9321
ensembl_id: "ENSG00000166503"
name: "HDGF like 3"
location: "15q25.2"
module: 124
arm: "+"
pooled_cpm: 65.31
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# HDGFL3

*HDGF like 3* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +18.4, q 0e+00, up in 30 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.41× (z +9.3, q 2e-18, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.252× (z -37.3, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM5]] (+0.69, fdr 1e-05), [[USP46]] (+0.65, fdr 2e-05), [[ARSB]] (+0.64, fdr 1e-05); moves opposite to [[IFT172]] (-0.58, fdr 6e-05), [[RAB3A]] (-0.58, fdr 1e-04), [[SUFU]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MARK1]] → it (grade B ⚠); 4 go from it, the strongest it → [[SUFU]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +18.4 | 0e+00 | 30/39 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +17.5 | 0e+00 | 30/35 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +14.1 | 4e-43 | 29/36 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +9.3 | 2e-18 | 24/38 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +7.5 | 6e-12 | 18/39 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +7.0 | 2e-10 | 24/38 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.25×** | +6.1 | 1e-07 | 19/37 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +5.6 | 2e-06 | 19/38 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +5.2 | 1e-05 | 18/38 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.13× | +4.8 | 1e-04 | 16/38 (CFPAC-1, NCI-H2347, …) | two highest doses | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +4.7 | 1e-04 | 12/38 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.18× | +4.4 | 5e-04 | 14/38 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +4.0 | 0.003 | 7/38 (A-427, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.026 | 14/38 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.035 | 13/38 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.044 | 6/38 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.13× | +3.2 | 0.046 | 9/37 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.047 | 9/38 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +3.0 | 0.082 | 7/39 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.252×** | -37.3 | 0e+00 | 38/38 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.252×** | -36.7 | 0e+00 | 38/38 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.350×** | -28.0 | 0e+00 | 38/38 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.579×** | -14.8 | 0e+00 | 32/38 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.689×** | -10.0 | 1e-21 | 25/38 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -7.3 | 3e-11 | 20/38 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.598×** | -7.2 | 4e-11 | 27/39 (C-33 A, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.676×** | -5.5 | 3e-06 | 21/38 (LOX-IMVI, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.858× | -4.1 | 0.003 | 11/38 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.868× | -3.7 | 0.011 | 12/38 (AN3 CA, J82, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.771×** | -3.6 | 0.014 | 15/39 (A-427, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.912× | -3.5 | 0.024 | 11/38 (SK-MEL-2, C32, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.893× | -3.0 | 0.11 | 9/39 (A-172, CFPAC-1, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.892× | -3.0 | 0.11 | 11/39 (HOP62, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 91.8 | 8 (7 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.04× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.131× (z -32.0) |
| [[CFPAC-1 (line)]] | alt | 79.5 | 7 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.1) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.53× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 105 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.176× (z -25.4) |
| [[A549 (line)]] | wt | 116 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -28.5) |
| [[HOP62 (line)]] | alt | 73.8 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.17× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.204× (z -18.9) |
| [[NCI-H2030 (line)]] | alt | 141 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 2.16× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.268× (z -21.8) |
| [[A-427 (line)]] | wt | 88.3 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +11.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -19.0) |
| [[A498 (line)]] | wt | 91.3 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -22.7) |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 2 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.166× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 75.2 | 2 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.173× (z -27.5) |
| [[PANC-1 (line)]] | alt | 45.7 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.235× (z -19.1) |
| [[SNU-423 (line)]] | alt | 50.0 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +12.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.284× (z -12.5) |
| [[A-172 (line)]] | wt | 82.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +13.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.210× (z -21.2) |
| [[HS-578T (line)]] | alt | 49.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.213× (z -14.8) |
| [[C-33 A (line)]] | alt | 181 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -25.4) |
| [[C32 (line)]] | wt | 70.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -17.1) |
| [[H4 (line)]] | wt | 109 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 39.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 88.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -14.6) |
| [[J82 (line)]] | alt | 111 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -26.8) |
| [[NCI-H1573 (line)]] | alt | 87.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -19.2) |
| [[SNU-1 (line)]] | wt | 151 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -18.5) |
| [[SW 900 (line)]] | alt | 62.8 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.8) ⚠ cell-cycle shift, explains ~67% of this change | [[Panobinostat (drug)]] 5 µM 0.293× (z -11.8) |
| [[AN3 CA (line)]] | alt | 169 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -12.8) |
| [[BT-474 (line)]] | alt | 74.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -16.0) |
| [[Hs 766T (line)]] | wt | 57.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 31.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 52.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 89.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -19.2) |
| [[SHP-77 (line)]] | alt | 159 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -20.3) |
| [[SK-MEL-2 (line)]] | alt | 78.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -14.0) |
| [[HCT15 (line)]] | alt | 56.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.281× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 39.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.4) ⚠ cell-cycle shift, explains ~67% of this change | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 81.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 95.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.224× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM5]] | +0.69 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[USP46]] | +0.65 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ARSB]] | +0.64 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.64 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[PRDM11]] | +0.62 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[ZMYND11]] | +0.60 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[JADE3]] | +0.60 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[FBXO30]] | +0.60 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[PYGO1]] | +0.59 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[DNMT3A]] | +0.59 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[RNASEH2B]] | +0.59 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[N4BP2]] | +0.59 | +0.40 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.58 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[RAB3A]] | -0.58 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[SUFU]] | -0.53 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[ORC4]] | -0.53 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[RANBP10]] | -0.53 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[SCRN2]] | -0.52 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.52 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[NPRL2]] | -0.52 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[RHPN2]] | -0.52 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[RNF114]] | -0.52 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[HEATR5B]] | -0.52 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[SLC27A1]] | -0.52 | -0.25 / -0.36 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARK1]] | B | MARK1 activity raises HDGFL3's level | lines that do not express MARK1 (24) vs lines expressing it (26) | 2.91× lower at baseline in the lines without MARK1 | 0.018 | ⚠ within organs, on part of the lines; also absent: FXYD6, COL4A4, ENSG00000283982 |
| [[IGF2BP1]] | B | IGF2BP1 activity raises HDGFL3's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 2.64× lower at baseline in the lines without IGF2BP1 | 0.064 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HDGFL3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HDGFL3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HECTD2]] | C | HECTD2 activity raises HDGFL3's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 8.85× lower at baseline in the lines without HECTD2 | 0.096 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUFU]] | B | HDGFL3 activity raises SUFU's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without HDGFL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |
| [[PBLD]] | B | HDGFL3 activity raises PBLD's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.16× lower at baseline in the lines without HDGFL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |
| [[SLC27A1]] | B | HDGFL3 activity raises SLC27A1's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without HDGFL3 | 0.073 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |
| [[PKD2]] | B | HDGFL3 activity raises PKD2's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without HDGFL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-9.1, 11.9); signed map (22.3, -29.3). **Vector** length 111, 29.4% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +18.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +9.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.8 | -0.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.8 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -37.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.7 | -36.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -28.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | HDGF like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:83,112,738-83,207,875 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRP-3, Hdgfrp3 |
| Gene groups (HGNC) | Heparin binding growth factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3E1](https://www.uniprot.org/uniprotkb/Q9Y3E1) (Hepatoma-derived growth factor-related protein 3):

> Enhances DNA synthesis and may play a role in cell proliferation.

**Summary**, from NCBI Gene [50810](https://www.ncbi.nlm.nih.gov/gene/50810):

> Predicted to enable microtubule binding activity. Predicted to be involved in microtubule polymerization; negative regulation of microtubule depolymerization; and neuron projection development. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24937) · Entrez [50810](https://www.ncbi.nlm.nih.gov/gene/50810) · UniProt [Q9Y3E1](https://www.uniprot.org/uniprotkb/Q9Y3E1) · Ensembl [ENSG00000166503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166503)

## Data

Gene col 9321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9321); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9321]; `tensor/DDL_lfc|DDL_z.npy` [9321]; `embed/gene_vectors.npy` [9321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9321 or target_col == 9321). Every well: [[HDGFL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDGFL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
