---
symbol: "HNRNPA0"
type: "gene"
col: 10862
ensembl_id: "ENSG00000177733"
name: "heterogeneous nuclear ribonucleoprotein A0"
location: "5q31.2"
module: 51
arm: "+"
pooled_cpm: 51.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# HNRNPA0

*heterogeneous nuclear ribonucleoprotein A0* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.01× (z +7.4, q 8e-11, up in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.37× (z +3.5, q 0.024, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 3.99×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 3.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HepG2/C3A 3.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.0791×; ⚠ cell-cycle shift, would explain all of this change); [[Tadalafil (drug)]] 5 µM in 1 line (NCI-H661 0.0556×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIR]] (+0.66, fdr 7e-06, ⚠ TRIR in the vector space only through flagged drug-doses), [[NCOA5]] (+0.56, fdr 1e-05), [[ZCCHC3]] (+0.54, fdr 1e-05), [[YTHDF2]] (+0.54, fdr 2e-05); moves opposite to [[EIF2AK1]] (-0.52, fdr 3e-05), [[ACP1]] (-0.50, fdr 6e-05), [[IQGAP1]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10862.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 3.99×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H23 3.13×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HepG2/C3A 3.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +7.4 | 8e-11 | 44/47 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.81×** | +6.5 | 1e-08 | 40/48 (HepG2/C3A, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.81×** | +6.5 | 1e-08 | 39/47 (NCI-H460, NCI-H2030, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.71×** | +5.9 | 4e-07 | 45/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.54×** | +4.6 | 5e-04 | 36/47 (C32, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.52×** | +4.6 | 5e-04 | 36/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.50×** | +4.3 | 0.001 | 27/43 (NCI-H23, A-172, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.45×** | +4.1 | 0.003 | 30/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.50×** | +4.0 | 0.005 | 28/45 (A-172, NCI-H1792, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.40×** | +3.7 | 0.013 | 26/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.024 | 25/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.25×** | +3.5 | 0.024 | 30/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.1 | 0.095 | 22/48 (AsPC-1, SK-MEL-2, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10862.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.0791×; ⚠ cell-cycle shift, would explain all of this change); [[Tadalafil (drug)]] 5 µM in 1 line (NCI-H661 0.0556×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 0.715× | -3.6 | 0.22 | 27/48 (SNU-423, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 89.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -32.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 54.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.99× (z +9.6) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 63.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[NCI-H661 (line)]] | alt | 44.4 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0556× (z -9.4) |
| [[A-172 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 65.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIR]] ⚠ | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[NCOA5]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[YTHDF2]] | +0.54 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[TPRN]] | +0.54 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[KMT2B]] | +0.53 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[STAG1]] | +0.53 | +0.62 / +0.28 | both halves | 3e-04 |  |
| [[IP6K1]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[GPATCH8]] | +0.53 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[ZNF200]] | +0.52 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[NCBP2AS2]] | +0.51 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[LINC00106]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SRSF4]] | +0.51 | +0.46 / +0.38 | both halves | 6e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 450 |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2AK1]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ACP1]] | -0.50 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[IQGAP1]] | -0.48 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SCOC]] | -0.48 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[GNPDA2]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[MPP1]] | -0.47 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[RALB]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[UBQLN1]] | -0.47 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SCP2]] | -0.47 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[CRYZ]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[COPS6]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ATP2C1]] | -0.46 | -0.56 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.379). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-39.1, 7.0); signed map (2.5, -12.1). **Vector** length 72.7, 19.8% of its response variance represented; |z| ≥ 3 in 631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.9 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.6 | +4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.4 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +2.8 | +6.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +1.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -5.6 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -5.4 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -4.7 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein A0 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:137,745,651-137,754,363 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNRPA0 |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 3 pathways, smallest: Dengue Virus-Host Interactions; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13151](https://www.uniprot.org/uniprotkb/Q13151) (Heterogeneous nuclear ribonucleoprotein A0):

> mRNA-binding component of ribonucleosomes. Specifically binds AU-rich element (ARE)-containing mRNAs. Involved in post-transcriptional regulation of cytokines mRNAs.

**Summary**, from NCBI Gene [10949](https://www.ncbi.nlm.nih.gov/gene/10949):

> This gene belongs to the A/B subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins …

**Accessions** — [HGNC:5030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5030) · Entrez [10949](https://www.ncbi.nlm.nih.gov/gene/10949) · UniProt [Q13151](https://www.uniprot.org/uniprotkb/Q13151) · Ensembl [ENSG00000177733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177733)

## Data

Gene col 10862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10862); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10862]; `tensor/DDL_lfc|DDL_z.npy` [10862]; `embed/gene_vectors.npy` [10862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10862 or target_col == 10862). Every well: [[HNRNPA0 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPA0.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
