---
symbol: "FTSJ1"
type: "gene"
col: 892
ensembl_id: "ENSG00000068438"
name: "FtsJ RNA 2'-O-methyltransferase 1"
location: "Xp11.23"
module: 52
arm: "+"
pooled_cpm: 20.73
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# FTSJ1

*FtsJ RNA 2'-O-methyltransferase 1* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.40× (z +9.6, q 5e-19, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.481× (z -15.5, q 0e+00, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC59]] (+0.64, fdr 7e-06), [[MSTO2P]] (+0.63, fdr 1e-05), [[TUBGCP6]] (+0.58, fdr 1e-05); moves opposite to [[LRCH3]] (-0.60, fdr 1e-05), [[WBP4]] (-0.55, fdr 2e-05), [[STXBP3]] (-0.54, fdr 8e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.40×** | +9.6 | 5e-19 | 39/45 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +8.0 | 3e-13 | 37/48 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +8.0 | 3e-13 | 34/48 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.9 | 1e-04 | 19/37 (SNU-423, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.7 | 3e-04 | 0/48 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.5 | 6e-04 | 14/31 (LS 180, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.481×** | -15.5 | 0e+00 | 37/46 (AsPC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.607×** | -10.5 | 2e-23 | 35/47 (SK-MEL-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.633×** | -6.8 | 2e-09 | 22/48 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -6.7 | 3e-09 | 27/46 (SW48, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -5.9 | 4e-07 | 26/48 (A-427, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.688×** | -5.4 | 7e-06 | 24/48 (SNU-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -5.2 | 1e-05 | 20/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.713×** | -5.1 | 3e-05 | 17/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.739×** | -4.5 | 4e-04 | 21/48 (SW 900, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.753×** | -4.2 | 0.001 | 19/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.768×** | -3.8 | 0.008 | 17/45 (SNU-423, AsPC-1, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.813×** | -3.7 | 0.011 | 11/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.014 | 19/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.841× | -3.6 | 0.014 | 16/48 (SW480, LS 180, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -3.5 | 0.015 | 17/48 (A-427, SW1417, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.843× | -3.5 | 0.018 | 12/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 31.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -16.0) |
| [[Hs 766T (line)]] | wt | 44.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -12.8) |
| [[A-427 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -8.8) |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 23.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -13.6) |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.9) |
| [[KATO III (line)]] | alt | 28.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -13.0) |
| [[LoVo (line)]] | wt | 16.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -8.5) |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 25.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.7) |
| [[RKO (line)]] | wt | 14.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -11.0) |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.139× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.0) |
| [[SW1417 (line)]] | alt | 41.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -11.4) |
| [[SW48 (line)]] | wt | 17.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0844× (z -10.6) |
| [[SW480 (line)]] | alt | 39.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.6) |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC59]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MSTO2P]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ATAD3A]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[YKT6]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[GCN1]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NOP9]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SEC61A1]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[B4GALT7]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[TBL3]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 | STRING 413 |
| [[ATAD3B]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[GAK]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRCH3]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[WBP4]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[STXBP3]] | -0.54 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[UBXN2A]] | -0.53 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[NDUFC1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[EIF1]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.53 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[EIF1B]] | -0.53 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[RNASEK]] | -0.51 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ZC3H6]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[NCOA1]] | -0.51 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[UNK]] | -0.51 | -0.54 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.7, -29.0); signed map (-53.7, 2.4). **Vector** length 80.2, 15.2% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.6 | -0.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -15.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.1 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | FtsJ RNA 2'-O-methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,476,021-48,486,364 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JM23, CDLIV, SPB1, TRM7, TRMT7; previously MRX9, MRX44 |
| Gene groups (HGNC) | 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UET6](https://www.uniprot.org/uniprotkb/Q9UET6) (tRNA):

> Methylates the 2'-O-ribose of nucleotides at positions 32 and 34 of the tRNA anticodon loop of substrate tRNAs. Requisite for faithful cytoplasmic translation. Requires THADA for methylation of the nucleotide at position 32 of the anticodon loop of substrate tRNAs. Requires WDR6 for methylation of the nucleotide at position 34 of the anticodon loop of substrate tRNAs. Promotes translation efficiency of the UUU codon. Plays a role in neurogenesis. Required for expression of genes involved in …

**Summary**, from NCBI Gene [24140](https://www.ncbi.nlm.nih.gov/gene/24140):

> This gene encodes a member of the methyltransferase superfamily. The encoded protein localizes to the nucleolus, binds to S-adenosylmethionine, and may be involved in the processing and modification of ribosomal RNA. Mutations in this gene are associated with cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:13254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13254) · Entrez [24140](https://www.ncbi.nlm.nih.gov/gene/24140) · UniProt [Q9UET6](https://www.uniprot.org/uniprotkb/Q9UET6) · Ensembl [ENSG00000068438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068438)

## Data

Gene col 892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 892); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 892]; `tensor/DDL_lfc|DDL_z.npy` [892]; `embed/gene_vectors.npy` [892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 892 or target_col == 892). Every well: [[FTSJ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FTSJ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
