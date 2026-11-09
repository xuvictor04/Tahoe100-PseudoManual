---
symbol: "DOCK11"
type: "gene"
col: 7167
ensembl_id: "ENSG00000147251"
name: "dedicator of cytokinesis 11"
location: "Xq24"
module: 132
arm: "+"
pooled_cpm: 30.14
n_lines_expressing: 37
n_dd_up: 17
n_dd_down: 29
n_dd_up_clean: 11
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# DOCK11

*dedicator of cytokinesis 11* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +12.4, q 2e-32, up in 19 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.428× (z -13.9, q 6e-41, down in 29 of 35 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.570× (z -9.5, q 3e-19, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNB5]] (+0.52, fdr 3e-05), [[STX2]] (+0.50, fdr 1e-05), [[FHL1]] (+0.49, fdr 6e-05); moves opposite to [[NDUFS3]] (-0.43, fdr 2e-04), [[LINS1]] (-0.42, fdr 2e-04), [[ARMC5]] (-0.42, fdr 1e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HNF1B]] → it (grade B ⚠); 3 go from it, the strongest it → [[GPR137B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +12.4 | 2e-32 | 19/35 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +10.1 | 2e-21 | 20/35 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +7.4 | 2e-11 | 18/35 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.8 | 8e-07 | 16/35 (SNU-423, HOP62, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.003 | 12/34 (SHP-77, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 0.003 | 6/35 (SHP-77, A498, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.005 | 5/35 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.27×** | +3.9 | 0.006 | 10/35 (A549, LoVo, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.006 | 9/35 (J82, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.17× | +3.9 | 0.006 | 11/35 (J82, RKO, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.016 | 7/34 (HOP62, A498, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +3.5 | 0.026 | 5/35 (KATO III, SW480, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +3.4 | 0.031 | 4/35 (J82, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.3 | 0.031 | 7/18 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.3 | 0.031 | 6/28 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.2 | 0.041 | 8/35 (BT-474, HOP62, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.043 | 7/34 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.060 | 5/35 (C-33 A, HOP62, …) | all doses, flat |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.071 | 6/35 (J82, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.074 | 5/35 (A549, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7167.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.428×** | -13.9 | 6e-41 | 29/35 (NCI-H460, RPMI-7951, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.617×** | -11.4 | 7e-28 | 22/35 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.570×** | -9.5 | 3e-19 | 20/35 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -7.9 | 4e-13 | 22/34 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.645×** | -7.4 | 1e-11 | 20/32 (SNU-1, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -7.2 | 7e-11 | 23/35 (MIA PaCa-2, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.692×** | -6.2 | 4e-08 | 18/35 (MIA PaCa-2, NCI-H1792, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.694×** | -6.2 | 5e-08 | 17/35 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.721×** | -5.5 | 2e-06 | 16/35 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -5.4 | 3e-06 | 18/35 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.559×** | -5.2 | 1e-05 | 14/34 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.561×** | -5.1 | 1e-05 | 18/35 (RKO, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.588×** | -4.7 | 1e-04 | 14/30 (SW 900, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -4.6 | 2e-04 | 14/35 (A-172, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.689×** | -4.5 | 3e-04 | 11/34 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -4.2 | 8e-04 | 14/35 (A-172, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -4.0 | 0.002 | 12/33 (RKO, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.651×** | -3.8 | 0.004 | 9/35 (SNU-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.733×** | -3.7 | 0.004 | 11/35 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.743×** | -3.6 | 0.008 | 9/35 (NCI-H1792, SW480, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.009 | 7/35 (LoVo, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 375 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -26.9) |
| [[NCI-H460 (line)]] | wt | 83.9 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.209× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 60.8 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 83.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -11.7) |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.211× (z -8.7) |
| [[SW480 (line)]] | alt | 32.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.8) |
| [[A549 (line)]] | wt | 21.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -8.6) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -10.1) |
| [[RKO (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0841× (z -14.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -12.0) |
| [[A-172 (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -13.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A498 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.305× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[KATO III (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LoVo (line)]] | wt | 9.89 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.13× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0884× (z -9.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW 900 (line)]] | alt | 9.06 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[AsPC-1 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB5]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[STX2]] | +0.50 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[FHL1]] | +0.49 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[RCAN3]] | +0.48 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[EPS15]] | +0.48 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[MAP3K15]] | +0.46 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[ZDHHC2]] | +0.46 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[RNF130]] | +0.45 | +0.51 / +0.37 | both halves | 9e-05 |  |
| [[RADIL]] | +0.45 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[BVES]] | +0.45 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[NBPF15]] | +0.45 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[TMEM170B]] | +0.45 | +0.36 / +0.40 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS3]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[LINS1]] | -0.42 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ARMC5]] | -0.42 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[HNF1B]] | -0.41 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[MED4]] | -0.41 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[PI4KB]] | -0.41 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[NFX1]] | -0.40 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[DIABLO]] | -0.39 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[GOSR1]] | -0.39 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[FBXW9]] | -0.39 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[NSUN3]] | -0.39 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[CTNND1]] | -0.38 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1B]] | B | HNF1B activity lowers DOCK11's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.28× higher at baseline in the lines without HNF1B | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[SDK1]] | B | SDK1 activity raises DOCK11's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 2.25× lower at baseline in the lines without SDK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR137B]] | B | DOCK11 activity raises GPR137B's level | lines that do not express DOCK11 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without DOCK11 | 0.005 | ⚠ within organs, on part of the lines; also absent: KIF26A, HOXD8, ABCA17P; maybe low, not absent |
| [[HNF1B]] | B | DOCK11 activity lowers HNF1B's level | lines that do not express DOCK11 (13) vs lines expressing it (37) | 3.07× higher at baseline in the lines without DOCK11 | 0.051 | ⚠ within organs, on part of the lines; also absent: KIF26A, HOXD8, ABCA17P; maybe low, not absent |
| [[KIF26A]] | C | DOCK11 activity raises KIF26A's level | lines that do not express DOCK11 (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without DOCK11 | 0.067 | ⚠ within organs, on part of the lines; also absent: KIF26A, HOXD8, ABCA17P; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.9, 46.0); signed map (-29.3, 37.4). **Vector** length 72.0, 14.1% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.5 | +3.5 |
| fall | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | -3.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.5 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:118,495,815-118,686,163 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32122, FLJ43653, ZIZ2, ACG |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Armadillo like helical domain containing; DOCK family Rho GEFs |
| Reactome | 7 pathways, smallest: Factors involved in megakaryocyte development and platelet production; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JSL3](https://www.uniprot.org/uniprotkb/Q5JSL3) (Dedicator of cytokinesis protein 11):

> Guanine nucleotide-exchange factor (GEF) that activates CDC42 by exchanging bound GDP for free GTP. Required for marginal zone (MZ) B-cell development, is associated with early bone marrow B-cell development, MZ B-cell formation, MZ B-cell number and marginal metallophilic macrophages morphology (By similarity). Facilitates filopodia formation through the activation of CDC42.

**Summary**, from NCBI Gene [139818](https://www.ncbi.nlm.nih.gov/gene/139818):

> Predicted to enable guanyl-nucleotide exchange factor activity. Involved in positive regulation of filopodium assembly. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23483) · Entrez [139818](https://www.ncbi.nlm.nih.gov/gene/139818) · UniProt [Q5JSL3](https://www.uniprot.org/uniprotkb/Q5JSL3) · Ensembl [ENSG00000147251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147251)

## Data

Gene col 7167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7167); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7167]; `tensor/DDL_lfc|DDL_z.npy` [7167]; `embed/gene_vectors.npy` [7167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7167 or target_col == 7167). Every well: [[DOCK11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
