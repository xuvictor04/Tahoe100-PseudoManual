---
symbol: "ERI1"
type: "gene"
col: 2476
ensembl_id: "ENSG00000104626"
name: "exoribonuclease 1"
location: "8p23.1"
module: 6
arm: "+"
pooled_cpm: 39.54
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ERI1

*exoribonuclease 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.17× (z +14.7, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.53× (z +8.1, q 9e-14, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 0.812× (z -4.0, q 0.043, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A-172 0.504×, A-427 0.463×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.289×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.363×; ⚠ cell-cycle shift, explains ~11% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.456×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFC4]] (+0.75, fdr 7e-06), [[DSCC1]] (+0.69, fdr 7e-06), [[RRM2]] (+0.67, fdr 7e-06); moves opposite to [[EIF4EBP3]] (-0.63, fdr 3e-05), [[TCEAL4]] (-0.59, fdr 2e-05), [[ZC2HC1C]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.17×** | +14.7 | 0e+00 | 47/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.14×** | +14.4 | 3e-44 | 46/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.11×** | +14.1 | 4e-43 | 45/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +8.1 | 9e-14 | 39/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.07×** | +7.2 | 8e-11 | 31/49 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +6.5 | 9e-09 | 30/47 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +5.7 | 1e-06 | 29/48 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.22×** | +5.4 | 6e-06 | 24/48 (SW 900, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +5.0 | 5e-05 | 22/48 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.6 | 2e-04 | 21/48 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.27×** | +4.4 | 5e-04 | 19/47 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +4.2 | 0.001 | 22/48 (LS 180, LoVo, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.21×** | +3.5 | 0.018 | 17/47 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.19× | +3.3 | 0.035 | 19/47 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.20×** | +3.3 | 0.035 | 13/47 (HS-578T, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.052 | 13/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.067 | 11/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2476.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A-172 0.504×, A-427 0.463×; ⚠ cell-cycle shift, explains ~22% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.289×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.363×; ⚠ cell-cycle shift, explains ~11% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.456×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.812×** | -4.0 | 0.043 | 19/47 (HepG2/C3A, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **0.828×** | -3.6 | 0.084 | 15/48 (SW 1088, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -3.5 | 0.084 | 15/48 (A-427, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.835× | -3.4 | 0.092 | 15/48 (A-427, A498, …) | all doses, flat |  |
| [[Ixazomib (drug)]] 5 µM |  | 0.721× | -3.2 | 0.13 | 17/48 (H4, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.844× | -3.1 | 0.17 | 12/47 (A-172, HOP62, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.752× | -3.1 | 0.17 | 7/48 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.893× | -3.0 | 0.18 | 9/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 36.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 45.5 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.456× (z -9.4) |
| [[LS 180 (line)]] | wt | 35.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 36.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.504× (z -9.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[C-33 A (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.1) ⚠ cell-cycle shift, explains ~11% of this change |
| [[NCI-H23 (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[A498 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFC4]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RRM2]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[FANCB]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[DDIAS]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[HAUS6]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[RECQL]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LSM4]] | +0.65 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RAD51]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CENPK]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[POLA1]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4EBP3]] | -0.63 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[TCEAL4]] | -0.59 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZC2HC1C]] | -0.58 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[ATF5]] | -0.58 | -0.58 / -0.38 | both halves | 7e-05 | same gene group |
| [[TCEAL1]] | -0.58 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC1]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[NQO1-DT]] | -0.58 | -0.66 / -0.30 | both halves | 2e-04 |  |
| [[RPP25L]] | -0.57 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[ZNF764]] | -0.57 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[CDK3]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.56 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[MYO16]] | -0.56 | -0.61 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.9, -45.3); signed map (-37.2, -41.6). **Vector** length 91.2, 20.3% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of the pre-replicative complex* (reactome, mean cos +0.51 to 22); *Activation of ATR in response to replication stress* (reactome, mean cos +0.53 to 23); *Homology Directed Repair* (reactome, mean cos +0.51 to 32).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.7 | +14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.8 | +14.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.5 | +14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +8.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +6.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +5.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.4 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -7.2 | -2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.5 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | exoribonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:9,002,147-9,116,746 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 3'HEXO; previously THEX1 |
| Gene groups (HGNC) | Exonucleases; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV48](https://www.uniprot.org/uniprotkb/Q8IV48) (3'-5' exoribonuclease 1):

> RNA exonuclease that binds to the 3'-end of histone mRNAs and degrades them, suggesting that it plays an essential role in histone mRNA decay after replication. A 2' and 3'-hydroxyl groups at the last nucleotide of the histone 3'-end is required for efficient 3'-end histone mRNA exonuclease activity and degradation of RNA substrates. Also able to degrade the 3'-overhangs of short interfering RNAs (siRNAs) in vitro, suggesting a possible role as regulator of RNA interference (RNAi). Required for …

**Summary**, from NCBI Gene [90459](https://www.ncbi.nlm.nih.gov/gene/90459):

> Enables 3'-5' exonuclease activity. Involved in maturation of 5.8S rRNA. Located in cytoplasm and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23994) · Entrez [90459](https://www.ncbi.nlm.nih.gov/gene/90459) · UniProt [Q8IV48](https://www.uniprot.org/uniprotkb/Q8IV48) · Ensembl [ENSG00000104626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104626)

## Data

Gene col 2476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2476); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2476]; `tensor/DDL_lfc|DDL_z.npy` [2476]; `embed/gene_vectors.npy` [2476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2476 or target_col == 2476). Every well: [[ERI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
