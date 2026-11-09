---
symbol: "MRPL24"
type: "gene"
col: 6709
ensembl_id: "ENSG00000143314"
name: "mitochondrial ribosomal protein L24"
location: "1q23.1"
module: 4
arm: "+"
pooled_cpm: 15.57
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MRPL24

*mitochondrial ribosomal protein L24* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.25× (z +11.4, q 3e-27, up in 24 of 26 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 7.34×, A549 10.0×, PANC-1 4.48×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 5.11×, KATO III 5.89×, PANC-1 3.98×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.639× (z -5.4, q 4e-05, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFRD2]] (+0.69, fdr 7e-06), [[TSEN2]] (+0.69, fdr 1e-05), [[ATIC]] (+0.68, fdr 1e-05); moves opposite to [[GNAS]] (-0.62, fdr 1e-05), [[SHOX2]] (-0.56, fdr 5e-05), [[MTCH1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 7.34×, A549 10.0×, PANC-1 4.48×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 5.11×, KATO III 5.89×, PANC-1 3.98×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.25×** | +11.4 | 3e-27 | 24/26 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.56×** | +10.8 | 8e-25 | 38/39 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +8.3 | 3e-14 | 29/34 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +5.3 | 1e-05 | 25/48 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.78×** | +4.9 | 1e-04 | 30/42 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.35×** | +3.6 | 0.034 | 22/48 (NCI-H23, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6709.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -5.4 | 4e-05 | 27/46 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -4.4 | 0.003 | 25/47 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -4.0 | 0.014 | 20/46 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -3.7 | 0.036 | 20/46 (SHP-77, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.653×** | -3.4 | 0.086 | 18/45 (H4, RKO, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.465× | -3.0 | 0.23 | 15/44 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.5) |
| [[A-427 (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.1) |
| [[A498 (line)]] | wt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.11× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +9.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.89× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -8.7) |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -9.9) |
| [[A-172 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFRD2]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 | STRING 471 |
| [[TSEN2]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ATIC]] | +0.68 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[MRPL12]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[CLYBL]] | +0.66 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DDX10]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[FARSB]] | +0.65 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[SLX4IP]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NAA15]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CMSS1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SERBP1]] | +0.64 | +0.69 / +0.49 | both halves | 1e-05 | STRING 603 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.62 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SHOX2]] | -0.56 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MTCH1]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-16.0, -41.7); signed map (-6.7, -47.2). **Vector** length 52.8, 10.8% of its response variance represented; |z| ≥ 3 in 586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.7 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.2 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -0.8 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,737,303-156,741,590 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-L18, uL24m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q96A35](https://www.uniprot.org/uniprotkb/Q96A35) carries no function annotation.

**Summary**, from NCBI Gene [79590](https://www.ncbi.nlm.nih.gov/gene/79590):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14037) · Entrez [79590](https://www.ncbi.nlm.nih.gov/gene/79590) · UniProt [Q96A35](https://www.uniprot.org/uniprotkb/Q96A35) · Ensembl [ENSG00000143314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143314)

## Data

Gene col 6709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6709); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6709]; `tensor/DDL_lfc|DDL_z.npy` [6709]; `embed/gene_vectors.npy` [6709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6709 or target_col == 6709). Every well: [[MRPL24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
