---
symbol: "PRKAA2"
type: "gene"
col: 8512
ensembl_id: "ENSG00000162409"
name: "protein kinase AMP-activated catalytic subunit alpha 2"
location: "1p32.2"
module: 11
arm: "+"
pooled_cpm: 73.71
n_lines_expressing: 34
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# PRKAA2

*protein kinase AMP-activated catalytic subunit alpha 2* — 1p32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.37× (z +6.5, q 4e-08, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.527× (z -13.2, q 4e-37, down in 25 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.639× (z -13.0, q 2e-36, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF182]] (+0.52, fdr 3e-05), [[ASF1A]] (+0.51, fdr 3e-05), [[PRKG2]] (+0.51, fdr 5e-05); moves opposite to [[GUCD1]] (-0.50, fdr 4e-05), [[PMPCA]] (-0.48, fdr 3e-05), [[LAPTM4A]] (-0.48, fdr 5e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF702P]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COL4A3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.5 | 4e-08 | 19/32 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +6.4 | 4e-08 | 17/33 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.0 | 3e-07 | 18/32 (LoVo, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.5 | 6e-06 | 14/32 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.022 | 10/31 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.022 | 9/32 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.077 | 8/31 (A-427, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.527×** | -13.2 | 4e-37 | 25/31 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -13.0 | 2e-36 | 26/33 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.565×** | -11.8 | 9e-30 | 25/32 (J82, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.598×** | -10.2 | 3e-22 | 25/32 (A-427, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.616×** | -10.0 | 2e-21 | 22/32 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.664×** | -8.1 | 5e-14 | 24/31 (J82, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.678×** | -8.0 | 1e-13 | 19/32 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.689×** | -7.7 | 1e-12 | 18/32 (J82, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.696×** | -7.5 | 6e-12 | 22/32 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.677×** | -7.4 | 6e-12 | 18/29 (HepG2/C3A, A549, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.693×** | -7.2 | 2e-11 | 22/34 (A-427, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -6.4 | 9e-09 | 16/32 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.735×** | -6.3 | 1e-08 | 20/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.557×** | -6.3 | 1e-08 | 20/33 (A498, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.742×** | -6.1 | 3e-08 | 19/32 (SNU-423, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.681×** | -4.1 | 0.001 | 13/32 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.826×** | -3.9 | 0.003 | 12/32 (NCI-H460, SW480, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.866× | -2.9 | 0.079 | 9/32 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[SBI-0640756 (drug)]] 5 µM |  | **0.766×** | -2.9 | 0.093 | 5/32 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | 0.870× | -2.8 | 0.098 | 5/32 (A549, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 370 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.8) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -17.2) |
| [[SW480 (line)]] | alt | 184 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -23.1) |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -18.7) |
| [[NCI-H1792 (line)]] | alt | 134 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -17.8) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -12.4) |
| [[J82 (line)]] | alt | 47.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[NCI-H23 (line)]] | alt | 104 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.9) ⚠ cell-cycle shift, explains ~78% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 80.6 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +9.9) ⚠ cell-cycle shift, explains ~41% of this change | [[Digitoxin (drug)]] 5 µM 0.410× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -12.4) |
| [[SNU-423 (line)]] | alt | 74.0 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.4) |
| [[A-427 (line)]] | wt | 101 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.6) ⚠ cell-cycle shift, explains ~78% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -13.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.464× (z -11.7) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 73.6 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +13.1) ⚠ cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 52.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -12.3) |
| [[A549 (line)]] | wt | 56.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.8) |
| [[A-172 (line)]] | wt | 49.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 51.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -10.1) ⚠ cell-cycle shift, explains ~65% of this change |
| [[AsPC-1 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.1) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[BT-474 (line)]] | alt | 53.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.5) |
| [[C-33 A (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.423× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[CFPAC-1 (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 41.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.13× (z +8.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.7) |
| [[A498 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF182]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[ASF1A]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[PRKG2]] | +0.51 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[DCTN6]] | +0.51 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[ZSCAN26]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[METTL18]] | +0.49 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[PDRG1]] | +0.49 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[NALCN]] | +0.48 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[EXOC6]] | +0.48 | +0.45 / +0.47 | both halves | 3e-05 | pathway: Organelle biogenesis and maintenance |
| [[OCIAD1]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[POLI]] | +0.48 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[PGBD1]] | +0.47 | +0.51 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUCD1]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PMPCA]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[LAPTM4A]] | -0.48 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[IMPA2]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[ZFYVE27]] | -0.46 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[MLEC]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SENP5]] | -0.43 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[SMG1P2]] | -0.43 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[SDC1]] | -0.43 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PPT2]] | -0.43 | -0.42 / -0.39 | both halves | 5e-05 | pathway: Fatty acid metabolism |
| [[MAP3K6]] | -0.42 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[AKT1]] | -0.42 | -0.43 / -0.38 | both halves | 6e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF702P]] | B | ZNF702P activity weakens PRKAA2's drug response | lines that do not express ZNF702P (17) vs lines expressing it (16) | the lines without ZNF702P respond 1.27× as strongly (z diff -1.17); strongest at Panobinostat 5 µM: 0.51x vs 0.70x (z diff -3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, VGLL3, GPA33; target measured in part of the lines; artifact flags |
| [[ZNF214]] | B | ZNF214 activity raises PRKAA2's level | lines that do not express ZNF214 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without ZNF214 | 0.089 | ⚠ within organs, on part of the lines; also absent: S100A6, CDKN1A, PRRG1; maybe low, not absent; its own permutation p |
| [[COL4A3]] | C | COL4A3 activity raises PRKAA2's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without COL4A3 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL4A3]] | C | PRKAA2 activity raises COL4A3's level | lines that do not express PRKAA2 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without PRKAA2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SGCE, GRIK4, BEX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.443). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.9, 8.0); signed map (2.1, -23.2). **Vector** length 89.2, 23.2% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.9 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.8 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +3.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.4 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.2 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.1 | -10.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.0 | -8.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase AMP-activated catalytic subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.2 — chr1:56,645,314-56,715,335 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AMPK, AMPKa2; previously PRKAA |
| Gene groups (HGNC) | Protein kinase AMP-activated catalytic subunit alpha family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 41 pathways, smallest: AMPK inhibits chREBP transcriptional activation activity; Lipophagy; Activation of PPARGC1A (PGC-1alpha) by phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P54646](https://www.uniprot.org/uniprotkb/P54646) (5'-AMP-activated protein kinase catalytic subunit alpha-2):

> Catalytic subunit of AMP-activated protein kinase (AMPK), an energy sensor protein kinase that plays a key role in regulating cellular energy metabolism. In response to reduction of intracellular ATP levels, AMPK activates energy-producing pathways and inhibits energy-consuming processes: inhibits protein, carbohydrate and lipid biosynthesis, as well as cell growth and proliferation. AMPK acts via direct phosphorylation of metabolic enzymes, and by longer-term effects via phosphorylation of …

**Summary**, from NCBI Gene [5563](https://www.ncbi.nlm.nih.gov/gene/5563):

> The protein encoded by this gene is a catalytic subunit of the AMP-activated protein kinase (AMPK). AMPK is a heterotrimer consisting of an alpha catalytic subunit, and non-catalytic beta and gamma subunits. AMPK is an important energy-sensing enzyme that monitors cellular energy status. In response to cellular metabolic stresses, AMPK is activated, and thus phosphorylates and inactivates acetyl-CoA carboxylase (ACC) and beta-hydroxy beta-methylglutaryl-CoA reductase (HMGCR), key enzymes …

**Accessions** — [HGNC:9377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9377) · Entrez [5563](https://www.ncbi.nlm.nih.gov/gene/5563) · UniProt [P54646](https://www.uniprot.org/uniprotkb/P54646) · Ensembl [ENSG00000162409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162409)

## Data

Gene col 8512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8512); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8512]; `tensor/DDL_lfc|DDL_z.npy` [8512]; `embed/gene_vectors.npy` [8512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8512 or target_col == 8512). Every well: [[PRKAA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
