---
symbol: "KCNRG"
type: "gene"
col: 12615
ensembl_id: "ENSG00000198553"
name: "potassium channel regulator"
location: "13q14.2"
module: 23
arm: "+"
pooled_cpm: 2.26
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# KCNRG

*potassium channel regulator* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.47× (z +9.8, q 1e-19, up in 0 of 0 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.53× (z +6.7, q 3e-09, up in 8 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.576× (z -6.2, q 2e-07, down in 15 of 43 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.468× (z -4.5, q 0.002, down in 9 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0744×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H460 0.0701×); [[5-Azacytidine (drug)]] 0.05 µM in 1 line (HOP62 0.0497×).
> Its strongest partners by |cos| (61 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 39 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC37A3]] (+0.67, fdr 4e-05), [[BAAT]] (+0.65, fdr 1e-05), [[RFX3-DT]] (+0.64, fdr 3e-04); moves opposite to [[DHTKD1]] (-0.60, fdr 5e-05), [[KHDRBS1]] (-0.58, fdr 3e-04), [[GNAI2]] (-0.57, fdr 6e-04).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +9.8 | 1e-19 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +7.0 | 5e-10 | 6/12 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +6.7 | 3e-09 | 8/43 (SW480, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +6.0 | 3e-07 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.5 | 4e-06 | 8/34 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +5.4 | 7e-06 | 9/32 (A498, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.0 | 4e-05 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +4.2 | 0.002 | 2/11 (A-172, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.013 | 3/47 (SW480, NCI-H23, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.018 | 3/35 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.021 | 1/31 (SW48) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.060 | 1/44 (SW48) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.070 | 2/16 (RKO, HT-29) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.080 | 6/23 (COLO 205, SW1417, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.1 | 0.080 | 3/11 (COLO 205, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Berbamine (dihydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.080 | 1/40 (KATO III) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.088 | 4/31 (NCI-H1573, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12615.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LS 180 0.0744×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H460 0.0701×); [[5-Azacytidine (drug)]] 0.05 µM in 1 line (HOP62 0.0497×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.576×** | -6.2 | 2e-07 | 15/43 (C32, RKO, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -4.5 | 0.002 | 9/36 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.735× | -3.4 | 0.11 | 3/43 (Hs 766T, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.744× | -3.4 | 0.11 | 6/43 (SHP-77, HepG2/C3A, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.582× | -3.2 | 0.16 | 4/31 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1.89 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.05 µM 0.0497× (z -9.3) |
| [[LS 180 (line)]] | wt | 4.37 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0744× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 2.18 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0701× (z -9.9) |
| [[A-172 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.824 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 35 of them with an alert (⚠; 35 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC37A3]] | +0.67 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[BAAT]] | +0.65 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[RFX3-DT]] | +0.64 | +0.61 / +0.28 | both halves | 3e-04 |  |
| [[ERMAP]] | +0.64 | +0.62 / +0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[RNF146]] | +0.63 | +0.56 / +0.27 | both halves | 3e-04 |  |
| [[AGBL3]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[RNPC3-DT]] | +0.62 | +0.56 / +0.25 | both halves | 4e-04 |  |
| [[DPH5-DT]] | +0.61 | +0.59 / +0.29 | both halves | 3e-04 |  |
| [[ZNF564]] | +0.61 | +0.62 / +0.26 | both halves | 4e-04 |  |
| [[AMY2B]] | +0.61 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[POLR2M]] | +0.60 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SCYL3]] | +0.60 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[GLIPR1-AS1]] | +0.60 | +0.56 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.60 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[KHDRBS1]] | -0.58 | -0.62 / -0.29 | both halves | 3e-04 |  |
| [[GNAI2]] | -0.57 | -0.44 / -0.21 | both halves | 6e-04 |  |
| [[SLC27A1]] | -0.56 | -0.54 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[KIAA1328]] | -0.55 | -0.49 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[SEPTIN6]] | -0.54 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[METTL26]] | -0.54 | -0.47 / -0.04 | ⚠ not reproduced | 0.006 |  |
| [[GMCL1]] | -0.53 | -0.54 / -0.21 | both halves | 7e-04 | same gene group |
| [[EIF3K]] | -0.52 | -0.39 / -0.21 | both halves | 6e-04 |  |
| [[SLC25A11]] | -0.52 | -0.32 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[MYH10]] | -0.52 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[EFHC1]] | -0.51 | -0.39 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.8, 10.2); signed map (25.3, -10.2). **Vector** length 31.5, 2.43% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.5 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.2 | -4.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -0.7 | -0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -0.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:50,015,254-50,020,922 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5I3](https://www.uniprot.org/uniprotkb/Q8N5I3) (Potassium channel regulatory protein):

> Inhibits potassium fluxes in cells. May regulate Kv1 family channel proteins by retaining a fraction of channels in endomembranes.

**Summary**, from NCBI Gene [283518](https://www.ncbi.nlm.nih.gov/gene/283518):

> This gene encodes a protein which regulates the activity of voltage-gated potassium channels. This gene is on chromosome 13 and overlaps the gene for tripartite motif containing 13 on the same strand. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:18893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18893) · Entrez [283518](https://www.ncbi.nlm.nih.gov/gene/283518) · UniProt [Q8N5I3](https://www.uniprot.org/uniprotkb/Q8N5I3) · Ensembl [ENSG00000198553](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198553)

## Data

Gene col 12615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12615); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12615]; `tensor/DDL_lfc|DDL_z.npy` [12615]; `embed/gene_vectors.npy` [12615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12615 or target_col == 12615). Every well: [[KCNRG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNRG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
