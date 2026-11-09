---
symbol: "NDUFB4"
type: "gene"
col: 790
ensembl_id: "ENSG00000065518"
name: "NADH:ubiquinone oxidoreductase subunit B4"
location: "3q13.33"
module: 24
arm: "+"
pooled_cpm: 51.59
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NDUFB4

*NADH:ubiquinone oxidoreductase subunit B4* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.91× (z +5.2, q 1e-04, up in 43 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.622× (z -3.9, q 0.047, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.364×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.77, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MRPS18C]] (+0.76, fdr 2e-05), [[IFI27L2]] (+0.73, fdr 1e-05), [[CHCHD1]] (+0.73, fdr 2e-05); moves opposite to [[IPO5]] (-0.67, fdr 3e-05), [[EIF4G1]] (-0.66, fdr 1e-05), [[MAPRE1]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF737]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +5.2 | 1e-04 | 43/47 (NCI-H2030, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.74×** | +4.7 | 9e-04 | 36/47 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +4.5 | 0.001 | 37/48 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.46× | +3.2 | 0.21 | 32/47 (LoVo, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.49× | +3.1 | 0.22 | 25/44 (A-427, A549, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 790.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.364×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.622×** | -3.9 | 0.047 | 38/48 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.673× | -3.3 | 0.29 | 27/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.480× | -3.1 | 0.35 | 31/49 (NCI-H460, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 0.694× | -3.0 | 0.35 | 26/48 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 97.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -8.7) |
| [[A-172 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 15 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.77 | +0.55 / +0.84 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | +0.76 | +0.48 / +0.83 | both halves | 2e-05 | STRING 506 |
| [[IFI27L2]] | +0.73 | +0.51 / +0.80 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.73 | +0.46 / +0.79 | both halves | 2e-05 | STRING 551 |
| [[RBIS]] | +0.71 | +0.51 / +0.83 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.71 | +0.48 / +0.80 | both halves | 2e-05 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY |
| [[CHCHD5]] | +0.71 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[MRPL32]] | +0.69 | +0.39 / +0.79 | both halves | 5e-05 |  |
| [[ZFAND2A-DT]] | +0.68 | +0.39 / +0.73 | both halves | 5e-05 |  |
| [[ATP5MJ]] | +0.67 | +0.50 / +0.83 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 400 |
| [[WDR83OS]] ⚠ | +0.67 | +0.57 / +0.69 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[KRT10]] ⚠ | +0.67 | +0.38 / +0.81 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CWC15]] | +0.67 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[ATP5MC2]] | +0.67 | +0.47 / +0.73 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 508 |
| [[TMEM126A]] | +0.67 | +0.48 / +0.68 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.67 | -0.45 / -0.71 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.66 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.64 | -0.43 / -0.72 | both halves | 3e-05 |  |
| [[GSPT1]] | -0.64 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[PSME3]] | -0.64 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[FAM120A]] | -0.63 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[MCM7]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[WDR1]] | -0.61 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[NUP188]] | -0.61 | -0.39 / -0.68 | both halves | 5e-05 |  |
| [[ARHGAP4]] | -0.60 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[FGD5-AS1]] | -0.60 | -0.47 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF737]] | B | ZNF737 activity raises NDUFB4's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 1.17× lower at baseline in the lines without ZNF737 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90 |
| [[ESRP2]] | B | ESRP2 activity raises NDUFB4's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.16× lower at baseline in the lines without ESRP2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.4, -15.7); signed map (-13.7, -4.3). **Vector** length 69.2, 23.2% of its response variance represented; |z| ≥ 3 in 423 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.9 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:120,596,328-120,602,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B15 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95168](https://www.uniprot.org/uniprotkb/O95168) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4710](https://www.ncbi.nlm.nih.gov/gene/4710):

> This gene encodes a non-catalytic subunit of the multisubunit NADH:ubiquinone oxidoreductase, the first enzyme complex in the mitochondrial electron transport chain (complex I). Mammalian complex I is composed of 45 different subunits and transfers electrons from NADH to ubiquinone. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:7699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7699) · Entrez [4710](https://www.ncbi.nlm.nih.gov/gene/4710) · UniProt [O95168](https://www.uniprot.org/uniprotkb/O95168) · Ensembl [ENSG00000065518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065518)

## Data

Gene col 790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 790); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 790]; `tensor/DDL_lfc|DDL_z.npy` [790]; `embed/gene_vectors.npy` [790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 790 or target_col == 790). Every well: [[NDUFB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
