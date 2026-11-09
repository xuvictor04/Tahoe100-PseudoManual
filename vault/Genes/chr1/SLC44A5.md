---
symbol: "SLC44A5"
type: "gene"
col: 6103
ensembl_id: "ENSG00000137968"
name: "solute carrier family 44 member 5"
location: "1p31.1"
module: 27
arm: "+"
pooled_cpm: 23.57
n_lines_expressing: 33
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 4
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SLC44A5

*solute carrier family 44 member 5* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +8.5, q 1e-14, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.582× (z -7.4, q 5e-11, down in 21 of 31 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.694× (z -5.0, q 5e-05, down in 18 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TACR3-AS1]] (+0.66, fdr 2e-05), [[BBOX1-AS1]] (+0.62, fdr 1e-05), [[LINC00649]] (+0.62, fdr 4e-05); moves opposite to [[SH2B2]] (-0.52, fdr 5e-05), [[TBC1D16]] (-0.51, fdr 2e-04), [[FBH1]] (-0.49, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LOXL4]] → it (grade B ⚠); 4 go from it, the strongest it → [[BBOX1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +8.5 | 1e-14 | 17/31 (HEC-1-A, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +7.8 | 2e-12 | 17/30 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.33×** | +5.4 | 1e-05 | 13/31 (A-172, KATO III, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.1 | 5e-05 | 14/31 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +5.0 | 6e-05 | 16/31 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 6e-05 | 12/31 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.001 | 12/30 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +3.9 | 0.006 | 10/31 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.9 | 0.007 | 3/27 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.70×** | +3.8 | 0.008 | 6/30 (A-172, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.7 | 0.010 | 5/23 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.7 | 0.011 | 6/23 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.011 | 7/31 (KATO III, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.036 | 5/31 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.036 | 9/31 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.036 | 11/31 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.039 | 5/30 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.039 | 11/30 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.039 | 5/31 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.049 | 10/30 (MIA PaCa-2, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.582×** | -7.4 | 5e-11 | 21/31 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.582×** | -7.4 | 5e-11 | 21/31 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.598×** | -7.0 | 5e-10 | 20/31 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.602×** | -6.9 | 7e-10 | 17/30 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.636×** | -6.2 | 7e-08 | 19/31 (SW480, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.645×** | -6.0 | 2e-07 | 19/31 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -5.0 | 5e-05 | 18/30 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.703×** | -4.8 | 1e-04 | 16/30 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.514×** | -4.7 | 1e-04 | 14/30 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.719×** | -4.5 | 4e-04 | 14/30 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.667×** | -3.9 | 0.004 | 9/31 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.769×** | -3.6 | 0.016 | 10/31 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.611×** | -3.5 | 0.019 | 14/30 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.791×** | -3.2 | 0.054 | 11/31 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.794×** | -3.2 | 0.060 | 9/30 (SW480, BT-474, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 163 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -22.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 0.336× (z -9.1) |
| [[SW480 (line)]] | alt | 34.7 | 0 | 9 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.132× (z -14.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 72.9 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0807× (z -19.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.278× (z -9.9) |
| [[Hs 766T (line)]] | wt | 92.6 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -15.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.222× (z -10.5) |
| [[A-172 (line)]] | wt | 72.5 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -15.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LS 180 (line)]] | wt | 48.6 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0581× (z -22.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.196× (z -13.0) |
| [[LoVo (line)]] | wt | 21.6 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0589× (z -18.5) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.213× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 1 (1 ⚠) | 3 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +8.9) ⚠ position not correctable | [[Ixazomib citrate (drug)]] 5 µM 0.122× (z -11.6) ⚠ cell-cycle shift, explains ~6% of this change |
| [[SHP-77 (line)]] | alt | 87.8 | 2 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.76× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HT-29 (line)]] | alt | 25.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -10.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0754× (z -10.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 35.7 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.226× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~72% of this change |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0666× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 14.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.21× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0546× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 74.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.96 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0581× (z -9.8) |
| [[KATO III (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.115× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0459× (z -10.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.95 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACR3-AS1]] | +0.66 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[BBOX1-AS1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[LINC00649]] | +0.62 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[LINC02466]] | +0.61 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[BANK1]] | +0.60 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SPINK5]] | +0.58 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[GLDN]] | +0.58 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[CES3]] | +0.58 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[DLEU1]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[UGT1A8]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP42]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[CASC9]] | +0.57 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2B2]] | -0.52 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[TBC1D16]] | -0.51 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[FBH1]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ODF2]] | -0.49 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[AGAP1]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[STEAP3]] | -0.46 | -0.55 / -0.32 | both halves | 1e-04 |  |
| [[RSKR]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL4]] | B | LOXL4 activity raises SLC44A5's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.96× lower at baseline in the lines without LOXL4 | 0.023 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[GNGT1]] | B | GNGT1 activity raises SLC44A5's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without GNGT1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[LINC02058]] | B | LINC02058 activity raises SLC44A5's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 2.67× lower at baseline in the lines without LINC02058 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |
| [[HPGD]] | B | HPGD activity raises SLC44A5's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without HPGD | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[LINC02058]] | B | LINC02058 activity strengthens SLC44A5's drug response | lines that do not express LINC02058 (20) vs lines expressing it (11) | the lines without LINC02058 respond 0.60× as strongly (z diff +1.72); strongest at Panobinostat 0.5 µM: 0.48x vs 0.22x (z diff +5.0) | 0.058 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TSPAN8]] | B | TSPAN8 activity raises SLC44A5's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.36× lower at baseline in the lines without TSPAN8 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SLC44A5's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[C4BPB]] | B | C4BPB activity raises SLC44A5's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without C4BPB | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[HDAC6]] | B | HDAC6 activity raises SLC44A5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM184A]] | B | TMEM184A activity raises SLC44A5's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 3.10× lower at baseline in the lines without TMEM184A | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BBOX1-AS1]] | B | SLC44A5 activity raises BBOX1-AS1's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.42× lower at baseline in the lines without SLC44A5 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |
| [[GNGT1]] | B | SLC44A5 activity raises GNGT1's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without SLC44A5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |
| [[TSPAN8]] | B | SLC44A5 activity raises TSPAN8's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without SLC44A5 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |
| [[MECOM]] | B | SLC44A5 activity raises MECOM's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.35× lower at baseline in the lines without SLC44A5 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.9, 43.4); signed map (58.6, 17.5). **Vector** length 79.0, 17.6% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +5.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -6.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.2 | -7.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.0 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.7 | -7.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 44 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:75,202,129-75,611,114 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34032, CTL5 |
| Gene groups (HGNC) | Solute carrier family 44 |
| Reactome | 8 pathways, smallest: SLC-mediated bile acid transport; SLC-mediated transport of organic anions; Synthesis of PC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCS7](https://www.uniprot.org/uniprotkb/Q8NCS7) (Choline transporter-like protein 5):

> Choline/H+ antiporter.

**Summary**, from NCBI Gene [204962](https://www.ncbi.nlm.nih.gov/gene/204962):

> Enables choline transmembrane transporter activity. Involved in choline transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28524) · Entrez [204962](https://www.ncbi.nlm.nih.gov/gene/204962) · UniProt [Q8NCS7](https://www.uniprot.org/uniprotkb/Q8NCS7) · Ensembl [ENSG00000137968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137968)

## Data

Gene col 6103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6103); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6103]; `tensor/DDL_lfc|DDL_z.npy` [6103]; `embed/gene_vectors.npy` [6103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6103 or target_col == 6103). Every well: [[SLC44A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC44A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
