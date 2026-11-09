---
symbol: "CDAN1"
type: "gene"
col: 6391
ensembl_id: "ENSG00000140326"
name: "codanin 1"
location: "15q15.2"
module: 3
arm: "+"
pooled_cpm: 8.83
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CDAN1

*codanin 1* — 15q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.71× (z +8.0, q 8e-13, up in 26 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.59× (z +7.0, q 9e-10, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.618× (z -7.0, q 2e-09, down in 9 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.770× (z -3.9, q 0.011, down in 15 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.0861×, KATO III 0.155×, NCI-H1573 0.213×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.256×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.118×; ⚠ toxic; transcription drop); [[Omeprazole (drug)]] 0.5 µM in 1 line (BT-474 0.0938×); [[Radotinib (drug)]] 0.5 µM in 1 line (SNU-1 0.104×); [[Vilanterol (drug)]] 0.5 µM in 1 line (AsPC-1 0.0745×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XYLT2]] (+0.72, fdr 7e-06), [[SLC9A6]] (+0.64, fdr 2e-05), [[MIGA2]] (+0.63, fdr 3e-05); moves opposite to [[KRT8P12]] (-0.58, fdr 1e-05), [[HNRNPC]] (-0.57, fdr 1e-05), [[PARD6G-AS1]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.0 | 8e-13 | 26/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +7.0 | 9e-10 | 24/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +6.6 | 1e-08 | 21/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +6.2 | 7e-08 | 23/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.8 | 1e-06 | 20/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +5.5 | 4e-06 | 22/46 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +5.4 | 6e-06 | 18/44 (COLO 205, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +5.2 | 2e-05 | 17/39 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +5.1 | 3e-05 | 13/41 (KATO III, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.032 | 9/44 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.3 | 0.041 | 9/45 (CFPAC-1, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +3.3 | 0.041 | 12/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.042 | 6/47 (A-427, LoVo, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.33×** | +3.1 | 0.089 | 2/35 (RKO, SHP-77) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6391.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.0861×, KATO III 0.155×, NCI-H1573 0.213×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.256×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.118×; ⚠ toxic; transcription drop); [[Omeprazole (drug)]] 0.5 µM in 1 line (BT-474 0.0938×); [[Radotinib (drug)]] 0.5 µM in 1 line (SNU-1 0.104×); [[Vilanterol (drug)]] 0.5 µM in 1 line (AsPC-1 0.0745×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -7.0 | 2e-09 | 9/17 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.641×** | -6.7 | 5e-09 | 24/37 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.745×** | -4.1 | 0.007 | 11/24 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.770×** | -3.9 | 0.011 | 15/45 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.841× | -3.7 | 0.023 | 13/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -3.6 | 0.031 | 13/48 (SHP-77, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 8.45 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 11.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.87× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 3.30 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0745× (z -8.8) |
| [[BT-474 (line)]] | alt | 7.43 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0938× (z -9.5) |
| [[Hs 766T (line)]] | wt | 5.80 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.116× (z -8.7) |
| [[KATO III (line)]] | alt | 9.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.22 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 8.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0861× (z -17.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.104× (z -8.8) |
| [[SW48 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0832× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XYLT2]] | +0.72 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.64 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[MIGA2]] | +0.63 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[ZNF500]] | +0.63 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[UNC45A]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GIT2]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[E4F1]] | +0.61 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.61 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[FZR1]] | +0.61 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[SMYD4]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT8P12]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPC]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | -0.57 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[YWHAZ]] | -0.57 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[HCG17]] | -0.57 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CCDC200]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ALG13]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[IL6ST]] | -0.55 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[TEX14]] | -0.55 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TUG1]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ANXA5]] | -0.54 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[PHEX]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.9, -5.4); signed map (-36.2, -1.7). **Vector** length 65.2, 10.00% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.6 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | codanin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:42,723,544-42,737,128 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDA-I, CDAI |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWY9](https://www.uniprot.org/uniprotkb/Q8IWY9) (Codanin-1):

> May act as a negative regulator of ASF1 in chromatin assembly.

**Summary**, from NCBI Gene [146059](https://www.ncbi.nlm.nih.gov/gene/146059):

> This gene encodes a protein that appears to play a role in nuclear envelope integrity, possibly related to microtubule attachments. Mutations in this gene cause congenital dyserythropoietic anemia type I, a disease resulting in morphological and functional abnormalities of erythropoiesis. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:1713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1713) · Entrez [146059](https://www.ncbi.nlm.nih.gov/gene/146059) · UniProt [Q8IWY9](https://www.uniprot.org/uniprotkb/Q8IWY9) · Ensembl [ENSG00000140326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140326)

## Data

Gene col 6391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6391); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6391]; `tensor/DDL_lfc|DDL_z.npy` [6391]; `embed/gene_vectors.npy` [6391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6391 or target_col == 6391). Every well: [[CDAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
