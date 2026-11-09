---
symbol: "SGSM1"
type: "gene"
col: 9406
ensembl_id: "ENSG00000167037"
name: "small G protein signaling modulator 1"
location: "22q11.23"
module: 115
arm: "+"
pooled_cpm: 10.84
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 27
n_dd_up_clean: 11
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 14
direction_downstream: 4
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# SGSM1

*small G protein signaling modulator 1* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.23× (z +29.7, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.433× (z -17.2, q 0e+00, down in 31 of 36 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.424× (z -12.5, q 2e-33, down in 29 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUSD4]] (+0.71, fdr 1e-05), [[LPCAT2]] (+0.70, fdr 1e-05), [[SBK1]] (+0.68, fdr 1e-05); moves opposite to [[ZNF689]] (-0.66, fdr 1e-05), [[EFCAB2]] (-0.66, fdr 3e-05), [[UBE3B]] (-0.65, fdr 1e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[EMID1]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC2A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.23×** | +29.7 | 0e+00 | 41/42 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.16×** | +23.9 | 0e+00 | 40/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.15×** | +23.9 | 0e+00 | 41/41 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.72×** | +19.1 | 0e+00 | 35/39 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.34×** | +17.6 | 0e+00 | 39/41 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.30×** | +17.4 | 0e+00 | 38/41 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.22×** | +8.9 | 4e-17 | 23/40 (A498, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.48×** | +5.7 | 8e-07 | 14/39 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 0.001 | 3/39 (PANC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.68×** | +3.9 | 0.005 | 5/36 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.9 | 0.005 | 5/29 (HS-578T, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.013 | 7/39 (A549, COLO 205, …) | two highest doses |  |
| [[Sulfisoxazole (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 7/39 (HS-578T, SW480, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 9/40 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.26×** | +3.2 | 0.048 | 6/34 (NCI-H2347, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.433×** | -17.2 | 0e+00 | 31/36 (LoVo, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.424×** | -12.5 | 2e-33 | 29/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -12.2 | 6e-32 | 29/39 (SHP-77, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -10.9 | 1e-25 | 29/37 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -9.2 | 3e-18 | 26/40 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.536×** | -9.1 | 1e-17 | 23/40 (A549, RKO, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -9.0 | 2e-17 | 25/39 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.564×** | -8.3 | 6e-15 | 23/38 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.569×** | -7.9 | 2e-13 | 22/39 (SNU-1, LoVo, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.689×** | -7.6 | 1e-12 | 24/42 (A-427, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.394×** | -7.1 | 7e-11 | 21/39 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.476×** | -5.6 | 8e-07 | 17/37 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -5.2 | 1e-05 | 20/38 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.536×** | -4.7 | 8e-05 | 10/37 (KATO III, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -4.5 | 2e-04 | 18/38 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.765×** | -3.6 | 0.011 | 7/41 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.022 | 5/38 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.808×** | -3.1 | 0.055 | 8/39 (KATO III, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 40.5 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -22.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -15.6) |
| [[SW480 (line)]] | alt | 13.7 | 5 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.92× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.0846× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.146× (z -13.7) |
| [[KATO III (line)]] | alt | 33.3 | 0 | 6 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0134× (z -13.6) |
| [[LS 180 (line)]] | wt | 6.05 | 5 | 1 | [[Tucidinostat (drug)]] 5 µM 16.4× (z +16.0) | [[Neratinib (drug)]] 0.05 µM 0.124× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 18.7 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.73× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -8.9) |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -13.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.102× (z -10.7) |
| [[A498 (line)]] | wt | 3.40 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 7.79× (z +12.2) | — |
| [[A549 (line)]] | wt | 8.87 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.08× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -10.4) |
| [[HCT15 (line)]] | alt | 53.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -13.0) |
| [[PANC-1 (line)]] | alt | 5.14 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.55× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.45 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 6.75× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 9.07 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.27× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 6.40 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.13× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.42× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 2.91 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 8.84× (z +11.1) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0906× (z -8.6) |
| [[RKO (line)]] | wt | 7.83 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.4× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -17.1) |
| [[SW1417 (line)]] | alt | 8.24 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.39× (z +13.2) | — |
| [[A-172 (line)]] | wt | 4.09 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.71× (z +8.8) | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.347× (z -9.5) |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -11.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 5.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 10.6× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 3.74 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.7× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 4.52 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.96× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 6.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.11× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0860× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 25.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0825× (z -11.0) |
| [[AN3 CA (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUSD4]] | +0.71 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[LPCAT2]] | +0.70 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SBK1]] | +0.68 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[WSCD1]] | +0.67 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[MLXIPL]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.67 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RGS9]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PRR5]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.63 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[FBXL16]] | +0.63 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TSPAN33]] | +0.63 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SH3GL3]] | +0.62 | +0.48 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF689]] | -0.66 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[EFCAB2]] | -0.66 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[UBE3B]] | -0.65 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SPRY3]] | -0.62 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZFX]] | -0.61 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[UBTF]] | -0.61 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[INO80D]] | -0.61 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[PKN2-AS1]] | -0.61 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[ARFGAP2]] | -0.60 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[RRP8]] | -0.60 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PBLD]] | -0.60 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.60 | -0.51 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMID1]] | B | EMID1 activity raises SGSM1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without EMID1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[SLAIN1]] | B | SLAIN1 activity raises SGSM1's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without SLAIN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2 |
| [[FXYD6]] | B | FXYD6 activity raises SGSM1's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without FXYD6 | 0.025 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6 |
| [[KCNK13]] | B | KCNK13 activity raises SGSM1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.62× lower at baseline in the lines without KCNK13 | 0.025 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[LMTK3]] | B | LMTK3 activity raises SGSM1's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without LMTK3 | 0.034 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[RBM11]] | B | RBM11 activity raises SGSM1's level | lines that do not express RBM11 (25) vs lines expressing it (25) | 1.62× lower at baseline in the lines without RBM11 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ANKRD20A11P, VWDE |
| [[OTUD7A]] | B | OTUD7A activity raises SGSM1's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.75× lower at baseline in the lines without OTUD7A | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[SLC4A8]] | B | SLC4A8 activity raises SGSM1's level | lines that do not express SLC4A8 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without SLC4A8 | 0.040 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SGSM1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EDA]] | B | EDA activity raises SGSM1's level | lines that do not express EDA (12) vs lines expressing it (38) | 2.19× lower at baseline in the lines without EDA | 0.043 | ⚠ within organs, on part of the lines |
| [[COL4A4]] | B | COL4A4 activity raises SGSM1's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.45× lower at baseline in the lines without COL4A4 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[ARHGAP44]] | B | ARHGAP44 activity raises SGSM1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.33× lower at baseline in the lines without ARHGAP44 | 0.062 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A3]] | B | SGSM1 activity lowers SLC2A3's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 2.69× higher at baseline in the lines without SGSM1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |
| [[KIF21B]] | B | SGSM1 activity raises KIF21B's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without SGSM1 | 0.083 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |
| [[KNDC1]] | B | SGSM1 activity raises KNDC1's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without SGSM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |
| [[BEX4]] | B | SGSM1 activity raises BEX4's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without SGSM1 | 0.094 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.4, 2.8); signed map (-21.1, 30.6). **Vector** length 105, 25.7% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.7 | +29.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.0 | +19.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +23.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +23.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.7 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +8.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.3 | -17.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.3 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | -2.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | small G protein signaling modulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:24,806,169-24,927,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1941; previously RUTBC2 |
| Gene groups (HGNC) | Small G protein signaling modulators; TBC1 domain family members; RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2NKQ1](https://www.uniprot.org/uniprotkb/Q2NKQ1) (Small G protein signaling modulator 1):

> Interacts with numerous Rab family members, functioning as Rab effector for some, and as GTPase activator for others. Promotes GTP hydrolysis by RAB34 and RAB36. Probably functions as a GTPase effector with RAB9A and RAB9B; does not stimulate GTP hydrolysis with RAB9A and RAB9B.

**Summary**, from NCBI Gene [129049](https://www.ncbi.nlm.nih.gov/gene/129049):

> Enables GTPase activator activity and small GTPase binding activity. Predicted to act upstream of or within positive regulation of transcription by RNA polymerase II. Located in cytoplasmic vesicle membrane and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29410) · Entrez [129049](https://www.ncbi.nlm.nih.gov/gene/129049) · UniProt [Q2NKQ1](https://www.uniprot.org/uniprotkb/Q2NKQ1) · Ensembl [ENSG00000167037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167037)

## Data

Gene col 9406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9406); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9406]; `tensor/DDL_lfc|DDL_z.npy` [9406]; `embed/gene_vectors.npy` [9406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9406 or target_col == 9406). Every well: [[SGSM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGSM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
