---
symbol: "TUBGCP2"
type: "gene"
col: 5091
ensembl_id: "ENSG00000130640"
name: "tubulin gamma complex component 2"
location: "10q26.3"
module: 30
arm: "+"
pooled_cpm: 58.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TUBGCP2

*tubulin gamma complex component 2* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.51× (z +11.2, q 4e-26, up in 28 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 2.48×, PANC-1 1.90×, A498 2.21×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 2.23×, KATO III 2.34×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.19×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.827× (z -7.4, q 6e-11, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (MIA PaCa-2 0.496×, RPMI-7951 0.443×, CFPAC-1 0.520×, HOP62 0.482×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 0.364×, HOP62 0.446×, SW 900 0.518×, NCI-H1573 0.568×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.344×, A-427 0.435×; ⚠ cell-cycle shift, explains ~0% of this change); [[Carbamazepine (drug)]] 0.5 µM in 1 line (SW 1088 0.0961×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC2]] (+0.59, fdr 3e-05), [[MARF1]] (+0.57, fdr 4e-05), [[USP48]] (+0.54, fdr 3e-05); moves opposite to [[SMAD1]] (-0.57, fdr 1e-04), [[HNF4G]] (-0.54, fdr 1e-04), [[MIER3]] (-0.52, fdr 3e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADAM8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5091.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 2.48×, PANC-1 1.90×, A498 2.21×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 2.23×, KATO III 2.34×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 3.19×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +11.2 | 4e-26 | 28/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.36×** | +8.2 | 6e-14 | 26/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +7.0 | 5e-10 | 25/48 (NCI-H1573, NCI-H2030, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.25×** | +6.3 | 5e-08 | 26/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 1.19× | +4.5 | 8e-04 | 20/45 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.17× | +4.1 | 0.004 | 12/48 (A-172, HOP62, …) | rises with dose | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.15× | +3.8 | 0.010 | 17/48 (NCI-H1573, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5091.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (MIA PaCa-2 0.496×, RPMI-7951 0.443×, CFPAC-1 0.520×, HOP62 0.482×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 0.364×, HOP62 0.446×, SW 900 0.518×, NCI-H1573 0.568×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.344×, A-427 0.435×; ⚠ cell-cycle shift, explains ~0% of this change); [[Carbamazepine (drug)]] 0.5 µM in 1 line (SW 1088 0.0961×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.827×** | -7.4 | 6e-11 | 23/48 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -6.1 | 3e-07 | 20/49 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -5.6 | 3e-06 | 1/49 (NCI-H2122) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -5.4 | 1e-05 | 18/48 (SW1417, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.826×** | -5.1 | 4e-05 | 19/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.879× | -5.0 | 5e-05 | 18/48 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.869× | -5.0 | 6e-05 | 16/48 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.849× | -4.6 | 3e-04 | 14/50 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.848× | -4.6 | 3e-04 | 17/49 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.859× | -4.1 | 0.003 | 16/47 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -4.0 | 0.003 | 20/48 (RPMI-7951, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.892× | -3.9 | 0.005 | 10/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.866× | -3.8 | 0.006 | 19/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.871× | -3.7 | 0.010 | 15/47 (HOP62, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.6 | 0.010 | 16/48 (MIA PaCa-2, RPMI-7951, …) | top dose only | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.868× | -3.6 | 0.011 | 10/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.881× | -3.3 | 0.027 | 10/48 (AsPC-1, LS 180, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.890× | -3.2 | 0.043 | 11/48 (AsPC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 0.894× | -3.1 | 0.059 | 4/49 (KATO III, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 84.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 86.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.8) |
| [[RKO (line)]] | wt | 48.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +15.5) | — |
| [[A-427 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 91.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 81.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 54.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | — |
| [[LoVo (line)]] | wt | 44.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.07× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 77.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 98.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | — |
| [[PANC-1 (line)]] | alt | 64.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 94.4 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0961× (z -9.2) |
| [[SW 900 (line)]] | alt | 88.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.3) |
| [[A-172 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 55.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC2]] | +0.59 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[MARF1]] | +0.57 | +0.69 / +0.43 | both halves | 4e-05 |  |
| [[USP48]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[PDZD11]] | +0.53 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[EFHC1]] | +0.50 | +0.38 / +0.22 | both halves | 6e-04 |  |
| [[POLR2G]] ⚠ | +0.50 | +0.29 / +0.27 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ECI2]] | +0.50 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[WDR54]] | +0.49 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[ARPC1A]] | +0.49 | +0.61 / +0.26 | both halves | 4e-04 |  |
| [[CETN2]] | +0.49 | +0.35 / +0.35 | both halves | 1e-04 | pathway: Centrosome maturation |
| [[F11R]] | +0.49 | +0.46 / +0.28 | both halves | 3e-04 |  |
| [[ZNF511]] | +0.49 | +0.53 / +0.29 | both halves | 3e-04 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MRI1]] | +0.48 | +0.31 / +0.23 | both halves | 5e-04 |  |
| [[GLG1]] | +0.48 | +0.54 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD1]] | -0.57 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[HNF4G]] | -0.54 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MIER3]] | -0.52 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[BAZ1A]] | -0.50 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[ZNF747]] | -0.49 | -0.52 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[DPY19L1P2]] | -0.49 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[ARAP2]] | -0.48 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[PHACTR2]] | -0.48 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[CCSER1]] | -0.48 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[RARRES1]] | -0.48 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[PTPRK]] | -0.48 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[HDX]] | -0.47 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[JADE3]] | -0.47 | -0.52 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM8]] | B | ADAM8 activity raises TUBGCP2's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.56× lower at baseline in the lines without ADAM8 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[RAC2]] | B | RAC2 activity raises TUBGCP2's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without RAC2 | 0.066 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.353). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (13.3, -23.7); signed map (-38.7, 12.7). **Vector** length 85.2, 16.7% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | +3.5 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.8 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.5 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.6 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | tubulin gamma complex component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,278,635-133,318,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCP2, Spc97p, SPBC97, hGCP2, ALP4 |
| Gene groups (HGNC) | Tubulin gamma complex component family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSJ2](https://www.uniprot.org/uniprotkb/Q9BSJ2) (Gamma-tubulin complex component 2):

> Component of the gamma-tubulin ring complex (gTuRC) which mediates microtubule nucleation. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation. Plays a role in neuronal migration.

**Summary**, from NCBI Gene [10844](https://www.ncbi.nlm.nih.gov/gene/10844):

> Predicted to enable gamma-tubulin binding activity. Predicted to contribute to microtubule minus-end binding activity. Involved in brain development and neuron migration. Located in centrosome. Implicated in pachygyria, microcephaly, developmental delay, and dysmorphic facies, with or without seizures. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18599) · Entrez [10844](https://www.ncbi.nlm.nih.gov/gene/10844) · UniProt [Q9BSJ2](https://www.uniprot.org/uniprotkb/Q9BSJ2) · Ensembl [ENSG00000130640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130640)

## Data

Gene col 5091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5091); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5091]; `tensor/DDL_lfc|DDL_z.npy` [5091]; `embed/gene_vectors.npy` [5091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5091 or target_col == 5091). Every well: [[TUBGCP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBGCP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
