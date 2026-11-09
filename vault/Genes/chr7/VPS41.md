---
symbol: "VPS41"
type: "gene"
col: 126
ensembl_id: "ENSG00000006715"
name: "VPS41 subunit of HOPS complex"
location: "7p14.1"
module: 122
arm: "+"
pooled_cpm: 137.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# VPS41

*VPS41 subunit of HOPS complex* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.94× (z +5.4, q 3e-05, up in 30 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.565× (z -14.3, q 2e-43, down in 46 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (SNU-423 0.322×, HepG2/C3A 0.272×, SW48 0.275×, LOX-IMVI 0.436×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.115×, NCI-H23 0.333×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1C1]] (+0.68, fdr 7e-06), [[CLN3]] (+0.65, fdr 7e-06), [[VPS8]] (+0.64, fdr 7e-06); moves opposite to [[POLG]] (-0.53, fdr 1e-05), [[MAPKAPK2]] (-0.52, fdr 2e-05), [[C11orf91]] (-0.51, fdr 2e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +5.4 | 3e-05 | 30/49 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 1.19× | +4.4 | 0.003 | 17/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.26×** | +4.2 | 0.005 | 31/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.005 | 23/48 (NCI-H460, A-172, …) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.006 | 24/47 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +3.5 | 0.037 | 27/50 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.5 | 0.037 | 20/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.037 | 26/50 (HEC-1-A, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.041 | 29/49 (BT-474, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.21×** | +3.4 | 0.042 | 22/49 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.11 | 20/48 (AsPC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 126.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (SNU-423 0.322×, HepG2/C3A 0.272×, SW48 0.275×, LOX-IMVI 0.436×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.115×, NCI-H23 0.333×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -14.3 | 2e-43 | 46/49 (SNU-423, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -6.1 | 3e-07 | 38/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.711×** | -5.9 | 7e-07 | 29/44 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.762×** | -4.9 | 1e-04 | 28/49 (NCI-H23, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.757×** | -4.8 | 2e-04 | 30/48 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.770×** | -4.5 | 6e-04 | 27/48 (A549, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.773×** | -4.4 | 7e-04 | 32/50 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **0.782×** | -4.4 | 7e-04 | 27/48 (KATO III, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.769×** | -4.4 | 8e-04 | 25/45 (SW48, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -4.1 | 0.002 | 27/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.808×** | -3.8 | 0.007 | 24/48 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.846× | -3.0 | 0.12 | 17/48 (SW48, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 181 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -17.0) |
| [[SW480 (line)]] | alt | 160 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 169 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 107 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 188 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.333× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[A-172 (line)]] | wt | 135 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 145 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +20.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -13.6) |
| [[A549 (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.4) |
| [[H4 (line)]] | wt | 188 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.5) |
| [[Hs 766T (line)]] | wt | 130 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.8) |
| [[KATO III (line)]] | alt | 203 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.348× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SNU-423 (line)]] | alt | 181 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -17.4) |
| [[A498 (line)]] | wt | 149 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -9.7) |
| [[BT-474 (line)]] | alt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.0) |
| [[C-33 A (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[C32 (line)]] | wt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.6) |
| [[COLO 205 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HepG2_C3A (line)]] | wt | 90.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -17.2) |
| [[HOP62 (line)]] | alt | 77.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -12.8) |
| [[HS-578T (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.0) |
| [[J82 (line)]] | alt | 71.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.6) |
| [[NCI-H2347 (line)]] | alt | 140 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.8) |
| [[RKO (line)]] | wt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 187 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.6) |
| [[SNU-1 (line)]] | wt | 129 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -14.2) |
| [[SW1417 (line)]] | alt | 166 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -13.9) |
| [[A-427 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 247 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 169 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 106 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 98.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1C1]] | +0.68 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[CLN3]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[VPS8]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 | same gene group; STRING 898 |
| [[RRAGB]] | +0.63 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[WASHC2C]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RABGAP1]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SPG21]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.60 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[WASHC5]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[EXOC3]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[GLMP]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ARL8B]] | +0.59 | +0.43 / +0.67 | both halves | 3e-05 | STRING 699 |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLG]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | -0.52 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[C11orf91]] | -0.51 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TLNRD1]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MFSD2A]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[FES]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[GJB2]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[CRK]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SCHIP1]] | -0.50 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[ARPC5L]] | -0.49 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[VPS9D1]] | -0.49 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[LINC02798]] | -0.48 | -0.46 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VPS41's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LOXL1]] | B | LOXL1 activity raises VPS41's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.09× lower at baseline in the lines without LOXL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.7, 13.9); signed map (-10.6, -19.7). **Vector** length 120, 40.9% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +7.1 | +4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +6.4 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.3 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +5.7 | -5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +1.6 |
|  | [[Afatinib (drug)]] 5 µM |  | +3.3 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -14.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.6 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.9 | -4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[AT7519 (drug)]] 5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | VPS41 subunit of HOPS complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:38,722,974-38,932,394 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HVSP41 |
| Gene groups (HGNC) | Ring finger proteins; HOPS complex; RING finger E3 ubiquitin protein ligases |
| Reactome | 5 pathways, smallest: SARS-CoV-2 modulates autophagy; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [P49754](https://www.uniprot.org/uniprotkb/P49754) (Vacuolar protein sorting-associated protein 41 homolog):

> Plays a role in vesicle-mediated protein trafficking to lysosomal compartments including the endocytic membrane transport and autophagic pathways. Acts as a component of the HOPS endosomal tethering complex. This complex is proposed to be involved in the Rab5-to-Rab7 endosome conversion probably implicating MON1A/B, and via binding SNAREs and SNARE complexes to mediate tethering and docking events during SNARE-mediated membrane fusion. The HOPS complex is proposed to be recruited to Rab7 on the …

**Summary**, from NCBI Gene [27072](https://www.ncbi.nlm.nih.gov/gene/27072):

> Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human ortholog of yeast Vps41 protein which is also conserved in Drosophila, tomato, and Arabidopsis. Expression studies in yeast and human indicate that this protein may be involved in the formation and fusion of …

**Accessions** — [HGNC:12713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12713) · Entrez [27072](https://www.ncbi.nlm.nih.gov/gene/27072) · UniProt [P49754](https://www.uniprot.org/uniprotkb/P49754) · Ensembl [ENSG00000006715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006715)

## Data

Gene col 126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 126); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 126]; `tensor/DDL_lfc|DDL_z.npy` [126]; `embed/gene_vectors.npy` [126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 126 or target_col == 126). Every well: [[VPS41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
