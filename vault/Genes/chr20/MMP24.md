---
symbol: "MMP24"
type: "gene"
col: 4698
ensembl_id: "ENSG00000125966"
name: "matrix metallopeptidase 24"
location: "20q11.22"
module: 21
arm: "+"
pooled_cpm: 6.13
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MMP24

*matrix metallopeptidase 24* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.93× (z +11.4, q 1e-27, up in 9 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +7.7, q 3e-12, up in 22 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 5 µM in 1 line (HEC-1-A 0.0871×); [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (KATO III 0.0592×); [[Ciclopirox (drug)]] 5 µM in 1 line (HCT15 0.0934×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZRANB2-AS1]] (+0.72, fdr 1e-05), [[SFRP4]] (+0.71, fdr 7e-06), [[MAL2-AS1]] (+0.70, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +11.4 | 1e-27 | 9/10 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +10.9 | 3e-25 | 21/28 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.7 | 3e-12 | 22/39 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +7.6 | 5e-12 | 10/16 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.6 | 3e-06 | 22/46 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +5.1 | 4e-05 | 16/42 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.9 | 7e-05 | 10/31 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.9 | 7e-05 | 12/37 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 1e-04 | 16/43 (A-172, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.063 | 13/44 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.70× | +3.1 | 0.11 | 4/22 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.11 | 5/45 (C32, Hs 766T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4698.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 5 µM in 1 line (HEC-1-A 0.0871×); [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (KATO III 0.0592×); [[Ciclopirox (drug)]] 5 µM in 1 line (HCT15 0.0934×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.848× | -6.3 | 1e-07 | 22/48 (CHP-212, SW48, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 5 µM |  | 0.742× | -3.2 | 0.30 | 11/43 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.743× | -3.2 | 0.30 | 10/43 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.750× | -3.0 | 0.38 | 6/45 (LoVo, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 12.1 | 0 | 2 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.123× (z -9.5) |
| [[A498 (line)]] | wt | 8.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 6.45 | 0 | 1 | — | [[Ciclopirox (drug)]] 5 µM 0.0934× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 4.53 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0871× (z -10.5) |
| [[Hs 766T (line)]] | wt | 4.17 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0590× (z -9.4) |
| [[KATO III (line)]] | alt | 5.21 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0592× (z -10.4) |
| [[A-172 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZRANB2-AS1]] | +0.72 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[SFRP4]] | +0.71 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.70 | +0.47 / +0.79 | both halves | 2e-05 |  |
| [[FAM217A]] | +0.70 | +0.42 / +0.74 | both halves | 4e-05 |  |
| [[PKD2L2]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[TICAM2-AS1]] | +0.67 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[SPATA21]] | +0.67 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[CHMP3-AS1]] | +0.67 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[ABHD15-AS1]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[DSG2-AS1]] | +0.66 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[TTC36-AS1]] | +0.66 | +0.46 / +0.74 | both halves | 3e-05 |  |
| [[BIRC6-AS2-1]] | +0.66 | +0.45 / +0.72 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers MMP24's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, 28.5); signed map (34.1, 6.8). **Vector** length 45.3, 4.94% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -6.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,226,690-35,276,998 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MT5-MMP |
| Gene groups (HGNC) | M10 matrix metallopeptidases |
| Reactome | 3 pathways, smallest: Activation of Matrix Metalloproteinases; Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5R2](https://www.uniprot.org/uniprotkb/Q9Y5R2) (Matrix metalloproteinase-24):

> Metalloprotease that mediates cleavage of N-cadherin (CDH2) and acts as a regulator of neuro-immune interactions and neural stem cell quiescence. Involved in cell-cell interactions between nociceptive neurites and mast cells, possibly by mediating cleavage of CDH2, thereby acting as a mediator of peripheral thermal nociception and inflammatory hyperalgesia. Key regulator of neural stem cells quiescence by mediating cleavage of CDH2, affecting CDH2-mediated anchorage of neural stem cells to …

**Summary**, from NCBI Gene [10893](https://www.ncbi.nlm.nih.gov/gene/10893):

> This gene encodes a member of the peptidase M10 family of matrix metalloproteinases (MMPs). Proteins in this family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. The encoded preproprotein is proteolytically processed to generate the mature protease. Unlike most MMPs, which are secreted, this protease is a member of the …

**Accessions** — [HGNC:7172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7172) · Entrez [10893](https://www.ncbi.nlm.nih.gov/gene/10893) · UniProt [Q9Y5R2](https://www.uniprot.org/uniprotkb/Q9Y5R2) · Ensembl [ENSG00000125966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125966)

## Data

Gene col 4698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4698); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4698]; `tensor/DDL_lfc|DDL_z.npy` [4698]; `embed/gene_vectors.npy` [4698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4698 or target_col == 4698). Every well: [[MMP24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
