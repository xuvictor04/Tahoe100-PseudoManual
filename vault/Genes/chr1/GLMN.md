---
symbol: "GLMN"
type: "gene"
col: 10533
ensembl_id: "ENSG00000174842"
name: "glomulin"
location: "1p22.1"
module: 18
arm: "+"
pooled_cpm: 54.49
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GLMN

*glomulin* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.49× (z +9.7, q 2e-19, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.514× (z -14.9, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.618× (z -11.3, q 3e-27, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL8]] (+0.69, fdr 7e-06), [[SFXN4]] (+0.63, fdr 7e-06), [[FASTKD1]] (+0.62, fdr 1e-05); moves opposite to [[YWHAZ]] (-0.65, fdr 7e-05), [[CHMP4B]] (-0.64, fdr 7e-06), [[TUG1]] (-0.58, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LMO7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +9.7 | 2e-19 | 41/48 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.36×** | +7.2 | 2e-10 | 30/47 (LoVo, Hs 766T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +6.7 | 3e-09 | 27/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 0.001 | 16/48 (LOX-IMVI, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.007 | 11/48 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.11× | +3.5 | 0.039 | 1/48 (LS 180) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.049 | 17/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.11× | +3.3 | 0.069 | 3/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.080 | 6/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.514×** | -14.9 | 0e+00 | 36/44 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.686×** | -12.9 | 1e-35 | 34/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -11.9 | 1e-30 | 36/47 (RKO, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.618×** | -11.3 | 3e-27 | 35/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -10.8 | 4e-25 | 36/48 (C32, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -10.4 | 2e-23 | 44/49 (NCI-H2030, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -10.1 | 7e-22 | 30/43 (LOX-IMVI, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -9.5 | 2e-19 | 31/48 (A-427, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.697×** | -8.8 | 1e-16 | 31/48 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -8.2 | 2e-14 | 31/48 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -7.1 | 6e-11 | 29/48 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -7.0 | 2e-10 | 25/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -6.2 | 2e-08 | 29/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.795×** | -5.6 | 1e-06 | 25/47 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.803×** | -5.3 | 4e-06 | 20/48 (MIA PaCa-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.814×** | -5.0 | 2e-05 | 23/48 (C-33 A, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.821×** | -4.8 | 6e-05 | 21/48 (MIA PaCa-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.825×** | -4.7 | 9e-05 | 17/48 (PANC-1, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -4.5 | 2e-04 | 9/48 (PANC-1, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.834× | -4.2 | 6e-04 | 16/47 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 69.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 98.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 51.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.438× (z -10.6) |
| [[SW480 (line)]] | alt | 77.9 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.457× (z -12.8) |
| [[HOP62 (line)]] | alt | 33.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 76.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -15.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 65.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.498× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 65.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -9.1) |
| [[SNU-1 (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.0) |
| [[A-427 (line)]] | wt | 54.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -15.7) |
| [[A549 (line)]] | wt | 42.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.377× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.241× (z -10.4) ⚠ toxic |
| [[HCT15 (line)]] | alt | 69.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.410× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 67.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.375× (z -10.6) |
| [[NCI-H596 (line)]] | alt | 59.0 | 1 | 1 | [[Salicylic acid (drug)]] 0.5 µM 1.71× (z +10.4) | [[Bimiralisib (drug)]] 5 µM 0.224× (z -16.5) |
| [[PANC-1 (line)]] | alt | 56.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.439× (z -10.0) |
| [[RKO (line)]] | wt | 87.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.8) |
| [[H4 (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -12.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 46.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.484× (z -9.2) |
| [[HS-578T (line)]] | alt | 47.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 89.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 | STRING 720 |
| [[SFXN4]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[FASTKD1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PHKA1]] | +0.61 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MRPS5]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[NT5M]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PIGU]] | +0.60 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MTX2]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[FBXL4]] | +0.59 | +0.61 / +0.57 | both halves | 8e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[LSM2]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[L2HGDH]] | +0.59 | +0.52 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAZ]] | -0.65 | -0.38 / -0.72 | both halves | 7e-05 |  |
| [[CHMP4B]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[TUG1]] | -0.58 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[ZSCAN30]] | -0.56 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[PURB]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ESRRB]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PRECSIT]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[NR3C1]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LINC01933]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[CHMP1B]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.54 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[LINC00907]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMO7]] | B | LMO7 activity lowers GLMN's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 1.70× higher at baseline in the lines without LMO7 | 0.008 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[NT5M]] | B | NT5M activity raises GLMN's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without NT5M | 0.052 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.6, -17.8); signed map (-40.3, -20.4). **Vector** length 118, 31.7% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | +8.9 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.4 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +6.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.8 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -9.3 | -10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.9 | -14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -8.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.6 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | glomulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:92,246,402-92,298,987 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAP48, FAP68, GLML, GVM, FKBPAP; previously VMGLOM |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92990](https://www.uniprot.org/uniprotkb/Q92990) (Glomulin):

> [Isoform 1]: Regulatory component of cullin-RING-based SCF (SKP1-Cullin-F-box protein) E3 ubiquitin-protein ligase complexes. Inhibits E3 ubiquitin ligase activity by binding to RBX1 (via RING domain) and inhibiting its interaction with the E2 ubiquitin-conjugating enzyme CDC34. Inhibits RBX1-mediated neddylation of CUL1. Required for normal stability and normal cellular levels of key components of SCF ubiquitin ligase complexes, including FBXW7, RBX1, CUL1, CUL2, CUL3, CUL4A, and thereby …

**Summary**, from NCBI Gene [11146](https://www.ncbi.nlm.nih.gov/gene/11146):

> This gene encodes a phosphorylated protein that is a member of a Skp1-Cullin-F-box-like complex. The protein is essential for normal development of the vasculature and mutations in this gene have been associated with glomuvenous malformations, also called glomangiomas. Multiple splice variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:14373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14373) · Entrez [11146](https://www.ncbi.nlm.nih.gov/gene/11146) · UniProt [Q92990](https://www.uniprot.org/uniprotkb/Q92990) · Ensembl [ENSG00000174842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174842)

## Data

Gene col 10533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10533); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10533]; `tensor/DDL_lfc|DDL_z.npy` [10533]; `embed/gene_vectors.npy` [10533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10533 or target_col == 10533). Every well: [[GLMN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLMN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
