---
symbol: "CORO7"
type: "gene"
col: 15383
ensembl_id: "ENSG00000262246"
name: "coronin 7"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 16.34
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CORO7

*coronin 7* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.05× (z +20.4, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.739× (z -6.9, q 4e-09, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.244×, SNU-1 0.162×, MIA PaCa-2 0.267×, LOX-IMVI 0.361×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.0516×; ⚠ cell-cycle shift, explains ~35% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (SHP-77 0.0808×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.196×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0922×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPST2]] (+0.70, fdr 1e-05), [[ANKRD27]] (+0.70, fdr 8e-06), [[LIMK1]] (+0.69, fdr 7e-06); moves opposite to [[FUNDC1]] (-0.75, fdr 7e-06), [[UBQLN2]] (-0.69, fdr 7e-06), [[NDUFA5]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.05×** | +20.4 | 0e+00 | 45/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +18.6 | 0e+00 | 45/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +17.1 | 0e+00 | 44/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.5 | 4e-19 | 33/47 (NCI-H2030, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +9.2 | 3e-18 | 36/45 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +9.2 | 4e-18 | 32/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.2 | 1e-14 | 25/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 6e-07 | 23/47 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.1 | 2e-05 | 20/47 (PANC-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +5.0 | 4e-05 | 15/47 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 8e-05 | 15/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.30×** | +4.8 | 8e-05 | 16/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.7 | 1e-04 | 15/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.4 | 4e-04 | 14/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.002 | 9/43 (LS 180, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.003 | 12/47 (SW480, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.005 | 12/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.011 | 12/48 (NCI-H2347, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15383.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.244×, SNU-1 0.162×, MIA PaCa-2 0.267×, LOX-IMVI 0.361×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.0516×; ⚠ cell-cycle shift, explains ~35% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (SHP-77 0.0808×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C32 0.196×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0922×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.739×** | -6.9 | 4e-09 | 23/48 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.723×** | -6.0 | 8e-07 | 21/46 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.771×** | -4.6 | 8e-04 | 18/46 (NCI-H23, BT-474, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.627×** | -4.5 | 0.001 | 12/44 (NCI-H23, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.842× | -3.2 | 0.18 | 12/47 (A498, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 17.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +10.1) | — |
| [[KATO III (line)]] | alt | 18.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +11.3) | — |
| [[LoVo (line)]] | wt | 12.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +11.4) | — |
| [[SW480 (line)]] | alt | 13.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 19.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 16.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 12.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.08× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 13.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.196× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 23.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 8.08 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0922× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0516× (z -17.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0808× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -10.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 14.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +8.5) | — |
| [[A-172 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.70 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[LIMK1]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PACS2]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[AXIN1]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[GRK6]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TCF3]] | +0.68 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.67 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SMG1P5]] | +0.67 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[ST6GALNAC6]] | +0.67 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SLC27A4]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SFI1]] | +0.66 | +0.65 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUNDC1]] | -0.75 | -0.74 / -0.60 | both halves | 7e-06 |  |
| [[UBQLN2]] | -0.69 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[NDUFA5]] | -0.68 | -0.77 / -0.61 | both halves | 7e-06 |  |
| [[BCLAF1]] | -0.67 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[AASDHPPT]] | -0.67 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.67 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[RBM7]] | -0.65 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CLK4]] | -0.64 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.63 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H11A]] | -0.63 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[FAM200A]] | -0.63 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[TIA1]] | -0.62 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (0.8, 0.3); signed map (-43.7, -5.4). **Vector** length 85.7, 16.8% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.1 | +17.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +20.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +18.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +9.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.4 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.0 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.4 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | coronin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,354,542-4,425,705 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22021, POD1 |
| Gene groups (HGNC) | WD repeat domain containing; Coronins |
| Matched by | ensembl_id |

**Function**, from UniProt [P57737](https://www.uniprot.org/uniprotkb/P57737) (Coronin-7):

> F-actin regulator involved in anterograde Golgi to endosome transport: upon ubiquitination via 'Lys-33'-linked ubiquitin chains by the BCR(KLHL20) E3 ubiquitin ligase complex, interacts with EPS15 and localizes to the trans-Golgi network, where it promotes actin polymerization, thereby facilitating post-Golgi trafficking. May play a role in the maintenance of the Golgi apparatus morphology.

**Summary**, from NCBI Gene [79585](https://www.ncbi.nlm.nih.gov/gene/79585):

> This gene encodes a member of the coronin protein family. However, unlike other coronin proteins, it is not an actin-binding protein but rather functions as an F-actin regulator directing anterograde Golgi to endosome transport. The encoded protein has two tandem WD-40 domain repeats and localizes to the trans-Golgi network. The protein undergoes K33-linked polyubiquitination via an E3 ligase complex. It is thought to play an essential role in maintenance of Golgi apparatus morphology. …

**Accessions** — [HGNC:26161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26161) · Entrez [79585](https://www.ncbi.nlm.nih.gov/gene/79585) · UniProt [P57737](https://www.uniprot.org/uniprotkb/P57737) · Ensembl [ENSG00000262246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000262246)

## Data

Gene col 15383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15383); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15383]; `tensor/DDL_lfc|DDL_z.npy` [15383]; `embed/gene_vectors.npy` [15383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15383 or target_col == 15383). Every well: [[CORO7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CORO7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
