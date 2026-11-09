---
symbol: "ADAMTS1"
type: "gene"
col: 7833
ensembl_id: "ENSG00000154734"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 1"
location: "21q21.3"
module: 9
arm: "+"
pooled_cpm: 21.47
n_lines_expressing: 24
n_dd_up: 35
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 16
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ADAMTS1

*ADAM metallopeptidase with thrombospondin type 1 motif 1* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (17 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.53× (z +14.6, q 3e-45, up in 18 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.606× (z -5.8, q 3e-06, down in 9 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLIT2]] (+0.65, fdr 7e-06), [[TOX]] (+0.65, fdr 1e-05), [[MMP16]] (+0.61, fdr 1e-05); moves opposite to [[ILKAP]] (-0.48, fdr 2e-05), [[TBCCD1]] (-0.46, fdr 5e-05), [[SEC14L2]] (-0.45, fdr 6e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[C12orf50]] → it (grade B ⚠); 9 go from it, the strongest it → [[C12orf50]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.53×** | +14.6 | 3e-45 | 18/21 (HS-578T, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.08×** | +11.9 | 2e-30 | 15/22 (A498, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.14×** | +8.8 | 3e-16 | 17/21 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.07×** | +8.4 | 6e-15 | 9/21 (SK-MEL-2, HS-578T, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +8.2 | 3e-14 | 9/22 (C32, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.03×** | +8.2 | 3e-14 | 18/21 (NCI-H1573, H4, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.10×** | +8.1 | 6e-14 | 17/21 (HEC-1-A, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.99×** | +7.9 | 1e-13 | 11/21 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.95×** | +7.7 | 9e-13 | 17/21 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.97×** | +7.6 | 2e-12 | 4/17 (HS-578T, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +7.4 | 5e-12 | 18/21 (H4, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.94×** | +7.1 | 7e-11 | 12/20 (SK-MEL-2, HS-578T, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.72×** | +6.3 | 1e-08 | 15/21 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.3 | 1e-08 | 7/22 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.75×** | +6.1 | 4e-08 | 13/18 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +5.9 | 2e-07 | 14/21 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.91×** | +5.3 | 3e-06 | 11/22 (A498, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.005 | 7/21 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.013 | 11/22 (SNU-423, A498, …) | rises with dose |  |
| [[Malotilate (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.017 | 2/21 (SNU-423, HOP62) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.019 | 4/21 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.038 | 4/22 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.0 | 0.051 | 6/21 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +3.0 | 0.051 | 7/21 (A498, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.606×** | -5.8 | 3e-06 | 9/21 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.609×** | -5.7 | 3e-06 | 18/21 (LOX-IMVI, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.642×** | -5.1 | 5e-05 | 14/21 (SNU-423, LOX-IMVI, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.759×** | -4.5 | 9e-04 | 12/22 (J82, C32, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.685×** | -4.4 | 0.001 | 10/21 (LOX-IMVI, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.766×** | -4.4 | 0.001 | 11/22 (SNU-423, A498, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.695×** | -4.2 | 0.002 | 11/21 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.717×** | -3.9 | 0.008 | 10/21 (NCI-H1792, HOP62, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.703×** | -3.8 | 0.010 | 9/21 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.734×** | -3.6 | 0.020 | 11/21 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.020 | 13/21 (LOX-IMVI, SNU-423, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.725×** | -3.4 | 0.027 | 4/21 (Hs 766T, CHP-212, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.745×** | -3.4 | 0.029 | 10/21 (RPMI-7951, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.752×** | -3.3 | 0.039 | 12/21 (SNU-423, A498, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.756×** | -3.2 | 0.045 | 15/21 (Hs 766T, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 226 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0273× (z -24.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 140 | 4 (4 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 10.2× (z +12.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -8.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.206× (z -8.7) |
| [[A498 (line)]] | wt | 36.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +22.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.28× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 94.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +13.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.17× (z +8.6) | — |
| [[H4 (line)]] | wt | 46.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.44× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 9.67 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.3× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 58.4 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.16× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C32 (line)]] | wt | 40.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +13.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 10.8× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 27.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +9.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.86× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -11.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H1573 (line)]] | alt | 17.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.67× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 23.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 8.58× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 10.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.18× (z +9.5) | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HOP62 (line)]] | alt | 34.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.57× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 34.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.74× (z +13.2) | — |
| [[J82 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.46× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.89× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 34.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.22× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.1× (z +12.3) | — |
| [[A549 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLIT2]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TOX]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[MMP16]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[ROR1-AS1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[FLNC]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NGF]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TNFRSF11B]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TUSC3]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[OFCC1]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[PCDH17]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ABCC9]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[COLEC10]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILKAP]] | -0.48 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TBCCD1]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SEC14L2]] | -0.45 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[ARHGAP1]] | -0.45 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PTPRA]] | -0.44 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ARMC8]] | -0.44 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[COPS8]] | -0.44 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[DENND6A]] | -0.44 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[MT1E]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | C12orf50 activity raises ADAMTS1's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 4.64× lower at baseline in the lines without C12orf50 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers ADAMTS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[KITLG]] | B | KITLG activity raises ADAMTS1's level | lines that do not express KITLG (10) vs lines expressing it (40) | 2.79× lower at baseline in the lines without KITLG | 0.082 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |
| [[SIM1]] | C | SIM1 activity raises ADAMTS1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 5.66× lower at baseline in the lines without SIM1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[NAV3]] | C | NAV3 activity raises ADAMTS1's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 4.84× lower at baseline in the lines without NAV3 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12; co-absent with the target |
| [[SERPINB2]] | C | SERPINB2 activity raises ADAMTS1's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 3.77× lower at baseline in the lines without SERPINB2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[SOX5]] | C | SOX5 activity raises ADAMTS1's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 4.92× lower at baseline in the lines without SOX5 | 0.048 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises ADAMTS1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 4.47× lower at baseline in the lines without CDH6 | 0.048 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[CCL3]] | C | CCL3 activity raises ADAMTS1's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 4.27× lower at baseline in the lines without CCL3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[PTHLH]] | C | PTHLH activity raises ADAMTS1's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.54× lower at baseline in the lines without PTHLH | 0.063 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1; co-absent with the target |
| [[PCDH9]] | C | PCDH9 activity raises ADAMTS1's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 3.73× lower at baseline in the lines without PCDH9 | 0.066 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises ADAMTS1's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.08× lower at baseline in the lines without TRPC4 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | ADAMTS1 activity raises C12orf50's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without ADAMTS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12 |
| [[SYNE1]] | B | ADAMTS1 activity raises SYNE1's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 3.38× lower at baseline in the lines without ADAMTS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12 |
| [[ADAMTSL1]] | B | ADAMTS1 activity raises ADAMTSL1's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 2.41× lower at baseline in the lines without ADAMTS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12 |
| [[ADAMTS16]] | C | ADAMTS1 activity raises ADAMTS16's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 4.13× lower at baseline in the lines without ADAMTS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |
| [[CALCRL]] | C | ADAMTS1 activity raises CALCRL's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 2.36× lower at baseline in the lines without ADAMTS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |
| [[NAV3]] | C | ADAMTS1 activity raises NAV3's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 3.10× lower at baseline in the lines without ADAMTS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |
| [[LINC01828]] | C | ADAMTS1 activity raises LINC01828's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without ADAMTS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |
| [[TUSC3]] | C | ADAMTS1 activity raises TUSC3's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 4.71× lower at baseline in the lines without ADAMTS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |
| [[NCKAP5]] | C | ADAMTS1 activity raises NCKAP5's level | lines that do not express ADAMTS1 (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without ADAMTS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: SALL1, ENSG00000289600, ADAM12; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.7, 26.2); signed map (39.6, 29.0). **Vector** length 88.2, 28.0% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +6.2 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.8 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | -1.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -5.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:26,835,755-26,845,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C3-C5, METH1, KIAA1346 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 8 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHI8](https://www.uniprot.org/uniprotkb/Q9UHI8) (A disintegrin and metalloproteinase with thrombospondin motifs 1):

> Metalloprotease which cleaves aggrecan, a cartilage proteoglycan, at the '1938-Glu-|-Leu-1939' site (within the chondroitin sulfate attachment domain), and may be involved in its turnover (By similarity). Also cleaves COMP. Has angiogenic inhibitor activity. May play a critical role in follicular rupture (By similarity).

**Summary**, from NCBI Gene [9510](https://www.ncbi.nlm.nih.gov/gene/9510):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motif) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The protein encoded by this gene contains two disintegrin loops and …

**Accessions** — [HGNC:217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:217) · Entrez [9510](https://www.ncbi.nlm.nih.gov/gene/9510) · UniProt [Q9UHI8](https://www.uniprot.org/uniprotkb/Q9UHI8) · Ensembl [ENSG00000154734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154734)

## Data

Gene col 7833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7833); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7833]; `tensor/DDL_lfc|DDL_z.npy` [7833]; `embed/gene_vectors.npy` [7833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7833 or target_col == 7833). Every well: [[ADAMTS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
