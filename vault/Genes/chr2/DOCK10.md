---
symbol: "DOCK10"
type: "gene"
col: 5773
ensembl_id: "ENSG00000135905"
name: "dedicator of cytokinesis 10"
location: "2q36.2"
module: 121
arm: "+"
pooled_cpm: 55.24
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 34
n_dd_up_clean: 11
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 13
direction_downstream: 16
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# DOCK10

*dedicator of cytokinesis 10* — 2q36.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +16.7, q 0e+00, up in 16 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.250× (z -23.1, q 0e+00, down in 22 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLR6]] (+0.66, fdr 9e-06), [[PHACTR1]] (+0.65, fdr 1e-05), [[TLR1]] (+0.62, fdr 2e-05); moves opposite to [[ZDHHC9]] (-0.59, fdr 1e-05), [[MINK1]] (-0.51, fdr 1e-04), [[PACSIN2]] (-0.50, fdr 5e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC02328]] → it (grade B ⚠); 16 go from it, the strongest it → [[PCED1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +16.7 | 0e+00 | 16/24 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +9.7 | 1e-19 | 17/24 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.8 | 8e-13 | 15/24 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +7.1 | 2e-10 | 13/24 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.7 | 1e-06 | 11/24 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.3 | 9e-06 | 12/23 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 2e-05 | 11/24 (SW 900, SNU-423, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.4 | 8e-04 | 12/24 (HOP62, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.009 | 13/23 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.028 | 9/24 (SNU-423, Hs 766T, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.23×** | +3.4 | 0.029 | 7/24 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.047 | 10/24 (NCI-H1792, J82, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.052 | 8/24 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.067 | 9/24 (NCI-H2347, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.250×** | -23.1 | 0e+00 | 22/24 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.250×** | -23.1 | 0e+00 | 21/24 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.353×** | -17.4 | 0e+00 | 22/24 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.628×** | -7.8 | 1e-12 | 19/24 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -6.7 | 2e-09 | 19/25 (NCI-H1573, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -6.2 | 4e-08 | 16/24 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -5.9 | 3e-07 | 17/22 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.707×** | -5.5 | 2e-06 | 18/24 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.727×** | -5.3 | 7e-06 | 16/24 (H4, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.2 | 1e-05 | 18/24 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.727×** | -4.9 | 6e-05 | 16/24 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.752×** | -4.7 | 1e-04 | 16/24 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.819×** | -4.7 | 1e-04 | 12/24 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.755×** | -4.7 | 1e-04 | 15/24 (NCI-H1573, SW 1088, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.753×** | -4.4 | 5e-04 | 14/22 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.607×** | -4.3 | 5e-04 | 16/24 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.774×** | -4.3 | 7e-04 | 11/24 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.739×** | -4.1 | 0.001 | 11/24 (NCI-H1573, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.783×** | -4.1 | 0.001 | 12/24 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.788×** | -4.0 | 0.002 | 13/24 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -24.8) |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.197× (z -16.8) |
| [[A498 (line)]] | wt | 204 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 116 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.79× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.132× (z -21.9) |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -11.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.248× (z -10.9) |
| [[A-172 (line)]] | wt | 38.8 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +25.0) | — |
| [[Hs 766T (line)]] | wt | 21.3 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.6) | [[Allantoin (drug)]] 0.05 µM 0.137× (z -11.9) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.198× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 207 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.144× (z -16.9) |
| [[J82 (line)]] | alt | 68.7 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +20.4) | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 36.8 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -10.4) |
| [[A549 (line)]] | wt | 117 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.119× (z -21.2) |
| [[HS-578T (line)]] | alt | 130 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.0) | [[Belinostat (drug)]] 5 µM 0.172× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 152 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -19.1) |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -18.6) |
| [[RPMI-7951 (line)]] | alt | 127 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -11.2) |
| [[SNU-423 (line)]] | alt | 71.4 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +19.0) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -12.5) |
| [[SW 900 (line)]] | alt | 95.7 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.251× (z -12.9) |
| [[H4 (line)]] | wt | 65.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -9.8) |
| [[PANC-1 (line)]] | alt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.4) | — |
| [[A-427 (line)]] | wt | 8.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.45 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.36 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLR6]] | +0.66 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[PHACTR1]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TLR1]] | +0.62 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ZNF804A]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ADAMTS12]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[EBF1]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CNTN6]] | +0.58 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[DGKI]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.57 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[MSR1]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[BNC2]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[FAP]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC9]] | -0.59 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MINK1]] | -0.51 | -0.45 / -0.34 | both halves | 1e-04 | same gene group |
| [[PACSIN2]] | -0.50 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SLC35A3]] | -0.50 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[ESYT2]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RALGAPA2]] | -0.49 | -0.48 / -0.29 | both halves | 2e-04 | same gene group |
| [[AP3S1]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[FHIP1B]] | -0.48 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[CYB5R3]] | -0.48 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[COPS8]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[RAP1A]] | -0.47 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[RPS6KA2]] | -0.47 | -0.42 / -0.35 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02328]] | B | LINC02328 activity raises DOCK10's level | lines that do not express LINC02328 (14) vs lines expressing it (36) | 3.22× lower at baseline in the lines without LINC02328 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, PDE4B; maybe low, not absent |
| [[AMIGO2]] | B | AMIGO2 activity raises DOCK10's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.99× lower at baseline in the lines without AMIGO2 | 0.062 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[NR3C1]] | B | NR3C1 activity lowers DOCK10's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PCED1B]] | B | PCED1B activity raises DOCK10's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.68× lower at baseline in the lines without PCED1B | 0.092 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[EBF1]] | C | EBF1 activity raises DOCK10's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 7.95× lower at baseline in the lines without EBF1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises DOCK10's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 9.32× lower at baseline in the lines without MSC-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises DOCK10's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 5.72× lower at baseline in the lines without FRMD4A | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[MSC]] | C | MSC activity raises DOCK10's level | lines that do not express MSC (34) vs lines expressing it (16) | 7.28× lower at baseline in the lines without MSC | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[ABCC9]] | C | ABCC9 activity raises DOCK10's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 4.27× lower at baseline in the lines without ABCC9 | 0.056 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[SLC4A4]] | C | SLC4A4 activity raises DOCK10's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 3.17× lower at baseline in the lines without SLC4A4 | 0.056 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[TEX41]] | C | TEX41 activity raises DOCK10's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 5.81× lower at baseline in the lines without TEX41 | 0.075 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[NRG1]] | C | NRG1 activity raises DOCK10's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 6.60× lower at baseline in the lines without NRG1 | 0.088 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 6, C 10. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCED1B]] | B | DOCK10 activity raises PCED1B's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without DOCK10 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| [[ARHGAP31]] | B | DOCK10 activity raises ARHGAP31's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 2.96× lower at baseline in the lines without DOCK10 | 0.077 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| cells under [[Carbamazepine (drug)]] 0.5 µM | B | DOCK10 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express DOCK10 (24) vs lines expressing it (24) | the lines without DOCK10: 1.17× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | B | DOCK10 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express DOCK10 (24) vs lines expressing it (24) | the lines without DOCK10: 0.67× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| cells under [[Mebendazole (drug)]] 5 µM | B | DOCK10 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express DOCK10 (24) vs lines expressing it (24) | the lines without DOCK10: 0.72× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM | B | DOCK10 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.05 µM (protects the cells) | lines that do not express DOCK10 (24) vs lines expressing it (24) | the lines without DOCK10: 0.85× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| [[MSC-AS1]] | C | DOCK10 activity raises MSC-AS1's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 10.66× lower at baseline in the lines without DOCK10 | 0.011 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |
| [[NRP2]] | C | DOCK10 activity raises NRP2's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 3.56× lower at baseline in the lines without DOCK10 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |
| [[FRMD4A]] | C | DOCK10 activity raises FRMD4A's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 5.16× lower at baseline in the lines without DOCK10 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |
| [[EBF1]] | C | DOCK10 activity raises EBF1's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 5.80× lower at baseline in the lines without DOCK10 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |
| [[FRMPD4]] | C | DOCK10 activity raises FRMPD4's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 3.88× lower at baseline in the lines without DOCK10 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |
| [[LINC01828]] | C | DOCK10 activity raises LINC01828's level | lines that do not express DOCK10 (24) vs lines expressing it (26) | 2.90× lower at baseline in the lines without DOCK10 | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.6, 24.7); signed map (40.3, 27.0). **Vector** length 111, 38.6% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.1 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.3 | -17.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.2 | -4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -23.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -23.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.2 — chr2:224,765,090-225,042,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZIZ3, KIAA0694 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Armadillo like helical domain containing; DOCK family Rho GEFs; MicroRNA protein coding host genes |
| Hallmark sets | COMPLEMENT |
| Reactome | 9 pathways, smallest: RAC2 GTPase cycle; RAC3 GTPase cycle; Factors involved in megakaryocyte development and platelet production |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BY6](https://www.uniprot.org/uniprotkb/Q96BY6) (Dedicator of cytokinesis protein 10):

> Guanine nucleotide-exchange factor (GEF) that activates CDC42 and RAC1 by exchanging bound GDP for free GTP. Essential for dendritic spine morphogenesis in Purkinje cells and in hippocampal neurons, via a CDC42-mediated pathway. Sustains B-cell lymphopoiesis in secondary lymphoid tissues and regulates FCER2/CD23 expression.

**Summary**, from NCBI Gene [55619](https://www.ncbi.nlm.nih.gov/gene/55619):

> This gene encodes a member of the dedicator of cytokinesis protein family. Members of this family are guanosine nucleotide exchange factors for Rho GTPases and defined by the presence of conserved DOCK-homology regions. The encoded protein belongs to the D (or Zizimin) subfamily of DOCK proteins, which also contain an N-terminal pleckstrin homology domain. Alternatively spliced transcript variants that encode different isoforms have been described. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:23479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23479) · Entrez [55619](https://www.ncbi.nlm.nih.gov/gene/55619) · UniProt [Q96BY6](https://www.uniprot.org/uniprotkb/Q96BY6) · Ensembl [ENSG00000135905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135905)

## Data

Gene col 5773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5773); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5773]; `tensor/DDL_lfc|DDL_z.npy` [5773]; `embed/gene_vectors.npy` [5773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5773 or target_col == 5773). Every well: [[DOCK10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
