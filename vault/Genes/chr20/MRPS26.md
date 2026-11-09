---
symbol: "MRPS26"
type: "gene"
col: 4691
ensembl_id: "ENSG00000125901"
name: "mitochondrial ribosomal protein S26"
location: "20p13"
module: 54
arm: "+"
pooled_cpm: 12.39
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MRPS26

*mitochondrial ribosomal protein S26* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.32× (z +6.0, q 1e-06, up in 34 of 41 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.357× (z -8.2, q 9e-14, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PET117]] (+0.80, fdr 1e-05), [[ZNF74]] (+0.80, fdr 7e-06), [[MRPS34]] (+0.77, fdr 7e-06); moves opposite to [[NID1]] (-0.64, fdr 1e-04), [[PRKAR1A]] (-0.63, fdr 3e-05), [[RAB1B]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C2orf27A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +6.0 | 1e-06 | 34/41 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.62×** | +3.8 | 0.035 | 24/41 (SW 900, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.32× | +3.1 | 0.33 | 18/48 (NCI-H460, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.357×** | -8.2 | 9e-14 | 41/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.565×** | -6.5 | 3e-08 | 32/45 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -5.3 | 2e-05 | 28/47 (SNU-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.582×** | -4.3 | 0.002 | 28/46 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -4.1 | 0.005 | 24/46 (HCT15, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -12.1) |
| [[A498 (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -8.8) |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0651× (z -13.3) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0524× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.33 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -8.7) |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0856× (z -9.5) |
| [[SNU-423 (line)]] | alt | 8.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -10.1) |
| [[SW48 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0969× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 18.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -8.8) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PET117]] | +0.80 | +0.56 / +0.81 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.80 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[MRPS34]] | +0.77 | +0.65 / +0.79 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 998 |
| [[POP7]] | +0.74 | +0.45 / +0.81 | both halves | 3e-05 |  |
| [[MRPS23]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 987 |
| [[GEMIN6]] | +0.70 | +0.49 / +0.76 | both halves | 2e-05 |  |
| [[RPP21]] | +0.70 | +0.42 / +0.76 | both halves | 4e-05 |  |
| [[SAC3D1]] | +0.70 | +0.41 / +0.80 | both halves | 4e-05 |  |
| [[MPHOSPH10]] | +0.70 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.69 | +0.41 / +0.80 | both halves | 4e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 869 |
| [[C1orf35]] | +0.69 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[RPP40]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NID1]] | -0.64 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[PRKAR1A]] | -0.63 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[RAB1B]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TPP1]] | -0.60 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[WSB2]] | -0.58 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TUG1]] | -0.57 | -0.24 / -0.63 | both halves | 4e-04 |  |
| [[LEPROT]] | -0.57 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[LINC00641]] | -0.57 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[ENSA]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf27A]] | B | C2orf27A activity raises MRPS26's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.60× lower at baseline in the lines without C2orf27A | 0.078 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.8, -9.0); signed map (-20.2, -7.7). **Vector** length 74.3, 17.9% of its response variance represented; |z| ≥ 3 in 567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -1.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,046,052-3,048,250 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S13, MRP-S26, RPMS13, dJ534B8.3, mS26; previously C20orf193 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BYN8](https://www.uniprot.org/uniprotkb/Q9BYN8) carries no function annotation.

**Summary**, from NCBI Gene [64949](https://www.ncbi.nlm.nih.gov/gene/64949):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14045) · Entrez [64949](https://www.ncbi.nlm.nih.gov/gene/64949) · UniProt [Q9BYN8](https://www.uniprot.org/uniprotkb/Q9BYN8) · Ensembl [ENSG00000125901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125901)

## Data

Gene col 4691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4691); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4691]; `tensor/DDL_lfc|DDL_z.npy` [4691]; `embed/gene_vectors.npy` [4691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4691 or target_col == 4691). Every well: [[MRPS26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
