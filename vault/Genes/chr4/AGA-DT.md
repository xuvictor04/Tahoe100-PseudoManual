---
symbol: "AGA-DT"
type: "gene"
col: 14666
ensembl_id: "ENSG00000250131"
name: "AGA divergent transcript"
location: "4q34.3"
module: 10
arm: "+"
pooled_cpm: 13.41
n_lines_expressing: 44
n_dd_up: 21
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 11
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# AGA-DT

*AGA divergent transcript* — 4q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +13.5, q 6e-39, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.445× (z -8.0, q 8e-13, down in 26 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.542× (z -6.0, q 3e-07, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF1B-AS1]] (+0.79, fdr 9e-06), [[PCNX4-DT]] (+0.73, fdr 1e-05), [[RP1]] (+0.72, fdr 2e-05); moves opposite to [[GTF2E2]] (-0.62, fdr 1e-04), [[WASF3]] (-0.61, fdr 3e-04), [[MPG]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCDHA6]] → it (grade B ⚠); 11 go from it, the strongest it → [[ZNF207]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +13.5 | 6e-39 | 29/39 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.00×** | +6.8 | 3e-09 | 29/41 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +5.8 | 1e-06 | 19/40 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.6 | 2e-06 | 19/38 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.5 | 3e-06 | 6/15 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.76×** | +5.4 | 7e-06 | 23/38 (SW480, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.3 | 8e-06 | 9/28 (LoVo, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.43×** | +5.0 | 5e-05 | 19/41 (A-427, RKO, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.65×** | +4.9 | 5e-05 | 19/41 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +4.7 | 2e-04 | 6/18 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +4.6 | 2e-04 | 22/39 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.002 | 14/42 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 10/40 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.006 | 13/40 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +3.6 | 0.011 | 13/42 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.021 | 11/41 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.021 | 13/41 (C32, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.055 | 3/39 (HEC-1-A, C32, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.070 | 8/40 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.089 | 10/42 (A498, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.445×** | -8.0 | 8e-13 | 26/36 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.460×** | -7.7 | 5e-12 | 30/41 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.542×** | -6.0 | 3e-07 | 24/41 (CFPAC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.549×** | -5.9 | 5e-07 | 28/41 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.556×** | -5.8 | 8e-07 | 25/41 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.385×** | -4.9 | 8e-05 | 19/35 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.623×** | -4.7 | 2e-04 | 18/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -4.6 | 3e-04 | 16/39 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.632×** | -4.5 | 4e-04 | 22/40 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.638×** | -4.4 | 5e-04 | 17/41 (CFPAC-1, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.642×** | -4.4 | 6e-04 | 17/41 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -4.0 | 0.003 | 16/42 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.691×** | -3.6 | 0.012 | 14/37 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **0.690×** | -3.5 | 0.017 | 17/33 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.705×** | -3.4 | 0.021 | 7/41 (NCI-H2030, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.705×** | -3.3 | 0.032 | 9/41 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.715×** | -3.3 | 0.032 | 12/41 (HEC-1-A, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 95.9 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.8) |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.204× (z -20.0) |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0376× (z -10.5) ⚠ cell-cycle shift, explains ~88% of this change |
| [[KATO III (line)]] | alt | 5.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 6.23 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0948× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 10.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.147× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 5.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0992× (z -9.0) |
| [[C32 (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +8.7) | — |
| [[H4 (line)]] | wt | 9.74 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0444× (z -9.3) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HEC-1-A (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +8.6) | — |
| [[J82 (line)]] | alt | 5.95 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0837× (z -9.3) |
| [[LoVo (line)]] | wt | 7.98 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -9.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0779× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0595× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 7.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +8.8) | — |
| [[A-172 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1B-AS1]] | +0.79 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[PCNX4-DT]] | +0.73 | +0.78 / +0.49 | both halves | 1e-05 | same gene group |
| [[RP1]] | +0.72 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | +0.70 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD31]] | +0.69 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[DPH6-DT]] | +0.67 | +0.72 / +0.41 | both halves | 4e-05 | same gene group |
| [[LINC00240]] | +0.67 | +0.76 / +0.39 | both halves | 6e-05 |  |
| [[OXA1L-DT]] | +0.67 | +0.71 / +0.38 | both halves | 6e-05 | same gene group |
| [[TMEM202-AS1]] | +0.67 | +0.76 / +0.32 | both halves | 2e-04 |  |
| [[PDCL3P4]] | +0.66 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[WARS2-AS1]] | +0.66 | +0.71 / +0.33 | both halves | 1e-04 |  |
| [[SUCLG2-DT]] | +0.66 | +0.66 / +0.38 | both halves | 6e-05 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.62 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[WASF3]] | -0.61 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[MPG]] | -0.59 | -0.67 / -0.30 | both halves | 2e-04 |  |
| [[FAM118A]] | -0.59 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[RGS10]] | -0.58 | -0.64 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHA6]] | B | PCDHA6 activity raises AGA-DT's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without PCDHA6 | 0.060 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers AGA-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF207]] | B | AGA-DT activity raises ZNF207's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.31× lower at baseline in the lines without AGA-DT | 0.020 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[HHAT]] | B | AGA-DT activity raises HHAT's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.69× lower at baseline in the lines without AGA-DT | 0.048 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[CFAP70]] | B | AGA-DT activity raises CFAP70's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without AGA-DT | 0.048 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[ZCWPW1]] | B | AGA-DT activity raises ZCWPW1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without AGA-DT | 0.054 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[FAM66C]] | B | AGA-DT activity raises FAM66C's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without AGA-DT | 0.058 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[ZMAT1]] | B | AGA-DT activity raises ZMAT1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.91× lower at baseline in the lines without AGA-DT | 0.067 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[SYT9-AS1]] | B | AGA-DT activity raises SYT9-AS1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.25× lower at baseline in the lines without AGA-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[PPP1R12A-AS2]] | B | AGA-DT activity raises PPP1R12A-AS2's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without AGA-DT | 0.075 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[RIPK2-DT]] | B | AGA-DT activity raises RIPK2-DT's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without AGA-DT | 0.077 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[SLC38A4-AS1]] | B | AGA-DT activity raises SLC38A4-AS1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without AGA-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[OCIAD1]] | B | AGA-DT activity raises OCIAD1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without AGA-DT | 0.091 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.759). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (19.0, 19.6); signed map (32.8, -10.2). **Vector** length 87.3, 19.5% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.0 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.8 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.7 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -3.1 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | AGA divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q34.3 — chr4:177,442,519-177,681,381 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27730) · Entrez [285500](https://www.ncbi.nlm.nih.gov/gene/285500) · Ensembl [ENSG00000250131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250131)

## Data

Gene col 14666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14666); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14666]; `tensor/DDL_lfc|DDL_z.npy` [14666]; `embed/gene_vectors.npy` [14666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14666 or target_col == 14666). Every well: [[AGA-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGA-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
