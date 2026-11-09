---
symbol: "MRPS23"
type: "gene"
col: 11199
ensembl_id: "ENSG00000181610"
name: "mitochondrial ribosomal protein S23"
location: "17q22"
module: 33
arm: "+"
pooled_cpm: 16.54
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MRPS23

*mitochondrial ribosomal protein S23* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.37× (z +10.9, q 6e-25, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.75× (z +7.1, q 1e-10, up in 34 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS26]] (+0.73, fdr 7e-06), [[WDR3]] (+0.72, fdr 7e-06), [[NUDCD3]] (+0.71, fdr 7e-06); moves opposite to [[GNAS]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.37×** | +10.9 | 6e-25 | 46/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +10.3 | 2e-22 | 37/45 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.17×** | +9.8 | 2e-20 | 43/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.99×** | +8.7 | 4e-16 | 38/47 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +7.1 | 1e-10 | 34/47 (HOP62, A-427, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.71×** | +6.8 | 1e-09 | 25/41 (LoVo, NCI-H1792, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +5.9 | 2e-07 | 31/47 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.3 | 7e-06 | 34/46 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.3 | 9e-06 | 25/46 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.45×** | +4.7 | 2e-04 | 21/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +4.5 | 3e-04 | 20/45 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.5 | 3e-04 | 23/47 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.29×** | +4.5 | 3e-04 | 22/47 (NCI-H1792, Panc 03.27, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 19/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.3 | 5e-04 | 21/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +4.3 | 7e-04 | 19/47 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +4.1 | 0.001 | 21/48 (KATO III, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.014 | 20/47 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.69×** | +3.5 | 0.015 | 14/47 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.026 | 15/48 (A549, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.63×** | +3.2 | 0.029 | 12/44 (SK-MEL-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.030 | 11/47 (HOP62, A-427, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.56×** | +2.9 | 0.064 | 4/46 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.763× | -3.5 | 0.16 | 12/47 (SW 1271, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.764× | -3.4 | 0.16 | 18/46 (H4, RKO, …) | rises with dose | low cells (technical?); position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.782× | -3.0 | 0.46 | 12/47 (RKO, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 9.87 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS26]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 987 |
| [[WDR3]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[NUDCD3]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CTU1]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GEMIN6]] | +0.70 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[SCO1]] | +0.70 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[ZNF74]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[POLR3A]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NKRF]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-44.6, -8.8); signed map (-16.1, -22.3). **Vector** length 67.3, 12.8% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.53 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +10.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | +0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.0 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:57,834,781-57,850,056 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S23, CGI-138, HSPC329, mS23 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y3D9](https://www.uniprot.org/uniprotkb/Q9Y3D9) carries no function annotation.

**Summary**, from NCBI Gene [51649](https://www.ncbi.nlm.nih.gov/gene/51649):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14509) · Entrez [51649](https://www.ncbi.nlm.nih.gov/gene/51649) · UniProt [Q9Y3D9](https://www.uniprot.org/uniprotkb/Q9Y3D9) · Ensembl [ENSG00000181610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181610)

## Data

Gene col 11199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11199); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11199]; `tensor/DDL_lfc|DDL_z.npy` [11199]; `embed/gene_vectors.npy` [11199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11199 or target_col == 11199). Every well: [[MRPS23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
