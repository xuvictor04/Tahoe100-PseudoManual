---
symbol: "EMC9"
type: "gene"
col: 2041
ensembl_id: "ENSG00000100908"
name: "ER membrane protein complex subunit 9"
location: "14q12"
module: 12
arm: "+"
pooled_cpm: 6.03
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# EMC9

*ER membrane protein complex subunit 9* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +15.3, q 0e+00, up in 38 of 40 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +6.5, q 1e-08, up in 28 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (PANC-1 4.46×, CFPAC-1 4.95×, A498 4.60×, SW1417 4.99×, …; ⚠ cell-cycle shift, explains ~43% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 6.13×; ⚠ cell-cycle shift, explains ~34% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (HCT15 0.0617×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK16]] (+0.69, fdr 7e-06), [[DNAL4]] (+0.67, fdr 7e-06), [[FBXO48]] (+0.66, fdr 7e-06); moves opposite to [[NUTF2]] (-0.60, fdr 7e-06), [[RPUSD4]] (-0.60, fdr 1e-05), [[UBE2G2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2041.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 12 lines (PANC-1 4.46×, CFPAC-1 4.95×, A498 4.60×, SW1417 4.99×, …; ⚠ cell-cycle shift, explains ~43% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 6.13×; ⚠ cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **3.36×** | +15.3 | 0e+00 | 38/40 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **3.77×** | +11.4 | 1e-27 | 43/45 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.52×** | +8.3 | 3e-14 | 33/39 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **2.10×** | +6.6 | 5e-09 | 24/34 (SW1417, J82, …) | all doses, flat | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.5 | 1e-08 | 28/41 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.95×** | +6.0 | 3e-07 | 27/46 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.89×** | +5.5 | 3e-06 | 7/11 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.75×** | +5.0 | 4e-05 | 23/47 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +4.5 | 3e-04 | 23/47 (SW1417, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.64×** | +4.4 | 5e-04 | 15/28 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.59×** | +3.8 | 0.009 | 7/16 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.23×** | +3.7 | 0.009 | 9/44 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.51×** | +3.7 | 0.010 | 17/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.028 | 13/32 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.061 | 12/40 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2041.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (HCT15 0.0617×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dabrafenib (drug)]] 5 µM |  | 0.521× | -3.0 | 0.96 | 3/48 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.17 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +11.3) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A498 (line)]] | wt | 5.13 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +10.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A549 (line)]] | wt | 7.15 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +8.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[CFPAC-1 (line)]] | alt | 9.39 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +10.9) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HCT15 (line)]] | alt | 9.79 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0617× (z -9.7) |
| [[J82 (line)]] | alt | 9.71 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 3.27 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +9.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.0) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2347 (line)]] | alt | 9.22 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.32 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +8.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[Panc 03.27 (line)]] | alt | 9.19 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +9.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SNU-423 (line)]] | alt | 4.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +8.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW1417 (line)]] | alt | 7.48 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +10.0) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK16]] | +0.69 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[FBXO48]] | +0.66 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[TRAFD1]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TIMM17B]] ⚠ | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[LENG1]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[METTL25B]] | +0.64 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[MED19]] | +0.64 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[SNAPIN]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PRR14]] | +0.63 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.62 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[AMZ2P1-1]] | +0.62 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[KMT2A]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTF2]] | -0.60 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[RPUSD4]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.58 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[PPT1]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[C1orf216]] | -0.56 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.56 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[AHSA1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ADAT2]] | -0.54 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[HACD3]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.4, 1.1); signed map (0.3, -14.1). **Vector** length 60.8, 10.5% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +7.3 | +15.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.6 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.2 | +8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | +6.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | +2.7 | +6.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,138,959-24,141,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-112; previously C14orf122, FAM158A |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3B6](https://www.uniprot.org/uniprotkb/Q9Y3B6) (ER membrane protein complex subunit 9):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [51016](https://www.ncbi.nlm.nih.gov/gene/51016):

> Contributes to membrane insertase activity. Involved in protein insertion into ER membrane by stop-transfer membrane-anchor sequence and tail-anchored membrane protein insertion into ER membrane. Located in cytoplasm. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20273) · Entrez [51016](https://www.ncbi.nlm.nih.gov/gene/51016) · UniProt [Q9Y3B6](https://www.uniprot.org/uniprotkb/Q9Y3B6) · Ensembl [ENSG00000100908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100908)

## Data

Gene col 2041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2041); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2041]; `tensor/DDL_lfc|DDL_z.npy` [2041]; `embed/gene_vectors.npy` [2041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2041 or target_col == 2041). Every well: [[EMC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
