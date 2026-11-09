---
symbol: "MRPL54"
type: "gene"
col: 11424
ensembl_id: "ENSG00000183617"
name: "mitochondrial ribosomal protein L54"
location: "19p13.3"
module: 24
arm: "+"
pooled_cpm: 3.99
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MRPL54

*mitochondrial ribosomal protein L54* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.23× (z +7.0, q 2e-09, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.492× (z -6.4, q 1e-07, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTRHD1]] (+0.65, fdr 3e-05, ⚠ PTRHD1 in the vector space only through flagged drug-doses), [[SCAND1]] (+0.63, fdr 4e-05), [[CHCHD5]] (+0.62, fdr 2e-04), [[FMC1]] (+0.62, fdr 4e-05); moves opposite to [[IPO5]] (-0.57, fdr 1e-04), [[MACROH2A1]] (-0.57, fdr 8e-05), [[MAPK9]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DNAJC12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.0 | 2e-09 | 2/7 (A498, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +6.2 | 2e-07 | 14/24 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.53×** | +3.9 | 0.022 | 14/26 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.44× | +3.3 | 0.13 | 13/39 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.67× | +3.3 | 0.13 | 4/24 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.44× | +3.2 | 0.15 | 8/30 (SW 900, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.492×** | -6.4 | 1e-07 | 28/47 (MIA PaCa-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.519×** | -5.9 | 1e-06 | 26/47 (NCI-H1792, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.530×** | -5.7 | 2e-06 | 22/44 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.551×** | -5.4 | 1e-05 | 22/47 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -4.5 | 7e-04 | 15/35 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.645×** | -3.9 | 0.008 | 18/39 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.740×** | -3.8 | 0.011 | 20/38 (HT-29, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.455×** | -3.3 | 0.077 | 7/42 (H4, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 12 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTRHD1]] ⚠ | +0.65 | +0.45 / +0.70 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SCAND1]] | +0.63 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[CHCHD5]] | +0.62 | +0.30 / +0.74 | both halves | 2e-04 |  |
| [[FMC1]] | +0.62 | +0.40 / +0.70 | both halves | 4e-05 |  |
| [[NFKBIL1]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[SPOP]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[MRPL57]] | +0.61 | +0.37 / +0.65 | both halves | 8e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 911 |
| [[SMIM26]] ⚠ | +0.61 | +0.38 / +0.69 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KRT10]] ⚠ | +0.60 | +0.36 / +0.65 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IFI27L2]] | +0.59 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[EPC1]] | +0.59 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[NDUFB4]] | +0.58 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[SUGT1P3-1]] | +0.58 | +0.32 / +0.40 | both halves | 1e-04 |  |
| [[DCXR]] | +0.58 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[LAGE3]] | +0.58 | +0.43 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.57 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[MACROH2A1]] | -0.57 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[MAPK9]] | -0.54 | -0.39 / -0.60 | both halves | 6e-05 | STRING 465 |
| [[TTL]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[LAMB1]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[HACD3]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ITPR3]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC12]] | B | DNAJC12 activity lowers MRPL54's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.13× higher at baseline in the lines without DNAJC12 | 0.058 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[HDAC6]] | B | HDAC6 activity raises MRPL54's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.0, -15.8); signed map (-12.3, -4.2). **Vector** length 34.8, 3.33% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +1.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.1 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.0 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | +1.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.7 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,762,682-3,768,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mL54 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q6P161](https://www.uniprot.org/uniprotkb/Q6P161) carries no function annotation.

**Summary**, from NCBI Gene [116541](https://www.ncbi.nlm.nih.gov/gene/116541):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16685) · Entrez [116541](https://www.ncbi.nlm.nih.gov/gene/116541) · UniProt [Q6P161](https://www.uniprot.org/uniprotkb/Q6P161) · Ensembl [ENSG00000183617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183617)

## Data

Gene col 11424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11424); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11424]; `tensor/DDL_lfc|DDL_z.npy` [11424]; `embed/gene_vectors.npy` [11424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11424 or target_col == 11424). Every well: [[MRPL54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
