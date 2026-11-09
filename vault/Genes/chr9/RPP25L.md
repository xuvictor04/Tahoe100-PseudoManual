---
symbol: "RPP25L"
type: "gene"
col: 9044
ensembl_id: "ENSG00000164967"
name: "ribonuclease P/MRP subunit p25 like"
location: "9p13.3"
module: 11
arm: "+"
pooled_cpm: 3.35
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RPP25L

*ribonuclease P/MRP subunit p25 like* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.34× (z +5.3, q 7e-05, up in 27 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.480× (z -4.8, q 0.001, down in 19 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf131]] (+0.82, fdr 7e-06), [[EID2]] (+0.80, fdr 7e-06), [[METTL18]] (+0.78, fdr 7e-06); moves opposite to [[BCAP31]] (-0.70, fdr 7e-06), [[TECR]] (-0.70, fdr 7e-06), [[TM9SF2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Hydroxyurea (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.34×** | +5.3 | 7e-05 | 27/42 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.18×** | +5.0 | 1e-04 | 25/44 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +5.0 | 1e-04 | 0/2 | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.5 | 1e-03 | 11/18 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +4.2 | 0.004 | 8/19 (HT-29, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.56×** | +4.1 | 0.005 | 18/37 (AsPC-1, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.010 | 12/44 (A549, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +3.6 | 0.021 | 9/35 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.40× | +3.1 | 0.13 | 9/34 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.59× | +3.0 | 0.15 | 3/21 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -4.8 | 0.001 | 19/46 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.499×** | -4.5 | 0.002 | 19/43 (NCI-H2030, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -4.2 | 0.004 | 16/30 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.558×** | -3.8 | 0.023 | 19/44 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.564×** | -3.7 | 0.023 | 14/43 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -3.5 | 0.048 | 15/39 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.597×** | -3.3 | 0.068 | 13/39 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.605×** | -3.3 | 0.079 | 19/42 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 5.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0441× (z -9.0) |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.998 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf131]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[EID2]] | +0.80 | +0.75 / +0.83 | both halves | 7e-06 |  |
| [[METTL18]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[PPCS]] | +0.78 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[RPP38]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 | STRING 976 |
| [[PBDC1]] | +0.76 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[SDSL]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PEX12]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[FDX2]] | +0.74 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[MPLKIP]] | +0.74 | +0.72 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.70 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[TECR]] | -0.70 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[TM9SF2]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.68 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[TBCD]] | -0.66 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.66 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[TCF3]] | -0.65 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[RPA1]] | -0.65 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[INTS1]] | -0.64 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[PRKCSH]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[COL18A1]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | RPP25L's natural level lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | RPP25L's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.405 over the table, 0.089 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.861). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.2, 5.2); signed map (2.2, -19.0). **Vector** length 57.1, 9.54% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.4 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease P/MRP subunit p25 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,610,486-34,612,104 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA296L22.5, MGC29635; previously C9orf23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5L8](https://www.uniprot.org/uniprotkb/Q8N5L8) (Ribonuclease P protein subunit p25-like protein):

> May be a component of ribonuclease P or MRP.

**Summary**, from NCBI Gene [138716](https://www.ncbi.nlm.nih.gov/gene/138716):

> This gene encodes a protein that appears to belong to a family of evolutionarily related proteins (DUF78), that may share one or more domains in common. Members of this family are small archaebacterial proteins with no known function. Alternative splicing has been observed at this locus and two variants, both encoding the same protein, have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19909) · Entrez [138716](https://www.ncbi.nlm.nih.gov/gene/138716) · UniProt [Q8N5L8](https://www.uniprot.org/uniprotkb/Q8N5L8) · Ensembl [ENSG00000164967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164967)

## Data

Gene col 9044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9044); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9044]; `tensor/DDL_lfc|DDL_z.npy` [9044]; `embed/gene_vectors.npy` [9044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9044 or target_col == 9044). Every well: [[RPP25L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPP25L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
