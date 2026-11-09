---
symbol: "KRTCAP2"
type: "gene"
col: 8693
ensembl_id: "ENSG00000163463"
name: "keratinocyte associated protein 2"
location: "1q22"
module: 24
arm: "+"
pooled_cpm: 27.5
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# KRTCAP2

*keratinocyte associated protein 2* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +5.5, q 3e-05, up in 38 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.273× (z -4.0, q 0.025, down in 40 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.0603×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2J]] (+0.76, fdr 1e-05, ⚠ POLR2J in the vector space only through flagged drug-doses), [[SMIM26]] (+0.76, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MED19]] (+0.75, fdr 1e-05), [[NKAP]] (+0.75, fdr 7e-06), [[LAMTOR5]] (+0.72, fdr 2e-05); moves opposite to [[RPSA]] (-0.67, fdr 1e-05), [[HNRNPA3]] (-0.65, fdr 1e-05), [[YWHAQ]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.65×** | +5.5 | 3e-05 | 38/43 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.22×** | +4.7 | 9e-04 | 28/34 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.97×** | +4.1 | 0.007 | 33/45 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8693.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.0603×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.273×** | -4.0 | 0.025 | 40/45 (A-427, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.283×** | -3.9 | 0.025 | 37/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.331× | -3.4 | 0.12 | 35/46 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 19.7 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0603× (z -9.0) |
| [[A-172 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 19 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J]] ⚠ | +0.76 | +0.52 / +0.84 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMIM26]] ⚠ | +0.76 | +0.56 / +0.81 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MED19]] | +0.75 | +0.57 / +0.80 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | +0.75 | +0.67 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | +0.75 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[UQCR10]] ⚠ | +0.72 | +0.45 / +0.79 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | +0.72 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[TMEM258]] | +0.72 | +0.59 / +0.77 | both halves | 7e-06 | same gene group; STRING 971 |
| [[RPL36AL]] ⚠ | +0.71 | +0.53 / +0.75 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | +0.70 | +0.47 / +0.80 | both halves | 2e-05 |  |
| [[GADD45GIP1]] | +0.70 | +0.26 / +0.84 | both halves | 4e-04 |  |
| [[COX5A]] ⚠ | +0.70 | +0.58 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | +0.70 | +0.43 / +0.74 | both halves | 4e-05 |  |
| [[INAFM1]] | +0.70 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[YIF1A]] | +0.70 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.69 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[TMEM205]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.69 | +0.59 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | -0.67 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.65 | -0.51 / -0.71 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.65 | -0.66 / -0.70 | both halves | 7e-06 |  |
| [[DHFR]] | -0.64 | -0.29 / -0.74 | both halves | 2e-04 |  |
| [[U2AF2]] | -0.63 | -0.37 / -0.68 | both halves | 9e-05 |  |
| [[LY6G5B]] | -0.63 | -0.28 / -0.64 | both halves | 3e-04 |  |
| [[TMX3]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.61 | -0.30 / -0.71 | both halves | 2e-04 |  |
| [[IPO5]] | -0.61 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[MAT2A]] | -0.60 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.60 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[NAA50]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.9, -15.6); signed map (-12.7, -2.3). **Vector** length 61.8, 19.5% of its response variance represented; |z| ≥ 3 in 416 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +0.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.3 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -4.0 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | keratinocyte associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,169,408-155,173,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCP2 |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6L1](https://www.uniprot.org/uniprotkb/Q8N6L1) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit KCP2):

> Subunit of STT3A-containing oligosaccharyl transferase (OST-A) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates …

**Summary**, from NCBI Gene [200185](https://www.ncbi.nlm.nih.gov/gene/200185):

> Enables enzyme activator activity and protein-macromolecule adaptor activity. Involved in protein N-linked glycosylation. Located in endoplasmic reticulum membrane. Part of oligosaccharyltransferase complex A. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28942) · Entrez [200185](https://www.ncbi.nlm.nih.gov/gene/200185) · UniProt [Q8N6L1](https://www.uniprot.org/uniprotkb/Q8N6L1) · Ensembl [ENSG00000163463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163463)

## Data

Gene col 8693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8693); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8693]; `tensor/DDL_lfc|DDL_z.npy` [8693]; `embed/gene_vectors.npy` [8693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8693 or target_col == 8693). Every well: [[KRTCAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRTCAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
