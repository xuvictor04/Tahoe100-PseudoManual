---
symbol: "PMPCB"
type: "gene"
col: 2669
ensembl_id: "ENSG00000105819"
name: "peptidase, mitochondrial processing subunit beta"
location: "7q22.1"
module: 28
arm: "+"
pooled_cpm: 52.69
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# PMPCB

*peptidase, mitochondrial processing subunit beta* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.78× (z +13.8, q 2e-40, up in 35 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.28× (z +6.0, q 2e-07, up in 31 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.332×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.426×; ⚠ cell-cycle shift, explains ~41% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (RPMI-7951 0.102×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Sonidegib (drug)]] 5 µM in 1 line (SHP-77 0.0928×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW 1271 0.0851×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM204A]] (+0.77, fdr 7e-06), [[NDUFA5]] (+0.71, fdr 7e-06), [[COPS5]] (+0.69, fdr 7e-06); moves opposite to [[PAQR4]] (-0.60, fdr 1e-05), [[GNA12]] (-0.60, fdr 3e-05), [[ZBED4]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +13.8 | 2e-40 | 35/49 (A549, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.43×** | +11.0 | 2e-25 | 32/48 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +10.2 | 6e-22 | 34/45 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.7 | 6e-20 | 31/44 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +7.7 | 2e-12 | 32/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +6.0 | 2e-07 | 31/48 (A-427, NCI-H1573, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.28×** | +5.6 | 2e-06 | 27/48 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +4.7 | 2e-04 | 23/49 (NCI-H1573, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.002 | 20/47 (C32, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +4.1 | 0.002 | 17/47 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 15/48 (HS-578T, NCI-H1573, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | 1.19× | +4.1 | 0.002 | 23/47 (SNU-423, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.18× | +3.9 | 0.004 | 19/48 (KATO III, NCI-H1573, …) | top dose only | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.005 | 13/48 (LoVo, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 14/48 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.061 | 7/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.20×** | +2.9 | 0.082 | 6/48 (NCI-H2347, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.20× | +2.9 | 0.090 | 12/48 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +2.9 | 0.093 | 8/48 (A498, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2669.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.332×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.426×; ⚠ cell-cycle shift, explains ~41% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (RPMI-7951 0.102×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Sonidegib (drug)]] 5 µM in 1 line (SHP-77 0.0928×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW 1271 0.0851×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.873× | -3.1 | 0.74 | 14/47 (A549, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 58.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.1) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 5 µM 0.417× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.2) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A498 (line)]] | wt | 45.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.1) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[KATO III (line)]] | alt | 63.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 66.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 56.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 70.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 47.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.4) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A549 (line)]] | wt | 49.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +11.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +9.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.62× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.332× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.102× (z -10.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 37.9 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0928× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 65.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.9) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SW 1271 (line)]] | alt | 55.2 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0851× (z -8.6) |
| [[A-427 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM204A]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 | STRING 927 |
| [[COPS5]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TCTN1]] | +0.67 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[IFT74]] | +0.67 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC17]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ATRX]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MED12]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CLUAP1]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[CUL5]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.62 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[ETFRF1]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR4]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[GNA12]] | -0.60 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[ZBED4]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[BRI3BP]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[FOXK2]] | -0.58 | -0.70 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP8]] | -0.58 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[TSEN54]] | -0.57 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TMEM104]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SLC27A4]] | -0.57 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[GNB1L]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[LRP8]] | -0.56 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[CPSF4]] | -0.56 | -0.63 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.9, 3.4); signed map (8.5, -25.3). **Vector** length 74.8, 14.5% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.2 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.6 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +10.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | peptidase, mitochondrial processing subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:103,297,407-103,331,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MPPB, MPPP52, MAS1, beta-MPP |
| Gene groups (HGNC) | M16 metallopeptidases |
| Reactome | 5 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O75439](https://www.uniprot.org/uniprotkb/O75439) (Mitochondrial-processing peptidase subunit beta):

> Catalytic subunit of the essential mitochondrial processing protease (MPP), which cleaves the mitochondrial sequence off newly imported precursors proteins (Probable). Preferentially, cleaves after an arginine at position P2 (By similarity). Required for PINK1 turnover by coupling PINK1 mitochondrial import and cleavage, which results in subsequent PINK1 proteolysis.

**Summary**, from NCBI Gene [9512](https://www.ncbi.nlm.nih.gov/gene/9512):

> This gene is a member of the peptidase M16 family and encodes a protein with a zinc-binding motif. This protein is located in the mitochondrial matrix and catalyzes the cleavage of the leader peptides of precursor proteins newly imported into the mitochondria, though it only functions as part of a heterodimeric complex. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9119) · Entrez [9512](https://www.ncbi.nlm.nih.gov/gene/9512) · UniProt [O75439](https://www.uniprot.org/uniprotkb/O75439) · Ensembl [ENSG00000105819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105819)

## Data

Gene col 2669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2669); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2669]; `tensor/DDL_lfc|DDL_z.npy` [2669]; `embed/gene_vectors.npy` [2669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2669 or target_col == 2669). Every well: [[PMPCB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMPCB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
