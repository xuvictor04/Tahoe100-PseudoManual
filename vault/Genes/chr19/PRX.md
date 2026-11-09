---
symbol: "PRX"
type: "gene"
col: 2566
ensembl_id: "ENSG00000105227"
name: "periaxin"
location: "19q13.2"
module: 53
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PRX

*periaxin* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.02× (z +22.7, q 0e+00, up in 35 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.5 µM in 1 line (A549 0.0846×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.123×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE9]] (+0.73, fdr 7e-06), [[EFNA2]] (+0.69, fdr 7e-06), [[GDF1]] (+0.68, fdr 7e-06); moves opposite to [[RPE]] (-0.53, fdr 2e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LAG3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.02×** | +22.7 | 0e+00 | 35/37 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.47×** | +13.4 | 3e-38 | 35/42 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.4 | 7e-15 | 20/37 (A549, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +8.0 | 2e-13 | 2/7 (CFPAC-1, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.13×** | +6.6 | 4e-09 | 22/42 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +6.2 | 5e-08 | 17/37 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.1 | 7e-08 | 17/35 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +5.7 | 8e-07 | 26/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **3.12×** | +5.3 | 7e-06 | 16/30 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +5.1 | 2e-05 | 21/47 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.71×** | +4.8 | 9e-05 | 9/24 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 2e-04 | 18/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.005 | 10/39 (SNU-423, A549, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.50×** | +3.6 | 0.014 | 4/23 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +3.5 | 0.016 | 8/39 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.016 | 13/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.5 | 0.016 | 6/46 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[SBI-0640756 (drug)]] 5 µM |  | **2.01×** | +3.3 | 0.034 | 3/29 (A549, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.038 | 7/35 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2566.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.5 µM in 1 line (A549 0.0846×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.123×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.714× | -3.0 | 0.53 | 7/46 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.707× | -3.0 | 0.53 | 13/34 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.3× (z +20.9) | — |
| [[HEC-1-A (line)]] | alt | 5.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 2.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +16.9) | — |
| [[SW480 (line)]] | alt | 3.52 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +12.0) | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -9.4) |
| [[A549 (line)]] | wt | 4.97 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0846× (z -9.5) |
| [[C32 (line)]] | wt | 7.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.2× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 6.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 3.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +14.3) | — |
| [[HT-29 (line)]] | alt | 2.73 | 1 | 0 | [[Auranofin (drug)]] 5 µM 24.2× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 5.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +12.6) | — |
| [[LoVo (line)]] | wt | 5.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +14.3) | — |
| [[LOX-IMVI (line)]] | wt | 6.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 4.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 7.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 5.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 3.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 5.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +12.5) | — |
| [[A-172 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE9]] | +0.73 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[EFNA2]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[GDF1]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[POLG2]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[PYY]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[APC2]] | +0.64 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[ELAVL3]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TINCR]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[HCN2]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | -0.53 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAG3]] | B | LAG3 activity raises PRX's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without LAG3 | 0.025 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises PRX's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without ASGR1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, -16.1); signed map (17.3, 14.2). **Vector** length 67.6, 10.9% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +22.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.8 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.6 | -0.1 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | periaxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,393,766-40,414,793 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1620 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 2 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXM0](https://www.uniprot.org/uniprotkb/Q9BXM0) (Periaxin):

> Scaffolding protein that functions as part of a dystroglycan complex in Schwann cells, and as part of EZR and AHNAK-containing complexes in eye lens fiber cells. Required for the maintenance of the peripheral myelin sheath that is essential for normal transmission of nerve impulses and normal perception of sensory stimuli. Required for normal transport of MBP mRNA from the perinuclear to the paranodal regions. Required for normal remyelination after nerve injury. Required for normal elongation …

**Summary**, from NCBI Gene [57716](https://www.ncbi.nlm.nih.gov/gene/57716):

> This gene encodes a protein involved in peripheral nerve myelin upkeep. The encoded protein contains 2 PDZ domains which were named after PSD95 (post synaptic density protein), DlgA (Drosophila disc large tumor suppressor), and ZO1 (a mammalian tight junction protein). Two alternatively spliced transcript variants have been described for this gene which encode different protein isoforms and which are targeted differently in the Schwann cell. Mutations in this gene cause Charcot-Marie-Tooth …

**Accessions** — [HGNC:13797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13797) · Entrez [57716](https://www.ncbi.nlm.nih.gov/gene/57716) · UniProt [Q9BXM0](https://www.uniprot.org/uniprotkb/Q9BXM0) · Ensembl [ENSG00000105227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105227)

## Data

Gene col 2566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2566); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2566]; `tensor/DDL_lfc|DDL_z.npy` [2566]; `embed/gene_vectors.npy` [2566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2566 or target_col == 2566). Every well: [[PRX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
