---
symbol: "TYK2"
type: "gene"
col: 2596
ensembl_id: "ENSG00000105397"
name: "tyrosine kinase 2"
location: "19p13.2"
module: 60
arm: "-"
pooled_cpm: 29.97
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# TYK2

*tyrosine kinase 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +16.0, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.717× (z -5.7, q 6e-06, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.125×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.139×; ⚠ transcription drop; cell-cycle shift, explains ~3% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 0.286×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D10A]] (+0.65, fdr 7e-06), [[MGRN1]] (+0.60, fdr 3e-05), [[YY1AP1]] (+0.58, fdr 1e-05); moves opposite to [[CCT5]] (-0.58, fdr 1e-05), [[CCT4]] (-0.58, fdr 1e-05), [[GCLM]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +16.0 | 0e+00 | 44/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +8.3 | 2e-14 | 33/48 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +6.7 | 3e-09 | 32/48 (A-172, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +6.3 | 5e-08 | 29/48 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +6.0 | 2e-07 | 27/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +5.2 | 2e-05 | 24/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.9 | 8e-05 | 23/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +4.9 | 8e-05 | 21/48 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 2e-04 | 21/47 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.006 | 18/47 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.1 | 0.089 | 6/31 (A-172, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (H4 0.125×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.139×; ⚠ transcription drop; cell-cycle shift, explains ~3% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AsPC-1 0.286×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -5.7 | 6e-06 | 25/48 (NCI-H2347, A498, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.7 | 7e-04 | 3/48 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -3.3 | 0.19 | 14/48 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.830× | -3.2 | 0.19 | 11/48 (A498, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 42.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +18.2) | — |
| [[PANC-1 (line)]] | alt | 23.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +17.9) | — |
| [[H4 (line)]] | wt | 27.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -9.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +17.2) | — |
| [[A549 (line)]] | wt | 23.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 25.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -9.4) |
| [[HS-578T (line)]] | alt | 80.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.98× (z +8.6) | — |
| [[LoVo (line)]] | wt | 16.7 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.91× (z +11.7) | — |
| [[SW48 (line)]] | wt | 28.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.108× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.9) | — |
| [[J82 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 44.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 31.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.9) | — |
| [[A498 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D10A]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MGRN1]] | +0.60 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[YY1AP1]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[XRCC1]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ACAP3]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[STARD10]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[FAM110A]] | +0.53 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[ICAM5]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TMEM63B]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ICAM3]] | +0.52 | +0.60 / +0.44 | both halves | 3e-05 | ⚠ same locus (10.9 kb, same strand: neighbours can correlate without regulation) |
| [[MTMR4]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[NBPF19]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CCT4]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[GCLM]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CDC42BPA]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[TXNRD1]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | -0.55 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TXN]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CCT3]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[HSPD1]] | -0.53 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ATXN7L3B]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PTGES3]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 | pathway: Potential therapeutics for SARS |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-13.8, -27.1); signed map (-10.0, 4.4). **Vector** length 88.3, 19.5% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +16.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.1 | +2.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.7 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.3 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,350,533-10,380,608 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JTK1 |
| Gene groups (HGNC) | FERM domain containing; Jak family tyrosine kinases |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 41 pathways, smallest: Interleukin-23 signaling; MAPK1 (ERK2) activation; Interleukin-27 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P29597](https://www.uniprot.org/uniprotkb/P29597) (Non-receptor tyrosine-protein kinase TYK2):

> Non-membrane spanning protein tyrosine kinase involved in numerous cytokines and interferons signaling, which regulates cell growth, development, cell migration, innate and adaptive immunity. Plays both structural and catalytic roles in numerous interleukins and interferons (IFN-alpha/beta) signaling. Associates with heterodimeric cytokine receptor complexes and activates STAT family members including STAT1, STAT3, STAT4 or STAT6. The heterodimeric cytokine receptor complexes are composed of …

**Summary**, from NCBI Gene [7297](https://www.ncbi.nlm.nih.gov/gene/7297):

> This gene encodes a member of the tyrosine kinase and, more specifically, the Janus kinases (JAKs) protein families. This protein associates with the cytoplasmic domain of type I and type II cytokine receptors and promulgate cytokine signals by phosphorylating receptor subunits. It is also a component of both the type I and type III interferon signaling pathways. As such, it may play a role in anti-viral immunity. A mutation in this gene has been associated with Immunodeficiency 35. [provided …

**Accessions** — [HGNC:12440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12440) · Entrez [7297](https://www.ncbi.nlm.nih.gov/gene/7297) · UniProt [P29597](https://www.uniprot.org/uniprotkb/P29597) · Ensembl [ENSG00000105397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105397)

## Data

Gene col 2596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2596); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2596]; `tensor/DDL_lfc|DDL_z.npy` [2596]; `embed/gene_vectors.npy` [2596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2596 or target_col == 2596). Every well: [[TYK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
