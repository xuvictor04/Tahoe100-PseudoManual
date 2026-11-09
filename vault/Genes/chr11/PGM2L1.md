---
symbol: "PGM2L1"
type: "gene"
col: 9120
ensembl_id: "ENSG00000165434"
name: "phosphoglucomutase 2 like 1"
location: "11q13.4"
module: 5
arm: "-"
pooled_cpm: 59.78
n_lines_expressing: 46
n_dd_up: 40
n_dd_down: 11
n_dd_up_clean: 37
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PGM2L1

*phosphoglucomutase 2 like 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.90× (z +24.1, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.364× (z -12.0, q 3e-30, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMOD1]] (+0.59, fdr 1e-05), [[CYRIA]] (+0.55, fdr 1e-05), [[RIPK2]] (+0.54, fdr 1e-05); moves opposite to [[ALG8]] (-0.62, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.57, fdr 1e-05), [[SP2-AS1]] (-0.54, fdr 6e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SESN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.90×** | +24.1 | 0e+00 | 40/44 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +23.1 | 0e+00 | 37/44 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.70×** | +22.6 | 0e+00 | 37/44 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +16.6 | 0e+00 | 32/44 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +15.4 | 0e+00 | 37/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +10.4 | 2e-23 | 31/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +9.9 | 4e-21 | 29/44 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +9.5 | 1e-19 | 25/44 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.46×** | +8.6 | 4e-16 | 28/43 (NCI-H2030, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +8.6 | 6e-16 | 31/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +8.4 | 2e-15 | 25/45 (C32, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +8.1 | 3e-14 | 25/45 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +8.0 | 5e-14 | 21/44 (A549, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM |  | **1.38×** | +7.8 | 3e-13 | 26/46 (BT-474, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +7.6 | 1e-12 | 23/43 (C32, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +7.1 | 3e-11 | 21/44 (C32, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -12.0 | 3e-30 | 34/45 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -10.5 | 3e-23 | 35/44 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.681×** | -8.7 | 6e-16 | 23/43 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -7.0 | 5e-10 | 21/44 (A-172, SW48, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -6.3 | 4e-08 | 21/44 (SW48, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.759×** | -6.2 | 4e-08 | 22/44 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.779×** | -5.4 | 4e-06 | 20/44 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.812×** | -4.7 | 2e-04 | 15/43 (NCI-H460, HS-578T, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.678×** | -4.6 | 3e-04 | 16/34 (C32, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -4.5 | 4e-04 | 21/44 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.821×** | -4.4 | 5e-04 | 17/44 (A-172, A549, …) | rises with dose | composition shift |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.887× | -3.8 | 0.006 | 7/44 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 0.846× | -3.8 | 0.007 | 18/43 (hTERT-HPNE, A549, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.841× | -3.8 | 0.007 | 16/46 (NCI-H460, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.5 | 0.020 | 16/44 (COLO 205, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.855× | -3.3 | 0.029 | 14/43 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.047 | 11/43 (NCI-H460, SW480, …) | all doses, flat | low cells (technical?) |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.903× | -3.1 | 0.063 | 6/44 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.873× | -2.9 | 0.083 | 8/44 (A549, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 184 | 0 | 27 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -19.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -12.3) |
| [[BT-474 (line)]] | alt | 112 | 8 (1 ⚠) | 1 (1 ⚠) | [[Afatinib (drug)]] 0.5 µM 3.79× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -8.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2030 (line)]] | alt | 35.7 | 6 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.88× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.4) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -10.0) |
| [[PANC-1 (line)]] | alt | 43.8 | 6 | 1 | [[Panobinostat (drug)]] 5 µM 4.37× (z +17.7) | [[TAK-901 (drug)]] 5 µM 0.142× (z -12.3) |
| [[SW480 (line)]] | alt | 49.9 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.9) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.13× (z +9.8) | [[PH-797804 (drug)]] 5 µM 0.284× (z -8.6) |
| [[A-427 (line)]] | wt | 40.0 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 4.12× (z +12.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -9.3) |
| [[A549 (line)]] | wt | 119 | 1 (1 ⚠) | 5 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.20× (z +10.7) ⚠ cell-cycle shift, explains ~15% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.146× (z -9.6) |
| [[COLO 205 (line)]] | alt | 95.6 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.102× (z -17.0) |
| [[HT-29 (line)]] | alt | 39.5 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 4.23× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.306× (z -8.5) |
| [[LoVo (line)]] | wt | 26.2 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.26× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 36.2 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.35× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 87.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.4) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 21.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +10.0) | — |
| [[RKO (line)]] | wt | 16.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +9.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.93× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 162 | 4 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.37× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -21.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 88.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[J82 (line)]] | alt | 29.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +10.3) | — |
| [[KATO III (line)]] | alt | 38.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.19× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 21.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.59× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 20.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.28× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 85.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.74× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 94.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.4) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -13.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H596 (line)]] | alt | 64.9 | 1 | 1 | [[Oxaprozin (drug)]] 5 µM 2.31× (z +9.3) | [[Fulvestrant (drug)]] 5 µM 0.219× (z -17.2) |
| [[SW1417 (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.28× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A498 (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +15.7) ⚠ cell-cycle shift, explains ~81% of this change | — |
| [[C32 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0799× (z -11.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0923× (z -8.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 51.6 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.217× (z -11.7) |
| [[SNU-423 (line)]] | alt | 89.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.238× (z -8.5) |
| [[SW 900 (line)]] | alt | 28.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.84× (z +8.8) | — |
| [[SW48 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.213× (z -10.1) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMOD1]] | +0.59 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.54 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PLPP1]] | +0.53 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RAB11FIP1]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[TUBA1A]] | +0.53 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[KRAS]] | +0.52 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[DAAM1]] | +0.52 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SPAG9]] | +0.51 | +0.37 / +0.40 | both halves | 8e-05 |  |
| [[RAB8B]] | +0.51 | +0.37 / +0.54 | both halves | 7e-05 |  |
| [[TAOK3]] | +0.51 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[CCDC112]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.62 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SP2-AS1]] | -0.54 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[E2F3]] | -0.54 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[WDR4]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ACAD9]] | -0.54 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MRM1]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[EMG1]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TSR1]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PIGW]] | -0.53 | -0.48 / -0.37 | both halves | 9e-05 | STRING 412 |
| [[PRMT3]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[EEF1AKMT1]] | -0.51 | -0.50 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SESN3]] | B | SESN3 activity raises PGM2L1's level | lines that do not express SESN3 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without SESN3 | 0.049 | ⚠ within organs, on part of the lines; also absent: EPHA4, GNG2, ST6GALNAC5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (17.8, -1.9); signed map (-8.8, 14.5). **Vector** length 119, 32.4% of its response variance represented; |z| ≥ 3 in 1,581 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +16.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +9.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +5.2 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +15.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +8.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +8.4 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.1 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglucomutase 2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,330,316-74,398,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32029, BM32A |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PCE3](https://www.uniprot.org/uniprotkb/Q6PCE3) (Glucose 1,6-bisphosphate synthase):

> Glucose 1,6-bisphosphate synthase using 1,3-bisphosphoglycerate as a phosphate donor and a series of 1-phosphate sugars, including glucose 1-phosphate, mannose 1-phosphate, ribose 1-phosphate and deoxyribose 1-phosphate, as acceptors. In vitro, also exhibits very low phosphopentomutase and phosphoglucomutase activity which are most probably not physiologically relevant.

**Summary**, from NCBI Gene [283209](https://www.ncbi.nlm.nih.gov/gene/283209):

> Enables glucose-1,6-bisphosphate synthase activity and phosphoglucomutase activity. Predicted to be involved in glucose metabolic process. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20898) · Entrez [283209](https://www.ncbi.nlm.nih.gov/gene/283209) · UniProt [Q6PCE3](https://www.uniprot.org/uniprotkb/Q6PCE3) · Ensembl [ENSG00000165434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165434)

## Data

Gene col 9120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9120); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9120]; `tensor/DDL_lfc|DDL_z.npy` [9120]; `embed/gene_vectors.npy` [9120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9120 or target_col == 9120). Every well: [[PGM2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGM2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
