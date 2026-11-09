---
symbol: "UQCR10"
type: "gene"
col: 11489
ensembl_id: "ENSG00000184076"
name: "ubiquinol-cytochrome c reductase, complex III subunit X"
location: "22q12.2"
module: 48
arm: "+"
pooled_cpm: 29.37
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# UQCR10

*ubiquinol-cytochrome c reductase, complex III subunit X* — 22q12.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.45× (z +5.8, q 4e-06, up in 30 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.177×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHCHD1]] (+0.84, fdr 7e-06), [[ATP5MF]] (+0.79, fdr 7e-06), [[ROMO1]] (+0.79, fdr 7e-06); moves opposite to [[ATN1]] (-0.60, fdr 1e-04), [[CROCC]] (-0.58, fdr 4e-04), [[U2AF2]] (-0.58, fdr 7e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.45×** | +5.8 | 4e-06 | 30/36 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.81×** | +5.7 | 4e-06 | 38/43 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **2.07×** | +4.9 | 2e-04 | 36/46 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.3 | 0.002 | 39/45 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | 1.66× | +3.2 | 0.18 | 23/38 (J82, CFPAC-1, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11489.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.696× | -3.4 | 0.32 | 27/47 (A-427, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | 0.395× | -3.2 | 0.32 | 40/48 (SHP-77, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.414× | -3.1 | 0.32 | 32/46 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.8) |
| [[A-172 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 22 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD1]] | +0.84 | +0.66 / +0.90 | both halves | 7e-06 | STRING 489 |
| [[ATP5MF]] | +0.79 | +0.68 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 909 |
| [[ROMO1]] | +0.79 | +0.68 / +0.80 | both halves | 7e-06 | STRING 759 |
| [[POLR2J]] ⚠ | +0.78 | +0.65 / +0.76 | both halves | 7e-06 | STRING 482; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFC2]] | +0.77 | +0.65 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 975 |
| [[UQCRQ]] ⚠ | +0.77 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | +0.76 | +0.62 / +0.83 | both halves | 7e-06 |  |
| [[NDUFB11]] ⚠ | +0.75 | +0.70 / +0.76 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 974; ⚠ in the vector space only through flagged drug-doses |
| [[KRT10]] ⚠ | +0.75 | +0.57 / +0.80 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | +0.75 | +0.45 / +0.77 | both halves | 3e-05 |  |
| [[UQCR11]] | +0.74 | +0.63 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999 |
| [[LAMTOR5]] | +0.74 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[ELOB]] | +0.74 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.73 | +0.56 / +0.78 | both halves | 1e-05 | STRING 634 |
| [[ATP5MJ]] | +0.73 | +0.59 / +0.74 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 626 |
| [[KRTCAP2]] | +0.72 | +0.45 / +0.79 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATN1]] | -0.60 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[CROCC]] | -0.58 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[U2AF2]] | -0.58 | -0.20 / -0.64 | both halves | 7e-04 |  |
| [[NPEPL1]] | -0.58 | -0.34 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.4, -19.0); signed map (-33.5, 8.3). **Vector** length 59.2, 18.1% of its response variance represented; |z| ≥ 3 in 407 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex IV assembly* (reactome, mean cos +0.62 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.67 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.64 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | -0.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +0.8 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.8 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -5.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -4.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -4.4 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase, complex III subunit X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,767,369-29,770,413 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC051, UCRC, QCR9, UCCR7.2 |
| Gene groups (HGNC) | Mitochondrial complex III: ubiquinol-cytochrome c reductase complex subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UDW1](https://www.uniprot.org/uniprotkb/Q9UDW1) (Cytochrome b-c1 complex subunit 9):

> Component of the ubiquinol-cytochrome c oxidoreductase, a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular …

**Summary**, from NCBI Gene [29796](https://www.ncbi.nlm.nih.gov/gene/29796):

> UCRC is a subunit of mitochondrial complex III (ubiquinol-cytochrome c reductase; EC 1.10.2.2), which forms the middle segment of the respiratory chain of the inner mitochondrial membrane (Schagger et al., 1995 [PubMed 8592474]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30863) · Entrez [29796](https://www.ncbi.nlm.nih.gov/gene/29796) · UniProt [Q9UDW1](https://www.uniprot.org/uniprotkb/Q9UDW1) · Ensembl [ENSG00000184076](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184076)

## Data

Gene col 11489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11489); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11489]; `tensor/DDL_lfc|DDL_z.npy` [11489]; `embed/gene_vectors.npy` [11489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11489 or target_col == 11489). Every well: [[UQCR10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UQCR10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
