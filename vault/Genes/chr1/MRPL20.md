---
symbol: "MRPL20"
type: "gene"
col: 14318
ensembl_id: "ENSG00000242485"
name: "mitochondrial ribosomal protein L20"
location: "1p36.33"
module: 7
arm: "+"
pooled_cpm: 26.2
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MRPL20

*mitochondrial ribosomal protein L20* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +9.1, q 7e-17, up in 37 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.50× (z +4.8, q 2e-04, up in 28 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (H4 0.278×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP36]] (+0.76, fdr 7e-06), [[SCO1]] (+0.70, fdr 7e-06), [[MRM2]] (+0.69, fdr 7e-06); moves opposite to [[APLP2]] (-0.61, fdr 1e-05), [[AZIN2]] (-0.57, fdr 1e-05), [[RFX2]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.15×** | +9.1 | 7e-17 | 37/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.98×** | +7.8 | 1e-12 | 29/35 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.69×** | +5.6 | 4e-06 | 30/40 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.8 | 2e-04 | 28/48 (SW480, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.6 | 5e-04 | 32/45 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 7e-04 | 29/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.47×** | +4.4 | 8e-04 | 29/48 (LS 180, A-172, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +3.9 | 0.007 | 25/48 (KATO III, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.94×** | +3.9 | 0.007 | 24/47 (PANC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.36×** | +3.5 | 0.022 | 26/47 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +3.4 | 0.034 | 17/47 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +3.3 | 0.043 | 17/46 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.2 | 0.063 | 20/40 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.20×** | +3.1 | 0.069 | 17/48 (HS-578T, A-427, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.097 | 17/46 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.097 | 14/47 (A-172, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14318.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (H4 0.278×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.760× | -3.3 | 0.65 | 17/48 (A-427, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP36]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[SCO1]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[MRM2]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 | STRING 808 |
| [[DDX28]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | STRING 891 |
| [[RRS1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 | STRING 982 |
| [[NDUFAF4]] | +0.67 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[NOL9]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[CIAPIN1]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[FEM1A]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.64 | +0.72 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLP2]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[AZIN2]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[RFX2]] | -0.56 | -0.67 / -0.39 | both halves | 5e-05 |  |
| [[NPTN]] | -0.56 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[MLF1]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ARL6IP1]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 | STRING 826 |
| [[PHF1]] | -0.55 | -0.64 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.6, 3.1); signed map (-0.4, -43.4). **Vector** length 60.5, 12.1% of its response variance represented; |z| ≥ 3 in 584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,401,909-1,407,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10024, bL20m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BYC9](https://www.uniprot.org/uniprotkb/Q9BYC9) carries no function annotation.

**Summary**, from NCBI Gene [55052](https://www.ncbi.nlm.nih.gov/gene/55052):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14478) · Entrez [55052](https://www.ncbi.nlm.nih.gov/gene/55052) · UniProt [Q9BYC9](https://www.uniprot.org/uniprotkb/Q9BYC9) · Ensembl [ENSG00000242485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242485)

## Data

Gene col 14318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14318); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14318]; `tensor/DDL_lfc|DDL_z.npy` [14318]; `embed/gene_vectors.npy` [14318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14318 or target_col == 14318). Every well: [[MRPL20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
