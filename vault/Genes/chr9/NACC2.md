---
symbol: "NACC2"
type: "gene"
col: 7281
ensembl_id: "ENSG00000148411"
name: "NACC family member 2"
location: "9q34.3"
module: 17
arm: "-"
pooled_cpm: 32.31
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NACC2

*NACC family member 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +10.0, q 9e-21, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 2.50×, LoVo 2.61×, LS 180 2.27×, A498 1.77×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 5.84×, J82 3.24×, BT-474 3.85×; ⚠ cell-cycle shift, explains ~68% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.47×, J82 2.78×; ⚠ cell-cycle shift, explains ~33% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.98×, A498 2.50×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.461× (z -13.3, q 1e-37, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNMT3A]] (+0.66, fdr 1e-05), [[SOGA1]] (+0.65, fdr 8e-06), [[JADE3]] (+0.63, fdr 3e-05); moves opposite to [[IFT172]] (-0.60, fdr 3e-05), [[RFC1]] (-0.57, fdr 4e-05), [[NPHP1]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7281.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 2.50×, LoVo 2.61×, LS 180 2.27×, A498 1.77×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 5.84×, J82 3.24×, BT-474 3.85×; ⚠ cell-cycle shift, explains ~68% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.47×, J82 2.78×; ⚠ cell-cycle shift, explains ~33% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.98×, A498 2.50×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +10.0 | 9e-21 | 31/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +4.2 | 0.007 | 19/47 (SNU-423, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.21× | +3.2 | 0.29 | 17/47 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.29 | 12/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.461×** | -13.3 | 1e-37 | 40/48 (A498, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.489×** | -12.3 | 2e-32 | 37/48 (A498, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.567×** | -9.8 | 3e-20 | 34/47 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.586×** | -8.9 | 1e-16 | 28/48 (NCI-H460, RKO, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -8.5 | 2e-15 | 34/48 (NCI-H2030, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.741×** | -7.3 | 3e-11 | 25/48 (NCI-H2030, RKO, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.660×** | -7.2 | 7e-11 | 29/48 (NCI-H460, LOX-IMVI, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.670×** | -6.9 | 4e-10 | 24/42 (RKO, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.672×** | -6.9 | 4e-10 | 31/47 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.723×** | -5.4 | 4e-06 | 18/34 (C32, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.614×** | -4.4 | 6e-04 | 19/45 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -4.0 | 0.003 | 17/48 (RKO, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.803×** | -3.8 | 0.006 | 20/47 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.666×** | -3.7 | 0.010 | 18/46 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.012 | 17/47 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.801×** | -3.5 | 0.018 | 15/48 (LOX-IMVI, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 0.837× | -3.0 | 0.085 | 14/47 (LOX-IMVI, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.7 | 3 (1 ⚠) | 11 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +13.6) | [[Harringtonine (drug)]] 5 µM 0.130× (z -20.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.408× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 27.7 | 0 | 7 (6 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0487× (z -12.1) |
| [[RKO (line)]] | wt | 72.4 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -19.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.364× (z -10.0) |
| [[A498 (line)]] | wt | 64.5 | 2 | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -15.4) |
| [[C32 (line)]] | wt | 35.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.343× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 58.7 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -13.4) |
| [[LoVo (line)]] | wt | 33.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0964× (z -9.2) |
| [[SW480 (line)]] | alt | 39.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -10.2) |
| [[A-172 (line)]] | wt | 52.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.5) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.426× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 31.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HepG2_C3A (line)]] | wt | 41.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +17.5) ⚠ cell-cycle shift, explains ~68% of this change | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -10.8) |
| [[J82 (line)]] | alt | 35.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.9) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[LS 180 (line)]] | wt | 31.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.317× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -11.0) |
| [[PANC-1 (line)]] | alt | 33.1 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.47× (z +11.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 32.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -9.4) |
| [[SNU-423 (line)]] | alt | 25.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 37.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -8.5) |
| [[BT-474 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.3) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.5 µM 0.0658× (z -9.1) |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -9.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT3A]] | +0.66 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SOGA1]] | +0.65 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[JADE3]] | +0.63 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[CCNJ]] | +0.62 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SETD1B]] | +0.61 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[TRIM65]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PHF2]] | +0.59 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TLNRD1]] | +0.59 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[PTPRG]] | +0.59 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[UBTF]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ZBTB8A]] | +0.54 | +0.44 / +0.40 | both halves | 5e-05 | same gene group |
| [[QRICH2]] | +0.54 | +0.33 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.60 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RFC1]] | -0.57 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[NPHP1]] | -0.55 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MAP3K13]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[GALM]] | -0.53 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[DYNC2LI1]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[DYNC2H1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CYB5R4]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NME7]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RADX]] | -0.52 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[POT1]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ACACB]] | -0.51 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-6.2, 11.6); signed map (8.9, -4.4). **Vector** length 96.8, 22.0% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.2 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +0.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -13.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -12.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -8.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -9.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NACC family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,006,537-136,095,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23427, BEND9, BTBD31; previously BTBD14A |
| Gene groups (HGNC) | BEN domain containing; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BF6](https://www.uniprot.org/uniprotkb/Q96BF6) (Nucleus accumbens-associated protein 2):

> Functions as a transcriptional repressor through its association with the NuRD complex. Recruits the NuRD complex to the promoter of MDM2, leading to the repression of MDM2 transcription and subsequent stability of p53/TP53.

**Summary**, from NCBI Gene [138151](https://www.ncbi.nlm.nih.gov/gene/138151):

> Enables several functions, including DNA-binding transcription repressor activity, RNA polymerase II-specific; histone deacetylase binding activity; and protein homodimerization activity. Involved in several processes, including negative regulation of transcription by RNA polymerase II; positive regulation of intrinsic apoptotic signaling pathway in response to DNA damage; and protein homooligomerization. Located in chromatin and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23846) · Entrez [138151](https://www.ncbi.nlm.nih.gov/gene/138151) · UniProt [Q96BF6](https://www.uniprot.org/uniprotkb/Q96BF6) · Ensembl [ENSG00000148411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148411)

## Data

Gene col 7281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7281); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7281]; `tensor/DDL_lfc|DDL_z.npy` [7281]; `embed/gene_vectors.npy` [7281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7281 or target_col == 7281). Every well: [[NACC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NACC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
