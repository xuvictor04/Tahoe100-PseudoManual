---
symbol: "NTRK3"
type: "gene"
col: 6427
ensembl_id: "ENSG00000140538"
name: "neurotrophic receptor tyrosine kinase 3"
location: "15q25.3"
module: 61
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 18
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# NTRK3

*neurotrophic receptor tyrosine kinase 3* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.84× (z +16.2, q 0e+00, up in 7 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.497× (z -4.7, q 0.001, down in 4 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.274×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALT1]] (+0.64, fdr 8e-06), [[SNTG2]] (+0.61, fdr 3e-05), [[FMN2]] (+0.60, fdr 1e-05); moves opposite to [[DZANK1]] (-0.56, fdr 2e-04), [[CEP89]] (-0.54, fdr 6e-05), [[GLE1]] (-0.47, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DSEL]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IL3RA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.84×** | +16.2 | 0e+00 | 7/10 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.47×** | +15.3 | 0e+00 | 4/9 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.54×** | +13.0 | 4e-36 | 12/14 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.90×** | +12.4 | 5e-33 | 2/3 (A549, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.02×** | +11.7 | 2e-29 | 2/5 (A549, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.18×** | +9.6 | 8e-20 | 3/3 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.10×** | +8.2 | 2e-14 | 6/9 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.60×** | +6.9 | 3e-10 | 9/11 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.43×** | +6.4 | 8e-09 | 11/14 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +6.0 | 1e-07 | 6/9 (A498, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.06×** | +5.2 | 8e-06 | 6/12 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.05×** | +5.2 | 1e-05 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.02×** | +5.1 | 2e-05 | 7/11 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +4.7 | 1e-04 | 8/14 (HS-578T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +4.6 | 2e-04 | 4/12 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.001 | 2/14 (A498, HS-578T) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +3.9 | 0.002 | 0/6 | top dose only | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.018 | 2/7 (A549, SNU-423) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.047 | 4/11 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.50×** | +2.9 | 0.073 | 1/8 (HS-578T) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0682×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.274×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.497×** | -4.7 | 0.001 | 4/13 (RPMI-7951, H4, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.582×** | -4.0 | 0.021 | 0/13 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.618× | -3.3 | 0.21 | 2/14 (HS-578T, J82) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.913 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.1× (z +11.2) | — |
| [[A549 (line)]] | wt | 99.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.1) |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.846 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.600 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALT1]] | +0.64 | +0.57 / +0.66 | both halves | 8e-06 |  |
| [[SNTG2]] | +0.61 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[FMN2]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ASIC2]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[LMNTD1]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[ERC2]] | +0.58 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[TMEFF2]] | +0.58 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[NRXN3]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[FSTL5]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 | same gene group |
| [[FAM184A]] | +0.57 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[GALNT9]] | +0.56 | +0.37 / +0.62 | both halves | 9e-05 |  |
| [[LINC00958]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | -0.56 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[CEP89]] | -0.54 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[GLE1]] | -0.47 | -0.26 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSEL]] | B | DSEL activity lowers NTRK3's level | lines that do not express DSEL (16) vs lines expressing it (34) | 1.26× higher at baseline in the lines without DSEL | 0.072 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: HDX, GLRB, AFAP1L1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL3RA]] | B | NTRK3 activity raises IL3RA's level | lines that do not express NTRK3 (32) vs lines expressing it (18) | 1.25× lower at baseline in the lines without NTRK3 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF732, SYNDIG1, LINC00648; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, 28.8); signed map (37.8, 28.8). **Vector** length 22.7, 4.00% of its response variance represented; |z| ≥ 3 in 363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | -0.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | +1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.6 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | neurotrophic receptor tyrosine kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.3 — chr15:87,859,751-88,256,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRKC |
| Gene groups (HGNC) | I-set domain containing; Neurotrophic receptor tyrosine kinase family |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 17 pathways, smallest: Activated NTRK3 signals through PLCG1; NTRK3 as a dependence receptor; Activated NTRK3 signals through PI3K |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16288](https://www.uniprot.org/uniprotkb/Q16288) (NT-3 growth factor receptor):

> Receptor tyrosine kinase involved in nervous system and probably heart development. Upon binding of its ligand NTF3/neurotrophin-3, NTRK3 autophosphorylates and activates different signaling pathways, including the phosphatidylinositol 3-kinase/AKT and the MAPK pathways, that control cell survival and differentiation.

**Summary**, from NCBI Gene [4916](https://www.ncbi.nlm.nih.gov/gene/4916):

> This gene encodes a member of the neurotrophic tyrosine receptor kinase (NTRK) family. This kinase is a membrane-bound receptor that, upon neurotrophin binding, phosphorylates itself and members of the MAPK pathway. Signalling through this kinase leads to cell differentiation and may play a role in the development of proprioceptive neurons that sense body position. Mutations in this gene have been associated with medulloblastomas, secretory breast carcinomas and other cancers. Several …

**Accessions** — [HGNC:8033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8033) · Entrez [4916](https://www.ncbi.nlm.nih.gov/gene/4916) · UniProt [Q16288](https://www.uniprot.org/uniprotkb/Q16288) · Ensembl [ENSG00000140538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140538)

## Data

Gene col 6427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6427); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6427]; `tensor/DDL_lfc|DDL_z.npy` [6427]; `embed/gene_vectors.npy` [6427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6427 or target_col == 6427). Every well: [[NTRK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTRK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
