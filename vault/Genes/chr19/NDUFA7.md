---
symbol: "NDUFA7"
type: "gene"
col: 15579
ensembl_id: "ENSG00000267855"
name: "NADH:ubiquinone oxidoreductase subunit A7"
location: "19p13.2"
module: 24
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NDUFA7

*NADH:ubiquinone oxidoreductase subunit A7* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.35× (z +7.6, q 2e-11, up in 18 of 21 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +4.6, q 5e-04, up in 15 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAGE3]] (+0.70, fdr 8e-05), [[COX5B]] (+0.70, fdr 4e-05), [[MTLN]] (+0.69, fdr 4e-05, ⚠ MTLN in the vector space only through flagged drug-doses), [[TRIM7-AS2]] (+0.68, fdr 7e-05); moves opposite to [[MTA1]] (-0.65, fdr 1e-05), [[CERS2]] (-0.63, fdr 3e-05), [[WASH8P]] (-0.63, fdr 1e-05, ⚠ WASH8P in the vector space only through flagged drug-doses), [[SFPQ]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.35×** | +7.6 | 2e-11 | 18/21 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.20×** | +7.1 | 3e-10 | 3/4 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.35×** | +5.4 | 1e-05 | 8/16 (NCI-H23, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.30×** | +4.9 | 1e-04 | 4/5 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.6 | 5e-04 | 15/33 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.567× | -3.6 | 0.12 | 22/46 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.574× | -3.5 | 0.12 | 21/43 (Panc 03.27, NCI-H2030, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 0.603× | -3.2 | 0.25 | 14/45 (NCI-H2347, SW1417, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.616× | -3.0 | 0.33 | 13/39 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 28 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAGE3]] | +0.70 | +0.37 / +0.74 | both halves | 8e-05 |  |
| [[COX5B]] | +0.70 | +0.41 / +0.73 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 982 |
| [[MTLN]] ⚠ | +0.69 | +0.42 / +0.75 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CHCHD1]] | +0.68 | +0.20 / +0.78 | ⚠ one half (not replicated) | 8e-04 | STRING 532 |
| [[POLR2J]] ⚠ | +0.68 | +0.23 / +0.78 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TRIM7-AS2]] | +0.68 | +0.38 / +0.77 | both halves | 7e-05 |  |
| [[OCEL1]] | +0.67 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[NDUFA2]] | +0.67 | +0.32 / +0.71 | both halves | 2e-04 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[DDT]] | +0.67 | +0.34 / +0.73 | both halves | 1e-04 |  |
| [[SMIM27]] | +0.66 | +0.36 / +0.78 | both halves | 9e-05 |  |
| [[IFI27L2]] | +0.66 | +0.40 / +0.68 | both halves | 5e-05 |  |
| [[C16orf91]] | +0.66 | +0.27 / +0.71 | both halves | 3e-04 |  |
| [[NUDT8]] | +0.66 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[RNF181]] | +0.65 | +0.27 / +0.70 | both halves | 3e-04 |  |
| [[MPLKIP]] | +0.64 | +0.35 / +0.77 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTA1]] | -0.65 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[CERS2]] | -0.63 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[WASH8P]] ⚠ | -0.63 | -0.52 / -0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SFPQ]] | -0.62 | -0.29 / -0.64 | both halves | 3e-04 |  |
| [[U2AF2]] | -0.62 | -0.32 / -0.67 | both halves | 2e-04 |  |
| [[SRSF1]] | -0.60 | -0.22 / -0.64 | both halves | 6e-04 |  |
| [[LENG8]] | -0.59 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[DBN1]] | -0.59 | -0.37 / -0.66 | both halves | 8e-05 |  |
| [[DHFR]] | -0.58 | +0.02 / -0.72 | ⚠ one half (not replicated) | 1.00 |  |
| [[EWSR1]] | -0.58 | -0.22 / -0.64 | both halves | 6e-04 |  |
| [[WASH9P]] | -0.57 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[DAZAP1]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[LY6G5B]] | -0.57 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[KLC2]] | -0.56 | -0.37 / -0.63 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.0, -17.1); signed map (-31.7, 7.5). **Vector** length 40.2, 5.23% of its response variance represented; |z| ≥ 3 in 659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +2.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Bendamustine (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +0.8 | +1.8 |
|  | [[Decitabine (drug)]] 0.5 µM |  | +0.8 | +1.9 |
|  | [[Silodosin (drug)]] 5 µM |  | +0.7 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.0 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -1.8 | +7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,308,768-8,321,375 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B14.5a |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95182](https://www.uniprot.org/uniprotkb/O95182) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4701](https://www.ncbi.nlm.nih.gov/gene/4701):

> This gene encodes a subunit of NADH:ubiquinone oxidoreductase (complex I), which is a multiprotein complex located in the inner mitochondrial membrane. Complex I functions in the transfer of electrons from NADH to the respiratory chain. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:7691](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7691) · Entrez [4701](https://www.ncbi.nlm.nih.gov/gene/4701) · UniProt [O95182](https://www.uniprot.org/uniprotkb/O95182) · Ensembl [ENSG00000267855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267855)

## Data

Gene col 15579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15579); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15579]; `tensor/DDL_lfc|DDL_z.npy` [15579]; `embed/gene_vectors.npy` [15579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15579 or target_col == 15579). Every well: [[NDUFA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
