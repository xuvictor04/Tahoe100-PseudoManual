---
symbol: "VKORC1L1"
type: "gene"
col: 12273
ensembl_id: "ENSG00000196715"
name: "vitamin K epoxide reductase complex subunit 1L1"
location: "7q11.21"
module: 36
arm: "+"
pooled_cpm: 86.73
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# VKORC1L1

*vitamin K epoxide reductase complex subunit 1L1* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.55× (z +9.6, q 6e-19, up in 43 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.23× (z +4.6, q 9e-04, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.591× (z -16.2, q 0e+00, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.572× (z -11.7, q 4e-29, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALT2]] (+0.70, fdr 7e-06), [[NTAQ1]] (+0.68, fdr 7e-06), [[ZBED4]] (+0.68, fdr 7e-06); moves opposite to [[ARRDC3]] (-0.65, fdr 1e-05), [[BHLHE41]] (-0.63, fdr 7e-06), [[DZIP3]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ABCA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +9.6 | 6e-19 | 43/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +5.8 | 2e-06 | 27/48 (SNU-423, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 9e-04 | 20/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +4.5 | 0.001 | 22/48 (SNU-423, SW 900, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.2 | 0.003 | 9/49 (H4, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.003 | 22/48 (SHP-77, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.1 | 0.003 | 21/47 (NCI-H1792, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.20× | +3.9 | 0.006 | 22/48 (SNU-423, SW 900, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.5 | 0.026 | 0/50 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.028 | 8/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.064 | 15/48 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.16× | +3.2 | 0.064 | 16/48 (NCI-H460, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.064 | 13/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.068 | 14/47 (NCI-H2030, SW480, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.16× | +3.1 | 0.071 | 16/48 (HT-29, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.591×** | -16.2 | 0e+00 | 38/48 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.572×** | -11.7 | 4e-29 | 40/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -7.4 | 4e-11 | 27/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.584×** | -6.1 | 1e-07 | 31/49 (A-172, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.789×** | -5.2 | 3e-05 | 24/49 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.807×** | -4.2 | 0.002 | 23/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.830×** | -4.1 | 0.004 | 20/48 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -4.0 | 0.004 | 17/48 (RKO, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.8 | 0.010 | 8/48 (HCT15, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.843× | -3.7 | 0.011 | 20/49 (BT-474, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | 0.849× | -3.6 | 0.018 | 20/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.853× | -3.3 | 0.040 | 15/47 (MIA PaCa-2, CHP-212, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.904× | -3.1 | 0.076 | 13/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 96.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -22.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.255× (z -15.0) |
| [[A-427 (line)]] | wt | 108 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0928× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.244× (z -16.8) |
| [[A498 (line)]] | wt | 120 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.289× (z -16.8) |
| [[HS-578T (line)]] | alt | 96.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.264× (z -13.9) |
| [[HOP62 (line)]] | alt | 76.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -16.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.445× (z -8.7) |
| [[LoVo (line)]] | wt | 103 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.281× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 136 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.363× (z -11.8) |
| [[SW48 (line)]] | wt | 122 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.283× (z -10.7) |
| [[SW480 (line)]] | alt | 124 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.88× (z +9.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.378× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[A549 (line)]] | wt | 73.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -12.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.430× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -13.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -10.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 43.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.300× (z -9.0) |
| [[J82 (line)]] | alt | 83.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -19.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 73.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.61× (z +9.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 83.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 90.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -19.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.288× (z -18.6) |
| [[RKO (line)]] | wt | 92.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -18.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[H4 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 63.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 76.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.35× (z +10.0) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 96.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.57× (z +8.8) ⚠ unreliable plate only | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT2]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[NTAQ1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ZBED4]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 | STRING 503 |
| [[ZMYND19]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[CAMKK2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SRM]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[HIRA]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[DKC1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[WRN]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRDC3]] | -0.65 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[BHLHE41]] | -0.63 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[DZIP3]] | -0.61 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[BTN2A2]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[LGALS8]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZNF436]] | -0.60 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[TET2]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PHYH]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ATP23]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[PHF21A]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | ABCA3 activity raises VKORC1L1's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without ABCA3 | 0.039 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[ADCY3]] | B | ADCY3 activity raises VKORC1L1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.23× lower at baseline in the lines without ADCY3 | 0.061 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[HDAC6]] | B | HDAC6 activity lowers VKORC1L1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZC3H12A]] | B | ZC3H12A activity lowers VKORC1L1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.32× higher at baseline in the lines without ZC3H12A | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[BHLHE41]] | B | BHLHE41 activity lowers VKORC1L1's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.22× higher at baseline in the lines without BHLHE41 | 0.099 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[ZNF436]] | C | ZNF436's natural level weakens VKORC1L1's drug response | ZNF436's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.29; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[GARNL3]] | C | GARNL3 activity raises VKORC1L1's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without GARNL3 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.1, -28.1); signed map (-44.9, -17.2). **Vector** length 131, 38.0% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.5 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.9 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.7 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.4 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.9 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -9.5 | -16.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -5.2 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | vitamin K epoxide reductase complex subunit 1L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.21 — chr7:65,873,074-65,959,563 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Vitamin K epoxide reductase complex subunit 1 family |
| Reactome | 3 pathways, smallest: Metabolism of vitamin K; Metabolism of fat-soluble vitamins; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0U8](https://www.uniprot.org/uniprotkb/Q8N0U8) (Vitamin K epoxide reductase complex subunit 1-like protein 1):

> Involved in vitamin K metabolism. Can reduce inactive vitamin K 2,3-epoxide to active vitamin K, and may contribute to vitamin K-mediated protection against oxidative stress. Plays a role in vitamin K-dependent gamma-carboxylation of Glu residues in target proteins.

**Summary**, from NCBI Gene [154807](https://www.ncbi.nlm.nih.gov/gene/154807):

> This gene encodes an enzyme important in the vitamin K cycle, which is involved in the carboxylation of glutamate residues present in vitamin K-dependent proteins. The encoded enzyme catalyzes the de-epoxidation of vitamin K 2,3-epoxide. Oxidative stress may upregulate expression of this gene and the encoded protein may protect cells and membrane proteins form oxidative damage. This gene and a related gene (Gene ID: 79001) may have arisen by gene duplication of an ancestral gene. [provided by …

**Accessions** — [HGNC:21492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21492) · Entrez [154807](https://www.ncbi.nlm.nih.gov/gene/154807) · UniProt [Q8N0U8](https://www.uniprot.org/uniprotkb/Q8N0U8) · Ensembl [ENSG00000196715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196715)

## Data

Gene col 12273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12273); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12273]; `tensor/DDL_lfc|DDL_z.npy` [12273]; `embed/gene_vectors.npy` [12273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12273 or target_col == 12273). Every well: [[VKORC1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VKORC1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
