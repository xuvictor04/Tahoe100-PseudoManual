---
symbol: "UQCRQ"
type: "gene"
col: 8944
ensembl_id: "ENSG00000164405"
name: "ubiquinol-cytochrome c reductase complex III subunit VII"
location: "5q31.1"
module: 48
arm: "+"
pooled_cpm: 71.07
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# UQCRQ

*ubiquinol-cytochrome c reductase complex III subunit VII* — 5q31.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.84× (z +8.0, q 8e-13, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HOP62 8.61×, NCI-H460 7.66×, NCI-H1573 8.42×, NCI-H1792 9.63×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 7.07×, NCI-H1573 7.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 4.70×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.126×); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.0602×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROMO1]] (+0.92, fdr 7e-06), [[COX6C]] (+0.87, fdr 7e-06), [[UQCR11]] (+0.86, fdr 7e-06); moves opposite to [[TEX261]] (-0.62, fdr 4e-05), [[ZNF460]] (-0.62, fdr 5e-05), [[ATN1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8944.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (HOP62 8.61×, NCI-H460 7.66×, NCI-H1573 8.42×, NCI-H1792 9.63×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 7.07×, NCI-H1573 7.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 4.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **4.84×** | +8.0 | 8e-13 | 48/49 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **3.50×** | +6.4 | 4e-08 | 39/42 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +4.9 | 2e-04 | 45/47 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.58×** | +4.7 | 4e-04 | 42/45 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.32×** | +4.5 | 8e-04 | 43/48 (SW48, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **2.01×** | +3.7 | 0.019 | 41/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.95×** | +3.6 | 0.027 | 45/48 (COLO 205, HOP62, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.57×** | +3.4 | 0.042 | 34/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.82× | +3.1 | 0.13 | 41/48 (NCI-H2030, J82, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.49× | +3.0 | 0.15 | 43/48 (CHP-212, NCI-H661, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8944.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.126×); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.0602×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.640× | -3.3 | 0.39 | 33/48 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.319× | -3.2 | 0.39 | 40/49 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 51.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H1573 (line)]] | alt | 52.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 1 | 1 | [[Fulvestrant (drug)]] 5 µM 4.70× (z +8.9) | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.126× (z -10.7) |
| [[CHP-212 (line)]] | wt | 53.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0602× (z -9.1) |
| [[HOP62 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.61× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[LS 180 (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.01× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H1792 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.63× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H460 (line)]] | wt | 72.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A-172 (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 16 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROMO1]] | +0.92 | +0.85 / +0.93 | both halves | 7e-06 | STRING 755 |
| [[COX6C]] | +0.87 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[UQCR11]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999 |
| [[UBL5]] | +0.86 | +0.78 / +0.86 | both halves | 7e-06 | STRING 508 |
| [[COX6A1]] | +0.86 | +0.77 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 996 |
| [[COX6B1]] | +0.84 | +0.68 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[ATP5PD]] | +0.83 | +0.66 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 967 |
| [[ATP5MK]] | +0.83 | +0.69 / +0.84 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 898 |
| [[COX7C]] | +0.82 | +0.73 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFB11]] ⚠ | +0.81 | +0.75 / +0.82 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 979; ⚠ in the vector space only through flagged drug-doses |
| [[SPCS1]] | +0.81 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[NDUFA4]] | +0.81 | +0.71 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 980 |
| [[ATP5F1E]] | +0.81 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 863 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX261]] | -0.62 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[ZNF460]] | -0.62 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[ATN1]] | -0.60 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SRSF6]] | -0.60 | -0.46 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.923). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-46.4, -22.1); signed map (-34.9, 9.4). **Vector** length 65.0, 31.1% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex IV assembly* (reactome, mean cos +0.74 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.79 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.77 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +2.9 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | -0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[Allantoin (drug)]] 0.5 µM |  | +0.9 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +0.9 | +0.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -6.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | -5.9 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -5.7 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.0 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase complex III subunit VII |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,866,630-132,868,847 (+) |
| Ensembl biotype | protein_coding |
| Also known as | QP-C, QCR8, UQCR7 |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Complex III assembly; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O14949](https://www.uniprot.org/uniprotkb/O14949) (Cytochrome b-c1 complex subunit 8):

> Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular …

**Summary**, from NCBI Gene [27089](https://www.ncbi.nlm.nih.gov/gene/27089):

> This gene encodes a ubiquinone-binding protein of low molecular mass. This protein is a small core-associated protein and a subunit of ubiquinol-cytochrome c reductase complex III, which is part of the mitochondrial respiratory chain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29594) · Entrez [27089](https://www.ncbi.nlm.nih.gov/gene/27089) · UniProt [O14949](https://www.uniprot.org/uniprotkb/O14949) · Ensembl [ENSG00000164405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164405)

## Data

Gene col 8944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8944); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8944]; `tensor/DDL_lfc|DDL_z.npy` [8944]; `embed/gene_vectors.npy` [8944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8944 or target_col == 8944). Every well: [[UQCRQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCRQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
