---
symbol: "HAUS7"
type: "gene"
col: 13102
ensembl_id: "ENSG00000213397"
name: "HAUS augmin like complex subunit 7"
location: "Xq28"
module: 33
arm: "+"
pooled_cpm: 2.82
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# HAUS7

*HAUS augmin like complex subunit 7* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.36× (z +9.3, q 8e-18, up in 13 of 17 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.85× (z +4.7, q 3e-04, up in 19 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.198×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (HS-578T 0.0652×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL12]] (+0.71, fdr 1e-05), [[POLR3K]] (+0.69, fdr 2e-05), [[DCTPP1]] (+0.67, fdr 1e-05); moves opposite to [[NKIRAS1]] (-0.59, fdr 5e-05), [[RPL41]] (-0.59, fdr 3e-05), [[HOXB-AS3]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TERT]] → it (grade B ⚠); 2 go from it, the strongest it → [[TREX2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **3.36×** | +9.3 | 8e-18 | 13/17 (PANC-1, SW1417, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.29×** | +8.4 | 8e-15 | 4/5 (PANC-1, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.37×** | +7.1 | 3e-10 | 2/3 (PANC-1, A498) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +4.7 | 3e-04 | 19/44 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.76×** | +4.3 | 0.002 | 2/17 (A-427, HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.69×** | +4.0 | 0.006 | 9/44 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.5 | 0.039 | 0/16 | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 1.51× | +3.1 | 0.12 | 11/42 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.48× | +3.0 | 0.16 | 9/37 (MIA PaCa-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13102.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.198×); [[Valdecoxib (drug)]] 0.5 µM in 1 line (HS-578T 0.0652×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.614× | -3.7 | 0.10 | 8/35 (A498, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.745× | -3.2 | 0.28 | 13/33 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.455× | -3.2 | 0.28 | 8/36 (J82, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 0.752× | -3.1 | 0.28 | 15/45 (A-172, Hs 766T, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.37 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0652× (z -8.5) |
| [[J82 (line)]] | alt | 5.24 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -9.3) |
| [[A-172 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL12]] | +0.71 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[POLR3K]] | +0.69 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[DCTPP1]] | +0.67 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[MIS18A]] | +0.59 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[SLC39A3]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[HMBS]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CNOT10]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TREX2]] | +0.57 | +0.57 / +0.42 | both halves | 4e-05 | STRING 512; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PRIM1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EEFSEC]] | +0.57 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CDT1]] | +0.56 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[PUSL1]] | +0.56 | +0.28 / +0.54 | both halves | 3e-04 |  |
| [[GINS2]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKIRAS1]] | -0.59 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[RPL41]] | -0.59 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[HOXB-AS3]] | -0.58 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[ZNF451-AS1]] | -0.58 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[USF2]] | -0.57 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[LINC00938]] | -0.56 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[CHD3]] | -0.55 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[CSDE1]] | -0.55 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[GNAS]] | -0.55 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[RNF11]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[C12orf73]] | -0.54 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[ZNF821]] | -0.54 | -0.54 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises HAUS7's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without TERT | 0.069 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TREX2]] | C | HAUS7's natural level strengthens TREX2's drug response | HAUS7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.08; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[DAZAP2]] | C | HAUS7's natural level strengthens DAZAP2's drug response | HAUS7's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.13; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.428). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.5, -42.9); signed map (-11.3, -53.4). **Vector** length 42.5, 5.43% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +2.0 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.0 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +1.9 | +4.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +2.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +3.0 |
|  | [[Thymol (drug)]] 5 µM |  | +0.8 | +0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +0.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -3.0 | -3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -1.8 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,447,668-153,495,516 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UIP1; previously UCHL5IP |
| Gene groups (HGNC) | HAUS augmin like complex |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99871](https://www.uniprot.org/uniprotkb/Q99871) (HAUS augmin-like complex subunit 7):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex.

**Summary**, from NCBI Gene [55559](https://www.ncbi.nlm.nih.gov/gene/55559):

> This gene encodes a subunit of the augmin complex, which regulates centrosome and mitotic spindle integrity, and is necessary for the completion of cytokinesis. The encoded protein was identified by interaction with ubiquitin C-terminal hydrolase 37. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:32979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32979) · Entrez [55559](https://www.ncbi.nlm.nih.gov/gene/55559) · UniProt [Q99871](https://www.uniprot.org/uniprotkb/Q99871) · Ensembl [ENSG00000213397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213397)

## Data

Gene col 13102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13102); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13102]; `tensor/DDL_lfc|DDL_z.npy` [13102]; `embed/gene_vectors.npy` [13102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13102 or target_col == 13102). Every well: [[HAUS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
