---
symbol: "WFDC3"
type: "gene"
col: 4481
ensembl_id: "ENSG00000124116"
name: "WAP four-disulfide core domain 3"
location: "20q13.12"
module: 13
arm: "+"
pooled_cpm: 13.98
n_lines_expressing: 35
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 16
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# WFDC3

*WAP four-disulfide core domain 3* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +7.1, q 5e-10, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.211× (z -16.7, q 0e+00, down in 29 of 32 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WFDC10B]] (+0.88, fdr 7e-06, ⚠ same locus), [[ITGA2-AS1]] (+0.55, fdr 1e-04), [[SERPINB9P1]] (+0.55, fdr 2e-05), [[TMEM217]] (+0.54, fdr 1e-04); moves opposite to [[SLC5A4-AS1]] (-0.60, fdr 2e-05), [[NFIA]] (-0.54, fdr 1e-05), [[PPA2]] (-0.52, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); 16 go from it, the strongest it → [[BCL10-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.1 | 5e-10 | 14/33 (Hs 766T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.9 | 1e-04 | 3/19 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 1e-04 | 16/32 (SW48, SW480, …) | two highest doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.58×** | +4.9 | 1e-04 | 15/32 (C32, AsPC-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.7 | 3e-04 | 15/33 (Hs 766T, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.004 | 15/32 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[4EGI-1 (drug)]] 5 µM |  | **2.03×** | +4.0 | 0.006 | 12/28 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +3.8 | 0.012 | 11/32 (AsPC-1, SW480, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.94×** | +3.7 | 0.013 | 14/33 (MIA PaCa-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.5 | 0.031 | 10/32 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.045 | 6/32 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.72× | +3.0 | 0.11 | 6/32 (SW480, C32, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.211×** | -16.7 | 0e+00 | 29/32 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.215×** | -16.5 | 0e+00 | 32/32 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.406×** | -13.7 | 3e-40 | 25/31 (NCI-H2347, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.325×** | -12.0 | 3e-31 | 31/32 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.313×** | -12.0 | 6e-31 | 27/32 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.374×** | -10.5 | 5e-24 | 28/32 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.419×** | -9.3 | 9e-19 | 22/32 (SNU-423, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.439×** | -8.8 | 7e-17 | 25/32 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.446×** | -8.7 | 3e-16 | 24/32 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.454×** | -8.5 | 1e-15 | 25/32 (NCI-H1792, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.458×** | -8.4 | 3e-15 | 26/32 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.463×** | -7.9 | 9e-14 | 22/29 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.527×** | -6.9 | 3e-10 | 19/31 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.355×** | -5.8 | 3e-07 | 19/33 (AsPC-1, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.634×** | -4.9 | 4e-05 | 15/32 (SW 900, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -4.5 | 3e-04 | 17/32 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.659×** | -4.5 | 3e-04 | 15/32 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.761×** | -4.1 | 0.001 | 18/33 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.688×** | -3.8 | 0.005 | 14/32 (COLO 205, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -3.4 | 0.018 | 14/32 (J82, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 53.3 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0394× (z -25.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0313× (z -18.7) |
| [[SNU-423 (line)]] | alt | 87.3 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0502× (z -22.7) |
| [[RPMI-7951 (line)]] | alt | 48.7 | 0 | 11 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0379× (z -17.1) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0518× (z -16.1) |
| [[COLO 205 (line)]] | alt | 43.9 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0349× (z -26.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0149× (z -22.4) |
| [[MIA PaCa-2 (line)]] | alt | 73.6 | 0 | 9 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0495× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 32.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0544× (z -27.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0586× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 22.9 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0115× (z -22.5) |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0356× (z -18.3) |
| [[SW1417 (line)]] | alt | 29.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -16.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.121× (z -13.6) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.111× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0363× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.108× (z -11.8) |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0752× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0890× (z -9.2) |
| [[C32 (line)]] | wt | 6.50 | 0 | 2 | — | [[Flutamide (drug)]] 0.5 µM 0.0690× (z -9.0) |
| [[HS-578T (line)]] | alt | 6.90 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0367× (z -12.2) |
| [[J82 (line)]] | alt | 11.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0834× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0990× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 5.87 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -10.4) |
| [[H4 (line)]] | wt | 8.40 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM 0.0579× (z -8.6) |
| [[HCT15 (line)]] | alt | 9.86 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0835× (z -8.5) |
| [[Hs 766T (line)]] | wt | 5.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.14× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 9.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 5.15 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0777× (z -8.5) |
| [[SW48 (line)]] | wt | 11.4 | 0 | 1 | — | [[Binimetinib (drug)]] 0.05 µM 0.126× (z -8.5) |
| [[A-172 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 7 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WFDC10B]] | +0.88 | +0.91 / +0.86 | both halves | 7e-06 | same gene group; STRING 713; ⚠ same locus (42.9 kb, same strand: neighbours can correlate without regulation) |
| [[ITGA2-AS1]] | +0.55 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[SERPINB9P1]] | +0.55 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TMEM217]] | +0.54 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[MYH16]] | +0.54 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[BCL10-AS1]] | +0.54 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[KCTD5]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SLC35F4]] | +0.52 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[ZBTB43]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[UBE2R2-AS1]] | +0.51 | +0.21 / +0.55 | both halves | 7e-04 |  |
| [[KPNA7]] | +0.51 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[VPS4B]] | +0.50 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[RABGEF1P3]] | +0.50 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | -0.60 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[NFIA]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PPA2]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SLC22A5]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ZFAND4]] | -0.49 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[REV1]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CPT1A]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CHPT1]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MTARC2]] | -0.46 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[ACSF2]] | -0.46 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[THRA]] | -0.46 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[PON2]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises WFDC3's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 3.12× lower at baseline in the lines without ZNF341-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity raises WFDC3's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without ADAM8 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[WFDC10B]] | B | WFDC10B activity strengthens WFDC3's drug response | lines that do not express WFDC10B (5) vs lines expressing it (27) | the lines without WFDC10B respond 0.38× as strongly (z diff +3.65); strongest at Homoharringtonine 5 µM: 0.93x vs 0.26x (z diff +6.3) | 0.032 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[KPNA7]] | B | KPNA7 activity raises WFDC3's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without KPNA7 | 0.033 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[HRH1]] | B | HRH1 activity raises WFDC3's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.26× lower at baseline in the lines without HRH1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[CLCF1]] | B | CLCF1 activity raises WFDC3's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 2.43× lower at baseline in the lines without CLCF1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[WFDC10B]] | C | WFDC10B activity raises WFDC3's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 3.97× lower at baseline in the lines without WFDC10B | 2e-04 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent; co-absent with the target |
| [[TP53]] | C | TP53 activity weakens WFDC3's drug response | recorded loss-of-function mutation of TP53 in 23 lines vs 9 not recorded | the TP53-altered lines respond 1.96× as strongly (z diff -3.09); strongest at Homoharringtonine 5 µM: 0.23x vs 0.68x (z diff -5.5) | 0.593 over the table, 0.031 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL10-AS1]] | B | WFDC3 activity raises BCL10-AS1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without WFDC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[SERPINB9P1]] | B | WFDC3 activity raises SERPINB9P1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without WFDC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[DNTTIP1]] | B | WFDC3 activity raises DNTTIP1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 2.09× lower at baseline in the lines without WFDC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[ZNF341-AS1]] | B | WFDC3 activity raises ZNF341-AS1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without WFDC3 | 0.008 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[CPT1A]] | B | WFDC3 activity lowers CPT1A's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.72× higher at baseline in the lines without WFDC3 | 0.016 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[LUCAT1]] | B | WFDC3 activity raises LUCAT1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without WFDC3 | 0.019 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[CLCF1]] | B | WFDC3 activity raises CLCF1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without WFDC3 | 0.032 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[LRRC8A]] | B | WFDC3 activity raises LRRC8A's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.35× lower at baseline in the lines without WFDC3 | 0.034 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[ZBTB43]] | B | WFDC3 activity raises ZBTB43's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without WFDC3 | 0.046 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[NFIA]] | B | WFDC3 activity lowers NFIA's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 3.09× higher at baseline in the lines without WFDC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[ADAM8]] | B | WFDC3 activity raises ADAM8's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 2.19× lower at baseline in the lines without WFDC3 | 0.057 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[SCAT1]] | B | WFDC3 activity raises SCAT1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without WFDC3 | 0.059 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.145). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.1, 38.8); signed map (2.7, 30.8). **Vector** length 88.6, 20.4% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -12.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | WAP four-disulfide core domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,747,944-45,791,932 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ447F3.3, WAP14 |
| Gene groups (HGNC) | WAP four-disulfide core domain containing |
| Matched by | ensembl_id |

UniProt [Q8IUB2](https://www.uniprot.org/uniprotkb/Q8IUB2) carries no function annotation.

**Summary**, from NCBI Gene [140686](https://www.ncbi.nlm.nih.gov/gene/140686):

> This gene encodes a member of the WAP-type four-disulfide core (WFDC) domain family. The WFDC domain, or WAP signature motif, contains eight cysteines forming four disulfide bonds at the core of the protein, and functions as a protease inhibitor. The encoded protein contains four WFDC domains. Most WFDC genes are localized to chromosome 20q12-q13 in two clusters: centromeric and telomeric. This gene belongs to the telomeric cluster. Alternatively spliced transcript variants have been observed …

**Accessions** — [HGNC:15957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15957) · Entrez [140686](https://www.ncbi.nlm.nih.gov/gene/140686) · UniProt [Q8IUB2](https://www.uniprot.org/uniprotkb/Q8IUB2) · Ensembl [ENSG00000124116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124116)

## Data

Gene col 4481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4481); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4481]; `tensor/DDL_lfc|DDL_z.npy` [4481]; `embed/gene_vectors.npy` [4481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4481 or target_col == 4481). Every well: [[WFDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WFDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
