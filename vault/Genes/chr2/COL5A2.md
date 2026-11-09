---
symbol: "COL5A2"
type: "gene"
col: 12839
ensembl_id: "ENSG00000204262"
name: "collagen type V alpha 2 chain"
location: "2q32.2"
module: 66
arm: "+"
pooled_cpm: 181.07
n_lines_expressing: 21
n_dd_up: 19
n_dd_down: 27
n_dd_up_clean: 15
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 25
direction_downstream: 17
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# COL5A2

*collagen type V alpha 2 chain* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.02× (z +13.3, q 1e-37, up in 5 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.63× (z +6.8, q 1e-09, up in 17 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.587× (z -9.1, q 7e-17, down in 17 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL3A1]] (+0.73, fdr 7e-06, ⚠ same locus), [[EFEMP1]] (+0.67, fdr 1e-05), [[NREP]] (+0.63, fdr 1e-05), [[TGFBI]] (+0.61, fdr 1e-05); moves opposite to [[BDH1]] (-0.54, fdr 3e-05), [[MAPK13]] (-0.50, fdr 2e-04), [[LASTR]] (-0.50, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 17 go from it, the strongest it → [[OLFML2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +13.3 | 1e-37 | 5/20 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +9.3 | 5e-18 | 6/18 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +7.5 | 9e-12 | 4/18 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.63×** | +6.8 | 1e-09 | 17/19 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.71×** | +6.5 | 7e-09 | 18/20 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.70×** | +6.2 | 7e-08 | 15/19 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 2e-06 | 15/19 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.41×** | +4.8 | 9e-05 | 17/21 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +4.5 | 4e-04 | 17/18 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.002 | 12/20 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.41×** | +3.9 | 0.006 | 10/18 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.007 | 15/20 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.020 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.026 | 0/21 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Capmatinib (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.028 | 8/19 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.047 | 11/19 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.099 | 17/19 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.59×** | +2.9 | 0.099 | 7/19 (MIA PaCa-2, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.587×** | -9.1 | 7e-17 | 17/19 (AN3 CA, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.501×** | -8.3 | 3e-14 | 19/19 (C32, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -8.2 | 5e-14 | 15/19 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.582×** | -6.5 | 1e-08 | 18/19 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.594×** | -6.3 | 4e-08 | 16/19 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.601×** | -6.1 | 9e-08 | 13/19 (H4, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.617×** | -5.8 | 5e-07 | 18/19 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.653×** | -5.1 | 2e-05 | 13/19 (J82, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.656×** | -4.9 | 7e-05 | 12/19 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.671×** | -4.8 | 9e-05 | 19/19 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -4.4 | 5e-04 | 12/19 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.712×** | -4.1 | 0.002 | 12/19 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -4.0 | 0.002 | 19/19 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.719×** | -4.0 | 0.003 | 9/18 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.735×** | -3.7 | 0.008 | 9/19 (hTERT-HPNE, C32, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.556×** | -3.7 | 0.008 | 12/19 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.738×** | -3.7 | 0.009 | 2/18 (NCI-H460, A549) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.565×** | -3.6 | 0.010 | 7/20 (NCI-H460, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.010 | 1/18 (A549) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -3.4 | 0.017 | 15/19 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.740×** | -3.2 | 0.033 | 2/19 (Hs 766T, MIA PaCa-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 314 | 13 (3 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.36× (z +21.5) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 4.93× (z +11.0) | [[Auranofin (drug)]] 5 µM 0.189× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 1,706 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.169× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 522 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -16.1) |
| [[C-33 A (line)]] | alt | 1,135 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0809× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.191× (z -12.7) |
| [[C32 (line)]] | wt | 118 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.0) |
| [[A549 (line)]] | wt | 166 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -10.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.188× (z -10.0) |
| [[Hs 766T (line)]] | wt | 89.9 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.211× (z -11.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 229 | 1 | 3 | [[Trametinib (drug)]] 5 µM 3.05× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -14.8) |
| [[AN3 CA (line)]] | alt | 283 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0618× (z -23.0) |
| [[HS-578T (line)]] | alt | 177 | 2 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.24× (z +9.1) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Selinexor (drug)]] 0.5 µM 2.91× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.7) |
| [[J82 (line)]] | alt | 200 | 1 | 2 (1 ⚠) | [[Trametinib (drug)]] 5 µM 3.18× (z +9.2) | [[Auranofin (drug)]] 5 µM 0.219× (z -12.4) |
| [[H4 (line)]] | wt | 204 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 96.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 1,845 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 78.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.6) |
| [[SNU-423 (line)]] | alt | 71.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -8.9) |
| [[SW 1088 (line)]] | alt | 322 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -8.5) |
| [[A-172 (line)]] | wt | 837 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 30.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 25.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL3A1]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ANGIOGENESIS; STRING 998; ⚠ same locus (19.2 kb: neighbours can correlate without regulation) |
| [[EFEMP1]] | +0.67 | +0.53 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[NREP]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TGFBI]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 417 |
| [[COL8A1]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 647 |
| [[DCLK2]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[OLFML2A]] | +0.59 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[COL11A1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 976 |
| [[COL1A2]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 998 |
| [[SAMD11]] | +0.57 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[COL1A1]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 995 |
| [[SULF1]] | +0.57 | +0.45 / +0.66 | both halves | 3e-05 | STRING 630 |
| [[FBN1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 924 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDH1]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MAPK13]] | -0.50 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[LASTR]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PTPRE]] | -0.45 | -0.37 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 3, C 22. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers COL5A2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[MAPK13]] | B | MAPK13 activity lowers COL5A2's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.42× higher at baseline in the lines without MAPK13 | 0.083 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[SAMD11]] | B | SAMD11 activity raises COL5A2's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 4.39× lower at baseline in the lines without SAMD11 | 0.094 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[COL3A1]] | C | COL3A1 activity raises COL5A2's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 12.02× lower at baseline in the lines without COL3A1 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises COL5A2's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 8.74× lower at baseline in the lines without COL1A2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[FBXL7]] | C | FBXL7 activity raises COL5A2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 6.49× lower at baseline in the lines without FBXL7 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[UTY]] | C | UTY activity raises COL5A2's level | lines that do not express UTY (31) vs lines expressing it (19) | 3.73× lower at baseline in the lines without UTY | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[GASK1B]] | C | GASK1B activity raises COL5A2's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 4.85× lower at baseline in the lines without GASK1B | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises COL5A2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 6.04× lower at baseline in the lines without PDGFRB | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises COL5A2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 5.23× lower at baseline in the lines without FBN1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[P3H2-AS1]] | C | P3H2-AS1 activity raises COL5A2's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 3.34× lower at baseline in the lines without P3H2-AS1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[DCLK2]] | C | DCLK2 activity raises COL5A2's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 5.57× lower at baseline in the lines without DCLK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OLFML2A]] | B | COL5A2 activity raises OLFML2A's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without COL5A2 | 0.041 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[MAPK13]] | B | COL5A2 activity lowers MAPK13's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 2.91× higher at baseline in the lines without COL5A2 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[IFT81]] | B | COL5A2 activity raises IFT81's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 1.48× lower at baseline in the lines without COL5A2 | 0.066 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[LINC01013]] | B | COL5A2 activity raises LINC01013's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 2.17× lower at baseline in the lines without COL5A2 | 0.068 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[PDE4B]] | B | COL5A2 activity raises PDE4B's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without COL5A2 | 0.078 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[COL1A2]] | C | COL5A2 activity raises COL1A2's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 9.29× lower at baseline in the lines without COL5A2 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[P3H2-AS1]] | C | COL5A2 activity raises P3H2-AS1's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without COL5A2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[FBXL7]] | C | COL5A2 activity raises FBXL7's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 7.05× lower at baseline in the lines without COL5A2 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[P3H2]] | C | COL5A2 activity raises P3H2's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without COL5A2 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[UTY]] | C | COL5A2 activity raises UTY's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 3.74× lower at baseline in the lines without COL5A2 | 0.028 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[COL3A1]] | C | COL5A2 activity raises COL3A1's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 6.01× lower at baseline in the lines without COL5A2 | 0.037 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[DCLK2]] | C | COL5A2 activity raises DCLK2's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 4.05× lower at baseline in the lines without COL5A2 | 0.063 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.7, 22.6); signed map (26.4, 34.8). **Vector** length 85.8, 27.6% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Scavenging by Class A Receptors* (reactome, mean cos +0.54 to 5); *Binding and Uptake of Ligands by Scavenger Receptors* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +9.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -6.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | collagen type V alpha 2 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,031,898-189,225,312 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Fibrillar collagens |
| Hallmark sets | ANGIOGENESIS, UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 30 pathways, smallest: Fibronectin matrix formation; Attachment of bacteria to epithelial cells; Biofilm formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P05997](https://www.uniprot.org/uniprotkb/P05997) (Collagen alpha-2(V) chain):

> Type V collagen is a member of group I collagen (fibrillar forming collagen). It is a minor connective tissue component of nearly ubiquitous distribution. Type V collagen binds to DNA, heparan sulfate, thrombospondin, heparin, and insulin. Type V collagen is a key determinant in the assembly of tissue-specific matrices (By similarity).

**Summary**, from NCBI Gene [1290](https://www.ncbi.nlm.nih.gov/gene/1290):

> This gene encodes an alpha chain for one of the low abundance fibrillar collagens. Fibrillar collagen molecules are trimers that can be composed of one or more types of alpha chains. Type V collagen is found in tissues containing type I collagen and appears to regulate the assembly of heterotypic fibers composed of both type I and type V collagen. This gene product is closely related to type XI collagen and it is possible that the collagen chains of types V and XI constitute a single collagen …

**Accessions** — [HGNC:2210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2210) · Entrez [1290](https://www.ncbi.nlm.nih.gov/gene/1290) · UniProt [P05997](https://www.uniprot.org/uniprotkb/P05997) · Ensembl [ENSG00000204262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204262)

## Data

Gene col 12839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12839); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12839]; `tensor/DDL_lfc|DDL_z.npy` [12839]; `embed/gene_vectors.npy` [12839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12839 or target_col == 12839). Every well: [[COL5A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL5A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
