---
symbol: "PKIG"
type: "gene"
col: 9689
ensembl_id: "ENSG00000168734"
name: "cAMP-dependent protein kinase inhibitor gamma"
location: "20q13.12"
module: 17
arm: "+"
pooled_cpm: 39.93
n_lines_expressing: 44
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 9
direction_downstream: 15
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PKIG

*cAMP-dependent protein kinase inhibitor gamma* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.50× (z +9.1, q 4e-17, up in 26 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.483× (z -22.9, q 0e+00, down in 36 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBS5]] (+0.66, fdr 9e-06), [[USP30]] (+0.62, fdr 2e-05), [[EHMT2]] (+0.62, fdr 1e-05); moves opposite to [[GNG12-AS1]] (-0.61, fdr 1e-05), [[ZNF800]] (-0.60, fdr 3e-05), [[SIAH2-AS1]] (-0.60, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NFASC]] → it (grade B ⚠); 15 go from it, the strongest it → [[TTBK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +9.1 | 4e-17 | 26/42 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +6.3 | 6e-08 | 21/42 (C32, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.4 | 1e-05 | 20/42 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +5.3 | 2e-05 | 19/42 (HOP62, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.56×** | +5.1 | 4e-05 | 16/41 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 5e-05 | 12/41 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.7 | 2e-04 | 16/42 (LS 180, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.6 | 3e-04 | 16/41 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +4.4 | 7e-04 | 16/42 (H4, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 8e-04 | 10/42 (BT-474, HOP62, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +4.2 | 0.001 | 14/42 (PANC-1, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +4.2 | 0.001 | 12/42 (H4, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 15/42 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.004 | 13/42 (HepG2/C3A, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.005 | 16/42 (LS 180, BT-474, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.20×** | +3.8 | 0.005 | 10/41 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.008 | 11/42 (MIA PaCa-2, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.483×** | -22.9 | 0e+00 | 36/42 (RPMI-7951, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.454×** | -16.9 | 0e+00 | 36/42 (BT-474, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.608×** | -15.7 | 0e+00 | 31/42 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -14.9 | 0e+00 | 31/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -11.5 | 2e-28 | 33/42 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.598×** | -11.4 | 3e-28 | 30/42 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -10.8 | 3e-25 | 34/42 (C-33 A, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.621×** | -10.6 | 2e-24 | 30/42 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.715×** | -10.6 | 3e-24 | 26/42 (BT-474, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -9.9 | 3e-21 | 30/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.673×** | -8.8 | 6e-17 | 27/42 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.708×** | -7.4 | 8e-12 | 19/35 (SK-MEL-2, C-33 A, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.727×** | -6.8 | 4e-10 | 22/41 (NCI-H460, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.764×** | -6.0 | 8e-08 | 22/42 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.804×** | -4.8 | 5e-05 | 19/42 (SW480, J82, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.699×** | -4.1 | 0.001 | 16/42 (RPMI-7951, A-172, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.002 | 16/42 (SHP-77, A549, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.859× | -3.2 | 0.031 | 13/42 (NCI-H460, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.0 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -19.9) |
| [[NCI-H1792 (line)]] | alt | 51.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 160 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -20.4) |
| [[BT-474 (line)]] | alt | 73.0 | 0 | 4 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.323× (z -13.3) |
| [[J82 (line)]] | alt | 47.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 54.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.9) |
| [[SW480 (line)]] | alt | 40.7 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -12.0) |
| [[A-427 (line)]] | wt | 60.4 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.460× (z -12.4) |
| [[C-33 A (line)]] | alt | 65.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.3) |
| [[C32 (line)]] | wt | 66.9 | 1 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.73× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.4) |
| [[HOP62 (line)]] | alt | 25.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 67.3 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 68.2 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 60.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.7) |
| [[SNU-423 (line)]] | alt | 88.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -13.7) |
| [[A-172 (line)]] | wt | 76.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 46.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -16.0) |
| [[HS-578T (line)]] | alt | 58.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 55.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -12.9) |
| [[SNU-1 (line)]] | wt | 45.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.2) |
| [[SW1417 (line)]] | alt | 57.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -11.3) |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.6) |
| [[H4 (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 61.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.3) |
| [[NCI-H661 (line)]] | alt | 64.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0637× (z -10.8) |
| [[PANC-1 (line)]] | alt | 54.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -12.0) |
| [[SW 1271 (line)]] | alt | 47.4 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0586× (z -9.6) |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -9.9) |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS5]] | +0.66 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[USP30]] | +0.62 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[EHMT2]] | +0.62 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[FAM229B]] | +0.61 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ESD]] | +0.61 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[LMBRD1]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ARNT]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[STX7]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[IRAK1BP1]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[OSBPL9]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.59 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[SKIC3]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12-AS1]] | -0.61 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ZNF800]] | -0.60 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[SIAH2-AS1]] | -0.60 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[AGO2]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MPDU1]] | -0.57 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.57 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ALG13]] | -0.57 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SECISBP2]] | -0.56 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[DGKH]] | -0.54 | -0.60 / -0.30 | both halves | 2e-04 |  |
| [[PHC2-AS1]] | -0.54 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[AOC2]] | -0.54 | -0.53 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFASC]] | B | NFASC activity raises PKIG's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without NFASC | 0.008 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[GXYLT2]] | B | GXYLT2 activity raises PKIG's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.64× lower at baseline in the lines without GXYLT2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[TOP2A]] | B | TOP2A activity raises PKIG's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF420]] | B | ZNF420 activity raises PKIG's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 3.98× lower at baseline in the lines without ZNF420 | 0.059 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[DYNC2H1]] | B | DYNC2H1 activity raises PKIG's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 3.04× lower at baseline in the lines without DYNC2H1 | 0.092 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[ZNF540]] | C | ZNF540 activity raises PKIG's level | lines that do not express ZNF540 (5) vs lines expressing it (45) | 6.55× lower at baseline in the lines without ZNF540 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZFP14, ZNF573; maybe low, not absent; co-absent with the target |
| [[LRP12]] | C | LRP12 activity raises PKIG's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 3.46× lower at baseline in the lines without LRP12 | 0.040 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1; co-absent with the target |
| [[DNAAF4]] | C | DNAAF4 activity raises PKIG's level | lines that do not express DNAAF4 (3) vs lines expressing it (47) | 7.55× lower at baseline in the lines without DNAAF4 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; co-absent with the target; its own permutation p |
| [[TBC1D19]] | C | TBC1D19 activity raises PKIG's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 3.83× lower at baseline in the lines without TBC1D19 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTBK2]] | B | PKIG activity raises TTBK2's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without PKIG | 0.011 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[GXYLT2]] | B | PKIG activity raises GXYLT2's level | lines that do not express PKIG (6) vs lines expressing it (44) | 4.55× lower at baseline in the lines without PKIG | 0.039 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[LYPLAL1]] | B | PKIG activity raises LYPLAL1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without PKIG | 0.039 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[IRAK1BP1]] | B | PKIG activity raises IRAK1BP1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.42× lower at baseline in the lines without PKIG | 0.044 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[CRYZL1]] | B | PKIG activity raises CRYZL1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without PKIG | 0.046 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[IGF2BP3]] | B | PKIG activity raises IGF2BP3's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without PKIG | 0.054 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[TTLL7]] | B | PKIG activity raises TTLL7's level | lines that do not express PKIG (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without PKIG | 0.063 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[CISD1]] | B | PKIG activity raises CISD1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without PKIG | 0.063 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[TBC1D19]] | B | PKIG activity raises TBC1D19's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.80× lower at baseline in the lines without PKIG | 0.069 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[LINC00880]] | B | PKIG activity lowers LINC00880's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.91× higher at baseline in the lines without PKIG | 0.082 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[FAM229B]] | B | PKIG activity raises FAM229B's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without PKIG | 0.088 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[PLEKHA6]] | B | PKIG activity lowers PLEKHA6's level | lines that do not express PKIG (6) vs lines expressing it (44) | 4.23× higher at baseline in the lines without PKIG | 0.091 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-0.8, -9.1); signed map (-29.1, -9.3). **Vector** length 104, 24.8% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +5.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -16.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -22.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -10.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cAMP-dependent protein kinase inhibitor gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,531,785-44,624,247 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2B9](https://www.uniprot.org/uniprotkb/Q9Y2B9) (cAMP-dependent protein kinase inhibitor gamma):

> Extremely potent competitive inhibitor of cAMP-dependent protein kinase activity, this protein interacts with the catalytic subunit of the enzyme after the cAMP-induced dissociation of its regulatory chains.

**Summary**, from NCBI Gene [11142](https://www.ncbi.nlm.nih.gov/gene/11142):

> This gene encodes a member of the protein kinase inhibitor family. Studies of a similar protein in mice suggest that this protein acts as a potent competitive cAMP-dependent protein kinase inhibitor, and is a predominant form of inhibitor in various tissues. The encoded protein may be involved in osteogenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:9019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9019) · Entrez [11142](https://www.ncbi.nlm.nih.gov/gene/11142) · UniProt [Q9Y2B9](https://www.uniprot.org/uniprotkb/Q9Y2B9) · Ensembl [ENSG00000168734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168734)

## Data

Gene col 9689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9689); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9689]; `tensor/DDL_lfc|DDL_z.npy` [9689]; `embed/gene_vectors.npy` [9689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9689 or target_col == 9689). Every well: [[PKIG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKIG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
