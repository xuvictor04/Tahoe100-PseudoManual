---
symbol: "APOBEC3F"
type: "gene"
col: 4881
ensembl_id: "ENSG00000128394"
name: "apolipoprotein B mRNA editing enzyme catalytic subunit 3F"
location: "22q13.1"
module: 32
arm: "+"
pooled_cpm: 8.34
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 27
n_dd_up_clean: 16
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# APOBEC3F

*apolipoprotein B mRNA editing enzyme catalytic subunit 3F* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +6.5, q 5e-08, up in 20 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.400× (z -14.9, q 0e+00, down in 34 of 41 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.419× (z -10.0, q 6e-21, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF11]] (+0.74, fdr 1e-05), [[APOL2]] (+0.73, fdr 7e-06), [[PARP14]] (+0.72, fdr 7e-06); moves opposite to [[SMYD3]] (-0.58, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LY6E-DT]] → it (grade B ⚠); 5 go from it, the strongest it → [[HLA-B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.5 | 5e-08 | 20/40 (hTERT-HPNE, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.1 | 1e-04 | 15/45 (A498, A-172, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.6 | 6e-04 | 7/17 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.35×** | +4.6 | 6e-04 | 13/44 (NCI-H23, CFPAC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +4.1 | 0.005 | 11/43 (A498, A549, …) | rises with dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.44×** | +4.0 | 0.006 | 7/42 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.006 | 14/43 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.007 | 13/42 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.022 | 16/41 (SNU-423, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.024 | 7/45 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.024 | 12/43 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.030 | 10/45 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.034 | 9/44 (Hs 766T, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.034 | 12/42 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.30×** | +3.3 | 0.034 | 7/45 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.034 | 4/41 (NCI-H23, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.034 | 12/44 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.062 | 7/44 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.400×** | -14.9 | 0e+00 | 34/41 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.419×** | -10.0 | 6e-21 | 29/45 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.422×** | -9.9 | 8e-21 | 32/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.436×** | -9.5 | 3e-19 | 25/39 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.474×** | -8.5 | 1e-15 | 33/44 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.484×** | -8.3 | 8e-15 | 27/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.501×** | -7.9 | 2e-13 | 28/43 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.518×** | -7.5 | 4e-12 | 30/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.541×** | -6.8 | 8e-10 | 22/34 (A-427, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -6.6 | 3e-09 | 25/41 (SNU-423, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.385×** | -5.7 | 5e-07 | 24/39 (SNU-423, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -5.5 | 1e-06 | 23/43 (CFPAC-1, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.603×** | -5.5 | 2e-06 | 20/45 (C-33 A, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.642×** | -5.1 | 2e-05 | 23/44 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.489×** | -4.3 | 7e-04 | 17/39 (HCT15, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.699×** | -4.1 | 0.002 | 16/39 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.732×** | -3.6 | 0.011 | 12/40 (SK-MEL-2, CFPAC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.739×** | -3.5 | 0.015 | 7/45 (NCI-H2030, C-33 A, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.733×** | -3.4 | 0.022 | 11/43 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.753×** | -3.1 | 0.052 | 6/45 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.609×** | -3.0 | 0.068 | 5/42 (A549, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.762×** | -2.9 | 0.076 | 11/41 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -11.9) |
| [[A549 (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0217× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[PANC-1 (line)]] | alt | 5.77 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -15.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.189× (z -8.6) |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0354× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -16.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -10.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.152× (z -8.7) |
| [[A-427 (line)]] | wt | 9.86 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 5.76 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0509× (z -10.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.206× (z -9.7) |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0938× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 4.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 4.89 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0699× (z -9.5) |
| [[A498 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.998 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF11]] | +0.74 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[APOL2]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[PARP14]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[NMI]] | +0.71 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[GBP3]] | +0.70 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[TRIM21]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SCAMP1-AS1]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PARP10]] | +0.69 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[SLC15A3]] | +0.68 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[IFI35]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[APOL3]] | +0.68 | +0.57 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD3]] | -0.58 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LY6E-DT]] | B | LY6E-DT activity raises APOBEC3F's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without LY6E-DT | 0.014 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers APOBEC3F's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PKP2]] | B | PKP2 activity raises APOBEC3F's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 1.29× lower at baseline in the lines without PKP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[HLA-H]] | B | HLA-H activity raises APOBEC3F's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without HLA-H | 0.075 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[HLA-B]] | B | HLA-B activity raises APOBEC3F's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without HLA-B | 0.086 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-B]] | C | APOBEC3F activity raises HLA-B's level | lines that do not express APOBEC3F (3) vs lines expressing it (47) | 5.94× lower at baseline in the lines without APOBEC3F | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, HOMER3, UGDH; its own permutation p |
| [[PARP12]] | C | APOBEC3F activity raises PARP12's level | lines that do not express APOBEC3F (3) vs lines expressing it (47) | 3.15× lower at baseline in the lines without APOBEC3F | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, HOMER3, UGDH; its own permutation p |
| [[NMI]] | C | APOBEC3F activity raises NMI's level | lines that do not express APOBEC3F (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without APOBEC3F | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, HOMER3, UGDH |
| [[HLA-C]] | C | APOBEC3F activity raises HLA-C's level | lines that do not express APOBEC3F (3) vs lines expressing it (47) | 3.54× lower at baseline in the lines without APOBEC3F | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, HOMER3, UGDH; its own permutation p |
| [[RBM43]] | C | APOBEC3F activity raises RBM43's level | lines that do not express APOBEC3F (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without APOBEC3F | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, HOMER3, UGDH; its own permutation p |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.4, 53.1); signed map (61.4, 31.4). **Vector** length 75.3, 14.4% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.55 to 56); *interferon gamma response* (hallmark, mean cos +0.56 to 60); *interferon* (control, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.7 | -8.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -10.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein B mRNA editing enzyme catalytic subunit 3F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,040,604-39,055,972 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARP8, BK150C2.4.MRNA, KA6 |
| Gene groups (HGNC) | Apolipoprotein B mRNA editing enzyme catalytic subunits |
| Hallmark sets | COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUX4](https://www.uniprot.org/uniprotkb/Q8IUX4) (DNA dC->dU-editing enzyme APOBEC-3F):

> DNA deaminase (cytidine deaminase) which acts as an inhibitor of retrovirus replication and retrotransposon mobility via deaminase-dependent and -independent mechanisms. Exhibits antiviral activity against viruse such as HIV-1 or HIV-2. After the penetration of retroviral nucleocapsids into target cells of infection and the initiation of reverse transcription, it can induce the conversion of cytosine to uracil in the minus-sense single-strand viral DNA, leading to G-to-A hypermutations in the …

**Summary**, from NCBI Gene [200316](https://www.ncbi.nlm.nih.gov/gene/200316):

> This gene is a member of the cytidine deaminase gene family. It is one of seven related genes or pseudogenes found in a cluster, thought to result from gene duplication, on chromosome 22. Members of the cluster encode proteins that are structurally and functionally related to the C to U RNA-editing cytidine deaminase APOBEC1. It is thought that the proteins may be RNA editing enzymes and have roles in growth or cell cycle control. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:17356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17356) · Entrez [200316](https://www.ncbi.nlm.nih.gov/gene/200316) · UniProt [Q8IUX4](https://www.uniprot.org/uniprotkb/Q8IUX4) · Ensembl [ENSG00000128394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128394)

## Data

Gene col 4881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4881); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4881]; `tensor/DDL_lfc|DDL_z.npy` [4881]; `embed/gene_vectors.npy` [4881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4881 or target_col == 4881). Every well: [[APOBEC3F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOBEC3F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
