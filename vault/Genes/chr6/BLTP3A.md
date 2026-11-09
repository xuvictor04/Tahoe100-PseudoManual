---
symbol: "BLTP3A"
type: "gene"
col: 772
ensembl_id: "ENSG00000065060"
name: "bridge-like lipid transfer protein family member 3A"
location: "6p21.31"
module: 133
arm: "+"
pooled_cpm: 49.14
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 18
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# BLTP3A

*bridge-like lipid transfer protein family member 3A* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.36× (z +8.0, q 6e-13, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.386× (z -18.0, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPG]] (+0.71, fdr 7e-06), [[YARS1]] (+0.71, fdr 7e-06), [[TMEM268]] (+0.70, fdr 7e-06); moves opposite to [[PTGS1]] (-0.51, fdr 2e-05), [[PAEP]] (-0.49, fdr 3e-05), [[ADAM8]] (-0.49, fdr 4e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MTSS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.36×** | +8.0 | 6e-13 | 38/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +6.5 | 2e-08 | 33/47 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +6.5 | 2e-08 | 33/48 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +6.4 | 3e-08 | 32/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +6.3 | 3e-08 | 28/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +6.2 | 7e-08 | 30/47 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.37×** | +5.9 | 3e-07 | 29/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +4.7 | 2e-04 | 26/47 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.18× | +4.3 | 0.001 | 18/49 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 23/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.006 | 15/47 (A549, A498, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.007 | 21/48 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.013 | 10/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.013 | 19/47 (C-33 A, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.016 | 15/47 (SHP-77, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.016 | 18/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.018 | 14/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -18.0 | 0e+00 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.417×** | -16.6 | 0e+00 | 44/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.508×** | -12.8 | 3e-35 | 41/47 (HT-29, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -10.0 | 2e-21 | 36/48 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.642×** | -8.4 | 5e-15 | 34/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.667×** | -7.4 | 2e-11 | 30/47 (SNU-1, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.682×** | -7.0 | 3e-10 | 22/40 (SHP-77, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.703×** | -6.4 | 1e-08 | 32/48 (RKO, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.743×** | -5.6 | 1e-06 | 30/47 (HT-29, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.814×** | -5.4 | 5e-06 | 25/48 (KATO III, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.754×** | -5.1 | 2e-05 | 24/47 (RKO, NCI-H2030, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -4.4 | 5e-04 | 18/48 (SNU-1, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.802×** | -3.9 | 0.005 | 23/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.822×** | -3.7 | 0.009 | 17/47 (A-427, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.821×** | -3.6 | 0.012 | 20/48 (A-172, A-427, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.045 | 16/48 (SW48, PANC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.720×** | -3.1 | 0.067 | 15/47 (MIA PaCa-2, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.845× | -2.9 | 0.088 | 16/47 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.732×** | -2.9 | 0.093 | 9/47 (SW48, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.807×** | -2.9 | 0.093 | 13/48 (PANC-1, SW48, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 78.2 | 0 | 12 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -12.4) |
| [[RKO (line)]] | wt | 92.2 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0632× (z -27.6) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -15.9) |
| [[HT-29 (line)]] | alt | 70.6 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -18.5) |
| [[KATO III (line)]] | alt | 76.7 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -17.6) |
| [[A-172 (line)]] | wt | 39.1 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -12.8) |
| [[LoVo (line)]] | wt | 66.0 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -17.6) |
| [[MIA PaCa-2 (line)]] | alt | 77.5 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -16.4) |
| [[SW480 (line)]] | alt | 64.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -19.9) |
| [[A-427 (line)]] | wt | 81.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.370× (z -11.9) |
| [[SW1417 (line)]] | alt | 50.8 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 76.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -11.5) |
| [[SW48 (line)]] | wt | 76.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -14.2) |
| [[A549 (line)]] | wt | 38.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -9.9) |
| [[LS 180 (line)]] | wt | 53.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 59.9 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.355× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 54.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.1) |
| [[SNU-1 (line)]] | wt | 77.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -15.4) |
| [[A498 (line)]] | wt | 35.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -10.3) |
| [[C-33 A (line)]] | alt | 79.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.413× (z -8.5) |
| [[HS-578T (line)]] | alt | 47.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.341× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 36.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 53.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -10.9) |
| [[AN3 CA (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0523× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -10.4) |
| [[C32 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 72.1 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.150× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPG]] | +0.71 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[YARS1]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TMEM268]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[ZBED3]] | +0.70 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[SLC3A2]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[PCK2]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[AARS1]] | +0.65 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[TARS1]] | +0.62 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[PROSER1]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[NIBAN1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MARS1]] | +0.61 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[XPOT]] | +0.60 | +0.55 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGS1]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PAEP]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ADAM8]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[LYPD3]] | -0.47 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[TRIOBP]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[GIPR]] | -0.46 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[ELL]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[MTSS1]] | -0.46 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[CYBA]] | -0.46 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[PDE2A]] | -0.45 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[FRMD8]] | -0.45 | -0.43 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTSS1]] | B | MTSS1 activity lowers BLTP3A's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.37× higher at baseline in the lines without MTSS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[PTGS1]] | B | PTGS1 activity lowers BLTP3A's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.34× higher at baseline in the lines without PTGS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[ZBED3]] | C | ZBED3 activity raises BLTP3A's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |
| [[MTHFD1L]] | C | MTHFD1L's natural level strengthens BLTP3A's drug response | MTHFD1L's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.21; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.0, 46.7); signed map (-12.5, 22.0). **Vector** length 122, 36.3% of its response variance represented; |z| ≥ 3 in 1,221 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +8.0 | +6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.5 | +6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.7 | +6.4 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.6 | +8.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.7 | +3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.7 | +5.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -18.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.9 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.9 |
|  | [[Ritonavir (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | bridge-like lipid transfer protein family member 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,792,083-34,877,514 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20302, dJ349A12.1; previously C6orf107, UHRF1BP1 |
| Gene groups (HGNC) | Bridge-like lipid transfer protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6BDS2](https://www.uniprot.org/uniprotkb/Q6BDS2) (Bridge-like lipid transfer protein family member 3A):

> Tube-forming lipid transport protein which probably mediates the transfer of lipids between membranes at organelle contact sites. May be involved in the retrograde traffic of vesicle clusters in the endocytic pathway to the Golgi complex.

**Summary**, from NCBI Gene [54887](https://www.ncbi.nlm.nih.gov/gene/54887):

> Enables histone deacetylase binding activity and identical protein binding activity. Located in late endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21216) · Entrez [54887](https://www.ncbi.nlm.nih.gov/gene/54887) · UniProt [Q6BDS2](https://www.uniprot.org/uniprotkb/Q6BDS2) · Ensembl [ENSG00000065060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065060)

## Data

Gene col 772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 772); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 772]; `tensor/DDL_lfc|DDL_z.npy` [772]; `embed/gene_vectors.npy` [772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 772 or target_col == 772). Every well: [[BLTP3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLTP3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
