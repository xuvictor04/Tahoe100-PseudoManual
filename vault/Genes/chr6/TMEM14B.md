---
symbol: "TMEM14B"
type: "gene"
col: 5987
ensembl_id: "ENSG00000137210"
name: "transmembrane protein 14B"
location: "6p24.2"
module: 105
arm: "+"
pooled_cpm: 116.63
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# TMEM14B

*transmembrane protein 14B* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.48× (z +8.6, q 7e-15, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.476× (z -15.4, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYCP2L]] (+0.67, fdr 7e-06, ⚠ same locus), [[CLEC4A]] (+0.65, fdr 7e-06), [[EFCAB3P1]] (+0.65, fdr 1e-05), [[RNMT]] (+0.63, fdr 1e-05); moves opposite to [[ZBTB45]] (-0.60, fdr 1e-05), [[ZNF747]] (-0.53, fdr 4e-05), [[TRIP12]] (-0.52, fdr 7e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SYCP2L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +8.6 | 7e-15 | 35/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.5 | 2e-08 | 28/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +6.5 | 2e-08 | 35/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.7 | 1e-06 | 28/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +5.7 | 1e-06 | 32/48 (A-172, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.7 | 2e-04 | 28/48 (A-172, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.002 | 24/48 (LS 180, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.15× | +4.0 | 0.004 | 11/48 (PANC-1, HCT15, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.010 | 21/48 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.16× | +3.2 | 0.066 | 18/49 (HOP62, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.476×** | -15.4 | 0e+00 | 44/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -11.6 | 8e-29 | 44/48 (RPMI-7951, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -10.1 | 7e-22 | 36/48 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.409×** | -10.1 | 7e-22 | 44/49 (MIA PaCa-2, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.708×** | -10.0 | 2e-21 | 32/48 (C32, A498, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -9.0 | 2e-17 | 38/48 (C32, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.682×** | -8.3 | 1e-14 | 31/49 (LS 180, HCT15, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.709×** | -7.1 | 7e-11 | 27/44 (SNU-1, C-33 A, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.712×** | -7.1 | 1e-10 | 34/47 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.698×** | -6.8 | 6e-10 | 35/48 (HOP62, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.727×** | -6.4 | 1e-08 | 28/45 (SW48, C32, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -5.6 | 8e-07 | 30/48 (C32, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.770×** | -5.6 | 8e-07 | 28/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.773×** | -5.5 | 1e-06 | 28/48 (SW480, LS 180, …) | inconsistent across doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -5.5 | 1e-06 | 2/50 (NCI-H661, SW 1088) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.795×** | -4.7 | 1e-04 | 27/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.8 | 0.004 | 22/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.020 | 13/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 201 | 0 | 16 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.178× (z -20.3) |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -15.3) |
| [[H4 (line)]] | wt | 123 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.242× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 152 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.342× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.410× (z -13.0) |
| [[SW480 (line)]] | alt | 97.7 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.73× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.409× (z -13.8) |
| [[LS 180 (line)]] | wt | 140 | 1 (1 ⚠) | 3 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.262× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.353× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0748× (z -14.1) |
| [[SNU-1 (line)]] | wt | 235 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0711× (z -27.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.108× (z -12.6) |
| [[C-33 A (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -27.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.393× (z -10.1) |
| [[HCT15 (line)]] | alt | 278 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.452× (z -8.5) |
| [[HOP62 (line)]] | alt | 148 | 1 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.04× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.480× (z -8.8) |
| [[J82 (line)]] | alt | 190 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.517× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.541× (z -8.8) |
| [[LoVo (line)]] | wt | 112 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.21× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.422× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[PANC-1 (line)]] | alt | 156 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.79× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.424× (z -13.9) |
| [[SNU-423 (line)]] | alt | 193 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.356× (z -12.1) |
| [[SW1417 (line)]] | alt | 80.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.425× (z -9.3) |
| [[A498 (line)]] | wt | 76.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -16.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.332× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -13.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.470× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.282× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.447× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 198 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.01× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.474× (z -8.7) |
| [[SHP-77 (line)]] | alt | 75.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.8) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.35× (z +8.6) | — |
| [[SW48 (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 97.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.41× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.307× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 96.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.381× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 89.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 57.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.478× (z -8.6) |
| [[RKO (line)]] | wt | 106 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.191× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 79.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCP2L]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 | ⚠ same locus (34.1 kb, same strand: neighbours can correlate without regulation) |
| [[CLEC4A]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[EFCAB3P1]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[RNMT]] | +0.63 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PRKRIP1]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[FUT11]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TMEM161B-DT]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[LINC02649]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SLC2A1-DT]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GRK3]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[C4orf47]] | +0.57 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SEC31B]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB45]] | -0.60 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF747]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[TRIP12]] | -0.52 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[FIZ1]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[RBM15B]] | -0.51 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[RUSC1-AS1]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[PPP2CA]] | -0.50 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[MOCS3]] | -0.50 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[HPS6]] | -0.48 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[ZNF613]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TMEM62]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[C7orf25]] | -0.48 | -0.39 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2L]] | B | SYCP2L activity raises TMEM14B's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without SYCP2L | 0.012 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TMEM14B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TMEM14B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RBPMS]] | B | RBPMS activity lowers TMEM14B's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.38× higher at baseline in the lines without RBPMS | 0.096 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, -18.9); signed map (-34.0, 26.4). **Vector** length 121, 38.6% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.6 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.3 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.2 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +4.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -8.2 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -8.2 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -7.0 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -6.5 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.0 | -10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -9.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.5 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 14B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:10,747,759-10,852,753 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC1223 |
| Gene groups (HGNC) | Transmembrane protein 14 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUH8](https://www.uniprot.org/uniprotkb/Q9NUH8) (Transmembrane protein 14B):

> Primate-specific protein involved in cortical expansion and folding in the developing neocortex. May drive neural progenitor proliferation through nuclear translocation of IQGAP1, which in turn promotes G1/S cell cycle transitions.

**Summary**, from NCBI Gene [81853](https://www.ncbi.nlm.nih.gov/gene/81853):

> Enables identical protein binding activity. Involved in cerebral cortex development; neural precursor cell proliferation; and regulation of G1/S transition of mitotic cell cycle. Predicted to be located in membrane. Predicted to be active in mitochondrial membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21384) · Entrez [81853](https://www.ncbi.nlm.nih.gov/gene/81853) · UniProt [Q9NUH8](https://www.uniprot.org/uniprotkb/Q9NUH8) · Ensembl [ENSG00000137210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137210)

## Data

Gene col 5987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5987); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5987]; `tensor/DDL_lfc|DDL_z.npy` [5987]; `embed/gene_vectors.npy` [5987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5987 or target_col == 5987). Every well: [[TMEM14B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM14B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
