---
symbol: "SLC16A2"
type: "gene"
col: 7146
ensembl_id: "ENSG00000147100"
name: "solute carrier family 16 member 2"
location: "Xq13.2"
module: 66
arm: "+"
pooled_cpm: 20.91
n_lines_expressing: 36
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# SLC16A2

*solute carrier family 16 member 2* — Xq13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +7.9, q 2e-12, up in 17 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.550× (z -12.0, q 2e-30, down in 22 of 34 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.479× (z -10.5, q 4e-23, down in 23 of 34 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSTL1]] (+0.58, fdr 3e-05), [[EDIL3-DT]] (+0.57, fdr 3e-05), [[CTSC]] (+0.51, fdr 4e-05); moves opposite to [[MKNK2]] (-0.45, fdr 1e-04), [[POLR2I]] (-0.44, fdr 2e-04), [[HAUS3]] (-0.43, fdr 4e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); 5 go from it, the strongest it → [[FRMD6-AS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.9 | 2e-12 | 17/33 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.018 | 10/34 (A-172, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.018 | 13/33 (HOP62, MIA PaCa-2, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.030 | 9/34 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.030 | 11/34 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.050 | 10/34 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.050 | 12/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.050 | 11/32 (HOP62, A-172, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.084 | 6/34 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.25× | +3.1 | 0.12 | 8/34 (hTERT-HPNE, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Finasteride (drug)]] 5 µM |  | 1.25× | +3.0 | 0.13 | 6/34 (HOP62, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.550×** | -12.0 | 2e-30 | 22/34 (NCI-H2030, RKO, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.479×** | -10.5 | 4e-23 | 23/34 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -10.2 | 3e-22 | 26/34 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.487×** | -9.8 | 1e-20 | 22/34 (RKO, NCI-H2030, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.504×** | -9.8 | 2e-20 | 23/34 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.550×** | -8.5 | 2e-15 | 24/34 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.592×** | -7.1 | 1e-10 | 22/34 (NCI-H23, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -6.4 | 8e-09 | 18/31 (NCI-H23, BT-474, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.684×** | -5.4 | 4e-06 | 14/33 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.691×** | -5.2 | 9e-06 | 15/34 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.717×** | -4.7 | 1e-04 | 15/34 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **0.720×** | -4.7 | 1e-04 | 16/31 (SW480, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.731×** | -4.5 | 4e-04 | 15/34 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.741×** | -4.3 | 8e-04 | 13/34 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -4.3 | 8e-04 | 14/34 (PANC-1, C32, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.765×** | -3.7 | 0.008 | 15/34 (NCI-H1573, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.780×** | -3.5 | 0.013 | 13/34 (PANC-1, BT-474, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.030 | 13/34 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.795×** | -3.3 | 0.030 | 12/34 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.797×** | -3.1 | 0.052 | 6/34 (C-33 A, SW 1271, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.806×** | -3.1 | 0.054 | 10/34 (J82, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 43.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.190× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 10.7 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.318× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 29.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 16.7× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.195× (z -9.8) |
| [[PANC-1 (line)]] | alt | 46.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.355× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 59.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -19.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 24.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 100 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.12× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[C32 (line)]] | wt | 12.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -9.3) |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A498 (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 17.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0965× (z -10.2) |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0590× (z -13.1) |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.217× (z -9.1) |
| [[A-427 (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSTL1]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[EDIL3-DT]] | +0.57 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[CTSC]] | +0.51 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[BHLHE40-AS1]] | +0.50 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[MOXD1]] | +0.49 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[LAMC1]] | +0.49 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[BMAL2]] | +0.49 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[DSE]] | +0.49 | +0.43 / +0.40 | both halves | 4e-05 |  |
| [[EDIL3]] | +0.48 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TNFRSF11B]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[OLR1]] | +0.47 | +0.40 / +0.30 | both halves | 2e-04 |  |
| [[GLIPR1]] | +0.47 | +0.47 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK2]] | -0.45 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[POLR2I]] | -0.44 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[HAUS3]] | -0.43 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[HERPUD1]] | -0.43 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[MPHOSPH10]] | -0.42 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[DDX19B]] | -0.42 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[SH3TC1]] | -0.41 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[PMM1]] | -0.41 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[CALCOCO2]] | -0.41 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[ID1]] | -0.40 | -0.19 / -0.39 | ⚠ not reproduced | 9e-04 |  |
| [[UBE2B]] | -0.40 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[MT1X]] | -0.40 | -0.22 / -0.34 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises SLC16A2's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.91× lower at baseline in the lines without MIR1915HG | 0.028 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[MRAS]] | B | MRAS activity raises SLC16A2's level | lines that do not express MRAS (11) vs lines expressing it (39) | 3.64× lower at baseline in the lines without MRAS | 0.049 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[RSPO3]] | B | RSPO3 activity raises SLC16A2's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 2.76× lower at baseline in the lines without RSPO3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[GJA1]] | B | GJA1 activity raises SLC16A2's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without GJA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[P3H2]] | B | P3H2 activity raises SLC16A2's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without P3H2 | 0.066 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1 |
| [[BNC2]] | B | BNC2 activity raises SLC16A2's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.80× lower at baseline in the lines without BNC2 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[KLHL5]] | C | KLHL5 activity raises SLC16A2's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 6.14× lower at baseline in the lines without KLHL5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6-AS2]] | B | SLC16A2 activity raises FRMD6-AS2's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without SLC16A2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |
| [[MT2A]] | B | SLC16A2 activity raises MT2A's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 2.46× lower at baseline in the lines without SLC16A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |
| [[LAMC1]] | B | SLC16A2 activity raises LAMC1's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without SLC16A2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |
| [[HAUS3]] | B | SLC16A2 activity raises HAUS3's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 1.14× lower at baseline in the lines without SLC16A2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405 |
| [[KLHL5]] | C | SLC16A2 activity raises KLHL5's level | lines that do not express SLC16A2 (14) vs lines expressing it (36) | 3.20× lower at baseline in the lines without SLC16A2 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC2A3, LOXL2, ENSG00000234405; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.8, 22.3); signed map (41.2, 18.1). **Vector** length 82.1, 18.2% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -8.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.4 | -3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.2 — chrX:74,421,493-74,533,917 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XPCT, MCT8, MCT7, DXS128E; previously DXS128, AHDS, MRX22 |
| Gene groups (HGNC) | Solute carrier family 16 |
| Reactome | 4 pathways, smallest: Organic anion transport by SLCO transporters; SLC-mediated transport of organic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P36021](https://www.uniprot.org/uniprotkb/P36021) (Monocarboxylate transporter 8):

> Specific thyroid hormone transmembrane transporter, that mediates both uptake and efflux of thyroid hormones across the cell membrane independently of pH or a Na(+) gradient. Major substrates are the iodothyronines T3 and T4 and to a lesser extent rT3 and 3,3-diiodothyronine (3,3'-T2). Acts as an important mediator of thyroid hormone transport, especially T3, through the blood-brain barrier (Probable). Mediates the efflux of 3,5-diiodo-L-tyrosine (DIT) and 3-iodo-L-tyrosine (MIT).

**Summary**, from NCBI Gene [6567](https://www.ncbi.nlm.nih.gov/gene/6567):

> This gene encodes an integral membrane protein that functions as a transporter of thyroid hormone. The encoded protein facilitates the cellular importation of thyroxine (T4), triiodothyronine (T3), reverse triiodothyronine (rT3) and diidothyronine (T2). This gene is expressed in many tissues and likely plays an important role in the development of the central nervous system. Loss of function mutations in this gene are associated with psychomotor retardation in males while females exhibit no …

**Accessions** — [HGNC:10923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10923) · Entrez [6567](https://www.ncbi.nlm.nih.gov/gene/6567) · UniProt [P36021](https://www.uniprot.org/uniprotkb/P36021) · Ensembl [ENSG00000147100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147100)

## Data

Gene col 7146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7146); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7146]; `tensor/DDL_lfc|DDL_z.npy` [7146]; `embed/gene_vectors.npy` [7146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7146 or target_col == 7146). Every well: [[SLC16A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
