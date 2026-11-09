---
symbol: "LRRC8A"
type: "gene"
col: 5903
ensembl_id: "ENSG00000136802"
name: "leucine rich repeat containing 8 VRAC subunit A"
location: "9q34.11"
module: 160
arm: "+"
pooled_cpm: 48.06
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 25
n_dd_up_clean: 13
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# LRRC8A

*leucine rich repeat containing 8 VRAC subunit A* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +18.1, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.637× (z -7.6, q 2e-11, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK2]] (+0.68, fdr 7e-06), [[KCTD5]] (+0.67, fdr 1e-05), [[SENP5]] (+0.67, fdr 7e-06); moves opposite to [[ZNF280D]] (-0.64, fdr 7e-06), [[CHIC1]] (-0.63, fdr 1e-05), [[VPS13C]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[WFDC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +18.1 | 0e+00 | 36/48 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +10.4 | 1e-22 | 41/48 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.3 | 6e-11 | 36/48 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.38×** | +5.7 | 2e-06 | 29/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 3e-06 | 24/48 (HEC-1-A, SW48, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.73×** | +5.0 | 6e-05 | 24/48 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 0.001 | 23/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.3 | 0.001 | 20/49 (HT-29, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.002 | 20/47 (HT-29, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +4.1 | 0.003 | 19/48 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.003 | 17/45 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.003 | 21/48 (HEC-1-A, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.009 | 17/47 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.015 | 19/49 (BT-474, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +3.5 | 0.015 | 19/48 (LoVo, RKO, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.053 | 17/48 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.056 | 10/49 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.063 | 9/48 (Panc 03.27, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.637×** | -7.6 | 2e-11 | 32/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.656×** | -7.1 | 4e-10 | 26/48 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.759×** | -6.8 | 2e-09 | 29/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.683×** | -6.7 | 4e-09 | 32/48 (KATO III, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.706×** | -6.1 | 1e-07 | 35/48 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -6.0 | 1e-07 | 29/48 (NCI-H2347, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.689×** | -6.0 | 1e-07 | 28/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.710×** | -5.8 | 6e-07 | 29/48 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.731×** | -5.5 | 3e-06 | 28/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.782×** | -5.3 | 8e-06 | 23/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.733×** | -5.2 | 9e-06 | 26/47 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.736×** | -5.2 | 9e-06 | 28/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.744×** | -5.2 | 1e-05 | 24/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.820×** | -4.9 | 4e-05 | 24/48 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.769×** | -4.8 | 7e-05 | 23/49 (SW480, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.830×** | -4.6 | 2e-04 | 25/48 (SW480, HCT15, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 76.0 | 0 | 12 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.341× (z -10.6) |
| [[A-427 (line)]] | wt | 25.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.300× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.214× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 68.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.76× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +20.2) | — |
| [[Hs 766T (line)]] | wt | 140 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -21.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -12.5) |
| [[J82 (line)]] | alt | 69.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.4) | [[Belumosudil (drug)]] 5 µM 0.430× (z -9.1) |
| [[KATO III (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.344× (z -9.2) |
| [[LoVo (line)]] | wt | 31.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 35.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.382× (z -12.4) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H460 (line)]] | wt | 29.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +18.1) | — |
| [[SW1417 (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -8.7) |
| [[A549 (line)]] | wt | 41.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 48.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 37.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.8) | — |
| [[C32 (line)]] | wt | 41.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -9.6) ⚠ cell-cycle shift, explains ~96% of this change |
| [[Panc 03.27 (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.8) | — |
| [[RKO (line)]] | wt | 51.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +16.6) | — |
| [[SK-MEL-2 (line)]] | alt | 38.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[SW 1271 (line)]] | alt | 61.3 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0731× (z -8.8) |
| [[SW48 (line)]] | wt | 44.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.4) | — |
| [[A498 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK2]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[KCTD5]] | +0.67 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SENP5]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[RCOR1]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[PLEKHM1P1]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[CYTH1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PPARD]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[CAP1]] | +0.63 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[EHBP1L1]] | +0.63 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ATG101]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF280D]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[CHIC1]] | -0.63 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[VPS13C]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MTARC2]] | -0.59 | -0.60 / -0.58 | both halves | 8e-06 |  |
| [[NHLRC2]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[SREK1]] | -0.58 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[LSM14A]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[RBM26]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[KPNA5]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[CXCL2]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MTPAP]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC3]] | B | WFDC3 activity raises LRRC8A's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.35× lower at baseline in the lines without WFDC3 | 0.034 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[GJB3]] | B | GJB3 activity raises LRRC8A's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without GJB3 | 0.052 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[TGFA]] | B | TGFA activity raises LRRC8A's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.42× lower at baseline in the lines without TGFA | 0.068 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[FAM83A]] | B | FAM83A activity raises LRRC8A's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 1.50× lower at baseline in the lines without FAM83A | 0.071 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[PLEK2]] | B | PLEK2 activity raises LRRC8A's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.33× lower at baseline in the lines without PLEK2 | 0.079 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[MAP2K1]] | B | MAP2K1 activity raises LRRC8A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[MEIS3]] | B | MEIS3 activity lowers LRRC8A's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 1.50× higher at baseline in the lines without MEIS3 | 0.084 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (17.3, -7.3); signed map (-12.9, 39.4). **Vector** length 128, 37.0% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.8 | +18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.6 | +10.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.5 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +5.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.3 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.0 | -6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 8 VRAC subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,882,133-128,918,039 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1437, FLJ10337, SWELL1; previously LRRC8 |
| Gene groups (HGNC) | Volume regulated anion channel subunits |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWT6](https://www.uniprot.org/uniprotkb/Q8IWT6) (Volume-regulated anion channel subunit LRRC8A):

> Essential component of the volume-regulated anion channel (VRAC, also named VSOAC channel), an anion channel required to maintain a constant cell volume in response to extracellular or intracellular osmotic changes. The VRAC channel conducts iodide better than chloride and can also conduct organic osmolytes like taurine. Mediates efflux of amino acids, such as aspartate and glutamate, in response to osmotic stress. LRRC8A and LRRC8D are required for the uptake of the drug cisplatin. In complex …

**Summary**, from NCBI Gene [56262](https://www.ncbi.nlm.nih.gov/gene/56262):

> This gene encodes a protein belonging to the leucine-rich repeat family of proteins, which are involved in diverse biological processes, including cell adhesion, cellular trafficking, and hormone-receptor interactions. This family member is a putative four-pass transmembrane protein that plays a role in B cell development. Defects in this gene cause autosomal dominant non-Bruton type agammaglobulinemia, an immunodeficiency disease resulting from defects in B cell maturation. Multiple …

**Accessions** — [HGNC:19027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19027) · Entrez [56262](https://www.ncbi.nlm.nih.gov/gene/56262) · UniProt [Q8IWT6](https://www.uniprot.org/uniprotkb/Q8IWT6) · Ensembl [ENSG00000136802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136802)

## Data

Gene col 5903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5903); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5903]; `tensor/DDL_lfc|DDL_z.npy` [5903]; `embed/gene_vectors.npy` [5903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5903 or target_col == 5903). Every well: [[LRRC8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
