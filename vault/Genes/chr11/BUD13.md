---
symbol: "BUD13"
type: "gene"
col: 6044
ensembl_id: "ENSG00000137656"
name: "BUD13 spliceosome associated protein"
location: "11q23.3"
module: 17
arm: "+"
pooled_cpm: 18.98
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# BUD13

*BUD13 spliceosome associated protein* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.93× (z +10.9, q 5e-25, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 2.11×, PANC-1 2.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 4.87×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.28×; ⚠ cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.475× (z -13.9, q 4e-41, down in 24 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.746× (z -5.7, q 3e-06, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AUNIP]] (+0.62, fdr 1e-05), [[ZNF16]] (+0.60, fdr 1e-05), [[PARP2]] (+0.60, fdr 1e-05); moves opposite to [[GLS]] (-0.53, fdr 2e-05), [[LINC01033]] (-0.50, fdr 2e-05), [[SDCBP]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6044.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 2.11×, PANC-1 2.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SW480 4.87×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.28×; ⚠ cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.93×** | +10.9 | 5e-25 | 37/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +7.2 | 2e-10 | 22/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.29×** | +5.0 | 1e-04 | 19/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.4 | 0.002 | 11/28 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.2 | 0.003 | 16/43 (SW 900, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.16× | +4.1 | 0.005 | 18/47 (HepG2/C3A, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.2 | 0.084 | 12/48 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +3.2 | 0.084 | 16/48 (PANC-1, SW480, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -13.9 | 4e-41 | 24/31 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.508×** | -13.1 | 7e-37 | 31/40 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -5.7 | 3e-06 | 22/47 (A-172, HEC-1-A, …) | rises with dose |  |
| [[OTS514 (drug)]] 5 µM |  | **0.576×** | -5.6 | 3e-06 | 22/43 (PANC-1, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -4.9 | 1e-04 | 20/46 (SW48, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -4.7 | 2e-04 | 16/48 (A498, SW1417, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -4.5 | 5e-04 | 18/48 (AN3 CA, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.793×** | -4.5 | 5e-04 | 14/47 (CHP-212, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.780×** | -4.5 | 5e-04 | 12/35 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.732×** | -4.0 | 0.004 | 13/47 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.690×** | -3.8 | 0.009 | 7/45 (SNU-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.6 | 0.013 | 18/48 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.843× | -3.3 | 0.041 | 10/48 (CHP-212, H4, …) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | 0.846× | -3.2 | 0.048 | 10/46 (SW48, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.084 | 11/47 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.2 | 2 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.166× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.242× (z -8.5) |
| [[SW48 (line)]] | wt | 19.1 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0795× (z -12.0) |
| [[SW480 (line)]] | alt | 25.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.87× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -9.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.184× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.53 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.146× (z -11.4) ⚠ transcription drop |
| [[A498 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.103× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0684× (z -18.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.219× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0968× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AUNIP]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PARP2]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[LIN9]] | +0.59 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[ZNF567]] | +0.59 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[TERF1]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SASS6]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[METTL14]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[IMMP1L]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CEP192]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RBL1]] | +0.56 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LINC01033]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SDCBP]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PTPRK]] | -0.48 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[SLIT2]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TBILA]] | -0.47 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[LINC02955]] | -0.47 | -0.46 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-44.1, -55.3); signed map (-43.1, -35.7). **Vector** length 67.0, 10.6% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | -0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +0.8 |
|  | [[Ataluren (drug)]] 0.05 µM |  | +0.9 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | BUD13 spliceosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:116,748,170-116,772,987 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13125, fSAP71, Cwc26 |
| Gene groups (HGNC) | NTC associated proteins; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRD0](https://www.uniprot.org/uniprotkb/Q9BRD0) (BUD13 homolog):

> Involved in pre-mRNA splicing as component of the activated spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs.

**Summary**, from NCBI Gene [84811](https://www.ncbi.nlm.nih.gov/gene/84811):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28199) · Entrez [84811](https://www.ncbi.nlm.nih.gov/gene/84811) · UniProt [Q9BRD0](https://www.uniprot.org/uniprotkb/Q9BRD0) · Ensembl [ENSG00000137656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137656)

## Data

Gene col 6044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6044); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6044]; `tensor/DDL_lfc|DDL_z.npy` [6044]; `embed/gene_vectors.npy` [6044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6044 or target_col == 6044). Every well: [[BUD13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BUD13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
