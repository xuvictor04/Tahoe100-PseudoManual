---
symbol: "PANK2"
type: "gene"
col: 4662
ensembl_id: "ENSG00000125779"
name: "pantothenate kinase 2"
location: "20p13"
module: 142
arm: "+"
pooled_cpm: 69.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# PANK2

*pantothenate kinase 2* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.32× (z +10.7, q 9e-24, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.515× (z -10.9, q 1e-24, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.761× (z -4.7, q 6e-04, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-172 0.172×, A-427 0.153×, A549 0.255×, CFPAC-1 0.249×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.399×, NCI-H23 0.328×, CFPAC-1 0.409×, J82 0.448×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.414×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW 1088 0.0603×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBOX5]] (+0.64, fdr 1e-05), [[KANSL2]] (+0.62, fdr 7e-06), [[ARHGAP1]] (+0.57, fdr 1e-05); moves opposite to [[VPS8]] (-0.51, fdr 2e-05), [[EXPH5]] (-0.49, fdr 4e-05), [[VPS13C]] (-0.49, fdr 3e-05).
> It is in [[Module 142]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.32×** | +10.7 | 9e-24 | 47/49 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.38×** | +7.6 | 6e-12 | 32/49 (NCI-H460, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +7.3 | 7e-11 | 36/48 (A-172, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +6.5 | 1e-08 | 31/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 5e-04 | 28/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.28×** | +4.1 | 0.003 | 24/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +4.0 | 0.006 | 23/48 (LS 180, LoVo, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.006 | 23/49 (J82, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.23×** | +3.5 | 0.032 | 22/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.22×** | +3.3 | 0.064 | 20/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.21×** | +3.2 | 0.074 | 21/48 (LS 180, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-172 0.172×, A-427 0.153×, A549 0.255×, CFPAC-1 0.249×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.399×, NCI-H23 0.328×, CFPAC-1 0.409×, J82 0.448×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.414×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SW 1088 0.0603×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -10.9 | 1e-24 | 31/44 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.546×** | -10.3 | 2e-22 | 40/49 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -4.7 | 6e-04 | 29/48 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.833× | -3.1 | 0.26 | 16/49 (CHP-212, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +12.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.3) | — |
| [[A-172 (line)]] | wt | 90.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 78.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 64.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -14.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 78.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 66.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.94× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -11.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 53.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.70× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 73.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -16.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 98.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -14.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -12.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 70.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -9.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 47.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 107 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.00× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 92.7 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0603× (z -10.0) |
| [[SW48 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 100 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.02× (z +9.7) | — |
| [[A498 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBOX5]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[KANSL2]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | same gene group |
| [[ARHGAP1]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ZNF251]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MED17]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZNF410]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SMPD4BP]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[LENG8-AS1]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SMPD4]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CWF19L1]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[RAB43]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[CERS5]] | +0.51 | +0.33 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS8]] | -0.51 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[EXPH5]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[VPS13C]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[IFT57]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[JUN]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[RFK]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 | pathway: Metabolism of vitamins and cofactors |
| [[RALGAPA1]] | -0.47 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[TBL1X]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ATXN1]] | -0.46 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[MYCBP2]] | -0.44 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[TRAPPC3]] | -0.43 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ZBTB20]] | -0.43 | -0.34 / -0.47 | both halves | 1e-04 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-51.3, 4.9); signed map (-11.0, -13.9). **Vector** length 94.9, 24.3% of its response variance represented; |z| ≥ 3 in 782 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.4 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +7.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | +1.8 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | pantothenate kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,888,839-3,929,887 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSS, FLJ11729, PKAN, HARP; previously C20orf48, NBIA1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Pantothenate kinase family |
| Reactome | 4 pathways, smallest: Coenzyme A biosynthesis; Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZ23](https://www.uniprot.org/uniprotkb/Q9BZ23) (Pantothenate kinase 2, mitochondrial):

> [Isoform 1]: Mitochondrial isoform that catalyzes the phosphorylation of pantothenate to generate 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) synthesis. Required for angiogenic activity of umbilical vein of endothelial cells (HUVEC).; [Isoform 4]: Cytoplasmic isoform that catalyzes the phosphorylation of pantothenate to generate 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) synthesis.

**Summary**, from NCBI Gene [80025](https://www.ncbi.nlm.nih.gov/gene/80025):

> This gene encodes a protein belonging to the pantothenate kinase family and is the only member of that family to be expressed in mitochondria. Pantothenate kinase is a key regulatory enzyme in the biosynthesis of coenzyme A (CoA) in bacteria and mammalian cells. It catalyzes the first committed step in the universal biosynthetic pathway leading to CoA and is itself subject to regulation through feedback inhibition by acyl CoA species. Mutations in this gene are associated with HARP syndrome and …

**Accessions** — [HGNC:15894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15894) · Entrez [80025](https://www.ncbi.nlm.nih.gov/gene/80025) · UniProt [Q9BZ23](https://www.uniprot.org/uniprotkb/Q9BZ23) · Ensembl [ENSG00000125779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125779)

## Data

Gene col 4662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4662); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4662]; `tensor/DDL_lfc|DDL_z.npy` [4662]; `embed/gene_vectors.npy` [4662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4662 or target_col == 4662). Every well: [[PANK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PANK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
