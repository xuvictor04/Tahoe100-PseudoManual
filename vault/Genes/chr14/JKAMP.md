---
symbol: "JKAMP"
type: "gene"
col: 560
ensembl_id: "ENSG00000050130"
name: "JNK1/MAPK8 associated membrane protein"
location: "14q23.1"
module: 183
arm: "+"
pooled_cpm: 31.58
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# JKAMP

*JNK1/MAPK8 associated membrane protein* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.28× (z +8.3, q 4e-14, up in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~24% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.33× (z +6.6, q 2e-08, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.476× (z -25.1, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC40]] (+0.76, fdr 7e-06), [[HEATR6]] (+0.75, fdr 7e-06), [[RTCA]] (+0.72, fdr 7e-06); moves opposite to [[HIVEP2]] (-0.62, fdr 7e-06), [[KDM6B]] (-0.62, fdr 1e-05), [[AGO2]] (-0.61, fdr 1e-05).
> It is in [[Module 183]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +8.3 | 4e-14 | 27/48 (CFPAC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +6.6 | 2e-08 | 25/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +5.8 | 1e-06 | 24/48 (J82, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +5.8 | 1e-06 | 21/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.52×** | +5.3 | 1e-05 | 18/47 (NCI-H1792, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.2 | 2e-05 | 17/33 (A549, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 3e-04 | 17/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.20×** | +4.4 | 7e-04 | 15/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.19× | +4.2 | 0.001 | 10/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.002 | 12/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.004 | 11/47 (LS 180, C-33 A, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.8 | 0.007 | 9/45 (COLO 205, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.007 | 9/48 (NCI-H2347, J82, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.017 | 8/47 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.019 | 5/48 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.033 | 3/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Relugolix (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.081 | 3/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.476×** | -25.1 | 0e+00 | 41/47 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -11.2 | 1e-26 | 31/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.618×** | -11.0 | 5e-26 | 31/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -9.6 | 2e-19 | 33/47 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -8.7 | 2e-16 | 30/47 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.717×** | -7.9 | 2e-13 | 24/46 (A-427, SW480, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.732×** | -7.5 | 7e-12 | 24/48 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.756×** | -6.7 | 2e-09 | 26/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.774×** | -6.1 | 5e-08 | 22/47 (KATO III, NCI-H2347, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.758×** | -6.1 | 5e-08 | 21/42 (KATO III, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.769×** | -6.0 | 9e-08 | 19/38 (NCI-H460, LS 180, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.797×** | -5.4 | 3e-06 | 20/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.790×** | -5.4 | 3e-06 | 20/48 (RKO, NCI-H460, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.814×** | -4.9 | 4e-05 | 18/48 (NCI-H460, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.822×** | -4.5 | 3e-04 | 20/48 (NCI-H2347, C32, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.905× | -3.3 | 0.027 | 9/48 (SW 1088, HT-29, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.866× | -3.3 | 0.030 | 8/47 (NCI-H2347, H4, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 0.883× | -2.9 | 0.084 | 10/48 (LS 180, BT-474, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.884× | -2.9 | 0.084 | 8/47 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.790×** | -2.9 | 0.084 | 13/48 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.887× | -2.8 | 0.099 | 3/48 (LoVo, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.3 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0745× (z -26.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.231× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 39.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -16.0) |
| [[SW 900 (line)]] | alt | 42.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.9) |
| [[KATO III (line)]] | alt | 21.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 32.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 55.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.68× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.2) |
| [[A-427 (line)]] | wt | 33.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 30.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.1) |
| [[C32 (line)]] | wt | 29.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.9) |
| [[LS 180 (line)]] | wt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 84.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.9) |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.108× (z -9.7) |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.255× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -19.6) |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0708× (z -8.8) |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HOP62 (line)]] | alt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -16.3) |
| [[Hs 766T (line)]] | wt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.5) |
| [[J82 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.9) |
| [[LoVo (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.313× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0631× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.3) |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.7) |
| [[SNU-1 (line)]] | wt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -14.3) |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.0) |
| [[SW480 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC40]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[RTCA]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[FAM104A]] | +0.69 | +0.72 / +0.57 | both halves | 8e-06 |  |
| [[USP30]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TRAPPC2]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[BCL9]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[TENT2]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[KDM6B]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[AGO2]] | -0.61 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[SKIL]] | -0.61 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[THOC6]] | -0.60 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ABR]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[NFATC1]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[DDX5]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.57 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.0, -10.8); signed map (-31.2, -12.1). **Vector** length 102, 23.1% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +6.0 | +8.3 |
|  | [[NG25 (drug)]] 5 µM |  | +5.3 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +4.7 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.9 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -25.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -4.6 | -7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.5 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.5 | -6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | JNK1/MAPK8 associated membrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:59,484,443-59,505,410 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC213, JAMP, HSPC327, CDA06; previously C14orf100 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P055](https://www.uniprot.org/uniprotkb/Q9P055) (JNK1/MAPK8-associated membrane protein):

> Regulates the duration of MAPK8 activity in response to various stress stimuli (By similarity). Facilitates the degradation of misfolded endoplasmic reticulum (ER) proteins through the recruitment of components of the proteasome and endoplasmic reticulum-associated degradation (ERAD) system. Is required for proper degradation of prosaposin receptor GPR37.

**Summary**, from NCBI Gene [51528](https://www.ncbi.nlm.nih.gov/gene/51528):

> Enables ubiquitin protein ligase binding activity. Involved in ERAD pathway. Predicted to be located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20184) · Entrez [51528](https://www.ncbi.nlm.nih.gov/gene/51528) · UniProt [Q9P055](https://www.uniprot.org/uniprotkb/Q9P055) · Ensembl [ENSG00000050130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050130)

## Data

Gene col 560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 560); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 560]; `tensor/DDL_lfc|DDL_z.npy` [560]; `embed/gene_vectors.npy` [560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 560 or target_col == 560). Every well: [[JKAMP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JKAMP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
