---
symbol: "PLEKHM2"
type: "gene"
col: 3839
ensembl_id: "ENSG00000116786"
name: "pleckstrin homology and RUN domain containing M2"
location: "1p36.21"
module: 172
arm: "+"
pooled_cpm: 44.9
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# PLEKHM2

*pleckstrin homology and RUN domain containing M2* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.87× (z +10.9, q 5e-25, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.576× (z -10.9, q 7e-25, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.751× (z -5.6, q 3e-06, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.206×, NCI-H1573 0.161×, KATO III 0.145×, A-172 0.230×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (SNU-423 0.389×, A-172 0.399×, RPMI-7951 0.350×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.183×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC26A11]] (+0.65, fdr 7e-06), [[RAB32]] (+0.65, fdr 7e-06), [[RRAGC]] (+0.64, fdr 7e-06); moves opposite to [[PRKDC]] (-0.59, fdr 1e-05), [[RBBP7]] (-0.59, fdr 1e-05), [[PAICS]] (-0.58, fdr 1e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +10.9 | 5e-25 | 44/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +9.7 | 9e-20 | 39/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.6 | 1e-19 | 29/48 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +9.0 | 2e-17 | 35/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.9 | 6e-10 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.7 | 2e-09 | 30/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +6.1 | 1e-07 | 23/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 8e-07 | 27/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.7 | 8e-07 | 34/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.2 | 1e-05 | 23/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 0.002 | 20/48 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 21/48 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 20/48 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 20/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.006 | 17/47 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.026 | 16/48 (LS 180, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3839.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.206×, NCI-H1573 0.161×, KATO III 0.145×, A-172 0.230×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Panobinostat (drug)]] 5 µM in 3 lines (SNU-423 0.389×, A-172 0.399×, RPMI-7951 0.350×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.183×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.576×** | -10.9 | 7e-25 | 44/48 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.674×** | -7.8 | 2e-12 | 39/48 (SNU-423, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.675×** | -7.7 | 2e-12 | 38/48 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.751×** | -5.6 | 3e-06 | 28/48 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.768×** | -5.0 | 7e-05 | 20/40 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.773×** | -4.9 | 1e-04 | 24/48 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -3.4 | 0.052 | 17/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -3.4 | 0.052 | 14/48 (A-427, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | 0.843× | -3.3 | 0.052 | 19/47 (NCI-H1573, SW1417, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.889× | -3.3 | 0.063 | 16/47 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.2 | 0.063 | 0/49 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.845× | -3.2 | 0.071 | 18/49 (C32, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.1 | 0.077 | 15/48 (SHP-77, SW 1088, …) | rises with dose |  |
| [[Busulfan (drug)]] 5 µM |  | 0.894× | -3.1 | 0.077 | 12/49 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.077 | 12/48 (LS 180, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 45.0 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 39.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A549 (line)]] | wt | 36.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[KATO III (line)]] | alt | 26.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H460 (line)]] | wt | 48.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 88.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.389× (z -10.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 30.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[A498 (line)]] | wt | 42.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.83× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 68.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.183× (z -9.4) |
| [[C32 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -9.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 74.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 58.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.42× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.335× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 45.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 39.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.6) | — |
| [[RKO (line)]] | wt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 94.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A-427 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A11]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[RAB32]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RFNG]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ZNF579]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[IP6K1]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[HPS1]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SLC38A7]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ZNF302]] | +0.61 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ZDHHC1]] | +0.60 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ZNF358]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[EIF3J-DT]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.59 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PAICS]] | -0.58 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RRM2]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RANBP1]] | -0.55 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MAD2L1]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ATP5F1A]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[EIF5A]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[LSM4]] | -0.55 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TMX1]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MCM6]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PKM]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PLEKHM2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HOMER3]] | C | HOMER3 activity raises PLEKHM2's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.5, 13.7); signed map (-6.8, -0.1). **Vector** length 86.1, 19.1% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.8 | +1.4 |
| fall | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.2 | -1.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RUN domain containing M2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:15,684,320-15,734,769 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0842 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; RUN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWE5](https://www.uniprot.org/uniprotkb/Q8IWE5) (Pleckstrin homology domain-containing family M member 2):

> Plays a role in lysosomes movement and localization at the cell periphery acting as an effector of ARL8B. Required for ARL8B to exert its effects on lysosome location, recruits kinesin-1 to lysosomes and hence direct their movement toward microtubule plus ends. Binding to ARL8B provides a link from lysosomal membranes to plus-end-directed motility. Critical factor involved in NK cell-mediated cytotoxicity. Drives the polarization of cytolytic granules and microtubule-organizing centers (MTOCs) …

**Summary**, from NCBI Gene [23207](https://www.ncbi.nlm.nih.gov/gene/23207):

> This gene encodes a protein that binds the plus-end directed microtubule motor protein kinesin, together with the lysosomal GTPase Arl8, and is required for lysosomes to distribute away from the microtubule-organizing center. The encoded protein belongs to the multisubunit BLOC-one-related complex that regulates lysosome positioning. It binds a Salmonella effector protein called Salmonella induced filament A and is a critical host determinant in Salmonella pathogenesis. It has a domain …

**Accessions** — [HGNC:29131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29131) · Entrez [23207](https://www.ncbi.nlm.nih.gov/gene/23207) · UniProt [Q8IWE5](https://www.uniprot.org/uniprotkb/Q8IWE5) · Ensembl [ENSG00000116786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116786)

## Data

Gene col 3839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3839); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3839]; `tensor/DDL_lfc|DDL_z.npy` [3839]; `embed/gene_vectors.npy` [3839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3839 or target_col == 3839). Every well: [[PLEKHM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
