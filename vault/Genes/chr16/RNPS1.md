---
symbol: "RNPS1"
type: "gene"
col: 13025
ensembl_id: "ENSG00000205937"
name: "RNA binding protein with serine rich domain 1"
location: "16p13.3"
module: 33
arm: "+"
pooled_cpm: 73.25
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RNPS1

*RNA binding protein with serine rich domain 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (17 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.31× (z +12.0, q 3e-30, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.780× (z -4.6, q 0.001, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPSA]] (+0.79, fdr 7e-06), [[NSUN2]] (+0.77, fdr 7e-06), [[URB1]] (+0.74, fdr 7e-06); moves opposite to [[SMDT1]] (-0.70, fdr 7e-06), [[TMEM205]] (-0.69, fdr 7e-06), [[PIM3]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.31×** | +12.0 | 3e-30 | 45/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.08×** | +11.2 | 9e-27 | 47/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.72×** | +10.3 | 2e-22 | 39/48 (NCI-H1792, NCI-H23, …) | all doses, flat | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +10.1 | 5e-22 | 47/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +9.9 | 4e-21 | 41/47 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.9 | 4e-21 | 37/48 (AsPC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.71×** | +9.5 | 2e-19 | 39/45 (KATO III, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.43×** | +6.5 | 5e-09 | 32/43 (NCI-H1792, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +6.5 | 6e-09 | 34/48 (LS 180, AsPC-1, …) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.6 | 2e-06 | 25/36 (NCI-H1573, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.74×** | +5.5 | 2e-06 | 36/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.33×** | +5.4 | 3e-06 | 29/48 (Hs 766T, SW480, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +5.4 | 3e-06 | 36/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.32×** | +5.0 | 2e-05 | 28/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.29×** | +4.7 | 8e-05 | 24/48 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.002 | 28/48 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.007 | 20/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.026 | 19/48 (Hs 766T, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.027 | 16/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.041 | 12/48 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.047 | 11/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +2.9 | 0.068 | 21/48 (SW480, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.780×** | -4.6 | 0.001 | 31/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.719×** | -4.6 | 0.001 | 29/47 (Hs 766T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.792×** | -4.5 | 0.001 | 24/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.806×** | -4.2 | 0.003 | 27/48 (SW480, A498, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.806×** | -4.2 | 0.003 | 23/48 (COLO 205, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.846× | -4.0 | 0.004 | 19/48 (C-33 A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.813×** | -4.0 | 0.004 | 23/48 (A-427, SW1417, …) | two highest doses | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.848× | -3.8 | 0.009 | 16/48 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.012 | 23/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.016 | 18/49 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.838× | -3.6 | 0.016 | 16/50 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -3.5 | 0.022 | 18/48 (KATO III, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.5 | 0.022 | 20/48 (NCI-H23, MIA PaCa-2, …) | two highest doses | composition shift; position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.880× | -3.4 | 0.024 | 5/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.887× | -3.3 | 0.034 | 4/48 (HEC-1-A, J82, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 0.850× | -3.2 | 0.054 | 9/49 (SW48, A498, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.894× | -3.1 | 0.060 | 4/48 (C-33 A, RKO, …) | inconsistent across doses | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **0.741×** | -3.0 | 0.075 | 11/48 (A498, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 0.898× | -3.0 | 0.077 | 7/48 (Panc 03.27, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 80.7 | 5 (3 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.47× (z +10.6) | — |
| [[KATO III (line)]] | alt | 82.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.77× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 66.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.53× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 44.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 54.7 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.61× (z +11.2) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 56.6 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.83× (z +9.8) ⚠ toxic | — |
| [[LoVo (line)]] | wt | 66.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.44× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 66.6 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.14× (z +10.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.75× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.8 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.65× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 49.9 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.40× (z +12.2) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 5.30× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 94.0 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 3.76× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 49.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.84× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 85.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -12.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[AN3 CA (line)]] | alt | 93.9 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.252× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 110 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.6) | — |
| [[RKO (line)]] | wt | 95.4 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.78× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0721× (z -8.7) |
| [[SW1417 (line)]] | alt | 90.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.6) | — |
| [[SW48 (line)]] | wt | 115 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.05× (z +9.1) | — |
| [[A-172 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | +0.79 | +0.75 / +0.79 | both halves | 7e-06 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[NSUN2]] | +0.77 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[URB1]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[CHID1]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CCAR2]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[EIF3B]] | +0.71 | +0.76 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1 |
| [[BLTP2]] | +0.70 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.68 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MTRR]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GCN1]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[NOM1]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMDT1]] | -0.70 | -0.72 / -0.65 | both halves | 7e-06 |  |
| [[TMEM205]] | -0.69 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[PIM3]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | -0.65 | -0.58 / -0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CHMP2B]] | -0.64 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[JUND]] | -0.64 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[GIHCG]] | -0.63 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[LINC01273]] | -0.63 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[PNRC1]] | -0.63 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[UBE2B]] | -0.62 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[RAB9A]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises RNPS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[LGALS3]] | B | LGALS3 activity lowers RNPS1's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.27× higher at baseline in the lines without LGALS3 | 0.072 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[ATXN1]] | B | ATXN1 activity lowers RNPS1's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.42× higher at baseline in the lines without ATXN1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.2, -28.4); signed map (-23.7, -45.4). **Vector** length 111, 31.1% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +5.9 | +6.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.7 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.3 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -7.0 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -4.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding protein with serine rich domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,253,116-2,268,397 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing; ASAP complex subunits |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 16 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15287](https://www.uniprot.org/uniprotkb/Q15287) (RNA-binding protein with serine-rich domain 1):

> Part of pre- and post-splicing multiprotein mRNP complexes. Auxiliary component of the splicing-dependent multiprotein exon junction complex (EJC) deposited at splice junction on mRNAs. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex only transiently either during EJC assembly or during subsequent mRNA metabolism. Component of the ASAP and PSAP complexes which bind RNA in a sequence-independent …

**Summary**, from NCBI Gene [10921](https://www.ncbi.nlm.nih.gov/gene/10921):

> This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons. This protein binds to the mRNA and remains bound after nuclear export, acting as a …

**Accessions** — [HGNC:10080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10080) · Entrez [10921](https://www.ncbi.nlm.nih.gov/gene/10921) · UniProt [Q15287](https://www.uniprot.org/uniprotkb/Q15287) · Ensembl [ENSG00000205937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205937)

## Data

Gene col 13025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13025); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13025]; `tensor/DDL_lfc|DDL_z.npy` [13025]; `embed/gene_vectors.npy` [13025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13025 or target_col == 13025). Every well: [[RNPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
