---
symbol: "MYLK3"
type: "gene"
col: 6449
ensembl_id: "ENSG00000140795"
name: "myosin light chain kinase 3"
location: "16q11.2"
module: 21
arm: "+"
pooled_cpm: 3.0
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MYLK3

*myosin light chain kinase 3* — 16q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.36× (z +24.2, q 0e+00, up in 32 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (A-172 0.0553×); [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM in 1 line (A-172 0.0682×); [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (A-172 0.0807×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COLEC11]] (+0.74, fdr 7e-06), [[ZNF451-AS1]] (+0.73, fdr 1e-05), [[SPATA21]] (+0.69, fdr 9e-06); moves opposite to [[RRP1B]] (-0.57, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.36×** | +24.2 | 0e+00 | 32/33 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.49×** | +16.4 | 0e+00 | 29/34 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.06×** | +9.9 | 5e-21 | 30/41 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +9.4 | 8e-19 | 15/28 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +8.8 | 1e-16 | 21/35 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.45×** | +8.2 | 2e-14 | 26/39 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +6.3 | 2e-08 | 15/46 (NCI-H460, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +6.3 | 3e-08 | 15/33 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +5.8 | 4e-07 | 21/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +5.6 | 2e-06 | 21/47 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +5.1 | 2e-05 | 16/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.9 | 5e-05 | 12/46 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.8 | 6e-05 | 11/47 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +4.7 | 9e-05 | 11/46 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.62×** | +4.7 | 1e-04 | 9/28 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6449.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (A-172 0.0553×); [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM in 1 line (A-172 0.0682×); [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (A-172 0.0807×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | 0.702× | -3.3 | 0.50 | 6/46 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.713× | -3.1 | 0.50 | 8/46 (SW48, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.43 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +8.8) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0553× (z -9.8) |
| [[A498 (line)]] | wt | 3.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.17× (z +10.5) | — |
| [[A549 (line)]] | wt | 4.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 4.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 4.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 3.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +8.5) | — |
| [[A-427 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COLEC11]] | +0.74 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[ZNF451-AS1]] | +0.73 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SPATA21]] | +0.69 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[PPP1R42]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.68 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[MROH8]] | +0.67 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ADCY10]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[UPK2]] | +0.66 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SLC3A1]] | +0.66 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ABHD15-AS1]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[KLF3-AS1]] | +0.65 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TOMM20L-DT]] | +0.65 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.57 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYLK3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[VAMP5]] | B | VAMP5 activity lowers MYLK3's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.69× higher at baseline in the lines without VAMP5 | 0.068 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.5, 24.6); signed map (31.7, 0.2). **Vector** length 49.4, 5.89% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +24.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.9 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +16.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.9 | +4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.6 | +3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.4 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.2 | +5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -0.9 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q11.2 — chr16:46,702,282-46,790,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | caMLCK, MLCK |
| Gene groups (HGNC) | Myosin light chain kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32MK0](https://www.uniprot.org/uniprotkb/Q32MK0) (Myosin light chain kinase 3):

> Kinase that phosphorylates MYL2 in vitro (By similarity). Has been proposed to be calmodulin-dependent, although MYL2 phosphorylation has also been observed in the presence or absence of calmodulin (By similarity). Promotes sarcomere formation in cardiomyocytes and increases cardiomyocyte contractility (By similarity).

**Summary**, from NCBI Gene [91807](https://www.ncbi.nlm.nih.gov/gene/91807):

> Phosphorylation of cardiac myosin heavy chains (see MYH7B, MIM 609928) and light chains (see MYL2, MIM 160781) by a kinase, such as MYLK3, potentiates the force and rate of cross-bridge recruitment in cardiac myocytes (Chan et al., 2008 [PubMed 18202317]).[supplied by OMIM, Jul 2008]

**Accessions** — [HGNC:29826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29826) · Entrez [91807](https://www.ncbi.nlm.nih.gov/gene/91807) · UniProt [Q32MK0](https://www.uniprot.org/uniprotkb/Q32MK0) · Ensembl [ENSG00000140795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140795)

## Data

Gene col 6449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6449); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6449]; `tensor/DDL_lfc|DDL_z.npy` [6449]; `embed/gene_vectors.npy` [6449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6449 or target_col == 6449). Every well: [[MYLK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYLK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
