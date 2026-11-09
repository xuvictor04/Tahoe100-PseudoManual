---
symbol: "WFDC10B"
type: "gene"
col: 11344
ensembl_id: "ENSG00000182931"
name: "WAP four-disulfide core domain 10B"
location: "20q13.12"
module: 13
arm: "+"
pooled_cpm: 14.91
n_lines_expressing: 30
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# WFDC10B

*WAP four-disulfide core domain 10B* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.54× (z +5.6, q 2e-05, up in 16 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.220× (z -13.5, q 1e-38, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WFDC3]] (+0.88, fdr 7e-06, ⚠ same locus), [[ADAMTS9-AS2]] (+0.53, fdr 1e-05), [[SERPINB9P1]] (+0.52, fdr 1e-05), [[LINC02882]] (+0.51, fdr 3e-05); moves opposite to [[SLC5A4-AS1]] (-0.61, fdr 3e-05), [[NFIA]] (-0.53, fdr 3e-05), [[SLC22A5]] (-0.49, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EVA1A-AS]] → it (grade B ⚠); 17 go from it, the strongest it → [[SERPINB9P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.6 | 2e-05 | 16/28 (SW 900, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.7 | 8e-04 | 2/13 (SW480, NCI-H2347) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 0.002 | 4/28 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.59×** | +4.2 | 0.004 | 12/27 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.007 | 13/27 (SW480, SW 900, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +3.6 | 0.025 | 12/27 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.52×** | +3.6 | 0.025 | 8/28 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.025 | 10/27 (SW480, AsPC-1, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **2.07×** | +3.4 | 0.040 | 6/25 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.040 | 9/28 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.063 | 10/27 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.063 | 12/27 (NCI-H1792, SW 1271, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.076 | 5/27 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.077 | 9/27 (J82, RPMI-7951, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.090 | 6/27 (SNU-423, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.220×** | -13.5 | 1e-38 | 25/27 (SK-MEL-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.362×** | -12.8 | 6e-35 | 24/27 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.264×** | -11.9 | 3e-30 | 26/27 (RPMI-7951, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.289×** | -10.6 | 3e-24 | 25/27 (COLO 205, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.319×** | -10.2 | 3e-22 | 25/27 (COLO 205, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.325×** | -10.0 | 1e-21 | 23/27 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.330×** | -9.9 | 5e-21 | 26/27 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.412×** | -7.9 | 2e-13 | 24/27 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.452×** | -7.1 | 1e-10 | 23/27 (NCI-H23, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.416×** | -7.0 | 1e-10 | 24/27 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.483×** | -6.5 | 5e-09 | 24/27 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.494×** | -6.3 | 2e-08 | 20/27 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.302×** | -5.6 | 1e-06 | 23/28 (RPMI-7951, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.551×** | -5.0 | 3e-05 | 20/27 (SNU-423, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.571×** | -5.0 | 3e-05 | 19/26 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.673×** | -4.9 | 3e-05 | 18/27 (SK-MEL-2, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -4.0 | 0.002 | 16/27 (AsPC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.437×** | -3.8 | 0.003 | 15/27 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.764×** | -3.2 | 0.036 | 8/28 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.789×** | -2.9 | 0.075 | 9/27 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.723×** | -2.9 | 0.089 | 7/27 (COLO 205, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 70.7 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0108× (z -22.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -18.5) |
| [[SNU-423 (line)]] | alt | 130 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0904× (z -19.2) |
| [[COLO 205 (line)]] | alt | 55.0 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0138× (z -21.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0516× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 73.1 | 0 | 13 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0348× (z -18.3) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.164× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0280× (z -20.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0360× (z -18.7) |
| [[NCI-H1792 (line)]] | alt | 37.1 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0296× (z -18.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0586× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 36.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0304× (z -20.7) |
| [[J82 (line)]] | alt | 12.3 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0573× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.214× (z -9.6) |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -14.3) |
| [[SW1417 (line)]] | alt | 35.5 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0923× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.0) |
| [[SW480 (line)]] | alt | 17.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 9.31 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0434× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0540× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0501× (z -11.4) |
| [[HOP62 (line)]] | alt | 10.6 | 1 | 1 | [[Cobimetinib (drug)]] 5 µM 10.3× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 9.03 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0505× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 5.79 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Dexamethasone (drug)]] 0.5 µM 0.166× (z -8.8) |
| [[HCT15 (line)]] | alt | 8.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0584× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WFDC3]] | +0.88 | +0.91 / +0.86 | both halves | 7e-06 | same gene group; STRING 713; ⚠ same locus (42.9 kb, same strand: neighbours can correlate without regulation) |
| [[ADAMTS9-AS2]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SERPINB9P1]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[LINC02882]] | +0.51 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ALDH1A2]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[ZNF585B]] | +0.48 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[CLDN14-AS1]] | +0.48 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[EFCAB13]] | +0.48 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[LINC01500]] | +0.46 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[OR9Q1]] | +0.45 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[MTMR9LP]] | +0.45 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[DUOX2]] | +0.44 | +0.42 / +0.31 | both halves | 2e-04 |  |
| [[LINC02904]] | +0.43 | +0.30 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[NFIA]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SLC22A5]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TPD52L1]] | -0.48 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[GK5]] | -0.46 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ZFAND4]] | -0.45 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ACSF2]] | -0.45 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[CHPT1]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[FLVCR2]] | -0.44 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[PPA2]] | -0.43 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[MERTK]] | -0.43 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[GATA4]] | -0.43 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EVA1A-AS]] | B | EVA1A-AS activity raises WFDC10B's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without EVA1A-AS | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[CLCF1]] | B | CLCF1 activity raises WFDC10B's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without CLCF1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[NFIA]] | B | NFIA activity lowers WFDC10B's level | lines that do not express NFIA (11) vs lines expressing it (39) | 3.08× higher at baseline in the lines without NFIA | 0.087 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[WFDC3]] | C | WFDC3 activity raises WFDC10B's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 4.34× lower at baseline in the lines without WFDC3 | 0.002 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent; co-absent with the target |
| [[MAF]] | C | MAF activity raises WFDC10B's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.61× lower at baseline in the lines without MAF | 0.058 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB9P1]] | B | WFDC10B activity raises SERPINB9P1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without WFDC10B | 0.003 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[NFIA]] | B | WFDC10B activity lowers NFIA's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 3.43× higher at baseline in the lines without WFDC10B | 0.006 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[DNTTIP1]] | B | WFDC10B activity raises DNTTIP1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without WFDC10B | 0.008 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[ASIC1]] | B | WFDC10B activity lowers ASIC1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.94× higher at baseline in the lines without WFDC10B | 0.027 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[ALDH1A2]] | B | WFDC10B activity raises ALDH1A2's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.49× lower at baseline in the lines without WFDC10B | 0.031 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[STYXL1]] | B | WFDC10B activity raises STYXL1's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.18× lower at baseline in the lines without WFDC10B | 0.031 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[MANCR]] | B | WFDC10B activity raises MANCR's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 3.02× lower at baseline in the lines without WFDC10B | 0.032 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[WFDC3]] | B | WFDC10B activity strengthens WFDC3's drug response | lines that do not express WFDC10B (5) vs lines expressing it (27) | the lines without WFDC10B respond 0.38× as strongly (z diff +3.65); strongest at Homoharringtonine 5 µM: 0.93x vs 0.26x (z diff +6.3) | 0.032 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DNTTIP1]] | B | WFDC10B activity strengthens DNTTIP1's drug response | lines that do not express WFDC10B (20) vs lines expressing it (29) | the lines without WFDC10B respond 0.51× as strongly (z diff +2.26); strongest at Panobinostat 5 µM: 0.98x vs 0.54x (z diff +4.1) | 0.034 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MYH16]] | B | WFDC10B activity raises MYH16's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without WFDC10B | 0.035 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[ADAMTS9-AS2]] | B | WFDC10B activity raises ADAMTS9-AS2's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without WFDC10B | 0.058 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[LRP4]] | B | WFDC10B activity lowers LRP4's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.96× higher at baseline in the lines without WFDC10B | 0.061 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.256). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.0, 38.8); signed map (31.3, 48.8). **Vector** length 79.0, 20.4% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.9 |
| fall | [[Brivudine (drug)]] 5 µM |  | -2.4 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | -7.0 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | WAP four-disulfide core domain 10B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,684,651-45,705,019 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WAP12 |
| Gene groups (HGNC) | WAP four-disulfide core domain containing |
| Matched by | ensembl_id |

UniProt [Q8IUB3](https://www.uniprot.org/uniprotkb/Q8IUB3) carries no function annotation.

**Summary**, from NCBI Gene [280664](https://www.ncbi.nlm.nih.gov/gene/280664):

> This gene encodes a member of the WAP-type four-disulfide core (WFDC) domain family. The WFDC domain, or WAP signature motif, contains eight cysteines forming four disulfide bonds at the core of the protein, and functions as a protease inhibitor. Most WFDC gene members are localized to chromosome 20q12-q13 in two clusters: centromeric and telomeric. This gene belongs to the telomeric cluster. Two alternatively spliced transcript variants have been found for this gene, and they encode distinct …

**Accessions** — [HGNC:20479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20479) · Entrez [280664](https://www.ncbi.nlm.nih.gov/gene/280664) · UniProt [Q8IUB3](https://www.uniprot.org/uniprotkb/Q8IUB3) · Ensembl [ENSG00000182931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182931)

## Data

Gene col 11344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11344); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11344]; `tensor/DDL_lfc|DDL_z.npy` [11344]; `embed/gene_vectors.npy` [11344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11344 or target_col == 11344). Every well: [[WFDC10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WFDC10B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
